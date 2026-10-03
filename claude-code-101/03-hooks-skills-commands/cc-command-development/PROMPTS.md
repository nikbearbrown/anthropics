# PROMPTS — cc-command-development

The only prompts in this reel are typed by Liam or shown on-screen in Claude Code composer chrome. No image, video, or audio prompts were sent to a paid service. Every asset is Kokoro (`am_onyx`) or a component render.

## Session prompts (typed by Liam)

- `B00` — `/review-v1`
- `B03` — `/review-v2`
- `B01` VERIFY (`!` bang commands, plain shell):
  - `wc -l out-v1.md`
  - `grep -c '🔴' out-v1.md`
  - `grep -c '```' out-v1.md`
  - `tail -1 out-v1.md`
- `B04` VERIFY:
  - `wc -l out-v2.md`
  - `grep -c '🔴' out-v2.md`
  - `grep -c '```' out-v2.md`
  - `tail -1 out-v2.md`

## Composer prompt shown in BHTF

```
Take one slash command in .claude/commands/ (or write your first) and rewrite it
as a spec: frontmatter with description, argument-hint, allowed-tools; then an
imperative body saying what to read, what to look for, and the exact shape of
the output. Test it on one file. Show me the diff.
```
