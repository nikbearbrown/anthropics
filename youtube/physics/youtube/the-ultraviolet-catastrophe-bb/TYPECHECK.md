# TYPECHECK.md — GATE T

Reel: `the-ultraviolet-catastrophe-bb`  |  Checked: 2026-08-01T13:36  |  Overall: PASS  |  Beats checked: 32  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| H01 | ? | min-size §8.1: dark-background frame (mean lum 28.2) — INK check N/A (Manim palette) | PASS | — |
| H02 | ? | min-size §8.1: dark-background frame (mean lum 28.4) — INK check N/A (Manim palette) | PASS | — |
| H03 | ? | min-size §8.1: dark-background frame (mean lum 27.4) — INK check N/A (Manim palette) | PASS | — |
| H04 | ? | min-size §8.1: dark-background frame (mean lum 26.8) — INK check N/A (Manim palette) | PASS | — |
| M01 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| M02 | ? | min-size §8.1: dark-background frame (mean lum 26.8) — INK check N/A (Manim palette) | PASS | — |
| M03 | ? | min-size §8.1: dark-background frame (mean lum 27.2) — INK check N/A (Manim palette) | PASS | — |
| M04 | ? | min-size §8.1: dark-background frame (mean lum 27.6) — INK check N/A (Manim palette) | PASS | — |
| M05 | ? | min-size §8.1: dark-background frame (mean lum 27.9) — INK check N/A (Manim palette) | PASS | — |
| P01 | ? | min-size §8.1: dark-background frame (mean lum 26.9) — INK check N/A (Manim palette) | PASS | — |
| P02 | ? | min-size §8.1: dark-background frame (mean lum 28.3) — INK check N/A (Manim palette) | PASS | — |
| P03 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| P04 | ? | min-size §8.1: dark-background frame (mean lum 27.1) — INK check N/A (Manim palette) | PASS | — |
| D01 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| D02 | ? | min-size §8.1: dark-background frame (mean lum 26.2) — INK check N/A (Manim palette) | PASS | — |
| D03 | ? | min-size §8.1: dark-background frame (mean lum 26.3) — INK check N/A (Manim palette) | PASS | — |
| F01 | ? | min-size §8.1: dark-background frame (mean lum 26.2) — INK check N/A (Manim palette) | PASS | — |
| F02 | ? | min-size §8.1: dark-background frame (mean lum 26.4) — INK check N/A (Manim palette) | PASS | — |
| F03 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| F04 | ? | min-size §8.1: dark-background frame (mean lum 26.2) — INK check N/A (Manim palette) | PASS | — |
| Y01 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| Y02 | ? | min-size §8.1: dark-background frame (mean lum 26.8) — INK check N/A (Manim palette) | PASS | — |
| Y03 | ? | min-size §8.1: dark-background frame (mean lum 26.8) — INK check N/A (Manim palette) | PASS | — |
| S01 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| S02 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| B01 | ? | min-size §8.1: dark-background frame (mean lum 26.4) — INK check N/A (Manim palette) | PASS | — |
| B02 | ? | min-size §8.1: dark-background frame (mean lum 26.4) — INK check N/A (Manim palette) | PASS | — |
| B03 | ? | min-size §8.1: dark-background frame (mean lum 26.8) — INK check N/A (Manim palette) | PASS | — |
| BVDT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 32 | 0 |
| overflow §8.2 | 32 | 0 |
| contrast §8.3 | 32 | 0 |
| contrast-local §8.3b | 32 | 0 |
| bbox-overlap §8.6b | 32 | 0 |
| kerning §8.4 | 28 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
