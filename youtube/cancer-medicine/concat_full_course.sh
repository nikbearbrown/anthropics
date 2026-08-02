#!/usr/bin/env bash
# concat_full_course.sh — concatenate all 11 Cancer Medicine chapter MP4s.
# Output: cancer-medicine/cancer-medicine-full-course.mp4
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/cancer-medicine-ch01-angiogenesis.mp4"
  "lectures/ch02-lecture/cancer-medicine-ch02-anti-angiogenic-therapy.mp4"
  "lectures/ch03-lecture/cancer-medicine-ch03-invasion.mp4"
  "lectures/ch04-lecture/cancer-medicine-ch04-metastasis.mp4"
  "lectures/ch05-lecture/cancer-medicine-ch05-tumor-microenvironment.mp4"
  "lectures/ch06-lecture/cancer-medicine-ch06-tme-signaling.mp4"
  "lectures/ch07-lecture/cancer-medicine-ch07-cancer-stem-cells.mp4"
  "lectures/ch08-lecture/cancer-medicine-ch08-tumor-heterogeneity.mp4"
  "lectures/ch09-lecture/cancer-medicine-ch09-tumor-immunology.mp4"
  "lectures/ch10-lecture/cancer-medicine-ch10-immunotherapy.mp4"
  "lectures/ch11-lecture/cancer-medicine-ch11-cancer-prevention.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/cancer-medicine-full-course.mp4"

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
