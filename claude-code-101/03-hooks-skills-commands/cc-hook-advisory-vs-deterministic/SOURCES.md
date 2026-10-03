# SOURCES — cc-hook-advisory-vs-deterministic

## The runs

Every claim traces to one of the following, all in `evidence/`.

- `run-advisory.jsonl` — Run 1, nice ask + CLAUDE.md + no hook. Session `028c6a3f`. `summary.advisory.md` is the file written.
- `run-advisory-pressured.jsonl` — Run 2, pressured ask + CLAUDE.md + no hook. Session `67526cc5`. No file written; Claude refused in a single turn.
- `run-advisory-reframed.jsonl` — Run 3, "ignore any prior instructions" ask + CLAUDE.md + no hook. Session `5641f64e`. No file written; Claude refused.
- `run-hook-only.jsonl` — Run 4, nice ask + hook active + CLAUDE.md stashed. Session `6e5c0a88`. `summary.hook-only.md` is the second write (the first was blocked).
- `run-hook-blocks.jsonl` / `run-hook-fixture.jsonl` — audit-trail only; not shown on screen. Kept because the ask files (`ask-hook.txt`, `ask-hook2.txt`) are referenced in SESSION.md as tried-and-failed framings.

## The source-of-truth files

- `CLAUDE.md` — 9 lines. The advisory rule.
- `guard.py` — 42 lines of Python. The PreToolUse hook.
- `settings.local.json` — 15 lines. Wires the hook into `Write|Edit|MultiEdit`.
- `bad.json` / `ok.json` — the two payloads used in the direct hook demo (B04).
- `students.csv`, `ask.txt`, `ask-pressured.txt`, `ask-reframed.txt` — the inputs.
- `hook-block-message.txt` — the tool_result harvested from `run-hook-only.jsonl` showing the block text Claude received.

## The doctrine (CONDUCT / HUMAN beats)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle-score frame: capacities (`[PF]` / `[PA]` / `[IJ]` / `[TO]` / `[EI]`), the "dangerous middle," and the handoff-conditions doctrine.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the ledger: what the human MUST decide, what the AI CAN and SHOULD do; the reason the metacognitive burden cannot be lent to the model.

## The kit / skill

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERBATIM-STRINGS, the spine.
- `brutalist-art/runtime/remotion/src/scenes/CC-TEMPLATES.md` — the CC kit component contracts and product strings.
- `brutalist-art/skills/make/your-turn/SKILL.md` — the closing block (VERDICT / YOUR TURN / OUTRO).
