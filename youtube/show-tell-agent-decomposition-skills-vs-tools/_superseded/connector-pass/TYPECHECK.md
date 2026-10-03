# TYPECHECK.md — GATE T

Reel: `show-tell-agent-decomposition-skills-vs-tools`  |  Checked: 2026-09-30T16:23  |  Overall: **FAIL**  |  Beats checked: 14  |  FAILs: 4

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 69px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | min-size §8.1: smallest text run 35px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B01 | manim | light | min-size §8.1: min text-run height 73px >= floor 41px | PASS | — |
| B02 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 25% >= 10% — two labels are printing on top of e… | **FAIL** | Separate label positions — two text elements overlap |
| B03 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 73px >= floor 41px | PASS | — |
| B05 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 55% >= 10% — two labels are printing on top of e… | **FAIL** | Separate label positions — two text elements overlap |
| B06 | manim | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 73px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 89px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B09 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 80% >= 10% — two labels are printing on top of e… | **FAIL** | Separate label positions — two text elements overlap |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B00 (manim)
- **min-size §8.1**: smallest text run 35px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B02 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 25% >= 10% — two labels are printing on top of each other: blob@(1667,751)–(3090,1678) ∩ blob@(1413,962)–(1750,1035) (25% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(1667,751)–(3090,1678) h=927px (9.7×med)
- **Fix:** Separate label positions — two text elements overlap

### B05 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 55% >= 10% — two labels are printing on top of each other: blob@(1349,938)–(2490,1641) ∩ blob@(1220,1029)–(1509,1137) (55% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(1349,938)–(2490,1641) h=703px (6.5×med)
- **Fix:** Separate label positions — two text elements overlap

### B09 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 80% >= 10% — two labels are printing on top of each other: blob@(1372,884)–(2467,1599) ∩ blob@(1332,1028)–(1534,1077) (80% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(1372,884)–(2467,1599) h=715px (9.9×med)
- **Fix:** Separate label positions — two text elements overlap

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 14 | 1 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 3 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 10 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
