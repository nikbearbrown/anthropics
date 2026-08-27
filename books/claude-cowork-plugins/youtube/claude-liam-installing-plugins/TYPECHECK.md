# TYPECHECK.md — GATE T

Reel: `claude-liam-installing-plugins`  |  Checked: 2026-08-26T18:01  |  Overall: PASS  |  Beats checked: 34  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B07] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B11] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 210px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 28 | 0 |
| min-size §8.1 | 34 | 0 |
| overflow §8.2 | 34 | 0 |
| contrast §8.3 | 34 | 0 |
| contrast-local §8.3b | 34 | 0 |
| bbox-overlap §8.6b | 34 | 0 |
| card-clip §8.13 | 34 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 11 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
