# CHECKS-REPORT.md — Thinking on Canvas (Film 4)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=14, body=9, total=282s.

Static checker per class (`static_scene_check.py scenes.py --class <C>`),
final run — all clean:

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01Ask | 1 clean · 0 warn · 0 error |
| M04_B02Judge | 1 clean · 0 warn · 0 error |
| M05_B03Pick | 1 clean · 0 warn · 0 error |
| M06_B04Map | 1 clean · 0 warn · 0 error |
| M07_B05Read | 1 clean · 0 warn · 0 error |
| M08_B06Ground | 1 clean · 0 warn · 0 error |
| M09_B07Editor | 1 clean · 0 warn · 0 error |
| M10_B08Loop | 1 clean · 0 warn · 0 error |
| M11_B09Why | 1 clean · 0 warn · 0 error |
| M12_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 12 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
- M06_B04Map, M07_B05Read, M10_B08Loop, M11_B09Why: `construct() raised
  NameError: name 'np' is not defined`. The checker's manim stub does not
  export `np` from `from manim import *`. Fix: added `import numpy as np` at
  the top of scenes.py. All four passed on re-run. Nothing hidden.

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md).
- Numbers spoken as words in `line` ("two to three", "three"), digits on screen.
- Attributed judgments voiced exactly as FACTCHECK.md requires ("his words",
  "his verdict"); the "ask, draw, refine" loop voiced as the film's framing.
- BVDT is exactly 3 lines (one per act). BOUT carries the next-film teaser.
