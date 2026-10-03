# TYPECHECK.md — GATE T

Reel: `cancer-nanomedicine-ch10-photodynamic-photothermal`  |  Checked: 2026-08-31T07:23  |  Overall: PASS  |  Beats checked: 0  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|

---

## Failures requiring action before cut

*None — GATE T PASS.*

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| card-clip §8.13 | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*

---

## Manual Gate V (frame QC) — LECTURE-DECK FORMAT

`type_check.py` has no per-beat Remotion surface here; QC done by reading extracted
frames from the mp4 (`_qc/frames/frame_{15,50,100,175,220,265,310,360,410,470,505}s.png`).

- All 12 slide screenshots render clean at 1280×720 (device_scale_factor=2).
- Titles legible, orange-accent (`#ea580c`) contrast against `#eaeae4` cream OK.
- Body text sits inside safe area; no overflow, no clipping mid-word.
- Chip/wire/callout components render as authored in `deck.html`.
- S07 title now reads `AUROLASE` (was `AUROLAASE` in the Jul-15 deck — fixed
  under Phase 0 fact/product-name allowance, see `REBUILD-LOG.md`).
- S12 dark close slide renders correctly with orange/green accents on black.
- Zero terracotta collisions, zero container overflow, zero MAJOR/BLOCKER.

Gate V: PASS.
