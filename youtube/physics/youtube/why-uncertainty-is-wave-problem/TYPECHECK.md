# TYPECHECK.md — GATE T

Reel: `why-uncertainty-is-wave-problem`  |  Checked: 2026-08-01T15:07  |  Overall: PASS  |  Beats checked: 21  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A00 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| A01 | ? | min-size §8.1: min text-run height 43px >= floor 35px | PASS | — |
| A02 | ? | min-size §8.1: min text-run height 72px >= floor 35px | PASS | — |
| A03 | ? | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| A04 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A05 | ? | min-size §8.1: min text-run height 72px >= floor 35px | PASS | — |
| A06 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A08 | ? | min-size §8.1: min text-run height 93px >= floor 35px | PASS | — |
| A09 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A10 | ? | min-size §8.1: min text-run height 72px >= floor 35px | PASS | — |
| A11 | ? | min-size §8.1: min text-run height 72px >= floor 35px | PASS | — |
| A12 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A13 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A14 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A15 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A16 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 45px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 21 | 0 |
| overflow §8.2 | 21 | 0 |
| contrast §8.3 | 21 | 0 |
| contrast-local §8.3b | 21 | 0 |
| bbox-overlap §8.6b | 21 | 0 |
| kerning §8.4 | 17 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
