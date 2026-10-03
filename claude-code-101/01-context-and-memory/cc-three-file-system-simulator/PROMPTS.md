# PROMPTS — cc-three-file-system-simulator

The two prompts issued to `claude -p` (headless, `--strict-mcp-config`,
`--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls|cat|python3|git|wc)"`,
`--permission-mode acceptEdits`, `--max-turns 16`):

## 1. Bare run (session `91fc369c-…`) — folder: `scratch/` with README.md + ask.txt

```
Build a sorting simulator for a ninth-grade class as index.html.
```

## 2. Three-file run (session `a97af0bb-…`) — folder: the same plus CLAUDE.md + DESIGN.md + PROJECT.md + check.py

```
Build a sorting simulator for a ninth-grade class as index.html.
```

Same one-sentence ask. The only change is the folder's contents. That is the film.

The viewer's prompt (BHTF) is the film's exit hand-off: Claude interviewing them
so *they* write the three files before their next build.
