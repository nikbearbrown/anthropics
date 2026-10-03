# TYPECHECK.md — GATE T

Reel: `vox-tumor-pressure`  |  Checked: 2026-08-30T20:21  |  Overall: **FAIL**  |  Beats checked: 13  |  FAILs: 9

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B04 | ? | light | min-size §8.1: min text-run height 44px >= floor 20px | PASS | — |
| B05 | ? | light | min-size §8.1: smallest text run 12px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B06 | ? | light | min-size §8.1: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B08 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B09 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B10 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B11 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B12 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

### B01 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B03 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **bbox-overlap §8.6b**: text-run bbox overlap 50% >= 10% — two labels are printing on top of each other: blob@(891,789)–(917,802) ∩ blob@(910,794)–(924,802) (50% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(385,293)–(427,321) h=28px (2.8×med), blob@(889,764)–(928,790) h=26px (2.6×med), blob@(1071,764)–(1110,789) h=25px (2.5×med)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B05 (?)
- **min-size §8.1**: smallest text run 12px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B06 (?)
- **min-size §8.1**: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B07 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B08 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B09 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B10 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 10 | 9 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 1 |
| card-clip §8.13 | 10 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
