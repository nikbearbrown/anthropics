# CHECKS-REPORT — cc-writing-rules

Written before the first compile.

## SHOW / HOLD / CARD

- **SHOW (13 beats)** — every body beat renders on `CCSession` / `CCPlainShell` and traces to `SESSION.md`. The two off-terminal beats (BIDEA `BrutalistHesitantWriter`, BDEFS `CCDefinitions`) each name `shot.leaves_terminal_because`.
- **HOLD** — none. Every beat's narration lands inside its rendered duration; audio (Kokoro `am_onyx`) is the master clock.
- **CARD** — the four bookends (BIDEA, BDEFS, BVDT, BHTF, BOUT). Everything else is a terminal frame.

## TERMINAL-FIRST accounting

- Body cycles (B00/B01, B03/B04, B05): 5 `CCSession` beats — all inside the terminal.
- Non-terminal beats: BIDEA + BDEFS + B02 (`CCPlainShell` — still a shell but not the Claude Code session). No two consecutive card beats.
- Every non-terminal beat carries a `shot.leaves_terminal_because` string.

## Teaching arc

- **Prediction before reveal** — B00 shows the bare run happening; B01 makes the viewer pause on `grep -c '^name:' → 0` before saying the word "wrong". BVDT's FALSIFIABLE line names what would disprove the reel: a bare run that reads a SKILL it wasn't shown.
- **Concrete before abstract** — the schema is only introduced (B02) after the bare failure (B00/B01) has shown *why* it matters.
- **Useful friction** — B05 tests the pattern regex against three real paths; the viewer sees one match, one match, one None. Same law as the exemplar's `check.py` comparison.
- **Handoff to practice** — YOUR TURN (BHTF) is the scaffolded task; the human ledger (B07) is the scaffolding.

## BUILD-SHOW: not armed — concept film

`metadata.build` is unset. The film explains a Claude Code feature (skills on disk) and does **not** build a shippable artifact whose output the viewer must see. The two artifacts on screen (`settings.json`, `hookify.<name>.local.md`) serve as the VERIFY receipts for two different behaviors, not as a "here is the thing we built and ran" BSHOW.

## Sheet budgets (from `author_sheet.py`)

- 13 beats, ~322 s narration estimate; audio measured 275.5 s.
- No text-block warnings (all `CCSession` text rows ≤ 44 chars).
- No `CCHumanLedger` row over 34 chars; no `CCBoondoggleScore` step over 46 chars.
- BVDT is 4 artifact lines — two per page, no orphan.
- All `CCSession` beats set `mascot: "off"` (full block stacks; guards against Clawd landing on the last rows).
