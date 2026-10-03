# TYPECHECK.md — GATE T

Reel: `vox-tumor-pressure`  |  Checked: 2026-08-30T20:19  |  Overall: **FAIL**  |  Beats checked: 19  |  FAILs: 7

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| NBB00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B04 | ? | light | min-size §8.1: min text-run height 45px >= floor 20px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 31px >= floor 20px | PASS | — |
| B06 | ? | light | min-size §8.1: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B08 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B09 | ? | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B10 | ? | light | min-size §8.1: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B11 | ? | light | min-size §8.1: smallest text run 11px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| NBB01 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| NBB02 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| NBB03 | ? | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B03 (?)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **bbox-overlap §8.6b**: text-run bbox overlap 58% >= 10% — two labels are printing on top of each other: blob@(831,481)–(843,489) ∩ blob@(835,482)–(849,490) (58% of smaller); separate label positions in scenes.py or Remotion component | §8.6c ADVISORY: possible fused run(s) — blob@(483,753)–(561,802) h=49px (5.8×med)
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
- **min-size §8.1**: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **min-size §8.1**: smallest text run 11px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 18 | 7 |
| overflow §8.2 | 18 | 0 |
| contrast §8.3 | 18 | 0 |
| contrast-local §8.3b | 18 | 0 |
| bbox-overlap §8.6b | 18 | 1 |
| card-clip §8.13 | 18 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 4 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
