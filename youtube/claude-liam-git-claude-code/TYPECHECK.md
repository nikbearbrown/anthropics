# TYPECHECK.md — GATE T

Reel: `claude-liam-git-claude-code`  |  Checked: 2026-08-01T18:52  |  Overall: PASS  |  Beats checked: 20  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 147px >= floor 35px | PASS | — |
| B05 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B05b | ? | min-size §8.1: min text-run height 41px >= floor 35px | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B08 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | min-size §8.1: min text-run height 48px >= floor 35px | PASS | — |
| B11 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11b | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | min-size §8.1: min text-run height 73px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B17 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 11 | 0 |
| min-size §8.1 | 20 | 0 |
| overflow §8.2 | 20 | 0 |
| contrast §8.3 | 20 | 0 |
| contrast-local §8.3b | 20 | 0 |
| bbox-overlap §8.6b | 20 | 0 |
| kerning §8.4 | 5 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
