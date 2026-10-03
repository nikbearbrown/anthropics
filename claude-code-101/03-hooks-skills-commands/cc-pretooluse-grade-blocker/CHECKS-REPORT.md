# CHECKS-REPORT — cc-pretooluse-grade-blocker

## SHOW / HOLD / CARD

- SHOW beats: B00 (bare run), B01 (build ask), B02 (refusal), B04 (unit tests), B05 (hooked run block+retry) — all reconstructed from stream-json.
- HOLD beats: BSHOW (grep+wc receipts on the two summary files) — the reel's evidence, held long enough to read.
- CARD beats: BIDEA (the argument), BDEFS (five terms), BFLOW (the pipeline).

## Teaching arc

- **Prediction before reveal.** BIDEA states the argument (hope vs. hook) before B01 builds the fence; B04 predicts the exit codes before B05 shows the same ask hitting them.
- **Concrete before abstract.** BFLOW comes AFTER the reader has already seen the hook fire in B05's mind — the diagram names what they just saw, it doesn't teach it cold.
- **The falsifiability beat.** BVDT's last line is the falsifiable claim ("a bare run that refuses the letter-grade line on its own").
- **The scaffolded task.** BHUMAN names the four MUST rows; BHTF asks the viewer to run the same pattern on their own project ("customer email, API key, raw SSN") — same shape, different pattern.

## BUILD-SHOW arming

- `metadata.build: true` — build film. BFLOW and BSHOW both present, immediately before CONDUCT.
- BFLOW: FlowDiagram (skin=claude) with six nodes named from the session: `claude`, `harness`, `hook` (block-grades.py), `stdin` (tool_input JSON), `deny` (exit 2 + stderr), `retry`.
- BSHOW: CCPlainShell with wc + grep counts on `evidence/summary.bare.md` and `evidence/summary.hooked.md` — the built thing's receipt on disk.

## Voice / persona lock

- Liam (`am_onyx`) on every beat. IN-FOR-BEAR LAW satisfied twice: B00 cold open ("This is Liam, in for Bear"), BOUT outro ("Liam, in for Bear").
- Handoff into recap on BVDT: "Let's recap with Claude."
- No name other than Liam or Bear is spoken; product surface strings verbatim; nothing datable said.

## Kit gotchas checked

- CCSession text blocks: every block ≤ 44 chars (`author_sheet.py` asserts).
- CCHumanLedger rows: every row ≤ 30 chars (asserted).
- CCBoondoggleScore step text: every step ≤ 44 chars (asserted).
- CCDefinitions terms ≤ 18, meanings ≤ 75 (asserted).
- CCPlainShell lines ≤ 60 (asserted).
- ClaudeVerdictArtifact: 4 lines (asserted).
- `mascot: "off"` on every CCSession with a tall block stack (all body beats).
- Status `tokens` strings: none used (no `↓` risk).

## LIBRARY-FIRST (GATE L)

- Every pattern in the sheet is registered in `runtime/remotion/src/scenes.json` (verified before authoring): `CCSession`, `CCPlainShell`, `CCDefinitions`, `BrutalistHesitantWriter`, `FlowDiagram`, `CCBoondoggleScore`, `CCHumanLedger`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `ClaudeTitleOutro`. No PUNTs.
