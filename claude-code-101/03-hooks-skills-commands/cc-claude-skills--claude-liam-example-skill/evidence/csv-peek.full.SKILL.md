---
name: csv-peek
description: This skill should be used when the user asks to "peek at a CSV", "inspect columns", "show the first rows", or discusses inspecting a tabular data file. Prints a fixed peek: file, rows, columns, first three data rows.
version: 1.0.0
---

# csv-peek

Fixed inspection format for a CSV file. Always the same shape, so two peeks are directly comparable.

## When This Skill Applies

Any request that asks to look at a CSV file's contents at a glance:
- "peek at data.csv"
- "show me the columns of X.csv"
- "what does sales.csv look like"

## Output shape

Write the peek to `peek.md` in this exact order:

```
## FILE: <name>
## ROWS: <n>
## COLUMNS: <c1, c2, …>
## HEAD:
    <row 1>
    <row 2>
    <row 3>
```

## Rules

- Never invent columns. Read them from the header line.
- Rows count excludes the header.
- HEAD is the first three data rows only. Never a summary, never averages.

## Definition of done

`python3 .claude/skills/csv-peek/check_peek.py peek.md` prints `PASS`.
