#!/usr/bin/env python3
"""
reconcile_schema.py — Schema reconcile for claude-cowork-plugins series.

Transforms all 14 beat_sheet.json files:
  - id → beat_id (required by all pipeline scripts)
  - Adds metadata.voice_kokoro (kokoro engine reads this, not metadata.voice)
  - Adds shot object per beat based on lane/scene fields
  - Adds estimated_duration_s per beat from word count
  - Maps scene names to registered Remotion patterns
  - MANIM beats: adds engine="manim" at beat level

Registered pattern mappings used:
  SegmentCard / SparkBeat → VRSegmentCard (CLAUDE tokens, acts as segment slate)
  ChipGrid                → VRChipGrid
  PredictCard             → VRPredictCard
  SourceFlow              → VRSourceFlow
  LayerStack              → VRLayerStack
  ClaudeComposerAsk       → ClaudeComposerAsk
  ClaudeVerdictArtifact   → ClaudeVerdictArtifact
  ClaudeTitleOutro        → ClaudeTitleOutro
  code-block              → ClaudeCodeBeat
  illustration/*          → SlateCard (renders as slate; pantry fill or
                            custom Remotion component needed before Gate D1)

Preserves all existing fields; never removes content, narration, or acts.
Backs up original as beat_sheet.json.bak (skips if bak already exists).
"""
import json, re, shutil
from pathlib import Path

BASE = Path(__file__).parent

REELS = [
    "claude-liam-what-plugins-are",
    "claude-liam-installing-plugins",
    "claude-liam-productivity",
    "claude-liam-marketing",
    "claude-liam-sales",
    "claude-liam-research",
    "claude-liam-data",
    "claude-liam-enterprise-search",
    "claude-liam-product",
    "claude-liam-support",
    "claude-liam-legal-finance",
    "claude-liam-building-plugins",
    "claude-liam-combining-plugins",
    "claude-liam-troubleshooting",
]

WORDS_PER_SEC = 2.9

SCENE_TO_PATTERN = {
    "ClaudeComposerAsk":    "ClaudeComposerAsk",
    "ClaudeTitleOutro":     "ClaudeTitleOutro",
    "ClaudeVerdictArtifact": "ClaudeVerdictArtifact",
    "SegmentCard":          "VRSegmentCard",
    "SparkBeat":            "VRSegmentCard",
    "ChipGrid":             "VRChipGrid",
    "PredictCard":          "VRPredictCard",
    "SourceFlow":           "VRSourceFlow",
    "LayerStack":           "VRLayerStack",
    "code-block":           "ClaudeCodeBeat",
    "illustration/LayerStack": "VRLayerStack",  # reuse registered wrapper
}


def act_numeral(act_str: str) -> str:
    """Extract roman numeral from 'ACT I', 'ACT II', etc."""
    m = re.search(r'ACT\s+(I+V?|VI*|IV|IX)', str(act_str), re.IGNORECASE)
    return m.group(1).upper() if m else ""


def est_dur(text: str, minimum: float = 4.0) -> float:
    words = len(text.split()) if text else 0
    return round(max(minimum, words / WORDS_PER_SEC), 1)


def build_ask_props(beat: dict, meta: dict) -> dict:
    """Build ClaudeComposerAsk props from beat + metadata."""
    props = beat.get("props") or {}
    model_chip = meta.get("model_chip") or {}
    p = {
        "command":     props.get("command", beat.get("narration_text", "")[:160]),
        "topic":       meta.get("topic", "CLAUDE · COWORK PLUGINS"),
        "segment":     meta.get("title", "Claude, Equipped"),
        "greeting":    beat.get("greeting", "Hola, Liam"),
        "runningText": props.get("runningText", "thinking…"),
        "folderLabel": meta.get("folderLabel", "@NikBearBrown"),
        "modelLabel":  model_chip.get("model", "Fable 5"),
        "effortLabel": model_chip.get("effort", "High"),
    }
    if "output" in props:
        p["output"] = props["output"]
    return p


def build_verdict_props(beat: dict) -> dict:
    props = beat.get("props") or {}
    return {
        "artifactTitle":   props.get("artifactTitle", "Recap"),
        "artifactHeading": props.get("artifactHeading", "What we covered"),
        "artifactLines":   props.get("artifactLines", []),
    }


def build_outro_props(beat: dict) -> dict:
    props = beat.get("props") or {}
    return {
        "title":   props.get("title", beat.get("narration_text", "")[:80]),
        "handle":  props.get("handle", "@NikBearBrown"),
        "subline": props.get("subline", ""),
    }


def build_segment_card_props(beat: dict) -> dict:
    props = beat.get("props") or {}
    return {
        "act":       act_numeral(beat.get("act", "")),
        "title":     props.get("title", beat.get("spark_line", "")),
        "sparkLine": beat.get("spark_line", props.get("title", "")),
    }


def build_chip_grid_props(beat: dict) -> dict:
    viz = beat.get("viz") or {}
    props = beat.get("props") or {}
    items = (viz.get("chips") or props.get("chips")
             or viz.get("items") or props.get("items") or [])
    return {
        "items":     items,
        "sparkLine": beat.get("spark_line", ""),
        "cols":      viz.get("cols") or props.get("cols"),
    }


def build_predict_card_props(beat: dict) -> dict:
    show = beat.get("show", "")
    narr = beat.get("narration_text", "")
    question = show[:120] if show else narr[:120]
    return {
        "question":  question,
        "commit":    beat.get("spark_line", ""),
        "sparkLine": beat.get("spark_line", ""),
    }


def build_source_flow_props(beat: dict) -> dict:
    viz = beat.get("viz") or {}
    return {
        "sourceLabel": viz.get("source", "your tools + your data"),
        "feeds":       [{"label": f} for f in (viz.get("feeds") or [])],
        "destApp":     viz.get("target", "the plugin"),
        "destTitle":   viz.get("destTitle", ""),
        "sparkLine":   beat.get("spark_line", ""),
    }


def build_layer_stack_props(beat: dict) -> dict:
    viz = beat.get("viz") or {}
    props = beat.get("props") or {}
    layers = (viz.get("layers") or props.get("layers") or [])
    if layers and isinstance(layers[0], str):
        layers = [{"title": l, "sub": ""} for l in layers]
    return {
        "layers":    layers,
        "sparkLine": beat.get("spark_line", ""),
        "caption":   viz.get("caption") or props.get("caption"),
    }


def build_code_beat_props(beat: dict) -> dict:
    props = beat.get("props") or {}
    return {
        "title":     "Cowork",
        "code":      props.get("code", ""),
        "sparkLine": beat.get("spark_line", ""),
    }


def pattern_for_scene(scene: str) -> str:
    """Map a scene name to a registered Remotion pattern."""
    if scene in SCENE_TO_PATTERN:
        return SCENE_TO_PATTERN[scene]
    if scene.startswith("illustration/") or scene.startswith("media/"):
        return "SlateCard"
    return "SlateCard"


def build_remotion_props(beat: dict, pattern: str, meta: dict) -> dict:
    """Build props dict for a given pattern."""
    if pattern == "ClaudeComposerAsk":
        return build_ask_props(beat, meta)
    if pattern == "ClaudeVerdictArtifact":
        return build_verdict_props(beat)
    if pattern == "ClaudeTitleOutro":
        return build_outro_props(beat)
    if pattern == "VRSegmentCard":
        return build_segment_card_props(beat)
    if pattern == "VRChipGrid":
        return build_chip_grid_props(beat)
    if pattern == "VRPredictCard":
        return build_predict_card_props(beat)
    if pattern == "VRSourceFlow":
        return build_source_flow_props(beat)
    if pattern == "VRLayerStack":
        return build_layer_stack_props(beat)
    if pattern == "ClaudeCodeBeat":
        return build_code_beat_props(beat)
    if pattern == "SlateCard":
        return {
            "label":   beat.get("spark_line") or beat.get("scene", ""),
            "beatId":  beat.get("id") or beat.get("beat_id", ""),
            "caption": (beat.get("narration_text") or "")[:120],
        }
    return beat.get("props") or {}


def reconcile_beat(beat: dict, meta: dict) -> tuple[dict, list[str]]:
    """Return (reconciled_beat, retint_notes)."""
    notes = []
    b = dict(beat)

    # 1. id → beat_id
    if "id" in b and "beat_id" not in b:
        b["beat_id"] = b.pop("id")

    lane = b.get("lane", "")
    scene = b.get("scene", "")

    # 2. Estimate duration if missing
    if "estimated_duration_s" not in b and "actual_duration_s" not in b:
        narr = b.get("narration_text", "")
        b["estimated_duration_s"] = est_dur(narr)

    # 3. VOX beats: already have shot, keep them
    if "shot" in b:
        return b, notes

    # 4. MANIM beats
    if lane == "MANIM" or (scene and scene.startswith("manim/")):
        b["engine"] = "manim"
        b["shot"] = {"type": "GRAPHIC", "source": "own"}
        return b, notes

    # 5. REMOTION / CARD / ASK beats
    pattern = pattern_for_scene(scene)
    if pattern not in ("SlateCard", "ClaudeComposerAsk", "ClaudeVerdictArtifact",
                        "ClaudeTitleOutro", "ClaudeCodeBeat"):
        # VR* patterns use CLAUDE tokens already — note the retint
        notes.append(
            f"  {b.get('beat_id','?')} ({scene}) → {pattern} — already uses CLAUDE tokens"
            f" (cream/ink/terracotta); no additional retint needed."
        )

    props = build_remotion_props(b, pattern, meta)
    b["shot"] = {
        "type":    "REMOTION",
        "source":  "own",
        "remotion": {
            "pattern": pattern,
            "props":   props,
        },
    }
    if pattern == "SlateCard" and scene and not scene.startswith("media/"):
        notes.append(
            f"  {b.get('beat_id','?')} ({scene}) → SlateCard (unregistered custom"
            f" illustration — will render as slate in previz; needs Remotion component"
            f" or pantry still before final cut)."
        )
    return b, notes


def reconcile_reel(slug: str) -> dict:
    """Reconcile one reel's beat_sheet.json. Returns a summary dict."""
    reel_dir = BASE / slug
    bs_path = reel_dir / "beat_sheet.json"
    bak_path = reel_dir / "beat_sheet.json.bak"

    if not bs_path.exists():
        return {"slug": slug, "status": "SKIP — no beat_sheet.json"}

    # Backup
    if not bak_path.exists():
        shutil.copy2(bs_path, bak_path)

    bs = json.loads(bs_path.read_text())
    meta = bs.get("metadata", {})

    # Add voice_kokoro if missing (kokoro reads this, not metadata.voice)
    if "voice_kokoro" not in meta and "voice" in meta:
        meta["voice_kokoro"] = meta["voice"]

    # Add topic if missing
    if "topic" not in meta:
        meta["topic"] = "CLAUDE · COWORK PLUGINS"

    all_retint_notes = []
    new_beats = []
    for beat in bs.get("beats", []):
        new_beat, notes = reconcile_beat(beat, meta)
        new_beats.append(new_beat)
        all_retint_notes.extend(notes)

    bs["metadata"] = meta
    bs["beats"] = new_beats

    bs_path.write_text(json.dumps(bs, indent=2, ensure_ascii=False) + "\n")

    # Write BUILD-LOG.md
    log_path = reel_dir / "BUILD-LOG.md"
    log_content = f"# BUILD LOG — {slug}\n\n"
    log_content += "## Step 1 — Schema Reconcile\n\n"
    log_content += "**Status:** DONE\n\n"
    log_content += "Changes applied:\n"
    log_content += "- `id` → `beat_id` for all beats\n"
    log_content += "- `metadata.voice_kokoro: am_onyx` added (pipeline reads this, not `.voice`)\n"
    log_content += "- `metadata.topic: CLAUDE · COWORK PLUGINS` added\n"
    log_content += "- `shot` object added to all beats without one\n"
    log_content += "- `estimated_duration_s` derived from word count (2.9 wps) for beats lacking it\n\n"
    log_content += "**Remotion patterns used (VR* series — all use CLAUDE tokens natively):**\n\n"
    if all_retint_notes:
        for note in all_retint_notes:
            log_content += note + "\n"
    else:
        log_content += "  No retint notes.\n"
    log_content += "\n**Retint log:** VR* patterns (VRSegmentCard, VRChipGrid, VRPredictCard, "
    log_content += "VRSourceFlow, VRLayerStack) are from VercelRefactorIllu.tsx which imports "
    log_content += "`CLAUDE` tokens directly — cream #F2F0E9, ink #3D3929, accent/terracotta "
    log_content += "#D97757. No additional retinting required.\n\n"
    log_content += "## Step 2 — Lane-Mix Lint\n\n"
    log_content += "Pending audio lock.\n\n"
    log_content += "## Step 3 — Gate P\n\n"
    log_content += "**GATE P REQUIRED** — present full narration for sign-off before audio.\n\n"

    log_path.write_text(log_content)

    # Lane histogram for lint
    from collections import Counter
    lanes = Counter(b.get("lane", "?") for b in new_beats)
    total = len(new_beats)
    # Count body beats (exclude ASK bookends + CARD bookends like ClaudeTitleOutro, ClaudeVerdictArtifact)
    bookend_ids = {b.get("beat_id") for b in new_beats
                   if b.get("beat_id") in ("B00", "V01", "H01", "O01")}
    body = [b for b in new_beats if b.get("beat_id") not in bookend_ids]
    body_total = len(body)
    body_lanes = Counter(b.get("lane", "?") for b in body)
    vox_pct = round(100 * body_lanes.get("VOX", 0) / max(1, body_total))
    manim_pct = round(100 * body_lanes.get("MANIM", 0) / max(1, body_total))
    rem_pct = round(100 * body_lanes.get("REMOTION", 0) / max(1, body_total))
    card_pct = round(100 * body_lanes.get("CARD", 0) / max(1, body_total))

    return {
        "slug": slug,
        "status": "OK",
        "beats": total,
        "lanes": dict(lanes),
        "body_beats": body_total,
        "vox_pct": vox_pct,
        "manim_pct": manim_pct,
        "remotion_pct": rem_pct,
        "card_pct": card_pct,
        "slate_count": sum(1 for b in new_beats
                           if (b.get("shot") or {}).get("remotion", {}).get("pattern") == "SlateCard"),
    }


def main():
    print("=== claude-cowork-plugins — Schema Reconcile ===\n")
    results = []
    for slug in REELS:
        print(f"Processing {slug}...")
        r = reconcile_reel(slug)
        results.append(r)
        if r["status"] == "OK":
            print(f"  ✓ {r['beats']} beats | body: VOX {r['vox_pct']}% "
                  f"MANIM {r['manim_pct']}% REMOTION {r['remotion_pct']}% "
                  f"CARD {r['card_pct']}% | slates: {r['slate_count']}")
            # Lint
            vox_ok = 15 <= r["vox_pct"] <= 30
            manim_ok = 20 <= r["manim_pct"] <= 45
            rem_ok = 25 <= r["remotion_pct"] <= 50
            if not vox_ok:
                print(f"  ⚠ VOX {r['vox_pct']}% outside 15–30% band")
            if not manim_ok:
                print(f"  ⚠ MANIM {r['manim_pct']}% outside 20–45% band")
        else:
            print(f"  {r['status']}")

    print("\n=== Summary ===")
    for r in results:
        status = "✓" if r["status"] == "OK" else "✗"
        print(f"  {status} {r['slug']}")

    print("\nAll done. Beat_sheet.json files updated. Backups at beat_sheet.json.bak")
    print("\nNext steps:")
    print("  1. Review GATE P narration (see each reel's BUILD-LOG.md)")
    print("  2. Run: python3 runtime/scripts/generate_audio_kokoro.py <reel> --dry-run")
    print("  3. After approval: python3 runtime/scripts/generate_audio_kokoro.py <reel>")


if __name__ == "__main__":
    main()
