# SOURCES — cc-pretooluse-grade-blocker

## The session (everything on screen)

- `SESSION.md` — the reel's source of truth; three real headless runs.
- `evidence/run-bare.jsonl`, `evidence/run-build.jsonl`, `evidence/run-build-resume.jsonl`, `evidence/run-hooked.jsonl` — stream-json for every run.
- `evidence/summary.bare.md`, `evidence/summary.hooked.md` — the two `summary.md` outputs written to disk by each run.
- `evidence/block-grades.py` — the hook as Claude wrote it (archived from `scratch/hooks/block-grades.py`).
- `evidence/settings.local.json` — the wiring as Liam typed it (archived from `scratch/.claude/settings.local.json`).
- `evidence/bad.json`, `evidence/ok.json`, `evidence/quantity.json` — the three unit-test payloads.
- `evidence/hook-block-message.txt` — the stderr the hook returned to Claude Code, verbatim.

## Doctrine (CONDUCT / HUMAN)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score frame; who did what and the handoff between steps.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — Tier 4 human ledger; why the metacognitive burden cannot be lent to the model.

## Product surface (never paraphrased)

- Claude Code hooks (`PreToolUse`, `matcher`, `exit 2`, stderr → reason, `is_error` on the tool result) — verbatim strings only.
- Fields visible on screen come from the kit's `tokens/claudecode.ts` via the CC components; never restyled here.
