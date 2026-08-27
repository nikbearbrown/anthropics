# TYPECHECK.md — GATE T

Reel: `claude-liam-building-plugins`  |  Checked: 2026-08-27T05:48  |  Overall: **FAIL**  |  Beats checked: 37  |  FAILs: 8

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B06] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B17] narration recites the card (0.88) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| C01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | kerning §8.4: max inter-glyph gap 321px > threshold 44px (25.4× expected 13px) — check ker… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B03 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B04 | MANIM | light | kerning §8.4: max inter-glyph gap 35px > threshold 17px (7.0× expected 5px) — check kern t… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B05 | MANIM | light | min-size §8.1: min text-run height 20px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| C02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | REMOTION | light | card-clip §8.13: §8.13 text blob touches card left boundary (col 275 vs card_left 272, tol… | **FAIL** | — |
| B08 | MANIM | light | min-size §8.1: min text-run height 26px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B09 | REMOTION | light | card-clip §8.13: §8.13 text blob touches card left boundary (col 272 vs card_left 272, tol… | **FAIL** | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | MANIM | light | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| C03 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B14 | MANIM | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B15 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 553px >= floor 20px | PASS | — |
| C04 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 45px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B19 | MANIM | light | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B20 | MANIM | light | min-size §8.1: smallest text run 19px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B21 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| C05 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | MANIM | light | min-size §8.1: min text-run height 26px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B24 | MANIM | light | min-size §8.1: min text-run height 20px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B25 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| V01 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| H01 | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| O01 | CARD | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

### B02 (MANIM)
- **kerning §8.4**: max inter-glyph gap 321px > threshold 44px (25.4× expected 13px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B04 (MANIM)
- **kerning §8.4**: max inter-glyph gap 35px > threshold 17px (7.0× expected 5px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B07 (REMOTION)
- **card-clip §8.13**: §8.13 text blob touches card left boundary (col 275 vs card_left 272, tol=4px) — text is clipped inside the card

### B09 (REMOTION)
- **card-clip §8.13**: §8.13 text blob touches card left boundary (col 272 vs card_left 272, tol=4px) — text is clipped inside the card

### B11 (MANIM)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **bbox-overlap §8.6b**: text-run bbox overlap 33% >= 10% — two labels are printing on top of each other: blob@(566,372)–(812,532) ∩ blob@(569,517)–(809,562) (33% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Use INK on cream; add backing plate under accent text

### B14 (MANIM)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(770,417)–(1149,554) ∩ blob@(965,482)–(1002,505) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Separate label positions — two text elements overlap

### B19 (MANIM)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### B20 (MANIM)
- **min-size §8.1**: smallest text run 19px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(297,478)–(596,601) ∩ blob@(446,537)–(478,556) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 16 | 0 |
| min-size §8.1 | 37 | 1 |
| overflow §8.2 | 37 | 0 |
| contrast §8.3 | 37 | 2 |
| contrast-local §8.3b | 37 | 0 |
| bbox-overlap §8.6b | 37 | 3 |
| card-clip §8.13 | 37 | 2 |
| kerning §8.4 | 14 | 2 |
| redundancy §8.10 (advisory) | 4 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
