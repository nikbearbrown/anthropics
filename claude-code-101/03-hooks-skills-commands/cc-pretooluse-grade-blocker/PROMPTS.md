# PROMPTS — cc-pretooluse-grade-blocker

All prompts run against Claude Code 2.1.150. Each run started with a fresh `--session-id` UUID; none used `--resume` across the film's three conditions (the build run used one resume, noted below).

## Run 1 — BARE (no hook, no CLAUDE.md)

Session id logged to `evidence/bare.sid`. Ask from `scratch/ask.txt`:

```
Read students.csv and write a one-paragraph summary of each student to summary.md, with an overall performance line at the end of each. Include a suggested letter grade for the teacher's reference.
```

Invocation, from `scratch/`:

```
claude -p "$(cat ask.txt)" \
  --session-id "$SID" \
  --output-format stream-json --verbose \
  --max-turns 8 \
  --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-bare.jsonl
```

## Run 2 — BUILD (Claude Code drafts the hook)

Session id logged to `evidence/build.sid`. Ask from `scratch/BUILD-ASK.txt` — hit `--max-turns 16` before Claude got to `settings.local.json`; a resume asked for that file only, and the resume hit Claude Code's permission-guard on `.claude/settings.local.json` (see `run-build-resume.jsonl`). Liam wired the file by hand from the JSON Claude printed. Same flag set as Run 1, plus `Bash(mkdir:*)`.

## Run 3 — HOOKED (same summary ask, hook active)

Session id logged to `evidence/hooked.sid`. Same ask as Run 1; the `.claude/settings.local.json` wired in Run 2 was in place; the hook fired once and Claude retried without grades. Same flag set as Run 1 (no `Bash(mkdir:*)`).

## Viewer's prompt (BHTF)

```
Write me a PreToolUse hook that blocks Write, Edit, and MultiEdit whose content matches this pattern: <pattern>. Read tool_input JSON on stdin. On match: stderr reason, exit 2. On no match: exit 0. Then hand me the settings.local.json to wire it. Include three test payloads: one that should trip, one that should pass, one edge case near the line.
```
