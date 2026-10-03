---
description: Review every Python file for bugs by line number
allowed-tools: Read, Glob, Grep
argument-hint: [path]
---

Read every `.py` file at `$ARGUMENTS` (default: this repo). For each file, list bugs and security issues with the file path, line number, and one-sentence explanation. Rank each: HIGH, MEDIUM, LOW.

Look for at least:
- SQL injection or shell injection (string concatenation into `execute()` or `os.system`)
- Mutable default arguments (`def f(x=[])`)
- Bare `except:` that swallows errors
- Off-by-one errors on slice bounds

Output one row per issue as: `path:line — SEV — description`. End with a one-line count.
