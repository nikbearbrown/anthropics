# BUILD-LOG.md — Your First Prompts (Film 2)

## 2026-10-03 — Film 2 build
- Read REFERENCE-film-pattern.md, SERIES-PLAN.md, transcript §§3–4.
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand.
- Wrote make_sheet.py with the 15-beat plan (10 body beats, 280s total);
  asserts hold: beats=15, body=10, all scenes start with "M", voice "Muse".
- Wrote scenes.py (13 classes, house template) directly.
- **Bug caught before QC:** M13 phase-2 transition faded `card` twice
  (`FadeOut(card)` plus a blanket `FadeOut` over all mobjects). Fixed by
  collecting phase-2 mobjects into `turn_g` and fading once. Logged, not
  hidden.
- Ran the full gate myself: py_compile clean; all 13 classes
  `1 clean · 0 warn · 0 error` on the first checker run.
- Verified every quoted on-screen string is spoken in its beat's line
  (scripted check; digits↔words, "JLPT N5", "@NikBearBrown" as the allowed
  exceptions, same as Film 1).
- Filled CLAUDE-CODE-PROMPT.md from the template; wrote CLAUDE-CODE-RENDER.md.
- Deleted __pycache__. Nothing committed (per instructions).

## Next
- Parent pushes the 12 files to `muse/film-02-your-first-prompts/`.
- Bear pastes CLAUDE-CODE-PROMPT.md into Claude Code on his Mac → audio +
  review cut + 4K master.
