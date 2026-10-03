# CHECKS-REPORT — cc-hook-advisory-vs-deterministic

## The spine

- B00 COLD OPEN (`CCSession`) · BIDEA (`BrutalistHesitantWriter`) · BDEFS (`CCDefinitions`)
- Loop cycle 1 — advisory holds: B00 shows PROMPT + THINK/TOOLS + CHANGE; B01 is the VERIFY (Liam's commands, not Claude's ✓)
- Correction cycle — advisory under attack: B02 (pressured), B03 (reframed) — VERIFY is Claude's verbatim refusal
- B04 — THE HOOK, RUN DIRECTLY (`CCPlainShell`, `leaves_terminal_because` = "the hook mechanism is a shell script outside a Claude session; running it directly proves the contract")
- Loop cycle 2 — hook enforces: B05 (Write attempt + BLOCKED tool_result); B06 (Claude reads stashed rule, corrects, second Write succeeds); B07 (VERIFY: wc, grep for `^Grade`, grep for `gradebook` — the honest edge case)
- Closing block — BCONDUCT (`CCBoondoggleScore`) · BHUMAN (`CCHumanLedger`) · BVDT · BHTF · BOUT

## Gates

- **TERMINAL-FIRST** — 13 of 15 body beats are `CCSession`; 1 (BIDEA) is the writer with `leaves_terminal_because`; 1 (B04) is `CCPlainShell` with `leaves_terminal_because`. Two consecutive non-terminal beats: **none**. PASS.
- **REAL-SESSION** — every tool name, path, exit code, and verbatim quote in the sheet traces to `evidence/run-*.jsonl` or the source-of-truth files. Documented in `FACTCHECK.md` row-by-row. PASS.
- **TYPES-NOT-NARRATES** — prompt blocks show what was typed (compressed at 44-char boundary; the full ask lives in narration and `evidence/ask.txt`). None are voiceover. PASS.
- **VERBATIM PRODUCT STRINGS** — mode strings (`accept-edits`, `default`), tool names (`Read`, `Write`, `Bash`), status verbs, and the block message are verbatim from the runs and the CC kit's `VERBS`. PASS.
- **VERIFY IS A COMMAND** — every cycle ends on Liam's shell (`wc`, `grep`, `tail`) or on Claude's own tool_result carrying the block; no cycle rests on a `✓`. PASS.
- **BUILD-SHOW** — not armed. This is a concept film that explains a Claude Code feature (`metadata.build` unset). BFLOW/BSHOW skipped. Note recorded here per the SKILL.
- **OUTRO-LOCK** — `ClaudeTitleOutro`; `handle: "@NikBearBrown"`; `subline: ""`; title restate exact. Liam says "in for Bear." PASS.
- **Never publish** — master will stay in the reel folder. TOPOST only on explicit `post` (not this run).

## Teaching arc

- **Prediction before reveal:** BIDEA asks the question ("advice is enough?") and the misconception is corrected on-screen ("not enough") before the demo lands.
- **Concrete before abstract:** the CLAUDE.md rule and the guard.py exit code are shown running before the CONDUCT/HUMAN abstraction.
- **Handoff to practice:** BVDT's FALSIFIABLE line ("a hook-active run that lands a matching grade line on disk") is what a viewer would run to disprove the reel; BHTF's Your Turn asks them to build the two-layer defense for their own project.
