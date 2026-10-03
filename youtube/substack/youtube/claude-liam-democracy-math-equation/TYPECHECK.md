# TYPECHECK.md — GATE T

Reel: `claude-liam-democracy-math-equation`  |  Checked: 2026-09-07T13:15  |  Overall: PASS  |  Beats checked: 41  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 76px >= floor 41px | PASS | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | light | min-size §8.1: diegetic-palette pattern (B05_ReverseEngineerBox) — geometric ink markers a… | PASS | — |
| B06 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B09 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | — | no video | SKIP | — |
| B11 | ? | — | no video | SKIP | — |
| B12 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B15 | ? | light | min-size §8.1: diegetic-palette pattern (B15_LogitCurve) — geometric ink markers are notat… | PASS | — |
| B16 | ? | light | min-size §8.1: diegetic-palette pattern (B16_TwoCol) — geometric ink markers are notation,… | PASS | — |
| B17 | ? | light | min-size §8.1: diegetic-palette pattern (B17_BetaPol) — geometric ink markers are notation… | PASS | — |
| B18 | ? | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B19 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | ? | light | min-size §8.1: min text-run height 77px >= floor 41px | PASS | — |
| B21 | ? | — | no video | SKIP | — |
| B22 | ? | light | min-size §8.1: diegetic-palette pattern (B22_Changepoint) — geometric ink markers are nota… | PASS | — |
| B23 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B24 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | ? | light | min-size §8.1: min text-run height 58px >= floor 41px | PASS | — |
| B26 | ? | light | min-size §8.1: diegetic-palette pattern (B26_Update) — geometric ink markers are notation,… | PASS | — |
| B27 | ? | light | min-size §8.1: min text-run height 69px >= floor 41px | PASS | — |
| B28 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B29 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B31 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B32 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B35 | ? | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B36 | ? | light | min-size §8.1: diegetic-palette pattern (B36_Falsify) — geometric ink markers are notation… | PASS | — |
| B37 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 12 | 0 |
| min-size §8.1 | 37 | 0 |
| overflow §8.2 | 37 | 0 |
| contrast §8.3 | 37 | 0 |
| contrast-local §8.3b | 37 | 0 |
| bbox-overlap §8.6b | 37 | 0 |
| card-clip §8.13 | 37 | 0 |
| kerning §8.4 | 20 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
