# TYPECHECK.md — GATE T

Reel: `vox-delivery-diagnosis`  |  Checked: 2026-08-30T19:03  |  Overall: **FAIL**  |  Beats checked: 16  |  FAILs: 5

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.6 GOLDEN STRINGS:**

> - B01: headline 74 chars — adversarial overflow risk (golden LONGEST test fails at this length)
> - BOUT: headline 74 chars — adversarial overflow risk (golden LONGEST test fails at this length)

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B08] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B04 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B05 | ? | light | min-size §8.1: min text-run height 37px >= floor 13px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 13px >= floor 13px (individual-char fallback at 1×) | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 35px >= floor 13px | PASS | — |
| B08 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | ? | light | contrast-local §8.3b: per-blob contrast 1.23:1 < 3.0:1 — text unreadable on actual local b… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B10 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B11 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B12 | ? | light | min-size §8.1: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a captio… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| BVDT | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B04 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B09 (?)
- **contrast-local §8.3b**: per-blob contrast 1.23:1 < 3.0:1 — text unreadable on actual local background (blob@(590,419)–(618,434) fg≈(49, 35, 24) bg≈(64, 50, 40)); move label off its background or change text color
- **bbox-overlap §8.6b**: text-run bbox overlap 100% >= 10% — two labels are printing on top of each other: blob@(510,412)–(769,449) ∩ blob@(590,419)–(618,434) (100% of smaller); separate label positions in scenes.py or Remotion component
- **Fix:** Use INK on cream; add backing plate under accent text

### B10 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **overflow §8.2**: 2 text run(s) outside title-safe box (64,36)→(1216,684) at 1280×720
- **Fix:** Increase font_size in scenes.py or Remotion component

### B12 (?)
- **min-size §8.1**: smallest text run 8px < floor 13px (1.9% of 720px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 14 | 4 |
| overflow §8.2 | 14 | 1 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 1 |
| bbox-overlap §8.6b | 14 | 1 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 4 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
