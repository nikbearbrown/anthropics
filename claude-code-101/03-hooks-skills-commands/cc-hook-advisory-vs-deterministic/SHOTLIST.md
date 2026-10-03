# SHOTLIST — cc-hook-advisory-vs-deterministic

| Beat | Surface | Narration seconds | Content |
|---|---|---|---|
| B00 | CCSession | 18.5 | Cold open — advisory run: prompt, two Reads, Write, Claude's note |
| BIDEA | BrutalistHesitantWriter | 17.6 | "Advice is enough" → "not enough" |
| BDEFS | CCDefinitions | 22.1 | advisory · deterministic · PreToolUse hook · exit 2 |
| B01 | CCSession | 11.7 | Verify advisory: wc → 14, grep → 0, tail note |
| B02 | CCSession | 14.5 | Pressured ask, Claude verbatim refusal |
| B03 | CCSession | 15.7 | Reframed ask, Claude verbatim refusal |
| B04 | CCPlainShell | 22.4 | The hook run directly — bad.json → 2, ok.json → 0 |
| B05 | CCSession | 18.4 | Hook-only run — Read, Write attempt, BLOCKED tool_result |
| B06 | CCSession | 18.5 | Claude reads stash, second Write succeeds |
| B07 | CCSession | 13.2 | Verify hook-only: wc → 13, grep → 0, gradebook → 1 |
| BCONDUCT | CCBoondoggleScore | 28.3 | Six steps, dangerous middle = 5 |
| BHUMAN | CCHumanLedger | 26.6 | MUST/SHOULD ledger, closing line |
| BVDT | ClaudeVerdictArtifact | 26.6 | Four verdict lines with falsifiable |
| BHTF | ClaudeComposerAsk | 18.5 | Your turn — build your own hook |
| BOUT | ClaudeTitleOutro | 4.4 | Title restate |

Total narration: ~276.8 s (4:37). Runtime after slate holds ~5:00–5:30 expected.
