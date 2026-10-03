# TYPECHECK.md — GATE T

Reel: `ai-creative-work-belongs-to-nobody`  |  Checked: 2026-09-01T01:18  |  Overall: **FAIL**  |  Beats checked: 14  |  FAILs: 6

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| NBB00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 294px >= floor 13px | PASS | — |
| B03 | ? | light | min-size §8.1: smallest text run 10px < floor 13px (1.9% of 720px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B04 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B05 | ? | light | min-size §8.1: smallest text run 10px < floor 13px (1.9% of 720px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B06 | ? | light | min-size §8.1: min text-run height 107px >= floor 13px | PASS | — |
| B07 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B08 | ? | light | min-size §8.1: smallest text run 9px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B09 | ? | light | min-size §8.1: min text-run height 93px >= floor 13px | PASS | — |
| B10 | ? | light | min-size §8.1: smallest text run 9px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| NBB01 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| NBB02 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| NBB03 | ? | light | min-size §8.1: min text-run height 96px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B03 (?)
- **min-size §8.1**: smallest text run 10px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B04 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B05 (?)
- **min-size §8.1**: smallest text run 10px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(189,205)–(1090,298) ∩ blob@(644,256)–(662,266) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Increase font_size in scenes.py or Remotion component

### B07 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B08 (?)
- **min-size §8.1**: smallest text run 9px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B10 (?)
- **min-size §8.1**: smallest text run 9px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 14 | 6 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 1 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
