#!/usr/bin/env bash
# engineloop.sh — unattended repo→film factory. A sibling of bookloop.sh.
#
# bookloop.sh films a book's CHAPTERS. engineloop.sh films a REPO: point it at a
# repo folder (default: the-reallocation-engine-fresh) and it builds one film for
#   1. the engine itself        (README + DOMAIN + DATA_CONTRACT + AGENTS)
#   2. every skill              (.claude/skills/*/SKILL.md)
#   3. every maintained script  (scripts/**, .claude/hooks, .githooks, book/*.sh)
# Liam persona (Kokoro am_onyx, free) on every film. Long sources get the
# deep-explainer treatment (5–10 min). Sources under $SHORT_LINES lines get the
# short ai-explainer treatment — a 60-line shell script does not carry ten minutes.
#
# Same architecture as bookloop, for the same reason: one Claude session cannot
# run all night — it fills its context. The loop lives in the shell, Claude is
# invoked ONCE PER FILM with a fresh context, and all state is on disk, so a
# crash, a reboot, or a killed session resumes where it stopped.
#
#   ./engineloop.sh [repo-dir]             run every unbuilt film, then exit
#   ./engineloop.sh [repo-dir] --once      one film, then exit   (RUN THIS FIRST)
#   ./engineloop.sh [repo-dir] --n N       N films, then exit
#   ./engineloop.sh [repo-dir] --dry       print the plan, invoke nothing
#   ./engineloop.sh [repo-dir] --kind K    only engine | skill | script
#   ./engineloop.sh [repo-dir] --only S    only items whose slug contains S
#   ./engineloop.sh [repo-dir] --rebuild   rebuild items already marked done
#   ./engineloop.sh [repo-dir] --forever   keep rescanning for new sources
#   ./engineloop.sh [repo-dir] --no-halt   do not halt after consecutive failures
#
# A film is DONE when its reel folder holds <slug>.mp4 that is newer than
# beat_sheet.json, audible (mean volume > -40 dB), passes narration_lint.py, and
# the supervisor has written ENGINELOOP-DONE.txt beside it. NO PANTRY, NO STOPPING,
# NEVER PUBLISHES, NEVER SPENDS, READ-ONLY against the repo's source.
set -uo pipefail

REPO=""
N=0; DRY=0; FOREVER=0; NOHALT=0; REBUILD=0; KIND=""; ONLY=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --once)    N=1; shift ;;
    --n)       shift
               [[ "${1:-}" =~ ^[0-9]+$ && "${1:-0}" -ge 1 ]] || { echo "--n requires an integer >= 1" >&2; exit 2; }
               N="$1"; shift ;;
    --dry)     DRY=1; shift ;;
    --kind)    shift; KIND="${1:-}"; [[ "$KIND" =~ ^(engine|skill|script)$ ]] || { echo "--kind must be engine|skill|script" >&2; exit 2; }; shift ;;
    --only)    shift; ONLY="${1:-}"; shift ;;
    --rebuild) REBUILD=1; shift ;;
    --forever) FOREVER=1; shift ;;
    --no-halt) NOHALT=1; shift ;;
    -h|--help) awk 'NR>1 && /^#/ { sub(/^# ?/, ""); print; next } NR>1 { exit }' "$0"; exit 0 ;;
    -*)        echo "unknown flag: $1" >&2; exit 2 ;;
    *)         [[ -z "$REPO" ]] || { echo "only one repo folder at a time (got '$REPO' and '$1')" >&2; exit 2; }
               REPO="$1"; shift ;;
  esac
done

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOKS="$(cd "$HERE/.." && pwd)"
[[ -n "$REPO" ]] || REPO="$BOOKS/the-reallocation-engine-fresh"
REPO="$(cd "$REPO" 2>/dev/null && pwd)" || { echo "FATAL: no such folder: $REPO" >&2; exit 1; }

STATE="$REPO/.engineloop"
QUEUE="$STATE/queue.json"
LOG="$STATE/engineloop.log"
LOCK="$STATE/queue.lock"
PROMPT="${ENGINELOOP_PROMPT:-$HERE/ENGINELOOP-PROMPT.md}"
MODEL="${ENGINELOOP_MODEL:-}"
BRUTALIST_ART="${BRUTALIST_ART:-$BOOKS/brutalist.art}"   # brutalist-art (hyphen) retired 2026-09-17
export BRUTALIST_ART
CHANNEL="${ENGINELOOP_CHANNEL:-claude-liam}"          # Liam persona: Kokoro am_onyx, free
DEEP_SKILL="${ENGINELOOP_DEEP_SKILL:-deep-explainer}"  # 5–10 min, for real sources
SHORT_SKILL="${ENGINELOOP_SHORT_SKILL:-ai-explainer}"  # the short Claude-bookended reel, for tiny sources
SHORT_LINES="${ENGINELOOP_SHORT_LINES:-60}"           # a source under this many lines is "very short"
OUT_DIR="${ENGINELOOP_OUT:-$REPO/youtube}"
PREFIX="${ENGINELOOP_PREFIX:-claude-liam-}"           # matches the reels already in youtube/
MAX_ATTEMPTS=2
COOLDOWN=20
MIN_FREE_GB="${ENGINELOOP_MIN_FREE_GB:-8}"
CONSEC_FAIL_STOP="${ENGINELOOP_CONSEC_FAIL_STOP:-4}"
DEEP_TIMEOUT="${ENGINELOOP_DEEP_TIMEOUT:-9000}"       # 2.5h for a deep explainer
SHORT_TIMEOUT="${ENGINELOOP_SHORT_TIMEOUT:-5400}"     # 1.5h for a short one
AUDIBLE_TIMEOUT="${ENGINELOOP_AUDIBLE_TIMEOUT:-120}"
WORKER="${ENGINELOOP_WORKER:-$$}"

mkdir -p "$STATE"
say(){ printf '%s  [w%s]  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$WORKER" "$*" | tee -a "$LOG"; }

[[ -f "$REPO/README.md" ]]    || { say "FATAL: $REPO has no README.md — point me at a repo folder"; exit 1; }
[[ -d "$REPO/scripts" ]]      || { say "FATAL: $REPO has no scripts/"; exit 1; }
[[ -f "$PROMPT" ]]            || { say "FATAL: $PROMPT missing"; exit 1; }
[[ -x "$BRUTALIST_ART/art" ]] || { say "FATAL: BRUTALIST_ART=$BRUTALIST_ART has no ./art — nothing can be rendered"; exit 1; }
[[ -f "$BRUTALIST_ART/skills/make/$DEEP_SKILL/SKILL.md" ]]  || { say "FATAL: skill $DEEP_SKILL missing"; exit 1; }
[[ -f "$BRUTALIST_ART/skills/make/$SHORT_SKILL/SKILL.md" ]] || { say "FATAL: skill $SHORT_SKILL missing"; exit 1; }
[[ -f "$HERE/narration_lint.py" ]] || { say "FATAL: $HERE/narration_lint.py missing"; exit 1; }
command -v claude  >/dev/null || { say "FATAL: claude CLI not on PATH"; exit 1; }
command -v ffprobe >/dev/null || { say "FATAL: ffprobe not on PATH — cannot verify audio"; exit 1; }

TIMEOUT_BIN=""
if   command -v timeout  >/dev/null 2>&1; then TIMEOUT_BIN="timeout -k 60"
elif command -v gtimeout >/dev/null 2>&1; then TIMEOUT_BIN="gtimeout -k 60"
else say "WARNING: no timeout/gtimeout on PATH — claude invocations run unwrapped, no watchdog"
fi

# audible <mp4>: 0 = audible, 1 = not, 2 = the check itself timed out (bookloop's 8h50m wedge).
audible(){
  local t="" out raw mv rc
  [[ -n "$TIMEOUT_BIN" ]] && t="$TIMEOUT_BIN $AUDIBLE_TIMEOUT"
  out="$($t ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$1" </dev/null 2>/dev/null)"; rc=$?
  (( rc == 124 )) && return 2
  [[ -n "$out" ]] || return 1
  raw="$($t ffmpeg -nostdin -i "$1" -af volumedetect -f null - </dev/null 2>&1)"; rc=$?
  (( rc == 124 )) && return 2
  mv="$(printf '%s' "$raw" | sed -n 's/.*mean_volume: \(-\{0,1\}[0-9.]*\) dB.*/\1/p' | tail -1)"
  [[ -n "$mv" ]] || return 1
  python3 -c "import sys; sys.exit(0 if float('$mv') > -40 else 1)"
}

review_cut(){  # master preferred, then review, then slate
  local d="$1" s="$2" f
  for f in "$d/$s.mp4" "$d/$s-review.mp4" "$d/$s-slate.mp4"; do [[ -f "$f" ]] && { echo "$f"; return; }; done
  find "$d" -maxdepth 1 -name '*.mp4' -print 2>/dev/null | head -1
}
ref_file(){ [[ -f "$1/beat_sheet.json" ]] && echo "$1/beat_sheet.json" || echo "$2"; }
free_gb(){ df -g "$REPO" 2>/dev/null | awk 'NR==2{print $4}' || echo 999; }

# ---------------------------------------------------------------- queue
# One item per film. kind=engine|skill|script. sources = the files the worker
# must read (pipe-joined). lines = size of the primary source, which picks the
# skill. The legacy copies under data/80-days-to-stay/ are NOT queued —
# scripts/README.md names scripts/ as the maintained tree. Tests, fixtures,
# requirements, __init__, README and __pycache__ are never films.
build_queue(){
  say "scanning $REPO (short < $SHORT_LINES lines → $SHORT_SKILL, else $DEEP_SKILL)"
  python3 - "$REPO" "$QUEUE" "$OUT_DIR" "$PREFIX" "$SHORT_LINES" "$DEEP_SKILL" "$SHORT_SKILL" "$KIND" "$ONLY" "$REBUILD" <<'PY'
import json, os, re, sys, glob
repo, out, outdir, prefix, short_lines, deep, short, kind_f, only, rebuild = sys.argv[1:11]
short_lines, rebuild = int(short_lines), rebuild == "1"

def rel(p): return os.path.relpath(p, repo)
def nlines(p):
    try: return sum(1 for _ in open(p, encoding="utf-8", errors="ignore"))
    except Exception: return 0
def exists(*ps): return [rel(p) for p in ps if os.path.isfile(p)]
def kebab(s): return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")

items = []

# 1. the engine itself — the repo's front door and its contracts
engine_src = exists(*[os.path.join(repo, f) for f in
    ("README.md", "DOMAIN.md", "DATA_CONTRACT.md", "AGENTS.md", "PROJECT_RULES.md",
     "docs/labor-separation.md", "recipes/README.md", "scripts/README.md", "package.json")])
items.append(dict(kind="engine", name="the-engine", title="The Reallocation Engine — how the whole machine runs",
                  primary="README.md", sources=engine_src,
                  lines=sum(nlines(os.path.join(repo, s)) for s in engine_src), slug=prefix + "engine-overview"))

# 2. every skill
for sk in sorted(glob.glob(os.path.join(repo, ".claude", "skills", "*", "SKILL.md"))):
    d = os.path.dirname(sk); name = os.path.basename(d)
    srcs = exists(sk) + sorted(rel(p) for p in glob.glob(os.path.join(d, "**", "*"), recursive=True)
                               if p != sk and os.path.isfile(p) and "__pycache__" not in p and not p.endswith(".pyc"))
    items.append(dict(kind="skill", name=name, title=f"Skill: {name}", primary=rel(sk), sources=srcs,
                      lines=nlines(sk), slug=prefix + "skill-" + kebab(name)))

# 3. every maintained script
SKIP_NAME = re.compile(r"(^__init__\.py$|^README|\.test\.mjs$|^test_|requirements\.txt$|\.gitkeep$|\.md$|\.json$|\.txt$|\.pyc$)", re.I)
SKIP_DIR  = re.compile(r"(__pycache__|fixtures|/tests?/|/contrib/)")
roots = [os.path.join(repo, "scripts"), os.path.join(repo, ".claude", "hooks"),
         os.path.join(repo, ".githooks"), os.path.join(repo, "book")]
seen = set()
for root in roots:
    if not os.path.isdir(root): continue
    for dp, dn, fn in os.walk(root):
        dn[:] = [x for x in dn if x != "__pycache__" and x != "node_modules"]
        for f in sorted(fn):
            p = os.path.join(dp, f)
            if root.endswith("book") and not f.endswith(".sh"): continue   # book/: only its build scripts
            if SKIP_NAME.search(f) or SKIP_DIR.search(p + "/"): continue
            if not re.search(r"\.(mjs|js|py|sh)$|^pre-commit$", f): continue
            if p in seen: continue
            seen.add(p)
            r = rel(p)
            stem = re.sub(r"\.(mjs|js|py|sh)$", "", r)
            stem = re.sub(r"^scripts/", "", stem)
            stem = re.sub(r"^\.claude/hooks/", "hook-", stem)
            stem = re.sub(r"^\.githooks/", "githook-", stem)
            slug = prefix + "script-" + kebab(stem)
            base = os.path.basename(stem)
            # companion docs: the recipe of the same name (+ its card), the folder README, the package.json entry
            srcs = [r]
            srcs += exists(os.path.join(repo, "recipes", base + ".md"), os.path.join(repo, "recipes", base + ".card.md"),
                           os.path.join(dp, "README.md"))
            if dp != os.path.join(repo, "scripts"): srcs += exists(os.path.join(repo, "scripts", "README.md"))
            srcs += exists(os.path.join(repo, "DATA_CONTRACT.md"))
            items.append(dict(kind="script", name=base, title=f"Script: {r}", primary=r, sources=srcs,
                              lines=nlines(p), slug=slug))

# filters, skill choice, done-markers
prev = {}
if os.path.exists(out):
    try:
        for i in json.load(open(out))["items"]: prev[i["slug"]] = i
    except Exception: pass
final = []
for i in items:
    if kind_f and i["kind"] != kind_f: continue
    if only and only not in i["slug"]: continue
    i["skill"] = deep if (i["kind"] == "engine" or i["lines"] >= short_lines) else short
    i["dir"] = os.path.join(outdir, i["slug"])
    old = prev.get(i["slug"], {})
    done_marker = os.path.join(i["dir"], "ENGINELOOP-DONE.txt")
    if os.path.exists(done_marker) and not rebuild:
        i["status"], i["note"] = "done", open(done_marker).read().strip()
    else:
        i["status"] = "pending"
        i["note"] = old.get("note", "") if old.get("status") != "done" else ""
    i["attempts"] = old.get("attempts", 0) if old.get("status") not in ("done", None) else 0
    final.append(i)
json.dump({"repo": repo, "items": final}, open(out, "w"), indent=1)
import collections; c = collections.Counter(i["status"] for i in final)
k = collections.Counter(i["kind"] for i in final); s = collections.Counter(i["skill"] for i in final)
print(f"queued {len(final)} films  {dict(k)}  {dict(s)}  {dict(c)}")
PY
}

claim(){
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do
    sleep 1; waited=$((waited+1)); (( waited > 120 )) && { say "stale lock after ${waited}s — clearing"; rm -rf "$LOCK"; }
  done
  python3 - "$QUEUE" "$WORKER" <<'PY'
import json, sys
p, w = sys.argv[1], sys.argv[2]
q = json.load(open(p))
for i in q["items"]:
    if i["status"] == "pending":
        i["status"], i["worker"] = "building", w
        json.dump(q, open(p, "w"), indent=1)
        print("\t".join([i["slug"], i["dir"], i["kind"], i["skill"], i["primary"], "|".join(i["sources"]), i["title"], str(i["lines"])]))
        break
PY
  rm -rf "$LOCK"
}

set_status(){  # slug status note
  local waited=0
  until mkdir "$LOCK" 2>/dev/null; do sleep 1; waited=$((waited+1)); (( waited > 120 )) && rm -rf "$LOCK"; done
  python3 - "$QUEUE" "$1" "$2" "${3:-}" "$MAX_ATTEMPTS" <<'PY'
import json, sys
p, s, st, note, mx = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
q = json.load(open(p))
for i in q["items"]:
    if i["slug"] == s:
        i["status"], i["note"] = st, note
        if st == "failed":
            i["attempts"] += 1
            if i["attempts"] < mx: i["status"] = "pending"
json.dump(q, open(p, "w"), indent=1)
PY
  rm -rf "$LOCK"
}

counts(){ python3 - "$QUEUE" <<'PY'
import json, sys, collections
q = json.load(open(sys.argv[1])); c = collections.Counter(i["status"] for i in q["items"])
print(" ".join(f"{k}={v}" for k, v in sorted(c.items())) or "empty")
PY
}

render_prompt(){  # $1 skill  $2 kind  $3 primary  $4 sources  $5 reel dir  $6 slug  $7 title
  sed -e "s#\$BRUTALIST_ART#$BRUTALIST_ART#g" -e "s#\$REPO#$REPO#g" -e "s#\$CHANNEL#$CHANNEL#g" \
      -e "s#\$SKILL#$1#g" -e "s#\$KIND#$2#g" -e "s#\$PRIMARY#$3#g" -e "s#\$SOURCES#$4#g" \
      -e "s#\$REEL_DIR#$5#g" -e "s#\$SLUG#$6#g" -e "s#\$TITLE#$7#g" -e "s#\$LINT#$HERE/narration_lint.py#g" "$PROMPT"
}

build_queue >/dev/null   # rescan every start: ENGINELOOP-DONE.txt markers on disk are the truth
say "repo: $REPO   out: $OUT_DIR"
say "deep: $DEEP_SKILL   short: $SHORT_SKILL (< $SHORT_LINES lines)   channel: $CHANNEL (Liam / Kokoro am_onyx)   pantry: OFF"
say "queue: $(counts)"

script_start=$(date +%s); attempted=0; done_count=0; failed_count=0; failures=()
print_summary(){
  say "SUMMARY: attempted=$attempted done=$done_count failed=$failed_count wall=$(( $(date +%s) - script_start ))s"
  local f; for f in "${failures[@]:-}"; do [[ -n "$f" ]] && say "  FAILED: $f"; done
  say "queue: $(counts)"
}

if (( DRY )); then
  say "DRY RUN — nothing is invoked, nothing is rendered, the queue is left untouched."
  python3 - "$QUEUE" "$N" <<'PY'
import json, sys
q, n = json.load(open(sys.argv[1])), int(sys.argv[2])
items = [i for i in q["items"] if i["status"] == "pending"]
if n > 0: items = items[:n]
for k, i in enumerate(items, 1):
    print(f"  {k:>2}. [{i['kind']:<6}] {i['skill']:<14} {i['lines']:>5} lines  {i['slug']}")
    print(f"        primary : {i['primary']}")
    print(f"        also    : {', '.join(s for s in i['sources'] if s != i['primary']) or '-'}")
print(f"\n  {len(items)} film(s) would be built. done already: {sum(1 for i in q['items'] if i['status']=='done')}")
PY
  exit 0
fi

consec_fail=0
while true; do
  IFS=$'\t' read -r slug d kind skill primary sources title lines < <(claim)
  if [[ -z "${slug:-}" ]]; then
    if (( FOREVER == 0 )); then say "queue drained."; print_summary; exit 0; fi
    say "queue drained. rescanning in 30m — new scripts and skills get picked up automatically."
    sleep 1800; build_queue >/dev/null; continue
  fi
  if [[ ! -f "$REPO/$primary" ]]; then
    set_status "$slug" "blocked" "primary source is gone — stale queue entry"; say "   SKIP $slug — $primary missing"; continue
  fi
  gb="$(free_gb)"
  if [[ "$gb" -lt "$MIN_FREE_GB" ]]; then
    say "PAUSED: only ${gb}GB free (need ${MIN_FREE_GB})."; set_status "$slug" "pending" "paused for disk"; sleep 600; continue
  fi
  timeout_s="$DEEP_TIMEOUT"; [[ "$skill" == "$SHORT_SKILL" ]] && timeout_s="$SHORT_TIMEOUT"
  say "── $slug   [$kind · $skill · $lines lines]  ← $primary   (free ${gb}GB, $(counts))"

  mkdir -p "$d"
  if (( REBUILD )); then
    n_old=$(find "$d" -maxdepth 1 -name '*.mp4' -print 2>/dev/null | wc -l | tr -d ' ')
    find "$d" -maxdepth 1 -name '*.mp4' -delete 2>/dev/null; rm -f "$d/ENGINELOOP-DONE.txt"
    say "   REBUILD — cleared $n_old prior cut(s)"
  fi
  start=$(date +%s); attempted=$((attempted+1))
  # Fresh context per film. --dangerously-skip-permissions is appropriate ONLY because every
  # output is regenerable from the source + beat sheet, and the prompt forbids writes to the repo source.
  ( cd "$BRUTALIST_ART" && \
    REPO="$REPO" REEL_DIR="$d" REEL_SLUG="$slug" PRIMARY="$primary" SOURCES="$sources" KIND="$kind" SKILL="$skill" \
    BRUTALIST_ART="$BRUTALIST_ART" BOOKLOOP_NO_PANTRY=1 \
    ${TIMEOUT_BIN:+$TIMEOUT_BIN "$timeout_s"} claude -p "$(render_prompt "$skill" "$kind" "$primary" "$sources" "$d" "$slug" "$title")

TARGET FOR THIS INVOCATION
  kind          : $kind
  skill         : $skill
  primary source: $REPO/$primary   ($lines lines)
  also read     : $(printf '%s' "$sources" | tr '|' '\n' | sed "s#^#$REPO/#" | tr '\n' ' ')
  reel folder   : $d
  slug          : $slug
  reel path relative to books/ (for ./brutalist-art/art): ${d#$BOOKS/}
Build this one film. When it is done or has failed, stop — the supervisor starts the next." \
      ${MODEL:+--model "$MODEL"} --dangerously-skip-permissions \
      </dev/null >>"$STATE/$slug.w$WORKER.out" 2>&1 )
  rc=$?; dur=$(( $(date +%s) - start ))
  cut="$(review_cut "$d" "$slug")"; ref="$(ref_file "$d" "$REPO/$primary")"

  if (( rc == 124 )); then
    note="claude invocation timed out after ${dur}s"
    set_status "$slug" "failed" "$note"; say "   FAILED — $note"
    consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
  else
    aud_rc=9; [[ -n "$cut" ]] && { audible "$cut"; aud_rc=$?; }
    if (( aud_rc == 2 )); then
      note="audio check TIMED OUT after ${AUDIBLE_TIMEOUT}s — reel skipped, loop kept moving"
      set_status "$slug" "failed" "$note"; say "   FAILED — $note"
      consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
    elif [[ -n "$cut" ]] && [[ "$cut" -nt "$ref" ]] && (( aud_rc == 0 )); then
      # No book title passed: the repo is public, naming it is fine. The HARD set
      # ("chapter", "the book", part numbers, course apparatus) still gates.
      lint_out="$(python3 "$HERE/narration_lint.py" "$d/beat_sheet.json" 2>&1)"; lint_rc=$?
      printf '%s\n' "$lint_out" | sed 's/^/     /' >>"$LOG"
      if (( lint_rc != 0 )); then
        note="narration names the book/chapter apparatus — not review-ready"
        set_status "$slug" "failed" "$note"; say "   FAILED — $note"
        printf '%s\n' "$lint_out" | grep -E '^  (HARD|soft)' | head -4 | sed 's/^/     /'
        consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: law")
      else
        printf '%s  %s  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$(basename "$cut")" "$skill · $kind · $primary" >"$d/ENGINELOOP-DONE.txt"
        rm -f "$d/$slug-slate.mp4" "$d"/media/_ext_*.mp4 2>/dev/null   # regenerable intermediates
        set_status "$slug" "done" "review-ready: $(basename "$cut") in ${dur}s"
        say "   DONE in ${dur}s — $(basename "$cut") (audible, law-clean)"; consec_fail=0; done_count=$((done_count+1))
      fi
    else
      if tail -c 400 "$STATE/$slug.w$WORKER.out" 2>/dev/null | grep -q "hit your session limit"; then
        set_status "$slug" "pending" "session limit hit — requeued"; say "   LIMIT — requeued $slug, sleeping 30m"; sleep 1800; continue
      fi
      if   [[ -n "$cut" ]] && (( aud_rc == 1 )); then note="cut exists but is SILENT — not review-ready"
      elif [[ -n "$cut" ]];                     then note="cut exists but is STALE (older than $(basename "$ref"))"
      elif (( rc == 0 ));                        then note="exit 0 but no review cut"
      else                                            note="claude exited $rc after ${dur}s"; fi
      set_status "$slug" "failed" "$note"; say "   FAILED after ${dur}s — $note (see $STATE/$slug.w$WORKER.out)"
      consec_fail=$((consec_fail+1)); failed_count=$((failed_count+1)); failures+=("$slug: $note")
    fi
  fi

  if (( NOHALT == 0 && consec_fail >= CONSEC_FAIL_STOP )); then
    say "HALT: $consec_fail films failed in a row — that is a systemic bug, not bad luck. Queue preserved at $QUEUE."
    print_summary; exit 1
  fi
  if (( N > 0 && attempted >= N )); then print_summary; exit 0; fi
  sleep "$COOLDOWN"
done
