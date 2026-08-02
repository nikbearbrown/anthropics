#!/usr/bin/env bash
# concat_full_course.sh — concat all claude-agentic-ai chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/claude-agentic-ai-ch01-chapter-1-chatbot-assistant-agent.mp4"
  "lectures/ch02-lecture/claude-agentic-ai-ch02-chapter-2-the-agentic-loop.mp4"
  "lectures/ch03-lecture/claude-agentic-ai-ch03-chapter-3-tools-permissions-and-the-acti.mp4"
  "lectures/ch04-lecture/claude-agentic-ai-ch04-chapter-4-claude-code-as-agentic-enginee.mp4"
  "lectures/ch05-lecture/claude-agentic-ai-ch05-chapter-5-claude-cowork-as-agentic-knowl.mp4"
  "lectures/ch06-lecture/claude-agentic-ai-ch06-chapter-6-mcp-and-external-capabilities.mp4"
  "lectures/ch07-lecture/claude-agentic-ai-ch07-chapter-7-planning-before-acting.mp4"
  "lectures/ch08-lecture/claude-agentic-ai-ch08-chapter-8-verification-is-the-control-sy.mp4"
  "lectures/ch09-lecture/claude-agentic-ai-ch09-chapter-9-failure-modes-of-agentic-work.mp4"
  "lectures/ch10-lecture/claude-agentic-ai-ch10-chapter-10-designing-human-approval-gate.mp4"
  "lectures/ch11-lecture/claude-agentic-ai-ch11-chapter-11-agentic-ai-in-teams-and-organ.mp4"
  "lectures/ch12-lecture/claude-agentic-ai-ch12-chapter-12-capstone-the-supervised-agent.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/claude-agentic-ai-full-course.mp4"

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
