# TYPECHECK.md — GATE T

Reel: `show-tell-context-is-a-budget`  |  Checked: 2026-09-26T15:39  |  Overall: **FAIL**  |  Beats checked: 13  |  FAILs: 6

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 61px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | min-size §8.1: smallest text run 40px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B01 | manim | light | min-size §8.1: min text-run height 1328px >= floor 41px | PASS | — |
| B02 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B03 | manim | light | min-size §8.1: min text-run height 1328px >= floor 41px | PASS | — |
| B04 | manim | light | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B05 | manim | light | min-size §8.1: min text-run height 67px >= floor 41px | PASS | — |
| B06 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B07 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B08 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

### B00 (manim)
- **min-size §8.1**: smallest text run 40px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B02 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(2450,1301)–(3405,1925) ∩ blob@(3067,1430)–(3142,1476) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(2450,1301)–(3405,1925) h=624px (1.9×med)
- **Fix:** Separate label positions — two text elements overlap

### B04 (manim)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### B06 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(2266,1097)–(3232,1682) ∩ blob@(2312,1114)–(3186,1630) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(612,794)–(2221,1844) h=1050px (15.7×med), blob@(2266,1097)–(3232,1682) h=585px (8.7×med), blob@(2312,1114)–(3186,1630) h=516px (7.7×med)
- **Fix:** Separate label positions — two text elements overlap

### B07 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(612,795)–(2221,1844) ∩ blob@(1248,1265)–(1577,1471) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(612,795)–(2221,1844) h=1049px (3.4×med)
- **Fix:** Separate label positions — two text elements overlap

### B08 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(1106,909)–(2621,1898) ∩ blob@(1888,1048)–(2199,1242) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(1106,909)–(2621,1898) h=989px (5.1×med), blob@(315,1144)–(914,1506) h=362px (1.9×med)
- **Fix:** Separate label positions — two text elements overlap

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 13 | 1 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 1 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 4 |
| card-clip §8.13 | 13 | 0 |
| kerning §8.4 | 9 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
