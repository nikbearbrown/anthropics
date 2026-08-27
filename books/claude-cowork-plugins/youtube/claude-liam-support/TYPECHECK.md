# TYPECHECK.md — GATE T

Reel: `claude-liam-support`  |  Checked: 2026-08-27T04:39  |  Overall: PASS  |  Beats checked: 31  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B04] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B17] narration recites the card (0.86) — discuss it, don't read it
> - §8.10 [BVDT] narration recites the card (0.88) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | MANIM | light | min-size §8.1: min text-run height 46px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 33px >= floor 13px | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 87px >= floor 13px | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 369px >= floor 13px | PASS | — |
| B07 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 26px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | MANIM | light | min-size §8.1: min text-run height 107px >= floor 13px | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 28px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B14 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 71px >= floor 13px | PASS | — |
| B16 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 38px >= floor 20px | PASS | — |
| B19 | MANIM | light | min-size §8.1: min text-run height 14px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B20 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | dark | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |
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
| no-wordy-card §8.5 | 13 | 0 |
| min-size §8.1 | 31 | 0 |
| overflow §8.2 | 31 | 0 |
| contrast §8.3 | 31 | 0 |
| contrast-local §8.3b | 31 | 0 |
| bbox-overlap §8.6b | 31 | 0 |
| card-clip §8.13 | 31 | 0 |
| kerning §8.4 | 11 | 0 |
| redundancy §8.10 (advisory) | 4 | 3 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
