# CHECKS-REPORT — cc-writer-reviewer-pattern

Pre-compile audit before the first `./art run`.

## Spine (cc-explainer, 16:9, concept film — no `metadata.build`)

- B00 cold open → **BIDEA** the idea → **BDEFS** definitions → loop (B01 same-context review · B02 clean-context setup · B03 clean-context review) → correction is the same loop's cycle-2 axis (B02–B03) → verify (B04) → **CONDUCT** (B05) → **HUMAN** (B06) → **BVDT** → **BHTF** → **BOUT**.
- **BUILD-SHOW: not armed — concept film.** The subject is the *technique* (two reviewers, same code, different context), not building an artifact. `metadata.build` is unset; BFLOW/BSHOW are skipped by design.

## TERMINAL-FIRST audit

| Beat | Surface | Leaves terminal? | Named reason |
|---|---|---|---|
| B00 | `CCSession` | no | — |
| BIDEA | `BrutalistHesitantWriter` | yes | "the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix" |
| BDEFS | `CCDefinitions` | yes | "definitions for a chat-window audience" |
| B01 | `CCSession` | no | — |
| B02 | `CCPlainShell` | yes | "the setup is a plain shell before any session; no claude session is running yet" — this is the correction axis: leaving the writer's session is the fix, so the fix's surface cannot be `CCSession` |
| B03 | `CCSession` | no | — |
| B04 | `CCPlainShell` | yes | "the receipts live in a plain shell; the two review transcripts are grepped against each other" |
| B05 | `CCBoondoggleScore` | closing block | — (governed by the CONDUCT contract, not TERMINAL-FIRST) |
| B06 | `CCHumanLedger` | closing block | — (governed by the HUMAN contract) |
| BVDT/BHTF/BOUT | bookends | your-turn standard | — |

No two consecutive body beats leave the terminal without a named reason.

## LAWS — pass/fail

- **REAL-SESSION**: PASS — every `CCSession` block traces to `SESSION.md`.
- **TYPES-NOT-NARRATES**: PASS — the two `prompt` blocks (B00, B01, B03) are what Liam typed (the ask and the review prompt), never his narration.
- **VERBATIM PRODUCT STRINGS**: PASS — mode strings `accept-edits` and `default` from the kit's tokens; no restyle.
- **VERIFY IS A COMMAND**: PASS — B00 ends on `python3 pass_fail.py` (Liam's), B04 is a plain-shell grep audit (Liam's), not a `✓` from Claude.
- **IDEA, DEFINITIONS, THEN THE LOOP**: PASS — BIDEA at beat 2, BDEFS at beat 3, loop from B01.
- **CONDUCT AND HUMAN BEFORE THE RECAP**: PASS — B05 CONDUCT, B06 HUMAN, then BVDT/BHTF/BOUT.
- **OUTRO-LOCK**: PASS — `ClaudeTitleOutro`, `handle:"@NikBearBrown"`, `subline:""`, exact title restate, "Liam, in for Bear."
- **NO EXTERNAL NAMES**: PASS — narration and props reference Liam and Bear only. Student names (Ada, Ben, Cai, Dee, Eli) are synthetic CSV rows.

## Kit-gotcha audit (from SKILL.md's list)

- CCSession text-block ≤ 44 chars: PASS (author_sheet.py asserts).
- CCHumanLedger row ≤ 34 chars: PASS (asserted; the one 37-char row was rewritten).
- CCBoondoggleScore step ≤ 46 chars: PASS (asserted).
- CCPlainShell line ≤ 50 chars: PASS (asserted).
- ClaudeVerdictArtifact has 4 lines, not 5: PASS.
- Full-height CCSession beats set `mascot: "off"`: PASS (B00, B01, B03).
- Status blocks never write `"↓ 1.2k tokens"`: PASS — no `status`-type blocks with `tokens` used in this reel.

## Teaching arc

- The **falsifiability beat** is BVDT's last line: "a resumed session that leads with a numbered bug and never says 'I picked'."
- The **scaffolded task** for YOUR TURN is B06 (HUMAN) → BHTF: run two terminals with the same prompt, one resumed and one fresh, and score them by "I" openings vs line cites.
- The **prediction before reveal** is B01→B03: Liam names what he expects to see in each transcript (a narration vs a review) before B04 counts it.

## Duration estimate

12 beats, est 310s (5:10). Actual will land inside 4–8 min band per SKILL.md.
