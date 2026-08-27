# TYPECHECK.md — GATE T

Reel: `claude-liam-simple-fixed-content`  |  Checked: 2026-08-26T22:14  |  Overall: PASS  |  Beats checked: 19  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | — | no video | SKIP | — |
| S01 | ? | light | min-size §8.1: min text-run height 69px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| S02 | ? | light | min-size §8.1: min text-run height 71px >= floor 41px | PASS | — |
| S03 | ? | light | min-size §8.1: min text-run height 83px >= floor 41px | PASS | — |
| S04 | ? | light | min-size §8.1: min text-run height 46px >= floor 41px | PASS | — |
| S05 | ? | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| S06 | ? | light | min-size §8.1: min text-run height 72px >= floor 41px | PASS | — |
| S07 | ? | light | min-size §8.1: min text-run height 422px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| S08 | ? | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| S09 | ? | light | min-size §8.1: min text-run height 171px >= floor 41px | PASS | — |
| S10 | ? | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| S11 | ? | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| S12 | ? | light | min-size §8.1: min text-run height 83px >= floor 41px | PASS | — |
| S13 | ? | light | min-size §8.1: min text-run height 247px >= floor 41px | PASS | — |
| S14 | ? | light | min-size §8.1: min text-run height 67px >= floor 41px | PASS | — |
| S15 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| BCRY | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 96px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 18 | 0 |
| overflow §8.2 | 18 | 0 |
| contrast §8.3 | 18 | 0 |
| contrast-local §8.3b | 18 | 0 |
| bbox-overlap §8.6b | 18 | 0 |
| card-clip §8.13 | 18 | 0 |
| kerning §8.4 | 15 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
