# TYPECHECK.md — GATE T

Reel: `energy-levels-arent-evenly-spaced`  |  Checked: 2026-08-01T02:17  |  Overall: **FAIL**  |  Beats checked: 14  |  FAILs: 8

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| H01 | ? | kerning §8.4: max inter-glyph gap 697px > threshold 109px (22.3× expected 31px) — check ke… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| H02 | ? | min-size §8.1: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| A01 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A02 | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A03 | ? | min-size §8.1: min text-run height 218px >= floor 35px | PASS | — |
| A04 | ? | overflow §8.2: 1 text run(s) outside title-safe box (96,54)→(1824,1026) at 1920×1080 | **FAIL** | Move text inside title-safe 90% box |
| A05 | ? | min-size §8.1: smallest text run 22px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| A06 | ? | min-size §8.1: smallest text run 25px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| A07 | ? | min-size §8.1: smallest text run 25px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| A08 | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| BVDT | ? | min-size §8.1: min text-run height 45px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### H01 (?)
- **kerning §8.4**: max inter-glyph gap 697px > threshold 109px (22.3× expected 31px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### H02 (?)
- **min-size §8.1**: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **kerning §8.4**: max inter-glyph gap 535px > threshold 108px (17.3× expected 31px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Increase font_size in scenes.py or Remotion component

### A02 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A04 (?)
- **overflow §8.2**: 1 text run(s) outside title-safe box (96,54)→(1824,1026) at 1920×1080
- **Fix:** Move text inside title-safe 90% box

### A05 (?)
- **min-size §8.1**: smallest text run 22px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **kerning §8.4**: max inter-glyph gap 345px > threshold 13px (96.2× expected 4px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Increase font_size in scenes.py or Remotion component

### A06 (?)
- **min-size §8.1**: smallest text run 25px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **kerning §8.4**: max inter-glyph gap 72px > threshold 9px (27.6× expected 3px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Increase font_size in scenes.py or Remotion component

### A07 (?)
- **min-size §8.1**: smallest text run 25px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Increase font_size in scenes.py or Remotion component

### A08 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **kerning §8.4**: max inter-glyph gap 52px > threshold 21px (8.6× expected 6px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Use INK on cream; add backing plate under accent text

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 14 | 4 |
| overflow §8.2 | 14 | 1 |
| contrast §8.3 | 14 | 3 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 0 |
| kerning §8.4 | 10 | 5 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
