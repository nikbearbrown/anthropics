#!/usr/bin/env python3
"""Universal pass-2: voice + OUTRO dedup/fix + YOURTURN act/bid fix.

Handles the structural mess left by pass-1 patches:
- Original OUTRO (act="OUTRO", OutroSeries or no pattern) was not converted
- A second ClaudeTitleOutro OUTRO was appended
- A YOURTURN with act="CLOSE" was appended
This script normalises all of that without requiring new content authoring.
"""
import json, os, shutil, glob

BASE = "/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/youtube"

TOPICS = [
    "behind-the-model", "claude-agent-skills", "claude-basics",
    "claude-code", "claude-cowork", "claude-for-education",
    "claude-mcp-connectors", "claude-news", "claude-plugins",
    "claude-prompting", "claude-research", "claude-skills", "claude-youtube",
]

def fix_voice(meta):
    meta.pop("voice_id", None)
    # Unconditionally reset — fixes voice=NikBearBrown left by pass-1
    meta["engine"] = "kokoro"
    meta["voice"] = "am_onyx"
    meta["voice_kokoro"] = "am_onyx"

def is_outro(b):
    bid = b.get("beat_id", b.get("id",""))
    act = b.get("act","")
    scene = b.get("scene","")
    shot = b.get("shot") or {}
    rem = shot.get("remotion") if isinstance(shot,dict) else None
    if not isinstance(rem, dict): rem = {}
    pat = rem.get("pattern","")
    top_rem = b.get("remotion") or {}
    if not isinstance(top_rem, dict): top_rem = {}
    pat_top = top_rem.get("pattern","")
    return (
        act == "OUTRO" or "outro" in bid.lower()
        or "Outro" in pat or "Outro" in pat_top or "Outro" in scene
        or bid in ("OUTRO","BOUT")
    )

def get_outro_quality(b):
    """Returns (has_claudetitleoutro, has_title, has_mascotSeed)"""
    shot = b.get("shot") or {}
    rem = shot.get("remotion") if isinstance(shot,dict) else None
    if not isinstance(rem, dict): rem = {}
    pat = rem.get("pattern","")
    top_rem = b.get("remotion") or {}
    if not isinstance(top_rem, dict): top_rem = {}
    pat_top = top_rem.get("pattern","")

    for check_pat, check_rem in [(pat, rem), (pat_top, top_rem)]:
        if check_pat == "ClaudeTitleOutro":
            props = check_rem.get("props",{}) if isinstance(check_rem,dict) else {}
            return (True, bool(props.get("title")), bool(props.get("mascotSeed")))
    return (False, False, False)

def make_outro_beat(bid_val, title, slug):
    return {
        "beat_id": bid_val,
        "act": "OUTRO",
        "narration_text": f"{title}.",
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {"title": title, "handle": "@NikBearBrown", "mascotSeed": slug},
            },
        },
    }

def is_yourturn(b):
    bid = b.get("beat_id", b.get("id",""))
    act = b.get("act","").lower()
    shot = b.get("shot") or {}
    rem = shot.get("remotion") if isinstance(shot,dict) else None
    if not isinstance(rem, dict): rem = {}
    pat = rem.get("pattern","")
    narr = b.get("narration_text", b.get("narration","")) or ""
    # Strong signals
    if bid in ("YOURTURN","BHTF","H01"): return True
    if act in ("handoff","your-turn","close") and pat == "ClaudeComposerAsk": return True
    # ClaudeComposerAsk + "Your turn." in narration (not cold open)
    if pat == "ClaudeComposerAsk" and bid not in ("B00","B01") and "Your turn." in narr: return True
    return False

def has_valid_yourturn(b):
    bid = b.get("beat_id", b.get("id",""))
    act = b.get("act","").lower()
    shot = b.get("shot") or {}
    rem = shot.get("remotion") if isinstance(shot,dict) else None
    if not isinstance(rem, dict): rem = {}
    pat = rem.get("pattern","")
    narr = b.get("narration_text", b.get("narration","")) or ""
    props = rem.get("props",{}) if isinstance(rem,dict) else {}
    cmd = props.get("command","") or ""
    return (
        "Your turn." in narr and narr.strip() != "Your turn."
        and "[Your turn" not in narr
        and cmd and "[Your turn" not in cmd
        and pat == "ClaudeComposerAsk"
    )

def fix_beats(beats, title, slug):
    """
    1. Find all outro and yourturn beat indices.
    2. Keep the best outro (ClaudeTitleOutro preferred), update it, remove others.
    3. Keep the best yourturn (valid content), update its act/bid, ensure before outro.
    """
    outro_indices = [i for i, b in enumerate(beats) if is_outro(b)]
    yt_indices = [i for i, b in enumerate(beats) if is_yourturn(b)]

    # ── OUTRO ────────────────────────────────────────────────────────────────
    if not outro_indices:
        # Append a new OUTRO
        beats.append(make_outro_beat("OUTRO", title, slug))
        outro_idx = len(beats) - 1
    else:
        # Pick the best outro: prefer one with ClaudeTitleOutro props, else last one
        best_outro = outro_indices[-1]
        for i in outro_indices:
            q = get_outro_quality(beats[i])
            if q[0]:  # has ClaudeTitleOutro
                best_outro = i
                break

        # Remove all outros except best_outro
        for i in sorted(set(outro_indices) - {best_outro}, reverse=True):
            beats.pop(i)
            # Update indices after removal
            best_outro = best_outro if i > best_outro else best_outro - 1
            yt_indices = [x - (1 if i < x else 0) for x in yt_indices]

        # Now update the kept outro in-place
        b = beats[best_outro]
        if not isinstance(b.get("shot"), dict):
            b["shot"] = {}
        b["shot"]["type"] = "REMOTION"
        b["shot"]["source"] = "own"
        b["shot"]["remotion"] = {
            "pattern": "ClaudeTitleOutro",
            "props": {"title": title, "handle": "@NikBearBrown", "mascotSeed": slug},
        }
        b.pop("remotion", None)  # remove stale top-level remotion
        b["act"] = "OUTRO"
        outro_idx = best_outro

    # ── YOURTURN ─────────────────────────────────────────────────────────────
    valid_yt_indices = [i for i in yt_indices if has_valid_yourturn(beats[i])]

    if not valid_yt_indices:
        return  # No valid YOURTURN content — nothing to restructure here

    # Pick the valid YOURTURN (prefer one after content, before current outro)
    yt_idx = valid_yt_indices[0]
    for i in valid_yt_indices:
        if i < outro_idx:
            yt_idx = i
            break
    # If all valid YTs are after outro, use the first one
    if yt_idx > outro_idx:
        yt_idx = valid_yt_indices[0]

    # Remove all OTHER yourturn-like beats (keep only the valid one)
    remove_yt = sorted(
        [i for i in yt_indices if i != yt_idx], reverse=True
    )
    for i in remove_yt:
        beats.pop(i)
        if i < yt_idx: yt_idx -= 1
        if i < outro_idx: outro_idx -= 1

    # Update the kept YOURTURN
    b = beats[yt_idx]
    b["beat_id"] = "YOURTURN"
    b["act"] = "your-turn"
    shot = b.setdefault("shot", {})
    shot["type"] = "REMOTION"
    shot["source"] = "own"
    rem = shot.get("remotion") if isinstance(shot.get("remotion"), dict) else {}
    if not rem:
        rem = {}
    rem["pattern"] = "ClaudeComposerAsk"
    shot["remotion"] = rem
    b.pop("remotion", None)

    # Ensure YOURTURN is immediately before OUTRO
    if yt_idx != outro_idx - 1:
        yt_beat = beats.pop(yt_idx)
        if yt_idx < outro_idx:
            outro_idx -= 1
        beats.insert(outro_idx, yt_beat)


def needs_fix(path):
    d = json.load(open(path))
    meta = d.get("metadata", {})
    beats = d.get("beats", d.get("scenes", []))

    if "voice_id" in meta or meta.get("voice") == "NikBearBrown":
        return True

    outro_ok = False
    for b in beats:
        if is_outro(b):
            q = get_outro_quality(b)
            if q[0] and q[1] and q[2]:  # ClaudeTitleOutro + title + mascotSeed
                outro_ok = True
            break
    if not outro_ok:
        return True

    return False  # only voice+outro checked here; YT is content-dependent


fixed = 0
skipped = 0

all_paths = []
for topic in TOPICS:
    all_paths.extend(sorted(glob.glob(f"{BASE}/{topic}/*/beat_sheet.json")))

for path in all_paths:
    slug = os.path.basename(os.path.dirname(path))
    if slug.startswith("nbb-"):
        continue

    d = json.load(open(path))
    meta = d.get("metadata", {})
    title = meta.get("title", slug)
    beats = d.get("beats", d.get("scenes", []))

    voice_bad = "voice_id" in meta or meta.get("voice") == "NikBearBrown"

    # Check OUTRO
    outro_ok = False
    for b in beats:
        if is_outro(b):
            q = get_outro_quality(b)
            if q[0] and q[1] and q[2]:
                outro_ok = True
            break

    # Check YT structure
    valid_yt_exists = any(is_yourturn(b) and has_valid_yourturn(b) for b in beats)
    yt_has_wrong_structure = any(
        is_yourturn(b) and b.get("beat_id","") not in ("YOURTURN","BHTF","H01")
        and b.get("act","").lower() not in ("your-turn","handoff")
        for b in beats if is_yourturn(b)
    )
    multiple_outros = sum(1 for b in beats if is_outro(b)) > 1

    if not voice_bad and outro_ok and not yt_has_wrong_structure and not multiple_outros:
        skipped += 1
        continue

    bak = path + ".bak-pass2-v1"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)

    fix_voice(meta)
    fix_beats(beats, title, slug)

    with open(path, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

    fixed += 1
    print(f"FIXED: {os.path.basename(os.path.dirname(os.path.dirname(path)))}/{slug}")

print(f"\nDone. {fixed} fixed, {skipped} already OK.")
