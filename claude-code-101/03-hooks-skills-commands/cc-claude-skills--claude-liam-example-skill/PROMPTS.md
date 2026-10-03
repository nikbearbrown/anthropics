# PROMPTS — cc-claude-skills--claude-liam-example-skill

The ONE headless prompt used across all three runs (`evidence/ask.txt`):

```
Peek at sales.csv and write the result to peek.md.
```

Invocation (exact command, with the run-specific session id):

```
claude -p "$ASK" \
  --session-id "<uuid>" \
  --output-format stream-json --verbose \
  --max-turns 16 \
  --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*),Bash(grep:*)" \
  < /dev/null > "$REEL/evidence/run-<label>.jsonl"
```

Sessions (`evidence/run-*.jsonl`):

| Label | UUID | Setup |
|---|---|---|
| bare | `46660809-ee64-4a11-b5cc-2df31caa82fd` | scratch/ with only README.md + sales.csv |
| full | `caf097fb-8b1e-44e6-b1b7-e03ad9fb4036` | scratch/.claude/skills/csv-peek/SKILL.md (40 lines) + check_peek.py |
| bare-front | `670b0d5b-0213-4cf5-82e9-7d5ddf254650` | scratch/.claude/skills/csv-peek/SKILL.md (4 lines, frontmatter only) + check_peek.py |

Each `scratch/` was copied into a fresh `/tmp/cc-example-skill.XXXXXX` before the run so no parent `CLAUDE.md` reached the session.

The `Skill()` tool result is the router's signature. `grep -c '"name":"Skill"'` on each JSONL:

```
run-bare.jsonl:0
run-full.jsonl:1
run-bare-front.jsonl:1
```
