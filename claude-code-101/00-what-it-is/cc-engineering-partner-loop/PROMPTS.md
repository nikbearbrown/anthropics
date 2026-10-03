# PROMPTS — cc-engineering-partner-loop

The exact `claude -p` invocations that produced `evidence/run-*.jsonl`. Reproducible from the `scratch/` folder at commit `fc0e333`.

## Run 1 — bare (session `64af6ebc-84b7-46b8-ba69-f2f0e9342b5b`)

```bash
claude -p "Fix the failing tests." \
  --session-id "64af6ebc-84b7-46b8-ba69-f2f0e9342b5b" \
  --output-format stream-json --verbose --max-turns 12 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-bare.jsonl
```

- turns=7 · 24.9s · $0.281
- outcome: Read ranges.py → Read test_ranges.py → run tests → Edit → run tests → OK

## Run 2 — partner loop (session `a4c91437-a753-4a6c-8445-ef4158ea0ffc`)

### Turn 1 — PLAN ONLY (Edit/Write withheld)

```bash
claude -p "The oracle is test_ranges.py — read it. Then read ranges.py. Do not edit anything yet. Give me a numbered plan for making the oracle green with the MINIMAL change to parse_range only — nothing outside that function. Show the exact diff you would apply, in \`\`\`diff fences. Stop after the plan." \
  --session-id "a4c91437-a753-4a6c-8445-ef4158ea0ffc" \
  --output-format stream-json --verbose --max-turns 8 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-partner-plan.jsonl
```

- turns=3 · 23.6s · $0.196
- outcome: Read + Read + text-only plan and diff (no edit possible)

### Turn 2 — APPLY (resumed session, Edit re-allowed)

```bash
claude -p "Plan approved. Apply the diff exactly as shown. Then run the oracle (python3 -m unittest test_ranges -v) and report the exit summary line only." \
  --resume "a4c91437-a753-4a6c-8445-ef4158ea0ffc" \
  --output-format stream-json --verbose --max-turns 10 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-partner-apply.jsonl
```

- turns=3 · 12.4s · $0.195
- outcome: Edit + Bash unittest → OK

### Turn 3 — CORRECTION (resumed session, docstring-only)

```bash
claude -p "The docstring is stale — it says '' or reversed is an error, but the code now also raises on extra dashes. Update ONLY the docstring in parse_range to match what the code actually raises. No logic change. Then show me the diff and run the oracle." \
  --resume "a4c91437-a753-4a6c-8445-ef4158ea0ffc" \
  --output-format stream-json --verbose --max-turns 10 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-partner-correct.jsonl
```

- turns=3 · 18.0s · $0.201
- outcome: Edit (docstring only) + Bash git diff + Bash unittest → OK

## Total spend

$0.873 across 4 runs. Kokoro narration is free.
