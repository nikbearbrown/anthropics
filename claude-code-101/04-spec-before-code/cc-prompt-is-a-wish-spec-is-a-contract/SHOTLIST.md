# SHOTLIST — cc-prompt-is-a-wish-spec-is-a-contract

| ID | Duration | Surface | What's on screen |
|---|---|---|---|
| B00   | 17.3 s | CCSession (wish) | ask types, AskUserQuestion (denied), Read README, Write auth.py, "choices I made without asking" |
| BIDEA | 21.6 s | BrutalistHesitantWriter | four lines type; "prompt" corrects to "wish" |
| BDEFS | 21.7 s | CCDefinitions | five terms land row-by-row |
| B01   | 18.9 s | CCSession (verify) | wc → 40, grep -c def → 3, unittest → 1 fail, the three def lines |
| B02   | 26.1 s | CCPlainShell | wc SPEC.md → 22; five numbered invariants; handoff line |
| B03   | 18.1 s | CCSession (spec run) | ask, Reads SPEC + tests, plan sentence, Write, unittest → OK |
| B04   | 19.0 s | CCSession (verify) | wc → 33, def count → 2, iters → 100k, secrets, ValueError on empty verify |
| B05   | 26.4 s | CCSession (middle) | same ask, denied, Read test_auth.py, "the spec is the tests", OK — with drift |
| B06   | 33.3 s | CCBoondoggleScore | 6 steps, dangerousMiddle=3, tally on the right |
| B07   | 21.8 s | CCHumanLedger | 4 AI rows (CAN/SHOULD), 4 HUMAN rows (MUST/SHOULD), closing |
| BVDT  | 25.7 s | ClaudeVerdictArtifact | 4 verdict lines, last is FALSIFIABLE |
| BHTF  | 17.1 s | ClaudeComposerAsk | greeting "Your turn.", the SPEC-writing prompt |
| BOUT  | 4.4 s  | ClaudeTitleOutro | title restate, @NikBearBrown |

Total narrated: 271.3 s (~4:31). Aspect 16:9, fps 30, Kokoro `am_onyx` (Liam) on every beat.
