# TYPECHECK.md — GATE T

Reel: `claude-api-one-endpoint-ladder`  |  Checked: 2026-09-05T00:21  |  Overall: PASS  |  Beats checked: 16  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [A11] narration recites the card (0.90) — discuss it, don't read it
> - §8.10 [A21] narration recites the card (0.84) — discuss it, don't read it
> - §8.10 [A31] narration recites the card (0.92) — discuss it, don't read it
> - §8.10 [EX] narration recites the card (0.82) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A10 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A11 | REMOTION | light | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 8 words in 'artifactLines[… | PASS | — |
| A20 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A21 | REMOTION | light | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 8 words in 'artifactLines[… | PASS | — |
| A30 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A31 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A40 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A41 | REMOTION | light | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 9 words in 'artifactLines[… | PASS | — |
| A50 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A51 | REMOTION | light | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 10 words in 'sparkLine') | PASS | — |
| EX | REMOTION | light | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 10 words in 'sparkLine') | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 12 | 0 |
| min-size §8.1 | 16 | 0 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 0 |
| card-clip §8.13 | 16 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 8 | 4 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
