# SHOTLIST — cc-writer-reviewer-pattern

| Beat | Surface | Beats' role | Source |
|---|---|---|---|
| B00 | `CCSession` (accept-edits) | Writer run: ask, Read grades.csv, Write pass_fail.py, python3 → 5 lines | `run-writer.jsonl` |
| BIDEA | `BrutalistHesitantWriter` (CC palette) | The idea: same-session review is narration; correction word "reviewer" → "writer" | — |
| BDEFS | `CCDefinitions` | 4 terms: same-context, clean-context, session, --resume | — |
| B01 | `CCSession` (default, resumed) | Same-session review: 4 headers, six 'I' openings | `run-review-same.jsonl` |
| B02 | `CCPlainShell` | Setup: cp four files, new uuid, `claude -p --session-id` | shell commands used to launch run 3 |
| B03 | `CCSession` (accept-edits, new) | Clean review: ls + Reads + "Real bugs" numbered + line cites | `run-review-clean.jsonl` |
| B04 | `CCPlainShell` | grep receipts: 'I' counts (6 vs 0), line cites (3 vs 0), 59.3 re-derived | derived from the two transcripts |
| B05 | `CCBoondoggleScore` | 7 steps; step 3 = dangerous middle (same-session review); PF/PA/TO/IJ/EI tally | `SESSION.md` |
| B06 | `CCHumanLedger` | MUST/SHOULD × human / CAN/SHOULD × AI | `SESSION.md` |
| BVDT | `ClaudeVerdictArtifact` | 4 lines — last is FALSIFIABLE: a resumed session leading with a line-cite | — |
| BHTF | `ClaudeComposerAsk` | Your turn — two terminals, same prompt, side by side | — |
| BOUT | `ClaudeTitleOutro` | @NikBearBrown, exact title restate, "Liam, in for Bear." | — |
