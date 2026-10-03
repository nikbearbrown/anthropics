# CHECKS-REPORT — cc-grading-skill-definition

Written before the first compile.

## Show / hold / card

- **Show, not tell.** Every claim about the skill is a claim about a transcript line — the `Skill()` tool call, the `Write`, the `Bash python3 check_feedback.py`. The verify beats show `grep` and `wc` outputs. No card asserts a fact the session cannot verify.
- **Hold.** BFLOW (anatomy) and BSHOW (durability) hold long enough to read — BFLOW's five rows land one at a time; BSHOW's Bash tool call and PASS text are the last beats before the closing block.
- **Card.** Two cards leave the terminal legitimately: BIDEA (the idea, on `BrutalistHesitantWriter`) and BDEFS (four terms, on `CCDefinitions`). BFLOW's `CCPlanCard` is also a card, per BUILD-SHOW LAW.

## Teaching arc

- **Prediction before reveal.** The bare run in B00 sets up a prediction — will Claude add a grade? — before B01 answers it.
- **Concrete before abstract.** Three real feedback files precede the anatomy card in BFLOW.
- **Useful friction.** Each of the two `## FAIL` verify beats is a moment of prediction failure that funds the correction beat that follows.
- **Handoff.** BVDT's `FALSIFIABLE:` line is the falsifiability beat. BHTF is the scaffolded task: the viewer builds their own SKILL.md the same way the reel just did.

## BUILD-SHOW gate

Armed: `metadata.build: true`. Both slots present:
- BFLOW: `CCPlanCard` — the four sections of `SKILL.md`, labelled by role.
- BSHOW: `CCSession` — the durability run on `priya.md`, real transcript, real PASS.

Both sit immediately before CONDUCT.

## Kit gotchas checked at authoring

- Every `CCSession` `text` block is ≤ 44 characters (author_sheet.py asserts).
- Every `CCHumanLedger` row is ≤ 30 characters.
- Every `CCBoondoggleScore` step is ≤ 44 characters.
- BVDT is 4 lines; the fourth is `FALSIFIABLE:`.
- Every `CCSession` beat sets `mascot:"off"` — the stacks reach the bottom of the shell.
- `CCPlainShell` used for B02 (writing the SKILL.md file) and B05 (adding the two blocks); those are edits outside a Claude session.
- Every `CCSession` `blocks` array length matches its `cues` array length.
- No datable strings in narration: no model names, no version numbers, no prices, no "as of."
