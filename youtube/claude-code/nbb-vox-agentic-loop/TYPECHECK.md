# TYPECHECK.md — GATE T

Reel: `vox-agentic-loop`  |  Checked: 2026-08-10T04:17  |  Overall: PASS  |  Beats checked: 20  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.6 GOLDEN STRINGS:**

> - NBB03: headline 77 chars — adversarial overflow risk (golden LONGEST test fails at this length)
> - BOUT: headline 77 chars — adversarial overflow risk (golden LONGEST test fails at this length)

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| NBB00 | ? | light | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B01 | LANE_A | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| B03 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B04 | ? | dark | min-size §8.1: hand-drawn pattern (CCSession) — §8.1 hachure/crossbar fragments are false … | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B06 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 50px >= floor 35px | PASS | — |
| B08 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 50px >= floor 35px | PASS | — |
| B10 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B11 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| NBB01 | ? | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| NBB02 | ? | light | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| NBB03 | ? | light | min-size §8.1: min text-run height 103px >= floor 35px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: min text-run height 58px >= floor 35px | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 103px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 20 | 0 |
| overflow §8.2 | 20 | 0 |
| contrast §8.3 | 20 | 0 |
| contrast-local §8.3b | 20 | 0 |
| bbox-overlap §8.6b | 20 | 0 |
| kerning §8.4 | 10 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
