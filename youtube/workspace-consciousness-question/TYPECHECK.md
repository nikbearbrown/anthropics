# TYPECHECK.md — GATE T

Reel: `workspace-consciousness-question`  |  Checked: 2026-08-25T01:33  |  Overall: **FAIL**  |  Beats checked: 16  |  FAILs: 4

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B03 | ? | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 46px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 69px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B08 | ? | light | min-size §8.1: smallest text run 37px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B09 | ? | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'sparkLine') | PASS | — |
| B10 | ? | light | min-size §8.1: smallest text run 34px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B11 | ? | light | bbox-overlap §8.6b: text-run bbox overlap 100% >= 10% — two labels are printing on top of … | **FAIL** | Separate label positions — two text elements overlap |
| B12 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B14 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B15 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

### B02 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(783,1658)–(1436,1905) ∩ blob@(900,1747)–(983,1797) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Use INK on cream; add backing plate under accent text

### B08 (?)
- **min-size §8.1**: smallest text run 37px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B10 (?)
- **min-size §8.1**: smallest text run 34px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(2538,699)–(3353,1028) ∩ blob@(3060,802)–(3135,846) (100% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(486,699)–(1301,1028) h=329px (6.6×med), blob@(1512,699)–(2327,1028) h=329px (6.6×med), blob@(2538,699)–(3353,1028) h=329px (6.6×med)
- **Fix:** Separate label positions — two text elements overlap

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 16 | 2 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 1 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 2 |
| card-clip §8.13 | 16 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
