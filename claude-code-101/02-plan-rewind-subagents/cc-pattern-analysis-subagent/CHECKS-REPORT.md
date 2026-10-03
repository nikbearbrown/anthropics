# CHECKS-REPORT — cc-pattern-analysis-subagent

- **Skill:** cc-explainer · Claude Code 101 · tier 02-plan-rewind-subagents.
- **Ask verb:** "deploy" — build film. `metadata.build: true` — BFLOW + BSHOW armed.
- **BUILD-SHOW:** armed. BFLOW = topology across two windows (FlowDiagram, claude skin, real names). BSHOW = the produced `feedback_focus.md`, in CCPlainShell, verbatim.
- **Operator:** Liam, in for Bear. Kokoro `am_onyx` for every beat, body and closing block.
- **IN-FOR-BEAR LAW:** satisfied twice — B00 ("This is Liam, in for Bear") and BOUT ("Liam, in for Bear.").

## Spine present

- B00 COLD OPEN (CCSession, inline run: the ask + 6 real Reads + Write)
- BIDEA THE IDEA (BrutalistHesitantWriter — CC palette; ONE word corrected: `prompt` → `subagent`)
- BDEFS DEFINITIONS (CCDefinitions — 4 terms the chat-window audience will hear)
- Cycle 1 INLINE: B00 (PROMPT/THINK/TOOLS/CHANGE) → B01 (VERIFY — Liam's `!wc`, `!grep`, `!jq`)
- Cycle 2 CORRECTION: B02 (the deployment, CCPlainShell, outside any session) → B03 (SUBAGENT — Task + Write) → B04 (VERIFY)
- BFLOW (FlowDiagram — six real-named nodes; every label traces to `SESSION.md`)
- BSHOW (CCPlainShell — `cat feedback_focus.md`, three verbatim findings)
- CONDUCT B05 (CCBoondoggleScore — 6 steps, `dangerousMiddle: 3` = the deployment file the human wrote)
- HUMAN B06 (CCHumanLedger — 4 human rows, 4 AI rows, closing)
- BVDT (ClaudeVerdictArtifact — exactly **4** lines, last line `FALSIFIABLE:`)
- BHTF (ClaudeComposerAsk — greeting `Your turn.`, topic `YOUR TURN · CLAUDE CODE 101`)
- BOUT (ClaudeTitleOutro — exact title, `@NikBearBrown`, `subline: ""`)

## Teaching arc

- The **falsifiability** beat is BVDT's last line: *"a subagent invocation whose main session Reads a batch file after the summary returns"* — testable by grep on any future run.
- The **scaffolded task** for YOUR TURN is B06's ledger: writing a whitelist for a triage subagent (name, description, three-tool whitelist) — the same skeleton Liam wrote for `pattern-analyzer.md`.

## SHOW / HOLD / CARD

| Beat | Surface | Reason for surface |
|---|---|---|
| B00, B01, B03, B04 | CCSession | terminal-first LAW — the interface is the subject |
| BIDEA | BrutalistHesitantWriter | idea beat, always; corrected word carries the film's pedagogy |
| BDEFS | CCDefinitions | jargon the chat-window audience will hear |
| B02 | CCPlainShell | the deployment file is OUTSIDE any session — reading it in a Claude session would be a lie |
| BFLOW | FlowDiagram | topology across two windows; not visible in either window |
| BSHOW | CCPlainShell | the built artifact, `$ cat …`; not a mockup |
| B05 | CCBoondoggleScore | CONDUCT beat contract |
| B06 | CCHumanLedger | HUMAN beat contract |
| BVDT, BHTF, BOUT | ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro | your-turn standard |

## Non-terminal beats

Only BIDEA / BDEFS / B02 / BFLOW / BSHOW / B05 / B06 leave `CCSession`. Every non-terminal beat carries `shot.leaves_terminal_because` naming what the terminal cannot show (idea; jargon; outside-session file; topology; produced artifact; conductor/ledger contracts). No two consecutive body beats leave the terminal without reason — B02 is followed by B03 (in-session), and BFLOW/BSHOW sit between the last verify and CONDUCT per BUILD-SHOW LAW.

## Kit gotchas checked

- CCSession `text` blocks: every block ≤ 44 chars (asserted in `author_sheet.py`).
- CCSession status blocks: none used (the `!` prompt trick shows tokens as free text, not a status block).
- CCHumanLedger rows: all ≤ 34 chars (asserted).
- CCBoondoggleScore `text`: all ≤ 46 chars (asserted); `system` header 26 chars.
- CCPlainShell lines: B02 = 13 lines, BSHOW = 11 lines (max is 14).
- `mascot: 'off'` on every CCSession that has full-height block stacks.
- ClaudeVerdictArtifact: 4 lines exactly. Never 5.
- `handle: "@NikBearBrown"`, `subline: ""` on BOUT.
- IN-FOR-BEAR LAW: two mentions, B00 and BOUT.

## Cost gate

Zero paid generation. Kokoro (free, local) for every beat. Two headless `claude -p` runs against my own API balance are the only spend and were already made before authoring.
