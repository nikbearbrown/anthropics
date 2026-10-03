# FACTCHECK — cc-engineering-partner-loop

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (two real headless sessions, four runs total) and `evidence/`.

**Verification boundary.** Every number, tool call, prompt string, diff line, and shell line on screen traces to `evidence/run-{bare,partner-plan,partner-apply,partner-correct}.jsonl`, `evidence/verify.txt`, and the files in `scratch/`. Claude's sentences are verbatim spans from the run transcripts. Kit-inflicted rewording — CCSession text blocks must fit ≤ ~44 chars and are wrapped at clause boundaries; multi-line prompt blocks are shortened at authoring — is marked "PARAPHRASE-KIT". The source concept's framing ("engineering partner", not code generator) is kept.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Bare-run prompt "Fix the failing tests." | PASS | verbatim; used as `claude -p` argument for run-bare | — |
| 2 | B00 | Bare-run tool sequence: Read ranges.py, Read test_ranges.py, Bash unittest, Edit ranges.py, Bash unittest | PASS | `run-bare.jsonl` (initial `Bash ls` omitted for height — CCSession has 4 lines of tool budget) | — |
| 3 | B00 | Claude's line "Two failures — reversed and extra dashes both need to raise." | PASS | run-bare.jsonl assistant text: "Two failures: reversed ranges and extra dashes need to raise `ValueError`." — split at 44-char boundaries and lightly reworded to fit kit type budget | PARAPHRASE-KIT |
| 4 | B00 | Final line "Ran 5 tests. OK." | PASS | run-bare.jsonl Bash result tail lines: `Ran 5 tests in 0.000s / OK` | — |
| 5 | B01 | 5 tests all green, `git diff --stat ranges.py` → 7 insertions / 1 deletion, `grep -c 'raise ValueError'` → 2 | PASS | `evidence/verify.txt` (partner-loop final state — same total-added count as bare because the substantive diff is identical) | — |
| 6 | B02 | Partner ask "Oracle is test_ranges.py. Don't edit. Give me the plan + exact diff." | PASS | shortened for the prompt block; the full sentence Liam typed for `run-partner-plan.jsonl` is in `SESSION.md` verbatim | PARAPHRASE-KIT |
| 7 | B02 | Tool sequence: Read test_ranges.py, Read ranges.py; status "Planning" | PASS | `run-partner-plan.jsonl` (Edit/Write withheld; only Reads possible) | — |
| 8 | B03 | The 4-step plan: len(parts) is neither 1 nor 2 raises; start > end raises; leave 1-part branch; nothing outside parse_range | PASS | `run-partner-plan.jsonl` assistant text (the four "Plan" bullets), condensed for the plan block | PARAPHRASE-KIT |
| 9 | B03 | Diff shape: 5 added lines, 1 removed | PASS | `run-partner-plan.jsonl` diff fences; `git diff ranges.py` after apply matches | — |
| 10 | B03 | Diff line strings (ValueError('invalid range'), ValueError('reversed range'), start/end) | PASS | derived from run-partner-plan diff; f-strings shortened to string literals for kit width — full text in evidence/ranges.partner.py | PARAPHRASE-KIT |
| 11 | B04 | "Plan approved. Apply the diff exactly." — Edit, unittest, OK | PASS | `run-partner-apply.jsonl` (turn 2, resumed session) — Edit + Bash + assistant text "Ran 5 tests in 0.000s — OK." | — |
| 12 | B05 | Grep output showing docstring says "'' or reversed is an error" and code raises 2 different errors | PASS | `evidence/verify.txt` interim state after the partner-apply turn (before turn 3); docstring drift verifiable via `grep '"""' evidence/ranges.partner.py` | — |
| 13 | B06 | Re-prompt: "Docstring is stale. Update only the docstring. No logic change." — Edit, git diff shows only docstring line change, unittest OK | PASS | `run-partner-correct.jsonl` — Edit + Bash `git diff ranges.py && python3 -m unittest test_ranges -v` → OK | — |
| 14 | B06 | Diff lines shown: "'' or reversed is an error" → "'', reversed, or extra dashes" | PASS | `evidence/ranges.final.py` docstring; matches `git diff` output in run-partner-correct.jsonl | — |
| 15 | BFLOW | Five nodes: ORACLE, ASK, PLAN, DIFF, VERIFY; edges in that order | PASS | mapping of the run structure to a diagram — every node traces to a session step (oracle=test_ranges.py, ask=user prompt, plan=turn-1 text, diff=turn-1 fences / turn-2 Edit, verify=turn-2 Bash unittest) | — |
| 16 | BSHOW | `python3 -m unittest test_ranges -v` output — 5 tests, all `ok`, `Ran 5 tests in 0.000s`, `OK` | PASS | `evidence/verify.txt` verbatim | — |
| 17 | BCND | Six-step Boondoggle score; dangerousMiddle=step 3 (Liam reads diff after) | PASS | maps to SESSION.md: step 1 F-human (name oracle), 2 C-claude (bare run), 3 C-human PA (post-hoc diff read), 4 F-human (partner ask), 5 C-claude (plan + apply), 6 H-human IJ (docstring drift) | — |
| 18 | BHMN | Ledger rows (each ≤ 30-34 chars) — MUST/SHOULD human, CAN/SHOULD AI | PASS | each row is a claim about the session; e.g. "fix a failing test in one shot" = run-bare's 7 turns; "write the plan before the edit" = run-partner-plan turn | — |
| 19 | BVDT | Verdict 4 lines: bare/partner/timing/FALSIFIABLE | PASS | rows 2, 6–11, 15; the falsifiable clause names a specific counter-observation | — |
| 20 | BHTF | Viewer's prompt | EXEMPT | instruction | — |
| 21 | all | Costs ($0.281, $0.196, $0.195, $0.201), turn counts, session UUIDs | EXEMPT | recorded in SESSION.md; not spoken or shown on screen | — |
| 22 | all | Claude Code version (2.1.150), 2026-09-09 date | EXEMPT | recorded, not spoken or shown | — |
| 23 | all | Model / provider names | EXEMPT | not shown or spoken | — |
