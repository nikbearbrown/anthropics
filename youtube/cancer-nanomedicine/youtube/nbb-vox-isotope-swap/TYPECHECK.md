# TYPECHECK.md — GATE T

Reel: `vox-isotope-swap`  |  Checked: 2026-08-31T04:54  |  Overall: **FAIL**  |  Beats checked: 16  |  FAILs: 5

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B09] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| NBB00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BOOKEND | light | min-size §8.1: min text-run height 13px >= floor 13px | PASS | — |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B04 | ? | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 27px >= floor 13px | PASS | — |
| B06 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 68px >= floor 13px | PASS | — |
| B09 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B11 | ? | light | min-size §8.1: smallest text run 10px < floor 13px (1.9% of 720px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B12 | ? | light | min-size §8.1: smallest text run 9px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| NBB01 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| NBB02 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| NBB03 | ? | dark | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B03 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B06 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B10 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **bbox-overlap §8.6b**: text-run bbox overlap 28% >= 10% — two labels are printing on top of each other: blob@(104,161)–(599,207) ∩ blob@(332,196)–(456,235) (28% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **min-size §8.1**: smallest text run 10px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B12 (?)
- **min-size §8.1**: smallest text run 9px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 14 | 5 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 1 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 3 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
