# CHECKS-REPORT.md — Muse the Agent (Film 12)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=17, body=12, total=386s.

Static checker per class (`static_scene_check.py scenes.py --class <C>`),
final run — all clean:

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01Loop | 1 clean · 0 warn · 0 error |
| M04_B02Errands | 1 clean · 0 warn · 0 error |
| M05_B03Tiers | 1 clean · 0 warn · 0 error |
| M06_B04Endure | 1 clean · 0 warn · 0 error |
| M07_B05Fees | 1 clean · 0 warn · 0 error |
| M08_B06Intent | 1 clean · 0 warn · 0 error |
| M09_B07Queues | 1 clean · 0 warn · 0 error |
| M10_B08Loyalty | 1 clean · 0 warn · 0 error |
| M11_B09Access | 1 clean · 0 warn · 0 error |
| M12_B10Inject | 1 clean · 0 warn · 0 error |
| M13_B11Setup | 1 clean · 0 warn · 0 error |
| M14_B12Rules | 1 clean · 0 warn · 0 error |
| M15_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 15 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
- M03_B01Loop: `construct() raised NameError: name 'Diamond' is not
  defined`. The checker's manim stub has no `Diamond` class. Fix: replaced
  the approval-gate diamond with `Square(side_length=0.95).rotate(45 *
  DEGREES)` — a true diamond shape from stub-safe primitives. Re-ran clean.
  Nothing hidden.

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md).
- Numbers spoken as words in `line` ("one hundred million", "three
  billion", "nineteen seventy-five"), digits on screen ("100M", "3B",
  "1975").
- Judgments voiced as the film's analysis (B04, B06 closing line, B07, B08,
  B10 adversarial-probability line) per FACTCHECK.md; records voiced as
  records ("Meta says", "the research notes", "his experience").
- BVDT is exactly 3 lines (one per act). BOUT closes the series
  ("Thanks for watching the series") with no next-film teaser.
- `@NikBearBrown` on the outro card follows the Film-1-consistent
  handle exception.
