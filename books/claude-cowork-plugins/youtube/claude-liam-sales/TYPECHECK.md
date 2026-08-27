# TYPECHECK.md — GATE T

Reel: `claude-liam-sales`  |  Checked: 2026-08-26T13:36  |  Overall: PASS  |  Beats checked: 37  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B04] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B19] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B23] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 17px >= floor 9px (individual-char fallback at 1×) | PASS | — |
| B03 | MANIM | — | no video | SKIP | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| B07 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 23px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B09 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| B12 | MANIM | — | no video | SKIP | — |
| B13 | MANIM | — | no video | SKIP | — |
| B14 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 39px >= floor 9px (individual-char fallback at 1×) | PASS | — |
| B16 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | — | no video | SKIP | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| C06 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| B22 | MANIM | — | no video | SKIP | — |
| B23 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | MANIM | — | no video | SKIP | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | dark | min-size §8.1: min text-run height 224px >= floor 41px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 16 | 0 |
| min-size §8.1 | 31 | 0 |
| overflow §8.2 | 31 | 0 |
| contrast §8.3 | 31 | 0 |
| contrast-local §8.3b | 31 | 0 |
| bbox-overlap §8.6b | 31 | 0 |
| card-clip §8.13 | 31 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 5 | 3 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
