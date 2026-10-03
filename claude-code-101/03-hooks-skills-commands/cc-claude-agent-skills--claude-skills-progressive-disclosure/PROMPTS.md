# PROMPTS — cc-claude-agent-skills--claude-skills-progressive-disclosure

All three headless runs used the SAME tool fence and the SAME session flags. Only the ask and the folder differ.

## Common flags

```
claude -p "<ask>" \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  --session-id "<uuid>" < /dev/null > evidence/<run>.jsonl
```

## Run A — bare (no skill in folder)

- **cwd** `/tmp/cc-pd-bare` (README.md + article.md + check.py only — no `.claude/skills/`).
- **ask** `Please summarize article.md into summary.md.`
- **session-id** `b99597fd-88aa-47f9-b49f-92196a15f62e`.

## Run B — skill on natural ask

- **cwd** `/tmp/cc-pd-skill` (full scratch: article.md + check.py + `.claude/skills/exec-summary/{SKILL.md, references/*.md}` + `.claude/skills/csv-summarize/SKILL.md`).
- **ask** `Write an executive summary of article.md into summary.md.`
- **session-id** `7b42e54e-48f5-4c3c-bb27-0a0eafcea1bd`.

## Run C — skill on strict-style ask

- **cwd** `/tmp/cc-pd-strict` (same as Run B's scratch).
- **ask** `Write an executive summary of article.md into summary.md, following our house style precisely.`
- **session-id** `e470fb9f-6d6f-48f4-a69d-e753d78f6ceb`.

## YOUR TURN (BHTF) — the viewer's paste

> Help me write the description for a skill named exec-summary — one sentence, under 20 words, that fires only on asks about summarizing documents in a house style. Then write two conditionals for the body: one that reads a house-style reference on strict-style asks, one that reads a length reference on board or incident asks. Don't build the body yet.
