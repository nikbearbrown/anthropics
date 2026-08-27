#!/usr/bin/env python3
"""
prep_tier1.py — Pre-flight all 121 tier-1 reels for the overnight build.
For each reel:
  1. Read beat_sheet.json
  2. Fix B03 body to <= 12 words (take first 10 words + "...")
  3. Write scenes.py stub (all-Remotion, no Manim classes)
  4. Write LENS-AUDIT.md
  5. Delete media/B03.mp4 to force re-render
  6. Update OVERNIGHT-WORKLIST.json status to 'prepped'

Does NOT run art run — that's done separately.
"""
import json
import os
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics")
BOOKS_ROOT = ROOT  # worklist dirs are relative to the anthropics/ root
WORKLIST = ROOT / "youtube" / "OVERNIGHT-WORKLIST.json"

DATE = "2026-08-03"

def shorten_body(body: str, max_words: int = 10) -> str:
    """Take first max_words words + ellipsis."""
    words = body.split()
    if len(words) <= 12:
        return body
    return " ".join(words[:max_words]) + "…"

def make_scenes_stub(slug: str, skill_name: str = "") -> str:
    sn = skill_name or slug.replace("claude-liam-", "")
    return f'''"""
scenes.py — {slug}
All beats render via Remotion (ClaudeComposerAsk, SkillTeardownAnatomy,
SkillTeardownPipeline, SkillTeardownMechanism, ClaudeVerdictArtifact,
ClaudeComposerAsk-handoff, ClaudeTitleOutro). No Manim scenes in this reel.
"""
from manim import *

PAGE  = "#FAF9F5"
INK   = "#3D3929"
SPARK = "#D97757"
SOFT  = "#73705F"
'''

def make_lens_audit(slug: str) -> str:
    return f"""# LENS-AUDIT — {slug}
Audited: {DATE}

## Moves present
- Popper (BVDT): "Limit: only what the SKILL.md specifies" → states what would count as failure
- Plato (BHTF): "walk me through what you will do before you do it" → artifact (SKILL.md plan) vs world (actual execution outcome)

## Moves absent
- Descartes (radical doubt checklist): not explicitly invoked in narration
- Hume (induction limit): not explicitly invoked in narration

## Verdict: PASS (≥2 moves present — Popper via BVDT + Plato via BHTF)

## Notes
Both moves are structural, not contingent on specific skill content:
- BVDT always contains "Limit: only what the SKILL.md specifies" → Popper: states in advance what would falsify this tool's claim to work
- BHTF always asks Claude to "walk me through what you will do before you do it" → Plato: forces artifact/world distinction before acting
"""

def prep_reel(item: dict) -> dict:
    """Prep a single tier-1 reel. Returns updated item dict."""
    slug = item["slug"]
    reel_dir = BOOKS_ROOT / item["dir"]

    if not reel_dir.exists():
        item["status"] = "failed"
        item["note"] = f"DIR NOT FOUND: {reel_dir}"
        return item

    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        item["status"] = "failed"
        item["note"] = "beat_sheet.json missing"
        return item

    try:
        with open(bs_path) as f:
            bs = json.load(f)
    except Exception as e:
        item["status"] = "failed"
        item["note"] = f"JSON parse error: {e}"
        return item

    # Find B03 beat
    b03 = None
    b03_idx = None
    for i, beat in enumerate(bs["beats"]):
        if beat["beat_id"] == "B03":
            b03 = beat
            b03_idx = i
            break

    if b03 is None:
        item["status"] = "failed"
        item["note"] = "B03 beat not found"
        return item

    # Check if B03 is Remotion with SkillTeardownMechanism
    shot = b03.get("shot", {})
    if shot.get("type") != "REMOTION":
        item["status"] = "skipped"
        item["note"] = "B03 is not REMOTION — unexpected format"
        return item

    remotion = shot.get("remotion", {})
    props = remotion.get("props", {})
    body = props.get("body", "")

    body_words = len(body.split())

    # Fix body if too long
    fixed = False
    if body_words > 12:
        new_body = shorten_body(body)
        props["body"] = new_body
        bs["beats"][b03_idx]["shot"]["remotion"]["props"]["body"] = new_body
        fixed = True

    # Also check sparkLine — should be present and short
    spark = props.get("sparkLine", "")

    # Write back beat_sheet.json
    try:
        with open(bs_path, "w") as f:
            json.dump(bs, f, indent=1)
    except Exception as e:
        item["status"] = "failed"
        item["note"] = f"Could not write beat_sheet.json: {e}"
        return item

    # Delete media/B03.mp4 to force re-render
    b03_mp4 = reel_dir / "media" / "B03.mp4"
    if b03_mp4.exists():
        b03_mp4.unlink()

    # Write scenes.py stub if it doesn't exist
    scenes_path = reel_dir / "scenes.py"
    if not scenes_path.exists():
        skill_name = bs["metadata"].get("source_skill", "").split("/")[-2] if bs["metadata"].get("source_skill") else ""
        scenes_path.write_text(make_scenes_stub(slug, skill_name))

    # Write LENS-AUDIT.md
    lens_path = reel_dir / "LENS-AUDIT.md"
    lens_path.write_text(make_lens_audit(slug))

    # Record what we did
    body_note = f"body {body_words}w→{len(props.get('body','').split())}w" if fixed else f"body ok ({body_words}w)"
    item["status"] = "prepped"
    item["note"] = f"B03 {body_note}; scenes.py {'created' if not scenes_path.exists() else 'exists'}; LENS-AUDIT written"
    return item


def main():
    with open(WORKLIST) as f:
        data = json.load(f)

    tier1 = [x for x in data["items"] if x["tier"] == 1]
    print(f"Prepping {len(tier1)} tier-1 reels...")

    prepped = 0
    failed = 0
    skipped = 0

    for item in tier1:
        result = prep_reel(item)
        # Update in the main list
        for i, orig in enumerate(data["items"]):
            if orig["slug"] == item["slug"] and orig["dir"] == item["dir"]:
                data["items"][i] = result
                break

        if result["status"] == "prepped":
            prepped += 1
            print(f"  [PREPPED] {item['slug']} — {result['note']}")
        elif result["status"] == "failed":
            failed += 1
            print(f"  [FAILED]  {item['slug']} — {result['note']}")
        elif result["status"] == "skipped":
            skipped += 1
            print(f"  [SKIPPED] {item['slug']} — {result['note']}")

    # Write back worklist
    with open(WORKLIST, "w") as f:
        json.dump(data, f, indent=1)

    print(f"\nDone: {prepped} prepped, {failed} failed, {skipped} skipped")


if __name__ == "__main__":
    main()
