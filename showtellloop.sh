#!/usr/bin/env bash
# Default: recursively convert existing beat sheets using the show-tell skill.
# See ./showtellloop.sh --help and SHOWTELL-CONVERT.md.
# The original Figma film factory below is retained behind --queue (first arg).
if [[ "${1:-}" != "--queue" ]]; then
  exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/showtell_convert.py" "$@"
fi
shift
# showtellloop.sh — unattended show-tell film factory in the Liam persona. A sibling of
# filmloop.sh and engineloop.sh, for the "Figma for Educational AI" series (or any repo
# that ships a SHOWTELL-QUEUE.tsv).
#
# One Claude session cannot run all night: it fills its context and stops. So the loop
# lives in the shell, Claude is invoked ONCE PER FILM with a fresh context, and all
# state is on disk, so a crash, a reboot, a session limit or a killed session resumes
# where it stopped.
#
#   ./showtellloop.sh [repo-dir]            build every unbuilt film in the queue, then exit
#   ./showtellloop.sh [repo-dir] --once     one film, then exit   (RUN THIS FIRST)
#   ./showtellloop.sh [repo-dir] --n N      N films, then exit
#   ./showtellloop.sh [repo-dir] --dry      print the plan, invoke nothing
#   ./showtellloop.sh [repo-dir] --only S   only films whose slug contains S
#   ./showtellloop.sh [repo-dir] --rebuild  rebuild films already marked done
#   ./showtellloop.sh [repo-dir] --no-halt  do not halt after consecutive failures
#
# The queue is $REPO/SHOWTELL-QUEUE.tsv, one film per line, tab-separated:
#   number  slug  title  mcp_budget  greeting  brief(what the agent does tonight)  pending(what needs Bear)
# Lines starting with # are comments.
#
# A film is DONE when $REPO/youtube/<slug>/exports/landscape/<slug>.mp4 exists, is newer
# than beat_sheet.json, is audible (mean volume > -40 dB), TYPECHECK.md shows 0 FAILs,
# and the supervisor has written SHOWTELL-DONE.txt beside the sheet.
# NEVER PUBLISHES, NEVER SPENDS, NEVER COMMITS. The Figma MCP server must be connected
# in the terminal Claude Code once (interactive `claude`, /mcp, figma, Connect) before
# films that write to Figma can run; the loop probes for that and refuses to start
# without it unless --no-figma is given.
set -uo pipefail

REPO=""; N=0; DRY=0; NOHALT=0; REBUILD=0; ONLY=""; NOFIGMA=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --once)     N=1; shift ;;
    --n)        shift; [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--n requires an integer >= 1" >&2; exit 2; }; N="$1"; shift ;;
    --dry)      DRY=1; shift ;;
    --only)     shift; ONLY="${1:-}"; shift ;;
    --rebuild)  REBUILD=1; shift ;;
    --no-halt)  NOHALT=1; shift ;;
    --no-figma) NOFIGMA=1; shift ;;
    -h|--help)  awk 'NR>1 && /^#/ { sub(/^# ?/, ""); print; next } NR>1 { exit }' "$0"; exit 0 ;;
    -*)         echo "unknown flag: $1" >&2; exit 2 ;;
    *)          [[ -z "$REPO" ]] || { echo "only one repo folder at a time" >&2; exit 2; }; REPO="$1"; shift ;;
  esac
done

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOKS="$(cd "$HERE/.." && pwd)"
[[ -n "$REPO" ]] || REPO="$BOOKS/figma-for-educational-ai"
REPO="$(cd "$REPO" 2>/dev/null && pwd)" || { echo "FATAL: no such folder: $REPO" >&2; exit 1; }

STATE="$REPO/.showtellloop"
QUEUE_TSV="$REPO/SHOWTELL-QUEUE.tsv"
QUEUE="$STATE/queue.json"
LOG="$STATE/showtellloop.log"
LOCK="$STATE/queue.lock"
RENDER_LOCK="${SHOWTELL_RENDER_LOCK:-$STATE/render.lock}"
PROMPT="${SHOWTELL_PROMPT:-$HERE/SHOWTELL-LOOP-PROMPT.md}"
MODEL="${SHOWTELL_MODEL:-}"
BRUTALIST_ART="${BRUTALIST_ART:-$BOOKS/brutalist.art}"
export BRUTALIST_ART
OUT_DIR="$REPO/youtube"
MAX_ATTEMPTS=2
COOLDOWN=20
MIN_FREE_GB="${SHOWTELL_MIN_FREE_GB:-8}"
CONSEC_FAIL_STOP="${SHOWTELL_CONSEC_FAIL_STOP:-3}"
FILM_TIMEOUT="${SHOWTELL_TIMEOUT:-12000}"        # 3h20m: the gate loops on a 4K show-tell ran past 9000 s before
AUDIBLE_TIMEOUT="${SHOWTELL_AUDIBLE_TIMEOUT:-120}"
LIMIT_SLEEP="${SHOWTELL_LIMIT_SLEEP:-1800}"

mkdir -p "$STATE"
say(){ printf '%s  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "$LOG"; }
[[ -f "$PROMPT" ]]    || { say "FATAL: $PROMPT missing"; exit 1; }
[[ -f "$QUEUE_TSV" ]] || { say "FATAL: $QUEUE_TSV missing (one film per line: number, slug, title, mcp_budget, greeting, brief, pending)"; exit 1; }
[[ -x "$BRUTALIST_ART/art" ]] || { say "FATAL: BRUTALIST_ART=$BRUTALIST_ART has no ./art"; exit 1; }
command -v claude  >/dev/null || { say "FATAL: claude CLI not on PATH"; exit 1; }
command -v ffprobe >/dev/null || { say "FATAL: ffprobe not on PATH"; exit 1; }
TIMEOUT_BIN=""
if command -v timeout >/dev/null 2>&1; then TIMEOUT_BIN="timeout -k 60"
elif command -v gtimeout >/dev/null 2>&1; then TIMEOUT_BIN="gtimeout -k 60"
else say "WARNING: no timeout/gtimeout on PATH — no watchdog"; fi

# audible <mp4>: 0 = audible, 1 = not, 2 = the check timed out.
audible(){
  ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$1" 2>/dev/null | grep -q . || return 1
  local mv
  mv="$(${TIMEOUT_BIN:+$TIMEOUT_BIN "$AUDIBLE_TIMEOUT"} ffmpeg -nostdin -i "$1" -af volumedetect -f null - </dev/null 2>&1 | sed -n 's/.*mean_volume: \(-\{0,1\}[0-9.]*\) dB.*/\1/p' | tail -1)"
  [[ -n "$mv" ]] || return 2
  python3 -c "import sys; sys.exit(0 if float('$mv') > -40 else 1)"
}
typecheck_clean(){  # <reel dir>: TYPECHECK.md exists and reports no FAIL rows
  [[ -f "$1/TYPECHECK.md" ]] || return 1
  ! grep -qE '\| *FAIL *\||FAIL ✗|FAILs: *[1-9]' "$1/TYPECHECK.md"
}
free_gb(){ df -g "$REPO" 2>/dev/null | awk 'NR==2{print $4}' || echo 999; }

# ---------------------------------------------------------------- Figma MCP pre-flight
figma_ready(){
  # A headless session sees only authenticate tools until Bear connects the plugin server once.
  local out
  out="$(cd "$BOOKS" && ${TIMEOUT_BIN:+$TIMEOUT_BIN 180} claude -p "List the tool names you have whose name contains figma, comma-separated, nothing else." --output-format text </dev/null 2>/dev/null)"
  grep -q "get_design_context\|use_figma\|get_figjam" <<<"$out"
}

# ---------------------------------------------------------------- queue
build_queue(){
  python3 - "$QUEUE_TSV" "$QUEUE" "$OUT_DIR" "$ONLY" "$REBUILD" <<'PY'
import json,sys,os,csv
tsv,out,outdir,only,rebuild=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]=="1"
items=[]
for row in csv.reader((l for l in open(tsv,encoding='utf-8') if l.strip() and not l.startswith('#')),delimiter='\t'):
    if len(row)<7: print(f"skip malformed row: {row[:2]}",file=sys.stderr); continue
    num,slug,title,budget,greet,brief,pending=[c.strip() for c in row[:7]]
    if only and only not in slug: continue
    d=os.path.join(outdir,slug)
    done=os.path.exists(os.path.join(d,"SHOWTELL-DONE.txt")) and not rebuild
    items.append(dict(num=int(num),slug=slug,title=title,budget=budget,greeting=greet,brief=brief,pending=pending,dir=d,status="done" if done else "pending",attempts=0,note="already built" if done else ""))
items.sort(key=lambda i:i["num"])
json.dump({"items":items},open(out,"w"),indent=1)
print(f"queue: {len(items)} films, {sum(i['status']=='pending' for i in items)} pending")
PY
}
with_lock(){ local w=0; until mkdir "$LOCK" 2>/dev/null; do sleep 1; w=$((w+1)); (( w>120 )) && rm -rf "$LOCK"; done; "$@"; rm -rf "$LOCK"; }
claim(){ python3 - "$QUEUE" <<'PY'
import json,sys
p=sys.argv[1]; q=json.load(open(p))
for i in q["items"]:
    if i["status"]=="pending":
        i["status"]="building"; json.dump(q,open(p,'w'),indent=1)
        print("\t".join(str(i[k]) for k in ("num","slug","title","budget","greeting","brief","pending","dir"))); break
PY
}
set_status(){ python3 - "$QUEUE" "$1" "$2" "${3:-}" "$MAX_ATTEMPTS" <<'PY'
import json,sys
p,slug,st,note,mx=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5])
q=json.load(open(p))
for i in q["items"]:
    if i["slug"]==slug:
        i["status"]=st; i["note"]=note
        if st=="failed": i["attempts"]+=1
        if st=="failed" and i["attempts"]<mx: i["status"]="pending"
json.dump(q,open(p,'w'),indent=1)
PY
}
counts(){ python3 -c "
import json,collections;q=json.load(open('$QUEUE'));c=collections.Counter(i['status'] for i in q['items']);print(' '.join(f'{k}={v}' for k,v in sorted(c.items())) or 'empty')"; }
render_prompt(){  # num slug title budget greeting brief pending dir
  sed -e "s#\$BRUTALIST_ART#$BRUTALIST_ART#g" -e "s#\$REPO#$REPO#g" -e "s#\$BOOKS#$BOOKS#g" \
      -e "s#\$NUM#$1#g" -e "s#\$SLUG#$2#g" -e "s#\$TITLE#$3#g" -e "s#\$BUDGET#$4#g" -e "s#\$GREETING#$5#g" \
      -e "s#\$BRIEF#$6#g" -e "s#\$PENDING#$7#g" -e "s#\$REEL_DIR#$8#g" -e "s#\$RENDER_LOCK#$RENDER_LOCK#g" "$PROMPT"
}

build_queue | tee -a "$LOG"
say "queue: $(counts)"
if (( ! DRY && ! NOFIGMA )); then
  say "pre-flight: probing the Figma MCP server from a headless session…"
  if figma_ready; then say "pre-flight: Figma tools present."
  else say "FATAL: headless Claude sees no Figma tools. Run \`claude\` once, then /mcp → figma → Connect, and rerun. Or pass --no-figma for films that don't need it."; exit 1; fi
fi

script_start=$(date +%s); attempted=0; done_count=0; failed_count=0; consec_fail=0; failures=()
summary(){ say "SUMMARY: attempted=$attempted done=$done_count failed=$failed_count wall=$(( $(date +%s)-script_start ))s"; local f; for f in "${failures[@]:-}"; do [[ -n "$f" ]] && say "  FAILED: $f"; done; say "queue: $(counts)"; }

while true; do
  row="$(with_lock claim)"
  if [[ -z "$row" ]]; then say "queue drained."; (( DRY )) && rm -f "$QUEUE"; summary; exit 0; fi
  IFS=$'\t' read -r num slug title budget greeting brief pending d <<<"$row"
  gb="$(free_gb)"
  if [[ "$gb" -lt "$MIN_FREE_GB" ]]; then say "PAUSED: only ${gb}GB free"; with_lock set_status "$slug" "pending" "paused: disk"; sleep 600; continue; fi
  say "── film $num  $slug  ($title)  budget=$budget  free ${gb}GB  $(counts)"
  if (( DRY )); then say "DRY: would run claude -p for $slug into $d"; with_lock set_status "$slug" "dry" "dry-run: not built"; (( attempted+=1 )); if (( N>0 && attempted>=N )); then rm -f "$QUEUE"; exit 0; fi; continue; fi
  mkdir -p "$d"
  if (( REBUILD )); then rm -f "$d/SHOWTELL-DONE.txt"; fi
  start=$(date +%s); attempted=$((attempted+1))
  # Fresh context per film. --dangerously-skip-permissions is appropriate ONLY because this
  # loop never publishes, never commits, never spends, and every output is regenerable.
  ( cd "$BOOKS" && \
    ${TIMEOUT_BIN:+$TIMEOUT_BIN "$FILM_TIMEOUT"} claude -p "$(render_prompt "$num" "$slug" "$title" "$budget" "$greeting" "$brief" "$pending" "$d")" \
      ${MODEL:+--model "$MODEL"} --dangerously-skip-permissions \
      </dev/null >>"$STATE/$slug.out" 2>&1 )
  rc=$?; dur=$(( $(date +%s)-start ))
  rm -rf "$RENDER_LOCK" 2>/dev/null   # a killed session must not leave the render lock behind
  cut="$d/exports/landscape/$slug.mp4"
  if (( rc == 124 )); then
    note="timed out after ${dur}s"; with_lock set_status "$slug" "failed" "$note"; say "   FAILED — $note"; consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
  elif tail -c 600 "$STATE/$slug.out" 2>/dev/null | grep -qi "hit your session limit\|hit your weekly limit\|rate_limit"; then
    with_lock set_status "$slug" "pending" "session limit — requeued"; say "   LIMIT — requeued $slug; sleeping ${LIMIT_SLEEP}s"; sleep "$LIMIT_SLEEP"; continue
  elif [[ -f "$cut" && "$cut" -nt "$d/beat_sheet.json" ]] && audible "$cut" && typecheck_clean "$d"; then
    printf '%s  %s  film %s  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$(basename "$cut")" "$num" "$title" >"$d/SHOWTELL-DONE.txt"
    with_lock set_status "$slug" "done" "master in ${dur}s"; say "   DONE in ${dur}s — $(basename "$cut") (4K, audible, GATE T clean)"; consec_fail=0; done_count=$((done_count+1))
  else
    if [[ ! -f "$cut" ]]; then note="no master at exports/landscape after ${dur}s (rc=$rc)"
    elif [[ ! "$cut" -nt "$d/beat_sheet.json" ]]; then note="master is STALE (older than beat_sheet.json)"
    elif ! typecheck_clean "$d"; then note="TYPECHECK.md has FAILs or is missing"
    else note="master exists but is SILENT"; fi
    with_lock set_status "$slug" "failed" "$note"; say "   FAILED after ${dur}s — $note (see $STATE/$slug.out)"; consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
  fi
  if (( consec_fail >= CONSEC_FAIL_STOP && ! NOHALT )); then say "HALT: $consec_fail films failed in a row. Diagnose before restarting; the queue is at $QUEUE."; summary; exit 1; fi
  if (( N>0 && attempted>=N )); then summary; exit 0; fi
  sleep "$COOLDOWN"
done
