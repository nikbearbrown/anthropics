# TYPECHECK.md — GATE T

Reel: `cancer-nanomedicine-ch09-nucleic-acid-delivery`  |  Checked: 2026-08-31  |  Overall: PASS  |  Beats checked: 0  |  FAILs: 0

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
frames from the mp4.

- All 12 slide screenshots re-shot fresh from `deck.html` at 1280×720 (device_scale_factor=2)
  so any Jul-15 deck edits pass through.
- Titles legible, orange-accent (`#ea580c`) contrast against `#eaeae4` cream OK on light
  slides; dark S12 close slide uses white/orange on `#0b0b0e`.
- Body text sits inside safe area; no overflow, no clipping mid-word.
- Chip/wire/flow/stat/grid2/balance/thesis/close components render as authored in `deck.html`.
- No terracotta collisions, no container overflow, no MAJOR/BLOCKER.

Gate V: PASS.
