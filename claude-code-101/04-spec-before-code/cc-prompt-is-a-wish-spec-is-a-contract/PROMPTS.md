# PROMPTS — cc-prompt-is-a-wish-spec-is-a-contract

The three real headless invocations that produced this reel's evidence.

## Wish run (B00, B01)

```
cd scratch/wish
claude -p "Write me a login function." \
  --output-format stream-json --verbose --max-turns 16 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../../evidence/run-wish.jsonl
```

## Spec run (B03, B04)

```
cd scratch/spec
claude -p "Read SPEC.md, then build auth.py per its conditions. Then run python3 -m unittest test_auth.py." \
  --output-format stream-json --verbose --max-turns 16 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../../evidence/run-spec.jsonl
```

## Tests-only middle case (B05)

```
cd scratch/testsonly
claude -p "Write me a login function." \
  --output-format stream-json --verbose --max-turns 16 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../../evidence/run-testsonly.jsonl
```

Model: `claude-opus-4-7[1m]` (Claude Code 2.1.150). All three runs used the same tool fence; `AskUserQuestion` was not in the allowlist, so Claude's clarifying questions in the wish and testsonly runs were denied — the film uses that denial as the pedagogy.

## The viewer's turn (BHTF)

```
Before you write any code, ask me the invariants, the boundary, and the handoff
condition — a command I can run that says you are done. Write my answers into
SPEC.md. Then stop, and wait for me to run it.
```
