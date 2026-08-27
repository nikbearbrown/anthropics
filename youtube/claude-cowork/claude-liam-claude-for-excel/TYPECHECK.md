# TYPECHECK.md — GATE T

Reel: `claude-for-excel`  |  Checked: 2026-08-10T04:02  |  Overall: PASS  |  Beats checked: 12  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B02 | ? | dark | no-wordy-card §8.5: 2 element(s), 2 words — within budget. Detail: 2 chips (2 words) | PASS | — |
| B03 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | dark | no-wordy-card §8.5: 2 element(s), 2 words — within budget. Detail: 2 chips (2 words) | PASS | — |
| B06 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| BHTF | ? | light | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 7 | 0 |
| min-size §8.1 | 12 | 0 |
| overflow §8.2 | 12 | 0 |
| contrast §8.3 | 12 | 0 |
| contrast-local §8.3b | 12 | 0 |
| bbox-overlap §8.6b | 12 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
