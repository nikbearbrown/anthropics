# CHECKS-REPORT — criteria-first-habit (FormBCard previz)

**Slate:** `criteria-first-habit-slate.mp4`
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
| GATE BOOKEND | FAIL (expected) | Incomplete reel — B00/B05/B06 still SLATE; required four-bookend structure not present |

## FormBCard beat

**B01** — Four Criteria Types
- `icon: target` → Accuracy / traceable to source (cueFrame 100)
- `icon: list-checks` → Completeness / every section accounted for (cueFrame 270)
- `icon: frame` → Format / shape of the output (cueFrame 450)
- `icon: circle-x` → Failure / wrong regardless of merit (cueFrame 620)
- `dark: false` (light card)
- All 4 icons: Lucide MIT, real SVG (zero BOX placeholders)
- Rendered: `media/B01.mp4` ✓

---

## FormBCard N-aware recheck — 2026-07-28

**Component version:** N-aware layout table + calculateMetadata + height-based font floor.

| Check | Result | Detail |
|-------|--------|--------|
| GATE T | **PASS** | label 43px, sub 39px — both above 35px floor (was FAIL on sub before floor fix) |
| GATE BANNED-CARD | **PASS** | No banned patterns |
| SKIN LINT | WARN B00/B06 | Pre-existing (cold open / outro un-annotated); not FormBCard scope |
| Final frame — all N items appear | **PASS** | cueFrame 620 now within 710-frame composition (calculateMetadata) |
| N=4 four-up layout | **PASS** | Single row, panels centered, karaoke accumulate-and-stay |
| 0 BOX placeholders | **PASS** | target ✓ list-checks ✓ frame ✓ circle-x ✓ — all in library |
| Visual QC (8-pt) | **PASS** | See detail below |

**Visual detail:** cream ground, PILL panels, EB Garamond labels/sub, 44px Lucide icons, no eyebrow/blob/rule, generous top/bottom space, polarity light ✓. Four-up row fits 1920px frame with ~12% margins on each side. Final frame shows all 4 panels fully revealed.

**Slate path:** `claude-prompt-engineering/youtube/claude-liam-criteria-first-habit/criteria-first-habit.mp4`

STOP — slate only. No 4K / art post / publish.
