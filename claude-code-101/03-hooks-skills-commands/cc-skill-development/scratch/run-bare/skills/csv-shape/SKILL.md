---
name: csv-shape
description: This skill should be used whenever a session needs a fast, dependency-free summary of an unfamiliar CSV file — row count, column count, header names, and a per-column dtype guess. Reach for it when a user asks "what's in this CSV", "show me the shape of this CSV", "how many rows and columns does this file have", or "inspect this CSV before I load it". Prefer it over ad-hoc pandas or awk one-liners for quick reconnaissance on any .csv path.
---

# csv-shape

## Purpose

This skill wraps the local helper `csv_shape.py`, a ~30-line standard-library
script that reports the shape of a CSV: the number of data rows, the number of
columns, the header names, and a coarse dtype (`int`, `float`, `bool`, `str`, or
`empty`) inferred from the first non-empty value in each column. It exists so
that quick CSV reconnaissance stays deterministic, reproducible, and free of
pandas overhead when nothing more is actually needed.

## When to invoke

Invoke this skill for questions that are answered by a shape summary alone:

- "What does this CSV look like?"
- "How many rows and columns are in `data.csv`?"
- "What are the column names and rough types?"
- "Is this file empty or malformed at the header?"
- Any triage step before deciding whether a heavier tool (pandas, DuckDB, a
  spreadsheet) is warranted.

Skip this skill when the request is about actual analysis — filtering, joining,
aggregating, plotting, statistics, or per-row inspection. Those tasks belong to
pandas, DuckDB, or a purpose-built script. The role of `csv_shape.py` is
strictly reconnaissance: enough information to plan the next step, and nothing
more.

## How to run it

From the directory that contains `csv_shape.py`, run:

```bash
python3 csv_shape.py <path-to-csv>
```

With no argument the script defaults to `sample.csv` in the current directory.
Output goes to stdout in a stable, greppable format:

```
rows: 3
cols: 4
  name: str
  age: int
  city: str
  active: bool
```

The row count excludes the header line. The dtype for each column is guessed
from the first non-empty value in that column, in this order: `int` → `float` →
`bool` (matching `true`/`false`/`yes`/`no`, case-insensitive) → `str`. Columns
whose first non-empty value cannot be found fall back to `empty`.

## Interpreting the output

A few notes worth keeping in mind when reading the result:

- The dtype is a first-value guess, not a full-column scan. A column reported as
  `int` may still contain floats or strings further down. Treat the label as a
  hint, not a contract.
- `bool` only fires on the literal tokens `true`, `false`, `yes`, `no`
  (case-insensitive). Numeric 0/1 booleans surface as `int`.
- Quoted fields containing commas are handled correctly — the script uses the
  standard `csv` module, not a naive split.
- Ragged rows (rows shorter than the header) are tolerated; missing cells count
  as empty when guessing that column's dtype.

## When the output looks wrong

If the reported shape disagrees with expectations, the usual culprits are:

- **Wrong delimiter.** The script assumes commas. Tab- or semicolon-separated
  files will report a single wide column. Convert or preprocess first.
- **BOM or stray header whitespace.** The first column name may include a
  leading `﻿` on Windows-exported files.
- **Blank leading rows.** Some exports emit a title row before the header; the
  script treats the first row as the header regardless.

In any of these cases, prefer fixing the file (or noting the caveat) over
patching the script — its brevity is the point.

## Boundaries

This skill does not modify files, write output artifacts, or call any network
service. It reads the CSV, prints a summary, and exits. Anything beyond that —
sampling rows, computing statistics, coercing types, writing a cleaned copy —
belongs to a different tool. Keeping the surface small is what makes the
summary trustworthy at a glance.

## Related follow-ups

After running `csv_shape.py`, common next steps include:

- Loading the file into pandas with explicit `dtype=` hints, informed by the
  guessed types.
- Piping the same path into DuckDB for SQL-shaped exploration.
- Opening the file in a spreadsheet or a TUI viewer when a human eyeball is
  the fastest next move.

Chaining those tools is out of scope here; the skill's contract begins and ends
at the shape summary produced by `csv_shape.py`.
