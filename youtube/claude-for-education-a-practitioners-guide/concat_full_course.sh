#!/usr/bin/env bash
# concat_full_course.sh — concat all claude-for-education-a-practitioners-guide chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/claude-for-education-a-practitioners-guide-ch01-chapter-1-what-claude-can-and-cannot-do.mp4"
  "lectures/ch02-lecture/claude-for-education-a-practitioners-guide-ch02-chapter-2-learning-outcomes-before-promp.mp4"
  "lectures/ch03-lecture/claude-for-education-a-practitioners-guide-ch03-chapter-3-prompting-claude-like-an-instr.mp4"
  "lectures/ch04-lecture/claude-for-education-a-practitioners-guide-ch04-chapter-4-lesson-planning-and-activity-d.mp4"
  "lectures/ch05-lecture/claude-for-education-a-practitioners-guide-ch05-chapter-5-feedback-that-teaches.mp4"
  "lectures/ch06-lecture/claude-for-education-a-practitioners-guide-ch06-chapter-6-differentiation-and-accessibil.mp4"
  "lectures/ch07-lecture/claude-for-education-a-practitioners-guide-ch07-chapter-7-rubrics-exemplars-and-criteria.mp4"
  "lectures/ch08-lecture/claude-for-education-a-practitioners-guide-ch08-chapter-8-assessment-in-the-age-of-claud.mp4"
  "lectures/ch09-lecture/claude-for-education-a-practitioners-guide-ch09-chapter-9-privacy-student-data-and-insti.mp4"
  "lectures/ch10-lecture/claude-for-education-a-practitioners-guide-ch10-chapter-10-student-use-from-ban-to-bound.mp4"
  "lectures/ch11-lecture/claude-for-education-a-practitioners-guide-ch11-chapter-11-research-advising-and-faculty.mp4"
  "lectures/ch12-lecture/claude-for-education-a-practitioners-guide-ch12-chapter-12-capstone-a-claude-supported-u.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/claude-for-education-a-practitioners-guide-full-course.mp4"

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
