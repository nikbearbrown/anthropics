# TYPECHECK.md — GATE T

Reel: `mas-epistemics-short`  |  Checked: 2026-08-26T22:51  |  Overall: PASS  |  Beats checked: 20  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (0.87) — discuss it, don't read it
> - §8.10 [B03] narration recites the card (0.88) — discuss it, don't read it
> - §8.10 [B15] narration recites the card (0.82) — discuss it, don't read it
> - §8.10 [B22] narration recites the card (0.85) — discuss it, don't read it
> - §8.10 [B26] narration recites the card (0.80) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | — | no video | SKIP | — |
| B01 | ? | — | no video | SKIP | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | — | no video | SKIP | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | — | no video | SKIP | — |
| B08 | ? | — | no video | SKIP | — |
| B10 | ? | — | no video | SKIP | — |
| B13 | ? | — | no video | SKIP | — |
| B15 | ? | — | no video | SKIP | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | — | no video | SKIP | — |
| B19 | ? | — | no video | SKIP | — |
| B20 | ? | — | no video | SKIP | — |
| B21 | ? | — | no video | SKIP | — |
| B22 | ? | — | no video | SKIP | — |
| B23 | ? | — | no video | SKIP | — |
| B26 | ? | — | no video | SKIP | — |
| B29 | ? | — | no video | SKIP | — |
| BEND | ? | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| card-clip §8.13 | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 7 | 5 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
