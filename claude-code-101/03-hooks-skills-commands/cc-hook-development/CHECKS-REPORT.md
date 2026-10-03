# CHECKS-REPORT — cc-hook-development

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · 2026-09-10.

## SHOW / HOLD / CARD (per beat)

| beat | surface | classification | leaves_terminal_because |
|---|---|---|---|
| B00 COLD OPEN — BARE | `CCSession` | SHOW | — (in terminal) |
| BIDEA THE IDEA | `BrutalistHesitantWriter` | CARD | the idea is not in any session; writer types it and corrects the misconception |
| BDEFS DEFINITIONS | `CCDefinitions` | CARD | definitions for a chat-window audience who may not know the words |
| B01 DRAFT — SCRIPT | `CCSession` | SHOW | — |
| B02 DRAFT — THE WALL | `CCSession` | SHOW | — |
| B03 HUMAN WIRING | `CCPlainShell` | SHOW | file cat'd in a plain shell before the next session; no Claude session contains this |
| B04 SMOKE — VERIFY | `CCSession` | SHOW | — |
| B05 FIRES — REAL RUN | `CCSession` | SHOW | — |
| B06 HONEST LIMIT | `CCSession` (side-by-side) | HOLD | — (in terminal; the terminal is the illustration) |
| B07 CONDUCT | `CCBoondoggleScore` | CARD | CONDUCT contract — score the session just run |
| B08 HUMAN | `CCHumanLedger` | CARD | HUMAN contract — MUST/SHOULD/CAN ledger from the session |
| BVDT VERDICT | `ClaudeVerdictArtifact` | CARD | recap contract |
| BHTF YOUR TURN | `ClaudeComposerAsk` | CARD | your-turn contract |
| BOUT OUTRO | `ClaudeTitleOutro` | CARD | outro contract |

TERMINAL-FIRST budget: 8 of 14 beats live inside `CCSession`/`CCPlainShell`; no two consecutive non-terminal body beats. BIDEA and BDEFS are the two required non-terminal openers; the closing block (CONDUCT / HUMAN / VERDICT / YOUR TURN / OUTRO) is the your-turn contract, exempt from the terminal budget. Every off-terminal body beat names `leaves_terminal_because`.

## Teaching arc

- **Prediction before reveal.** BIDEA promises "a shell command at a moment" — the audience predicts a mechanism, not a magic. B01 shows Claude drafting exactly that. B02 breaks the prediction one way (the settings file, not the script, is the wall); B04 tests it defensively before the real run puts anything on it.
- **Concrete before abstract.** The bare cold open shows an ordinary edit — no receipt. Only after the smoke test does the film say what a matcher is or what an event contract means. B06 is the abstraction: PostToolUse vs PreToolUse, exit 0 vs exit 2 — earned by watching one work.
- **Useful friction.** The correction cycle in this reel is *not* a re-prompt to Claude. It is Liam picking up the pen after the harness refuses Claude four times. That is the pedagogy: the two lines only you can sign.
- **Scaffolded handoff.** BHTF's YOUR TURN prompt — "Draft a PostToolUse hook that logs every Write and Edit. Two files. Do not run." — is deliberately the same shape as the reel's own draft ask, so the viewer's first hook attempt looks like the film's B01, and their B03 is the same wire-up by hand. The falsifiable line in BVDT gives them an experiment they can actually run.

## Falsifiability

`BVDT` last line: **"FALSIFIABLE: Claude edits `.claude/settings.local.json` on its own, without a paste."** Anyone can retry the draft cycle in a fresh scratch and check whether the harness still refuses. If it stops refusing, this reel is out of date.

## BUILD-SHOW: not armed

This is a **concept film**, not a build film. `metadata.build` is not set. Per the cc-explainer skill's build-show rule, BFLOW and BSHOW are skipped and declared here. The concept is the mechanism of hooks (event + matcher + command + exit code), not the delivery of a new working artifact for the viewer to run.

## Gates (final)

| gate | result | notes |
|---|---|---|
| Gate V | PASS | 0/0/0 (no PUNT, no REDRAW, no BLOCKER) |
| GATE T (§8) | PASS | 14/14 beats, 0 FAILs, `TYPECHECK.md` |
| GATE BOOKEND | PASS | B00 CCSession cold open; BVDT / BHTF / BOUT ids; `@NikBearBrown` handle; subline `""` |
| GATE SHARPNESS | PASS | median LV 598.2, all beats above 50% |
| GATE LOUDNESS | PASS | -24.29 LUFS, -2.83 dBTP |
| GATE MASTER | PASS | 3840×2160, 277.58 s, drift 0.02 s |
| FACTCHECK | PASS | see `FACTCHECK.md` |
| PLACEHOLDER | PASS | no unfilled slots |

Master: `cc-hook-development.mp4` (4:37, 3840×2160, native 4K). Not published; not staged to TOPOST.
