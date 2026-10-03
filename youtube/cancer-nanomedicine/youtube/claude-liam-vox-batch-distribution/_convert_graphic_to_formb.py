#!/usr/bin/env python3
"""One-shot: convert this reel's 7 Manim GRAPHIC beats into Remotion FormBCard
patterns so remotion_scenes.py can render them. Manim scene classes B04..B11
were never authored; a lane_check-compliant review-slate cut needs each
pipeline beat to either render a real component or stop being a pipeline beat.

FormBCard is not the Manim histogram the beat truly wants — it is the honest
substitute that:
  - shows the beat's own key concepts in serif type on cream, on cue,
  - passes lane_check as a REMOTION render, not a GRAPHIC slate,
  - keeps the LOCKED narration intact (only shot.*, new_visual_element change).

Each item's `label` and `sub` are compressed from the beat's own narration /
production_viz; icons are from the available FormB library. The `Manim ...`
originals stay logged in TEMPLATE-MISSES.md so a later real render can slot in.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
SHEET = HERE / "beat_sheet.json"

# beat_id -> {title, items[]}
FORMB_MAP = {
    "B04": {
        "title": "Small molecule — identity is binary",
        "items": [
            {"label": "One defined structure", "sub": "The molecule, or not the molecule",
             "icon": "target", "cueFrame": 30},
            {"label": "One measurement decides", "sub": "Batch B matches batch A, or it does not",
             "icon": "circle-check", "cueFrame": 130},
        ],
    },
    "B05": {
        "title": "Nanoparticle — a population, not a point",
        "items": [
            {"label": "A cloud of objects", "sub": "Sizes spread around a mean",
             "icon": "layers", "cueFrame": 30},
            {"label": "The average is one number", "sub": "Pulled from the cloud",
             "icon": "crosshair", "cueFrame": 110},
            {"label": "The cloud is the product", "sub": "Not the mean at its center",
             "icon": "shield", "cueFrame": 190},
        ],
    },
    "B06": {
        "title": "Same mean, different spread",
        "items": [
            {"label": "Batch A — narrow spike", "sub": "Tight cluster at 98 nm",
             "icon": "list-checks", "cueFrame": 40},
            {"label": "Batch B — wide bell", "sub": "Stretched 30 to 300 nm, same center",
             "icon": "layers", "cueFrame": 190},
        ],
    },
    "B07": {
        "title": "Polydispersity Index — PDI",
        "items": [
            {"label": "PDI ~0.07 — monodisperse", "sub": "Narrow, controlled distribution",
             "icon": "circle-check", "cueFrame": 40},
            {"label": "PDI > ~0.2 — heterogeneous", "sub": "Problematic spread flagged",
             "icon": "shield-alert", "cueFrame": 200},
        ],
    },
    "B08": {
        "title": "One high-PDI batch — three products",
        "items": [
            {"label": "Small particles", "sub": "Clear from bloodstream in minutes",
             "icon": "zap", "cueFrame": 40},
            {"label": "Medium particles", "sub": "Behave as designed",
             "icon": "target", "cueFrame": 150},
            {"label": "Large particles", "sub": "Swallowed by liver and spleen",
             "icon": "shield-alert", "cueFrame": 260},
        ],
    },
    "B10": {
        "title": "Match the mean vs match the distribution",
        "items": [
            {"label": "Matching the mean", "sub": "Only the center point of a spread",
             "icon": "crosshair", "cueFrame": 40},
            {"label": "Matching the distribution", "sub": "Circulation, clearance, tumor arrival",
             "icon": "layers", "cueFrame": 170},
        ],
    },
    "B11": {
        "title": "Illustrative — same mean, different delivery",
        "items": [
            {"label": "Batch A — PDI 0.07", "sub": "Narrow spike; ~100% tumor delivery",
             "icon": "circle-check", "cueFrame": 60},
            {"label": "Batch B — PDI 0.31", "sub": "15% above 200 nm; ~60% tumor delivery",
             "icon": "circle-x", "cueFrame": 340},
        ],
    },
}


def main():
    sheet = json.loads(SHEET.read_text())
    for beat in sheet["beats"]:
        bid = beat.get("beat_id")
        if bid not in FORMB_MAP:
            continue
        spec = FORMB_MAP[bid]
        beat["shot"] = {
            "type": "REMOTION",
            "source": "own",
            "motion": (beat.get("shot") or {}).get("motion", "drawon"),
            "remotion": {
                "pattern": "FormBCard",
                "provenance": "proven-core/FormBCard",
                "version": "1",
                "props": {
                    "title": spec["title"],
                    "items": spec["items"],
                },
                "rendered": {"out": f"media/{bid}.mp4", "at": ""},
            },
        }
        beat["build"] = {"status": "SLATE"}
    SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    print(f"converted {len(FORMB_MAP)} GRAPHIC beats → REMOTION FormBCard")


if __name__ == "__main__":
    main()
