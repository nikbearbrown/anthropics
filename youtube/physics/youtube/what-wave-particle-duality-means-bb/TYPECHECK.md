# TYPECHECK.md — GATE T

Reel: `what-wave-particle-duality-means-bb`  |  Checked: 2026-08-01T15:06  |  Overall: PASS  |  Beats checked: 24  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| H01 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| H02 | ? | min-size §8.1: dark-background frame (mean lum 26.9) — INK check N/A (Manim palette) | PASS | — |
| H03 | ? | min-size §8.1: dark-background frame (mean lum 27.2) — INK check N/A (Manim palette) | PASS | — |
| H04 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| M01 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| M02 | ? | min-size §8.1: dark-background frame (mean lum 30.0) — INK check N/A (Manim palette) | PASS | — |
| M03 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| S01 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| S02 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| S03 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| A01 | ? | min-size §8.1: dark-background frame (mean lum 29.4) — INK check N/A (Manim palette) | PASS | — |
| A02 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| A03 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| A04 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| Y01 | ? | min-size §8.1: dark-background frame (mean lum 26.1) — INK check N/A (Manim palette) | PASS | — |
| Y02 | ? | min-size §8.1: dark-background frame (mean lum 29.2) — INK check N/A (Manim palette) | PASS | — |
| N01 | ? | min-size §8.1: dark-background frame (mean lum 26.4) — INK check N/A (Manim palette) | PASS | — |
| N02 | ? | min-size §8.1: dark-background frame (mean lum 26.6) — INK check N/A (Manim palette) | PASS | — |
| B01 | ? | min-size §8.1: dark-background frame (mean lum 26.9) — INK check N/A (Manim palette) | PASS | — |
| B02 | ? | min-size §8.1: dark-background frame (mean lum 27.3) — INK check N/A (Manim palette) | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 68px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 96px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 24 | 0 |
| overflow §8.2 | 24 | 0 |
| contrast §8.3 | 24 | 0 |
| contrast-local §8.3b | 24 | 0 |
| bbox-overlap §8.6b | 24 | 0 |
| kerning §8.4 | 20 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
