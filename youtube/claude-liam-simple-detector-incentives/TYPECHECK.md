# TYPECHECK.md — GATE T

Reel: `claude-liam-simple-detector-incentives`  |  Checked: 2026-08-15T20:01  |  Overall: PASS  |  Beats checked: 20  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | — | no video | SKIP | — |
| S01 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S02 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S03 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S04 | ? | light | min-size §8.1: min text-run height 761px >= floor 35px | PASS | — |
| S05 | ? | light | min-size §8.1: min text-run height 74px >= floor 35px | PASS | — |
| S06 | ? | light | min-size §8.1: min text-run height 79px >= floor 35px | PASS | — |
| S07 | ? | light | min-size §8.1: min text-run height 93px >= floor 35px | PASS | — |
| S08 | ? | light | min-size §8.1: min text-run height 93px >= floor 35px | PASS | — |
| S09 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S10 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S11 | ? | light | min-size §8.1: min text-run height 82px >= floor 35px | PASS | — |
| S12 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S13 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S14 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S15 | ? | light | min-size §8.1: min text-run height 269px >= floor 35px | PASS | — |
| S16 | ? | light | min-size §8.1: min text-run height 269px >= floor 35px | PASS | — |
| BCRY | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 97px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 19 | 0 |
| overflow §8.2 | 19 | 0 |
| contrast §8.3 | 19 | 0 |
| contrast-local §8.3b | 19 | 0 |
| bbox-overlap §8.6b | 19 | 0 |
| kerning §8.4 | 16 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
