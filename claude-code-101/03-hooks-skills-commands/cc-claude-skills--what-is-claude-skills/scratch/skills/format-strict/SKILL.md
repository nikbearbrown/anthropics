---
name: format-strict
description: Clean up markdown formatting — normalise headings, remove trailing whitespace, ensure a single blank line between blocks.
---

# format-strict

Take a markdown file and normalise its formatting only. Do not change words, meaning, or headings.

## Rules

1. Collapse runs of blank lines to a single blank line.
2. Strip trailing whitespace at end of lines.
3. Ensure exactly one space after `#` in ATX headings.
4. Do not add, remove, or rewrite any prose.
5. Do not touch code fences or their contents.
