# TYPECHECK.md — GATE T

Reel: `cc-hook-enforcement`  |  Checked: 2026-09-10T01:13  |  Overall: PASS  |  Beats checked: 14  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| BIDEA | IDEA | dark | min-size §8.1: min text-run height 69px >= floor 41px | PASS | — |
| BDEFS | CARD | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B02 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B03 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B04 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B05 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B06 | TERMINAL | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| BCONDUCT | TERMINAL | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHUMAN | TERMINAL | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
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
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 14 | 0 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 0 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
