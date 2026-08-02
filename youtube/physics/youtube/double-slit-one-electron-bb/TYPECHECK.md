# TYPECHECK.md — GATE T

Reel: `double-slit-one-electron-bb`  |  Checked: 2026-08-01T15:11  |  Overall: PASS  |  Beats checked: 28  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| H01 | ? | min-size §8.1: dark-background frame (mean lum 29.9) — INK check N/A (Manim palette) | PASS | — |
| H02 | ? | min-size §8.1: dark-background frame (mean lum 29.9) — INK check N/A (Manim palette) | PASS | — |
| H03 | ? | min-size §8.1: dark-background frame (mean lum 30.1) — INK check N/A (Manim palette) | PASS | — |
| H04 | ? | min-size §8.1: dark-background frame (mean lum 30.0) — INK check N/A (Manim palette) | PASS | — |
| W01 | ? | min-size §8.1: dark-background frame (mean lum 30.1) — INK check N/A (Manim palette) | PASS | — |
| W02 | ? | min-size §8.1: dark-background frame (mean lum 30.8) — INK check N/A (Manim palette) | PASS | — |
| L01 | ? | min-size §8.1: dark-background frame (mean lum 29.9) — INK check N/A (Manim palette) | PASS | — |
| L02 | ? | min-size §8.1: dark-background frame (mean lum 30.1) — INK check N/A (Manim palette) | PASS | — |
| T01 | ? | min-size §8.1: dark-background frame (mean lum 30.1) — INK check N/A (Manim palette) | PASS | — |
| T02 | ? | min-size §8.1: dark-background frame (mean lum 30.0) — INK check N/A (Manim palette) | PASS | — |
| T03 | ? | min-size §8.1: dark-background frame (mean lum 30.0) — INK check N/A (Manim palette) | PASS | — |
| T04 | ? | min-size §8.1: dark-background frame (mean lum 30.6) — INK check N/A (Manim palette) | PASS | — |
| T05 | ? | min-size §8.1: dark-background frame (mean lum 30.5) — INK check N/A (Manim palette) | PASS | — |
| T06 | ? | min-size §8.1: dark-background frame (mean lum 30.0) — INK check N/A (Manim palette) | PASS | — |
| A01 | ? | min-size §8.1: dark-background frame (mean lum 31.6) — INK check N/A (Manim palette) | PASS | — |
| A02 | ? | min-size §8.1: dark-background frame (mean lum 26.6) — INK check N/A (Manim palette) | PASS | — |
| A03 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| A04 | ? | min-size §8.1: dark-background frame (mean lum 26.2) — INK check N/A (Manim palette) | PASS | — |
| Y01 | ? | min-size §8.1: dark-background frame (mean lum 31.8) — INK check N/A (Manim palette) | PASS | — |
| Y02 | ? | min-size §8.1: dark-background frame (mean lum 30.3) — INK check N/A (Manim palette) | PASS | — |
| N01 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| N02 | ? | min-size §8.1: dark-background frame (mean lum 26.7) — INK check N/A (Manim palette) | PASS | — |
| B01 | ? | min-size §8.1: dark-background frame (mean lum 26.5) — INK check N/A (Manim palette) | PASS | — |
| B02 | ? | min-size §8.1: dark-background frame (mean lum 27.0) — INK check N/A (Manim palette) | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 68px >= floor 35px | PASS | — |
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
| min-size §8.1 | 28 | 0 |
| overflow §8.2 | 28 | 0 |
| contrast §8.3 | 28 | 0 |
| contrast-local §8.3b | 28 | 0 |
| bbox-overlap §8.6b | 28 | 0 |
| kerning §8.4 | 24 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
