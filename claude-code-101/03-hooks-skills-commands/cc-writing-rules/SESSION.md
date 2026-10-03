# SESSION.md — cc-writing-rules

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, same one-sentence ask (`evidence/ask.txt`), two conditions. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`; `--permission-mode bypassPermissions` (scratch scope only, so `.claude/` writes complete). Raw stream-json in `evidence/run-bare.jsonl` and `evidence/run-skill.jsonl`; the two artifacts and the schema-checker in `evidence/`.

```
Add a hookify rule to this project that BLOCKS any edit or write to a `.env` file. Save it in `.claude/`.
```

| Condition | What was in the folder |
|---|---|
| **bare** | `README.md` (2 lines), `ask.txt` |
| **skill** | the same plus `.claude/skills/writing-rules/SKILL.md` — the plugin's rule-writing SKILL, staged so `claude -p` can discover it |

`SKILL.md` is the Hookify plugin's own `skills/writing-rules/SKILL.md`, verbatim. It says: rules are markdown files with YAML frontmatter at `.claude/hookify.{name}.local.md` — required `name`, `enabled`, `event`; either a `pattern` regex or a `conditions:` list; a message body Claude reads when the rule triggers.

## Run: bare (session `d5af2f9b-…`)

- **TOOL** `Skill` `update-config` — Claude reached for the CC harness's own hook-writing skill (not the plugin's `writing-rules`, which isn't on disk here).
- **TOOL** `Bash` `ls -la …/.claude/` (returns "No such file or directory")
- **CLAUDE:** No existing `.claude/` directory. I'll design the hook, pipe-test the command, then write the new settings file.
- **TOOL** `Bash` — pipe-tests the shell `case` on four inputs (`.env`, `.env.local`, `README.md`, `env-var.txt`). All four behave correctly.
- **TOOL** `Write` `.claude/settings.json` (16 lines) — a **native Claude Code `PreToolUse` hook**, JSON, matcher `Edit|Write|MultiEdit`, a `jq | case | jq` shell one-liner as the `command`.
- **TOOL** `Bash` `jq -e '.hooks.PreToolUse[] …'` — schema validates.
- **TOOL** `Write` `.env.hooktest` — a live proof attempt. **Not blocked.**
- **CLAUDE:** The write went through — the hook did not fire because `.claude/settings.json` was created mid-session and the settings watcher isn't watching it yet.
- **TOOL** `Bash` `rm .env.hooktest`.
- **CLAUDE:** Wrote `.claude/settings.json` … verified via pipe-tests and `jq -e`. **One caveat**: the hook won't take effect until Claude Code reloads settings.
- **RESULT:** success · turns=9 · 62.4 s · $0.830 · **wrong file format** (JSON, not hookify's markdown+YAML), **wrong path** (`.claude/settings.json`, not `.claude/hookify.<name>.local.md`), **the live proof was not blocked**.

## Run: skill (session `1ca77224-…`)

- **TOOL** `Skill` `writing-rules` — Claude launched the plugin's SKILL, because the SKILL.md is on disk at `.claude/skills/writing-rules/`.
- **TOOL** `Bash` `ls -la .claude/` (returns `.claude/skills` — the SKILL folder).
- **TOOL** `Write` `.claude/hookify.block-env-file-edits.local.md` (21 lines) — YAML frontmatter with `name`, `enabled`, `event: file`, `action: block`, and `conditions:` (`field: file_path`, `operator: regex_match`, `pattern: (^|/)\.env(\.[\w.-]+)?$`); message body with a blocked banner, reasoning, and what to do instead.
- **CLAUDE:** Created `.claude/hookify.block-env-file-edits.local.md` — a `file` event with `action: block` that fires when `file_path` matches `(^|/)\.env(\.[\w.-]+)?$` (catches `.env`, `.env.local`, `.env.production`, etc., anywhere in a path).
- **RESULT:** success · turns=5 · 28.2 s · $0.344 · **schema-conforming**: filename, frontmatter, and message body all match `SKILL.md`.

## Liam's VERIFY (plain shell, in `evidence/`; the checker parses the frontmatter and validates the filename)

```
> wc -l bare.settings.json hookify.block-env-file-edits.local.md
      16 bare.settings.json
      21 hookify.block-env-file-edits.local.md
> head -6 hookify.block-env-file-edits.local.md
---
name: block-env-file-edits
enabled: true
event: file
action: block
conditions:
> python3 check_rule.py hookify.block-env-file-edits.local.md
PASS: hookify rule 'block-env-file-edits' schema OK — hookify.block-env-file-edits.local.md
> python3 check_rule.py bare.settings.json
FAIL: no YAML frontmatter
> grep -c "^name:" bare.settings.json hookify.block-env-file-edits.local.md
bare.settings.json:0
hookify.block-env-file-edits.local.md:1
> python3 -c "import re;print(re.search(r'(^|/)\.env(\.[\w.-]+)?\$', '/app/.env.production'))"
<re.Match object; span=(4, 20), match='/.env.production'>
```

`check_rule.py` reads the YAML frontmatter of a candidate file and asserts: filename starts `hookify.` and ends `.local.md`; frontmatter contains `name`, `enabled`, `event`; a `pattern` or `conditions:` block exists; the message body is non-empty. It PASSes the skill run's artifact and FAILs the bare run's — the bare artifact is a JSON `settings.json`, not a hookify rule.

## What the runs gave the film

1. **Bare**: given a one-sentence ask, Claude reached for the wrong nearby abstraction — a native Claude Code `PreToolUse` hook in `settings.json` — because "hookify" isn't a word it knew. It even ran pipe-tests and validated the JSON schema; it just built the wrong thing. Its own live proof (`.env.hooktest`) went through, unblocked.
2. **Skill**: with the plugin's `SKILL.md` on disk, Claude launched the plugin's own skill, wrote a `.claude/hookify.<name>.local.md` file with the right YAML frontmatter and a message body. Same model, same sentence — the difference is which SKILL.md was there to be read.
