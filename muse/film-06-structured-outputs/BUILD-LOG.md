# BUILD-LOG.md — Structured Outputs (Film 6)

## 2026-10-03 — Film 6 build (subagent, series build sprint)
- Read REFERENCE-film-pattern.md, the Claude Code prompt template,
  SERIES-PLAN.md (Film 6 entry), transcript-outline §8, and Film 4's full
  package as the style reference.
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand.
- Wrote make_sheet.py (14 beats, 9 body, 284s); asserts hold:
  beats=14 body=9 total=284s.
- Wrote scenes.py (12 classes; M12 covers BVDT+BHTF+BOUT).
- QC first pass: 12/12 clean · 0 warn · 0 err. No fixes needed. py_compile
  clean on both .py files.
- Spot-checked narration: numbers as words ("seventy out of one hundred"),
  every on-screen word voiced, judgments labeled ("the film's reading").
- Filled CLAUDE-CODE-PROMPT.md from the template; wrote CLAUDE-CODE-RENDER.md.
- __pycache__ removed. Nothing committed (parent pushes via gh-put-file.py).

## Notes
- The source is thin (one outline section); every claim traces to transcript
  §8 lines. The seventy-out-of-one-hundred walkthrough detail comes from the
  series brief's §8 beat plan and is marked Judgment in FACTCHECK.md.
