# BUILD-LOG.md — Thinking on Canvas (Film 4)

## 2026-10-03 — Film 4 build (subagent, series build sprint)
- Read REFERENCE-film-pattern.md, the Claude Code prompt template, and
  transcript-outline §6 (brainstorming + mermaid diagrams, 26:00–36:38).
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand.
- Wrote make_sheet.py (14 beats, 9 body, 282s); asserts hold:
  beats=14 body=9 total=282s.
- Wrote scenes.py (12 classes; M12 covers BVDT+BHTF+BOUT).
- QC first pass: 8 classes clean; M06, M07, M10, M11 failed with
  `NameError: name 'np' is not defined` — the checker's manim stub does not
  export `np`. Fixed by adding `import numpy as np` to scenes.py. Re-ran:
  12/12 clean · 0 warn · 0 err.
- Spot-checked narration: attributions intact ("his words", "his verdict"),
  numbers as words, every on-screen word voiced.
- Filled CLAUDE-CODE-PROMPT.md from the template; wrote CLAUDE-CODE-RENDER.md.
- __pycache__ removed. Nothing committed (parent pushes via gh-put-file.py).

## Notes
- The source is thin (one outline section); every claim traces to transcript
  §6 lines. The "ask, draw, refine" loop is labeled as the film's framing
  (Judgment in FACTCHECK), not the instructor's words.
