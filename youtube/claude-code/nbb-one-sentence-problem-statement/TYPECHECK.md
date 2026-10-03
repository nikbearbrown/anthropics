# TYPECHECK.md — GATE T

Reel: `one-sentence-problem-statement`  |  Checked: 2026-08-31T15:02  |  Overall: PASS  |  Beats checked: 7  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.6 GOLDEN STRINGS:**

> - BOUT: headline 76 chars — adversarial overflow risk (golden LONGEST test fails at this length)

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | BODY | light | min-size §8.1: min text-run height 44px >= floor 20px | PASS | — |
| B03 | BODY | light | min-size §8.1: min text-run height 47px >= floor 20px | PASS | — |
| B04 | BODY | light | min-size §8.1: min text-run height 43px >= floor 20px | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 7 | 0 |
| overflow §8.2 | 7 | 0 |
| contrast §8.3 | 7 | 0 |
| contrast-local §8.3b | 7 | 0 |
| bbox-overlap §8.6b | 7 | 0 |
| card-clip §8.13 | 7 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
