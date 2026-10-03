# TYPECHECK.md — GATE T

Reel: `claude-liam-the-missing-feedback-loop`  |  Checked: 2026-08-31T16:26  |  Overall: PASS  |  Beats checked: 29  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 43px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | VOX | — | no video | SKIP | — |
| B05 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 7 words in 'left.note') | PASS | — |
| B06 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| B09 | VOX | — | no video | SKIP | — |
| B10 | MANIM | light | min-size §8.1: min text-run height 261px >= floor 41px | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 6 words in 'sparkLine') | PASS | — |
| B12 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | VOX | — | no video | SKIP | — |
| B14 | MANIM | light | min-size §8.1: min text-run height 121px >= floor 41px | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B16 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'right.note') | PASS | — |
| B17 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B18 | VOX | — | no video | SKIP | — |
| B19 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 11 words in 'chips[2]') | PASS | — |
| B20 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | MANIM | light | min-size §8.1: min text-run height 94px >= floor 41px | PASS | — |
| B22 | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 10 words in 'chips[0]') | PASS | — |
| B23 | VOX | — | no video | SKIP | — |
| B24 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | MANIM | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 11 | 0 |
| min-size §8.1 | 24 | 0 |
| overflow §8.2 | 24 | 0 |
| contrast §8.3 | 24 | 0 |
| contrast-local §8.3b | 24 | 0 |
| bbox-overlap §8.6b | 24 | 0 |
| card-clip §8.13 | 24 | 0 |
| kerning §8.4 | 9 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
