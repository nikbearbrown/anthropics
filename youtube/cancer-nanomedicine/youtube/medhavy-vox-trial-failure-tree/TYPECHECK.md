# TYPECHECK.md — GATE T

Reel: `vox-trial-failure-tree`  |  Checked: 2026-08-28T12:44  |  Overall: **FAIL**  |  Beats checked: 15  |  FAILs: 2

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | — | no video | SKIP | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | — | no video | SKIP | — |
| B04 | ? | light | min-size §8.1: min text-run height 18px >= floor 9px | PASS | — |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | light | min-size §8.1: min text-run height 13px >= floor 9px (individual-char fallback at 1×) | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 12px >= floor 9px | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 12px >= floor 9px (individual-char fallback at 1×) | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 10px >= floor 9px (individual-char fallback at 1×) | PASS | — |
| B10 | ? | light | contrast §8.3: mean fg/bg contrast 4.39:1 < 4.5:1 WCAG (fg≈(182, 72, 74), bg≈(243, 234, 22… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B11 | ? | — | no video | SKIP | — |
| B12 | ? | light | min-size §8.1: smallest text run 8px < floor 9px (1.9% of 480px logical); likely a caption… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B13 | ? | — | no video | SKIP | — |
| B14 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

### B10 (?)
- **contrast §8.3**: mean fg/bg contrast 4.39:1 < 4.5:1 WCAG (fg≈(182, 72, 74), bg≈(243, 234, 220))
- **Fix:** Use INK on cream; add backing plate under accent text

### B12 (?)
- **min-size §8.1**: smallest text run 8px < floor 9px (1.9% of 480px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 9 | 1 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 1 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| card-clip §8.13 | 9 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
