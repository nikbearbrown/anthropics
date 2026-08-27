# TYPECHECK.md — GATE T

Reel: `mas-coordination`  |  Checked: 2026-08-16T12:27  |  Overall: PASS  |  Beats checked: 34  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B04] narration recites the card (0.86) — discuss it, don't read it
> - §8.10 [B25] narration recites the card (0.93) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B03 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | light | min-size §8.1: hand-drawn pattern (fig1_vuln_swarm) — §8.1 hachure/crossbar fragments are … | PASS | — |
| B08 | ? | light | min-size §8.1: hand-drawn pattern (fig1_vuln_swarm) — §8.1 hachure/crossbar fragments are … | PASS | — |
| B09 | ? | light | min-size §8.1: hand-drawn pattern (fig1_vuln_swarm) — §8.1 hachure/crossbar fragments are … | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B11 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B13 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B14 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B15 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | — | no video | SKIP | — |
| B18 | ? | light | min-size §8.1: hand-drawn pattern (fig2_merge_and_sharing) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B19 | ? | light | min-size §8.1: hand-drawn pattern (fig2_merge_and_sharing) — §8.1 hachure/crossbar fragmen… | PASS | — |
| B20 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B21 | ? | — | no video | SKIP | — |
| B22 | ? | light | min-size §8.1: hand-drawn pattern (fig3_pr_activity) — §8.1 hachure/crossbar fragments are… | PASS | — |
| B23 | ? | light | min-size §8.1: hand-drawn pattern (fig3_pr_activity) — §8.1 hachure/crossbar fragments are… | PASS | — |
| B24 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B25 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B26 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B27 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B28 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B29 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B31 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B32 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B33 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B34 | ? | dark | min-size §8.1: min text-run height 65px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 29 | 0 |
| overflow §8.2 | 29 | 0 |
| contrast §8.3 | 29 | 0 |
| contrast-local §8.3b | 29 | 0 |
| bbox-overlap §8.6b | 29 | 0 |
| kerning §8.4 | 7 | 0 |
| redundancy §8.10 (advisory) | 17 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
