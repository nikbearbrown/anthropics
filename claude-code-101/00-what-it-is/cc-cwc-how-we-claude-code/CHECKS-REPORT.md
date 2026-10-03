# CHECKS-REPORT — cc-cwc-how-we-claude-code

**Reel:** How Anthropic Uses Claude Code — a cc-explainer of the Anthropic CWC internal workflow (Brainstorm → Design → Verify) applied one phase at a time to a single small task. Liam, in for Bear. 15 beats, ~6:03 estimated.

## SHOW / HOLD / CARD per beat

| Beat | Role | Surface | Reason |
|---|---|---|---|
| B00 | cold open | `CCSession` (accept-edits) | the terminal IS the subject; TERMINAL-FIRST |
| BIDEA | the idea | `BrutalistHesitantWriter` | the film's claim is not in any session — writer types it, one word corrected (`better` → `different`) |
| BDEFS | definitions | `CCDefinitions` | 4 jargon terms (`brainstorm`, `design`, `verify`, `definition of done`) for chat-window viewers |
| B01 | bare — verify | `CCSession` (default) | Liam's bang-commands against the bare page in a Claude Code shell |
| B02 | brief — Phase 1 | `CCPlainShell` | brief.md is inspected in a normal shell before any session; no session shows it |
| B03 | design — Phase 2 | `CCSession` (accept-edits) | the diverge ask + 4 Writes lands cleanly in-terminal |
| B04 | the four mocks | `CCPlainShell` | four files inspected side-by-side; no single session shows this |
| B05 | pick + fixture | `CCPlainShell` | Liam's `fixture.py` is authored in a plain shell before the verify run |
| B06 | verify — Phase 3 | `CCSession` (accept-edits) | the loop with its own correction cycle: fixture FAIL → Edit → PASS |
| B07 | verify — verify | `CCSession` (default) | Liam's bang-commands against the final page — evidence, not Claude's ✓ |
| B08 | CONDUCT | `CCBoondoggleScore` | the score of the run — 7 steps, dangerous middle at step 3 |
| B09 | HUMAN | `CCHumanLedger` | what was Liam's to do, from what actually happened |
| BVDT | verdict | `ClaudeVerdictArtifact` | 6 lines (verdict.md paginates 2/page → 3 pages, never 5) |
| BHTF | your turn | `ClaudeComposerAsk` | greeting `Your turn.`, prompt read in full |
| BOUT | outro | `ClaudeTitleOutro` | OUTRO-LOCK, `@NikBearBrown`, no subline |

## TERMINAL-FIRST audit

10 body beats. 6 render on a CC terminal surface (`CCSession`), 3 leave the terminal for a `CCPlainShell` (each with a named `leaves_terminal_because`), 1 leaves for `BrutalistHesitantWriter` (the IDEA beat), 1 leaves for `CCDefinitions` (the jargon beat). No two consecutive card beats. No card that could have been a `CCSession` text block. **PASS.**

## Session-fidelity audit

- REAL-SESSION: every `CCSession` block traces to `evidence/run-{bare,design,verify}.jsonl`; `SESSION.md` is the source-of-truth transcript.
- TYPES-NOT-NARRATES: every `prompt` block is what Liam actually typed (or the ask in `ask.txt`); no narration in a prompt block.
- VERBATIM-STRINGS: modes (`accept-edits`, `default`), status output (`FAIL:`, `PASS:`), and tool names come from the real runs.
- VERIFY-IS-A-COMMAND: cycle 1 (bare) ends on Liam's `wc`/`grep`; cycle 3 (verify) ends on Claude's own `python3 fixture.py` — a command, not a claim. The correction cycle is a real correction (`FAIL: no monospace font-family` → Edit → PASS at 153).

## Teaching arc

The film builds the reader to their own three-phase run:
- **Prediction before reveal** — B01 shows what the bare page shipped; the viewer can see the mailto and the invented agenda before the recap names them.
- **Concrete before abstract** — every phase is shown on a small real task before the CONDUCT beat abstracts them.
- **Useful friction** — the pick (B05) is the audience's decision to make; the film pauses there.
- **Falsifiability** — BVDT's last line is the one thing that would prove the film wrong.
- **Handoff to practice** — BHTF hands the viewer the exact prompt to run the same workflow on their own smallest task, and the HUMAN ledger (B09) is the scaffolded-task setup for it.

## Component library check

`./art scenes` matches all patterns used: `CCSession`, `CCPlainShell`, `CCDefinitions`, `CCBoondoggleScore`, `CCHumanLedger`, `BrutalistHesitantWriter`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `ClaudeTitleOutro`. All registered in Root.tsx under `<Folder name="CC">` / `<Folder name="Claude">` / `<Folder name="Brutalist">`. No new components required. No PUNTs.

## Gates before compile

- GATE F (`factcheck_check.py`) — PASS, 21 rows, 0 uncovered.
- GATE T (`kerning` / `type_check.py`) — will run on `art run`.
- GATE V (visual) — will run on `art run`.
- GATE BOOKEND — `metadata.skill: "cc-explainer"` set; four bookends present with the required ids.
- GATE SRT — `stage_publish.py` not required (never publish rule).
