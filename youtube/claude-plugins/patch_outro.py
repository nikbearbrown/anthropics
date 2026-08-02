#!/usr/bin/env python3
"""Fix 5 claude-plugins failures: OUTRO props + stale top-level subline."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def fix_seven_surfaces():
    path = os.path.join(BASE, "claude-code-plugin-seven-surfaces", "beat_sheet.json")
    bak = path + ".bak-outro-v1"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    with open(path) as f:
        d = json.load(f)
    beats = d.get("beats", d.get("scenes", []))
    for beat in beats:
        bid = beat.get("id", beat.get("beat_id", ""))
        if bid == "OUTRO":
            beat["shot"] = {
                "type": "REMOTION",
                "source": "own",
                "remotion": {
                    "pattern": "ClaudeTitleOutro",
                    "props": {
                        "title": "Seven Surfaces, One Manifest",
                        "handle": "@NikBearBrown",
                        "mascotSeed": "claude-code-plugin-seven-surfaces"
                    }
                }
            }
            beat["build"]["note"] = "design-v1: remotion props added"
            break
    with open(path, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"FIXED (OUTRO props): claude-code-plugin-seven-surfaces")

def strip_toplevel_subline(slug):
    path = os.path.join(BASE, slug, "beat_sheet.json")
    bak = path + ".bak-outro-v1"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    with open(path) as f:
        d = json.load(f)
    beats = d.get("beats", d.get("scenes", []))
    fixed = 0
    for beat in beats:
        top_props = beat.get("props", {})
        if "subline" in top_props:
            del top_props["subline"]
            fixed += 1
    with open(path, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"FIXED (subline removed from {fixed} beat props): {slug}")

fix_seven_surfaces()
for slug in [
    "claude-liam-building-plugins",
    "claude-liam-combining-plugins",
    "claude-liam-installing-plugins",
    "claude-liam-what-plugins-are",
]:
    strip_toplevel_subline(slug)

print("\nDone.")
