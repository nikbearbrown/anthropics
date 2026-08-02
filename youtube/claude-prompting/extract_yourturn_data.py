#!/usr/bin/env python3
"""
Extract beat_sheet.json data for non-nbb slugs in claude-prompting/.
Outputs a Python dict-of-dicts for authoring YOURTURN prompts.
"""

import json
import os
import sys

BASE = "/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/youtube/claude-prompting"

results = {}

slugs = sorted(
    d for d in os.listdir(BASE)
    if not d.startswith("nbb-")
    and os.path.isdir(os.path.join(BASE, d))
    and os.path.isfile(os.path.join(BASE, d, "beat_sheet.json"))
)

for slug in slugs:
    path = os.path.join(BASE, slug, "beat_sheet.json")
    try:
        with open(path) as f:
            bs = json.load(f)
    except Exception as e:
        print(f"# ERROR reading {slug}: {e}", file=sys.stderr)
        continue

    meta = bs.get("metadata", {})
    beats = bs.get("beats", [])

    title = meta.get("title", "")
    voice_id_exists = "voice_id" in meta

    # B00: first beat
    b00_narration = ""
    if beats:
        b0 = beats[0]
        b00_narration = b0.get("narration") or b0.get("narration_text") or ""

    # YOURTURN beat
    yt_narration = ""
    for beat in beats:
        bid = beat.get("beat_id") or beat.get("id") or ""
        if bid == "YOURTURN":
            yt_narration = beat.get("narration") or beat.get("narration_text") or ""
            break

    # OUTRO beat — check shot.remotion.props.title
    outro_title_set = False
    for beat in beats:
        bid = beat.get("beat_id") or beat.get("id") or ""
        if bid == "OUTRO":
            shot = beat.get("shot", {})
            remotion = shot.get("remotion", {})
            props = remotion.get("props", {})
            outro_title_set = bool(props.get("title"))
            break

    results[slug] = {
        "title": title,
        "b00": b00_narration,
        "yt_narration": yt_narration,
        # bonus info (not in requested format but useful for patch script):
        "_voice_id_exists": voice_id_exists,
        "_outro_title_set": outro_title_set,
    }

# Print as Python dict-of-dicts
print("DATA = {")
for slug, d in results.items():
    print(f'    "{slug}": {{')
    print(f'        "title": {json.dumps(d["title"])},')
    print(f'        "b00": {json.dumps(d["b00"])},')
    print(f'        "yt_narration": {json.dumps(d["yt_narration"])},')
    print(f'        # _voice_id_exists={d["_voice_id_exists"]}, _outro_title_set={d["_outro_title_set"]}')
    print(f'    }},')
print("}")

print(f"\n# Total slugs: {len(results)}", file=sys.stderr)
print(f"# Has YOURTURN: {sum(1 for v in results.values() if v['yt_narration'])}", file=sys.stderr)
print(f"# Missing YOURTURN: {sum(1 for v in results.values() if not v['yt_narration'])}", file=sys.stderr)
