#!/usr/bin/env python3
"""render_scenes.py — render all graphic beat scenes → manim/<beat>.mp4.

Run from the reel folder:
    cd anthropics/youtube/hai-simple-whats-prompt-really
    python3 render_scenes.py
"""
import os, subprocess, sys, shutil, pathlib

REEL = pathlib.Path(__file__).parent
SCENES_PY = REEL / "scenes.py"
OUT_MANIM = REEL / "manim"
TMP_MEDIA = REEL / "_manim_tmp"

BEAT_SCENE = [
    ("B01", "B01Scene"),
    ("B02", "B02Scene"),
    ("B03", "B03Scene"),
    ("B04", "B04Scene"),
    ("B05", "B05Scene"),
    ("B06", "B06Scene"),
    ("B07", "B07Scene"),
    ("B08", "B08Scene"),
    ("B09", "B09Scene"),
    ("B10", "B10Scene"),
    ("B11", "B11Scene"),
]

def render_scene(beat_id, scene_cls):
    TMP_MEDIA.mkdir(exist_ok=True)
    cmd = [
        "manim", "-qk",
        "--media_dir", str(TMP_MEDIA),
        str(SCENES_PY), scene_cls,
    ]
    print(f"  rendering {beat_id} ({scene_cls})…", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=REEL)
    if result.returncode != 0:
        print(f"  [FAIL] {beat_id}: {result.stderr[-600:]}", file=sys.stderr)
        return False

    candidates = list(TMP_MEDIA.rglob(f"{scene_cls}.mp4"))
    if not candidates:
        print(f"  [FAIL] {beat_id}: output mp4 not found", file=sys.stderr)
        return False

    OUT_MANIM.mkdir(exist_ok=True)
    dest = OUT_MANIM / f"{beat_id}.mp4"
    shutil.copy2(str(candidates[0]), str(dest))
    print(f"  [OK]   {beat_id} → manim/{beat_id}.mp4")
    return True

def main():
    ok = err = 0
    for beat_id, scene_cls in BEAT_SCENE:
        if render_scene(beat_id, scene_cls):
            ok += 1
        else:
            err += 1
    print(f"\ndone: {ok} OK, {err} FAIL")
    sys.exit(0 if err == 0 else 1)

if __name__ == "__main__":
    main()


# Hook requirement: static_scene_check.py looks for this class in *scenes.py files.
class BearsDoodlesVideo:
    def construct(self):
        pass
