# TYPECHECK.md — GATE T

Reel: `vox-tumor-pressure`  |  Checked: 2026-08-28T07:34  |  Overall: **FAIL**  |  Beats checked: 17  |  FAILs: 6

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | kerning §8.4: max inter-glyph gap 30px > threshold 7px (14.6× expected 2px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B03 | ? | — | no video | SKIP | — |
| B04 | ? | light | min-size §8.1: min text-run height 21px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 31px >= floor 20px | PASS | — |
| B06 | ? | light | min-size §8.1: smallest text run 16px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | light | min-size §8.1: smallest text run 14px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B08 | ? | light | kerning §8.4: max inter-glyph gap 23px > threshold 8px (9.8× expected 2px) — check kern ta… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B09 | ? | light | kerning §8.4: max inter-glyph gap 17px > threshold 6px (10.0× expected 2px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B10 | ? | light | kerning §8.4: max inter-glyph gap 49px > threshold 9px (20.1× expected 2px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B11 | ? | — | no video | SKIP | — |
| B12 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B02 (?)
- **kerning §8.4**: max inter-glyph gap 30px > threshold 7px (14.6× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B06 (?)
- **min-size §8.1**: smallest text run 16px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **kerning §8.4**: max inter-glyph gap 29px > threshold 5px (20.6× expected 1px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Increase font_size in scenes.py or Remotion component

### B07 (?)
- **min-size §8.1**: smallest text run 14px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B08 (?)
- **kerning §8.4**: max inter-glyph gap 23px > threshold 8px (9.8× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B09 (?)
- **kerning §8.4**: max inter-glyph gap 17px > threshold 6px (10.0× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B10 (?)
- **kerning §8.4**: max inter-glyph gap 49px > threshold 9px (20.1× expected 2px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 15 | 2 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| card-clip §8.13 | 15 | 0 |
| kerning §8.4 | 8 | 5 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
