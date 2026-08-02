#!/usr/bin/env bash
# concat_full_course.sh — concat all claude chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/claude-ch01-chapter-1-the-work-chooses-the-tool.mp4"
  "lectures/ch02-lecture/claude-ch02-chapter-2-claude-ai-as-thinking-partner.mp4"
  "lectures/ch03-lecture/claude-ch03-chapter-3-prompting-as-specification.mp4"
  "lectures/ch04-lecture/claude-ch04-chapter-4-claude-code-as-engineering-par.mp4"
  "lectures/ch05-lecture/claude-ch05-chapter-5-claude-cowork-as-file-and-work.mp4"
  "lectures/ch06-lecture/claude-ch06-chapter-6-the-human-gate.mp4"
  "lectures/ch07-lecture/claude-ch07-chapter-7-research-writing-and-analysis.mp4"
  "lectures/ch08-lecture/claude-ch08-chapter-8-privacy-permissions-and-sensit.mp4"
  "lectures/ch09-lecture/claude-ch09-chapter-9-building-a-personal-claude-wor.mp4"
  "lectures/ch10-lecture/claude-ch10-chapter-10-capstone-one-project-three-cl.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/claude-full-course.mp4"

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
