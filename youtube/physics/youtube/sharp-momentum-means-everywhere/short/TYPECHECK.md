# TYPECHECK.md — GATE T

Reel: `sharp-momentum-means-everywhere-short`  |  Checked: 2026-08-01T15:41  |  Overall: PASS  |  Beats checked: 15  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 64px >= floor 31px | PASS | — |
| H01 | ? | min-size §8.1: min text-run height 88px >= floor 35px | PASS | — |
| H02 | ? | min-size §8.1: min text-run height 88px >= floor 35px | PASS | — |
| A01 | ? | min-size §8.1: min text-run height 88px >= floor 35px | PASS | — |
| A02 | ? | min-size §8.1: min text-run height 88px >= floor 35px | PASS | — |
| A03 | ? | min-size §8.1: min text-run height 88px >= floor 35px | PASS | — |
| A04 | ? | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |
| A05 | ? | min-size §8.1: min text-run height 53px >= floor 35px | PASS | — |
| A06 | ? | min-size §8.1: min text-run height 88px >= floor 35px | PASS | — |
| A07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A08 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 35px >= floor 31px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 64px >= floor 31px | PASS | — |
| BOUT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| END | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 14 | 0 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 0 |
| kerning §8.4 | 10 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
