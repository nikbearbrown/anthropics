# FACTCHECK — cc-context-cost

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (one real eight-message headless session) and `evidence/turns.json` / `turn*.jsonl`.

**Verification boundary.** Every token figure is read from the stream-json `usage` of the run (`evidence/turns.json`, derived by the script described in `SESSION.md`). "Context read" = `input + cache_read + cache_creation` for a call. Status-line token figures on screen are set to the measured first-call context of that message. The source concept's slogan ("message 30 costs 31 times more") is measured, not repeated; the measured multiplier is reported.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, BIDEA | "There's a line going around: message thirty costs thirty-one times more" | PASS | the source concept reel's title and its B02 claim; stated as the claim under test | — |
| 2 | B00 | Message 1 verbatim; "A tiny CLI gradebook that persists students and their scores to a `grades.json` file …"; 28.4k tokens read | PASS | `turn1.jsonl`: first-call context 28,450; status line set to it | — |
| 3 | B00 | "before I'd said anything real — the system prompt, the tool list, CLAUDE.md" | PASS | `/context` on the same session (`cc-context-check/evidence/context-output.md`): system prompt 9k, tools 8.9k + 19.2k deferred, skills 4.2k, CLAUDE.md 465 | — |
| 4 | BIDEA, B03 | "Message eight read 49,530 tokens" / "one hundred and eighty-three tokens out" | PASS | `turn8.jsonl`: first-call context 49,530; output 183 | — |
| 5 | B01 | Messages 2–7: rename, top N, export, refactor question, refactor, stats; "three tests, four, five, six"; the quoted "All N tests pass" lines | PASS | `ask2–7.txt`; Claude's answers in `SESSION.md`; the screen collapses six messages into one shell: message 2's loop, then the five test-count lines (message 5 had no tests; its line is omitted) | — |
| 6 | B01 | Status figures | EXEMPT | none on this beat | — |
| 7 | B02 | First-call context per message: 28,450 · 29,283 · 32,237 · 34,576 · 38,311 · 38,964 · 47,283 · 49,530 | PASS | `turns.json` | — |
| 8 | B02 | "it wrote seven thousand tokens of code that turn" (message 6) | PASS | `turn6.jsonl` output_tokens 7,897 | — |
| 9 | B02, B04 | "It never went down" / "nothing shrinks it unless you do" | PASS | the eight first-call values are monotonic; `/compact` (message 9, next film) is what shrank it | — |
| 10 | B03 | Message 8 verbatim; the five answer lines (display-shortened with `…`) | PASS | `ask8.txt`; `turn8.jsonl` | — |
| 11 | B04 | 49,530 / 28,450 = 1.74×; $0.224 / $0.113 = 1.98×; message 8 call: cache_read 15,744, cache_creation 33,780, input 6, output 183 | PASS | `turns.json`; `turn8.jsonl` result usage | — |
| 12 | B04, BDEFS | "most of a growing session is cache … re-reads cheaply" | PASS | prompt caching: cache reads are billed at a fraction of fresh input (Anthropic pricing); on message 8, 15,744 of 49,530 were cache reads and 33,780 were newly cached | — |
| 13 | BDEFS | "roughly three-quarters of a word" per token | PASS | the common English estimate (~0.75 words/token); high-level definition | — |
| 14 | B05 | Six steps; tally PF 1 · PA 1 · IJ 1 · TO 1 · EI 0 | PASS | maps to SESSION.md | — |
| 15 | B06 | Ledger rows | PASS | "say what it built — it did" → message 8; "re-read only what it needs — no" → the mechanism (row 7) | — |
| 16 | BVDT | Verdict lines | PASS | rows 4, 7, 11 | — |
| 17 | BHTF | The viewer's prompt; "type slash context and read the Messages row" | PASS | `/context` prints a Messages row (`cc-context-check/evidence/context-output.md`) | — |
| 18 | all | Model id (`claude-opus-4-7`) in the receipts | EXEMPT | never shown or spoken | — |
| 19 | metadata | Costs per message | EXEMPT | in SESSION.md; only the message-8 / message-1 ratio is spoken | — |
