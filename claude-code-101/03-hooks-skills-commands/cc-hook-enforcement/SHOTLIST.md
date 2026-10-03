# SHOTLIST — cc-hook-enforcement

| # | Beat | Surface | Frame headline |
|---|---|---|---|
| 1 | B00 | CCPlainShell | `guard.py` = 42 lines, bad.json → exit 2 with BLOCKED, ok.json → exit 0 |
| 2 | BIDEA | BrutalistHesitantWriter | four lines, mid-sentence correction "might" → "must" |
| 3 | BDEFS | CCDefinitions | five terms land one at a time |
| 4 | B01 | CCSession (advisory) | ask block × 2 + Claude's four-line verbatim refusal |
| 5 | B02 | CCSession (default) | `ls` → 5 files + `grep -c tool_use run-advisory.jsonl` → 0 |
| 6 | B03 | CCSession (accept-edits) | ask, Bash ls, Read csv, Write error, BLOCKED message (4 spans) |
| 7 | B04 | CCSession (accept-edits) | Claude explains block, Reads README + guard.py, second Write OK |
| 8 | B05 | CCSession (default) | `wc` → 13, pattern grep → 0, word grep → 3 |
| 9 | B06 | CCSession (default) | direct regex tests: gradebook → False, gradual → False, "Suggested grade: B+" → True |
| 10 | BCONDUCT | CCBoondoggleScore | 6 steps, dangerous middle ring on step 4, capacity tally |
| 11 | BHUMAN | CCHumanLedger | AI column lands first (CAN/CAN/SHOULD/SHOULD), then human MUST/MUST/MUST/SHOULD |
| 12 | BVDT | ClaudeVerdictArtifact | 4 lines, last line FALSIFIABLE |
| 13 | BHTF | ClaudeComposerAsk | greeting "Your turn.", prompt read in full |
| 14 | BOUT | ClaudeTitleOutro | title, @NikBearBrown, mascot |
