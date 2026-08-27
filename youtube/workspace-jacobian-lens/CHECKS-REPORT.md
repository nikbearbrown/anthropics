# CHECKS-REPORT — workspace-jacobian-lens

Slate cut compiled: **`workspace-jacobian-lens-slate.mp4`** (172.2 s, 16/17 beats filled)
Date: 2026-08-25

---

## Gate roster

| Gate | Result | Notes |
|---|---|---|
| GATE-T (type-lock) | **PASS** | All §8.1–§8.10 checks pass |
| GATE-F (factcheck) | **PASS** | 10 rows resolved, all claim-bearing beats covered |
| GATE-L (beat-mix lint) | **PASS** (advisory) | B01 card 9.7s > 8s with no `motion_claim` — not blocking |
| GATE-BANNED-CARD | **PASS** | |
| GATE-SWEEP-WARN | **PASS** | |
| GATE-G (dagre layout) | **PASS** | No diagram beats |
| GATE-V (visual QC) | **FAIL (soft)** | 2 COSMETIC defects in B07 — see below |
| GATE-T | NOT-RUN (after compile) | Pre-run type_check.py passed manually |
| GATE-SHARPNESS | NOT-RUN | |
| GATE-BOOKEND | NOT-RUN | |
| GATE-AUDIO | NOT-RUN | |
| GATE-MASTER | NOT-RUN | Master skipped (B09 SLATE) |
| GATE-LOUDNESS | NOT-RUN | |
| GATE-RECEIPTS | NOT-RUN | |

---

## GATE-T detail — §8.1 fixes applied this session

Three scenes had SERIF/26 caption/skeptic/header text producing blobs h=39–41 (floor=42).
Fix: bumped `font_size` 26→28 in five elements across B04, B06, B12.

| Scene | Element | Old h (px) | Expected h after fix |
|---|---|---|---|
| B04_ReadoutRanking | caption | 40 | ~43 ✓ |
| B06_SixPrompts | skeptic | 41 | ~44 ✓ |
| B12_TemplateOracle | header | 40 | ~43 ✓ |
| B12_TemplateOracle | lines_grp `t` | 40–41 | ~43–44 ✓ |
| B12_TemplateOracle | skeptic | 39 | ~42 ✓ |

Also fixed this session: B12 `←` Unicode arrow (h=34 false positive from prior render)
replaced with `—` em dash (caught by "too flat" filter).

---

## GATE-V detail — 2 COSMETIC defects (soft)

Both in **B07_LensBakeoff** (hand-drawn / doodle scene):

- `B07_50.png` — `low-contrast`: ink/background luminance separation 0.22 < 0.30
- `B07_85.png` — `low-contrast`: ink/background luminance separation 0.23 < 0.30

These are soft blocks (`COSMETIC`). B07 is a hand-drawn scene registered in
`HAND_DRAWN_PATTERNS`; the low luminance separation may be inherent to its palette.
**Bear decides** whether to fix (raise contrast in the doodle scene) or pass with
`ART_STRICT=0` / `--lenient`.

---

## Open items (not blocking the slate)

- **B09 PUNT** — 1 STILL/archive placeholder remains. Pipeline can author a Manim
  or Remotion scene; no pantry image is supplied.
- **Static 47%** — 8/17 beats are static (over the ~40% pantry cap advisory).
  No block, advisory only.
- **GATE-L advisory** — B01 act-title card runs 9.7s with no `motion_claim`. 
  Either add a `motion_claim` or shorten narration to < 8s.

---

## STOPPED — per standing order

Bear reviews. No autonomous next steps.
