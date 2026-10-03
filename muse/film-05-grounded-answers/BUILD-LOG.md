# BUILD-LOG.md — Grounded Answers (Film 5)

Build steps, 2026-10-03.

1. Read REFERENCE-film-pattern.md, SERIES-PLAN.md (Film 5 entry), and
   transcript-outline.md §7 (Search grounding, 36:45–44:52).
2. Wrote ACTS.md: hook + 4 terms + 3 acts (8 body beats) + recap/your-turn/
   outro; core promise "know when to ground and what it costs"; LEFT OUT
   named retailers, exact prices, the per-1k dollar rate (not in sources).
3. Wrote SHOTLIST.md: 11 scenes, every on-screen word read aloud.
4. Wrote FACTCHECK.md: 9 claims — 7 Verified (record), 2 Judgment; cuts
   recorded.
5. Wrote make_sheet.py (13 beats, 8 body, durations land at 282 s) and
   generated beat_sheet.json. Asserts hold: beats=13 body=8 total=282s.
6. Wrote scenes.py (11 classes, house template, `import numpy as np` at top
   after the Film 4 lesson).
7. QC: `py_compile` clean; static checker — 11 clean · 0 warnings · 0 errors
   on the first full run. Two cosmetic pre-QC edits (fragile mobject
   handling in M11, a no-op `next_to` in M04) made before the run.
8. Wrote SOURCES.md, CHECKS-REPORT.md, PROMPTS.md, CLAUDE-CODE-RENDER.md,
   and CLAUDE-CODE-PROMPT.md (filled from the template: title "Grounded
   Answers", 13 beats, 282 s, reel muse-film-05-grounded-answers).
9. Removed `__pycache__`. No MP3/MP4 created. Nothing committed (push is the
   parent's job).

No failures during the build. The only pre-QC edits were the two cosmetic
fixes above, made before the first checker run.
