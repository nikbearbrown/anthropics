#!/usr/bin/env python3
"""
batch_design_v1.py — Design-system conversion batch (GATE P: JSON edits only)

Applies design-v1 fixes to all in-scope claude-liam / NikBearBrown / am_onyx reels
across the 11 topic directories under books/anthropics/youtube/.

Fixes:
  1. OUTRO violations (subline removal, title match, handle, mascotSeed)
  2. Gen-AI VOX beats → Form A CARD
  3. Missing OUTRO → append new OUTRO beat
  4. Missing YOURTURN (when OUTRO also missing) → insert before OUTRO
  5. Metadata: design_version, voice, voice_kokoro
"""

import json
import os
import shutil
import glob
from pathlib import Path
from datetime import datetime

# ─── Constants ────────────────────────────────────────────────────────────────
BASE = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/youtube")

TOPICS_ORDER = [
    "claude-research",
    "claude-mcp-connectors",
    "claude-basics",
    "claude-skills",
    "claude-agent-skills",
    "claude-plugins",
    "claude-for-education",
    "behind-the-model",
    "claude-prompting",
    "claude-cowork",
    "claude-code",
]

PILOT_REELS = {
    "behind-the-model/claude-constitution-corrigibility-dial",
    "claude-code/claude-api-one-endpoint-ladder",
    "behind-the-model/what-is-behind-the-model",
    "claude-agent-skills/agent-decomposition-skills-vs-tools",
    "claude-news/claude-liam-claude-opus-4-5-migration",
    "claude-cowork/claude-liam-access-ladder-explained",
    "claude-prompting/claude-liam-agentic-approval-gate",
    "claude-basics/anthropic-retrieval-demo-wrapping-same-text-xml-changes",
}

BACKUP_SUFFIX = ".bak-design-v1"

# ─── Helper: detect beat ID field ─────────────────────────────────────────────
def get_bid(beat):
    """Return the beat's ID, using beat_id if present, else id."""
    return beat.get("beat_id", beat.get("id", ""))

def bid_key(beats):
    """Return 'beat_id' if that field is used, else 'id'."""
    if beats and "beat_id" in beats[0]:
        return "beat_id"
    return "id"


# ─── Helper: is beat an OUTRO? ─────────────────────────────────────────────
def is_outro(beat):
    bid = str(get_bid(beat)).upper()
    act = str(beat.get("act", "")).lower()
    shot = beat.get("shot", {})
    pattern = ""
    if isinstance(shot, dict):
        pattern = shot.get("remotion", {}).get("pattern", "") if isinstance(shot.get("remotion", {}), dict) else ""
    scene = str(beat.get("scene", ""))
    return (
        "OUTRO" in bid
        or "outro" in act
        or pattern == "ClaudeTitleOutro"
        or scene == "ClaudeTitleOutro"
    )


# ─── Helper: is beat a YOURTURN? ──────────────────────────────────────────
def is_yourturn(beat):
    bid = str(get_bid(beat)).upper()
    act = str(beat.get("act", "")).lower()
    return "YOURTURN" in bid or "your-turn" in act or "your_turn" in act


# ─── Scope check ──────────────────────────────────────────────────────────────
def is_in_scope(slug, metadata):
    """Return (in_scope: bool, reason: str)"""
    # nbb- prefix → skip
    if slug.startswith("nbb-"):
        return False, "nbb- prefix"

    # Bear's ElevenLabs clone
    if metadata.get("voice") == "NikBearBrown" and metadata.get("voice_id"):
        return False, "Bear ElevenLabs clone"

    # IN scope if:
    ch = metadata.get("channel", "").lower()
    voice = metadata.get("voice", "")
    voice_kokoro = metadata.get("voice_kokoro", "")
    if (
        slug.startswith("claude-liam-")
        or ch in ("nikbearbrown", "claude-liam")
        or voice == "am_onyx"
        or voice_kokoro == "am_onyx"
    ):
        return True, "in-scope"

    return False, "not claude-liam / NikBearBrown / am_onyx"


# ─── Check for exhibit media on disk ──────────────────────────────────────────
def has_exhibit_clip(reel_dir, beat):
    """Return True if a real rendered clip exists for this beat."""
    bid = get_bid(beat)
    media_path = reel_dir / "media" / f"{bid}.mp4"
    return media_path.exists()


# ─── Fix 1: OUTRO violations ──────────────────────────────────────────────────
def fix_outro(beat, title, slug):
    """
    Fix violations in a ClaudeTitleOutro beat.
    Returns list of fix labels applied (empty = no change).
    """
    shot = beat.get("shot", {})
    if not isinstance(shot, dict):
        return []

    remotion = shot.get("remotion", {})
    if not isinstance(remotion, dict):
        # Old-style beat with no remotion props — inject remotion block
        props = {
            "title": title,
            "handle": "@NikBearBrown",
            "mascotSeed": slug,
        }
        shot["remotion"] = {"pattern": "ClaudeTitleOutro", "props": props}
        shot.pop("type", None)
        shot["type"] = "REMOTION"
        shot.pop("source", None)
        shot["source"] = "own"
        beat["shot"] = shot
        beat["build"] = {"status": "SLATE", "src": None, "note": "design-v1: OUTRO props injected"}
        return ["outro-props-injected"]

    props = remotion.get("props", {})
    if not isinstance(props, dict):
        props = {}
        remotion["props"] = props

    fixes = []

    # Remove banned subline
    if "subline" in props:
        del props["subline"]
        fixes.append("subline-removed")

    # Fix title to match metadata.title
    if props.get("title") != title:
        props["title"] = title
        fixes.append("title-fixed")

    # Fix handle
    if props.get("handle") != "@NikBearBrown":
        props["handle"] = "@NikBearBrown"
        fixes.append("handle-fixed")

    # Add mascotSeed if missing
    if "mascotSeed" not in props:
        props["mascotSeed"] = slug
        fixes.append("mascotSeed-added")

    # If any prop changed, mark beat as SLATE
    if fixes:
        beat["build"] = {"status": "SLATE", "src": None, "note": "design-v1: " + ",".join(fixes)}

    return fixes


# ─── Fix 2: Gen-AI VOX → Form A CARD ─────────────────────────────────────────
def fix_ai_shot(beat, reel_dir, stop_list, topic, slug):
    """
    Replace ai-source shot with Form A CARD.
    Returns list of fix labels, or empty if no change needed.
    Updates stop_list if beat has no usable narration.
    """
    shot = beat.get("shot", {})
    if not isinstance(shot, dict):
        return []
    if shot.get("source") != "ai":
        return []

    bid = get_bid(beat)

    # Check exhibit: if real clip on disk, leave it alone
    if has_exhibit_clip(reel_dir, beat):
        return [f"EXHIBIT-PRESENT:{bid}"]

    # Get narration text
    narration = beat.get("narration_text") or beat.get("narration") or ""
    if narration == "[seed]" or not narration.strip():
        act_label = beat.get("act", bid)
        # Check if there's truly no narration content
        if not act_label or act_label.strip() == "[seed]":
            stop_list.append({
                "reel": f"{topic}/{slug}",
                "beat": bid,
                "reason": "ai-only beat with no narration — cannot auto-convert to FormA",
            })
            return []
        narration = act_label

    # Build Form A CARD shot
    new_shot = {
        "type": "CARD",
        "source": "own",
        "form": "A",
        "polarity": "light",
        "card": {
            "kind": "text-only",
            "typography": "EB Garamond",
            "ground": "#FAF9F5",
            "ink": "#3D3929",
            "copy": narration.strip(),
        },
    }
    beat["shot"] = new_shot

    # Set lane and form on beat
    if "lane" in beat:
        beat["lane"] = "CARD"
    if "form" in beat:
        beat["form"] = "A"

    # Update build status
    beat["build"] = {"status": "SLATE", "src": None, "note": "design-v1: ai→FormA"}

    return ["ai→FormA"]


# ─── Fix 3: Missing OUTRO — append ────────────────────────────────────────────
def add_outro(beats, title, slug, id_field):
    """Append a new OUTRO beat."""
    new_beat = {
        id_field: "OUTRO",
        "act": "outro",
        "narration_text": title,
        "voice": "am_onyx",
        "engine": "kokoro",
        "estimated_duration_s": 6,
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": title,
                    "handle": "@NikBearBrown",
                    "mascotSeed": slug,
                },
            },
        },
        "build": {"status": "SLATE", "src": None, "note": "design-v1: OUTRO added"},
        "design_version": "v1",
    }
    beats.append(new_beat)
    return ["OUTRO-added"]


# ─── Fix 4: Missing YOURTURN — insert before OUTRO ────────────────────────────
def add_yourturn(beats, title, slug, topic, id_field, b00_command):
    """Insert YOURTURN beat before the OUTRO."""
    # Resolve command
    command = b00_command or "[Your turn — paste the cold-open question here]"
    topic_field = f"CLAUDE · {topic.upper().replace('-', ' ')}"

    new_beat = {
        id_field: "YOURTURN",
        "act": "your-turn",
        "narration_text": f"Your turn. {command}",
        "voice": "am_onyx",
        "engine": "kokoro",
        "estimated_duration_s": 12,
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": topic_field,
                    "command": command,
                    "runningText": "paste this into Claude…",
                    "folderLabel": "@NikBearBrown",
                },
            },
        },
        "build": {"status": "SLATE", "src": None, "note": "design-v1: YOURTURN added"},
        "design_version": "v1",
    }

    # Find OUTRO index and insert before it
    outro_idx = None
    for i, b in enumerate(beats):
        if is_outro(b):
            outro_idx = i
            break

    if outro_idx is not None:
        beats.insert(outro_idx, new_beat)
    else:
        beats.append(new_beat)

    return ["YOURTURN-added"]


# ─── Extract B00 command ───────────────────────────────────────────────────────
def extract_b00_command(beats):
    """Pull command from B00 ClaudeComposerAsk props if present."""
    for b in beats:
        bid = get_bid(b)
        if str(bid) in ("B00", "b00", "0"):
            shot = b.get("shot", {})
            if isinstance(shot, dict):
                props = shot.get("remotion", {}).get("props", {})
                if isinstance(props, dict) and props.get("command"):
                    return props["command"]
            # Also check top-level props
            if b.get("props", {}).get("command"):
                return b["props"]["command"]
    return None


# ─── Process one reel ─────────────────────────────────────────────────────────
def process_reel(topic, slug, reel_dir, stop_list, form_a_count):
    """
    Apply all fixes to a single reel.
    Returns dict with fix summary.
    """
    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        return None  # Skip

    # Load
    try:
        with open(bs_path) as f:
            data = json.load(f)
    except Exception as e:
        return {"slug": slug, "error": str(e), "fixes": [], "skipped": True}

    metadata = data.get("metadata", {})
    beats = data.get("beats", [])
    title = metadata.get("title", slug)
    id_field = bid_key(beats)
    all_fixes = []

    # Backup
    bak_path = bs_path.parent / (bs_path.name + BACKUP_SUFFIX)
    if not bak_path.exists():
        shutil.copy2(bs_path, bak_path)

    # Scan for OUTRO and YOURTURN presence
    has_outro = any(is_outro(b) for b in beats)
    has_yourturn = any(is_yourturn(b) for b in beats)

    # Fix 2: Gen-AI → FormA
    for beat in beats:
        shot = beat.get("shot", {})
        if isinstance(shot, dict) and shot.get("source") == "ai":
            fixes = fix_ai_shot(beat, reel_dir, stop_list, topic, slug)
            for f in fixes:
                if f.startswith("EXHIBIT-PRESENT"):
                    all_fixes.append(f)
                elif f == "ai→FormA":
                    all_fixes.append("ai→FormA")
                    form_a_count[0] += 1

    # Fix 1: OUTRO violations (after the ai pass, so OUTRO beat is current)
    for beat in beats:
        if is_outro(beat):
            fixes = fix_outro(beat, title, slug)
            all_fixes.extend(fixes)

    # Fix 3: Missing OUTRO
    if not has_outro:
        fixes = add_outro(beats, title, slug, id_field)
        all_fixes.extend(fixes)

    # Fix 4: Missing YOURTURN (only when OUTRO was also missing)
    if not has_outro and not has_yourturn:
        b00_cmd = extract_b00_command(beats)
        fixes = add_yourturn(beats, title, slug, topic, id_field, b00_cmd)
        all_fixes.extend(fixes)

    # Fix 5: Metadata
    meta_fixes = []
    if metadata.get("design_version") != "v1":
        metadata["design_version"] = "v1"
        meta_fixes.append("design_version=v1")
    if metadata.get("voice") != "am_onyx":
        metadata["voice"] = "am_onyx"
        meta_fixes.append("voice=am_onyx")
    if metadata.get("voice_kokoro") != "am_onyx":
        metadata["voice_kokoro"] = "am_onyx"
        meta_fixes.append("voice_kokoro=am_onyx")
    all_fixes.extend(meta_fixes)

    # Write if anything changed
    if all_fixes:
        data["metadata"] = metadata
        data["beats"] = beats
        with open(bs_path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    return {
        "slug": slug,
        "fixes": all_fixes,
        "skipped": False,
    }


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    stop_list = []
    form_a_count = [0]  # mutable for nested fn
    report_lines = []
    topic_summaries = {}

    total_processed = 0
    total_skipped = 0
    skip_detail = {}

    all_reel_lines = []  # per-reel one-liners for report

    for topic in TOPICS_ORDER:
        topic_dir = BASE / topic
        if not topic_dir.exists():
            continue

        topic_processed = 0
        topic_skipped = 0

        slug_dirs = sorted([
            d for d in topic_dir.iterdir()
            if d.is_dir() and not d.name.startswith("_")
        ])

        for reel_dir in slug_dirs:
            slug = reel_dir.name
            reel_key = f"{topic}/{slug}"

            # Skip pilot reels
            if reel_key in PILOT_REELS:
                topic_skipped += 1
                total_skipped += 1
                skip_detail["pilot"] = skip_detail.get("pilot", 0) + 1
                continue

            # Check beat_sheet exists
            bs_path = reel_dir / "beat_sheet.json"
            if not bs_path.exists():
                topic_skipped += 1
                total_skipped += 1
                skip_detail["no_beat_sheet"] = skip_detail.get("no_beat_sheet", 0) + 1
                continue

            # Load metadata for scope check
            try:
                with open(bs_path) as f:
                    data = json.load(f)
                metadata = data.get("metadata", {})
            except Exception:
                topic_skipped += 1
                total_skipped += 1
                skip_detail["parse_error"] = skip_detail.get("parse_error", 0) + 1
                continue

            in_scope, reason = is_in_scope(slug, metadata)
            if not in_scope:
                topic_skipped += 1
                total_skipped += 1
                skip_detail[reason] = skip_detail.get(reason, 0) + 1
                continue

            # Process
            result = process_reel(topic, slug, reel_dir, stop_list, form_a_count)
            if result is None:
                topic_skipped += 1
                total_skipped += 1
                skip_detail["no_beat_sheet"] = skip_detail.get("no_beat_sheet", 0) + 1
                continue

            if result.get("skipped"):
                topic_skipped += 1
                total_skipped += 1
                skip_detail["error"] = skip_detail.get("error", 0) + 1
                continue

            topic_processed += 1
            total_processed += 1

            fixes = result["fixes"]
            if fixes:
                line = f"[{topic}/{slug}] fixes: {', '.join(fixes)}"
            else:
                line = f"[{topic}/{slug}] fixes: none (already compliant)"
            all_reel_lines.append(line)

        topic_summaries[topic] = (topic_processed, topic_skipped)

    # ─── Build report ─────────────────────────────────────────────────────
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    report_lines.append(f"# batch_design_v1 Report — {ts}\n")
    report_lines.append(f"**Total processed:** {total_processed}  ")
    report_lines.append(f"**Total skipped:** {total_skipped}\n")

    report_lines.append("## Per-Topic Summary\n")
    report_lines.append("| Topic | Processed | Skipped |")
    report_lines.append("|---|---|---|")
    for topic in TOPICS_ORDER:
        p, s = topic_summaries.get(topic, (0, 0))
        report_lines.append(f"| {topic} | {p} | {s} |")
    report_lines.append("")

    report_lines.append("## Skip Breakdown\n")
    for reason, cnt in sorted(skip_detail.items(), key=lambda x: -x[1]):
        report_lines.append(f"- {reason}: {cnt}")
    report_lines.append("")

    report_lines.append("## Per-Reel One-Line Summary\n")
    for line in all_reel_lines:
        report_lines.append(line)
    report_lines.append("")

    report_lines.append("## STOP List\n")
    if stop_list:
        for s in stop_list:
            report_lines.append(f"- **{s['reel']}** beat `{s['beat']}`: {s['reason']}")
    else:
        report_lines.append("None.")
    report_lines.append("")

    report_lines.append("## NEEDED ICONS\n")
    report_lines.append("None. (No icon-dependent beats were modified in this batch.)\n")

    report_lines.append("## Polarity Balance\n")
    report_lines.append(f"- FormA light cards added: {form_a_count[0]}")
    report_lines.append("- Dark beats: 0 (all gen-AI replacements default to light polarity)\n")

    # Fix frequency tallying
    from collections import Counter
    fix_counter = Counter()
    for line in all_reel_lines:
        if "fixes: " in line and "none" not in line:
            fix_part = line.split("fixes: ", 1)[1]
            for f in fix_part.split(", "):
                fix_counter[f.strip()] += 1

    report_lines.append("## Top Fix Types\n")
    for fix, cnt in fix_counter.most_common(10):
        report_lines.append(f"- `{fix}`: {cnt}")
    report_lines.append("")

    report_lines.append(f"## Final Totals\n")
    report_lines.append(f"- Reels processed: {total_processed}")
    report_lines.append(f"- Reels skipped: {total_skipped}")
    report_lines.append(f"  - Pilot (already done): {skip_detail.get('pilot', 0)}")
    report_lines.append(f"  - nbb- prefix: {skip_detail.get('nbb- prefix', 0)}")
    report_lines.append(f"  - Bear ElevenLabs clone: {skip_detail.get('Bear ElevenLabs clone', 0)}")
    report_lines.append(f"  - Not in scope: {skip_detail.get('not claude-liam / NikBearBrown / am_onyx', 0)}")
    report_lines.append(f"  - No beat_sheet: {skip_detail.get('no_beat_sheet', 0)}")
    report_lines.append(f"  - Parse error: {skip_detail.get('parse_error', 0)}")
    report_lines.append("")

    report_text = "\n".join(report_lines)
    report_path = BASE / "batch_design_v1_report.md"
    with open(report_path, "w") as f:
        f.write(report_text)

    print(f"Done. Processed: {total_processed}, Skipped: {total_skipped}")
    print(f"STOPs: {len(stop_list)}")
    print(f"FormA cards added: {form_a_count[0]}")
    print(f"Report: {report_path}")

    # Print top fixes
    print("\nTop fix types:")
    for fix, cnt in fix_counter.most_common(5):
        print(f"  {fix}: {cnt}")


if __name__ == "__main__":
    main()
