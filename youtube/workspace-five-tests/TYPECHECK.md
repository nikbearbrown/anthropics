# TYPECHECK.md — GATE T

Reel: `workspace-five-tests`  |  Checked: 2026-08-25T00:30  |  Overall: PASS  |  Beats checked: 18  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B11 | ? | light | min-size §8.1: min text-run height 181px >= floor 41px | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B13 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B14 | ? | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 10 words in 'sparkLine') | PASS | — |
| B15 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B16 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B17 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 18 | 0 |
| overflow §8.2 | 18 | 0 |
| contrast §8.3 | 18 | 0 |
| contrast-local §8.3b | 18 | 0 |
| bbox-overlap §8.6b | 18 | 0 |
| card-clip §8.13 | 18 | 0 |
| kerning §8.4 | 12 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
