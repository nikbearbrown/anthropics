# BUILD-LOG — cc-writer-reviewer-pattern

cc-explainer · Claude Code 101 · tier `02-plan-rewind-subagents`, film 2 · Liam, in for Bear · built 2026-09-09.

**The experiment.** One ambiguous ask — "Write pass_fail.py. It reads grades.csv and prints one line per student: '<name>: PASS' or '<name>: FAIL'. Passing is 70." — against a `grades.csv` with three awkward rows (a missing quiz, an all-blank row, an average-high/one-very-low). Three fresh headless `claude -p` runs: writer, same-context review (via `--resume`), clean-context review (fresh `--session-id` in a folder with only the four files).

**What the runs gave the film.** Both reviewers found the load-bearing issues — Dee being called FAIL after taking no quizzes, missing-quiz semantics flipping Cai's outcome, Eli passing on the mean with one very low score. What DIVERGED was the framing:

- Same-context review: four honest section headers, six paragraphs opening with "I" ("I picked", "I never asked", "I average only the two present", "I papered over"), zero line-cited findings. It reviewed the writer's *reasoning*.
- Clean-context review: leads with **Real bugs**, three numbered findings, three line cites (`pass_fail.py:10`, `:9`, `:7`), and re-derives Cai's flipped average (89 → 59.3) from `grades.csv` because it has no writer-memory to lean on.

That difference — same content, different verb — is the film's honest claim. Not "clean catches what same misses"; **same context reviews the writer, clean context reviews the code**. The starting context decides which question the reviewer asks.

**Compile.** One pass. `art run` (review cut) → GATE T PASS (§8.10 BVDT 0.84 advisory only — the verdict beat is designed to summarize the on-screen card). `art final` → content-check PASS, frame-check PASS, lane-check PASS, GATE AUDIO PASS (-23.7 dB). SKIN LINT flagged "B00: palette=claude but cold open is CCSession" — SKILL.md explicitly permits CCSession as a cc-explainer cold open surface, so the lint is a non-blocker known to the skill. Motion histogram warned type:58% — expected for a session-heavy film that lives inside the terminal.

Master: `cc-writer-reviewer-pattern.mp4`, 3840×2160, 24 fps, 250.1 s (4:10). Frame reads clean (checked B00, B01, B03, B05, B06, BVDT at 85 %) — session stacks fit, boondoggle score renders all 7 rows, ledger balanced two-column, verdict card 2/2 with the FALSIFIABLE line last.

**Kit gotcha survived:** author_sheet.py asserts CCSession text ≤ 44 chars, ledger row ≤ 34 chars, boondoggle step ≤ 46 chars, plain-shell line ≤ 50 chars. The one 37-char ledger row ("treat --resume as writing, not review") was shortened to "resume is writing, not review" before compile. Full-height CCSession beats set `mascot: "off"` per the SKILL note about Clawd landing on top of the last rows.

**Not published.** TOPOST only via `post`, only on ask. Master stays in this folder.
