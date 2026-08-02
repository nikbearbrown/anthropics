#!/usr/bin/env bash
# concat_full_course.sh — concat all claude-code-for-students chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/claude-code-for-students-ch01-chapter-1-the-homeworkquiz-gap-whats-act.mp4"
  "lectures/ch02-lecture/claude-code-for-students-ch02-chapter-2-what-youre-actually-good-at-an.mp4"
  "lectures/ch03-lecture/claude-code-for-students-ch03-chapter-3-the-teacher-student-ai-gap-why.mp4"
  "lectures/ch04-lecture/claude-code-for-students-ch04-chapter-4-conducting-not-prompting-the-c.mp4"
  "lectures/ch05-lecture/claude-code-for-students-ch05-chapter-5-the-five-supervisory-capacitie.mp4"
  "lectures/ch06-lecture/claude-code-for-students-ch06-chapter-6-gru-the-tool-built-for-this.mp4"
  "lectures/ch07-lecture/claude-code-for-students-ch07-chapter-7-the-software-design-document-b.mp4"
  "lectures/ch08-lecture/claude-code-for-students-ch08-chapter-8-writing-claude-prompts-that-ar.mp4"
  "lectures/ch09-lecture/claude-code-for-students-ch09-chapter-9-handoff-conditions-and-the-dan.mp4"
  "lectures/ch10-lecture/claude-code-for-students-ch10-chapter-10-brutalist-when-the-build-is-c.mp4"
  "lectures/ch11-lecture/claude-code-for-students-ch11-chapter-11-planning-your-first-boondoggl.mp4"
  "lectures/ch12-lecture/claude-code-for-students-ch12-chapter-12-running-the-build-claude-task.mp4"
  "lectures/ch13-lecture/claude-code-for-students-ch13-chapter-13-verification-how-you-know-it.mp4"
  "lectures/ch14-lecture/claude-code-for-students-ch14-chapter-14-your-first-full-build-from-pr.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/claude-code-for-students-full-course.mp4"

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
