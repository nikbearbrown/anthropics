# CHECKS-REPORT — cc-agentic-loop

Pre-compile checks; the pipeline gates (Gate V, GATE T, BOOKEND) will run at
`art run` / `art final`.

## Spine (cc-explainer)

- COLD OPEN (B00): CCSession, the loop run, `mascot: off` (full-stack).
- BIDEA (BIDEA): BrutalistHesitantWriter, CC palette; one word reconsidered — the misconception.
- BDEFS (BDEFS): CCDefinitions, 4 terms.
- LOOP CYCLE 1 (B00 + B01): PROMPT/THINK/TOOLS/CHANGE/VERIFY on the accept-edits run.
- CORRECTION (B02–B04): the reset + single-flag change to plan mode is the "same request, different permissions" correction cycle. B03 is the plan-mode PROMPT/THINK/TOOLS(stop) run; B04 is the plain-shell VERIFY.
- CONDUCT (B05): CCBoondoggleScore, 6 steps, dangerous middle at step 3.
- HUMAN (B06): CCHumanLedger, 4 rows per column, one-line closing.
- YOUR-TURN (BVDT / BHTF / BOUT): recap, composer, title outro. Liam owns all three.

## Build gates

- **BUILD-SHOW:** not armed — this is a CONCEPT film. The subject is the mechanism (loop vs. plan) itself, not a thing being built. `metadata.build` is unset; BFLOW / BSHOW are correctly skipped.
- **TERMINAL-FIRST LAW:** body beats are CCSession, CCPlainShell, or CCDefinitions/BrutalistHesitantWriter with `shot.leaves_terminal_because` naming the reason. Two consecutive non-terminal beats — BIDEA → BDEFS — are the intro block and both name reasons; no run of unreasoned card beats.
- **REAL-SESSION LAW:** every CCSession block traces to `evidence/run-{loop,plan}.jsonl`; every CCPlainShell line traces to SESSION.md's "Liam's VERIFY" or to a real command against `evidence/`; FACTCHECK rows enumerate the mapping.
- **TYPES-NOT-NARRATES LAW:** prompt blocks in B00 and B03 are the actual ask (`evidence/before/ask.txt`), not narration.
- **VERIFY IS A COMMAND:** each cycle ends with Liam running something. Loop cycle ends with B01 (`git diff --stat`, `unittest`); plan cycle ends with B04 (`git status`, `wc`, `head`).
- **VERBATIM PRODUCT STRINGS:** `accept-edits`, `plan` — the CCSession `mode` values, verbatim. `ExitPlanMode` — the real tool name Claude Code emits (see `run-plan.jsonl`).
- **NO EXTERNAL NAMES:** narration and on-screen text name only Liam and Bear. No third-party names.
- **OUTRO-LOCK:** BOUT uses ClaudeTitleOutro with `handle:"@NikBearBrown"`, `subline:""`, exact title.

## Kit budget compliance (author_sheet.py asserts)

- CCSession text blocks: all ≤ 44 chars (measured; author_sheet.py asserts on write).
- CCPlainShell lines: all ≤ 52 chars (measured).
- CCBoondoggleScore steps: 6 (≤ 7), each `text` ≤ 46 chars.
- CCHumanLedger rows: 4 per side (≤ 6), each `text` ≤ 34 chars; closing ≤ 14 words.
- CCDefinitions terms: 4 (≤ 5); terms ≤ 18 chars; meanings ≤ 70 chars.
- ClaudeVerdictArtifact: 4 lines (allowed set: {4, 6}).

## Teaching arc

- Prediction before reveal: BIDEA sets the misconception ("Claude Code is a faster chatbot"). B00 shows the loop finishing in one turn — the misconception fails immediately.
- Concrete before abstract: the concrete case (a real seven-tool loop closing a bug) precedes the abstract framing (agentic loop vs plan mode).
- Useful friction: BDEFS defines only the four words the film requires; nothing is redefined later.
- Falsifiability: BVDT's last line names the observation that would refute the film.
- Handoff to practice: BHTF's prompt is one keystroke away (`Shift+Tab twice`) with a real repo the viewer already has.

## Audio (already locked)

Kokoro `am_onyx` for all 12 beats via `generate_audio_kokoro.py`. Measured mp3
durations are the master clock and now sit in `beat_sheet.json`'s
`actual_duration_s` fields. Do not re-run `author_sheet.py` in place — it would
overwrite the audio stamps.
