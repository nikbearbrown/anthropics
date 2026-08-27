#!/usr/bin/env python3
"""
fix_bookends.py — Fix GATE BOOKEND issues in all tier-1 reels:
  1. BHTF topic must contain "YOUR TURN"
  2. BOUT subline must be empty ""

Reads OVERNIGHT-WORKLIST.json, processes all tier-1 reels.
"""
import json
import os
from pathlib import Path
from datetime import datetime

ROOT = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics")
WORKLIST = ROOT / "youtube" / "OVERNIGHT-WORKLIST.json"

def fix_reel(reel_dir: Path, slug: str) -> tuple[bool, str]:
    """Fix bookend props. Returns (success, note)."""
    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        return False, "beat_sheet.json missing"

    try:
        with open(bs_path) as f:
            bs = json.load(f)
    except Exception as e:
        return False, f"JSON error: {e}"

    changed = False
    notes = []

    for i, beat in enumerate(bs["beats"]):
        bid = beat["beat_id"]
        shot = beat.get("shot", {})

        if bid == "BHTF" and shot.get("type") == "REMOTION":
            props = shot.get("remotion", {}).get("props", {})
            topic = props.get("topic", "")
            if "YOUR TURN" not in topic.upper():
                # Add YOUR TURN to topic
                new_topic = topic + " · YOUR TURN"
                bs["beats"][i]["shot"]["remotion"]["props"]["topic"] = new_topic
                changed = True
                notes.append(f"BHTF topic: added YOUR TURN")

        elif bid == "BOUT" and shot.get("type") == "REMOTION":
            props = shot.get("remotion", {}).get("props", {})
            subline = props.get("subline", "")
            if subline != "":
                bs["beats"][i]["shot"]["remotion"]["props"]["subline"] = ""
                changed = True
                notes.append(f"BOUT subline: cleared '{subline[:30]}'")

    if changed:
        # Delete BHTF.mp4 and BOUT.mp4 to force re-render
        for mp4_name in ["BHTF.mp4", "BOUT.mp4"]:
            mp4 = reel_dir / "media" / mp4_name
            if mp4.exists():
                mp4.unlink()
                notes.append(f"deleted media/{mp4_name}")

        try:
            with open(bs_path, "w") as f:
                json.dump(bs, f, indent=1)
        except Exception as e:
            return False, f"Could not write: {e}"

    if not notes:
        return True, "no bookend changes needed"
    return True, "; ".join(notes)


def main():
    with open(WORKLIST) as f:
        data = json.load(f)

    tier1 = [x for x in data["items"] if x["tier"] == 1]
    print(f"Fixing bookends in {len(tier1)} tier-1 reels...")

    fixed = 0
    no_change = 0
    failed = 0

    for item in tier1:
        reel_dir = ROOT / item["dir"]
        if not reel_dir.exists():
            print(f"  [SKIP] {item['slug']} — dir not found")
            failed += 1
            continue

        ok, note = fix_reel(reel_dir, item["slug"])
        if ok:
            if "no bookend changes" in note:
                no_change += 1
                # Don't print these to keep output clean
            else:
                fixed += 1
                print(f"  [FIXED] {item['slug']} — {note}")
        else:
            failed += 1
            print(f"  [FAIL]  {item['slug']} — {note}")

    print(f"\nDone: {fixed} fixed, {no_change} no-change, {failed} failed")


if __name__ == "__main__":
    main()
