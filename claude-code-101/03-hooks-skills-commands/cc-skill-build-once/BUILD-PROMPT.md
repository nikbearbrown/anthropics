# BUILD-PROMPT — cc-skill-build-once

The prompt this reel was built from (the third-tier concept in the Claude Code 101 series):

> **Skill File Anatomy: Build Once, Invoke Every Semester.** Teachers re-specify the same grading workflow every two weeks. A `SKILL.md` file stores it once. Show what changes when the file is there vs when it isn't — and be honest about what a skill's `Never` section can and cannot enforce.

## What this reel actually films

Same one-sentence teacher's ask (`Grade student-submission.md — feedback and a final grade please.`), run four times headless against a small scratch folder in Claude Code 2.1.150:

1. **Bare** — no `.claude/skills/`, no checker. Claude invents a rubric and hands back `A- (92/100)`.
2. **With the skill** — same ask; `.claude/skills/grading-workflow/SKILL.md` (54 lines) + `check_grade.py` (34 lines) present. `Skill(grading-workflow)` appears in the transcript as a tool call; Claude follows the workflow, writes `feedback/mira.md`, runs the checker itself → `PASS`. Refuses a final grade even though the ask requested one.
3. **Durability** — a different student's submission. Same skill fires, same rubric shape, `PASS`.
4. **Pressure** — I really do need a percent, for the gradebook. Skill fires again, Claude reads the checker itself before writing, still refuses. `Never` held — but not because it is a law.

## Deviations from the concept card

- The concept framed skill invocation as `/grading-workflow` (slash command). Real Claude Code 2.1.150 auto-launches a skill by matching the natural-language ask against the `description:` in the frontmatter — visible as a `Skill()` tool call in the stream-json. Films the actual behavior.
- The concept's timing claim ("18 min → 90 sec") is generic. This reel does not stage a stopwatch; it shows the receipt (a 32-second bare wall-clock next to a 36-second skill wall-clock — the saving lives in Liam not re-typing the workflow, not in a Claude wall-clock delta).
- The concept's B03 named the `Never`-vs-hook distinction as a footnote. This reel makes it the correction cycle (B05) — the pressure test IS the falsifiability moment, and the verdict's `FALSIFIABLE:` line names the disproof condition.
