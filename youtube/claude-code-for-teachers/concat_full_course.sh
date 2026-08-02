#!/usr/bin/env bash
# concat_full_course.sh — concat all claude-code-for-teachers chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/claude-code-for-teachers-ch01-chapter-0-introduction-the-line.mp4"
  "lectures/ch02-lecture/claude-code-for-teachers-ch02-chapter-1-your-first-terminal-session-cl.mp4"
  "lectures/ch03-lecture/claude-code-for-teachers-ch03-chapter-2-claudemd-your-coding-constitut.mp4"
  "lectures/ch04-lecture/claude-code-for-teachers-ch04-chapter-3-from-prompts-to-specifications.mp4"
  "lectures/ch05-lecture/claude-code-for-teachers-ch05-chapter-4-handoff-conditions-the-gate-be.mp4"
  "lectures/ch06-lecture/claude-code-for-teachers-ch06-chapter-5-the-five-supervisory-capacitie.mp4"
  "lectures/ch07-lecture/claude-code-for-teachers-ch07-chapter-6-skills-build-once-use-every-se.mp4"
  "lectures/ch08-lecture/claude-code-for-teachers-ch08-chapter-7-hooks-the-enforcement-layer.mp4"
  "lectures/ch09-lecture/claude-code-for-teachers-ch09-chapter-8-the-dangerous-middle-when-clau.mp4"
  "lectures/ch10-lecture/claude-code-for-teachers-ch10-chapter-9-subagents-keeping-the-build-cl.mp4"
  "lectures/ch11-lecture/claude-code-for-teachers-ch11-bridge-from-tools-that-save-time-to-tool.mp4"
  "lectures/ch12-lecture/claude-code-for-teachers-ch12-chapter-10-the-three-file-system-intent.mp4"
  "lectures/ch13-lecture/claude-code-for-teachers-ch13-chapter-11-building-the-simulation-condu.mp4"
  "lectures/ch14-lecture/claude-code-for-teachers-ch14-chapter-12-deploying-in-class-from-build.mp4"
  "lectures/ch15-lecture/claude-code-for-teachers-ch15-chapter-13-teaching-the-discipline-what.mp4"
  "lectures/ch16-lecture/claude-code-for-teachers-ch16-chapter-14-your-terminal-deliverable-the.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/claude-code-for-teachers-full-course.mp4"

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
