#!/usr/bin/env bash
# render_scenes.sh — render all 16 GRAPHIC scenes and move to manim/
# Run from the reel folder:  bash render_scenes.sh
set -euo pipefail

REEL_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REEL_DIR"
mkdir -p manim

SCENES=(
  S01_UndecidedGap
  S02_SafetyLean
  S03_AnchorPlanted
  S04_CoinFlipAssumption
  S05_AnchorFills
  S06_IdenticalBars
  S07_BarsAlone
  S08_CountAndEmptyAxis
  S09_IdenticalAboveUnlikeBelow
  S10_AxisBecomesTwo
  S11_ThreeTestsGranted
  S12_OneFlag
  S13_AnchorPayoff
  S14_CrowdAndOneWord
  S15_DirectionA
  S16_DirectionB
)

BEAT_IDS=(
  S01 S02 S03 S04 S05 S06 S07 S08 S09 S10 S11 S12 S13 S14 S15 S16
)

for i in "${!SCENES[@]}"; do
  scene="${SCENES[$i]}"
  bid="${BEAT_IDS[$i]}"
  dest="manim/${bid}.mp4"

  if [ -f "$dest" ]; then
    echo "[skip] $bid already exists"
    continue
  fi

  echo "[render] $scene → $dest"
  manim -qk --fps 24 scenes.py "$scene" 2>&1 \
    | grep -v "SoX\|__init__\|sox\|proceed\|http://\|path var\|sox.sourceforge" || true

  found=$(find media/videos -name "${scene}.mp4" 2>/dev/null | head -1)
  if [ -n "$found" ]; then
    mv "$found" "$dest"
    echo "       → $dest"
  else
    echo "       [WARN] no output for $scene"
  fi
done

echo ""
echo "Done. manim/ contents:"
ls -lh manim/
