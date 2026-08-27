# TYPECHECK.md — GATE T

Reel: `claude-liam-four-places-your-data-goes`  |  Checked: 2026-08-13T23:10  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B01 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | BOOKEND | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B09 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | MANIM | light | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B18 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 20 | 0 |
| min-size §8.1 | 26 | 0 |
| overflow §8.2 | 26 | 0 |
| contrast §8.3 | 26 | 0 |
| contrast-local §8.3b | 26 | 0 |
| bbox-overlap §8.6b | 26 | 0 |
| kerning §8.4 | 1 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
