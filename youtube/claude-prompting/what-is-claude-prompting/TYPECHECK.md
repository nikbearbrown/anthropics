# TYPECHECK.md — GATE T

Reel: `what-is-claude-prompting`  |  Checked: 2026-07-25T01:12  |  Overall: PASS  |  Beats checked: 8  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B01 | ? | min-size §8.1: min text-run height 41px >= floor 35px | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B03 | ? | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'sparkLine') | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 41px >= floor 35px | PASS | — |
| B05 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 9 words in 'artifactLines[… | PASS | — |
| B06 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B07 | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 8 | 0 |
| overflow §8.2 | 8 | 0 |
| contrast §8.3 | 8 | 0 |
| kerning §8.4 | 3 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
