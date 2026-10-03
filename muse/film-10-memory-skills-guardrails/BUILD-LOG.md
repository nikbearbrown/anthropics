# BUILD-LOG.md — Memory, Skills, and Guardrails (Film 10)

## 2026-10-03 — Film 10 build (subagent, series build sprint)
- Read REFERENCE-film-pattern.md, the Claude Code prompt template,
  SERIES-PLAN.md (Film 10 entry), and transcript-outline §13 (skills,
  memory, approvals, sandbox, MCP).
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand.
- Wrote make_sheet.py (15 beats, 10 body, 288s); asserts hold:
  beats=15 body=10 total=288s.
- Wrote scenes.py (13 classes; M13 covers BVDT+BHTF+BOUT).
- QC first pass: all 13 classes clean · 0 warn · 0 err. Pre-QC code review
  fixed two issues before the checker ran: M04's check mark overlapped its
  glyph lines (repositioned), and an M08 skill chip started off-frame at
  x=-7.5 (moved to -6.3). Both recorded here, nothing hidden.
- No numpy needed in this film's scenes, so no `import numpy as np`
  (the Film 4 checker-stub lesson did not apply).
- Spot-checked narration: attributions intact ("his example", "the film's
  framing"), numbers as words, every on-screen word voiced in its beat.
- Filled CLAUDE-CODE-PROMPT.md from the template; wrote CLAUDE-CODE-RENDER.md.
- __pycache__ removed. Nothing committed (parent pushes via gh-put-file.py).

## Notes
- The source is one outline section (§13); the CSS-rule detail comes from
  the series plan's Film 10 key beats. Judgments (the trigger framing, the
  plugin takeaway, the always-true rule of thumb, the faucet line) are
  labeled as the film's in FACTCHECK.md.
