# BUILD-LOG.md — Agents and Frameworks (Film 8)

## 2026-10-03 — Film 8 build (subagent, series build sprint)
- Read REFERENCE-film-pattern.md, the Claude Code prompt template,
  SERIES-PLAN.md (Film 8 entry), and transcript-outline §§10–12 (agent SDK,
  LangChain, Claude Code on Muse).
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand.
- Wrote make_sheet.py (14 beats, 9 body, 280s); asserts hold:
  beats=14 body=9 total=280s.
- Wrote scenes.py (12 classes; M12 covers BVDT+BHTF+BOUT). `import numpy as
  np` included from the start (Film 4's checker-stub lesson); two-`Line`
  `check_mark()` throughout; no `Checkmark`.
- Pre-QC fix: `IndentationError: unexpected indent` in M01_Bidea (a stray
  closing paren left from an edit) — caught by `py_compile` before the
  checker ran; fixed, re-compiled clean.
- Static checker per class: 12/12 clean · 0 warn · 0 err on the first
  checker run. The M12 recap phase was rewritten mid-build (dead code from
  an edit removed; lines now reveal sequentially after the card fades in).
- Spot-checked narration: every on-screen word voiced in its beat (incl.
  the long recap/your-turn/outro cards); numbers as words in `line`
  ("one point two"), digits on screen; judgments voiced as the film's
  framing ("the film's checklist", "the film's reading", "the film's
  closing framing").
- Filled CLAUDE-CODE-PROMPT.md from the template; wrote CLAUDE-CODE-RENDER.md.
- __pycache__ removed. Nothing committed (parent pushes via gh-put-file.py).

## Notes
- The source is thin (three short outline sections); claims 3, 4, 11, 12 in
  FACTCHECK.md are labeled Judgment — the outline records the tasks, not
  every outcome or the film's framings. The "finished game" reading (claim 4)
  is the film's, not a quoted record.
