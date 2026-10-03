# FACTCHECK — cc-agentic-loop-not-chatgpt

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (two real headless runs) and `evidence/`.

**Verification boundary.** Every number, tool name, path, diff line and quoted span shown on screen comes from the two runs' stream-json (`evidence/run-naive.jsonl`, `evidence/run-calibrate.jsonl`), the naive-run outputs on disk (`evidence/index.naive.html`, `evidence/style.naive.css`, `evidence/diff.naive.patch`), and Liam's plain-shell checks against `class-website/`. Claude's sentences are verbatim spans, display-elided at ellipsis. The source concept's framing (turn-based vs. agentic; five-question calibration) is kept.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | The naive ask, verbatim | PASS | `evidence/ask.txt` and `run-naive.jsonl` (user message) | — |
| 2 | B00, B01 | Bash `ls`, three Reads (`index.html`, `style.css`, `README.md`) | PASS | `run-naive.jsonl` tool_use events | — |
| 3 | B00, B02 | Two Edits (`index.html`, `style.css`) after the caveats-first text | PASS | `run-naive.jsonl` tool_use events | — |
| 4 | B01, B02 | "Static site, no backend." / "'Reach me' routes to the front office." | PASS | Claude's pre-edit assistant text, split at clauses | — |
| 5 | B02 | "I'll add a simple, safe version" / mailto / placeholder / scrapeable | PASS | Claude's assistant text — verbatim spans, split ≤44 char at clause | — |
| 6 | B02 | The AskUserQuestion prompt was dismissed and the loop kept going | PASS | `run-naive.jsonl`: tool_use `AskUserQuestion` at message 9, then tool_result "Answer questions?" (dismissed by \< /dev/null), then the assistant pivots to "I'll add a simple, safe version" and Edits | — |
| 7 | B03 | `git status --short` → ` M index.html` / ` M style.css` | PASS | `evidence/diff.naive.patch` and the recorded VERIFY commands in `SESSION.md` | — |
| 8 | B03 | `git diff --stat` → `index.html \| 16 ++++++++++++++++`, `style.css \| 4 ++++` | PASS | `git diff --stat HEAD` after the naive run | — |
| 9 | B03 | Two `<input>` lines (name text, email) | PASS | `grep -o '<input[^>]*>' evidence/index.naive.html`; ends elided | — |
| 10 | B03 | `action="mailto:REPLACE-WITH-…"` | PASS | `evidence/index.naive.html` line 20; display-elided | — |
| 11 | B04 | The calibrate ask, verbatim on screen (display-shortened; full text in `evidence/ask-calibration.txt`) | PASS | on-screen prompt "Answer 5 questions before any change." is the shortened form; the five list items are the on-screen text blocks | — |
| 12 | B04 | Same Bash `ls`, three Reads on the calibrate run | PASS | `run-calibrate.jsonl` tool_use events | — |
| 13 | B04 | No Edit/Write tool called | PASS | `run-calibrate.jsonl` contains no `Write`/`Edit` tool_use; `--allowedTools` fenced them out | — |
| 14 | B05 | "a contact form is a bigger change than it looks" | PASS | Claude answer to Q3, verbatim | — |
| 15 | B05 | "'Reach me' is already a contact method." / "A form needs a backend." | PASS | Q3 answer, verbatim spans, split at clauses | — |
| 16 | B05 | Q4 "voice, footer, one-file structure — don't touch" | PASS | Q4 answer bullets summarised: "voice, scope, and content"; "footer warning"; "single-file, no-framework structure" | — |
| 17 | B05 | "(555) 010-1234 — reserved" / "Might be a teaching example." | PASS | Q5 answer verbatim: "reserved fictional prefix, which makes me think this may be a teaching example" | — |
| 18 | B06 | `git status --short` → clean; `git diff --stat` → nothing; `ls` → three files; `git log --oneline` → one seed commit | PASS | `SESSION.md` VERIFY block after the calibrate run | — |
| 19 | B07 | Six-step CONDUCT board; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | maps to `SESSION.md`; dangerousMiddle = step 2 (loop wrote to disk before caveats) | — |
| 20 | B08 | Ledger rows (`refuse when tools are fenced` → run-calibrate; `report tradeoffs after acting` → naive summary) | PASS | `SESSION.md`; `run-calibrate` used `--allowedTools` without Write/Edit | — |
| 21 | BVDT | 2 edits vs 0 edits; email input; mailto placeholder; "reserved fictional prefix" | PASS | rows above | — |
| 22 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 23 | all | Model/version strings; costs; wall-clock in ms | EXEMPT | not shown or spoken; recorded in `SESSION.md` only | — |
