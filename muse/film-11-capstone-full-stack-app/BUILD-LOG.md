# BUILD-LOG.md — Capstone: Ship a Full-Stack App (Film 11)

Built 2026-10-03. Capstone film: a real app from idea to running containers.

1. Read the pattern reference, series plan (Film 11 entry), and transcript
   outline §13 (capstone coverage 1:58:21–2:36:02).
2. Drafted the 15-beat spine: hook → 4 terms → plan (3) → build (4) →
   ship (3) → recap (3 lines) → your turn → outro (teaser Film 12).
3. Wrote `make_sheet.py` with the full beat dict; asserts held first run:
   beats=15, body=10, total=280s.
4. Generated `beat_sheet.json` from the sheet.
5. Wrote planning docs: ACTS.md, SHOTLIST.md, FACTCHECK.md (12 claims:
   8 Verified record, 4 Judgment), SOURCES.md.
6. Wrote `scenes.py` (13 classes) on the house template; `import numpy as np`
   included at top from the start per the Film 4 checker-stub lesson.
7. QC: `py_compile` clean; static checker 13/13 clean on the first pass —
   0 warnings, 0 errors. No fixes needed (recorded honestly in
   CHECKS-REPORT.md).
8. Wrote CLAUDE-CODE-RENDER.md and CLAUDE-CODE-PROMPT.md (reel slug
   `muse-film-11-capstone-full-stack-app`), filled from the template.
9. Wrote PROMPTS.md. Removed `__pycache__`. Nothing committed.

Decisions: the film stays at the architecture level — no endpoint paths,
table schemas, or compose literals on screen or in narration, because none
were verified. The "rough edges" list is named, not glossed over; that is
part of the capstone's credibility.
