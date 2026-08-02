# TYPECHECK.md — GATE T

Reel: `claude-constitution-corrigibility-dial`  |  Checked: 2026-08-01T02:38  |  Overall: **FAIL**  |  Beats checked: 16  |  FAILs: 4

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | REMOTION | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A10 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A11 | MANIM | contrast-local §8.3b: per-blob contrast 2.00:1 < 3.0:1 — text unreadable on actual local b… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A20 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A21 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A30 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A31 | CARD | contrast-local §8.3b: per-blob contrast 1.76:1 < 3.0:1 — text unreadable on actual local b… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A40 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A41 | MANIM | min-size §8.1: smallest text run 32px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| A50 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A51 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| EX | MANIM | contrast-local §8.3b: per-blob contrast 1.80:1 < 3.0:1 — text unreadable on actual local b… | **FAIL** | Use INK on cream; add backing plate under accent text |
| BVDT | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

### A11 (MANIM)
- **contrast-local §8.3b**: per-blob contrast 2.00:1 < 3.0:1 — text unreadable on actual local background (blob@(1003,567)–(2836,794) fg≈(59, 40, 31) bg≈(124, 78, 60)); move label off its background or change text color
- **Fix:** Use INK on cream; add backing plate under accent text

### A31 (CARD)
- **contrast-local §8.3b**: per-blob contrast 1.76:1 < 3.0:1 — text unreadable on actual local background (blob@(2192,705)–(3529,1216) fg≈(59, 40, 31) bg≈(111, 72, 56)); move label off its background or change text color
- **Fix:** Use INK on cream; add backing plate under accent text

### A41 (MANIM)
- **min-size §8.1**: smallest text run 32px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### EX (MANIM)
- **contrast-local §8.3b**: per-blob contrast 1.80:1 < 3.0:1 — text unreadable on actual local background (blob@(843,700)–(3532,1221) fg≈(46, 73, 52) bg≈(150, 89, 66)); move label off its background or change text color
- **Fix:** Use INK on cream; add backing plate under accent text

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 13 | 0 |
| min-size §8.1 | 16 | 1 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 3 |
| bbox-overlap §8.6b | 16 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
