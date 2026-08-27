#!/usr/bin/env python3
"""fix_worklist_notes.py — Correct Gate-T=FAIL notes in OVERNIGHT-WORKLIST.json
for the 6 fixup reels whose Gate T was falsely logged as FAIL due to a bug in
rebuild_fixup.py's run_gate_t() (missing returncode fallback).

Reads each reel's TYPECHECK.md to get the actual verdict, then updates the note.
Run AFTER rebuild_fixup.py completes.
"""

import json
from pathlib import Path

BOOKS = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
WORKLIST_PATH = BOOKS / "anthropics/youtube/OVERNIGHT-WORKLIST.json"

FIXUP_DIRS = [
    "financial-services/youtube/claude-liam-client-review",
    "healthcare/youtube/claude-liam-clinical-trial-protocol-skill",
    "knowledge-work-plugins/youtube/claude-liam-close-management",
    "knowledge-work-plugins/youtube/claude-liam-close-month",
    "claude-for-legal/youtube/claude-liam-cocounsel-legal:deep-research",
    "knowledge-work-plugins/youtube/claude-liam-code-review",
]


def read_typecheck_verdict(reel_dir: Path) -> str:
    tc = reel_dir / "TYPECHECK.md"
    if not tc.exists():
        return "UNKNOWN"
    text = tc.read_text()
    if "Overall: PASS" in text or "Overall: **PASS**" in text:
        return "PASS"
    if "Overall: FAIL" in text or "Overall: **FAIL**" in text:
        return "FAIL"
    return "UNKNOWN"


def main():
    with open(WORKLIST_PATH) as f:
        data = json.load(f)

    changed = 0
    for reldir in FIXUP_DIRS:
        reel_dir = BOOKS / "anthropics" / reldir
        slug = reel_dir.name
        verdict = read_typecheck_verdict(reel_dir)

        for item in data["items"]:
            if item.get("dir") == reldir and item.get("tier") == 1:
                old_note = item.get("note", "")
                if "Gate-T=FAIL" in old_note or "Gate-T=UNKNOWN" in old_note:
                    # Find the mp4 name from the note if present
                    mp4_name = f"{slug}.mp4"
                    for mp4 in reel_dir.glob("*.mp4"):
                        mp4_name = mp4.name
                        break
                    item["note"] = f"fixup {mp4_name} Gate-T={verdict}"
                    print(f"  {slug}: {old_note!r} → Gate-T={verdict}")
                    changed += 1
                else:
                    print(f"  {slug}: note OK ({old_note!r})")
                break

    if changed:
        with open(WORKLIST_PATH, "w") as f:
            json.dump(data, f, indent=2)
        print(f"\nUpdated {changed} worklist entries.")
    else:
        print("\nNo entries needed correction.")

    # Print summary
    print("\n--- Fixup reel Gate T summary ---")
    for reldir in FIXUP_DIRS:
        reel_dir = BOOKS / "anthropics" / reldir
        slug = reel_dir.name
        verdict = read_typecheck_verdict(reel_dir)
        mp4s = list(reel_dir.glob("*.mp4"))
        mp4_info = f"{mp4s[0].name} ({mp4s[0].stat().st_size // 1024}K)" if mp4s else "NO MP4"
        print(f"  {slug}: {mp4_info} | Gate T: {verdict}")


if __name__ == "__main__":
    main()
