# TYPECHECK.md — GATE T

Reel: `show-tell-how-a-skill-loads`  |  Checked: 2026-09-26T14:55  |  Overall: **FAIL**  |  Beats checked: 12  |  FAILs: 3

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 58px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | min-size §8.1: min text-run height 86px >= floor 41px | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 61px >= floor 41px | PASS | — |
| B02 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 24% >= 10% — two labels are printing on top of e… | **FAIL** | Separate label positions — two text elements overlap |
| B03 | manim | light | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B04 | manim | light | min-size §8.1: min text-run height 75px >= floor 41px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B06 | manim | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B07 | manim | light | min-size §8.1: min text-run height 105px >= floor 41px | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B02 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 24% >= 10% — two labels are printing on top of each other: blob@(758,537)–(1197,729) ∩ blob@(713,702)–(827,769) (24% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(758,537)–(1197,729) h=192px (2.6×med)
- **Fix:** Separate label positions — two text elements overlap

### B03 (manim)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(2567,848)–(2896,1049) ∩ blob@(2675,870)–(2788,944) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(296,877)–(1905,1898) h=1021px (5.1×med)
- **Fix:** Use INK on cream; add backing plate under accent text

### B06 (manim)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(534,1158)–(1698,1898) ∩ blob@(1369,1410)–(1553,1525) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Separate label positions — two text elements overlap

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 12 | 0 |
| overflow §8.2 | 12 | 0 |
| contrast §8.3 | 12 | 1 |
| contrast-local §8.3b | 12 | 0 |
| bbox-overlap §8.6b | 12 | 3 |
| card-clip §8.13 | 12 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
