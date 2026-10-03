# TYPECHECK.md — GATE T

Reel: `claude-liam-data`  |  Checked: 2026-08-27T12:05  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B03 | MANIM | light | min-size §8.1: min text-run height 48px >= floor 20px | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 91px >= floor 13px | PASS | — |
| B07 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | MANIM | light | min-size §8.1: min text-run height 16px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B11 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B12 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 323px >= floor 13px | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 26px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B17 | MANIM | light | min-size §8.1: min text-run height 14px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B18 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | MANIM | light | min-size §8.1: min text-run height 15px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B20 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | MANIM | light | min-size §8.1: min text-run height 15px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B23 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B24 | MANIM | light | min-size §8.1: min text-run height 75px >= floor 13px | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 15 | 0 |
| min-size §8.1 | 36 | 0 |
| overflow §8.2 | 36 | 0 |
| contrast §8.3 | 36 | 0 |
| contrast-local §8.3b | 36 | 0 |
| bbox-overlap §8.6b | 36 | 0 |
| card-clip §8.13 | 36 | 0 |
| kerning §8.4 | 14 | 0 |
| redundancy §8.10 (advisory) | 3 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
