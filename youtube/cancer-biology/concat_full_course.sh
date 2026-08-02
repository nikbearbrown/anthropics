#!/usr/bin/env bash
# concat_full_course.sh — concat all cancer-biology chapter MP4s
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch01-lecture/cancer-biology-ch01-chapter-1-the-building-blocks-of-life-no.mp4"
  "lectures/ch02-lecture/cancer-biology-ch02-chapter-2-introduction-to-cancer-a-disea.mp4"
  "lectures/ch03-lecture/cancer-biology-ch03-chapter-3-cancer-epidemiology-and-risk-f.mp4"
  "lectures/ch04-lecture/cancer-biology-ch04-chapter-4-genetics-and-genomic-instabili.mp4"
  "lectures/ch05-lecture/cancer-biology-ch05-chapter-5-oncogenes.mp4"
  "lectures/ch06-lecture/cancer-biology-ch06-chapter-6-tumor-suppressor-genes.mp4"
  "lectures/ch07-lecture/cancer-biology-ch07-chapter-7-epigenetics-in-cancer-the-meth.mp4"
  "lectures/ch08-lecture/cancer-biology-ch08-chapter-8-epigenetics-in-cancer-noncodin.mp4"
  "lectures/ch09-lecture/cancer-biology-ch09-chapter-9-cancer-etiology-chemical-and-r.mp4"
  "lectures/ch10-lecture/cancer-biology-ch10-chapter-10-cancer-etiology-viral-and-bac.mp4"
  "lectures/ch11-lecture/cancer-biology-ch11-chapter-11-cell-cycle-control-and-cancer.mp4"
  "lectures/ch12-lecture/cancer-biology-ch12-chapter-12-cell-cycle-control-and-cancer.mp4"
  "lectures/ch13-lecture/cancer-biology-ch13-chapter-13-apoptosis-in-cancer-the-death.mp4"
  "lectures/ch14-lecture/cancer-biology-ch14-chapter-14-apoptosis-in-cancer-evasion-a.mp4"
  "lectures/ch15-lecture/cancer-biology-ch15-chapter-15-cancer-metabolism-the-warburg.mp4"
  "lectures/ch16-lecture/cancer-biology-ch16-chapter-16-cancer-metabolism-lipids-amin.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/cancer-biology-full-course.mp4"

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
