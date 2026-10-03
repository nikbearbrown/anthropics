# PROMPTS — cc-claude-skills

The exact `claude -p` invocations that produced `evidence/run-{bare,skill,nomatch}.jsonl`. Claude Code 2.1.150, 2026-09-10, from `/tmp/cc-claude-skills-scratch/`.

## Common flags (all three runs)

```
--output-format stream-json
--verbose
--max-turns 12
--permission-mode acceptEdits
--strict-mcp-config
--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*)"
< /dev/null
```

`--strict-mcp-config` blocks every MCP server. `--allowedTools` fences the harness to the eight tools it needs. Stdin closed to `/dev/null` so no interactive follow-up ever arrives. Every run uses a fresh `--session-id`.

## Run A — bare (`evidence/run-bare.jsonl`)

**Folder state.** `.claude/skills/` did not exist (renamed to `.claude-off` for the run).

```
claude -p "Please summarize article.md." \
  --session-id 11111111-1111-1111-1111-111111111111 \
  [common flags]
```

Result: `success`, 2 turns, 10.5 s, $0.109. `grep -c '"name":"Skill"' run-bare.jsonl` → 0.

## Run B — skill on the natural ask (`evidence/run-skill.jsonl`)

**Folder state.** `.claude/skills/exec-summary/{SKILL.md, check_summary.py}` restored; description is `Utility for summarizing documents in a house style.`

```
claude -p "Please summarize article.md." \
  --session-id 22222222-2222-2222-2222-222222aaaaaa \
  [common flags]
```

Result: `success`, 6 turns, 25.8 s, $0.149. Tool sequence: `Skill(exec-summary)` → `Read(article.md)` → `Write(summary.md)` → `Bash(python3 …/check_summary.py summary.md)` → `PASS`. Output: `evidence/summary.skill.md`.

## Run C — skill on the paraphrased ask (`evidence/run-nomatch.jsonl`)

**Folder state.** Same as Run B. Same skill, same description.

```
claude -p "Wrap article.md for a leadership audience — the CEO reads this Friday." \
  --session-id 33333333-3333-3333-3333-333333333333 \
  [common flags]
```

Result: `success`, 8 turns, 63.9 s, $0.256. Tool sequence: `Skill(exec-summary)` → `Bash(ls …)` → `Read(article.md)` → `Read(check_summary.py)` → `Write(summary.md)` → `Bash(python3 …/check_summary.py summary.md)` → `PASS`. Output: `evidence/summary.nomatch.md`.

The ask contains no literal trigger word (`summarize`, `summary`, `TL;DR`, `brief`, `recap`). The description matched on meaning.

## Note

`--session-id 22222222-2222-2222-2222-222222222222` was consumed by the first (accidentally lost) attempt at Run B; the surviving Run B uses `22222222-2222-2222-2222-222222aaaaaa` on the same starting folder state.
