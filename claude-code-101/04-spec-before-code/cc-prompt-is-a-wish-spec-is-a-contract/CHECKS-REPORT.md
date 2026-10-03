# CHECKS-REPORT — cc-prompt-is-a-wish-spec-is-a-contract

cc-explainer · Claude Code 101 · tier `04-spec-before-code` · Liam, in for Bear · pre-compile.

## Show / Hold / Card per beat

| ID | Beat | Surface | Reason (SHOW / HOLD / CARD / off-terminal) |
|---|---|---|---|
| B00 | COLD OPEN — WISH | CCSession | SHOW — the wish run's real trace |
| BIDEA | THE IDEA | BrutalistHesitantWriter | off-terminal (leaves_terminal_because set) — the film's own thesis, typed |
| BDEFS | DEFINITIONS | CCDefinitions | off-terminal — chat-window audience needs the terms |
| B01 | WISH — VERIFY | CCSession | SHOW — Liam's commands + real outputs |
| B02 | THE SPEC | CCPlainShell | off-terminal — SPEC.md is read outside any session |
| B03 | SPEC — THE RUN | CCSession | SHOW — the spec run's real trace |
| B04 | SPEC — VERIFY | CCSession | SHOW — Liam's commands + real outputs |
| B05 | THE MIDDLE CASE | CCSession | SHOW — the tests-only run's real trace |
| B06 | CONDUCT | CCBoondoggleScore | CARD — the score of what just happened |
| B07 | HUMAN | CCHumanLedger | CARD — the ledger of who did what |
| BVDT | VERDICT | ClaudeVerdictArtifact | HOLD — recap card, 4 lines |
| BHTF | YOUR TURN | ClaudeComposerAsk | CARD — the viewer's prompt |
| BOUT | OUTRO | ClaudeTitleOutro | HOLD — locked outro |

Two consecutive non-terminal beats (BIDEA + BDEFS) is the standard IDEA→DEFINITIONS opening; both name `leaves_terminal_because`. B02 is off-terminal (plain shell) because SPEC.md is authored before any session runs — it has no CCSession to belong to.

## Teaching arc

- **Prediction beat:** B00 sets the wish. The viewer expects a broken function; they get 4-of-5 hygienic tests + one silent invariant failure + one unasked-for function. The surprise is the *shape* of the failure, not its presence.
- **Concrete before abstract:** three real runs before the score. B06 (CONDUCT) and B07 (HUMAN) generalize only what the runs already showed.
- **Falsifiability:** BVDT's last line names what would prove the reel wrong (a wish run whose choices all match a spec Claude was never shown).
- **Handoff to practice:** BHTF asks the viewer to run the same experiment on their next build — write a SPEC before Claude touches anything.

## Verifications complete before compile

- Session fidelity: every `CCSession` block in `beat_sheet.json` traces to a `run-*.jsonl` (see `FACTCHECK.md` rows).
- Product strings: `accept-edits` / `default` mode names verbatim; unittest output verbatim (`Ran 5 tests`, `OK`, `F....`).
- Kit gotchas: text blocks ≤ 44 chars (author_sheet asserts, clean); ledger rows ≤ 34 chars (clean); score steps ≤ 46 chars (clean); verdict is 4 lines; BOUT carries `handle` and `subline:""`; every full-stack session has `mascot:"off"`; status tokens carry no leading `↓`.
- Budgets: 13 beats · 342 s estimated (author) · 271 s narrated (Kokoro measured, ground truth).

## Build gate

- **BUILD-SHOW:** not armed — this is a concept film. It shows *what the difference between a wish and a spec looks like on the terminal*, not "here is a thing you build." No BFLOW / BSHOW required.

## Not-punts

- The verdict says "40 lines / 33 lines / 34 lines" — those are `wc -l` results reproducible from `evidence/`. Not punts.
- The CONDUCT beat's `dangerousMiddle: 3` is Liam's audit judgment (the step where he'd have to catch the empty-string invariant himself), grounded in the actual test output.
