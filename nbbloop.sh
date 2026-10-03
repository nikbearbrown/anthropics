#!/usr/bin/env bash
# nbbloop.sh — unattended REGISTER-CONVERSION factory. A sibling of bookloop.sh.
#
# bookloop.sh CREATES a film from a chapter. filmloop.sh AUDITS AND REBUILDS reels.
# nbbloop.sh CONVERTS an existing beat sheet into the NikBearBrown (Teardown) cut:
# point it at a folder of reels and it runs skills/make/nbb on every one.
#
# Same architecture, same reason: one Claude session cannot rewrite thousands of
# narration lines — it fills its context and stops. The loop lives in the shell,
# Claude is invoked ONCE PER REEL with a fresh context, and all state is on disk,
# so a crash, a reboot, or a killed session resumes exactly where it stopped.
#
#   ./nbbloop.sh <reels-dir>            convert every reel, then exit
#   ./nbbloop.sh <reels-dir> --once     one reel, then exit  (RUN THIS FIRST)
#   ./nbbloop.sh <reels-dir> --n N      N reels, then exit
#   ./nbbloop.sh <reels-dir> --dry      print the plan, invoke nothing
#   ./nbbloop.sh <reels-dir> --redo     reconvert reels already marked done
#   ./nbbloop.sh <reels-dir> --forever  keep rescanning for new reels
#   ./nbbloop.sh <reels-dir> --no-halt  do not halt after consecutive failures
#
# NO RENDERING. This loop produces beat_sheet.nbb.json and nothing else — no audio,
# no Remotion, no compile. Rendering the converted sheets is a separate pass, so a
# bad conversion costs seconds of review instead of an hour of GPU.
set -uo pipefail

SRC=""
N=0; DRY=0; FOREVER=0; NOHALT=0; REDO=0
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
    -h|--help) sed -n '2,23p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*)        echo "unknown flag: $1" >&2; exit 2 ;;
    *)         [[ -z "$SRC" ]] || { echo "one folder at a time (got '$SRC' and '$1')" >&2; exit 2; }
               SRC="$1"; shift ;;
  esac
done
[[ -n "$SRC" ]] || { echo "usage: $0 <reels-dir> [--once|--n N|--dry|--redo|--forever|--no-halt]" >&2; exit 2; }
SRC="$(cd "$SRC" 2>/dev/null && pwd)" || { echo "FATAL: no such folder: $SRC" >&2; exit 1; }

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE="$SRC/.nbbloop"
QUEUE="$STATE/queue.json"
LOG="$STATE/nbbloop.log"
LOCK="$STATE/queue.lock"
PROMPT="${NBBLOOP_PROMPT:-$HERE/NBBLOOP-PROMPT.md}"
MODEL="${NBBLOOP_MODEL:-}"
BRUTALIST_ART="${BRUTALIST_ART:-/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art}"
export BRUTALIST_ART
MAX_ATTEMPTS=2
COOLDOWN=8
CONSEC_FAIL_STOP="${NBBLOOP_CONSEC_FAIL_STOP:-4}"
NBBLOOP_TIMEOUT="${NBBLOOP_TIMEOUT:-1800}"   # a sheet rewrite, not a render: 30 min is generous
WORKER="${NBBLOOP_WORKER:-$$}"

mkdir -p "$STATE"
say(){ printf '%s  [w%s]  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$WORKER" "$*" | tee -a "$LOG"; }

[[ -f "$PROMPT" ]] || { say "FATAL: $PROMPT missing"; exit 1; }
[[ -f "$BRUTALIST_ART/skills/make/nbb/SKILL.md" ]] || { say "FATAL: BRUTALIST_ART=$BRUTALIST_ART has no nbb skill"; exit 1; }
command -v claude >/dev/null || { say "FATAL: claude CLI not on PATH"; exit 1; }

TIMEOUT_BIN=""
if   command -v timeout  >/dev/null 2>&1; then TIMEOUT_BIN="timeout -k 30"
elif command -v gtimeout >/dev/null 2>&1; then TIMEOUT_BIN="gtimeout -k 30"
else say "WARNING: no timeout/gtimeout on PATH — claude invocations run unwrapped, no watchdog"
fi

# ---------------------------------------------------------------- the check
# converted <source_sheet> <nbb_sheet>: is this a REAL conversion?
#   0 = converted   1 = not converted   3 = unreadable/invalid
# A scaffold is not a conversion. The failure this guards against is a session that
# exits 0 having touched nothing — the sheet is valid JSON and completely unchanged.
converted(){
  python3 - "$1" "$2" <<'PY'
import json, sys
try:
    src = json.load(open(sys.argv[1]))
    nbb = json.load(open(sys.argv[2]))
except Exception as e:
    print(f"unreadable: {e}"); sys.exit(3)

if nbb.get("_variant_todo"):
    print("_variant_todo still present — scaffold was never worked"); sys.exit(1)

sb = {b.get("beat_id"): b for b in src.get("beats", [])}
nb = nbb.get("beats", [])
if not nb:
    print("no beats"); sys.exit(3)

same = blank = 0
for b in nb:
    t = (b.get("narration_text") or "").strip()
    if not t:
        blank += 1; continue
    o = (sb.get(b.get("beat_id"), {}).get("narration_text") or "").strip()
    if o and t == o:
        same += 1
if blank:
    print(f"{blank} beat(s) have empty narration"); sys.exit(1)
# Allow a couple of legitimately-identical short lines (a title restate, a one-word beat).
if same > max(2, len(nb) // 5):
    print(f"{same}/{len(nb)} narrations identical to source — not rewritten"); sys.exit(1)

# Steps 3 and 4 are part of the conversion, not optional. A session that rewrote
# the register but dropped the exercise beat or the outro would otherwise pass.
tail = " ".join(str(b.get("act", "")) + " " + str(b.get("beat_id", "")) for b in nb[-3:]).lower()
if "exercise" not in tail and "your turn" not in (nb[-2].get("narration_text", "").lower() if len(nb) > 1 else ""):
    print("no LLM exercise beat near the end (nbb SKILL.md step 3)"); sys.exit(1)
if "outro" not in tail:
    print("no outro beat at the end (nbb SKILL.md step 4)"); sys.exit(1)

meta = nbb.get("metadata", {})
if str(meta.get("register", "")).lower() != "teardown":
    print(f"register is {meta.get('register')!r}, expected Teardown"); sys.exit(1)
if meta.get("voice_kokoro") != "am_onyx":
    print(f"voice_kokoro is {meta.get('voice_kokoro')!r}, expected am_onyx (Liam)"); sys.exit(1)

print(f"converted: {len(nb)} beats, {same} unchanged")
sys.exit(0)
PY
}

set_status(){  # dir status note
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1)); (( waited > 120 )) && rm -rf "$LOCK"
  done
  python3 - "$QUEUE" "$1" "$2" "${3:-}" "$MAX_ATTEMPTS" <<'PY'
import json, sys
p, d, st, note, mx = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
q = json.load(open(p))
for i in q["items"]:
    if i["dir"] == d:
        i["status"], i["note"] = st, note
        if st == "failed":
            i["attempts"] = i.get("attempts", 0) + 1
            if i["attempts"] < mx:
                i["status"] = "pending"
json.dump(q, open(p, "w"), indent=2)
PY
  rmdir "$LOCK" 2>/dev/null || true
}

counts(){
  python3 - "$QUEUE" <<'PY'
import json, sys, collections
q = json.load(open(sys.argv[1]))
c = collections.Counter(i["status"] for i in q["items"])
print(" ".join(f"{k}={v}" for k, v in sorted(c.items())) or "empty")
PY
}

render_prompt(){
  sed -e "s#\$BRUTALIST_ART#$BRUTALIST_ART#g" \
      -e "s#\$SOURCE_SHEET#$src_sheet#g" \
      -e "s#\$NBB_SHEET#$nbb_sheet#g" "$PROMPT"
}

# ---------------------------------------------------------------- queue
build_queue(){
  say "scanning $SRC for reels with beat_sheet.json"
  python3 - "$SRC" "$QUEUE" "$REDO" <<'PY'
import json, os, sys
src, out, redo = sys.argv[1], sys.argv[2], sys.argv[3] == "1"
prev = {}
if os.path.exists(out):
    try:
        for i in json.load(open(out))["items"]:
            prev[i["dir"]] = i
    except Exception:
        pass
items = []
for name in sorted(os.listdir(src)):
    d = os.path.join(src, name)
    if not os.path.isdir(d) or name.startswith(("nbb-", ".")):
        continue
    sheet = os.path.join(d, "beat_sheet.json")
    if not os.path.isfile(sheet):
        continue
    nbb_dir = os.path.join(src, f"nbb-{name}")
    it = {
        "slug": name,
        "dir": d,
        "src_sheet": sheet,
        "nbb_dir": nbb_dir,
        "nbb_sheet": os.path.join(nbb_dir, "beat_sheet.nbb.json"),
        "status": "pending",
        "attempts": 0,
        "note": "",
    }
    old = prev.get(d)
    if old and not redo:
        it["status"]   = old.get("status", "pending")
        it["attempts"] = old.get("attempts", 0)
        it["note"]     = old.get("note", "")
    items.append(it)
json.dump({"items": items}, open(out, "w"), indent=2)
print(f"queue: {len(items)} reel(s)")
PY
}

[[ -f "$QUEUE" ]] || build_queue
(( REDO )) && build_queue

next_pending(){
  python3 - "$QUEUE" <<'PY'
import json, sys
q = json.load(open(sys.argv[1]))
for i in q["items"]:
    if i["status"] == "pending":
        print("\t".join([i["slug"], i["dir"], i["src_sheet"], i["nbb_dir"], i["nbb_sheet"]])); break
PY
}

say "source: $SRC"
say "skill: nbb   register: Teardown   voice: Liam / Kokoro am_onyx (free)   rendering: OFF"
say "queue: $(counts)"

if (( DRY )); then
  say "DRY RUN — nothing is invoked, the queue is left untouched."
  python3 - "$QUEUE" <<'PY'
import json, sys
q = json.load(open(sys.argv[1]))
p = [i for i in q["items"] if i["status"] == "pending"]
for n, i in enumerate(p, 1):
    print(f"  {n:>3}. {i['slug']}\n       → {i['nbb_sheet']}")
print(f"\n  {len(p)} reel(s) would be converted — nbb / Teardown, no rendering")
PY
  exit 0
fi

attempted=0; done_count=0; failed_count=0; consec_fail=0; failures=()
start_all=$(date +%s)

while :; do
  line="$(next_pending)"
  if [[ -z "$line" ]]; then
    (( FOREVER )) || break
    say "queue drained — rescanning in 60s"; sleep 60; build_queue; continue
  fi
  IFS=$'\t' read -r slug d src_sheet nbb_dir nbb_sheet <<<"$line"

  if (( N > 0 && attempted >= N )); then break; fi
  if (( !NOHALT && consec_fail >= CONSEC_FAIL_STOP )); then
    say "HALT — $consec_fail consecutive failures. Something systemic is wrong; fix it and re-run."
    break
  fi

  say "── $slug   ($(counts))"

  if [[ ! -f "$nbb_sheet" ]]; then
    say "   scaffolding (brand_variant.py nbb)"
    ( cd "$BRUTALIST_ART" && python3 runtime/scripts/brand_variant.py "$d" nbb ) >>"$STATE/$slug.w$WORKER.out" 2>&1
    if [[ ! -f "$nbb_sheet" ]]; then
      set_status "$d" "failed" "scaffold did not produce $nbb_sheet"
      say "   FAILED — scaffold produced nothing"
      consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: scaffold"); continue
    fi
  fi

  start=$(date +%s); attempted=$((attempted+1))
  # Fresh context per reel. --dangerously-skip-permissions is appropriate here ONLY
  # because the ONLY writable output is beat_sheet.nbb.json in a derived nbb- folder;
  # the canonical source sheet is never modified and everything is regenerable.
  ( cd "$BRUTALIST_ART" && \
    SRC_DIR="$d" NBB_DIR="$nbb_dir" REEL_SLUG="$slug" BRUTALIST_ART="$BRUTALIST_ART" \
    ${TIMEOUT_BIN:+$TIMEOUT_BIN "$NBBLOOP_TIMEOUT"} claude -p "$(render_prompt)

TARGET REEL FOR THIS INVOCATION
  source sheet : $src_sheet
  nbb sheet    : $nbb_sheet
  slug         : $slug
Convert this one beat sheet. Do not render. When it is done or has failed, stop." \
      ${MODEL:+--model "$MODEL"} \
      --dangerously-skip-permissions \
      </dev/null >>"$STATE/$slug.w$WORKER.out" 2>&1 )
  rc=$?
  dur=$(( $(date +%s) - start ))

  if (( rc == 124 )); then
    note="claude invocation timed out after ${dur}s"
    set_status "$d" "failed" "$note"; say "   FAILED — $note"
    consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: timeout"); continue
  fi

  # A session limit is a PAUSE, not a failure — requeue without burning an attempt.
  if tail -c 400 "$STATE/$slug.w$WORKER.out" 2>/dev/null | grep -q "hit your session limit"; then
    set_status "$d" "pending" "session limit hit — requeued"
    say "   LIMIT — session limit; requeued $slug, sleeping 30m"; sleep 1800; continue
  fi
  if tail -c 400 "$STATE/$slug.w$WORKER.out" 2>/dev/null | grep -qi "OAuth\|authenticate"; then
    say "   FATAL — the claude CLI is not authenticated. Sign in and re-run; the queue is intact."
    break
  fi

  chk="$(converted "$src_sheet" "$nbb_sheet")"; chk_rc=$?
  if (( chk_rc == 0 )); then
    set_status "$d" "done" "$chk in ${dur}s"
    say "   DONE in ${dur}s — $chk"
    consec_fail=0; done_count=$((done_count+1))
  else
    note="not converted: $chk"
    set_status "$d" "failed" "$note"
    say "   FAILED after ${dur}s — $note (see $STATE/$slug.w$WORKER.out)"
    consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $chk")
  fi
  sleep "$COOLDOWN"
done

wall=$(( $(date +%s) - start_all ))
say "SUMMARY: attempted=$attempted done=$done_count failed=$failed_count wall=$((wall/60))m"
for f in "${failures[@]:-}"; do [[ -n "$f" ]] && say "   FAILED: $f"; done
say "queue: $(counts)"
