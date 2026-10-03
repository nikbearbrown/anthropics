# CHECKS-REPORT.md — Muse Can See (Film 3)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=14, body=9, total=282s.

Static checker per class (`static_scene_check.py scenes.py --class <C>`):

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01Shot | 1 clean · 0 warn · 0 error |
| M04_B02Percent | 1 clean · 0 warn · 0 error |
| M05_B03Footnote | 1 clean · 0 warn · 0 error |
| M06_B04Ref | 1 clean · 0 warn · 0 error |
| M07_B05Sys | 1 clean · 0 warn · 0 error |
| M08_B06Result | 1 clean · 0 warn · 0 error |
| M09_B07Judge | 1 clean · 0 warn · 0 error |
| M10_B08Iterate | 1 clean · 0 warn · 0 error |
| M11_B09Mobile | 1 clean · 0 warn · 0 error |
| M12_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 12 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
- **M12_BvdtHtfOut — 1 error on first run:** the recap lines were centered
  with `t.move_to([dot.get_center()[0] + 0.35 + t.width / 2, y, 0])`; the
  checker's static text-width estimate placed the result outside the frame
  (e.g. (9.2,1.3)). Fix: build each line as
  `VGroup(dot, text).arrange(RIGHT, buff=0.35, aligned_edge=UP)` and
  `move_to([0, y, 0])` — fixed position, no width arithmetic. Re-ran clean.
- All other classes passed first try (binding rule applied from the draft;
  custom two-`Line` check_mark/cross_mark; coordinates in the safe area).

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md).
- Numbers spoken as words in `line` ("a hundred percent", "two thousand
  three"); digits on screen ("100%").
- The "100%" transcription verdict is voiced as the instructor's own test
  result, per FACTCHECK.md. The encoding-glitch footnote attributes the
  fault to the editor, not the model.
- BVDT is exactly 3 lines (one per act). BOUT carries the next-film teaser.
