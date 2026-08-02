#!/usr/bin/env bash
# concat_full_course.sh — concatenate all 11 Cancer Research chapter MP4s.
# Output: cancer-research/cancer-research-full-course.mp4
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/cancer-research-ch01-cancer-screening.mp4"
  "lectures/ch02-lecture/cancer-research-ch02-cancer-diagnosis.mp4"
  "lectures/ch03-lecture/cancer-research-ch03-molecular-diagnostics.mp4"
  "lectures/ch04-lecture/cancer-research-ch04-therapy-principles.mp4"
  "lectures/ch05-lecture/cancer-research-ch05-precision-oncology.mp4"
  "lectures/ch06-lecture/cancer-research-ch06-surgical-oncology.mp4"
  "lectures/ch07-lecture/cancer-research-ch07-modern-surgical-oncology.mp4"
  "lectures/ch08-lecture/cancer-research-ch08-radiation-oncology.mp4"
  "lectures/ch09-lecture/cancer-research-ch09-modern-radiation-therapy.mp4"
  "lectures/ch10-lecture/cancer-research-ch10-chemotherapy-principles.mp4"
  "lectures/ch11-lecture/cancer-research-ch11-chemotherapy-pharmacology.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/cancer-research-full-course.mp4"

printf '' > "$LIST"
for ch in "${CHAPTERS[@]}"; do
  f="$HERE/$ch"
  if [[ ! -f "$f" ]]; then
    echo "[ERROR] missing: $f" >&2; exit 1
  fi
  printf "file '%s'\n" "$f" >> "$LIST"
done

echo "[concat] writing $OUT ..."
ffmpeg -y -f concat -safe 0 -i "$LIST" \
  -c:v copy -c:a aac -b:a 160k -movflags faststart "$OUT"
rm -f "$LIST"
echo "[ok] $(du -sh "$OUT" | cut -f1)  $OUT"
