# BUILD-PROMPT — cc-command-development

Reproduce this reel by re-running its two headless sessions and re-authoring the sheet.

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code-101/03-hooks-skills-commands/cc-command-development/scratch

# Fresh scratch state (this repo's git is already initialised with one commit)

# Run v1 (message-to-user command)
claude -p "/review-v1" \
  --output-format stream-json --verbose --max-turns 12 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(wc:*),Bash(git:*)" \
  < /dev/null > ../evidence/run-v1.jsonl

# Run v2 (imperative command)
claude -p "/review-v2" \
  --output-format stream-json --verbose --max-turns 12 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(wc:*),Bash(git:*)" \
  < /dev/null > ../evidence/run-v2.jsonl

# Author the beat sheet
cd ..
python3 author_sheet.py

# Audio — Kokoro (free, local), Liam (am_onyx), every beat
python3 /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code-101/03-hooks-skills-commands/cc-command-development

# Compile
cd /Users/bear/Documents/CoWork/bear-textbooks/books
./brutalist-art/art run   anthropics/claude-code-101/03-hooks-skills-commands/cc-command-development
./brutalist-art/art final anthropics/claude-code-101/03-hooks-skills-commands/cc-command-development
```

**Never publish. Master stays in the reel folder.**
