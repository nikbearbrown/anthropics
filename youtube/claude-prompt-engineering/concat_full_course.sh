#!/usr/bin/env bash
# concat_full_course.sh — concat all claude-prompt-engineering chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/claude-prompt-engineering-ch01-chapter-1-anatomy-of-a-claude-prompt.mp4"
  "lectures/ch02-lecture/claude-prompt-engineering-ch02-chapter-2-context-what-claude-needs-and.mp4"
  "lectures/ch03-lecture/claude-prompt-engineering-ch03-chapter-3-constraints-and-boundaries.mp4"
  "lectures/ch04-lecture/claude-prompt-engineering-ch04-chapter-4-examples-counterexamples-and-s.mp4"
  "lectures/ch05-lecture/claude-prompt-engineering-ch05-chapter-5-evaluation-criteria-before-out.mp4"
  "lectures/ch06-lecture/claude-prompt-engineering-ch06-chapter-6-iteration-and-revision-loops.mp4"
  "lectures/ch07-lecture/claude-prompt-engineering-ch07-chapter-7-prompts-for-research-and-liter.mp4"
  "lectures/ch08-lecture/claude-prompt-engineering-ch08-chapter-8-prompts-for-writing-and-editin.mp4"
  "lectures/ch09-lecture/claude-prompt-engineering-ch09-chapter-9-prompts-for-data-and-analysis.mp4"
  "lectures/ch10-lecture/claude-prompt-engineering-ch10-chapter-10-prompts-for-teaching-and-lear.mp4"
  "lectures/ch11-lecture/claude-prompt-engineering-ch11-chapter-11-prompts-as-handoffs-to-claude.mp4"
  "lectures/ch12-lecture/claude-prompt-engineering-ch12-chapter-12-building-a-reusable-prompt-li.mp4"
  "lectures/ch13-lecture/claude-prompt-engineering-ch13-chapter-13-capstone-one-workflow-three-p.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/claude-prompt-engineering-full-course.mp4"

printf '' > "$LIST"
for ch in "${CHAPTERS[@]}"; do
  f="$HERE/$ch"
  if [[ ! -f "$f" ]]; then echo "[ERROR] missing: $f" >&2; exit 1; fi
  printf "file '%s'\n" "$f" >> "$LIST"
done

echo "[concat] writing $OUT ..."
ffmpeg -y -f concat -safe 0 -i "$LIST" \
  -c:v copy -c:a aac -b:a 128k -movflags faststart "$OUT"
rm -f "$LIST"
echo "[ok] $(du -sh "$OUT" | cut -f1)  $OUT"
