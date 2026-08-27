# TYPECHECK.md — GATE T

Reel: `mas-turf-war-short`  |  Checked: 2026-08-16T13:09  |  Overall: PASS  |  Beats checked: 19  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B08] narration recites the card (0.87) — discuss it, don't read it
> - §8.10 [B20] narration recites the card (0.93) — discuss it, don't read it
> - §8.10 [B23] narration recites the card (0.89) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | — | no video | SKIP | — |
| B02 | ? | — | no video | SKIP | — |
| B04 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | — | no video | SKIP | — |
| B10 | ? | — | no video | SKIP | — |
| B11 | ? | — | no video | SKIP | — |
| B12 | ? | — | no video | SKIP | — |
| B15 | ? | — | no video | SKIP | — |
| B16 | ? | — | no video | SKIP | — |
| B18 | ? | — | no video | SKIP | — |
| B19 | ? | — | no video | SKIP | — |
| B20 | ? | — | no video | SKIP | — |
| B23 | ? | — | no video | SKIP | — |
| B26 | ? | — | no video | SKIP | — |
| END | ? | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 6 | 3 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
