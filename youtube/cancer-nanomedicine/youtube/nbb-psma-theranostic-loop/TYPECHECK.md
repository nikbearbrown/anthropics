# TYPECHECK.md — GATE T

Reel: `psma-theranostic-loop`  |  Checked: 2026-08-31T01:52  |  Overall: **FAIL**  |  Beats checked: 13  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.6 GOLDEN STRINGS:**

> - B09: headline 73 chars — adversarial overflow risk (golden LONGEST test fails at this length)
> - BHTF: headline 73 chars — adversarial overflow risk (golden LONGEST test fails at this length)
> - BOUT: headline 73 chars — adversarial overflow risk (golden LONGEST test fails at this length)

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | BODY | light | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B03 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | BODY | light | min-size §8.1: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B05 | BODY | light | no-wordy-card §8.5: NikBearBrownTerminalAsk: per-element check passed (max 0 words in 'n/a… | PASS | — |
| B06 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B04 (BODY)
- **min-size §8.1**: smallest text run 8px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 9 | 0 |
| min-size §8.1 | 13 | 1 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 0 |
| card-clip §8.13 | 13 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 5 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
