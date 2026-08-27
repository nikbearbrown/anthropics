# TYPECHECK.md — GATE T

Reel: `workspace-jacobian-lens`  |  Checked: 2026-08-25T10:53  |  Overall: PASS  |  Beats checked: 17  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 198px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 301px >= floor 41px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B05 | ? | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'left.note') | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: hand-drawn pattern (B07_LensBakeoff) — §8.1 hachure/crossbar fragments are … | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B09 | ? | — | no video | SKIP | — |
| B10 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | light | min-size §8.1: hand-drawn pattern (B11_SingleTokenBlindSpot) — §8.1 hachure/crossbar fragm… | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B13 | ? | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 7 words in 'title') | PASS | — |
| B14 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 16 | 0 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 0 |
| card-clip §8.13 | 16 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
