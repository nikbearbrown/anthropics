# CHECKS-REPORT — cc-engineering-partner-loop

Pre-compile check, cc-explainer, 2026-09-09.

## Spine (16:9 · build film)

| Beat | Lane | Pattern | Notes |
|---|---|---|---|
| B00 | COLD OPEN | CCSession | bare-loop quick tour: ask → Reads → Edit → tests OK |
| BIDEA | IDEA | BrutalistHesitantWriter | "generator" reconsidered → "partner" |
| BDEFS | CARD | CCDefinitions | 5 terms: oracle, plan, minimal diff, scope, partner loop |
| B01 | TERMINAL | CCSession | Liam's plain-shell verify on the bare fix |
| B02 | TERMINAL | CCSession | partner ASK; Edit withheld → status:Planning |
| B03 | TERMINAL | CCSession | PLAN block + DIFF block (Claude's plan, in text, before edit) |
| B04 | TERMINAL | CCSession | approve → Edit → unittest OK |
| B05 | SHELL | CCPlainShell | Liam's grep catches docstring/code drift |
| B06 | TERMINAL | CCSession | re-prompt: docstring-only Edit, oracle stays OK |
| BFLOW | FLOW | FlowDiagram (claude skin) | 5-node partner loop: ORACLE → ASK → PLAN → DIFF → VERIFY |
| BSHOW | SHELL | CCPlainShell | the actual `unittest -v` output from `evidence/verify.txt` |
| BCND | TERMINAL | CCBoondoggleScore | 6 steps, dangerousMiddle=3 |
| BHMN | TERMINAL | CCHumanLedger | 4 human rows / 4 AI rows |
| BVDT | BOOKEND | ClaudeVerdictArtifact | 4 lines, last is FALSIFIABLE |
| BHTF | BOOKEND | ClaudeComposerAsk | greeting "Your turn."; topic "YOUR TURN · CLAUDE CODE 101" |
| BOUT | BOOKEND | ClaudeTitleOutro | handle "@NikBearBrown"; subline "" |

## Teaching arc

- **Falsifiability beat.** BVDT's line 4: *a bare run that shows the plan before the edit, unasked*. Named counter-observation that would defeat the film's argument.
- **Scaffolded task → YOUR TURN.** HUMAN ledger tells viewers exactly what they cannot delegate (naming the oracle, approving the plan, reading the diff, catching drift). BHTF then hands over a working prompt that FORCES the plan gate.

## BUILD-SHOW arming

`metadata.build: true` — the ask is build-shaped ("run the loop on a failing test"). BFLOW draws the five gates as a diagram (the terminal implies them but does not draw them); BSHOW holds a real `unittest -v` output long enough to read (`evidence/verify.txt`, ≥ 6 s hold). Both slots sit immediately before CONDUCT.

## SHOW / HOLD / CARD

- SHOW: B00 (bare edit landing), B03 (plan + diff), B04 (Edit + OK), B06 (docstring-only edit), BSHOW (unittest).
- HOLD: BDEFS (definitions land 1×; then hold), BVDT (verdict), BOUT.
- CARD: BIDEA (writer types the idea), BDEFS, BFLOW.

## Non-terminal beats + their reasons (TERMINAL-FIRST LAW)

| Beat | Non-terminal because |
|---|---|
| BIDEA | idea of the film exists in no session; writer types it and corrects the film's one word |
| BDEFS | jargon defined for a chat-window audience |
| B05 | Liam's plain-shell audit; drift is what the session cannot see about itself |
| BFLOW | BUILD-SHOW: the five gates are implied but never drawn |
| BSHOW | BUILD-SHOW: real oracle output, held long enough to read |
| BCND | CONDUCT: score drawn from the session; terminal doesn't draw it itself |
| BHMN | HUMAN: ledger drawn from the session; terminal doesn't draw it itself |

No two consecutive non-terminal beats without reasons. B05 (SHELL) sits between two terminal beats (B04, B06). BFLOW+BSHOW+BCND+BHMN are the fourfold closing stack every cc-explainer runs.

## Kit gotchas checked

- CCSession text blocks all ≤ 44 chars (author_sheet.py asserts, 0 warnings).
- Prompt blocks ≤ ~140 chars.
- CCPlainShell lines ≤ 48 chars.
- CCHumanLedger rows ≤ 34 chars.
- CCBoondoggleScore system ≤ 28 chars, steps ≤ 46 chars.
- CCDefinitions: 5 terms ≤ 18 chars each; meanings ≤ 78 chars.
- ClaudeVerdictArtifact: exactly 4 lines (not 5).
- mascot: `off` on every CCSession beat (full stacks; PIXEL-ART LAW).
- Status blocks use `tokens: "1.4k tokens"` (no leading `↓`).
- Product strings verbatim: `Planning`, `accept-edits`, `default`, `Edit`, `Read`, `Bash`.

## What the runs cost

Total 4 headless `claude -p` runs = ~$0.87. Recorded per-run in SESSION.md. Kokoro only for narration. No paid generation.
