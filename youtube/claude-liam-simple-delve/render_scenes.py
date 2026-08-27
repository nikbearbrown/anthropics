#!/usr/bin/env python3
"""render_scenes.py — render all graphic beat scenes → manim/<beat>.mp4.

Run from the reel folder:
    cd anthropics/youtube/claude-liam-simple-delve
    python3 render_scenes.py
"""
import os, subprocess, sys, shutil, pathlib

REEL = pathlib.Path(__file__).parent
SCENES_PY = REEL / "scenes.py"
OUT_MANIM = REEL / "manim"
TMP_MEDIA = REEL / "_manim_tmp"

BEAT_SCENE = [
    ("S01", "S01Scene"),
    ("S02", "S02Scene"),
    ("S03", "S03Scene"),
    ("S04", "S04Scene"),
    ("S05", "S05Scene"),
    ("S06", "S06Scene"),
    ("S07", "S07Scene"),
    ("S08", "S08Scene"),
    ("S09", "S09Scene"),
    ("S10", "S10Scene"),
    ("S11", "S11Scene"),
    ("S12", "S12Scene"),
    ("S13", "S13Scene"),
    ("S14", "S14Scene"),
    ("S15", "S15Scene"),
    ("S16", "S16Scene"),
]

OUT_MANIM.mkdir(exist_ok=True)
TMP_MEDIA.mkdir(exist_ok=True)

failed = []
for beat_id, scene_cls in BEAT_SCENE:
    dest = OUT_MANIM / f"{beat_id}.mp4"
    if dest.exists():
        print(f"[skip] {beat_id}.mp4 already exists")
        continue

    print(f"[render] {beat_id} ({scene_cls}) …", flush=True)
    cmd = [
        "manim", "-qk", "--fps", "24",
        "--media_dir", str(TMP_MEDIA),
        str(SCENES_PY), scene_cls,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REEL))
    if r.returncode != 0:
        print(f"  FAIL\n{r.stderr[-2000:]}")
        failed.append(beat_id)
        continue

    # Manim writes to TMP_MEDIA/videos/scenes/1080p24/<Scene>.mp4
    candidates = list(TMP_MEDIA.rglob(f"{scene_cls}.mp4"))
    if not candidates:
        print(f"  FAIL — output not found after render")
        failed.append(beat_id)
        continue

    src = max(candidates, key=lambda p: p.stat().st_mtime)
    shutil.copy2(src, dest)
    print(f"  ok → manim/{beat_id}.mp4")

if failed:
    print(f"\nFAILED: {failed}")
    sys.exit(1)
else:
    print(f"\nAll {len(BEAT_SCENE)} beats rendered.")
