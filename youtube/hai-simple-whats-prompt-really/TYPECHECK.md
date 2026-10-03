# TYPECHECK.md — GATE T

Reel: `hai-simple-whats-prompt-really`  |  Checked: 2026-08-27T13:00  |  Overall: PASS  |  Beats checked: 15  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: min text-run height 77px >= floor 41px | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 83px >= floor 41px | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 66px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 69px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 48px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 83px >= floor 41px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 415px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 69px >= floor 41px | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 42px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| B11 | ? | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| BCRY | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 15 | 0 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| card-clip §8.13 | 15 | 0 |
| kerning §8.4 | 11 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
