# FACTCHECK — cc-five-questions-before-code

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (four real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the four runs' stream-json, the built files in `evidence/stats.<run>.py` and `evidence/test_stats.<run>.py`, and Liam's plain-shell verify against `evidence/production.log`. Claude's sentences are verbatim spans (or minor display truncation flagged in-cell). The source concept's framing (five questions in read-only mode; the dangerous moment is when Claude looks ready to build) is kept; its "hypothetical stylesheet story" is dropped in favour of a real, checkable session.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B04 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Cold run: Reads (stats.py, readings.log), "A few things here are ambiguous.", AskUserQuestion, dismissed, defaults, Edit stats.py, Write test_stats.py, `python3 -m unittest test_stats` → 7 tests OK | PASS | `evidence/run-cold.jsonl` (README + ask Reads omitted for height; the "ambiguous" line and "dismissed → recommended defaults" are Claude's own verbatim spans, trimmed) | — |
| 3 | B00 | "It tries to ask. The tool is fenced." | PASS | `AskUserQuestion` was outside the allowed-tools fence in the cold run; the tool result registered as a dismissal | — |
| 4 | B01 | `python3 -m unittest test_stats` → "Ran 7 tests. OK." on the cold build | PASS | `scratch-cold/` after run-cold; SESSION.md VERIFY | — |
| 5 | B01 | `read_log(prod), avg_temp(prod)` → `avg= nan` on `production.log` | PASS | SESSION.md VERIFY; `evidence/stats.cold.py` uses `float(v)` which accepts the string "NaN" and poisons the mean | — |
| 6 | B01 | `head -3 production.log` shows a NaN row on row 10:00 | PASS | `evidence/production.log` rows 1–3 verbatim | — |
| 7 | B02 | The five questions text, in order | PASS | `evidence/five-questions.txt` | — |
| 8 | B02 | `wc -l five-questions.txt` → 8 | PASS | the file is 8 lines (5 numbered + 2 header + 1 blank) | — |
| 9 | B03 | Calibration run: the 5-question prompt (abbreviated on-screen as "5 questions, read-only. Q1..Q5."), Reads (stats.py, readings.log), five short answers | PASS | `evidence/run-calib-q.jsonl` — the on-screen prompt is a legitimate shorthand of the full text Liam pasted (recorded verbatim in `SESSION.md`); the five text-block answers are one-line paraphrases of Claude's five markdown-headed answers | — |
| 10 | B03 | Q5 surfaces two pivots: (1) empty input, (2) malformed row; and Claude's line "1 and 2 would change the code." | PASS | `evidence/run-calib-q.jsonl` Q5 verbatim: "Numbers 1 and 2 are the ones I'd rather not guess — the answer changes the code." | — |
| 11 | B04 | Liam's answer to Q5 (empty → None; skip malformed; skip 'NaN' string; add NaN test), then Write ×2, then unittest → 8 OK, then production → 21.47142857142857 | PASS | `evidence/run-calib-build.jsonl`; `scratch-calib/test_stats.py` contains `test_nan_row_is_skipped`; Liam's shell verify recorded in SESSION.md | — |
| 12 | B04 | "Wrote both, did not run them." | PASS | Claude's line in `run-calib-build.jsonl` verbatim: "You said read-only until you said 'build it' — you have now, so I wrote both files but didn't run them." (trimmed for display) | — |
| 13 | B05 | Q5-only run: same two pivots surface (empty input; malformed row); "1 and 2 would change the code." | PASS | `evidence/run-q5only.jsonl` — same wording as B03: "Numbers 1 and 2 are the ones I'd rather not guess — the answer changes the code." | — |
| 14 | B06 | Six steps; dangerousMiddle = step 2; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | maps to SESSION.md (cold run = step 2; production verify = step 3; calibration + build = steps 4-5; Q5-only observation = step 6) | — |
| 15 | B07 | Ledger rows — "make silent choices when blocked" (cold run's AskUserQuestion), "pass its own tests" (7/7 green), "ask five questions when asked" (calibration Q1–Q4), "name what it is uncertain about" (Q5 answer) | PASS | all four rows trace to the runs | — |
| 16 | BVDT | Verdict lines; "21.47" | PASS | rows 4–15; `scratch-calib` verify against `production.log` → 21.47142857142857 | — |
| 17 | BHTF | The viewer's prompt (the five questions template) | EXEMPT | instruction | — |
| 18 | all | Model/version strings; "Claude Code 2.1.150" appears in SESSION.md but is not shown or spoken | EXEMPT | not shown or spoken | — |
| 19 | metadata | Costs ($0.419 / $0.268 / $0.296 / $0.258) and session ids | EXEMPT | recorded in SESSION.md, not spoken | — |
