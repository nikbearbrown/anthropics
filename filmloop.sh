#!/usr/bin/env bash
# filmloop.sh — 24/7 unattended film factory (v2: slate-with-audio is the deliverable).
#
# One Claude Code session cannot run for days: it fills its context and stops. So the
# loop lives in the shell and Claude is invoked ONCE PER REEL with a fresh context.
# All state is on disk, so a crash, a reboot, or a killed session resumes exactly where
# it stopped.
#
# v2 CHANGE: a reel is DONE when a review cut exists WITH AUDIBLE AUDIO — the full
# master (<slug>.mp4) or the slate cut (<slug>-slate.mp4). Bear reviews slates with
# audio; full renders are a later, flagged pass. A silent cut is a FAILURE.
#
#   ./filmloop.sh              run forever
#   ./filmloop.sh --once       one reel, then exit (use this first) — same as --n 1
#   ./filmloop.sh --n N        N reels, then exit
#   ./filmloop.sh --dry        pick a reel and print what would run, invoke nothing
#
set -uo pipefail
ROOT="${FILMLOOP_ROOT:-$(pwd)}"
STATE="$ROOT/.filmloop"
QUEUE="$STATE/queue.json"
LOG="$STATE/filmloop.log"
PROMPT="$ROOT/FILMLOOP-PROMPT.md"
MODEL="${FILMLOOP_MODEL:-}"
BRUTALIST_ART="${BRUTALIST_ART:-/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art}"
export BRUTALIST_ART
MAX_ATTEMPTS=2
COOLDOWN=20                 # seconds between reels
MIN_FREE_GB=20              # refuse to render below this
CONSEC_FAIL_STOP=3          # halt on a systemic bug rather than burning a night
FILMLOOP_TIMEOUT="${FILMLOOP_TIMEOUT:-5400}"   # wall-clock cap per claude invocation, seconds
WORKER="${FILMLOOP_WORKER:-$$}"
LOCK="$STATE/queue.lock"
N=0; DRY=0                  # N=0 means unbounded; --once is exactly --n 1
while [[ $# -gt 0 ]]; do
  case "$1" in
    --once) N=1; shift ;;
    --n)
      shift
      [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--n requires an integer >= 1" >&2; exit 2; }
      N="$1"; shift ;;
    --dry) DRY=1; shift ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done
mkdir -p "$STATE"
say(){ printf '%s  [w%s]  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$WORKER" "$*" | tee -a "$LOG"; }
[[ -f "$PROMPT" ]] || { say "FATAL: $PROMPT missing"; exit 1; }
[[ -x "$BRUTALIST_ART/art" ]] || { say "FATAL: BRUTALIST_ART=$BRUTALIST_ART has no ./art — without the real toolkit nothing can be rendered"; exit 1; }
command -v claude >/dev/null || { say "FATAL: claude CLI not on PATH"; exit 1; }
command -v ffprobe >/dev/null || { say "FATAL: ffprobe not on PATH — cannot verify audio"; exit 1; }
TIMEOUT_BIN=""
if command -v timeout >/dev/null 2>&1; then
  TIMEOUT_BIN="timeout -k 60"
elif command -v gtimeout >/dev/null 2>&1; then
  TIMEOUT_BIN="gtimeout -k 60"
else
  say "WARNING: no timeout/gtimeout on PATH — claude invocations run unwrapped, no watchdog is active"
fi
# audible <mp4>: audio stream exists AND mean_volume > -40 dB. A muxed-but-silent
# master has shipped before; it never ships again.
audible(){
  ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$1" 2>/dev/null | grep -q . || return 1
  local mv
  mv="$(ffmpeg -i "$1" -af volumedetect -f null - 2>&1 | sed -n 's/.*mean_volume: \(-\{0,1\}[0-9.]*\) dB.*/\1/p' | tail -1)"
  [[ -n "$mv" ]] || return 1
  python3 -c "import sys; sys.exit(0 if float('$mv') > -40 else 1)"
}
# review_cut <dir> <slug>: prints the path of the review deliverable, master preferred.
review_cut(){
  # The rendered file is NOT always "<slug>.mp4": a nested short renders as
  # "<parent>-short.mp4". Prefer the canonical names, then fall back to ANY
  # top-level mp4 in the reel folder newer than its beat sheet.
  if [[ -f "$1/$2.mp4" ]]; then echo "$1/$2.mp4"; return; fi
  if [[ -f "$1/$2-slate.mp4" ]]; then echo "$1/$2-slate.mp4"; return; fi
  local newest
  newest="$(find "$1" -maxdepth 1 -name '*.mp4' -newer "$1/beat_sheet.json" -print 2>/dev/null | head -1)"
  [[ -n "$newest" ]] && echo "$newest"
}
# ---------------------------------------------------------------- queue
build_queue(){
  say "scanning $ROOT against the current standard (rules v$(python3 -c "import re;print(re.search(r'RULES_VERSION *= *(\\d+)',open('$ROOT/queue_scan.py').read()).group(1))" 2>/dev/null || echo '?'))"
  python3 "$ROOT/queue_scan.py" --root "$ROOT" --out "$QUEUE" | tee -a "$LOG"
}
claim_reel(){
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1))
    if (( waited > 120 )); then say "stale lock after ${waited}s — clearing"; rm -rf "$LOCK"; fi
  done
  python3 - "$QUEUE" "$WORKER" <<'PY'
import json,sys
p,w=sys.argv[1],sys.argv[2]
q=json.load(open(p))
for i in q["items"]:
    if i["status"]=="pending":
        i["status"]="building"; i["worker"]=w
        json.dump(q,open(p,'w'),indent=1)
        print(i["dir"]); break
PY
  rm -rf "$LOCK"
}
set_status(){  # dir status note
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1)); (( waited > 120 )) && rm -rf "$LOCK"
  done
  python3 - "$QUEUE" "$1" "$2" "${3:-}" "$MAX_ATTEMPTS" <<'PY'
import json,sys
p,d,st,note,max_attempts=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5])
q=json.load(open(p))
for i in q["items"]:
    if i["dir"]==d:
        i["status"]=st; i["note"]=note
        if st=="failed": i["attempts"]+=1
        if st=="failed" and i["attempts"]<max_attempts: i["status"]="pending"
json.dump(q,open(p,'w'),indent=1)
PY
  rm -rf "$LOCK"
}
counts(){
  python3 - "$QUEUE" <<'PY'
import json,sys,collections
q=json.load(open(sys.argv[1]))
c=collections.Counter(i["status"] for i in q["items"])
print(" ".join(f"{k}={v}" for k,v in sorted(c.items())) or "empty")
PY
}
free_gb(){ df -g "$ROOT" 2>/dev/null | awk 'NR==2{print $4}' || echo 999; }  # -g is macOS-only (BSD df)
render_prompt(){ sed "s#\$BRUTALIST_ART#$BRUTALIST_ART#g" "$PROMPT"; }
[[ -f "$QUEUE" ]] || build_queue >/dev/null
say "queue: $(counts)"
script_start=$(date +%s)
attempted=0; done_count=0; failed_count=0
failures=()
print_summary(){
  local wall=$(( $(date +%s) - script_start ))
  say "SUMMARY: attempted=$attempted done=$done_count failed=$failed_count wall=${wall}s"
  local f
  for f in "${failures[@]:-}"; do
    [[ -n "$f" ]] && say "  FAILED: $f"
  done
  say "queue: $(counts)"
}
consec_fail=0
while true; do
  d="$(claim_reel)"
  if [[ -z "$d" ]]; then
    if (( N > 0 )); then
      say "queue drained."
      print_summary
      exit 0
    fi
    say "queue drained. rescanning in 30m — new beat sheets get picked up automatically."
    sleep 1800
    blocked=""
    if mkdir "$LOCK" 2>/dev/null; then
      blocked="$(python3 - "$QUEUE" <<'PY'
import json,sys
q=json.load(open(sys.argv[1]))
print("\n".join(i["dir"] for i in q["items"] if i["status"]=="blocked"))
PY
)"
      rm -f "$QUEUE"; build_queue >/dev/null
      rm -rf "$LOCK"
    fi
    if [[ -n "$blocked" ]]; then
      while IFS= read -r bd; do
        [[ -n "$bd" ]] && set_status "$bd" "blocked" "carried over as blocked on requeue"
      done <<<"$blocked"
    fi
    [[ -f "$QUEUE" ]] || sleep 30
    continue
  fi
  slug="$(basename "$d")"
  if [[ ! -d "$d" || ! -f "$d/beat_sheet.json" ]]; then
    set_status "$d" "blocked" "directory or beat_sheet.json no longer exists — stale queue entry"
    say "   SKIP $slug — reel folder is gone (stale queue entry)"
    continue
  fi
  gb="$(free_gb)"
  if [[ "$gb" -lt "$MIN_FREE_GB" ]]; then
    say "PAUSED: only ${gb}GB free (need ${MIN_FREE_GB}). Renders fail dirty when the disk fills."
    sleep 600; continue
  fi
  say "── $slug   (free ${gb}GB, $(counts))"
  if (( DRY )); then
    say "DRY: would run claude -p on $d"
    set_status "$d" "pending" "dry-run release"
    exit 0
  fi
  start=$(date +%s)
  attempted=$((attempted+1))
  # Fresh context per reel. --dangerously-skip-permissions is appropriate here ONLY
  # because this machine does nothing else and every output is regenerable from the
  # beat sheet, which is git-tracked. Wrapped in a wall-clock timeout so a hung
  # invocation can't block the loop forever.
  ( cd "$ROOT" && \
    REEL_DIR="$d" REEL_SLUG="$slug" BRUTALIST_ART="$BRUTALIST_ART" \
    ${TIMEOUT_BIN:+$TIMEOUT_BIN "$FILMLOOP_TIMEOUT"} claude -p "$(render_prompt)
TARGET REEL FOR THIS INVOCATION: $d
Work only on this reel. When it is done or has failed, stop — the supervisor starts the next one." \
      ${MODEL:+--model "$MODEL"} \
      --dangerously-skip-permissions \
      </dev/null >>"$STATE/$slug.w$WORKER.out" 2>&1 )
  rc=$?
  dur=$(( $(date +%s) - start ))
  cut="$(review_cut "$d" "$slug")"
  if (( rc == 124 )); then
    note="timed out after ${dur}s"
    set_status "$d" "failed" "$note"
    say "   FAILED — $note"
    consec_fail=$((consec_fail+1))
    failed_count=$((failed_count+1)); failures+=("$slug: $note")
  elif [[ -n "$cut" ]] && [[ "$cut" -nt "$d/beat_sheet.json" ]] && audible "$cut"; then
    # DONE = a review cut newer than the sheet, with audible audio. Slate cuts count:
    # slates-with-audio ARE the review deliverable. Silent or stale cuts do not.
    set_status "$d" "done" "review-ready: $(basename "$cut") in ${dur}s"
    say "   DONE in ${dur}s — $(basename "$cut") (audible)"
    consec_fail=0
    done_count=$((done_count+1))
  else
    # Ported from the viz-riff loop (ADAPT 5, 2026-08-25): an account session limit
    # is a PAUSE, not a failure. Requeue without burning an attempt and sleep until
    # the window resets — otherwise 3 limit hits in a row trip CONSEC_FAIL_STOP and
    # a healthy loop halts overnight.
    if tail -c 400 "$STATE/$slug.w$WORKER.out" 2>/dev/null | grep -q "hit your session limit"; then
      set_status "$d" "pending" "session limit hit — requeued"
      say "   LIMIT — session limit hit; requeued $slug, sleeping 30m"
      sleep 1800
      continue
    fi
    if [[ -n "$cut" ]]; then
      if ! audible "$cut"; then note="cut exists but is SILENT — not review-ready"
      else note="cut exists but is STALE (older than beat_sheet.json)"; fi
    elif (( rc == 0 )); then note="exit 0 but no review cut"
    else note="claude exited non-zero after ${dur}s"; fi
    set_status "$d" "failed" "$note"
    say "   FAILED after ${dur}s — $note (see $STATE/$slug.w$WORKER.out)"
    consec_fail=$((consec_fail+1))
    failed_count=$((failed_count+1)); failures+=("$slug: $note")
  fi
  if (( consec_fail >= CONSEC_FAIL_STOP )); then
    say "HALT: $consec_fail reels failed in a row. That is a systemic bug, not bad luck."
    say "      Diagnose before restarting; the queue is preserved at $QUEUE."
    (( N > 0 )) && print_summary
    exit 1
  fi
  if (( N > 0 && attempted >= N )); then
    print_summary
    exit 0
  fi
  sleep "$COOLDOWN"
done
