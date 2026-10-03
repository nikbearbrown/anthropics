# CHECKS-REPORT — cc-hook-enforcement

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · 2026-09-10.

## SHOW / HOLD / CARD

| Beat | Surface | Motion | Rationale |
|---|---|---|---|
| B00 | CCPlainShell | type | direct hook demo (out-of-session shell); the mechanism, unassisted |
| BIDEA | BrutalistHesitantWriter | type | the film's claim, typed and corrected ("might" → "must") |
| BDEFS | CCDefinitions | drawon | 5 terms a chat-window audience may not know |
| B01 | CCSession | type | advisory ask — Claude's verbatim refusal |
| B02 | CCSession | default (bang commands) | VERIFY: nothing on disk, no receipt |
| B03 | CCSession | type | hook-only run: Write attempted, is_error BLOCKED |
| B04 | CCSession | type | correction: Claude reads guard.py, rewrites clean |
| B05 | CCSession | default | VERIFY: wc, grep patterns, grep word |
| B06 | CCSession | default | HONEST LIMIT: gradebook / gradual pass the regex |
| BCONDUCT | CCBoondoggleScore | drawon | who did what — dangerous middle is step 4 |
| BHUMAN | CCHumanLedger | drawon | ledger — the redundancy is the design |
| BVDT | ClaudeVerdictArtifact | hold | 4 lines, last is FALSIFIABLE |
| BHTF | ClaudeComposerAsk | type | greeting "Your turn.", prompt read in full |
| BOUT | ClaudeTitleOutro | hold | OUTRO-LOCK: title, @NikBearBrown, subline "" |

## The teaching arc

- **Prediction before reveal.** BIDEA's writer types "sometimes the rule might" and then corrects it to "must" — the correction IS the finding.
- **Falsifiable.** BVDT's last line names the exact evidence that would refute the film: "a hook-active run that lands a matching grade-colon-letter line on disk."
- **Scaffolded practice.** BHUMAN sets up ownership (MUST/SHOULD human · CAN/SHOULD AI); BHTF is that ownership as a runnable prompt in the viewer's own project.

## TERMINAL-FIRST audit

Every non-terminal beat carries `shot.leaves_terminal_because`:
- B00 CCPlainShell: "the hook mechanism is a shell script; running it outside any Claude session proves the contract before we watch a session run it"
- BIDEA BrutalistHesitantWriter: "the idea is not in any session; the writer types the film's argument and corrects the one word the film exists to fix"
- BDEFS CCDefinitions: "definitions for a chat-window audience who may not know the terminal words"

No two consecutive non-terminal beats without a reason.

## BUILD-SHOW

Not armed — this is a **concept film** (`metadata.build` unset). The subject is the mechanism (what a hook IS and what its guarantee is), not a shipped artifact the viewer follows along to build. BFLOW / BSHOW slots not required per SKILL §8. BHTF is the closest thing to a build: the viewer builds their own hook after watching.

## Kit-gotcha budget (author_sheet.py assertion)

`author_sheet.py` prints `warnings: 0`. Verified:
- CCSession text/prompt blocks ≤ 44 chars — 0 over
- CCHumanLedger rows ≤ 30 chars — 0 over
- CCBoondoggleScore step text ≤ 44 chars, system ≤ 28 chars — 0 over
- CCPlainShell lines ≤ 48 chars — 0 over
- CCDefinitions term ≤ 18, meaning ≤ 70 — 0 over
- ClaudeVerdictArtifact `artifactLines` = 4 — legal (must be 4 or 6, never 5)
- `mascot: "off"` on every full-height CCSession — set

## Voice & register

Liam (Kokoro `am_onyx`), Teardown register, first person present tense. Cold open says "This is Liam, in for Bear." (IN-FOR-BEAR LAW). BVDT opens "Let's recap with Claude." BOUT reads exact title then "Liam, in for Bear."

## Nothing datable spoken

No model IDs, no version strings, no prices, no dates. Claude Code 2.1.150 and the run costs are in SESSION.md only.
