# BUILD-PROMPT — cc-claude-101

## What this film is

"Claude, Oversimplified." A beginner's working mental model of Claude — but the mental model isn't the marketing menu (surfaces, tiers, models). The mental model is: **Claude is one function; the ask is the whole difference.** Same folder, same model, four fresh headless runs — a concrete ask that produces a testable file, a vague ask with no ground (the model refuses to guess), a vague ask with a file (the dangerous middle: opinion sounds grounded), and a correction that rewrites the vague ask into something testable. Then the two closing-block beats (CONDUCT, HUMAN), the verdict, YOUR TURN, and the locked outro.

## How to build it

1. `python3 author_sheet.py` — writes `beat_sheet.json` from the beats above. Text-block, ledger-row, and step-length budgets are asserted at the bottom; fix warnings before continuing. (This author_sheet is what to change if a beat needs revision — never edit `beat_sheet.json` while `art run` is alive.)
2. `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py anthropics/claude-code-101/00-what-it-is/cc-claude-101` — Liam (`am_onyx`) narration for every beat.
3. `python3 brutalist-art/runtime/qc/factcheck_check.py anthropics/claude-code-101/00-what-it-is/cc-claude-101` — must print `clean`.
4. `./brutalist-art/art run anthropics/claude-code-101/00-what-it-is/cc-claude-101` — the review cut.
5. Read `_qc/REPORT.md` and `TYPECHECK.md` if Gate V or GATE T fails; fix at the source (shorten strings, `mascot: 'off'` on full stacks, 4 or 6 verdict lines), re-render only the failing beat.
6. `./brutalist-art/art final anthropics/claude-code-101/00-what-it-is/cc-claude-101` — clean master.
7. `BUILD-LOG.md` — record what the session gave the film, and every compile pass.
8. **STOP.** No `art post`, no TOPOST, no publish.
