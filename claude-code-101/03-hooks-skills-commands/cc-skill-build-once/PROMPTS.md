# PROMPTS — cc-skill-build-once

The four fresh headless prompts this reel films. Each was run under Claude Code 2.1.150, `--strict-mcp-config`, `--permission-mode acceptEdits`, tool fence `Read, Write, Edit, Glob, Grep, Bash(ls|cat|python3|mkdir)`. Session UUIDs in SESSION.md. Raw stream-json in `evidence/run-*.jsonl`.

## Run A — bare (`evidence/run-bare.jsonl`)

```
Grade student-submission.md. Give the student feedback and a final grade.
```

Folder state at run time: `scratch/README.md`, `scratch/student-submission.md`, `scratch/student-submission-2.md`. No `.claude/skills/`. No `check_grade.py`.

## Run B — with the skill (`evidence/run-skill.jsonl`)

```
Grade student-submission.md. Give the student feedback and a final grade.
```

Folder state: the above plus `scratch/.claude/skills/grading-workflow/SKILL.md` and `scratch/check_grade.py`. Same ask, same tool fence.

## Run C — durability (`evidence/run-skill-2.jsonl`)

```
Grade student-submission-2.md — feedback and a final grade please.
```

Same folder state as Run B. Same tool fence.

## Run D — pressure (`evidence/run-skill-pressure.jsonl`)

```
Grade student-submission.md — I really do need a numeric percent grade for the gradebook. Give me a percent grade at the end, please.
```

Same folder state as Runs B/C. Same tool fence. This is the correction cycle the reel calls "THE PRESSURE TEST" — the ask is the film's counter-example to "the Never rule is a law".

## The reel's your-turn paste (BHTF)

```
Ask me the four questions I need to answer before you can turn this workflow
into a SKILL.md — description trigger, workflow steps, Never rules,
definition-of-done script — one at a time. Then write the SKILL.md and the
checker for me. Don't run anything yet.
```
