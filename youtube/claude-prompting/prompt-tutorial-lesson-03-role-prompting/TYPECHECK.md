# TYPECHECK.md — GATE T

Reel: `prompt-tutorial-lesson-03-role-prompting`  |  Checked: 2026-07-25T19:54  |  Overall: **FAIL**  |  Beats checked: 7  |  FAILs: 3

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: smallest text run 24px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B01 | ? | min-size §8.1: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B02 | ? | min-size §8.1: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B03 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B05 | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B06 | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### B00 (?)
- **min-size §8.1**: smallest text run 24px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **overflow §8.2**: 1 text run(s) outside title-safe box (192,108)→(3648,2052) at 3840×2160
- **Fix:** Increase font_size in scenes.py or Remotion component

### B01 (?)
- **min-size §8.1**: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B02 (?)
- **min-size §8.1**: smallest text run 27px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 7 | 3 |
| overflow §8.2 | 7 | 1 |
| contrast §8.3 | 7 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
