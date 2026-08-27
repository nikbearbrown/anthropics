# TYPECHECK.md — GATE T

Reel: `claude-liam-enterprise-search`  |  Checked: 2026-08-26T16:00  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B11] narration recites the card (0.89) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 369px >= floor 14px | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 22px >= floor 21px | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | MANIM | light | min-size §8.1: min text-run height 109px >= floor 14px | PASS | — |
| B05 | MANIM | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 63px >= floor 14px | PASS | — |
| B09 | MANIM | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | MANIM | light | min-size §8.1: min text-run height 14px >= floor 14px (individual-char fallback at 1×) | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 43px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B14 | MANIM | light | min-size §8.1: min text-run height 28px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B15 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 59px >= floor 14px | PASS | — |
| B17 | MANIM | light | min-size §8.1: min text-run height 38px >= floor 21px | PASS | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 15px >= floor 14px (individual-char fallback at 1×) | PASS | — |
| B19 | MANIM | light | min-size §8.1: min text-run height 14px >= floor 14px (individual-char fallback at 1×) | PASS | — |
| B20 | MANIM | light | min-size §8.1: min text-run height 26px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| C06 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | MANIM | light | min-size §8.1: min text-run height 29px >= floor 14px | PASS | — |
| B23 | MANIM | light | min-size §8.1: min text-run height 46px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 203px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 12 | 0 |
| min-size §8.1 | 36 | 0 |
| overflow §8.2 | 36 | 0 |
| contrast §8.3 | 36 | 0 |
| contrast-local §8.3b | 36 | 0 |
| bbox-overlap §8.6b | 36 | 0 |
| card-clip §8.13 | 36 | 0 |
| kerning §8.4 | 16 | 0 |
| redundancy §8.10 (advisory) | 4 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
