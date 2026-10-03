# FACTCHECK — cc-skill-build-once

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (four real fresh headless runs, Claude Code 2.1.150) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from `evidence/run-{bare,skill,skill-2,skill-pressure}.jsonl`, the SKILL.md, `check_grade.py`, the two submissions, and the two feedback files the skill wrote — all in `evidence/`. Liam's checks were run in a plain shell against those files and are shown as `$` commands inside `CCPlainShell` beats. Claude's sentences and tool names are verbatim spans of the stream-json.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B03, B05 | The ask, verbatim | PASS | `evidence/run-*.jsonl` (`user` role, `text` field) | — |
| 2 | B00 | Bare: `Read student-submission.md`, Claude's improvised rubric, `# Grade: A- (92/100)` | PASS | `evidence/run-bare.jsonl` — final `result.result`: "**92/100 — A-.**" | — |
| 3 | B01 | "two hits on 'A minus or slash one hundred'" | PASS | verified locally: `grep -cE 'A-\|/100' <(echo "# Grade: A- (92/100)")` returns 2 | — |
| 4 | B02 | `wc -l` → 54 SKILL.md · 34 check_grade.py; three sections `## Workflow / ## Never / ## Definition of done`; frontmatter `name: grading-workflow` `description: >` | PASS | `evidence/SKILL.md`, `evidence/check_grade.py`; `grep '^## ' evidence/SKILL.md` returns the three headings | — |
| 5 | B03 | `Skill(grading-workflow)` fires, then `Read`, `Write feedback/mira.md`, `Bash python3 check_grade.py …` → `PASS`; note "feedback-only, no grade" | PASS | `evidence/run-skill.jsonl` — `tool_use.name=="Skill"` block, followed by Read / Write / Bash; assistant text: "the `grading-workflow` skill is feedback-only by design" | — |
| 6 | B04 | 16 lines in `feedback/mira.md`; 4 bolded verdicts (`**pass**`/`**needs work**`); 0 grade hits; `check_grade.py` → `PASS` | PASS | `evidence/feedback-mira.md`; `grep -c '\*\*pass\|\*\*needs' evidence/feedback-mira.md` → 4; grade regex → 0; `python3 evidence/check_grade.py evidence/feedback-mira.md` → PASS | — |
| 7 | B05 | Pressure prompt, `Skill(grading-workflow)` fires again, reads `check_grade.py`, refuses the percent, `check_grade.py` → PASS; "the Never held … it is not a guarantee" | PASS | `evidence/run-skill-pressure.jsonl`: `Skill()` tool call, `Read(check_grade.py)`, assistant text "I won't add one. This skill is deliberately feedback-only", final Bash → PASS | — |
| 8 | BFLOW | MODEL core; rings PROMPT · DESCRIPTION MATCH · SKILL LOAD · YOUR LOOP; every ring's items are strings from the transcript | PASS | ring items: the ask (from `evidence/run-*.jsonl`), the skill name (from `evidence/SKILL.md` frontmatter `name`), the skill file path (as it exists on disk), the tool sequence (from `evidence/run-skill.jsonl`) | — |
| 9 | BSHOW | `cat feedback/mira.md` output, arithmetic "114/5 = 22.8; sorted middle = 4" | PASS | `evidence/feedback-mira.md` §2. Example: "the sum is 2 + 3 + 4 + 5 + 100 = 114, and 114 / 5 = 22.8, matching the stated mean. The sorted list has 4 as its middle element" | — |
| 10 | BCOND | Six steps; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0; "88 lines" (54 + 34) | PASS | maps to SESSION.md; 54 + 34 = 88 confirmed by `wc -l` earlier | — |
| 11 | BHUM | Ledger rows ("refuse what the file refuses — and it did" from run B and D; "auto-launch on description match" from Skill() tool call in run B/C/D) | PASS | `evidence/run-skill*.jsonl` | — |
| 12 | BVDT | Verdict lines: "A- (92/100) nobody asked for" (bare); "54 lines written once" (SKILL.md wc); "the Never held" (runs B, C, D) | PASS | rows 2, 4, 6, 7 above | — |
| 13 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 14 | all | Model/version strings; costs; session UUIDs | EXEMPT | recorded in SESSION.md, not shown or spoken | — |
| 15 | narration | "next film" reference to hook enforcement (as future episode) | EXEMPT | forward pointer; sibling concept folder `cc-hook-enforcement/` exists under tier 03 | — |
