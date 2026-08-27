#!/usr/bin/env bash
# render_scenes.sh — render all 16 GRAPHIC scenes and move to manim/
# Run from the reel folder:  bash render_scenes.sh
set -euo pipefail

REEL_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REEL_DIR"
mkdir -p manim

SCENES=(
  S01_VerdictCard
  S02_ThreeLockedOut
  S03_AnchorPlanted
  S04_WrongGuess
  S05_SplitPanel
  S06_HoldFrame
  S07_OneKeyTwoJobs
  S08_WriteThenRead
  S09_PublishBreaks
  S10_TesterVouched
  S11_OneFlag
  S12_ProbingInfers
  S13_WorstOfBoth
  S14_AnchorPayoff
  S15_DetectedLimits
  S16_NotDetectedLimits
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
  # Render at 1080p/24fps with claude palette
  ART_PALETTE=claude manim -qh --fps 24 scenes.py "$scene" 2>&1 | grep -v "SoX\|__init__\|sox\|proceed\|http://\|path var" || true

  # Find and move the output
  found=$(find media/videos -name "${scene}.mp4" 2>/dev/null | head -1)
  if [ -n "$found" ]; then
    mv "$found" "$dest"
    echo "       → moved to $dest"
  else
    echo "       [WARN] no output found for $scene — check above"
  fi
done

echo "Done. manim/ contents:"
ls -lh manim/
