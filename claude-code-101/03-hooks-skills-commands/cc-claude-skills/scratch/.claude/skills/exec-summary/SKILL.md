---
name: exec-summary
description: Utility for summarizing documents in a house style.
---

# exec-summary

Write the summary to `summary.md`.

## Format

Four sections, in this order:

- `## What` — one paragraph, the thing itself.
- `## Why it matters` — one paragraph, the consequence.
- `## What's new` — one paragraph, what changed.
- `## What to do` — one paragraph, the action for the reader.

## Rules

- Never a numeric rating, letter grade, or star count.
- Never an emoji.
- Never a "TL;DR" line before the sections.

## Done

Run `python3 check_summary.py summary.md` and it prints `PASS`.
