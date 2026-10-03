# PROMPTS — cc-subagent-context

The two headless `claude -p` invocations this reel reconstructs. Both from the scratch project (`scratch/`), copied to fresh working folders (`scratch-inline/`, `scratch-subagent/`) before each run so the starting state is byte-identical.

## Run 1 — inline

```
cd scratch-inline && claude -p \
  "Read every file in policies/. Then, using what you find there, add a \
   late_penalty(days_late, base_score) function to grader.py that applies \
   the study group's late-submission rules. Add one unittest to \
   test_grader.py covering the one-day-late case. Run the tests to confirm \
   they pass." \
  --output-format stream-json --verbose --max-turns 20 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),\
                  Bash(python3:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-inline.jsonl
```

## Run 2 — subagent

```
cd scratch-subagent && claude -p \
  "Delegate the policy research to a subagent. Step 1: use the Agent tool \
   exactly ONCE (subagent_type: general-purpose) to launch a subagent that \
   reads every file in policies/ and returns ~120 words summarising the \
   study group's late-submission rules. Step 2: with only that summary in \
   hand, edit grader.py to add a late_penalty(days_late, base_score) \
   function and edit test_grader.py to add one unittest for the \
   one-day-late case. Do NOT read any file under policies/ yourself. \
   Run the tests." \
  --output-format stream-json --verbose --max-turns 20 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Agent,Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),\
                  Bash(python3:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-subagent.jsonl
```

## The fix (framed on B06 as the human's move; not run in this reel)

```
cd scratch-subagent && claude -p "$ASK" \
  --allowedTools "Agent,Read,Edit,Bash(python3:*)" \
  --disallowedTools "Read(**/policies/**)"
```

Tool boundary is a human decision. In Claude Code 2.1.150, path-scoped denies stop `Read` on the path; the model may still try `Bash cat` / `find`, so a stricter build removes those Bash sub-commands too.
