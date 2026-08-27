# TYPECHECK.md — GATE T

Reel: `claude-liam-combining-plugins`  |  Checked: 2026-08-26T10:24  |  Overall: **FAIL**  |  Beats checked: 39  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B23] narration recites the card (0.88) — discuss it, don't read it
> - §8.10 [V01] narration recites the card (0.93) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 95px >= floor 21px | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 22px >= floor 21px | PASS | — |
| B04 | MANIM | light | min-size §8.1: min text-run height 22px >= floor 21px (individual-char fallback at 1×) | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 69px >= floor 21px | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | MANIM | light | min-size §8.1: min text-run height 95px >= floor 21px | PASS | — |
| B11 | MANIM | light | min-size §8.1: min text-run height 34px >= floor 21px | PASS | — |
| B12 | MANIM | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B13 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 95px >= floor 21px | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 69px >= floor 21px | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 24px >= floor 21px | PASS | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| B21 | MANIM | light | min-size §8.1: min text-run height 95px >= floor 21px | PASS | — |
| B22 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C06 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 21px | PASS | — |
| B25 | MANIM | light | min-size §8.1: min text-run height 25px >= floor 21px | PASS | — |
| B26 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | dark | min-size §8.1: min text-run height 203px >= floor 41px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

### B12 (MANIM)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(338,350)–(717,446) ∩ blob@(605,394)–(639,415) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Separate label positions — two text elements overlap

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 17 | 0 |
| min-size §8.1 | 39 | 0 |
| overflow §8.2 | 39 | 0 |
| contrast §8.3 | 39 | 0 |
| contrast-local §8.3b | 39 | 0 |
| bbox-overlap §8.6b | 39 | 1 |
| card-clip §8.13 | 39 | 0 |
| kerning §8.4 | 15 | 0 |
| redundancy §8.10 (advisory) | 3 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
