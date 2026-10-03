#!/usr/bin/env bash
# explainerloop.sh — unattended expanded skill-explainer rebuild loop.
#
# The skill explainers can describe any SKILL.md, but the old cut was often too
# generic. This loop reruns build_skill_explainers.py with --force-sheet so each
# reel gets the expanded source-detail treatment: capabilities, constraints,
# referenced files, code/tool signals, and a dedicated B04 detail beat.
#
#   ./explainerloop.sh                 rebuild every eligible skill explainer
#   ./explainerloop.sh --once          rebuild one explainer, then exit
#   ./explainerloop.sh --n N           rebuild N explainers, then exit
#   ./explainerloop.sh --dry           print the queue, invoke nothing
#   ./explainerloop.sh --start N       start at SKILL-EXPLAINERS row N
#   ./explainerloop.sh --end N         stop at SKILL-EXPLAINERS row N
#   ./explainerloop.sh --redo          rebuild rows already marked done in this loop
#   ./explainerloop.sh --forever       keep rescanning for newly eligible rows
#   ./explainerloop.sh --no-halt       do not halt after consecutive failures
#
# This loop renders. It rewrites beat_sheet.json with a timestamped backup,
# regenerates Kokoro audio, rerenders Remotion clips, and compiles a review cut.
# It does not publish or upload anything.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE="$HERE/.explainerloop"
QUEUE="$STATE/queue.json"
LOG="$STATE/explainerloop.log"
LOCK="$STATE/queue.lock"
BUILDER="${EXPLAINERLOOP_BUILDER:-$HERE/build_skill_explainers.py}"
BATCH_LOG="${EXPLAINERLOOP_BATCH_LOG:-$HERE/SKILL-EXPLAINERS-BATCH-LOG.md}"
PYTHON="${PYTHON:-python3}"
N=0; DRY=0; REDO=0; FOREVER=0; NOHALT=0; START=1; END=9999
MAX_ATTEMPTS="${EXPLAINERLOOP_MAX_ATTEMPTS:-2}"
CONSEC_FAIL_STOP="${EXPLAINERLOOP_CONSEC_FAIL_STOP:-3}"
COOLDOWN="${EXPLAINERLOOP_COOLDOWN:-20}"
WORKER="${EXPLAINERLOOP_WORKER:-$$}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --once)    N=1; shift ;;
    --n)       shift
               [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--n requires an integer >= 1" >&2; exit 2; }
               N="$1"; shift ;;
    --dry)     DRY=1; shift ;;
    --redo)    REDO=1; shift ;;
    --forever) FOREVER=1; shift ;;
    --no-halt) NOHALT=1; shift ;;
    --start)   shift
               [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--start requires an integer >= 1" >&2; exit 2; }
               START="$1"; shift ;;
    --end)     shift
               [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--end requires an integer >= 1" >&2; exit 2; }
               END="$1"; shift ;;
    -h|--help) awk 'NR>1 && /^#/ { sub(/^# ?/, ""); print; next } NR>1 { exit }' "$0"; exit 0 ;;
    -*)        echo "unknown flag: $1" >&2; exit 2 ;;
    *)         echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "$STATE"
say(){ printf '%s  [w%s]  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$WORKER" "$*" | tee -a "$LOG"; }

[[ -f "$BUILDER" ]] || { say "FATAL: builder missing: $BUILDER"; exit 1; }
[[ -f "$BATCH_LOG" ]] || { say "FATAL: batch log missing: $BATCH_LOG"; exit 1; }
command -v "$PYTHON" >/dev/null || { say "FATAL: python not on PATH: $PYTHON"; exit 1; }

build_queue(){
  say "scanning $BATCH_LOG rows $START-$END"
  "$PYTHON" - "$BATCH_LOG" "$QUEUE" "$START" "$END" "$REDO" <<'PYQ'
import json, sys
from pathlib import Path
log, out, start, end, redo = Path(sys.argv[1]), Path(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5] == "1"
prev = {}
if out.exists() and not redo:
    try:
        for item in json.load(open(out))["items"]:
            prev[item["num"]] = item
    except Exception:
        pass
rows = []
in_table = False
for line in log.read_text(encoding="utf-8").splitlines():
    if line.startswith("| # |"):
        in_table = True
        continue
    if in_table and line.startswith("|---"):
        continue
    if in_table and line.startswith("|"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 9 and parts[0].isdigit():
            num = int(parts[0])
            if start <= num <= end and parts[3].endswith("/SKILL.md"):
                old = prev.get(parts[0], {})
                status = "pending" if redo else old.get("status", "pending")
                rows.append({
                    "num": parts[0],
                    "name": parts[1],
                    "repo": parts[2],
                    "canonical_path": parts[3],
                    "batch_status": parts[5],
                    "mp4_path": parts[6],
                    "status": status,
                    "attempts": old.get("attempts", 0),
                    "note": old.get("note", ""),
                })
out.write_text(json.dumps({"items": rows}, indent=2), encoding="utf-8")
print(f"queued {len(rows)} skill explainers")
PYQ
}

claim(){
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1)); (( waited > 120 )) && { say "stale lock after ${waited}s — clearing"; rm -rf "$LOCK"; }
  done
  "$PYTHON" - "$QUEUE" "$WORKER" <<'PYC'
import json, sys
p, worker = sys.argv[1], sys.argv[2]
q = json.load(open(p))
for item in q["items"]:
    if item["status"] == "pending":
        item["status"] = "building"
        item["worker"] = worker
        json.dump(q, open(p, "w"), indent=2)
        print("\t".join([item["num"], item["name"], item["canonical_path"]]))
        break
PYC
  rm -rf "$LOCK"
}

set_status(){
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1)); (( waited > 120 )) && rm -rf "$LOCK"
  done
  "$PYTHON" - "$QUEUE" "$1" "$2" "${3:-}" "$MAX_ATTEMPTS" <<'PYS'
import json, sys
p, num, status, note, max_attempts = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
q = json.load(open(p))
for item in q["items"]:
    if item["num"] == num:
        item["status"] = status
        item["note"] = note
        if status == "failed":
            item["attempts"] = item.get("attempts", 0) + 1
            if item["attempts"] < max_attempts:
                item["status"] = "pending"
json.dump(q, open(p, "w"), indent=2)
PYS
  rm -rf "$LOCK"
}

counts(){
  "$PYTHON" - "$QUEUE" <<'PYN'
import collections, json, sys
q = json.load(open(sys.argv[1]))
c = collections.Counter(i["status"] for i in q["items"])
print(" ".join(f"{k}={v}" for k, v in sorted(c.items())) or "empty")
PYN
}

[[ -f "$QUEUE" ]] || build_queue >/dev/null
(( REDO )) && build_queue >/dev/null
say "queue: $(counts)"

attempted=0; done_count=0; failed_count=0; consec_fail=0
started_at=$(date +%s)
failures=()

summary(){
  local wall=$(( $(date +%s) - started_at ))
  say "SUMMARY: attempted=$attempted done=$done_count failed=$failed_count wall=${wall}s"
  local f
  for f in "${failures[@]:-}"; do [[ -n "$f" ]] && say "  FAILED: $f"; done
  say "queue: $(counts)"
}

while true; do
  line="$(claim)"
  if [[ -z "$line" ]]; then
    if (( FOREVER )); then
      say "queue drained. rescanning in 30m."
      sleep 1800
      build_queue >/dev/null
      continue
    fi
    say "queue drained."
    summary
    exit 0
  fi

  IFS=$'\t' read -r row name skill_path <<<"$line"
  say "── row $row · $name · $skill_path"

  if (( DRY )); then
    say "DRY: would run $PYTHON $BUILDER --start $row --end $row --force-sheet"
    set_status "$row" "pending" "dry-run release"
    summary
    exit 0
  fi

  attempted=$((attempted+1))
  start_ts=$(date +%s)
  "$PYTHON" "$BUILDER" --start "$row" --end "$row" --force-sheet >>"$STATE/row-$row.w$WORKER.out" 2>&1
  rc=$?
  dur=$(( $(date +%s) - start_ts ))

  if (( rc == 0 )); then
    set_status "$row" "done" "expanded rebuild completed in ${dur}s"
    say "   DONE row $row in ${dur}s"
    done_count=$((done_count+1))
    consec_fail=0
  else
    tail_msg="$(tail -20 "$STATE/row-$row.w$WORKER.out" 2>/dev/null | tr '\n' ' ' | cut -c1-400)"
    set_status "$row" "failed" "rc=$rc after ${dur}s: $tail_msg"
    say "   FAILED row $row rc=$rc after ${dur}s"
    failed_count=$((failed_count+1))
    consec_fail=$((consec_fail+1))
    failures+=("row $row $name: rc=$rc")
    if (( ! NOHALT && consec_fail >= CONSEC_FAIL_STOP )); then
      say "HALT: $consec_fail consecutive failures. Use --no-halt to continue anyway."
      summary
      exit 1
    fi
  fi

  if (( N > 0 && attempted >= N )); then
    summary
    exit 0
  fi
  sleep "$COOLDOWN"
done
