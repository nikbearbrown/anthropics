#!/usr/bin/env python3
"""render_scenes.py — render all GRAPHIC beat scenes → manim/<beat>.mp4."""
import subprocess, sys, shutil, pathlib

REEL = pathlib.Path(__file__).parent
SCENES_PY = REEL / "scenes.py"
OUT_MANIM = REEL / "manim"
TMP_MEDIA = REEL / "_manim_tmp"

BEAT_SCENE = [
    ("B02", "B02_LoadingLogic"),
    ("B04", "B04_DARScale"),
    ("B06", "B06_HydrophobicLoad"),
    ("B07", "B07_ClearanceTrap"),
    ("B09", "B09_OptimumCurve"),
    ("B10", "B10_ExamplePharma"),
]

OUT_MANIM.mkdir(exist_ok=True)
TMP_MEDIA.mkdir(exist_ok=True)

failed = []
for beat_id, scene_cls in BEAT_SCENE:
    dest = OUT_MANIM / f"{beat_id}.mp4"
    if dest.exists():
        print(f"[skip] {beat_id}.mp4 already exists")
        continue
    print(f"[render] {beat_id} ({scene_cls}) ...", flush=True)
    cmd = [
        "manim", "-ql", "--fps", "24",
        "--media_dir", str(TMP_MEDIA),
        str(SCENES_PY), scene_cls,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REEL))
    if r.returncode != 0:
        print(f"  FAIL\n{r.stderr[-2000:]}")
        failed.append(beat_id)
        continue
    candidates = list(TMP_MEDIA.rglob(f"{scene_cls}.mp4"))
    if not candidates:
        print(f"  FAIL - output not found after render")
        failed.append(beat_id)
        continue
    src = max(candidates, key=lambda p: p.stat().st_mtime)
    shutil.copy2(src, dest)
    print(f"  ok -> manim/{beat_id}.mp4")

if failed:
    print(f"\nFAILED: {failed}")
    sys.exit(1)
else:
    print(f"\nAll {len(BEAT_SCENE)} beats rendered.")
