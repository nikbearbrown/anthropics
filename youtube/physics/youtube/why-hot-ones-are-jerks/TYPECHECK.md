# TYPECHECK.md — GATE T

Reel: `why-hot-ones-are-jerks`  |  Checked: 2026-08-01T15:43  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| A01 | ? | no video | SKIP | — |
| A02 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A03 | ? | no video | SKIP | — |
| A04 | ? | no video | SKIP | — |
| A05 | ? | no video | SKIP | — |
| A06 | ? | no video | SKIP | — |
| A07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A08 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A09 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A10 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A11 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A12 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A13 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A14 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A15 | ? | min-size §8.1: min text-run height 136px >= floor 35px | PASS | — |
| A16 | ? | min-size §8.1: min text-run height 69px >= floor 35px | PASS | — |
| A17 | ? | min-size §8.1: min text-run height 69px >= floor 35px | PASS | — |
| A18 | ? | min-size §8.1: min text-run height 193px >= floor 35px | PASS | — |
| A19 | ? | min-size §8.1: min text-run height 167px >= floor 35px | PASS | — |
| A20 | ? | min-size §8.1: min text-run height 167px >= floor 35px | PASS | — |
| A21 | ? | min-size §8.1: min text-run height 167px >= floor 35px | PASS | — |
| A22 | ? | no video | SKIP | — |
| BVDT | ? | min-size §8.1: min text-run height 73px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 20 | 0 |
| overflow §8.2 | 20 | 0 |
| contrast §8.3 | 20 | 0 |
| contrast-local §8.3b | 20 | 0 |
| bbox-overlap §8.6b | 20 | 0 |
| kerning §8.4 | 16 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
