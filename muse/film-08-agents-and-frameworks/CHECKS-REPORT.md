# CHECKS-REPORT.md — Agents and Frameworks (Film 8)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean (after one fix, see
below).
`beat_sheet.json` — parses; asserts hold: beats=14, body=9, total=280s.

Static checker per class (`static_scene_check.py scenes.py --class <C>`),
first checker run — all clean:

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01Sdk | 1 clean · 0 warn · 0 error |
| M04_B02Task | 1 clean · 0 warn · 0 error |
| M05_B03Result | 1 clean · 0 warn · 0 error |
| M06_B04Langchain | 1 clean · 0 warn · 0 error |
| M07_B05Config | 1 clean · 0 warn · 0 error |
| M08_B06Debug | 1 clean · 0 warn · 0 error |
| M09_B07Wrapper | 1 clean · 0 warn · 0 error |
| M10_B08Launch | 1 clean · 0 warn · 0 error |
| M11_B09Odd | 1 clean · 0 warn · 0 error |
| M12_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 12 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
- `IndentationError: unexpected indent` (scenes.py, M01_Bidea) — a stray
  closing paren left from a mid-build edit. Caught by `py_compile` before
  the checker ran. Fixed by removing the stray paren; re-compiled clean.
  Recorded, not hidden.
- M12_BvdtHtfOut was rewritten mid-build: dead code from an edit (`... if
  False else None`) removed; recap lines now reveal sequentially after the
  recap card fades in. The checker ran only against the final version.

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md).
- Numbers spoken as words in `line` ("one point two", "three"), digits on
  screen ("1.2", "3").
- Attributed judgments voiced exactly as FACTCHECK.md requires; the "works
  but looks odd" verdict voiced as his.
- BVDT is exactly 3 lines (one per act). BOUT carries the next-film teaser.
