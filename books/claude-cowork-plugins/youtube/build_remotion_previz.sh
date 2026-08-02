#!/usr/bin/env bash
# build_remotion_previz.sh — Gate D1 previz for claude-cowork-plugins batch
# Run from books/ root. Renders Remotion beats then compiles previz for each reel.
# Renders are foreground + sequential per CLAUDE.md rules.

set -e
BASE="$(cd "$(dirname "$0")" && pwd)"
BOOKS="$(cd "$BASE/../../../.." && pwd)"  # books/ root
RUNTIME="$BOOKS/brutalist-art/runtime/scripts"

REELS=(
  "claude-liam-installing-plugins"
  "claude-liam-productivity"
  "claude-liam-marketing"
  "claude-liam-sales"
  "claude-liam-research"
  "claude-liam-data"
  "claude-liam-enterprise-search"
  "claude-liam-product"
  "claude-liam-support"
  "claude-liam-legal-finance"
  "claude-liam-building-plugins"
  "claude-liam-combining-plugins"
  "claude-liam-troubleshooting"
)

echo "=== Gate D1 Previz Batch — claude-cowork-plugins reels 2-14 ==="
echo "Started: $(date)"
echo ""

for slug in "${REELS[@]}"; do
  REEL_PATH="$BASE/$slug"
  echo "--- $slug ---"
  echo "  [1/2] Rendering Remotion beats..."
  python3 "$RUNTIME/remotion_scenes.py" "$REEL_PATH"
  echo "  [2/2] Compiling previz..."
  python3 "$RUNTIME/compile.py" "$REEL_PATH" --review
  echo "  Done: $(date)"
  echo ""
done

echo "=== All 13 reels compiled. Gate D1 complete. ==="
echo "Review cuts at: <slug>/mp4/<slug>-review.mp4"
