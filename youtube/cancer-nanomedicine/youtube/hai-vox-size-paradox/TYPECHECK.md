# TYPECHECK.md — GATE T

Reel: `vox-size-paradox`  |  Checked: 2026-08-31T03:31  |  Overall: **FAIL**  |  Beats checked: 15  |  FAILs: 8

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (0.83) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | light | min-size §8.1: min text-run height 31px >= floor 20px | PASS | — |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 23px >= floor 20px | PASS | — |
| B04 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B05 | ? | light | min-size §8.1: min text-run height 56px >= floor 20px | PASS | — |
| B06 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B09 | ? | light | min-size §8.1: smallest text run 11px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B10 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B11 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B12 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B13 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B14 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

### B04 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B06 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B08 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B09 (?)
- **min-size §8.1**: smallest text run 11px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B10 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B12 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B13 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 13 | 8 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 0 |
| card-clip §8.13 | 13 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 2 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
