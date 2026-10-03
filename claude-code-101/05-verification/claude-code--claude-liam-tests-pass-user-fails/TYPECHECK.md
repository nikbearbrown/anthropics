# TYPECHECK.md — GATE T

Reel: `tests-pass-user-fails`  |  Checked: 2026-08-10T04:15  |  Overall: PASS  |  Beats checked: 13  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B02 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B03 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B04 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B05 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B06 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B07 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B08 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B09 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 13 | 0 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
