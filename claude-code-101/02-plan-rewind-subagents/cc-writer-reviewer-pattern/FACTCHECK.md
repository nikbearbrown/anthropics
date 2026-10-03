# FACTCHECK — cc-writer-reviewer-pattern

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (three real headless runs) and `evidence/`.

**Verification boundary.** Every number and phrase on screen comes from the three runs' stream-json (`evidence/run-writer.jsonl`, `run-review-same.jsonl`, `run-review-clean.jsonl`), the code and CSV in `evidence/`, and grep-verifiable counts on the two review transcripts. Claude's sentences that appear on screen are trimmed to fit the CCSession text-block budget (≤ ~44 chars); wording is preserved. Nothing datable (version numbers, model names, prices) is shown or spoken.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Reads grades.csv; Writes pass_fail.py; runs it; five lines: Ada PASS / Ben FAIL / Cai PASS / Dee FAIL / Eli PASS | PASS | `run-writer.jsonl` (initial `ls` omitted for height); `python3 pass_fail.py` output verbatim | — |
| 3 | B00 | "eleven lines of Python" | PASS | `wc -l evidence/pass_fail.py` → 11 | — |
| 4 | B00 | "five students", "three passes, two fails" | PASS | derived from output | — |
| 5 | B00, BIDEA, BDEFS | Same-context / clean-context / session / --resume framing | PASS | Claude Code product concepts; the `--resume` and `--session-id` flags are the real flags used in the runs | — |
| 6 | B01 | The review prompt, verbatim | PASS | `run-review-same.jsonl` user turn | — |
| 7 | B01 | "four section headers" naming Spec ambiguity / Missing data / Fragility / What I'd change first | PASS | `run-review-same.jsonl` — the four bold headers in Claude's reply, verbatim | — |
| 8 | B01 | "I picked. I never asked. I average only the two present. I papered over." | PASS | `run-review-same.jsonl` — these exact phrases appear in the reply | — |
| 9 | B02 | Copy the four files to /tmp/clean-review; new uuid `72948a3b-…`; new `claude -p --session-id` | PASS | the shell commands actually run to set up run 3; the uuid is in `evidence/run-review-clean.jsonl`'s session field | — |
| 10 | B03 | Same prompt; ls + Reads of pass_fail.py, grades.csv, ask.txt; response leads with "Real bugs"; three numbered findings; line cites `pass_fail.py:10`, `:9`, `:7`; "Cai … 89 … flips to 59.3" | PASS | `run-review-clean.jsonl` — tool_uses and text verbatim; the 59.3 arithmetic is the reviewer's own re-derivation from `grades.csv` | — |
| 11 | B04 | grep counts: `^I ` same=6, clean=0; `pass_fail.py:` three cites; `59.3` present | PASS | grep the review-text spans in the two jsonl files. Cited lines: `pass_fail.py:10` (Dee), `pass_fail.py:9` (missing semantics), `pass_fail.py:7` (whitespace name). 59.3 appears once in clean review; not in same review. | — |
| 12 | B05 | Seven-step Boondoggle Score; step 3 is the "dangerous middle" (the same-context review); tally shown | PASS | maps to `SESSION.md`; dangerous-middle framing follows `reference/three-beats.md` doctrine | — |
| 13 | B06 | Ledger rows all trace to the session behavior: Claude reviewed a file it had never seen (run 3, cold Reads); cited lines; re-derived arithmetic (59.3); "should read only the files, not the past" is the operating principle of run 3 vs run 2 | PASS | `run-review-clean.jsonl` (cold Reads then response) vs `run-review-same.jsonl` (zero Reads, one text turn) | — |
| 14 | BVDT | The four artifact lines summarize B01/B03/B04 counts | PASS | rows 7–11 above | — |
| 15 | BHTF | Viewer's prompt | EXEMPT | instruction; itself testable by the viewer with the same two flags | — |
| 16 | all | Model / Claude Code version / prices | EXEMPT | not shown or spoken; recorded in SESSION.md metadata only | — |
| 17 | B04 | The command syntax on `CCPlainShell` — `grep -c "^I "`, `grep -o "pass_fail.py:[0-9]*"` | PASS | these are the actual shell forms used to derive the counts | — |
| 18 | metadata | Session ids `4837f38e-…` (writer) and `72948a3b-…` (clean) | PASS | `run-writer.jsonl` / `run-review-clean.jsonl` `session_id` field | — |
