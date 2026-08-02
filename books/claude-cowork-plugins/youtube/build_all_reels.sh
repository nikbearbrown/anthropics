#!/usr/bin/env bash
# build_all_reels.sh — render doodles + Remotion + compile for reels 2-14
set -e
BASE="$(cd "$(dirname "$0")" && pwd)"
BOOKS="$(cd "$BASE/../../../.." && pwd)"
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

echo "=== Full rebuild: doodles + Remotion + compile for reels 2-14 ==="
echo "Started: $(date)"

for slug in "${REELS[@]}"; do
  REEL="$BASE/$slug"
  echo ""
  echo "--- $slug ---"

  # 1. Render Manim doodle scenes for all VOX→MANIM beats
  mkdir -p "$REEL/manim"
  python3 -c "
import json, subprocess, sys
from pathlib import Path
reel = Path('$REEL')
bs = json.loads((reel / 'beat_sheet.json').read_text())
for b in bs['beats']:
    if b.get('engine') == 'manim':
        bid = b['beat_id']
        cls = (b.get('shot') or {}).get('manim', {}).get('scene_class', '')
        if not cls: continue
        out = reel / 'manim' / f'{bid}.mp4'
        if out.exists(): continue
        print(f'  [manim] {bid} ({cls})', flush=True)
        r = subprocess.run(
            ['manim', 'scenes.py', cls, '--output_file', f'{bid}.mp4',
             '--resolution', '1920,1080', '--fps', '24', '--format', 'mp4',
             '--media_dir', '/tmp/manim_cowork', '-q', 'h'],
            cwd=str(reel), capture_output=True, text=True)
        mp4 = next(Path('/tmp/manim_cowork').rglob(f'{bid}.mp4'), None)
        if mp4:
            import shutil; shutil.copy(mp4, out)
            print(f'    → manim/{bid}.mp4 ok', flush=True)
        else:
            print(f'    ✗ {bid} failed', flush=True)
            if r.stderr: print(r.stderr[-400:], flush=True)
"

  # 2. Remotion renders (skips already-filled beats)
  echo "  [remotion] rendering..."
  python3 "$RUNTIME/remotion_scenes.py" "$REEL"

  # 3. Compile previz
  echo "  [compile] building review cut..."
  python3 "$RUNTIME/compile.py" "$REEL" --review --force

  echo "  Done: $(date)"
done

echo ""
echo "=== All 13 reels rebuilt. ==="
