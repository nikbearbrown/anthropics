# TYPECHECK.md — GATE T

Reel: `claude-liam-simple-watermark`  |  Checked: 2026-08-15T11:33  |  Overall: PASS  |  Beats checked: 17  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | — | no video | SKIP | — |
| S01 | ? | light | min-size §8.1: min text-run height 92px >= floor 35px | PASS | — |
| S02 | ? | light | min-size §8.1: hand-drawn pattern (S02Scene) — §8.1 hachure/crossbar fragments are false p… | PASS | — |
| S03 | ? | light | min-size §8.1: min text-run height 96px >= floor 35px | PASS | — |
| S04 | ? | light | min-size §8.1: min text-run height 52px >= floor 35px | PASS | — |
| S05 | ? | light | min-size §8.1: hand-drawn pattern (S05Scene) — §8.1 hachure/crossbar fragments are false p… | PASS | — |
| S06 | ? | light | min-size §8.1: hand-drawn pattern (S06Scene) — §8.1 hachure/crossbar fragments are false p… | PASS | — |
| S07 | ? | light | min-size §8.1: min text-run height 72px >= floor 35px | PASS | — |
| S08 | ? | light | min-size §8.1: min text-run height 72px >= floor 35px | PASS | — |
| S09 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| S10 | ? | light | min-size §8.1: min text-run height 96px >= floor 35px | PASS | — |
| S11 | ? | light | min-size §8.1: hand-drawn pattern (S11Scene) — §8.1 hachure/crossbar fragments are false p… | PASS | — |
| S12 | ? | light | min-size §8.1: min text-run height 233px >= floor 35px | PASS | — |
| S13 | ? | light | min-size §8.1: min text-run height 233px >= floor 35px | PASS | — |
| BCRY | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 16 | 0 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 0 |
| kerning §8.4 | 13 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
