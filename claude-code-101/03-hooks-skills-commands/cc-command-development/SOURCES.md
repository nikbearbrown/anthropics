# SOURCES — cc-command-development

## Primary — the film's own evidence

- `SESSION.md` — the two real headless runs this reel reconstructs. Ground truth for every `CCSession` block.
- `evidence/run-v1.jsonl`, `evidence/run-v2.jsonl` — raw `claude -p --output-format stream-json --verbose` transcripts.
- `evidence/review-v1.md`, `evidence/review-v2.md` — the two command files, exactly as they lived in `scratch/.claude/commands/`.
- `evidence/review-v1-v2.diff` — the diff shown in B02.
- `evidence/inventory.py` — the scratch repo's Python file with planted bugs; the target of both runs.
- `evidence/out-v1.md`, `evidence/out-v2.md` — Claude's harvested outputs; every count in the reel (`wc -l`, `grep -c`, `tail -1`) is run against these.

## Secondary — doctrine

- `anthropics/claude-code/plugins/plugin-dev/skills/command-development/SKILL.md` — the source SKILL. Its "Commands are Instructions FOR Claude, not messages TO the user" framing is the film's misconception-and-fix; its `Correct approach` / `Incorrect approach` examples are the template for `review-v1.md` (message-to-user) and `review-v2.md` (imperative).
- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — behind CONDUCT (Boondoggle Score, capacity labels).
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — behind HUMAN (the ledger, MUST/SHOULD × CAN/SHOULD).

## Not used

- Product-version strings (`claude-opus-4-7[1m]`, `2.1.150`), cost/duration numbers, and session UUIDs are recorded in `evidence/` but never spoken or shown on-screen.
