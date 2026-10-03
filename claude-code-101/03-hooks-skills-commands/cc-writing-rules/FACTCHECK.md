# FACTCHECK — cc-writing-rules

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (two real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the two runs' stream-json, the two artifacts, and the plugin's own `SKILL.md`, all captured in `evidence/`. Liam's checks were run in a plain shell on the evidence folder and are shown as bang commands inside the session. Claude's sentences are verbatim spans. The source concept's framing (a plugin's SKILL is the rule shape) is kept; the concept sheet's stub `.local.md` output-shape claims are replaced by two real runs.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B03 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Bare run: `Skill(update-config)`, `ls -la .claude/`, plan sentence, `Write .claude/settings.json` | PASS | `run-bare.jsonl`; text truncated at ~44 chars per row (kit wrap budget) | — |
| 3 | B01 | `wc -l .claude/settings.json` → 16; `grep -c '^name:'` → 0; the first three lines are `{` / `$schema` / `hooks: { PreToolUse …` | PASS | `evidence/bare.settings.json`; `grep -c '^name:' bare.settings.json` → 0; SESSION VERIFY | — |
| 4 | B01 | "the write went through — the hook did not fire because settings.json was created mid-session" | PASS | `run-bare.jsonl` — Claude wrote `.env.hooktest` and then `rm`-ed it; Claude's own sentence, verbatim | — |
| 5 | B02 | The plugin's SKILL.md fields (`name`, `enabled`, `event`) and file path convention `.claude/hookify.<name>.local.md` | PASS | `evidence/SKILL.md` — `Rules are stored in .claude/hookify.{rule-name}.local.md files.` and the frontmatter section | — |
| 6 | B02 | `wc -l SKILL.md` → 374 | PASS | `wc -l evidence/SKILL.md` — matches (SKILL.md is 374 lines) | — |
| 7 | B03 | Skill run: `Skill(writing-rules)`, `ls -la .claude/` shows `skills/`, `Write .claude/hookify.block-env-file-edits.local.md` | PASS | `run-skill.jsonl` | — |
| 8 | B04 | `wc -l hookify.*.local.md` → 21; head 5 shows `---` / `name: block-env-file-edits` / `enabled: true` / `event: file`; `check_rule.py` → PASS | PASS | `evidence/hookify.block-env-file-edits.local.md`; `evidence/check_rule.py` | — |
| 9 | B05 | Python `re.search` results across three paths — `.env` matches, `/a/.env.prod` matches, `env-var.txt` is None | PASS | verified interactively against `evidence/hookify.block-env-file-edits.local.md`'s pattern; on-screen `.env.prod` is the input to the second call, not a truncation of the first | — |
| 10 | B06 | Six steps; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | maps to SESSION.md; no plan mode, no subagents | — |
| 11 | B07 | Ledger rows (MUST/SHOULD × CAN/SHOULD) reflect what actually happened in the two runs | PASS | rows 3, 4 (SESSION.md) | — |
| 12 | BVDT | Verdict lines: bare 16-line settings.json; skill 21-line hookify rule; live proof passed; falsifiable | PASS | rows 2–4 | — |
| 13 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 14 | all | Model / version strings (e.g. "Claude Code 2.1.150", "2026-09-10", costs) | EXEMPT | not shown or spoken; recorded in SESSION.md/BUILD-LOG.md only | — |
| 15 | metadata | Costs ($0.830 / $0.344) and durations (62.4s / 28.2s) | EXEMPT | recorded, not spoken; only "9 turns" / "5 turns" narrative-adjacent claims are absent from narration | — |
