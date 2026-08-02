#!/usr/bin/env bash
# concat_full_course.sh — concat all cancer-nanomedicine chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/cancer-nanomedicine-ch01-what-counts.mp4"
  "lectures/ch02-lecture/cancer-nanomedicine-ch02-transport-barriers.mp4"
  "lectures/ch03-lecture/cancer-nanomedicine-ch03-nanocarrier-platforms.mp4"
  "lectures/ch04-lecture/cancer-nanomedicine-ch04-targeting-epr-silent.mp4"
  "lectures/ch05-lecture/cancer-nanomedicine-ch05-antibody-drug-conjugates.mp4"
  "lectures/ch06-lecture/cancer-nanomedicine-ch06-nano-imaging.mp4"
  "lectures/ch07-lecture/cancer-nanomedicine-ch07-radioligand-theranostics.mp4"
  "lectures/ch08-lecture/cancer-nanomedicine-ch08-theranostic-nanoparticles.mp4"
  "lectures/ch09-lecture/cancer-nanomedicine-ch09-nucleic-acid-delivery.mp4"
  "lectures/ch10-lecture/cancer-nanomedicine-ch10-photodynamic-photothermal.mp4"
  "lectures/ch11-lecture/cancer-nanomedicine-ch11-characterization-manufacturing-silent.mp4"
  "lectures/ch12-lecture/cancer-nanomedicine-ch12-clinical-strategy.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/cancer-nanomedicine-full-course.mp4"

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
