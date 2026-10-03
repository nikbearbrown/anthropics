# FACTCHECK — cc-grading-skill-definition

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (four real fresh headless runs, Claude Code 2.1.150) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the four runs' stream-json, the two feedback files Claude wrote per run, the two SKILL.md drafts, and the checker script — all in `evidence/`. Liam's checks were run in a plain shell on the evidence folder. Claude's sentences are verbatim spans from the transcripts.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | The ask, "grade Mira's paper, feedback and a final grade" | PASS | `evidence/ask-bare.txt` | — |
| 2 | B00 | Bare run: Reads submission and rubric, Writes feedback with `## Final grade` reading "4/4 pass — meets every criterion." | PASS | `run-bare.jsonl` (line: Write feedback/mira.md); `feedback-bare.md` line 19 | — |
| 3 | B01 | `wc -l feedback/mira.md` → 19; `grep -c 'Final grade'` → 1; `check_feedback.py` → FAIL on "## Final grade" | PASS | `feedback-bare.md`; `check_feedback.py` on it (measured) | — |
| 4 | B02 | 14 lines; frontmatter with `name:` and `description:`; three-step workflow body | PASS | `evidence/SKILL-minimal.md` (wc -l → 14) | — |
| 5 | B03 | Minimal run: `Skill(grading-feedback)` fires; Reads; Writes; the Final-grade heading appears; "3 pass / 1 needs work" | PASS | `run-minimal.jsonl` (tool call: Skill with `skill:"grading-feedback"`); `feedback-minimal.md` lines 15–18 | — |
| 6 | B04 | `grep -c '^## ' feedback/mira.md` → 6 headings; `grep 'Final grade'` present; checker FAIL | PASS | `feedback-minimal.md`; measured | — |
| 7 | B05 | 27 lines; the two added blocks — `## Never` (three bullets: no grade / no heading / name refusal) and `## Definition of done` (run `check_feedback.py`; must print PASS) | PASS | `evidence/SKILL-full.md` (wc -l → 27); `sed -n '15,27p' SKILL.md` | — |
| 8 | B06 | Full run: `Skill(grading-feedback)` fires; three Reads including `check_feedback.py`; Write feedback; `Bash python3 check_feedback.py` → PASS; Claude then says "per the skill's rules I did not attach a final grade" | PASS | `run-full.jsonl` (Skill, Read×3, Write, Bash tool calls; assistant text at end of transcript) | — |
| 9 | B07 | Plain-shell verify: `grep -c 'Final grade'` → 0; `grep -c '^## '` → 5 headings; `check_feedback.py` → PASS | PASS | `feedback-full.md`; measured | — |
| 10 | BFLOW | Four sections of SKILL.md: frontmatter name / description / Workflow / Never / Definition of done — five rows (name and description are two rows of the frontmatter) | PASS | `SKILL-full.md` structure | — |
| 11 | BSHOW | Durability run: same skill on `priya.md`; `Skill()` fires; Read + Write + Bash; checker PASS | PASS | `run-priya.jsonl`; `feedback-priya.md`; measured | — |
| 12 | BCONDUCT | Six steps; tally PF 2 · PA 1 · IJ 0 · TO 0 · EI 1 (dangerous middle = step 3) | PASS | maps to SESSION.md | — |
| 13 | BHUMAN | Ledger rows — the AI's CAN/SHOULD come from what the transcripts actually contain (Skill() firing, checker running, refusal spoken); the human's MUST comes from the file diff Liam made | PASS | run transcripts + `SKILL-full.md` diff vs `SKILL-minimal.md` | — |
| 14 | BVDT | Verdict lines: 4/4 vs 3-pass-1-needs-work vs full-skill PASS across two students | PASS | `feedback-bare.md`, `feedback-minimal.md`, `feedback-full.md`, `feedback-priya.md` | — |
| 15 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 16 | all | Model/version strings; costs; wall-clock durations | EXEMPT | not shown or spoken in narration | — |
