# BUILD-LOG — cc-claude-skills--claude-liam-example-skill

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · built 2026-09-10.

**The experiment.** One sentence — "Peek at sales.csv and write the result to peek.md." — under three shapes of the same skill folder, each a fresh headless run isolated to `/tmp`:

1. Bare — no `.claude/skills/` at all. Ad-hoc peek.md (28 lines, tables, quick notes). `Skill()` calls: **0**. `check_peek.py` → FAIL.
2. Full — csv-peek/SKILL.md 40 lines (frontmatter + format spec + rules + a definition of done). `Skill(csv-peek)` fires from the description alone. peek.md written in the exact 4-heading shape (5 lines). `check_peek.py` → **PASS**, called by Claude itself because the body told it to.
3. Bare frontmatter — same folder, SKILL.md gutted to 4 lines (only the frontmatter, no body). `Skill(csv-peek)` STILL fires. peek.md written with the same information but in a different shape (lowercase headings, no `##`). No automatic checker call. `check_peek.py` → FAIL.

**What the runs proved.** The template's central claim — description-as-trigger — is verified twice (Runs B and C). Its silent claim — that the body is decoration — is falsified: the body is where two runs of the same skill produce the same shape. That is the film's argument, and its FALSIFIABLE line is a claim you could actually run.

**Compile.** One pass, no re-renders needed. Bookend and TYPECHECK PASS on the first try. Gate V 0/0/0 BLOCKER/STRUCTURAL/COSMETIC across 30 sampled frames. GATE T PASS. GATE SHARPNESS PASS (median LV=633). GATE AUDIO PASS (-23.7 dB). GATE MASTER PASS (3840×2160 · 24fps · h264 · 261.0 s). GATE LOUDNESS PASS (-24.2 LUFS, tp -2.78 dBTP). GATE BOOKEND PASS. Frame QC at 90 % (B00, B03, B04, B08, B09, BVDT) — every dense beat reads cleanly, ledger and score strings within budget, verdict paginates 2+2 with FALSIFIABLE as the last line.

**Advisory notes (non-blocking):**
- SKIN LINT flag on B00 — "palette=claude but the cold open is CCSession (COLD OPEN LAW wants ClaudeComposerAsk)". Intentional: TERMINAL-FIRST LAW in this skill's SKILL.md explicitly permits `CCSession` as a cold-open surface for cc-explainer, and `metadata.skill: "cc-explainer"` is set so `bookend_check.py` accepts it (which it did — bookend PASS).
- MOTION histogram: `type:10 drawon:3 hold:2` — `type` at 66 % over the 40 % pantry ceiling. Every CCSession renders as `motion:"type"`; changing that would misrepresent what a terminal actually does. Accepted for this genre, matching all sibling cc-explainer reels.

**Not published.** Master stays in the reel folder. TOPOST via `post`, only on ask.

**Master.** `cc-claude-skills--claude-liam-example-skill.mp4` — 261.0 s (4:21), 3840×2160, h264/aac.
