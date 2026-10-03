# BUILD-PROMPT — cc-five-questions-before-code

The prompt to build this reel from scratch: read `brutalist-art/skills/make/cc-explainer/SKILL.md`, read the exemplar `anthropics/claude-code-101/01-context-and-memory/cc-three-files/` (author_sheet.py + SESSION.md + FACTCHECK.md), then film ONE calibration-vs-cold experiment against a tiny scratch project.

The concept, from `anthropics/claude-code-101/00-what-it-is/claude-code--claude-liam-five-questions-before-code/beat_sheet.json`: "The dangerous moment is when Claude has read the files and looks ready to build. Five questions in read-only mode surface the wrong assumption before the first tool call."

The film shows a real, checkable version of that claim:
- a scratch `study-readings` python module with an ambiguity the ask does not resolve (how to handle NaN readings from a real-world log Liam has);
- four fresh `claude -p` runs (cold, calibration-questions, calibration-build, Q5-only);
- Liam's plain-shell verify against `evidence/production.log` for each build.

Contract: TERMINAL-FIRST (default surface CCSession); REAL-SESSION (every block traces to `SESSION.md`); TYPES-NOT-NARRATES (prompt blocks are what Liam typed); Liam (Kokoro `am_onyx`), in for Bear, on every beat; CONDUCT + HUMAN before the recap; BVDT → BHTF → BOUT; OUTRO-LOCK. Never publishes.
