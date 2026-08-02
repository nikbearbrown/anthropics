#!/bin/bash
cd "$(dirname "$0")" || exit 1
EXCL="--exclude=*.mp3 --exclude=*.mp4 --exclude=*.mov --exclude=*.wav --exclude=*.m4a --exclude=*.webm --exclude=__pycache__ --exclude=node_modules --exclude=.git"
for pair in "claude-code-for-students:claude-code" "claude-code-for-teachers:claude-code" "claude-cowork:claude-cowork" "claude-for-education-a-practitioners-guide:claude-for-education" "claude-prompt-engineering:claude-prompting"; do
  book="${pair%%:*}"; cat="${pair##*:}"
  for d in ../../"$book"/youtube/*/; do
    [ -f "${d}beat_sheet.json" ] || continue
    slug="$(basename "$d")"
    mkdir -p "$cat/$slug"
    rsync -a --ignore-existing $EXCL "$d" "$cat/$slug/" 2>/dev/null
  done
done
echo "CLEAN COPY DONE" > _clean_copy.done
