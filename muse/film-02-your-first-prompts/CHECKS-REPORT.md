# CHECKS-REPORT.md — Your First Prompts (Film 2)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=15, body=10, total=280s
(inside the 280–330s brief envelope).

Static checker per class (`static_scene_check.py scenes.py --class <C>`):

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01 | 1 clean · 0 warn · 0 error |
| M04_B02 | 1 clean · 0 warn · 0 error |
| M05_B03 | 1 clean · 0 warn · 0 error |
| M06_B04 | 1 clean · 0 warn · 0 error |
| M07_B05 | 1 clean · 0 warn · 0 error |
| M08_B06 | 1 clean · 0 warn · 0 error |
| M09_B07 | 1 clean · 0 warn · 0 error |
| M10_B08 | 1 clean · 0 warn · 0 error |
| M11_B09 | 1 clean · 0 warn · 0 error |
| M12_B10 | 1 clean · 0 warn · 0 error |
| M13_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 13 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
1. **M13 double-fade (code review, before checker run):** the phase-2→3
   transition called `FadeOut(card)` and also faded every mobject, which
   included `card`. Fixed: phase-2 mobjects collected into `turn_g`,
   single `FadeOut(turn_g)`. Not a checker failure — caught by reading the
   code, recorded here.

No checker warnings or errors on any class on the first run: the binding
rule (every text reveal paired with a non-text shape change) was applied
from the first draft, the custom two-`Line` `check_mark()` used throughout,
all coordinates inside the safe area.

## Beat/sheet cross-checks (scripted)
- Every quoted on-screen string in `screen` is spoken in the same beat's
  `line` (verified by script; allowed: digits↔spoken words, "JLPT N5",
  "@NikBearBrown" — same convention as Film 1).
- Numbers spoken as words in `line` ("thirty dollars", "forty grammar
  points", "five dollars"), digits on screen.
- Attributed judgments voiced exactly as FACTCHECK.md requires ("His
  experience", "his test", "his habit").
- BVDT is exactly 4 lines (one per act). BOUT carries the "Muse Can See"
  teaser.
