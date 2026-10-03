# TYPECHECK.md — GATE T

Reel: `vox-targeting-uptake`  |  Checked: 2026-08-28T16:25  |  Overall: PASS  |  Beats checked: 12  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | light | min-size §8.1: min text-run height 14px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 19px >= floor 13px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 57px >= floor 13px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 14px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 22px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 57px >= floor 13px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 39px >= floor 13px | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 20px >= floor 13px | PASS | — |
| B11 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| card-clip §8.13 | 9 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
