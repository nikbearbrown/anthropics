# TYPECHECK.md — GATE T

Reel: `plan-review-checklist`  |  Checked: 2026-08-10T04:04  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B01 | LANE_A | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 52px >= floor 35px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 56px >= floor 35px | PASS | — |
| B04 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 10 | 0 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
