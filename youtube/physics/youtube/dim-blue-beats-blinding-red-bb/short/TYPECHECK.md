# TYPECHECK.md — GATE T

Reel: `dim-blue-beats-blinding-red-bb-short`  |  Checked: 2026-08-01T13:31  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 64px >= floor 31px | PASS | — |
| H01 | ? | min-size §8.1: dark-background frame (mean lum 26.9) — INK check N/A (Manim palette) | PASS | — |
| H02 | ? | min-size §8.1: dark-background frame (mean lum 27.3) — INK check N/A (Manim palette) | PASS | — |
| H03 | ? | min-size §8.1: dark-background frame (mean lum 27.4) — INK check N/A (Manim palette) | PASS | — |
| H04 | ? | min-size §8.1: dark-background frame (mean lum 26.2) — INK check N/A (Manim palette) | PASS | — |
| W01 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| W02 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| K01 | ? | min-size §8.1: dark-background frame (mean lum 29.3) — INK check N/A (Manim palette) | PASS | — |
| K02 | ? | min-size §8.1: dark-background frame (mean lum 26.3) — INK check N/A (Manim palette) | PASS | — |
| K03 | ? | min-size §8.1: dark-background frame (mean lum 30.5) — INK check N/A (Manim palette) | PASS | — |
| C01 | ? | min-size §8.1: dark-background frame (mean lum 28.0) — INK check N/A (Manim palette) | PASS | — |
| C02 | ? | min-size §8.1: dark-background frame (mean lum 27.9) — INK check N/A (Manim palette) | PASS | — |
| X01 | ? | min-size §8.1: dark-background frame (mean lum 27.9) — INK check N/A (Manim palette) | PASS | — |
| X02 | ? | min-size §8.1: dark-background frame (mean lum 27.9) — INK check N/A (Manim palette) | PASS | — |
| X03 | ? | min-size §8.1: dark-background frame (mean lum 27.4) — INK check N/A (Manim palette) | PASS | — |
| X04 | ? | min-size §8.1: dark-background frame (mean lum 33.8) — INK check N/A (Manim palette) | PASS | — |
| A03 | ? | min-size §8.1: dark-background frame (mean lum 26.0) — INK check N/A (Manim palette) | PASS | — |
| P01 | ? | min-size §8.1: dark-background frame (mean lum 28.3) — INK check N/A (Manim palette) | PASS | — |
| P02 | ? | min-size §8.1: dark-background frame (mean lum 26.0) — INK check N/A (Manim palette) | PASS | — |
| N02 | ? | min-size §8.1: dark-background frame (mean lum 30.2) — INK check N/A (Manim palette) | PASS | — |
| B01 | ? | min-size §8.1: dark-background frame (mean lum 28.0) — INK check N/A (Manim palette) | PASS | — |
| B02 | ? | min-size §8.1: dark-background frame (mean lum 28.1) — INK check N/A (Manim palette) | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 35px >= floor 31px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 64px >= floor 31px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 93px >= floor 31px | PASS | — |
| END | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 25 | 0 |
| overflow §8.2 | 25 | 0 |
| contrast §8.3 | 25 | 0 |
| contrast-local §8.3b | 25 | 0 |
| bbox-overlap §8.6b | 25 | 0 |
| kerning §8.4 | 21 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
