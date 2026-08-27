# TYPECHECK.md — GATE T

Reel: `seven-field-brief`  |  Checked: 2026-08-10T04:02  |  Overall: PASS  |  Beats checked: 11  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | LANE_A | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 48px >= floor 35px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 51px >= floor 35px | PASS | — |
| B05 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 11 | 0 |
| overflow §8.2 | 11 | 0 |
| contrast §8.3 | 11 | 0 |
| contrast-local §8.3b | 11 | 0 |
| bbox-overlap §8.6b | 11 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
