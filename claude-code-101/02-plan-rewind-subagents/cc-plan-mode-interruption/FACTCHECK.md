# FACTCHECK — cc-plan-mode-interruption

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every tool name, file path, count, and sentence on screen comes from the three runs' stream-json in `evidence/run-{a-accept,b-plan,c-plan-fixed}.jsonl`, the plans in `evidence/plan-{b,c}.md`, and the baseline files in `evidence/`. Liam's checks were run in a plain shell in `scratch/`. Claude's sentences are verbatim spans. The concept card's framing — "Shift+Tab twice freezes writes" — is the interactive-UI presentation of this mechanism; the film says so at BDEFS and stays on what the headless runs actually showed: `--permission-mode plan` writes zero bytes and returns a plan document.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B02, B05 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Run A: Reads, "I'll merge the schedule into the front page, remove the now-redundant schedule.html…", Write, `rm schedule.html`, Edit | PASS | `run-a-accept.jsonl` (turns 2–8; last line display-truncated) | — |
| 3 | B00, B01 | "schedule.html — deleted" | PASS | `run-a-accept.jsonl` turn 7: `Bash rm schedule.html`; `evidence/run-a-diff.txt`: `schedule.html \| 16 ----------------` and `evidence/run-a-deleted.txt`: `schedule.html` | — |
| 4 | B01 | `git diff --stat` → 3 files, 11 ins / 19 del | PASS | `evidence/run-a-diff.txt` | — |
| 5 | B01 | "not badly — differently than you intended" | PASS | characterisation of a competent-but-uninstructed default; the resulting page is well-formed HTML, just missing the file the teacher wanted kept | — |
| 6 | BDEFS | "plan mode: writes are frozen; Claude proposes a plan and waits" | PASS | Run B: `git diff --stat` empty after 11 turns of tool use (`run-b-plan.jsonl`); `ExitPlanMode` is the closing call | — |
| 7 | BDEFS | "Shift+Tab twice" as the interactive-UI trigger | EXEMPT | product-string reference, not shown as running behaviour in this film; verified against Claude Code interactive product-string reference (kit tokens `keybindings.planToggle`); flagged in SESSION.md as the honest UI limit of a headless demo | — |
| 8 | BDEFS | "ExitPlanMode: the tool call that presents the plan and asks the user to leave plan mode" | PASS | `run-b-plan.jsonl` and `run-c-plan-fixed.jsonl` both end with a `tool_use` named `ExitPlanMode`; input carries the plan as its `plan` argument | — |
| 9 | B02 | Run B: five Reads, `Write ~/.claude/plans/…`, `ExitPlanMode`; git diff empty | PASS | `run-b-plan.jsonl`; `git diff --stat` after Run B was empty (SESSION.md VERIFY) | — |
| 10 | B02 | "plan proposes to delete schedule.html" | PASS | `evidence/plan-b.md`: "**`schedule.html`** — delete." | — |
| 11 | B03 | Liam's correction prompt, verbatim | PASS | `run-c-plan-fixed.jsonl` first user message | — |
| 12 | B03 | Run C: 3 turns, revised plan; git diff still empty | PASS | `run-c-plan-fixed.jsonl` result: `num_turns=3`; `git diff --stat` still empty | — |
| 13 | B03 | "schedule.html — unchanged" in the revised plan | PASS | `evidence/plan-c.md`: "**`schedule.html`** — unchanged." | — |
| 14 | B03 | "plan revised: schedule.html, notes.md, and README.md all stay untouched" | PASS | `run-c-plan-fixed.jsonl` last assistant text | — |
| 15 | B04 | wc / git diff --stat / grep receipts | PASS | `evidence/run-a-diff.txt`, `evidence/plan-b.md`, `evidence/plan-c.md` | — |
| 16 | B05 | Cost figures ($0.35 / $0.56 / $0.27); turn counts (9 / 11 / 3); durations (36.6 s / 62.1 s / 30.0 s) | EXEMPT | recorded in SESSION.md, not spoken on screen (dated / model-priced values are not narrated) | — |
| 17 | B06 | Boondoggle score steps and tally | PASS | maps to SESSION.md: PF Liam (the one-sentence ask); Claude bare-run (rm schedule.html); PA Liam (reading Run A's diff); Claude plan-run (plan produced, zero writes); IJ Liam (reject the delete, keep schedule.html); Claude revised plan | — |
| 18 | B07 | Ledger rows | PASS | AI CAN: write to disk before the human sees the plan (Run A); produce a plan document instead of a diff (Runs B, C). AI SHOULD: run in plan mode on unfamiliar files; hand back a plan, not a change. HUMAN MUST: read the plan, not the summary; name what "unchanged" means; refuse a delete that would cost more than 30 s to recover from. HUMAN SHOULD: keep the plan mode session on for the first run in a new folder. | — |
| 19 | BVDT | Verdict lines | PASS | rows 3, 10, 13, 15; the falsifiable line inverts the mechanism | — |
| 20 | BHTF | The viewer's prompt | EXEMPT | instruction to the viewer | — |
| 21 | all | Model names / versions / any "as of" | EXEMPT | not shown or spoken; SESSION.md records costs but the numbers are not narrated | — |
