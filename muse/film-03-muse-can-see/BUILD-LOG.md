# BUILD-LOG.md — Muse Can See (Film 3)

## 2026-10-03 — Film 3 build
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand
  from transcript outline §§4–5 (the NHK transcription test + the PHP-Nuke
  website build).
- Wrote make_sheet.py by hand: 14 beats (9 body), asserts hold,
  beats=14 body=9 total=282s.
- Wrote scenes.py by hand: 12 classes, house template, custom two-Line
  check_mark() / cross_mark(), every text reveal paired with a shape change.
- **QC first pass:** 11/12 classes clean. M12_BvdtHtfOut failed with 1 error:
  the recap-line centering computed from `t.width` tripped the static
  checker's out-of-frame estimate (e.g. (9.2,1.3) in move_to). Fixed by
  laying out each line as a `VGroup(dot, text).arrange(RIGHT)` centered at a
  fixed x. Re-ran: 12/12 clean, 0 warnings, 0 errors.
- py_compile clean on both .py files; __pycache__ removed.
- Filled CLAUDE-CODE-PROMPT.md from the template (reel slug
  muse-film-03-muse-can-see); wrote CLAUDE-CODE-RENDER.md.
- Package complete in /tmp/muse_pkg/film-03-muse-can-see/ — handed to the
  parent for push.

## Next
- Parent pushes 12 files to muse/film-03-muse-can-see/ in nikbearbrown/anthropics.
- Bear renders via CLAUDE-CODE-PROMPT.md on his Mac.
- Then Film 4 ("Thinking on Canvas").
