# CHECKS-REPORT — cc-claude-101

Pre-compile checks; the file is authored before the first `art run`.

## Spine (SHOW / HOLD / CARD)

| Beat | Lane | Surface | Role | Notes |
|---|---|---|---|---|
| B00 | TERMINAL | CCSession | SHOW — the concrete run works | ≤44-char text blocks; mascot off; the ask sets the pattern |
| BIDEA | IDEA | BrutalistHesitantWriter | HOLD — the thesis, one word reconsidered | CC palette; "menu" → "function"; leaves_terminal_because named |
| BDEFS | CARD | CCDefinitions | CARD — five terms | for the chat-window audience; each term is used later; leaves_terminal_because named |
| B01 | TERMINAL | CCSession | SHOW — the concrete run passes verification | Liam's bang commands inside the session |
| B02 | TERMINAL | CCSession | SHOW — vague ask, no ground → routed back | no artifact; the model refuses to guess |
| B03 | TERMINAL | CCSession | SHOW — vague ask WITH file → opinion | the dangerous middle; sounds grounded |
| B04 | TERMINAL | CCSession | SHOW — the correction | rewrite the ask into something testable |
| B05 | TERMINAL | CCSession | SHOW — the correction verifies | wc + grep + cat |
| B06 | TERMINAL | CCBoondoggleScore | HOLD — who did what, dangerous middle ringed | eight steps, five capacities named |
| B07 | TERMINAL | CCHumanLedger | HOLD — MUST/SHOULD × human/AI | four rows each; closing line |
| BVDT | BOOKEND | ClaudeVerdictArtifact | HOLD — recap in Liam's voice | 6 artifact lines (paginates 3+3); FALSIFIABLE last |
| BHTF | BOOKEND | ClaudeComposerAsk | HOLD — your turn | "Your turn." greeting; prompt read aloud in full |
| BOUT | BOOKEND | ClaudeTitleOutro | HOLD — exact title | subline empty; handle @NikBearBrown |

**Non-terminal beats:** BIDEA, BDEFS (both carry `leaves_terminal_because`). None consecutive. TERMINAL-FIRST holds.

## Teaching arc

- **Cold open (B00)** — the concrete run: a testable answer, right away. Sets the pattern before the theory.
- **THE IDEA (BIDEA)** — what the film exists to fix: the "many"-menu view of Claude, replaced by "one function."
- **DEFINITIONS (BDEFS)** — the five words the rest of the film uses (ask, ground, function, right answer, headless).
- **CONCRETE VERIFY (B01)** — pay off B00's promise with Liam's shell.
- **VAGUE, NO FILE (B02)** — the honest empty case: the model refuses to guess. There is no artifact, and that is not a failure.
- **VAGUE, WITH FILE (B03)** — the dangerous middle. The file makes the opinion sound grounded. Nothing on shell to check.
- **THE CORRECTION (B04)** — the fix is the ask, not the prompt style.
- **CORRECTION VERIFY (B05)** — three checkable lines.
- **CONDUCT (B06)** — the dangerous-middle beat is explicitly ringed (step 4).
- **HUMAN (B07)** — MUST rows are the four things a chat-window user cannot delegate: define right answer, audit an opinion, sharpen vague into testable, write the check first.
- **VERDICT (BVDT)** — five recap lines + one FALSIFIABLE line; the reel's own falsification test.
- **YOUR TURN (BHTF)** — the exercise IS "write the check before the ask," turning HUMAN's SHOULD row into a task.
- **OUTRO (BOUT)** — the title, restated. Liam, in for Bear.

## Gates cleared here (pre-compile)

- LIAM LAW: `metadata.operator = Liam / am_onyx / kokoro`; cold open says "This is Liam, in for Bear."; BOUT says "Liam, in for Bear." Recap handoff line "Let's recap with Claude."
- TERMINAL-FIRST: 9 of 13 beats are terminal; the four non-terminal beats (BIDEA, BDEFS, and the two bookends) each carry a reason (or are bookends).
- REAL-SESSION: every `CCSession` block traces to `SESSION.md`.
- TYPES-NOT-NARRATES: every prompt block is what was typed (or a display-condensed form of it, documented in FACTCHECK), never the narration.
- VERIFY IS A COMMAND: B01 and B05 are Liam's commands. Claude's ✓ in B00 and B04 is followed by Liam's `wc`/`grep`/`cat`.
- VERBATIM PRODUCT STRINGS: modes `accept-edits` and `default` verbatim; status tokens omitted (no `↓` risk).
- OUTRO-LOCK: `ClaudeTitleOutro` with `handle: "@NikBearBrown"` and `subline: ""`.
- BVDT lines: 6 (paginates 3+3, not the forbidden 5).
- CCSession text blocks: all ≤44 chars (author_sheet.py asserts on save).
- CCBoondoggleScore step text: all ≤46 chars.
- CCHumanLedger rows: all ≤34 chars.
- Mascot: `off` on every full CCSession beat (avoids the last-row overprint).
- FACTCHECK: `clean` (23 rows, 12 beats covered, 1 claim-bearing).

## What Bear decides after the first cut

Nothing autonomous past `art run`. Bear reviews the review cut; the human decides `art final` and whether to `post` / publish.
