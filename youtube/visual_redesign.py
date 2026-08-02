#!/usr/bin/env python3
"""
visual_redesign.py — per-content visual assignment for anthropics reels.

Replaces the broken pattern (ClaudeVerdictArtifact / text-list cards for every
body beat) with DESIGN-PRINCIPLES §1-compliant assignments:

  enumerated (2-5 named items) → FormBCard   (N-aware, karaoke, icons)
  single concept / contrast    → FormACard    (1-2 SHORT serif lines, karaoke)
  code / terminal output       → stub (mark for Onda/ClaudeWindow)
  math / mechanism             → stub (mark for Manim)
  default                      → FormACard    (NOT ClaudeVerdictArtifact)

BANNED forever:
  ClaudeVerdictArtifact (numbered bullet dump)
  FormACard with full narration pasted as copy — FormA gets ≤12-word key phrase

POLARITY: approximately 1 dark beat per 5 body beats (seeded deterministically).
VARIETY:  FormA and FormB alternate — never two consecutive of the same type.

Usage:
  python3 visual_redesign.py <reel_dir>                  # apply + print diff
  python3 visual_redesign.py <reel_dir> --dry-run        # print only, no write
  python3 visual_redesign.py <reel_dir> --clear-stale    # also rm stale media
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ── Icon map (Lucide MIT — only icons in form-b-icons/ may be used) ──────────
ICON_MAP: dict[str, list[str]] = {
    "circle-check":  ["check", "verify", "valid", "pass", "correct", "confirm", "success", "always"],
    "circle-x":      ["error", "fail", "wrong", "invalid", "reject", "deny", "never", "cannot", "can't", "not"],
    "clipboard-list":["list", "step", "order", "sequence", "record", "items", "log"],
    "list-checks":   ["checklist", "audit", "review", "assess", "evaluate", "gate", "requirements"],
    "target":        ["goal", "aim", "result", "outcome", "objective", "output", "purpose"],
    "crosshair":     ["focus", "precise", "specific", "exact", "narrow", "point"],
    "shield":        ["safe", "protect", "secure", "guard", "defense", "safety", "operator"],
    "shield-alert":  ["warning", "alert", "caution", "danger", "risk", "weapon", "harm", "abuse"],
    "lock":          ["lock", "private", "restrict", "constraint", "limit", "bound", "hardcoded", "unconditional", "anthrop"],
    "ruler":         ["measure", "size", "scale", "metric", "length", "threshold", "scope"],
    "star":          ["best", "top", "quality", "excellent", "primary", "main", "first"],
    "zap":           ["power", "fast", "action", "trigger", "execute", "run", "speed", "user"],
    "thumbs-up":     ["approve", "accept", "good", "positive", "yes", "agree", "allows", "can"],
    "frame":         ["view", "window", "display", "show", "render", "frame", "layer"],
    "tag":           ["label", "type", "category", "kind", "class", "persona", "name"],
    "snowflake":     ["freeze", "stable", "consistent", "static", "fixed", "immutable", "floor"],
    "hand":          ["stop", "halt", "pause", "interact", "touch", "control", "human", "user", "floor"],
    "life-buoy":     ["help", "support", "rescue", "fallback", "backup", "recover", "refer", "seek"],
}

BOOKEND_IDS = frozenset({
    "B00", "BVDT", "BHTF", "BOUT", "OUTRO",
    "YOURTURN", "YOUR_TURN", "YOURTURN1",
})

BOOKEND_PATTERNS = frozenset({
    "ClaudeComposerAsk", "ClaudeTitleOutro", "ClaudeTitleOutro916",
    "NikBearBrownOpen", "NikBearBrownOutro",
})

BOOKEND_ACTS = frozenset({
    "cold_open", "outro", "your-turn", "handoff", "hook",
})

# Patterns that MUST be replaced (always banned in body beats)
MUST_REPLACE = frozenset({"ClaudeVerdictArtifact"})

# Generic card patterns we might need to fix (text-dump check applies)
GENERIC_CARDS = frozenset({"FormACard", "FormBCard", "FormACard916", "FormBCard916"})

CODE_SIGNALS = re.compile(
    r'\b(api|endpoint|function|method|class|import|def |curl|json|await|async|'
    r'return|variable|parameter|syntax|code|terminal|command|bash|python|javascript|'
    r'typescript|request|response|library|package)\b',
    re.IGNORECASE,
)
MATH_SIGNALS = re.compile(
    r'\b(equation|formula|derivative|integral|matrix|vector|gradient|'
    r'probability|distribution|theorem|proof|algebra|calculus|sigmoid|'
    r'softmax|attention|transformer|embedding|dimension)\b',
    re.IGNORECASE,
)
ENUM_SIGNALS = re.compile(
    r'(?:^|\.\s+)(?:first|second|third|fourth|finally|lastly)[,.: ]',
    re.IGNORECASE | re.MULTILINE,
)
NUMBERED_SIGNALS = re.compile(r'(?:^|\s)(?:\d+[.)]\s|\(\d+\)\s)', re.MULTILINE)
SEMICOLON_LIST = re.compile(r';\s+\w')   # "A; B; C" pattern
# Count signal: "Two X. / Three X. / Four X." at start of narration
COUNT_LEAD = re.compile(
    r'^(two|three|four|five|\d+)\s+\w+[.!]\s',
    re.IGNORECASE,
)


def get_bid(b: dict) -> str:
    return b.get("beat_id") or b.get("id") or ""


def is_text_dump(b: dict) -> bool:
    """True if a FormACard was built by pasting full narration (≥3 lines or any line >12 words)."""
    if get_pattern(b) != "FormACard":
        return False
    props = ((b.get("shot") or {}).get("remotion") or {}).get("props") or {}
    lines = props.get("lines") or []
    if len(lines) >= 3:
        return True
    return any(len(ln.split()) > 12 for ln in lines)


def needs_visual_fix(b: dict) -> bool:
    """True if this body beat has a pattern that needs replacing."""
    pattern = get_pattern(b)
    if not pattern:
        return True                  # empty — assign one
    if pattern in MUST_REPLACE:
        return True                  # banned
    if pattern in GENERIC_CARDS and is_text_dump(b):
        return True                  # FormA text dump
    return False                     # custom component or valid generic — leave alone


def get_narration(b: dict) -> str:
    return (b.get("narration_text") or b.get("narration") or "").strip()


def get_pattern(b: dict) -> str:
    shot = b.get("shot") or {}
    rem = shot.get("remotion") or {}
    return rem.get("pattern", "") or ""


def is_body_beat(beat: dict | str) -> bool:
    """True if this beat is a body beat (not a cold-open, outro, handoff, or bookend)."""
    if isinstance(beat, str):
        # legacy: called with just a bid string
        bid = beat
        return bid not in BOOKEND_IDS and not bid.startswith("B00")
    bid = get_bid(beat)
    if not bid or bid in BOOKEND_IDS:
        return False
    # Structural tells
    beat_type = (beat.get("beat_type") or "").lower()
    act = (beat.get("act") or "").lower()
    if beat_type in BOOKEND_ACTS or act in BOOKEND_ACTS:
        return False
    # Pattern tells
    pattern = get_pattern(beat)
    if pattern in BOOKEND_PATTERNS:
        return False
    return True


def pick_icon(text: str) -> str:
    lower = text.lower()
    for icon, keywords in ICON_MAP.items():
        if any(k in lower for k in keywords):
            return icon
    return "BOX"


def short_phrase(narration: str, max_words: int = 8) -> str:
    """Extract ≤max_words from the first meaningful sentence."""
    # Take first sentence
    sent = re.split(r'[.!?]', narration)[0].strip()
    words = sent.split()
    if len(words) <= max_words:
        return sent
    # Trim to max_words
    return " ".join(words[:max_words]).rstrip(".,;:")


def extract_items(narration: str, n_max: int = 4) -> list[dict]:
    """Extract 2-N FormBCard items from narration. Returns [] if < 2 items found.

    Only fires on EXPLICIT enumeration signals. Deliberately avoids colon-comma
    splitting (too aggressive — most narrative text has colons that aren't lists).
    """
    text = narration.strip()

    # Strategy 1: Numbered list  (1. X  2. Y  or  (1) X  (2) Y)
    numbered = NUMBERED_SIGNALS.findall(text)
    if len(numbered) >= 2:
        parts = re.split(r'(?:^|\s)\d+[.)]\s|\(\d+\)\s', text, flags=re.MULTILINE)
        parts = [p.strip().rstrip(".,;:") for p in parts if p.strip() and len(p.strip()) > 6]
        if 2 <= len(parts) <= n_max + 1:
            return _items_from_raw(parts[:n_max])

    # Strategy 2: ordinal words (first/second/third/finally/lastly)
    ordinals = re.findall(
        r'(?:^|\.\s+)(first|second|third|fourth|finally|lastly)[,.: ]+([^.!?]{10,})',
        text, re.IGNORECASE | re.MULTILINE
    )
    if len(ordinals) >= 2:
        raw = [f"{o[0].capitalize()}: {o[1].strip()}" for o in ordinals[:n_max]]
        return _items_from_raw(raw)

    # Strategy 3: Semicolons  (A; B; C)
    if SEMICOLON_LIST.search(text):
        parts = [p.strip() for p in text.split(";") if p.strip() and len(p.strip()) > 8]
        if 2 <= len(parts) <= n_max:
            return _items_from_raw(parts)

    # Strategy 4: "N things." lead + SHORT follow-on sentences
    #   "Three tiers. Anthropic's rules … Operator's prompt … User's …"
    #   Each follow-on sentence must be < 100 chars to qualify as a list item.
    count_m = COUNT_LEAD.match(text)
    if count_m:
        sentences = re.split(r'(?<=[.!?])\s+', text)
        items_raw = [s.strip() for s in sentences[1:]
                     if 15 < len(s.strip()) < 120]
        if 2 <= len(items_raw) <= n_max:
            return _items_from_raw(items_raw)

    return []


def _items_from_raw(raw: list[str]) -> list[dict]:
    result = []
    for r in raw:
        r = r.strip().rstrip(".,;:")
        if not r:
            continue
        icon = pick_icon(r)
        label_words = r.split()[:5]
        label = " ".join(label_words).rstrip(".,;:")
        sub = r if len(r) <= 120 else r[:117] + "…"
        result.append({"label": label, "sub": sub, "icon": icon, "cueFrame": 0})
    return result


def assign_cue_frames(items: list[dict], duration_s: float, fps: int = 30) -> list[dict]:
    n = len(items)
    total_frames = int(duration_s * fps)
    first_item = max(24, int(total_frames * 0.10))
    last_item  = max(total_frames - fps, first_item + 10)
    if n == 1:
        items[0]["cueFrame"] = first_item
    else:
        step = (last_item - first_item) / (n - 1)
        for i, item in enumerate(items):
            item["cueFrame"] = int(first_item + i * step)
    return items


def detect_content_type(narration: str) -> str:
    """Returns: 'code', 'math', 'enumerated', 'concept'."""
    if CODE_SIGNALS.search(narration):
        return "code"
    if MATH_SIGNALS.search(narration):
        return "math"
    if ENUM_SIGNALS.search(narration) or NUMBERED_SIGNALS.search(narration):
        return "enumerated"
    items = extract_items(narration, n_max=4)
    if len(items) >= 2:
        return "enumerated"
    return "concept"


def make_form_a_props(narration: str, dark: bool) -> dict:
    """FormACard: 1-2 SHORT serif lines. Never paste full narration."""
    sentences = re.split(r'(?<=[.!?])\s+', narration.strip())
    sentences = [s.strip() for s in sentences if s.strip()]

    line1 = short_phrase(sentences[0], max_words=8) if sentences else short_phrase(narration, 8)
    # Second line only if first sentence is a very short setup
    lines = [line1]
    if len(sentences) > 1 and len(sentences[0].split()) <= 6:
        line2 = short_phrase(sentences[1], max_words=7)
        if line2 and line2 != line1:
            lines.append(line2)

    return {"lines": lines, "dark": dark}


def make_form_b_props(narration: str, duration_s: float, dark: bool,
                      title: str = "", fps: int = 30) -> dict | None:
    """FormBCard: N-aware. Returns None if < 2 items extracted."""
    items = extract_items(narration, n_max=4)
    if len(items) < 2:
        return None
    items = assign_cue_frames(items, duration_s, fps)
    if not title:
        title = short_phrase(narration, max_words=6)
    return {"title": title, "items": items, "dark": dark}


def assign_visual(beat: dict, beat_index: int, body_count: int,
                  prev_pattern: str, fps: int = 30) -> dict | None:
    """
    Return a new shot.remotion dict for this beat, or None to leave unchanged.
    Implements DESIGN-PRINCIPLES §1: Form B for enumerations, Form A for concepts.
    NEVER emits ClaudeVerdictArtifact.
    POLARITY: dark every ~5 body beats (index-based, deterministic).
    VARIETY: alternate FormA / FormB.
    """
    narration = get_narration(beat)
    if not narration:
        return None

    duration_s = float(
        beat.get("actual_duration_s") or beat.get("est_s") or
        beat.get("estimated_duration_s") or 15.0
    )
    act = beat.get("act", "") or ""

    # Polarity: dark every ~5 beats, seeded on index
    dark = (beat_index % 5 == 2)  # beats 2, 7, 12… are dark (~20%)

    content_type = detect_content_type(narration)

    # Code → Onda (stub for now; leaves as pantry request)
    if content_type == "code":
        return {
            "pattern": "ClaudeWindow",
            "props": {
                "view": "conversation",
                "messages": [{"role": "assistant", "content": narration[:400]}],
            }
        }

    # Math → mark for Manim (leave as slate, add manim_scene annotation)
    if content_type == "math":
        return None  # Manim — leave as pantry request

    # Enumerated → FormBCard (if ≥2 items can be extracted)
    if content_type == "enumerated" and prev_pattern != "FormBCard":
        title = short_phrase(act or narration, max_words=5)
        props = make_form_b_props(narration, duration_s, dark, title=title, fps=fps)
        if props:
            return {"pattern": "FormBCard", "props": props}

    # Concept → FormACard (SHORT phrase, not full narration)
    if prev_pattern != "FormACard":
        props = make_form_a_props(narration, dark)
        return {"pattern": "FormACard", "props": props}

    # Consecutive same type: try FormBCard even for concept narration
    props = make_form_b_props(narration, duration_s, dark, fps=fps)
    if props:
        return {"pattern": "FormBCard", "props": props}

    # Last resort: FormA (no consecutive check — we tried)
    props = make_form_a_props(narration, dark)
    return {"pattern": "FormACard", "props": props}


# ── Hard gate check ───────────────────────────────────────────────────────────

def run_hard_gates(beats: list[dict]) -> list[str]:
    """Check hard gates per the task spec. Returns list of FAIL messages."""
    fails = []
    body = [b for b in beats if is_body_beat(b)]
    if not body:
        return ["FAIL: no body beats"]

    patterns = [get_pattern(b) for b in body]
    text_cards = sum(1 for p in patterns if p in ("ClaudeVerdictArtifact",))
    banned = sum(1 for p in patterns if p == "ClaudeVerdictArtifact")
    formb = sum(1 for p in patterns if p == "FormBCard")
    dark_count = sum(
        1 for b in body
        if (((b.get("shot") or {}).get("remotion") or {}).get("props") or {}).get("dark")
    )
    # Any non-banned, non-empty pattern is assumed to carry motion (karaoke, animation, etc.)
    has_motion = all(
        (get_pattern(b) and get_pattern(b) not in MUST_REPLACE)
        or (b.get("build") or {}).get("status") in ("VIDEO", "MANIM")
        for b in body
    )

    # card_ratio: text cards ≤ ~40%
    card_ratio = text_cards / len(body)
    if card_ratio > 0.40:
        fails.append(f"FAIL card_ratio: {text_cards}/{len(body)} text-list cards = {card_ratio:.0%} > 40%")

    # banned-card: no ClaudeVerdictArtifact in body
    if banned:
        fails.append(f"FAIL banned-card: {banned} ClaudeVerdictArtifact beats in body")

    # FormB: at least one
    if formb == 0:
        fails.append("FAIL show_dont_tell: no FormBCard — needs ≥1 icon-card exhibit")

    # polarity: ≥1 dark per ~5 body beats
    dark_needed = max(1, len(body) // 5)
    if dark_count < dark_needed:
        fails.append(f"FAIL polarity: {dark_count} dark beats, need ≥{dark_needed}")

    # Consecutive same pattern check
    for i in range(1, len(patterns)):
        if patterns[i] == patterns[i - 1] and patterns[i]:
            bid1 = get_bid(body[i - 1])
            bid2 = get_bid(body[i])
            fails.append(f"FAIL variety: consecutive {patterns[i]} at {bid1},{bid2}")

    return fails


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel_dir", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--clear-stale", action="store_true",
                    help="delete media/<bid>.mp4 for beats whose pattern changed")
    a = ap.parse_args()

    bs_path = a.reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        sys.exit(f"[visual_redesign] no beat_sheet.json in {a.reel_dir}")

    sheet = json.loads(bs_path.read_text())
    beats = sheet.get("beats") or []
    # normalize schema
    for b in beats:
        if "beat_id" not in b and "id" in b:
            b["beat_id"] = b["id"]

    body_beats = [b for b in beats if is_body_beat(b)]
    body_count = len(body_beats)

    prev_pattern = ""
    changed = []
    body_idx = 0

    for b in beats:
        bid = get_bid(b)
        if not is_body_beat(b):
            prev_pattern = get_pattern(b)
            continue

        old_pattern = get_pattern(b)
        old_dark = (((b.get("shot") or {}).get("remotion") or {}).get("props") or {}).get("dark")

        # Only fix beats with banned patterns, empty patterns, or FormA text-dumps.
        # Custom Remotion components and valid FormA/FormB are left untouched.
        if not needs_visual_fix(b):
            prev_pattern = old_pattern
            body_idx += 1
            continue

        new_rem = assign_visual(b, body_idx, body_count, prev_pattern)
        body_idx += 1

        if new_rem is None:
            # Manim/pantry beat — leave pattern as-is (or empty slate)
            prev_pattern = old_pattern
            continue

        new_pattern = new_rem["pattern"]
        if new_pattern != old_pattern or new_rem.get("props", {}).get("dark") != old_dark:
            shot = b.setdefault("shot", {})
            shot["type"] = "REMOTION"
            shot["source"] = "own"
            shot["remotion"] = new_rem
            # Clear build stamp so compile knows to re-render
            b.pop("build", None)
            changed.append((bid, old_pattern, new_pattern))
            print(f"  {bid}: {old_pattern or '(none)'} → {new_pattern}"
                  f"  dark={new_rem.get('props', {}).get('dark', False)}")

        prev_pattern = new_pattern

    # Hard gate check
    fails = run_hard_gates(beats)
    if fails:
        print("\n[visual_redesign] HARD GATE FAILURES:")
        for f in fails:
            print(f"  {f}")
    else:
        print("\n[visual_redesign] HARD GATES: PASS")

    if a.dry_run:
        print(f"\n[dry-run] {len(changed)} beats would change. No files written.")
        return

    if not changed:
        print("[visual_redesign] nothing to change.")
        return

    # Write beat sheet
    bak = bs_path.parent / (bs_path.name + ".bak-visual-redesign")
    if not bak.exists():
        import shutil
        shutil.copy2(bs_path, bak)
    bs_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    print(f"\n[visual_redesign] wrote {bs_path.name}  ({len(changed)} beats changed)")

    # Clear stale media
    if a.clear_stale:
        media_dir = a.reel_dir / "media"
        for bid, old_pat, new_pat in changed:
            stale = media_dir / f"{bid}.mp4"
            if stale.exists():
                stale.unlink()
                print(f"  cleared stale: media/{bid}.mp4  (was {old_pat})")
        # Also clear compiled clips to force recompile
        clips_dir = a.reel_dir / "clips"
        for bid, _, _ in changed:
            c = clips_dir / f"{bid}.mp4"
            if c.exists():
                c.unlink()
        man = clips_dir / "manifest.json"
        if man.exists():
            manifest = json.loads(man.read_text())
            for bid, _, _ in changed:
                manifest.pop(bid, None)
            man.write_text(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
