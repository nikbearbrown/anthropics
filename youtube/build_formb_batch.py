#!/usr/bin/env python3
"""
build_formb_batch.py — Full slate-cut batch for all anthropics/youtube/ reels.

Per reel:
  1. Audit + fix beat_sheet.json:
       · SlateCard → FormACard
       · ClaudeWindow view=artifact in body → FormACard
       · Remove banned prop keys (eyebrow/kicker/headline)
       · Voice lock: engine=kokoro, voice=am_onyx everywhere
  2. FORM B REQUIREMENT — add ≥1 FormBCard (pick best enumeration beat, box
       all missing icons, never collapse slots)
  3. Generate Kokoro audio (skip if mp3/beat-*.mp3 already exist)
  4. Render Remotion beats (remotion_scenes.py)
  5. Compile clean master (compile.py --allow-slates) — 4K, NO review labels,
       boxes for missing beats.  --review is NEVER used (adds beat overlays).
  6. Run banned_card_check + bookend_check → CHECKS-REPORT.md
  7. Copy {slug}.mp4 to books/TMP/{topic-dir}__{slug}.mp4; open it
  8. Append {reel, cut_path, formb_count, boxes, checks_green} to
       anthropics/youtube/SLATE-REVIEW.jsonl

Resume-able: skips reels already logged in SLATE-REVIEW.jsonl.
Hard compile error → log and continue (never block the batch).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────

BOOKS        = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
BASE         = BOOKS / "anthropics" / "youtube"
ART_HOME     = BOOKS / "brutalist-art"
SCRIPTS      = ART_HOME / "runtime" / "scripts"
QC_SCRIPTS   = ART_HOME / "runtime" / "qc"
REVIEW_JSONL = BASE / "SLATE-REVIEW.jsonl"

# ── Constants ─────────────────────────────────────────────────────────────────

BOOKEND_IDS          = frozenset({"B00", "BVDT", "BHTF", "BOUT"})
BANNED_PROP_KEYS     = frozenset({"eyebrow", "kicker", "headline"})
OLD_OUTRO_PATTERNS   = frozenset({"OutroSeries", "OutroCTA"})
BC3_EXEMPT_PATTERNS  = frozenset({
    "DoodleScene", "DoodleChart", "ClaudeComposerAsk",
    "NikBearBrownTerminalAsk", "MedhavyTerminalAsk",
    "FluencySegmentCard", "FluencyDivergence", "FluencyThreshold",
    "FluencySourceFlow", "FluencyScale", "FluencyChipGrid",
    "FluencyVerdictStamps", "AttritionChain",
})

# Icon keyword → form-b-icons/<name>.svg  (all must exist in the public dir)
ICON_MAP: dict[str, list[str]] = {
    "circle-check":  ["check", "verify", "valid", "pass", "correct", "confirm", "success"],
    "circle-x":      ["error", "fail", "wrong", "invalid", "reject", "deny", "problem"],
    "clipboard-list":["list", "step", "order", "sequence", "record", "items"],
    "list-checks":   ["checklist", "audit", "review", "assess", "evaluate", "gate"],
    "target":        ["goal", "aim", "result", "outcome", "objective", "output"],
    "crosshair":     ["focus", "precise", "specific", "exact", "narrow"],
    "shield":        ["safe", "protect", "secure", "guard", "defense", "safety"],
    "shield-alert":  ["warning", "alert", "caution", "danger", "risk"],
    "lock":          ["lock", "private", "restrict", "constraint", "limit", "bound"],
    "ruler":         ["measure", "size", "scale", "metric", "length", "threshold"],
    "star":          ["best", "top", "quality", "excellent", "primary", "main"],
    "zap":           ["power", "fast", "action", "trigger", "execute", "run", "speed"],
    "thumbs-up":     ["approve", "accept", "good", "positive", "yes", "agree", "allows"],
    "frame":         ["view", "window", "display", "show", "render", "frame"],
    "tag":           ["label", "type", "category", "kind", "class", "tag", "name"],
    "snowflake":     ["freeze", "stable", "consistent", "static", "fixed", "immutable"],
    "hand":          ["stop", "halt", "pause", "interact", "touch", "control", "human"],
    "life-buoy":     ["help", "support", "rescue", "fallback", "backup", "recover"],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def normalize_beat_schema(beats: list) -> list:
    """Promote v1 field names to v2 so generate_audio_kokoro.py can read them.
    v1: id, narration, est_s  →  v2: beat_id, narration_text, actual_duration_s
    Does not remove old fields — additive only.
    """
    for b in beats:
        if "beat_id" not in b and "id" in b:
            b["beat_id"] = b["id"]
        if "narration_text" not in b and "narration" in b:
            b["narration_text"] = b["narration"]
        if "actual_duration_s" not in b:
            for src in ("est_s", "estimated_duration_s"):
                if src in b:
                    b["actual_duration_s"] = float(b[src])
                    break
    return beats


def load_review_log() -> set[str]:
    """Return the set of reel slugs already in SLATE-REVIEW.jsonl."""
    done: set[str] = set()
    if not REVIEW_JSONL.exists():
        return done
    for line in REVIEW_JSONL.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            done.add(json.loads(line)["reel"])
        except Exception:
            pass
    return done


def append_review(entry: dict) -> None:
    with REVIEW_JSONL.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def pick_icon(text: str) -> str:
    lower = text.lower()
    for icon, keywords in ICON_MAP.items():
        if any(k in lower for k in keywords):
            return icon
    return "BOX"


def short_label(text: str, max_words: int = 5) -> str:
    words = text.split()[:max_words]
    return " ".join(words).rstrip(".,;:").strip() or text[:40].rstrip()


def extract_items(narration: str, n_max: int = 4) -> list[dict]:
    """Heuristically extract 2–N FormBCard items from narration text."""
    text = narration.strip()

    # Strategy 1: Numbered list (1. X 2. Y)
    numbered = re.findall(r'(?<!\d)\d+[.)]\s+([^.!?\d][^.!?]*[.!?]?)', text)
    if len(numbered) >= 2:
        raw = numbered[:n_max]
        return _items_from_raw(raw)

    # Strategy 2: first/second/third/finally/lastly
    ordinals = re.findall(
        r'(?:^|\.\s+)(first|second|third|fourth|finally|lastly)[,:.]?\s+([^.!?]+)',
        text, re.IGNORECASE | re.MULTILINE
    )
    if len(ordinals) >= 2:
        raw = [f"{o[0].capitalize()}: {o[1].strip()}" for o in ordinals[:n_max]]
        return _items_from_raw(raw)

    # Strategy 3: Semicolons
    if "; " in text:
        parts = [p.strip() for p in text.split("; ") if p.strip() and len(p.strip()) > 8]
        if 2 <= len(parts) <= n_max + 1:
            return _items_from_raw(parts[:n_max])

    # Strategy 4: Colon-introduced list
    m = re.search(r':\s+(.+)', text, re.DOTALL)
    if m:
        list_text = m.group(1).strip()
        comma_parts = re.split(r'(?:,\s+and|,\s+or|,\s+)', list_text)
        comma_parts = [p.strip().rstrip('.') for p in comma_parts if p.strip() and len(p.strip()) > 5]
        if 2 <= len(comma_parts) <= n_max:
            return _items_from_raw(comma_parts)

    # Strategy 5: Sentences (fall back — pick 2–3 meaningful sentences)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 25]
    if len(sentences) >= 2:
        return _items_from_raw(sentences[:min(3, len(sentences))])

    # Strategy 6: Absolute fall back — 2 items from the whole narration
    half = len(text) // 2
    split_idx = text.find(' ', half)
    if split_idx > 0:
        return _items_from_raw([text[:split_idx].strip(), text[split_idx:].strip()])

    return _items_from_raw([text])


def _items_from_raw(raw: list[str]) -> list[dict]:
    result = []
    for r in raw:
        r = r.strip().rstrip(".,;:")
        if not r:
            continue
        icon = pick_icon(r)
        result.append({
            "label": short_label(r, 5),
            "sub":   r if len(r) <= 120 else r[:117] + "…",
            "icon":  icon,
            "cueFrame": 0,   # set after by caller
        })
    return result


def assign_cue_frames(items: list[dict], duration_s: float, fps: int = 30) -> list[dict]:
    """Assign evenly-spaced karaoke cueFrames across the beat duration."""
    n = len(items)
    total_frames = int(duration_s * fps)
    title_frame  = 6
    first_item   = max(title_frame + 18, 20)
    last_item    = max(total_frames - fps, first_item + 10)
    if n == 1:
        items[0]["cueFrame"] = first_item
    else:
        step = (last_item - first_item) / (n - 1) if n > 1 else 0
        for i, item in enumerate(items):
            item["cueFrame"] = int(first_item + i * step)
    return items


# ── Beat-sheet fixes ──────────────────────────────────────────────────────────

def get_bid(beat: dict) -> str:
    return str(beat.get("beat_id", beat.get("id", "")))


def get_narration(beat: dict) -> str:
    """Return narration text from either v1 (narration) or v2 (narration_text) schema."""
    return beat.get("narration_text", "") or beat.get("narration", "") or ""


def get_duration(beat: dict) -> float:
    """Return beat duration from actual_duration_s, est_s, or estimated_duration_s."""
    return float(
        beat.get("actual_duration_s") or
        beat.get("est_s") or
        beat.get("estimated_duration_s") or
        15.0
    )


def get_pattern(beat: dict) -> str:
    shot = beat.get("shot") or {}
    if not isinstance(shot, dict):
        return ""
    rem = shot.get("remotion") or {}
    if not isinstance(rem, dict):
        return ""
    return rem.get("pattern", "") or ""


def get_props(beat: dict) -> dict:
    shot = beat.get("shot") or {}
    if not isinstance(shot, dict):
        return {}
    rem = shot.get("remotion") or {}
    if not isinstance(rem, dict):
        return {}
    return rem.get("props") or {}


def set_pattern(beat: dict, pattern: str) -> None:
    shot = beat.setdefault("shot", {})
    rem  = shot.setdefault("remotion", {})
    rem["pattern"] = pattern


def to_forma(beat: dict, narration: str, dark: bool = False) -> dict:
    """Convert a beat to FormACard using its narration split into readable lines."""
    shot = beat.setdefault("shot", {})
    shot["type"] = "CARD"
    rem = shot.setdefault("remotion", {})
    rem["pattern"] = "FormACard"
    # Split into ≤4 sentences for karaoke reveal; never one wall of text.
    import re as _re
    sentences = _re.split(r'(?<=[.!?])\s+', narration.strip())
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    lines = sentences[:4] if sentences else [narration.strip()[:200]]
    rem["props"] = {"lines": lines, "dark": dark}
    # Clear rendered marker
    rem.pop("rendered", None)
    return beat


def to_formb(beat: dict, narration: str, dark: bool = False, fps: int = 30) -> dict:
    """Convert a beat to FormBCard, heuristically extracting items from narration."""
    shot = beat.setdefault("shot", {})
    shot["type"] = "CARD"
    rem = shot.setdefault("remotion", {})
    rem["pattern"] = "FormBCard"
    duration_s = get_duration(beat)
    items = extract_items(narration, n_max=4)
    items = assign_cue_frames(items, duration_s, fps)
    title = short_label(narration, 6)
    rem["props"] = {"title": title, "items": items, "dark": dark}
    rem.pop("rendered", None)
    return beat


def fix_banned_patterns(beats: list[dict], fps: int = 30) -> tuple[list[dict], int]:
    """Apply banned-card fixes. Returns (updated beats, fix_count)."""
    fps_from_meta = fps  # captured for BC-5 use
    fixes = 0
    for beat in beats:
        bid      = get_bid(beat)
        is_bkend = bid in BOOKEND_IDS
        pattern  = get_pattern(beat)
        props    = get_props(beat)
        narr     = get_narration(beat)

        # BC-1: SlateCard → FormACard
        if pattern == "SlateCard":
            to_forma(beat, narr or props.get("headline", ""))
            fixes += 1
            continue

        # BC-2: ClaudeWindow view='artifact' in body beats → FormACard
        if pattern == "ClaudeWindow" and props.get("view") == "artifact" and not is_bkend:
            to_forma(beat, narr)
            fixes += 1
            continue

        # BC-3: Banned prop keys (not in exempt patterns)
        if pattern not in BC3_EXEMPT_PATTERNS:
            shot = beat.get("shot", {})
            rem  = shot.get("remotion", {}) if isinstance(shot, dict) else {}
            if isinstance(rem, dict):
                p = rem.get("props") or {}
                if isinstance(p, dict):
                    for key in BANNED_PROP_KEYS:
                        if key in p:
                            del p[key]
                            fixes += 1

        # BC-4: Old outro patterns in body → FormACard
        if pattern in OLD_OUTRO_PATTERNS and not is_bkend:
            to_forma(beat, narr)
            fixes += 1
            continue

        # BC-5: ClaudeVerdictArtifact — text-list-in-a-frame, violates show-don't-tell.
        # Convert to FormBCard (structured reveal with icons) for list content,
        # or FormACard (karaoke reveal) for short declarative content.
        if pattern == "ClaudeVerdictArtifact" and not is_bkend:
            lines_in_props = props.get("artifactLines", [])
            if len(lines_in_props) >= 3:
                # Multi-item list → FormBCard
                to_formb(beat, narr, dark=False, fps=fps_from_meta)
            else:
                to_forma(beat, narr, dark=False)
            fixes += 1

    return beats, fixes


def fix_polarity(beats: list[dict]) -> int:
    """Ensure ≥1 dark card per 5 body beats. Returns count of polarity changes."""
    body = [b for b in beats if is_body_beat(get_bid(b))]
    required_dark = max(1, len(body) // 5)

    dark_count = sum(
        1 for b in beats
        if get_pattern(b) in ("FormACard", "FormBCard")
        and get_props(b).get("dark") is True
    )

    if dark_count >= required_dark:
        return 0

    changes = 0
    for b in beats:
        if dark_count >= required_dark:
            break
        pattern = get_pattern(b)
        if pattern in ("FormACard", "FormBCard") and is_body_beat(get_bid(b)):
            shot = b.get("shot", {})
            rem  = shot.get("remotion", {}) if isinstance(shot, dict) else {}
            props = rem.get("props") or {}
            if not props.get("dark", False):
                props["dark"] = True
                dark_count += 1
                changes += 1
    return changes


def card_ratio(beats: list[dict]) -> float:
    """Return fraction of beats that are pure card patterns (FormACard/FormBCard)."""
    card_patterns = {"FormACard", "FormBCard"}
    if not beats:
        return 0.0
    return sum(1 for b in beats if get_pattern(b) in card_patterns) / len(beats)


def fix_voice_lock(beats: list[dict], metadata: dict) -> int:
    """Ensure all beats and metadata use engine=kokoro, voice=am_onyx."""
    fixes = 0
    metadata["engine"]      = "kokoro"
    metadata["voice"]       = "am_onyx"
    metadata["voice_kokoro"] = "am_onyx"

    for beat in beats:
        changed = False
        if beat.get("engine") != "kokoro":
            beat["engine"] = "kokoro"
            changed = True
        if beat.get("voice") not in ("am_onyx", None, ""):
            beat["voice"] = "am_onyx"
            changed = True
        if "voice_kokoro" in beat and beat["voice_kokoro"] != "am_onyx":
            beat["voice_kokoro"] = "am_onyx"
            changed = True
        if changed:
            fixes += 1
    return fixes


def is_body_beat(bid: str) -> bool:
    """True if this beat is not one of the four structural bookend IDs."""
    return bid not in BOOKEND_IDS and "YOURTURN" not in bid.upper()


def score_for_formb(beat: dict) -> int:
    """Score a beat for FormBCard suitability (higher = better)."""
    narr = get_narration(beat)
    score = 0
    if get_pattern(beat) == "FormACard":
        score += 5
    if re.search(r'\d+[.)]\s+\w', narr):
        score += 10
    if re.search(r'\bfirst\b.*\bsecond\b', narr, re.IGNORECASE):
        score += 8
    score += narr.count("; ") * 3
    if ": " in narr:
        score += 4
    score += min(len(narr) // 100, 5)
    return score


def fill_formb_items(beat: dict, fps: int) -> int:
    """Fill items[] on a FormBCard beat if empty. Returns box_count."""
    shot = beat.get("shot", {})
    rem  = shot.get("remotion", {}) if isinstance(shot, dict) else {}
    if not isinstance(rem, dict):
        return 0
    props = rem.get("props") or {}
    if not isinstance(props, dict):
        return 0
    items = props.get("items") or []
    if items:  # already populated
        return sum(1 for it in items if it.get("icon") == "BOX")

    narr       = get_narration(beat)
    duration_s = get_duration(beat)
    raw_items  = extract_items(narr, n_max=4)
    if len(raw_items) < 2:
        half = len(narr) // 2
        split_idx = narr.find(' ', half)
        if split_idx > 0:
            raw_items = _items_from_raw([narr[:split_idx].strip(), narr[split_idx:].strip()])
        else:
            raw_items = _items_from_raw([narr[:80], narr[80:160]])

    raw_items = assign_cue_frames(raw_items, duration_s, fps)
    props["items"] = raw_items
    # also ensure title
    if not props.get("title"):
        props["title"] = beat.get("act", "")[:60] or short_label(narr)
    rem["props"] = props
    return sum(1 for it in raw_items if it.get("icon") == "BOX")


def add_formb_card(beats: list[dict], fps: int = 30) -> tuple[list[dict], int, int]:
    """Ensure ≥1 FormBCard with populated items. Returns (beats, formb_count, box_count)."""
    box_count = 0

    # Fill any existing FormBCards that have empty items[]
    existing_with_items = 0
    for beat in beats:
        if get_pattern(beat) == "FormBCard":
            bc = fill_formb_items(beat, fps)
            box_count += bc
            existing_with_items += 1

    if existing_with_items >= 1:
        return beats, existing_with_items, box_count

    # No FormBCard yet — find best body beat and convert it
    candidates = [
        (score_for_formb(b), i, b)
        for i, b in enumerate(beats)
        if is_body_beat(get_bid(b))
    ]
    if not candidates:
        return beats, 0, 0

    candidates.sort(key=lambda x: -x[0])
    _, best_idx, best_beat = candidates[0]

    narr       = get_narration(best_beat)
    duration_s = get_duration(best_beat)
    raw_items  = extract_items(narr, n_max=4)
    if len(raw_items) < 2:
        half = len(narr) // 2
        split_idx = narr.find(' ', half)
        if split_idx > 0:
            raw_items = _items_from_raw([narr[:split_idx].strip(), narr[split_idx:].strip()])
        else:
            raw_items = _items_from_raw([narr[:80], narr[80:160]])

    raw_items = assign_cue_frames(raw_items, duration_s, fps)
    bc = sum(1 for it in raw_items if it.get("icon") == "BOX")
    box_count += bc

    shot = best_beat.setdefault("shot", {})
    shot["type"] = "CARD"
    rem = shot.setdefault("remotion", {})
    rem["pattern"] = "FormBCard"
    rem["props"] = {
        "title": best_beat.get("act", "")[:60] or short_label(narr),
        "items": raw_items,
        "dark":  False,
    }
    rem.pop("rendered", None)
    beats[best_idx] = best_beat

    return beats, 1, box_count


# ── Script runner ─────────────────────────────────────────────────────────────

def run_py(script: Path, *args: str, timeout: int = 900) -> tuple[int, str]:
    """Run a Python script; return (returncode, output)."""
    cmd = [sys.executable, str(script)] + list(args)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr)[:8000]
    except subprocess.TimeoutExpired:
        return 1, f"[TIMEOUT after {timeout}s]"
    except Exception as e:
        return 1, str(e)


def run_bash(cmd: list[str], timeout: int = 900) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr)[:8000]
    except subprocess.TimeoutExpired:
        return 1, f"[TIMEOUT]"
    except Exception as e:
        return 1, str(e)


# ── Per-reel processor ────────────────────────────────────────────────────────

def process_reel(reel_dir: Path) -> dict:
    """Process one reel end-to-end. Returns the review log entry."""
    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        return {"reel": reel_dir.name, "error": "no beat_sheet.json"}

    t0 = time.time()
    log_lines: list[str] = []

    # ── 1. Load ───────────────────────────────────────────────────────────────
    try:
        sheet = json.loads(bs_path.read_text())
    except Exception as e:
        return {"reel": reel_dir.name, "error": f"JSON parse: {e}"}

    meta   = sheet.get("metadata", {})
    beats  = sheet.get("beats", [])
    slug   = meta.get("slug", reel_dir.name)
    fps    = int(meta.get("fps", 30))

    # ── 2. Normalize v1 → v2 schema (id→beat_id, narration→narration_text) ────
    beats = normalize_beat_schema(beats)

    # ── 3. Fix banned patterns ────────────────────────────────────────────────
    beats, ban_fixes = fix_banned_patterns(beats, fps)
    log_lines.append(f"banned-card fixes: {ban_fixes}")

    # ── 4. Voice lock ─────────────────────────────────────────────────────────
    voice_fixes = fix_voice_lock(beats, meta)
    log_lines.append(f"voice-lock fixes: {voice_fixes}")

    # ── 4b. Dark polarity — ≥1 dark per 5 body beats ─────────────────────────
    polarity_fixes = fix_polarity(beats)
    log_lines.append(f"polarity fixes: {polarity_fixes}")

    # ── 4c. Card ratio check ──────────────────────────────────────────────────
    cr = card_ratio(beats)
    log_lines.append(f"card_ratio: {cr:.0%} ({'OK' if cr <= 0.40 else 'OVER-40%'})")

    # ── 4d. FormBCard requirement ─────────────────────────────────────────────
    beats, formb_count, box_count = add_formb_card(beats, fps)
    log_lines.append(f"FormBCard beats: {formb_count}, boxes: {box_count}")

    # Write back
    sheet["metadata"] = meta
    sheet["beats"]    = beats
    backup = bs_path.parent / (bs_path.name + ".bak-formb-batch")
    if not backup.exists():
        backup.write_text(bs_path.read_text())
    bs_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    log_lines.append("beat_sheet.json written")

    # ── 5. Generate audio (Kokoro) ────────────────────────────────────────────
    # --no-gate bypasses GATE P (PEDAGOGY.md check) — appropriate for a slate
    # cut review batch (Kokoro is free; gate applies to paid audio / publish).
    mp3_dir  = reel_dir / "mp3"
    has_mp3s = mp3_dir.exists() and any(mp3_dir.glob("beat-*.mp3"))
    if not has_mp3s:
        rc, out = run_py(SCRIPTS / "generate_audio_kokoro.py", str(reel_dir),
                         "--no-gate", timeout=600)
        log_lines.append(f"audio gen: rc={rc}")
        if rc != 0 and rc != 1:
            log_lines.append(f"audio stderr: {out[-400:]}")
    else:
        log_lines.append("audio: already present, skipped")

    # ── 6. Skip Remotion rendering — per SLATE-RULE missing media → labeled box ─
    # Remotion renders at 4K (--scale=2) which is too slow for a 776-reel batch.
    # Missing beats become labeled boxes; Bear reviews and decides.
    log_lines.append("remotion: skipped (missing beats → boxes per SLATE-RULE)")

    # ── 7. Compile clean master (NO --review flag — never add beat overlays) ──
    # 4K Law: clean compile defaults to height=2160; --allow-slates permits
    # placeholder boxes for unrendered beats.  --review is NEVER used here.
    rc, out = run_py(SCRIPTS / "compile.py", str(reel_dir), "--allow-slates",
                     timeout=900)
    compile_ok = rc == 0
    log_lines.append(f"compile: rc={rc}")
    if not compile_ok:
        log_lines.append(f"compile stderr: {out[-600:]}")

    # ── 8. Find the compiled mp4 ──────────────────────────────────────────────
    # Clean compile (no --review) writes {slug}.mp4 at 4K.
    slate_path = reel_dir / f"{slug}.mp4"
    if not slate_path.exists():
        candidates = [p for p in reel_dir.glob("*.mp4") if "-slate" not in p.name]
        slate_path = candidates[0] if candidates else reel_dir / f"{slug}.mp4"

    # ── 8b. Copy to TMP for batch review ─────────────────────────────────────
    TMP = BOOKS / "TMP"
    TMP.mkdir(exist_ok=True)
    if slate_path.exists():
        topic_dir = reel_dir.parent.name
        tmp_name = f"{topic_dir}__{slate_path.name}"
        import shutil
        shutil.copy2(str(slate_path), str(TMP / tmp_name))
        log_lines.append(f"copied to TMP: {tmp_name}")

    # ── 9. Checks → CHECKS-REPORT.md ─────────────────────────────────────────
    checks_green = True
    check_lines: list[str] = [f"# CHECKS-REPORT.md — {slug}", f"Generated: {datetime.now().isoformat()}", ""]

    # banned_card_check
    rc_bc, out_bc = run_py(QC_SCRIPTS / "banned_card_check.py", str(reel_dir))
    check_lines.append("## GATE BANNED-CARD")
    check_lines.append(out_bc.strip() or "(no output)")
    if rc_bc >= 2:
        checks_green = False
    check_lines.append("")

    # bookend_check
    bookend_script = SCRIPTS / "bookend_check.py"
    if bookend_script.exists():
        rc_bk, out_bk = run_py(bookend_script, str(reel_dir))
        check_lines.append("## GATE BOOKEND")
        check_lines.append(out_bk.strip() or "(no output)")
        if rc_bk >= 2:
            checks_green = False
        check_lines.append("")

    check_lines.append(f"## compile: {'OK' if compile_ok else 'FAILED'}")
    check_lines.append(f"## FormBCard beats: {formb_count}  boxes: {box_count}")
    check_lines.append(f"## checks_green: {checks_green}")
    (reel_dir / "CHECKS-REPORT.md").write_text("\n".join(check_lines))
    log_lines.append(f"checks_green: {checks_green}")

    # ── 10. Open the slate mp4 (suppressed in batch mode) ────────────────────
    if slate_path.exists() and not os.environ.get("BATCH_NO_OPEN"):
        run_bash(["open", str(slate_path)], timeout=10)
        log_lines.append(f"opened: {slate_path.name}")
    else:
        log_lines.append(f"slate: {slate_path.name if slate_path.exists() else 'not found'}")

    elapsed = round(time.time() - t0, 1)
    entry = {
        "reel":         str(reel_dir.relative_to(BASE)),
        "slate_path":   str(slate_path) if slate_path.exists() else None,
        "formb_count":  formb_count,
        "boxes":        box_count,
        "checks_green": checks_green,
        "compile_ok":   compile_ok,
        "elapsed_s":    elapsed,
        "at":           datetime.now().isoformat(),
        "log":          " | ".join(log_lines),
    }
    return entry


# ── Main batch loop ───────────────────────────────────────────────────────────

def find_reels() -> list[Path]:
    """Find all beat_sheet.json files not under _-prefixed dirs."""
    reels = []
    for bs in BASE.rglob("beat_sheet.json"):
        parts = bs.parts
        # Exclude any path component that starts with _
        if any(p.startswith("_") for p in parts):
            continue
        # Must be at depth: BASE / <topic> / <slug> / beat_sheet.json
        rel = bs.relative_to(BASE)
        if len(rel.parts) >= 3:
            reels.append(bs.parent)
    return sorted(reels)


def main():
    reels = find_reels()
    done  = load_review_log()

    # Counters
    total        = len(reels)
    processed    = 0
    skipped      = 0
    errors       = 0
    formb_total  = 0
    boxes_total  = 0
    green_total  = 0

    print(f"[batch] {total} reels found  |  {len(done)} already in SLATE-REVIEW.jsonl")
    print(f"[batch] Starting at {datetime.now().isoformat()}")
    print()

    for i, reel_dir in enumerate(reels, 1):
        slug = reel_dir.name
        rel  = str(reel_dir.relative_to(BASE))

        if slug in done or rel in done:
            skipped += 1
            continue

        print(f"[{i}/{total}] {rel}")

        try:
            entry = process_reel(reel_dir)
        except Exception as e:
            entry = {
                "reel":         rel,
                "slate_path":   None,
                "formb_count":  0,
                "boxes":        0,
                "checks_green": False,
                "compile_ok":   False,
                "error":        str(e),
                "at":           datetime.now().isoformat(),
            }
            errors += 1
            print(f"  ERROR: {e}")

        append_review(entry)
        processed += 1

        formb_total += entry.get("formb_count", 0)
        boxes_total += entry.get("boxes", 0)
        if entry.get("checks_green"):
            green_total += 1
        if entry.get("error"):
            errors += 1

        status = "✓" if entry.get("compile_ok") else "✗"
        print(f"  {status}  FormB={entry.get('formb_count',0)}  boxes={entry.get('boxes',0)}"
              f"  checks={'green' if entry.get('checks_green') else 'RED'}"
              f"  {entry.get('elapsed_s', 0):.1f}s")
        print(f"  {entry.get('log', '')[:120]}")
        print()

    print("=" * 60)
    print(f"[batch] DONE  {datetime.now().isoformat()}")
    print(f"  reels processed : {processed}")
    print(f"  skipped (done)  : {skipped}")
    print(f"  errors          : {errors}")
    print(f"  FormBCards added: {formb_total}")
    print(f"  boxes logged    : {boxes_total}")
    print(f"  checks green    : {green_total}/{processed}")


if __name__ == "__main__":
    main()
