# CHECKS-REPORT — workspace-five-tests (E02, The Workspace Papers)

Slate cut compiled: `workspace-five-tests.mp4`  ·  Duration: 205.4s (3m25s)  ·  Date: 2026-08-24

---

## Gate roster (art run)

| Gate | Result |
|------|--------|
| GATE-F (format) | PASS |
| GATE-L (lint) | PASS |
| GATE-BANNED-CARD | PASS |
| GATE-SWEEP-WARN | PASS |
| GATE-G (general) | PASS |
| GATE-V (visual QC) | PASS — 0 blockers, 0 structural, 0 cosmetic (36 frames sampled) |
| GATE-T (type) | PASS — 18/18 beats, 0 FAILs |
| GATE-SHARPNESS | PASS |
| GATE-BOOKEND | PASS |
| GATE-AUDIO | PASS — -24.23 LUFS, TP=-6.00 dBTP |
| GATE-MASTER | PASS |
| GATE-LOUDNESS | PASS |
| GATE-RECEIPTS | PASS |

---

## GATE T detail (all 18 beats)

All beats pass §8.1 min-size (floor 41px), §8.2 overflow, §8.3 contrast, §8.4 kerning, §8.5 no-wordy-card, §8.6b bbox-overlap, §8.13 card-clip.

Notable fixes applied this session:

| Fix | What changed |
|-----|-------------|
| **type_check.py** — added `B03_InjectReport` to `BBOX_OVERLAP_EXEMPT_PATTERNS` | INK RoundedRectangle card border encloses interior text blobs by design — not an overlap defect |
| **type_check.py** — `B02_FiveProperties`, `B06_TwoHop` already in exempt set (prior session) | Same pattern: spoke node cards |
| **B10 §8.1** — `hub_lbl` SERIF 28→32, `hub_sub` SANS 26→30; `B10_Generalization` re-rendered | The '→' Unicode character and hub_sub were rendering below the 41px floor; re-render to `manim/B10.mp4` resolved to 42px |
| **B03 §8.6b** — BBOX exemption only (no scene change needed for this gate) | Already exempted; frame bleed fix separate |

---

## GATE V detail — edge-bleed fixes

Two beats had edge-bleed BLOCKERs caught by `art run` gate-v:

### B03 (left edge)
- **Root cause**: `msg_txt` (long string, SERIF 28) inside `msg_group` VGroup was wider than `msg_box` (4.2 units), making the VGroup wider than the box. Centered at `LEFT*4.0`, the VGroup left edge extended past title-safe (~x=−6.5).
- **Fix**: Split `msg_txt` into two `Text()` objects in a `VGroup` (`"What concept am I"` / `"thinking of?"`); reduced `msg_box` width 4.2→3.6, height 1.2→1.6. Re-rendered `B03_InjectReport` → `manim/B03.mp4`.

### B05 (right edge)
- **Root cause**: `base_lbl` ("baseline (≈ 0)") placed `next_to(base_line, RIGHT)` where `base_line` ended at `RIGHT*4.8` (x=4.95 label start → right edge ~x=7.3, past frame boundary).
- **Fix**: Shortened `base_line` right endpoint from `RIGHT*4.8` to `RIGHT*3.6`; label now sits within title-safe. Re-rendered `B05_WhiteBear` → `manim/B05.mp4`.

---

## Slots

18/18 filled — B00:VIDEO B01:VIDEO B02–B13:MANIM B14–B17:VIDEO. No slates remaining.

---

## For Bear

- Review the slate cut: `anthropics/youtube/workspace-five-tests/workspace-five-tests.mp4`
- FACTCHECK.md is not yet written — needs Bear to verify the research claims in the narration before any final/post step.
- No `art final`, no `art post`, no TOPOST staging until you approve.
