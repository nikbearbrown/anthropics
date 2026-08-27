# TYPECHECK.md — GATE T

Reel: `claude-liam-marketing`  |  Checked: 2026-08-26T18:22  |  Overall: PASS  |  Beats checked: 35  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B04] narration recites the card (0.80) — discuss it, don't read it
> - §8.10 [BVDT] narration recites the card (0.88) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | — | no video | SKIP | — |
| C01 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | — | no video | SKIP | — |
| B03 | MANIM | — | no video | SKIP | — |
| C02 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | — | no video | SKIP | — |
| B07 | MANIM | — | no video | SKIP | — |
| B08 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | MANIM | — | no video | SKIP | — |
| C03 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | MANIM | — | no video | SKIP | — |
| B12 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | — | no video | SKIP | — |
| C04 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | MANIM | — | no video | SKIP | — |
| B16 | MANIM | — | no video | SKIP | — |
| B17 | MANIM | — | no video | SKIP | — |
| B18 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| C05 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | REMOTION | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | MANIM | — | no video | SKIP | — |
| B22 | MANIM | — | no video | SKIP | — |
| B23 | MANIM | — | no video | SKIP | — |
| V01 | REMOTION | — | no video | SKIP | — |
| H01 | ASK | — | no video | SKIP | — |
| O01 | CARD | — | no video | SKIP | — |
| BVDT | BOOKEND | — | no video | SKIP | — |
| BHTF | BOOKEND | — | no video | SKIP | — |
| BOUT | BOOKEND | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 15 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| card-clip §8.13 | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 5 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
