# CHECKS-REPORT.md — Grounded Answers (Film 5)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=13, body=8, total=282s.

Static checker per class (`static_scene_check.py scenes.py --class <C>`),
final run — all clean:

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01Question | 1 clean · 0 warn · 0 error |
| M04_B02Ungrounded | 1 clean · 0 warn · 0 error |
| M05_B03Grounded | 1 clean · 0 warn · 0 error |
| M06_B04SideBySide | 1 clean · 0 warn · 0 error |
| M07_B05Added | 1 clean · 0 warn · 0 error |
| M08_B06Blocked | 1 clean · 0 warn · 0 error |
| M09_B07Price | 1 clean · 0 warn · 0 error |
| M10_B08When | 1 clean · 0 warn · 0 error |
| M11_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 11 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
- None from the checker on the first full run. Two cosmetic fixes were made
  before the run: M11 used a fragile `self.mobjects[-7:]` slice to clear the
  recap phase (replaced with an explicit `shown` list); M04 positioned a tag
  with a no-op `next_to(VGroup(), ...)` (replaced with a plain `shift`).
  `import numpy as np` was included from the start, per the Film 4 lesson.

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md).
- Numbers spoken as words in `line` ("one thousand", "times two" badge shown
  as "x2" — the badge reads "times two" aloud), digits on screen.
- Judgments voiced exactly as FACTCHECK.md requires ("the film's rule of
  thumb", "the film's summary line"); no retailer names, no dollar figures.
- BVDT is exactly 3 lines (one per act). BOUT carries the next-film teaser.
