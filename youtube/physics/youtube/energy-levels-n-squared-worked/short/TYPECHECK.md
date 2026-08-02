# TYPECHECK.md — GATE T

Reel: `energy-levels-n-squared-worked-short`  |  Checked: 2026-08-01T15:46  |  Overall: PASS  |  Beats checked: 35  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.6 GOLDEN STRINGS:**

> - BOUT: headline 74 chars — adversarial overflow risk (golden LONGEST test fails at this length)

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | no video | SKIP | — |
| H01 | ? | no video | SKIP | — |
| H02 | ? | no video | SKIP | — |
| A01 | ? | no video | SKIP | — |
| A02 | ? | no video | SKIP | — |
| A03 | ? | no video | SKIP | — |
| A04 | ? | no video | SKIP | — |
| M01 | ? | no video | SKIP | — |
| M02 | ? | no video | SKIP | — |
| M03 | ? | no video | SKIP | — |
| M04 | ? | no video | SKIP | — |
| M05 | ? | no video | SKIP | — |
| M06 | ? | no video | SKIP | — |
| M07 | ? | no video | SKIP | — |
| M08 | ? | no video | SKIP | — |
| M09 | ? | no video | SKIP | — |
| W01 | ? | no video | SKIP | — |
| W02 | ? | no video | SKIP | — |
| W03 | ? | no video | SKIP | — |
| W04 | ? | no video | SKIP | — |
| W05 | ? | no video | SKIP | — |
| W06 | ? | no video | SKIP | — |
| W07 | ? | no video | SKIP | — |
| W08 | ? | no video | SKIP | — |
| P01 | ? | no video | SKIP | — |
| P02 | ? | no video | SKIP | — |
| P03 | ? | no video | SKIP | — |
| P04 | ? | no video | SKIP | — |
| R01 | ? | no video | SKIP | — |
| R02 | ? | no video | SKIP | — |
| R03 | ? | no video | SKIP | — |
| BVDT | ? | no video | SKIP | — |
| BHTF | ? | no video | SKIP | — |
| BOUT | ? | no video | SKIP | — |
| END | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
