# TYPECHECK.md — GATE T

Reel: `claude-basics--computer-use-best-practices`  |  Checked: 2026-08-29T18:57  |  Overall: **FAIL**  |  Beats checked: 10  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BASK | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B00 | ? | light | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |
| B01 | ? | light | min-size §8.1: hand-drawn pattern (B01Scene) — §8.1 hachure/crossbar fragments are false p… | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 24px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 20px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B04 | ? | light | min-size §8.1: hand-drawn pattern (B04Scene) — §8.1 hachure/crossbar fragments are false p… | PASS | — |
| BCRY | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BMASCOT | ? | light | min-size §8.1: no text blobs detected — GATE T could not verify this frame; absence of mea… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| BOUT | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

### BMASCOT (?)
- **min-size §8.1**: no text blobs detected — GATE T could not verify this frame; absence of measurement is not compliance (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 10 | 1 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 0 |
| card-clip §8.13 | 10 | 0 |
| kerning §8.4 | 4 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
