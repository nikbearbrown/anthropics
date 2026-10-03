# BUILD-LOG.md — Film 9: "Muse Code, the Harness"

## Build order
1. Read `REFERENCE-film-pattern.md`, `SERIES-PLAN.md`, `source/transcript-outline.md` §13.
2. Wrote `ACTS.md` (title, promise, acts, source facts, LEFT OUT with reasons).
3. Wrote `SHOTLIST.md` (beat → scene → visual → source; house word-mapping note).
4. Wrote `FACTCHECK.md` (17 claims; 13 Verified/record, 4 Judgment; cuts listed).
5. Wrote `make_sheet.py` (15-beat dict, asserts, prints, writes indented JSON) → ran it: `beats=15 body=10 total=280s`.
6. Wrote `scenes.py` (13 classes, house template, two-`Line` check_mark, `import numpy as np` at top).
7. `py_compile` clean on both `.py` files.
8. Static checker per class: **13 clean · 0 warnings · 0 errors, all first pass.**
9. Wrote `SOURCES.md`, `CHECKS-REPORT.md`, `PROMPTS.md`, `CLAUDE-CODE-RENDER.md`, `CLAUDE-CODE-PROMPT.md`.
10. Removed `__pycache__`. Nothing committed.

## Corrections / honest notes
- The exact install command is not in the source record; the film says "the
  docs carry the exact line" and never invents it (FACTCHECK #3, Cut list).
- Exact per-token cost of reasoning effort levels: cut as unverifiable
  (FACTCHECK #11).
- Bubblewrap sandbox detail and model switching via CLI: recorded in the
  source, cut for time; listed in FACTCHECK so the cut is visible.
- "dead ends" in B07's line is the film's gloss on session resume, disclosed
  in FACTCHECK #12.
- Total runtime landed at exactly 280s — the floor of the 280–330s envelope.
  Narration pacing: body beats 18–22s at ~135–160 wpm, inside Teardown
  delivery range.
