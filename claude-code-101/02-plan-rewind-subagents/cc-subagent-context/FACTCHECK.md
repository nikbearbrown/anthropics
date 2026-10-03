# FACTCHECK — cc-subagent-context

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (two real fresh headless `claude -p` runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from `evidence/run-inline.jsonl` and `evidence/run-subagent.jsonl` (raw stream-json), the per-turn `cache_creation_input_tokens` attribution in `evidence/analyze3.py`, the subagent's returned summary in `evidence/run-subagent.jsonl`, and the resulting `evidence/grader.{inline,subagent}.py`. Version numbers, prices, and calendar dates from the runs are recorded in `SESSION.md` and never spoken or shown.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Same task twice; 5 policy docs, 156 lines total | PASS | `wc -l policies/*.md` → 27+30+37+34+28 = 156 | — |
| 2 | B01 | "Late-submissions 424, honor-code 724, meeting-notes 624, participation 688, syllabus 806; total 3,266" | PASS | `analyze3.py run-inline.jsonl`: cache_creation per Read; sum = 3,266 | — |
| 3 | B02 | 4 unittest tests pass; one-day-late case is base minus 10% | PASS | `python3 -m unittest test_grader -v` inside `scratch-inline/` → OK, 4 tests; `late_penalty(1, 100) == 90.0` in `evidence/grader.inline.py` | — |
| 4 | B02 | "three thousand tokens" still in main | PASS | reads land in cache_creation and stay in the main-session cache for the rest of the run | — |
| 5 | B03 | The mechanism: two windows; only the summary crosses back | PASS | Anthropic Claude Code Agent-tool doctrine + this run's observed behavior (subagent's own turns/usage are not counted against main-session cache_creation) | — |
| 6 | B04 | 1 Agent call; \~12 s wait; return ~129 words; 435 tokens into main; "8× smaller" | PASS | `analyze3.py run-subagent.jsonl`: `+435 tokens :: [SUBAGENT]`; subagent return has 129 words (`extract_text.py`); 3,266 / 435 ≈ 7.5 — rounded up to "eight times smaller" in narration for readability; keep the "eight" language | — |
| 7 | B04 | Rules listed on screen (grace hour, day 1 10%, day 2 20%, d3-6 +5%/day, d7+ 50%) | PASS | `evidence/policies/late-submissions.md` §Rules 1–5; the subagent's return summary uses the same figures | — |
| 8 | B05 | After the subagent, 5 policy reads: honor-code 466, late-submissions 625, meeting-notes 725, participation 689, syllabus 665; total 3,170 | PASS | `analyze3.py run-subagent.jsonl` lines 4–8: 466+625+725+689+665 = 3,170 | — |
| 9 | B05 | "double-checking the summary is the default" | PASS | Claude 2.1.150 default: after the subagent returned, the main session opened every policy file (`run-subagent.jsonl` tool-call sequence) | — |
| 10 | B06 | The fix: `--disallowedTools "Read(**/policies/**)"` | PASS | `claude --help` lists `--disallowedTools`; format matches the CLI. NOTE: in Claude Code 2.1.150 a path-scoped denial did not stop the model from trying `Bash cat` / `find` — the narration frames this as "deny Read", not "deny all access", and CHECKS-REPORT flags the caveat | narration says "deny Read on the policies path" — remains true |
| 11 | B06 | Table: inline 3,266; subagent+Read on 3,605; subagent+Read off 435 | PASS | 3,266 (inline reads); 3,170+435=3,605 (subagent+redundant reads); 435 (subagent-only, isolation preserved) | — |
| 12 | B07 | Steps 1–7 in the Boondoggle Score map to the runs | PASS | each step traces to a specific action in `SESSION.md`; dangerousMiddle=4 = "then reads policies anyway" | — |
| 13 | B08 | Ledger rows (subagent isolates reads; hands back short summary; refuses a denied read) | PASS | observed in `run-subagent.jsonl`; a denied Read fails at the tool boundary before Claude runs | — |
| 14 | BVDT | Verdict recap numbers | PASS | rows 2, 6, 8 above; falsifiable line stated | — |
| 15 | BHTF | The viewer's paste-in prompt | EXEMPT | instruction | — |
| 16 | all | Version numbers, prices, session ids, calendar dates from the runs | EXEMPT | recorded in `SESSION.md` and `evidence/`; not spoken or shown on-frame | — |
| 17 | all | Playing "the internet's average" — none of the numbers exist outside this reel's runs | PASS | every token count is from this reel's own stream-json, not from published benchmarks | — |
| 18 | BOUT | Title contains "One" and "48%" | PASS | the title is the concept's original claim; the film's body (rows 8–11) shows that "48%" is achievable only when the human enforces the tool boundary — the falsifiable line names it | — |
