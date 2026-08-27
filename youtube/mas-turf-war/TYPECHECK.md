# TYPECHECK.md — GATE T

Reel: `mas-turf-war`  |  Checked: 2026-08-26T22:02  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B03] narration recites the card (0.84) — discuss it, don't read it
> - §8.10 [B07] narration recites the card (0.88) — discuss it, don't read it
> - §8.10 [B08] narration recites the card (0.87) — discuss it, don't read it
> - §8.10 [B20] narration recites the card (0.93) — discuss it, don't read it
> - §8.10 [B21] narration recites the card (0.89) — discuss it, don't read it
> - §8.10 [B22] narration recites the card (0.89) — discuss it, don't read it
> - §8.10 [B23] narration recites the card (0.89) — discuss it, don't read it
> - §8.10 [B24] narration recites the card (0.94) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B02 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B03 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B04 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B05 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B06 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B07 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B08 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B09 | ? | — | no video | SKIP | — |
| B10 | ? | light | min-size §8.1: hand-drawn pattern (fig6_turf_war_outcomes) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B11 | ? | light | min-size §8.1: hand-drawn pattern (fig6_turf_war_outcomes) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B12 | ? | light | min-size §8.1: hand-drawn pattern (fig6_turf_war_outcomes) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B13 | ? | light | min-size §8.1: hand-drawn pattern (fig6_turf_war_outcomes) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B14 | ? | light | min-size §8.1: hand-drawn pattern (fig6_turf_war_outcomes) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B15 | ? | — | no video | SKIP | — |
| B16 | ? | light | min-size §8.1: hand-drawn pattern (fig7_time_to_resolution) — §8.1 hachure/crossbar fragme… | PASS | — |
| B17 | ? | light | min-size §8.1: hand-drawn pattern (fig7_time_to_resolution) — §8.1 hachure/crossbar fragme… | PASS | — |
| B18 | ? | light | min-size §8.1: hand-drawn pattern (fig7_time_to_resolution) — §8.1 hachure/crossbar fragme… | PASS | — |
| B19 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B20 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B21 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B22 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B23 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B24 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B26 | ? | light | min-size §8.1: min text-run height 66px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 24 | 0 |
| overflow §8.2 | 24 | 0 |
| contrast §8.3 | 24 | 0 |
| contrast-local §8.3b | 24 | 0 |
| bbox-overlap §8.6b | 24 | 0 |
| card-clip §8.13 | 24 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 12 | 8 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
