# TYPECHECK.md — GATE T

Reel: `claude-liam-productivity`  |  Checked: 2026-08-26T21:04  |  Overall: PASS  |  Beats checked: 37  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B04] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [V01] narration recites the card (0.81) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 25px >= floor 21px | PASS | — |
| B03 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 117px >= floor 21px | PASS | — |
| B07 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | MANIM | light | min-size §8.1: min text-run height 26px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B12 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 16px >= floor 14px (individual-char fallback at 1×) | PASS | — |
| B14 | MANIM | light | min-size §8.1: min text-run height 38px >= floor 21px | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 16px >= floor 14px (individual-char fallback at 1×) | PASS | — |
| B17 | MANIM | light | min-size §8.1: min text-run height 24px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 14px >= floor 14px (individual-char fallback at 1×) | PASS | — |
| B19 | MANIM | light | min-size §8.1: min text-run height 58px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B20 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C06 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B23 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B24 | MANIM | light | min-size §8.1: min text-run height 93px >= floor 14px | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | dark | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 210px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 15 | 0 |
| min-size §8.1 | 37 | 0 |
| overflow §8.2 | 37 | 0 |
| contrast §8.3 | 37 | 0 |
| contrast-local §8.3b | 37 | 0 |
| bbox-overlap §8.6b | 37 | 0 |
| card-clip §8.13 | 37 | 0 |
| kerning §8.4 | 14 | 0 |
| redundancy §8.10 (advisory) | 3 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
