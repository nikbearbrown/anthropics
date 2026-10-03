# CHECKS-REPORT.md — What Muse Is (Film 1)

## Gate results (verified by the builder, 2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=16, body=11, total=286s.

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
| M13_B11 | 1 clean · 0 warn · 0 error |
| M14_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 14 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
None. The binding rule (every text reveal paired with a non-text shape
change) was applied from the first draft, the custom two-`Line`
`check_mark()` was used throughout, and all coordinates stayed inside the
safe area — so the gate passed on the first run of every class. Recorded
here rather than hidden, per the log rules: there was nothing to fix.

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md).
- Numbers spoken as words in `line` ("thirty billion", "one dollar
  twenty-five"), digits on screen.
- Attributed judgments voiced exactly as FACTCHECK.md requires
  ("the instructor's reading", "in Nik's experience", "at launch").
- BVDT is exactly 4 lines (one per act). BOUT carries the next-film teaser.
