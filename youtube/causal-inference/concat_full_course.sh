#!/usr/bin/env bash
# concat_full_course.sh — concatenate all 18 chapter MP4s.
# Output: Causal-Inference/Causal-Inference-full-course.mp4
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

CHAPTERS=(
  "lectures/ch02-lecture/Causal-Inference-ch02-chapter-scope.mp4"
  "lectures/ch02-lecture/Causal-Inference-ch02-the-language-of-causal-diagrams.mp4"
  "lectures/ch03-lecture/Causal-Inference-ch03-confounding-and-adjustment.mp4"
  "lectures/ch04-lecture/Causal-Inference-ch04-randomization-and-its-limits.mp4"
  "lectures/ch05-lecture/Causal-Inference-ch05-matching.mp4"
  "lectures/ch06-lecture/Causal-Inference-ch06-weighting-methods.mp4"
  "lectures/ch08-lecture/Causal-Inference-ch08-counterfactuals-and-mediation.mp4"
  "lectures/ch09-lecture/Causal-Inference-ch09-how-to-read-a-case-study.mp4"
  "lectures/ch10-lecture/Causal-Inference-ch10-chapter-llms-causal-reasoning.mp4"
  "lectures/ch11-lecture/Causal-Inference-ch11-chapter-sensitivity-analysis.mp4"
  "lectures/ch12-lecture/Causal-Inference-ch12-specification_bottleneck.mp4"
  "lectures/ch13-lecture/Causal-Inference-ch13-llm-causal-variable-identification.mp4"
  "lectures/ch20-lecture/Causal-Inference-ch20-case-counterfactuals-supply-chain.mp4"
  "lectures/ch21-lecture/Causal-Inference-ch21-case-llm-aegis-routing.mp4"
  "lectures/ch22-lecture/Causal-Inference-ch22-case-sensitivity-visamatch.mp4"
  "lectures/ch23-lecture/Causal-Inference-ch23-case-dag-ghosttrack-spotify.mp4"
  "lectures/ch24-lecture/Causal-Inference-ch24-case-agents-supply-chain-risk.mp4"
  "lectures/ch25-lecture/Causal-Inference-ch25-case-variables-brand-archetype.mp4"
)

LIST="$HERE/concat_list.txt"
OUT="$HERE/Causal-Inference-full-course.mp4"

printf '' > "$LIST"
for ch in "${CHAPTERS[@]}"; do
  f="$HERE/$ch"
  if [[ ! -f "$f" ]]; then
    echo "[SKIP] missing: $f" >&2; continue
  fi
  printf "file '%s'\n" "$f" >> "$LIST"
done

echo "[concat] writing $OUT ..."
ffmpeg -y -f concat -safe 0 -i "$LIST" \
  -c:v copy -c:a aac -b:a 160k -movflags faststart "$OUT"
rm -f "$LIST"
echo "[ok] $(du -sh "$OUT" | cut -f1)  $OUT"
