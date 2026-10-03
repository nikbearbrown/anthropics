# PROMPTS — cc-writing-rules

The one-sentence ask both runs used, verbatim (`evidence/ask.txt`):

```
Add a hookify rule to this project that BLOCKS any edit or write to a `.env` file. Save it in `.claude/`.
```

## Run 1 — bare (no SKILL.md staged)

Working dir: `scratch/bare/` (contains only `README.md` and `ask.txt`).

```
claude -p "$(cat ask.txt)" \
  --output-format stream-json --verbose --max-turns 12 \
  --permission-mode bypassPermissions \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-bare.jsonl
```

## Run 2 — skill (SKILL.md staged at `.claude/skills/writing-rules/SKILL.md`)

Working dir: `scratch/skill/` (same `README.md` and `ask.txt`, plus the Hookify plugin's SKILL.md placed where Claude will discover it).

```
cp anthropics/claude-code/plugins/hookify/skills/writing-rules/SKILL.md \
   scratch/skill/.claude/skills/writing-rules/SKILL.md
claude -p "$(cat ask.txt)" \
  --output-format stream-json --verbose --max-turns 12 \
  --permission-mode bypassPermissions \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-skill.jsonl
```

Permission mode: `bypassPermissions` because both scratch dirs are outside any real project and both writes target the scratch `.claude/`. `--strict-mcp-config` keeps external MCP servers out of the run so the tool trace is only what the toolchain fenced.
