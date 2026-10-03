# TYPECHECK.md — GATE T

Reel: `claude-liam-troubleshooting`  |  Checked: 2026-09-04T23:04  |  Overall: PASS  |  Beats checked: 27  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B03] narration recites the card (0.88) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 14px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B07 | MANIM | light | min-size §8.1: min text-run height 16px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | MANIM | light | min-size §8.1: min text-run height 163px >= floor 13px | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 17px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
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
| min-size §8.1 | 27 | 0 |
| overflow §8.2 | 27 | 0 |
| contrast §8.3 | 27 | 0 |
| contrast-local §8.3b | 27 | 0 |
| bbox-overlap §8.6b | 27 | 0 |
| card-clip §8.13 | 27 | 0 |
| kerning §8.4 | 5 | 0 |
| redundancy §8.10 (advisory) | 4 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
