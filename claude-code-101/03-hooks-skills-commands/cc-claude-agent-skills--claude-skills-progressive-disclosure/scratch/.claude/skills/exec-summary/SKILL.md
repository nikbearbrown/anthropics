---
name: exec-summary
description: Summarize a document in the house executive-summary style.
---

# exec-summary

When the user asks for a summary, brief, recap, TL;DR, or wrap of a document,
write `summary.md` in this exact four-section shape, in this order:

```
## What
## Why it matters
## What's new
## What to do
```

Rules: one or two sentences per section, never a bullet list, no emoji,
no exclamation marks.

## When to load the references

The two files under `references/` are on-demand. Do NOT read them for a plain
summary — they are large and cost tokens. Only read them when the ask says so.

- Read `references/house-style.md` **only if** the ask uses the words
  "house style", "style guide", or "strict style".
- Read `references/length.md` **only if** the ask names an audience:
  "board", "director", "incident", "postmortem", or "outage".
- Otherwise write the summary from the four-section shape alone.
