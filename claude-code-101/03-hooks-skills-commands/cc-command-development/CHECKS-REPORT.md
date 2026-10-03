# CHECKS-REPORT — cc-command-development

Written before first compile, per cc-explainer / nopunt.

## SHOW / HOLD / CARD

| Beat | Kind | Surface | On-screen |
|---|---|---|---|
| B00 | SHOW | `CCSession` | v1 slash-invoked; Bash + two Reads; the essay opens with an emoji heading and closes on a question |
| BIDEA | CARD | `BrutalistHesitantWriter` | "shortcut" reconsidered into "spec"; four lines land |
| BDEFS | CARD | `CCDefinitions` | five terms with plain-line meanings |
| B01 | SHOW | `CCSession` (default mode) | Liam's `wc/grep/tail` runs against `out-v1.md` |
| B02 | SHOW | `CCDiff` | `.claude/commands/review.md` — three prose lines out, frontmatter + imperative body + format spec in |
| B03 | SHOW | `CCSession` | v2 slash-invoked; Bash `find` + Read; five rows in the spec's format; ends on `5 issues found.` |
| B04 | SHOW | `CCSession` (default mode) | Liam's `wc/grep/tail` runs against `out-v2.md` |
| B05 | HOLD | `CCBoondoggleScore` | six steps, dangerousMiddle at 2 |
| B06 | HOLD | `CCHumanLedger` | 4 MUST/SHOULD, 4 CAN/SHOULD, closing line |
| BVDT | HOLD | `ClaudeVerdictArtifact` | four lines; last is `FALSIFIABLE:` |
| BHTF | CARD | `ClaudeComposerAsk` | greeting `Your turn.`, topic `YOUR TURN · CLAUDE CODE 101` |
| BOUT | HOLD | `ClaudeTitleOutro` | exact title restated; handle `@NikBearBrown`, no subline |

## Teaching arc

- **Prediction before reveal.** BIDEA sets the misconception (shortcut) and the correction (spec) before the second run lands.
- **Concrete before abstract.** B00 shows the failure mode — Claude's essay — before BIDEA names why it happened. The abstraction ("the file is the spec") arrives after the viewer has seen the two output shapes.
- **Falsifiability.** BVDT's last line names what would prove the reel wrong: an imperative command that still returns an emoji essay.
- **Scaffolded task.** B06 (HUMAN ledger) sets up BHTF (YOUR TURN): both operate on the same object — the command file — and the closing prompt asks the viewer to do the same rewrite on their own last slash command.

## BUILD-SHOW

Not armed — this is a concept film in the Claude Code 101 tier `03-hooks-skills-commands`, film "Command Development": the subject is the *shape* of a slash command file, not building a running system. `metadata.build` is unset; BFLOW and BSHOW are intentionally skipped.

## LIAM LAW

- Operator: Liam, in for Bear, on every beat (cold open, body, and closing block).
- Voice: Kokoro `am_onyx` for every beat (free, local).
- Cold open opens on "This is Liam, in for Bear." (B00).
- Outro says "Liam, in for Bear." (BOUT).
- BVDT opens on "Let's recap with Claude." (the your-turn hand-off, not a "thanks").

## TERMINAL-FIRST

- Body beats default to `CCSession` (B00, B01, B03, B04).
- Non-terminal beats (BIDEA, BDEFS, B02, B05, B06) each carry `shot.leaves_terminal_because` naming the reason the concept cannot live in the session.
- Two consecutive non-terminal beats appear once (BIDEA → BDEFS, both between B00 and B01), each with its own reason; the reason for BDEFS is "definitions for a chat-window audience" (the concept card allowance in the SKILL).

## Kit gotchas passed

- Every `CCSession` `text` block ≤ 44 chars (author-time assert prints no warnings).
- Every `CCHumanLedger` row ≤ 30 chars (author-time assert prints no warnings; `humanCue` set so the AI column fills first).
- Every `CCBoondoggleScore` step ≤ 46 chars; `system` header ≤ 28 chars.
- `mascot: "off"` on every `CCSession` beat (all reach the bottom of the shell).
- `ClaudeVerdictArtifact` has exactly 4 lines (not 5).
- No `tokens: "↓ …"` — CCSession blocks would be double-arrowed; no such strings authored.
- No datable strings spoken (model names, versions, prices).
