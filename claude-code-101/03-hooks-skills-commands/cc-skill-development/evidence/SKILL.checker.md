---
name: csv-shape
description: This skill should be used whenever a CSV file needs a quick structural summary — row count, column count, and per-column inferred data types. Typical triggers include "what shape is this CSV", "describe this csv", "how many rows and columns", "check the schema of a CSV", and "infer the dtypes in this file". Applies to any comma-separated data file the user shares or references by path.
---

# csv-shape

## Purpose

The csv-shape skill inspects a comma-separated-values file and reports its
overall shape: the number of data rows, the number of columns, and an inferred
data type for each column. The goal is to give a fast, reliable first look at
tabular data before any downstream analysis — before joins, before plots,
before modeling — so that surprises about missing headers, ragged rows, or
type coercions surface early.

## When this skill applies

The skill applies whenever a user shares a CSV file (by path, drag-and-drop,
or attachment) and asks a question that boils down to "what is in this
file?" — including but not limited to phrases like "describe this csv",
"how big is this file", "what are the columns", "what shape is this data",
"infer the dtypes", "check the schema", "how many rows are here", or "give me
a summary of this CSV". If the file is not a CSV — for example JSON, Parquet,
or a spreadsheet with multiple sheets — the skill does not apply and the
request should be redirected to a more appropriate tool.

## How to invoke

The skill ships with an executable helper, `csv_shape.py`, that does the real
work. Invoking it is the correct default path — reimplementing the logic
inline is discouraged because the helper already handles empty files, ragged
rows, and mixed types consistently.

Run the helper from the working directory:

```bash
python3 csv_shape.py path/to/file.csv
```

The output has a fixed format so that downstream steps can parse it:

```
rows: <N>
cols: <M>
  <column-name>: <inferred-dtype>
  ...
```

Inferred dtypes are one of: `int`, `float`, `bool`, `str`, or `empty` when
the sampled cell was blank. The helper samples the first non-empty value in
each column, which is a deliberate simplification — good enough for a shape
report, not a full type audit.

## Recommended workflow

1. Locate the CSV path from the request. If the path is ambiguous, list the
   candidate files and confirm which one is intended before running anything.
2. Run `csv_shape.py` against that path.
3. Relay the output verbatim, then add a one-sentence interpretation — for
   example, calling out that a column labeled `id` was inferred as `str`
   because the first sample contained a leading zero, or that a column shows
   `empty` because the sampled row was blank.
4. If the caller asks follow-up questions that go beyond shape (missing-value
   counts, uniqueness, distribution), note that `csv_shape.py` intentionally
   stops at shape and suggest a next step rather than extending the helper.

## What this skill does not do

This skill does not clean data, does not compute summary statistics, does not
detect delimiters other than comma, and does not open Excel or Parquet
files. It also does not stream — very large CSVs will be read fully into
memory by `csv_shape.py`. For files above roughly a gigabyte, warn the caller
before running and suggest sampling the head first.

## Failure modes to expect

- **Empty file** — `csv_shape.py` prints `empty file` and exits non-zero.
  Report that plainly; do not attempt to fabricate a schema.
- **Header-only file** — the row count will be `0` and every column will be
  reported as `empty`. That is correct behavior.
- **Ragged rows** — rows shorter than the header are tolerated silently;
  columns whose sampled position was missing fall back to `empty`. Flag this
  in the interpretation sentence if it seems relevant.
- **Non-UTF-8 encoding** — Python's default open will raise. If that happens,
  report the exception rather than silently retrying with a guessed encoding.

## Example

Given `sample.csv` in the working directory:

```
id,name,active,score
1,Ada,true,9.5
2,Grace,false,8.7
```

Running `python3 csv_shape.py sample.csv` produces:

```
rows: 2
cols: 4
  id: int
  name: str
  active: bool
  score: float
```

That is the canonical happy-path output shape callers should expect from any
successful invocation of this skill.
