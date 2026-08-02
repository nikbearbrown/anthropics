# TYPECHECK.md — GATE T

Reel: `double-slit-one-electron`  |  Checked: 2026-08-01T01:53  |  Overall: **FAIL**  |  Beats checked: 15  |  FAILs: 3

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| H01 | ? | min-size §8.1: min text-run height 111px >= floor 35px | PASS | — |
| H02 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A01 | ? | kerning §8.4: max inter-glyph gap 72px > threshold 5px (50.7× expected 1px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A02 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A03 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A04 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A05 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A06 | ? | kerning §8.4: max inter-glyph gap 113px > threshold 5px (79.0× expected 1px) — check kern … | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A07 | ? | kerning §8.4: max inter-glyph gap 494px > threshold 6px (267.3× expected 2px) — check kern… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A08 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A09 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 45px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### A01 (?)
- **kerning §8.4**: max inter-glyph gap 72px > threshold 5px (50.7× expected 1px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A06 (?)
- **kerning §8.4**: max inter-glyph gap 113px > threshold 5px (79.0× expected 1px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A07 (?)
- **kerning §8.4**: max inter-glyph gap 494px > threshold 6px (267.3× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 15 | 0 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| kerning §8.4 | 11 | 3 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
