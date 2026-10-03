# SHOTLIST — cc-agentic-harness

16:9 · 3840×2160 · Liam (Kokoro `am_onyx`) on every beat · measured audio is the clock.

| Beat | Act | Surface | What moves | Source |
|---|---|---|---|---|
| B00 | COLD OPEN — harness off | `CCSession` (title `claude -p --tools ""`) | the ask types; "Creating the file now."; `!ls` → README.md | SESSION Run A2 |
| BIDEA | THE IDEA | `BrutalistHesitantWriter`, CC palette (`leaves_terminal_because` set) | the idea of the film types; one word reconsidered and replaced | — |
| BDEFS | DEFINITIONS | `CCDefinitions` (`leaves_terminal_because` set) | five terms land one at a time, meaning after term | — |
| B01 | THE MANIFEST | `CCSession` (title `claude -p --output-format stream-json`, mascot off) | eight init-event lines land one by one | SESSION Run B init |
| B02 | HARNESS ON | `CCSession` (accept-edits, mascot off) | the ask; ✳ Writing; Write hello.txt; Claude's line; `!cat hello.txt` → hello | SESSION Run B |
| B03 | HALF OFF | `CCSession` (title `claude -p --tools ""  (connectors on)`, mascot off) | the Drive call; the permission refusal; Write → no such tool; Claude's explanation | SESSION Run A |
| B04 | THE LOOP | `CCPlainShell` (plain dark shell; `leaves_terminal_because` set) | tasks.md, LOOP.md, the for loop stagger in | SESSION Run C |
| B05 | ITERATION ONE | `CCSession` (accept-edits, mascot off) | the loop prompt; Read · Write · Edit; a two-line diff; "Did task: write a.md…" | SESSION loop1 |
| B06 | VERIFY | `CCSession` (default, mascot off) | four bang commands and their outputs; the last is `6` | SESSION VERIFY after the loop |
| B07 | THE MAP | `CCHarnessMap` (`leaves_terminal_because` set) | core, then PROMPT → CONTEXT → HARNESS → YOUR LOOP rings with their items; caption | SESSION (all) |
| B09 | CONDUCT | `CCBoondoggleScore` | six steps; step 3 ringed; IJ 0 · EI 0 red | SESSION (all) |
| B10 | HUMAN | `CCHumanLedger` | AI column, then HUMAN column; closing | SESSION (all) |
| BVDT | VERDICT | `ClaudeVerdictArtifact` | six lines | — |
| BHTF | YOUR TURN | `ClaudeComposerAsk` | the prompt types | — |
| BOUT | OUTRO | `ClaudeTitleOutro` | OUTRO-LOCK | — |

Non-terminal body beats: B04 (shell loop — no session contains it) and B07 (the diagram). Not consecutive.
