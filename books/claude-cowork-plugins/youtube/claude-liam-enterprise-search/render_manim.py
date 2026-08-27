#!/usr/bin/env python3
"""Render all Manim scenes for claude-liam-enterprise-search.
Run from the reel directory. Outputs to media/ (scenes_std.py) and manim/ (scenes.py).
"""
import subprocess, sys, shutil, os, glob
from pathlib import Path

REEL = Path(__file__).parent
MANIM = shutil.which("manim") or "manim"

def render(file, scene, out_path):
    out_path = REEL / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    tmp_dir = REEL / "_manim_tmp"
    tmp_dir.mkdir(exist_ok=True)

    cmd = [MANIM, "render", str(REEL / file), scene, "-qm",
           "--media_dir", str(tmp_dir), "-v", "warning"]
    print(f"  rendering {scene} → {out_path.name}...", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  FAILED {scene}:\n{r.stderr[-600:]}")
        return False

    # Find the rendered mp4 in tmp_dir
    matches = list(tmp_dir.glob(f"**/{scene}.mp4"))
    if not matches:
        print(f"  WARN: rendered file not found for {scene}")
        return False

    shutil.copy2(matches[0], out_path)
    print(f"  OK {out_path.relative_to(REEL)}")
    return True


SCENES_STD = [
    ("scenes_std.py", "Scene_B02_ClaudeLiamEnterprise", "media/B02.mp4"),
    ("scenes_std.py", "Scene_B04_ClaudeLiamEnterprise", "media/B04.mp4"),
    ("scenes_std.py", "Scene_B08_ClaudeLiamEnterprise", "media/B08.mp4"),
    ("scenes_std.py", "Scene_B10_ClaudeLiamEnterprise", "media/B10.mp4"),
    ("scenes_std.py", "Scene_B16_ClaudeLiamEnterprise", "media/B16.mp4"),
    ("scenes_std.py", "Scene_B18_ClaudeLiamEnterprise", "media/B18.mp4"),
    ("scenes_std.py", "Scene_B19_ClaudeLiamEnterprise", "media/B19.mp4"),
    ("scenes_std.py", "Scene_B22_ClaudeLiamEnterprise", "media/B22.mp4"),
]

SCENES_DOODLE = [
    ("scenes.py", "B03Doodle", "manim/B03.mp4"),
    ("scenes.py", "B13Doodle", "manim/B13.mp4"),
    ("scenes.py", "B14Doodle", "manim/B14.mp4"),
    ("scenes.py", "B17Doodle", "manim/B17.mp4"),
    ("scenes.py", "B20Doodle", "manim/B20.mp4"),
    ("scenes.py", "B23Doodle", "manim/B23.mp4"),
]

ok, fail = 0, 0
os.chdir(REEL)
for file, scene, out in SCENES_STD + SCENES_DOODLE:
    if render(file, scene, out):
        ok += 1
    else:
        fail += 1

print(f"\nDone: {ok} OK, {fail} failed")
if fail:
    sys.exit(1)
