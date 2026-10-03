# TYPECHECK.md — GATE T

Reel: `pattern-analysis-subagent`  |  Checked: 2026-08-31T09:31  |  Overall: PASS  |  Beats checked: 17  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| NBB00 | ? | — | no video | SKIP | — |
| B00 | BOOKEND | — | no video | SKIP | — |
| B01 | BOOKEND | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | — | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B03 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | — | no video | SKIP | — |
| B05 | ? | — | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | — | no video | SKIP | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| NBB01 | ? | — | no video | SKIP | — |
| NBB02 | ? | — | no video | SKIP | — |
| NBB03 | ? | — | no video | SKIP | — |
| BVDT | BOOKEND | — | no video | SKIP | — |
| BHTF | BOOKEND | — | no video | SKIP | — |
| BOUT | BOOKEND | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| card-clip §8.13 | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
