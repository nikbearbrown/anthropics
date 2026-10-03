# CHECKS-REPORT.md — Structured Outputs (Film 6)

Static QC gate: every scene class must read `1 clean · 0 warn · 0 error`.
`py_compile` clean on `make_sheet.py` and `scenes.py`. Verified 2026-10-03.

| Class | Beat(s) | Result |
|---|---|---|
| M01_Bidea | BIDEA | 1 clean · 0 warn · 0 error |
| M02_Bdefs | BDEFS | 1 clean · 0 warn · 0 error |
| M03_B01Why | B01 | 1 clean · 0 warn · 0 error |
| M04_B02Rubric | B02 | 1 clean · 0 warn · 0 error |
| M05_B03Save | B03 | 1 clean · 0 warn · 0 error |
| M06_B04Challenge | B04 | 1 clean · 0 warn · 0 error |
| M07_B05Attempt | B05 | 1 clean · 0 warn · 0 error |
| M08_B06Graded | B06 | 1 clean · 0 warn · 0 error |
| M09_B07Read | B07 | 1 clean · 0 warn · 0 error |
| M10_B08Feed | B08 | 1 clean · 0 warn · 0 error |
| M11_B09Report | B09 | 1 clean · 0 warn · 0 error |
| M12_BvdtHtfOut | BVDT+BHTF+BOUT | 1 clean · 0 warn · 0 error |

**Totals: 12 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)
None. All 12 classes passed on the first run. `import numpy as np` was
included from the start (the checker's manim stub does not export `np` —
lesson recorded from Film 4). Custom two-`Line` `check_mark()` used
throughout; `Checkmark` never used. Every text reveal is paired with a
non-text shape change (rings, arrows, cards, dots); no text-only scenes.
