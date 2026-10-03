# CHECKS-REPORT.md — Memory, Skills, and Guardrails (Film 10)

## Gate results (2026-10-03)
`python3 -m py_compile make_sheet.py scenes.py` — clean.
`beat_sheet.json` — parses; asserts hold: beats=15, body=10, total=288s.

Static checker per class (`static_scene_check.py scenes.py --class <C>`),
final run — all clean:

| Class | Result |
|---|---|
| M01_Bidea | 1 clean · 0 warn · 0 error |
| M02_Bdefs | 1 clean · 0 warn · 0 error |
| M03_B01Memory | 1 clean · 0 warn · 0 error |
| M04_B02Css | 1 clean · 0 warn · 0 error |
| M05_B03Where | 1 clean · 0 warn · 0 error |
| M06_B04Skill | 1 clean · 0 warn · 0 error |
| M07_B05Trigger | 1 clean · 0 warn · 0 error |
| M08_B06Plugin | 1 clean · 0 warn · 0 error |
| M09_B07Approvals | 1 clean · 0 warn · 0 error |
| M10_B08Sandbox | 1 clean · 0 warn · 0 error |
| M11_B09Mcp | 1 clean · 0 warn · 0 error |
| M12_B10Duck | 1 clean · 0 warn · 0 error |
| M13_BvdtHtfOut | 1 clean · 0 warn · 0 error |

**Totals: 13 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
- M04_B02Css: code review caught the check mark overlapping the written-line
  glyphs (both centered on the plate). Fixed by shortening the glyph lines
  and moving the check to the plate's right side. Never reached the checker.
- M08_B06Plugin: code review caught a skill chip starting at x=-7.5, outside
  the hard frame (±7.12). Fixed by starting the slide-in at x=-6.3.
  Never reached the checker.
- The checker itself reported zero issues on the first run. Nothing hidden.

## Beat/sheet cross-checks (manual)
- Every on-screen word in `screen` is spoken in the same beat's `line`
  (checked beat by beat against SHOTLIST.md). Term-card glosses were
  reworded during the draft so every gloss word appears in the BDEFS line
  ("notes read every session", "a bundle the agent calls", "who says yes",
  "plugs to outside tools").
- Numbers spoken as words in `line` ("memory dot md"), digits on screen.
- Attributed judgments voiced exactly as FACTCHECK.md requires ("his
  example", "the film's framing"); the DuckDuckGo lesson voiced as his
  debugging story.
- BVDT is exactly 3 lines (one per act). BOUT carries the next-film teaser.
