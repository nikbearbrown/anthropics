# TYPECHECK.md — GATE T

Reel: `show-tell-agent-decomposition-skills-vs-tools`  |  Checked: 2026-09-30T16:19  |  Overall: **FAIL**  |  Beats checked: 14  |  FAILs: 4

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 69px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 13% >= 10% — two labels are printing on top of e… | **FAIL** | Separate label positions — two text elements overlap |
| B01 | manim | light | min-size §8.1: min text-run height 75px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: smallest text run 39px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B03 | manim | light | min-size §8.1: min text-run height 304px >= floor 41px | PASS | — |
| B04 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B05 | manim | light | min-size §8.1: min text-run height 101px >= floor 41px | PASS | — |
| B06 | manim | light | min-size §8.1: smallest text run 39px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | manim | light | min-size §8.1: min text-run height 77px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 89px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 96px >= floor 41px | PASS | — |
| BHTF | bookend | — | no video | SKIP | — |
| BOUT | bookend | — | no video | SKIP | — |

---

## Failures requiring action before cut

### B00 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 13% >= 10% — two labels are printing on top of each other: blob@(1517,683)–(2291,1106) ∩ blob@(1022,1051)–(2817,1854) (13% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Separate label positions — two text elements overlap

### B02 (manim)
- **min-size §8.1**: smallest text run 39px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **bbox-overlap §8.6b**: text-run bbox overlap 25% >= 10% — two labels are printing on top of each other: blob@(1667,751)–(3090,1678) ∩ blob@(1413,979)–(1750,1018) (25% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(1667,751)–(3090,1678) h=927px (9.7×med)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B04 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(478,899)–(1525,1584) ∩ blob@(971,1102)–(1270,1284) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(478,899)–(1525,1584) h=685px (3.8×med), blob@(2314,899)–(3361,1584) h=685px (3.8×med)
- **Fix:** Separate label positions — two text elements overlap

### B06 (manim)
- **min-size §8.1**: smallest text run 39px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 12 | 2 |
| overflow §8.2 | 12 | 0 |
| contrast §8.3 | 12 | 0 |
| contrast-local §8.3b | 12 | 0 |
| bbox-overlap §8.6b | 12 | 3 |
| card-clip §8.13 | 12 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
