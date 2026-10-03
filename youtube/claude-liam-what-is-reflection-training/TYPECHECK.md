# TYPECHECK.md — GATE T

Reel: `claude-liam-what-is-reflection-training`  |  Checked: 2026-09-01T13:22  |  Overall: PASS  |  Beats checked: 13  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 41px >= floor 41px | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 41px >= floor 41px | PASS | — |
| B04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | MANIM | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 41px >= floor 41px | PASS | — |
| B07 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'right.note') | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 9 words in 'chips[1]') | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 104px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 13 | 0 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 0 |
| card-clip §8.13 | 13 | 0 |
| kerning §8.4 | 5 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
