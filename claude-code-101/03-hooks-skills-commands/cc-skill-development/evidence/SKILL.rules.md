---
name: csv-shape
description: This skill should be used when the user wants a fast, dependency-free summary of a CSV file's structure — its row count, column count, column names, and per-column dtype guessed from the first non-empty value. Trigger on requests like "what's in this csv", "shape of this csv", "how many rows and columns", "what are the column types", "inspect this csv", or "describe this csv" — especially when the user has not asked for pandas, statistics, or transformations. Prefer this over writing pandas one-liners for a quick look at an unfamiliar CSV.
---

# csv-shape

Run `csv_shape.py` to print a compact structural summary of any CSV: row count, column count, and each column's inferred dtype (`int`, `float`, `bool`, `str`, or `empty`). The script lives beside this skill folder in the working directory and uses only the Python standard library.

## When to reach for it

Reach for this skill on any first-look question about an unfamiliar CSV — shape, columns, column types — before writing pandas or opening the file by hand. Skip it when the task calls for row-level statistics (means, distributions, group-bys), filtering, joining, or any transformation of the data. Those tasks belong to pandas or a proper analysis workflow.

## How to run it

Invoke the script with the CSV path as its single argument:

```bash
python3 csv_shape.py path/to/file.csv
```

Omitting the argument makes the script fall back to `sample.csv` in the current directory.

Expected output for `sample.csv`:

```
rows: 3
cols: 4
  name: str
  age: int
  city: str
  active: bool
```

The `rows` count excludes the header line. Dtypes come from the first non-empty value in each column, in order — `int` is tried before `float`, and the strings `true`/`false`/`yes`/`no` (case-insensitive) resolve to `bool`.

## Interpreting the output

- `int` / `float` — the first non-empty value parsed as a number. A mixed column may show `int` if the top row happens to be integral.
- `bool` — the first non-empty value was `true`, `false`, `yes`, or `no`.
- `str` — nothing else matched, so treat the column as text.
- `empty` — every value in the column was blank; the script cannot guess further.

## When output looks wrong

For unexpected results — files with no header, ragged rows, quoted numbers, oddly encoded columns, tab-separated data, or a dtype guess that disagrees with the rest of the column — consult `references/troubleshooting.md` in this skill folder. That file catalogs the known edge cases and the workarounds for each.

## What this skill does not do

This skill inspects; it does not transform. For deduplication, filtering, joining, aggregation, or writing a modified CSV, reach for pandas or the standard `csv` module directly. Do not extend `csv_shape.py` with those features — keep it a fast, read-only structural probe.
