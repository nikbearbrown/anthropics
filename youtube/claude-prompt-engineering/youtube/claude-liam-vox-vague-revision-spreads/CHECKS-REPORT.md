# CHECKS-REPORT — vox-vague-revision-spreads (FormBCard previz)

**Slate:** `vox-vague-revision-spreads-slate.mp4`
**Built:** 2026-07-27
**Cut:** slate (previz only — no 4K, no final, no post)

## Gates

| Gate | Result | Notes |
|---|---|---|
| GATE L (beat-mix lint) | PASS | |
| GATE BANNED-CARD | PASS | No SlateCard, no banned ClaudeWindow body beats |
| GATE V (frame-level QC) | WARN (ART_STRICT=0) | Gray slate frames flagged as expected for previz |
| GATE T (type-lock) | PASS | |
| GATE SHARPNESS | SKIPPED | Missing pillow/numpy deps |
| GATE BOOKEND | FAIL (expected) | Most beats still SLATE; required four-bookend structure not present |

## FormBCard beat

**B12** — Name Three Things (was: GRAPHIC/Manim B12_Practice)
- `icon: crosshair` → Change Target / name the new goal explicitly (cueFrame 70)
- `icon: snowflake` → Freeze List / lock in what's working (cueFrame 180)
- `icon: clipboard-list` → Change Log / track what shifted and why (cueFrame 285)
- `dark: false` (light card)
- All 3 icons: Lucide MIT, real SVG (zero BOX placeholders)
- Rendered: `media/B12.mp4` ✓

**Override note:** B12 was originally a GRAPHIC/Manim practice-drill beat. FormBCard replaces the Manim enumeration — Bear may prefer to restore Manim here (the three items are a practice checklist, not just a taxonomy, so Manim could add pedagogical value). Backup at `beat_sheet.json.bak-formb`.
