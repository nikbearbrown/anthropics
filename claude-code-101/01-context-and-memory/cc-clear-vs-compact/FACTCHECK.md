# FACTCHECK — cc-clear-vs-compact

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (messages 9–11 of one real session) and `evidence/`.

**Verification boundary.** Token figures come from the stream-json usage (`evidence/turns.json`) and the `compact_boundary` event (`evidence/turn9.jsonl`). The `/clear` condition is a fresh `claude -p` session (headless has no `/clear`); `SESSION.md` records that equivalence. Claude's answers are verbatim spans, display-shortened with `…`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | "forty-nine and a half thousand tokens of context" at the end of the last film | PASS | message 8 first-call context 49,530 (`turns.json`) | — |
| 2 | B00 | `/compact` events: status compacting, compact_result success, compact_boundary trigger manual, pre_tokens 49713, post_tokens 6100, duration_ms 57048; "fifty-seven seconds" | PASS | `turn9.jsonl` (keys shown verbatim, in `key: value` form) | — |
| 3 | BIDEA, BDEFS | What `/compact` and `/clear` do | PASS | Claude Code slash commands: `/compact` summarizes the conversation, `/clear` resets it; both listed in the session's `slash_commands`; demonstrated by messages 9–11 | — |
| 4 | B01 | Message 10 verbatim answer (five items); 36,670 read; "down from forty-nine and a half" | PASS | `turn10.jsonl`; `turns.json`; status line set to 36.7k | — |
| 5 | B01 | "The fixed part … is about thirty thousand" | PASS | `/context` on the same session: system prompt 9k + tools 8.9k + deferred 19.2k + skills 4.2k + agents/memory ≈ 41.5k as the product counts it; the first-call context of a fresh session measured 28,676. "About thirty thousand" refers to the measured fresh-session first call (28,676) | — |
| 6 | B01 | "The conversation itself went from forty-nine thousand to six" | PASS | compact_boundary pre_tokens 49,713 → post_tokens 6,100 | — |
| 7 | B02 | Fresh session: 28,676 read; `git diff` twice; the answer verbatim (display-shortened); "tests included" | PASS | `turn11-fresh.jsonl`; status line set to 28.7k | — |
| 8 | B02 | "which the summary-based answer had left out" | PASS | message 10's answer has five items and no tests line; message 11's has six, the last being the tests | — |
| 9 | B03 | The three receipts; `Ran 6 tests … OK`; `2 files changed, 174 insertions(+), 13 deletions(-)` | PASS | `SESSION.md` VERIFY | — |
| 10 | B04 | Six steps; tally PF 1 · PA 1 · IJ 1 · TO 1 · EI 0 | PASS | maps to SESSION.md | — |
| 11 | B05 | "It should say when it's answering from a summary — it didn't" | PASS | message 10's answer contains no mention of a summary or compaction | — |
| 12 | BVDT | Verdict lines | PASS | rows 2, 4, 7, 9 | — |
| 13 | BHTF | The viewer's prompt; "/context … the Messages row" | PASS | `/context` output has a Messages row (`../cc-context-check/evidence/context-output.md`) | — |
| 14 | all | Model id | EXEMPT | not shown or spoken | — |
| 15 | metadata | Costs | EXEMPT | in SESSION.md | — |
