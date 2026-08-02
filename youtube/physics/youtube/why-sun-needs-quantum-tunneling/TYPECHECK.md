# TYPECHECK.md — GATE T

Reel: `why-sun-needs-quantum-tunneling`  |  Checked: 2026-08-01T13:29  |  Overall: **FAIL**  |  Beats checked: 20  |  FAILs: 4

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A00 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A01 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A02 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A03 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A04 | ? | kerning §8.4: max inter-glyph gap 21px > threshold 4px (18.5× expected 1px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A05 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A06 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A07 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A08 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A09 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A10 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A11 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A12 | ? | kerning §8.4: max inter-glyph gap 16px > threshold 5px (10.9× expected 1px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A13 | ? | kerning §8.4: max inter-glyph gap 40px > threshold 7px (20.2× expected 2px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A14 | ? | kerning §8.4: max inter-glyph gap 34px > threshold 6px (19.3× expected 2px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| A15 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 45px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### A04 (?)
- **kerning §8.4**: max inter-glyph gap 21px > threshold 4px (18.5× expected 1px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A12 (?)
- **kerning §8.4**: max inter-glyph gap 16px > threshold 5px (10.9× expected 1px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A13 (?)
- **kerning §8.4**: max inter-glyph gap 40px > threshold 7px (20.2× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### A14 (?)
- **kerning §8.4**: max inter-glyph gap 34px > threshold 6px (19.3× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 20 | 0 |
| overflow §8.2 | 20 | 0 |
| contrast §8.3 | 20 | 0 |
| contrast-local §8.3b | 20 | 0 |
| bbox-overlap §8.6b | 20 | 0 |
| kerning §8.4 | 16 | 4 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
