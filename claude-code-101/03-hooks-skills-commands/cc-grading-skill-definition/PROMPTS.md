# PROMPTS — cc-grading-skill-definition

Every ask actually sent, verbatim.

## Bare run (Run A)

```
Grade mira.md against the rubric in rubric/rubric.md. Give the student clear feedback with a final grade at the end. Save it to feedback/mira.md.
```

Sent with `claude -p` under the fenced tool allow-list, no `.claude/skills/` present.

## Minimal-skill run (Run B)

Same ask as above. Difference: `scratch/.claude/skills/grading-feedback/SKILL.md` present at 14 lines (`evidence/SKILL-minimal.md`).

## Full-skill run (Run C)

Same ask as above. Difference: `SKILL.md` rewritten to 27 lines (`evidence/SKILL-full.md`), adding `## Never` and `## Definition of done`.

## Durability run (Run D)

```
Grade priya.md against the rubric in rubric/rubric.md. Give the student clear feedback and a final grade. Save it to feedback/priya.md.
```

Same SKILL.md as Run C.

## Viewer's prompt (BHTF)

```
Help me write a SKILL.md for my most-repeated grading task. Ask me for the description line, the workflow, the Never, and the definition of done — one at a time. Then write the file into .claude/skills/grading. Don't grade anything yet.
```

## Invocation (all four)

```
claude -p "<ask>" \
  --output-format stream-json --verbose --max-turns 16 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-<name>.jsonl
```
