# TYPECHECK.md — GATE T

Reel: `two-spots-not-a-smear-bb`  |  Checked: 2026-08-01T20:13  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| H01 | ? | min-size §8.1: dark-background frame (mean lum 30.0) — INK check N/A (Manim palette) | PASS | — |
| H02 | ? | min-size §8.1: dark-background frame (mean lum 30.3) — INK check N/A (Manim palette) | PASS | — |
| H03 | ? | min-size §8.1: dark-background frame (mean lum 30.7) — INK check N/A (Manim palette) | PASS | — |
| H04 | ? | min-size §8.1: dark-background frame (mean lum 29.9) — INK check N/A (Manim palette) | PASS | — |
| H05 | ? | min-size §8.1: dark-background frame (mean lum 28.3) — INK check N/A (Manim palette) | PASS | — |
| W01 | ? | min-size §8.1: dark-background frame (mean lum 26.4) — INK check N/A (Manim palette) | PASS | — |
| W02 | ? | min-size §8.1: dark-background frame (mean lum 26.9) — INK check N/A (Manim palette) | PASS | — |
| W03 | ? | min-size §8.1: dark-background frame (mean lum 26.6) — INK check N/A (Manim palette) | PASS | — |
| W04 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| W05 | ? | min-size §8.1: dark-background frame (mean lum 27.4) — INK check N/A (Manim palette) | PASS | — |
| S01 | ? | min-size §8.1: dark-background frame (mean lum 28.3) — INK check N/A (Manim palette) | PASS | — |
| S02 | ? | min-size §8.1: dark-background frame (mean lum 28.2) — INK check N/A (Manim palette) | PASS | — |
| S03 | ? | min-size §8.1: dark-background frame (mean lum 28.2) — INK check N/A (Manim palette) | PASS | — |
| S04 | ? | min-size §8.1: dark-background frame (mean lum 28.1) — INK check N/A (Manim palette) | PASS | — |
| S05 | ? | min-size §8.1: dark-background frame (mean lum 28.3) — INK check N/A (Manim palette) | PASS | — |
| S06 | ? | min-size §8.1: dark-background frame (mean lum 28.2) — INK check N/A (Manim palette) | PASS | — |
| S07 | ? | min-size §8.1: dark-background frame (mean lum 27.8) — INK check N/A (Manim palette) | PASS | — |
| S08 | ? | min-size §8.1: dark-background frame (mean lum 27.9) — INK check N/A (Manim palette) | PASS | — |
| S09 | ? | min-size §8.1: dark-background frame (mean lum 27.8) — INK check N/A (Manim palette) | PASS | — |
| P01 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| P02 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| P03 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 45px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 26 | 0 |
| overflow §8.2 | 26 | 0 |
| contrast §8.3 | 26 | 0 |
| contrast-local §8.3b | 26 | 0 |
| bbox-overlap §8.6b | 26 | 0 |
| kerning §8.4 | 22 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
