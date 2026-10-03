# SOURCES — cc-hook-development

Every source cited on screen or leaned on for a factual claim.

## The session (primary; the film IS the reconstruction of it)

- `SESSION.md` — trimmed transcript of the three real headless `claude -p` runs, 2026-09-10.
- `evidence/ask.txt` — the ask, verbatim.
- `evidence/run-bare.jsonl`, `evidence/run-draft.jsonl`, `evidence/run-fires.jsonl` — raw `--output-format stream-json --verbose` streams for each run (18 / 38 / 16 events respectively).
- `evidence/run-{bare,draft,fires}.stderr` — captured stderr (all empty).
- `evidence/session-ids.txt` — Claude Code session ids for the three runs.
- `evidence/log-write.sh.CLAUDE_DRAFT` — the 20-line bash script Claude drafted, verbatim.
- `evidence/log-write.sh.MINE` — the tightened, chmod'd copy that ran under the hook.
- `evidence/hooks-log-write.sh` — the copy the hook actually shelled to.
- `evidence/settings.local.json` — the wired `.claude/settings.local.json` (15 lines, mine).
- `evidence/settings.local.json.MINE` — pre-run copy for the diff.
- `evidence/writes.log.smoke` — the log after the three smoke-test payloads.
- `evidence/writes.log.fires` — the log after the fires run (single line).
- `evidence/target.md.before`, `evidence/target.md.after_bare`, `evidence/target.md.after`, `evidence/target.md.final` — the four states of the file the runs touched.

## Source concept (this reel derives from)

- `anthropics/claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-hook-development/` — the earlier claude-explainer concept sheet whose title and Your-Turn intent this reel keeps; its beats and card body are replaced by the real session.
- `anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md` — Hook Development skill v0.1.0. The BDEFS terminology (PreToolUse / PostToolUse / matcher / hooks wrapper) and B06's contract summary (exit 0 vs exit 2; same script shape, different event) come from here.

## Doctrine for the closing block

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the framing for CONDUCT (Boondoggle Score): who did what, what the human's supervisory capacity was, what the handoff condition between steps had to be.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the framing for HUMAN (Ledger): the metacognitive burden can't be lent; verification is not the leftover work.

## Skill governance

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — the skill this reel is built under. LIAM LAW, TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERBATIM-STRINGS, and the spine come from here.
- `brutalist-art/skills/make/ai-explainer/SKILL.md` — parent skill. LOGO / REBUILD / FILL-THE-CANVAS / DOUBLE-CHECK / OUTRO-LOCK.
- `brutalist-art/skills/make/your-turn/SKILL.md` — the closing three (VERDICT · YOUR TURN · OUTRO) contract.
- `brutalist-art/skills/make/kerning/SKILL.md` and `runtime/scripts/type_check.py` — GATE T.
- `brutalist-art/runtime/remotion/src/scenes/CC-TEMPLATES.md` and `runtime/remotion/src/tokens/claudecode.ts` — the CC interface kit and its verbatim product strings.

## Nothing datable spoken

Model version numbers, prices, "as of" language, and any release-cycle claim are excluded from narration and on-screen text per REAL-SESSION LAW's datable-facts prohibition. Session costs are recorded in `SESSION.md` for provenance and not spoken.
