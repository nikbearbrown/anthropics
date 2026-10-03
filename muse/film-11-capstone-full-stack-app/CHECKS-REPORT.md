# CHECKS-REPORT.md — Capstone: Ship a Full-Stack App (Film 11)

Gate: `py_compile` clean on both `.py` files; every scene class
`1 clean · 0 warn · 0 error` on the static checker.

## Per-class results

| Class | Beat(s) | Result | First-pass issues |
|---|---|---|---|
| M01_Bidea | BIDEA | 1 clean · 0 warn · 0 error | none |
| M02_Bdefs | BDEFS | 1 clean · 0 warn · 0 error | none |
| M03_B01Doc | B01 | 1 clean · 0 warn · 0 error | none |
| M04_B02Stack | B02 | 1 clean · 0 warn · 0 error | none |
| M05_B03Sql | B03 | 1 clean · 0 warn · 0 error | none |
| M06_B04Goal | B04 | 1 clean · 0 warn · 0 error | none |
| M07_B05Decompose | B05 | 1 clean · 0 warn · 0 error | none |
| M08_B06Build | B06 | 1 clean · 0 warn · 0 error | none |
| M09_B07Mvp | B07 | 1 clean · 0 warn · 0 error | none |
| M10_B08Compose | B08 | 1 clean · 0 warn · 0 error | none |
| M11_B09React | B09 | 1 clean · 0 warn · 0 error | none |
| M12_B10Rough | B10 | 1 clean · 0 warn · 0 error | none |
| M13_BvdtHtfOut | BVDT+BHTF+BOUT | 1 clean · 0 warn · 0 error | none |

**Totals: 13 clean · 0 warnings · 0 errors.**

## Issues found and fixed (first pass)

None. The checker ran clean on the first pass against the final version.
The `import numpy as np` at the top of `scenes.py` was included from the
start (Film 4's lesson: the checker's manim stub does not export `np`), and
the two-`Line` `check_mark()` convention was followed throughout. Recorded
honestly: this was a first-pass clean run.
