#!/usr/bin/env bash
# bookloop.sh — unattended book→film factory. A sibling of filmloop.sh.
#
# filmloop.sh AUDITS AND REBUILDS reels that already have a beat_sheet.json.
# bookloop.sh CREATES one from nothing: point it at a book folder and it builds a
# deep-explainer film, Liam persona, for every chapter in <book>/chapters/.
#
# Same architecture as filmloop, and for the same reason: one Claude session cannot
# run for days — it fills its context and stops. The loop lives in the shell, Claude
# is invoked ONCE PER CHAPTER with a fresh context, and all state is on disk, so a
# crash, a reboot, or a killed session resumes exactly where it stopped.
#
#   ./bookloop.sh <book-dir>            run every chapter, then exit
#   ./bookloop.sh <book-dir> --once     one chapter, then exit  (RUN THIS FIRST)
#   ./bookloop.sh <book-dir> --n N      N chapters, then exit
#   ./bookloop.sh <book-dir> --dry      print the plan, invoke nothing
#   ./bookloop.sh <book-dir> --all      include front/back matter (default: skipped)
#   ./bookloop.sh <book-dir> --forever  keep rescanning for new chapters
#   ./bookloop.sh <book-dir> --no-halt  do not halt after consecutive failures
#
# NO PANTRY, NO STOPPING. Every beat is machine-buildable: Manim, Remotion, and the
# ~1,500-PNG local still library (Tier 0) only. The loop never writes a Tier 2/3
# shopping entry that would wait on a human, and it carries the "ship with slates"
# override that Gate D2 of the deep-explainer skill already provides for.
set -uo pipefail

BOOK=""
N=0; DRY=0; ALL=0; FOREVER=0; NOHALT=0; REBUILD=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --once)    N=1; shift ;;
    --n)       shift
               [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--n requires an integer >= 1" >&2; exit 2; }
               N="$1"; shift ;;
    --dry)     DRY=1; shift ;;
    --all)     ALL=1; shift ;;
    --forever) FOREVER=1; shift ;;
    --no-halt) NOHALT=1; shift ;;
    --rebuild) REBUILD=1; shift ;;
    -h|--help) sed -n '2,27p' "$0"; exit 0 ;;
    -*)        echo "unknown flag: $1" >&2; exit 2 ;;
    *)         [[ -z "$BOOK" ]] || { echo "only one book folder at a time (got '$BOOK' and '$1')" >&2; exit 2; }
               BOOK="$1"; shift ;;
  esac
done
[[ -n "$BOOK" ]] || { echo "usage: $0 <book-dir> [--once|--n N|--dry|--all|--forever|--no-halt]" >&2; exit 2; }
BOOK="$(cd "$BOOK" 2>/dev/null && pwd)" || { echo "FATAL: no such folder: $BOOK" >&2; exit 1; }

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE="$BOOK/.bookloop"
QUEUE="$STATE/queue.json"
LOG="$STATE/bookloop.log"
LOCK="$STATE/queue.lock"
PROMPT="${BOOKLOOP_PROMPT:-$HERE/BOOKLOOP-PROMPT.md}"
MODEL="${BOOKLOOP_MODEL:-}"
BRUTALIST_ART="${BRUTALIST_ART:-/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art}"   # brutalist-art (hyphen) retired 2026-09-17
export BRUTALIST_ART
CHANNEL="${BOOKLOOP_CHANNEL:-claude-liam}"     # Liam persona: Kokoro am_onyx, free
SKILL="${BOOKLOOP_SKILL:-deep-explainer}"
BOOK_TITLE="$(sed -n 's/^title:[[:space:]]*"\{0,1\}\([^"]*\)"\{0,1\}[[:space:]]*$/\1/p' "$BOOK/metadata.yaml" 2>/dev/null | head -1)"
MAX_ATTEMPTS=2
COOLDOWN=20
MIN_FREE_GB=20
CONSEC_FAIL_STOP="${BOOKLOOP_CONSEC_FAIL_STOP:-4}"
BOOKLOOP_TIMEOUT="${BOOKLOOP_TIMEOUT:-9000}"   # deep-explainer is 5–10 min of film; give it 2.5h
AUDIBLE_TIMEOUT="${BOOKLOOP_AUDIBLE_TIMEOUT:-120}"  # watchdog on the audio CHECK itself (see audible())
WORKER="${BOOKLOOP_WORKER:-$$}"

mkdir -p "$STATE"
say(){ printf '%s  [w%s]  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$WORKER" "$*" | tee -a "$LOG"; }

[[ -d "$BOOK/chapters" ]] || { say "FATAL: $BOOK has no chapters/ — point me at a book folder"; exit 1; }
[[ -f "$PROMPT" ]]       || { say "FATAL: $PROMPT missing"; exit 1; }
[[ -x "$BRUTALIST_ART/art" ]] || { say "FATAL: BRUTALIST_ART=$BRUTALIST_ART has no ./art — nothing can be rendered"; exit 1; }
command -v claude  >/dev/null || { say "FATAL: claude CLI not on PATH"; exit 1; }
command -v ffprobe >/dev/null || { say "FATAL: ffprobe not on PATH — cannot verify audio"; exit 1; }

TIMEOUT_BIN=""
if   command -v timeout  >/dev/null 2>&1; then TIMEOUT_BIN="timeout -k 60"
elif command -v gtimeout >/dev/null 2>&1; then TIMEOUT_BIN="gtimeout -k 60"
else say "WARNING: no timeout/gtimeout on PATH — claude invocations run unwrapped, no watchdog"
fi

# audible <mp4>: an audio stream exists AND mean_volume > -40 dB.
# A muxed-but-silent master has shipped before; it never ships again.
#
# Returns 0 = audible, 1 = not audible, 2 = THE CHECK ITSELF TIMED OUT.
# The watchdog is not paranoia: on 2026-08-30 this pipeline wedged for 8h50m and
# froze a whole overnight run on one already-built reel. A stuck check must cost
# one chapter, never the night.
audible(){
  local t="" out raw mv rc
  [[ -n "$TIMEOUT_BIN" ]] && t="$TIMEOUT_BIN $AUDIBLE_TIMEOUT"
  out="$($t ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$1" </dev/null 2>/dev/null)"
  rc=$?
  (( rc == 124 )) && return 2
  [[ -n "$out" ]] || return 1
  raw="$($t ffmpeg -nostdin -i "$1" -af volumedetect -f null - </dev/null 2>&1)"
  rc=$?
  (( rc == 124 )) && return 2
  mv="$(printf '%s' "$raw" | sed -n 's/.*mean_volume: \(-\{0,1\}[0-9.]*\) dB.*/\1/p' | tail -1)"
  [[ -n "$mv" ]] || return 1
  python3 -c "import sys; sys.exit(0 if float('$mv') > -40 else 1)"
}

# review_cut <dir> <slug>: the review deliverable, master preferred, then review, then slate.
review_cut(){
  local d="$1" s="$2" f
  for f in "$d/$s.mp4" "$d/$s-review.mp4" "$d/$s-slate.mp4"; do
    [[ -f "$f" ]] && { echo "$f"; return; }
  done
  find "$d" -maxdepth 1 -name '*.mp4' -print 2>/dev/null | head -1
}

# ref_file <dir> <chapter>: what the cut must be NEWER than. The sheet once it exists,
# otherwise the chapter source itself.
ref_file(){ [[ -f "$1/beat_sheet.json" ]] && echo "$1/beat_sheet.json" || echo "$2"; }

slug_of(){ basename "$1" .md | sed 's/^[0-9]\{1,\}[-_]*//'; }

# ---------------------------------------------------------------- queue
build_queue(){
  say "scanning $BOOK/chapters (skip front/back matter: $([[ $ALL -eq 1 ]] && echo no || echo yes))"
  python3 - "$BOOK" "$QUEUE" "$ALL" <<'PY'
import json, os, re, sys
book, out, allf = sys.argv[1], sys.argv[2], sys.argv[3] == "1"
# books/CLAUDE.md rule 5: front/back matter is SKIPPED, never filmed. The old
# pattern matched only *matter/colophon, so "00-introduction.md" was queued as a
# chapter and would have been built as a film. Match the STEM (after the leading
# number), never a substring — so a real chapter like "04-introduction-to-equity"
# is still built.
SKIP_SUB   = re.compile(r'(front-?matter|back-?matter|colophon)', re.I)
SKIP_STEMS = {"introduction", "preface", "foreword", "prologue", "epilogue",
              "afterword", "appendix", "glossary", "bibliography", "index",
              "acknowledgements", "acknowledgments", "about-the-author",
              "dedication", "copyright", "toc", "contents"}
items = []
for name in sorted(os.listdir(os.path.join(book, "chapters"))):
    if not name.endswith(".md"):
        continue
    slug = re.sub(r'^\d+[-_]*', '', name[:-3])
    if not allf and (SKIP_SUB.search(name) or slug.lower() in SKIP_STEMS):
        continue
    items.append({
        "chapter": os.path.join(book, "chapters", name),
        "dir":     os.path.join(book, "youtube", slug),
        "slug":    slug,
        "status":  "pending",
        "attempts": 0,
        "note":    "",
    })
json.dump({"book": book, "items": items}, open(out, "w"), indent=1)
print(f"queued {len(items)} chapters")
PY
}

claim(){
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1))
    (( waited > 120 )) && { say "stale lock after ${waited}s — clearing"; rm -rf "$LOCK"; }
  done
  python3 - "$QUEUE" "$WORKER" <<'PY'
import json, sys
p, w = sys.argv[1], sys.argv[2]
q = json.load(open(p))
for i in q["items"]:
    if i["status"] == "pending":
        i["status"], i["worker"] = "building", w
        json.dump(q, open(p, "w"), indent=1)
        print("%s\t%s\t%s" % (i["dir"], i["slug"], i["chapter"]))
        break
PY
  rm -rf "$LOCK"
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
            i["attempts"] += 1
            if i["attempts"] < mx:
                i["status"] = "pending"
json.dump(q, open(p, "w"), indent=1)
PY
  rm -rf "$LOCK"
}

counts(){
  python3 - "$QUEUE" <<'PY'
import json, sys, collections
q = json.load(open(sys.argv[1]))
c = collections.Counter(i["status"] for i in q["items"])
print(" ".join(f"{k}={v}" for k, v in sorted(c.items())) or "empty")
PY
}

free_gb(){ df -g "$BOOK" 2>/dev/null | awk 'NR==2{print $4}' || echo 999; }

render_prompt(){
  sed -e "s#\$BRUTALIST_ART#$BRUTALIST_ART#g" \
      -e "s#\$BOOK#$BOOK#g" \
      -e "s#\$CHANNEL#$CHANNEL#g" \
      -e "s#\$SKILL#$SKILL#g" "$PROMPT"
}

[[ -f "$QUEUE" ]] || build_queue >/dev/null
say "book: $BOOK"
say "skill: $SKILL   channel: $CHANNEL (Liam / Kokoro am_onyx)   pantry: OFF"
say "queue: $(counts)"

script_start=$(date +%s)
attempted=0; done_count=0; failed_count=0; failures=()
print_summary(){
  local wall=$(( $(date +%s) - script_start ))
  say "SUMMARY: attempted=$attempted done=$done_count failed=$failed_count wall=${wall}s"
  local f; for f in "${failures[@]:-}"; do [[ -n "$f" ]] && say "  FAILED: $f"; done
  say "queue: $(counts)"
}
# --dry enumerates the plan and exits. It claims nothing, invokes nothing, and
# renders nothing — so it is deliberately NOT gated on free disk.
if (( DRY )); then
  say "DRY RUN — nothing is invoked, nothing is rendered, the queue is left untouched."
  python3 - "$QUEUE" "$SKILL" "$CHANNEL" "${N}" <<'PY'
import json, sys
q, skill, chan, n = json.load(open(sys.argv[1])), sys.argv[2], sys.argv[3], int(sys.argv[4])
items = [i for i in q["items"] if i["status"] == "pending"]
if n > 0: items = items[:n]
for k, i in enumerate(items, 1):
    print(f"  {k:>2}. {i['slug']}")
    print(f"      chapter : {i['chapter']}")
    print(f"      reel    : {i['dir']}")
print(f"\n  {len(items)} film(s) would be built — skill={skill} channel={chan} pantry=OFF")
PY
  exit 0
fi

consec_fail=0

while true; do
  IFS=$'\t' read -r d slug chapter < <(claim)
  if [[ -z "${d:-}" ]]; then
    if (( FOREVER == 0 )); then
      say "queue drained."; print_summary; exit 0
    fi
    say "queue drained. rescanning in 30m — new chapters get picked up automatically."
    sleep 1800
    rm -f "$QUEUE"; build_queue >/dev/null
    continue
  fi

  if [[ ! -f "$chapter" ]]; then
    set_status "$d" "blocked" "chapter file is gone — stale queue entry"
    say "   SKIP $slug — chapter file missing"; continue
  fi

  gb="$(free_gb)"
  if [[ "$gb" -lt "$MIN_FREE_GB" ]]; then
    say "PAUSED: only ${gb}GB free (need ${MIN_FREE_GB}). Renders fail dirty when the disk fills."
    set_status "$d" "pending" "paused for disk"; sleep 600; continue
  fi

  say "── $slug   ($(basename "$chapter"), free ${gb}GB, $(counts))"

  mkdir -p "$d"
  if (( REBUILD )); then
    # Force a genuine rebuild: with a passing cut present the builder correctly
    # declines to touch it, so the reel would be re-marked done unchanged.
    n_old=$(find "$d" -maxdepth 1 -name '*.mp4' -print 2>/dev/null | wc -l | tr -d ' ')
    find "$d" -maxdepth 1 -name '*.mp4' -delete 2>/dev/null
    say "   REBUILD — cleared $n_old prior cut(s); the builder has nothing to short-circuit on"
  fi
  start=$(date +%s); attempted=$((attempted+1))
  # Fresh context per chapter. --dangerously-skip-permissions is appropriate here ONLY
  # because every output is regenerable from the chapter + beat sheet, both git-tracked.
  ( cd "$BRUTALIST_ART" && \
    BOOK="$BOOK" REEL_DIR="$d" REEL_SLUG="$slug" CHAPTER_FILE="$chapter" \
    BRUTALIST_ART="$BRUTALIST_ART" BOOKLOOP_NO_PANTRY=1 \
    ${TIMEOUT_BIN:+$TIMEOUT_BIN "$BOOKLOOP_TIMEOUT"} claude -p "$(render_prompt)

TARGET CHAPTER FOR THIS INVOCATION
  chapter file : $chapter
  reel folder  : $d
  slug         : $slug
Build this one film. When it is done or has failed, stop — the supervisor starts the next." \
      ${MODEL:+--model "$MODEL"} \
      --dangerously-skip-permissions \
      </dev/null >>"$STATE/$slug.w$WORKER.out" 2>&1 )
  rc=$?
  dur=$(( $(date +%s) - start ))
  cut="$(review_cut "$d" "$slug")"
  ref="$(ref_file "$d" "$chapter")"

  if (( rc == 124 )); then
    note="claude invocation timed out after ${dur}s"
    set_status "$d" "failed" "$note"; say "   FAILED — $note"
    consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
  else
    aud_rc=9
    [[ -n "$cut" ]] && { audible "$cut"; aud_rc=$?; }
  fi
  if (( rc == 124 )); then
    :
  elif (( aud_rc == 2 )); then
    note="audio check TIMED OUT after ${AUDIBLE_TIMEOUT}s — reel skipped, loop kept moving"
    set_status "$d" "failed" "$note"
    say "   FAILED — $note"
    consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
  elif [[ -n "$cut" ]] && [[ "$cut" -nt "$ref" ]] && (( aud_rc == 0 )); then
    # A film can render perfectly and still be unusable: 15 of 18 once shipped
    # naming the book and its chapter numbers. Audible is not review-ready.
    lint_out="$(python3 "$HERE/narration_lint.py" "$d/beat_sheet.json" "$BOOK_TITLE" 2>&1)"
    lint_rc=$?
    printf '%s\n' "$lint_out" | sed 's/^/     /' | tee -a "$LOG" >/dev/null
    printf '%s\n' "$lint_out" | grep -E '^  (HARD|soft|  )' | head -4 | sed 's/^/  /'
    if (( lint_rc != 0 )); then
      note="narration breaks the STANDALONE-IDEA LAW (names the book/chapter) — not review-ready"
      set_status "$d" "failed" "$note"
      say "   FAILED — $note"
      consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: law")
    else
      set_status "$d" "done" "review-ready: $(basename "$cut") in ${dur}s"
      say "   DONE in ${dur}s — $(basename "$cut") (audible, law-clean)"
      consec_fail=0; done_count=$((done_count+1))
    fi
  else
    # An account session limit is a PAUSE, not a failure — requeue without burning an
    # attempt, or a healthy loop halts overnight on three limit hits.
    if tail -c 400 "$STATE/$slug.w$WORKER.out" 2>/dev/null | grep -q "hit your session limit"; then
      set_status "$d" "pending" "session limit hit — requeued"
      say "   LIMIT — session limit; requeued $slug, sleeping 30m"; sleep 1800; continue
    fi
    if   [[ -n "$cut" ]] && (( aud_rc == 1 )); then note="cut exists but is SILENT — not review-ready"
    elif [[ -n "$cut" ]];                     then note="cut exists but is STALE (older than $(basename "$ref"))"
    elif (( rc == 0 ));                        then note="exit 0 but no review cut"
    else                                            note="claude exited non-zero after ${dur}s"; fi
    set_status "$d" "failed" "$note"
    say "   FAILED after ${dur}s — $note (see $STATE/$slug.w$WORKER.out)"
    consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
  fi

  if (( NOHALT == 0 && consec_fail >= CONSEC_FAIL_STOP )); then
    say "HALT: $consec_fail chapters failed in a row. That is a systemic bug, not bad luck."
    say "      Diagnose before restarting; the queue is preserved at $QUEUE."
    print_summary; exit 1
  fi
  if (( N > 0 && attempted >= N )); then print_summary; exit 0; fi
  sleep "$COOLDOWN"
done
