# TYPECHECK.md — GATE T

Reel: `why-schrodingers-cat-is-not-about-cats-short`  |  Checked: 2026-08-01T15:16  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 83px >= floor 31px | PASS | — |
| A00 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A01 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A02 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| A03 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A04 | ? | min-size §8.1: min text-run height 70px >= floor 35px | PASS | — |
| A05 | ? | min-size §8.1: min text-run height 331px >= floor 35px | PASS | — |
| A06 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A08 | ? | min-size §8.1: min text-run height 37px >= floor 35px | PASS | — |
| A09 | ? | min-size §8.1: min text-run height 331px >= floor 35px | PASS | — |
| A10 | ? | min-size §8.1: min text-run height 139px >= floor 35px | PASS | — |
| A11 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A12 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A13 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A14 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A15 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A16 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A17 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A18 | ? | min-size §8.1: min text-run height 411px >= floor 35px | PASS | — |
| A19 | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| A20 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 57px >= floor 31px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 83px >= floor 31px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 151px >= floor 31px | PASS | — |
| END | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 25 | 0 |
| overflow §8.2 | 25 | 0 |
| contrast §8.3 | 25 | 0 |
| contrast-local §8.3b | 25 | 0 |
| bbox-overlap §8.6b | 25 | 0 |
| kerning §8.4 | 21 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
