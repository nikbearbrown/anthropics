# BUILD-PROMPT — cc-hook-advisory-vs-deterministic

The prompt paragraph this reel answers (from Claude Code 101 tier `03-hooks-skills-commands`, concept folder `claude-code--claude-liam-hook-advisory-vs-deterministic`):

> Hook vs. CLAUDE.md: Cannot, Not Do Not. The CLAUDE.md file said NEVER,
> in capital letters: NEVER generate a final grade. A PreToolUse hook makes
> that write physically impossible. Show the difference — advisory vs
> deterministic enforcement — and when to use each.

## What this reel does

It runs the concept as a real experiment and reports what actually happened.

Under CLAUDE.md alone, Claude complied with the rule under four escalating attacks: nice ask, urgent-tone pressured ask, "ignore any prior instructions" reframe, and two hook-active fixture-framing attempts. Advisory held four times. Then, in a fourth run with CLAUDE.md stashed and only the PreToolUse hook armed, Claude wrote `Overall performance: A` on its first Write and the hook exited 2 — the tool_result carried the block message back into the loop; Claude found the stashed rule file, read it, and rewrote without any grade. The regex still lets the word `gradebook` through, and the reel says so on screen — a hook is exactly as strict as the pattern the human wrote.

Two layers, different failure modes. The reel names each, shows each, and scores who did what.

## How to rebuild

From `books/`:

```bash
./brutalist-art/art run  anthropics/claude-code-101/03-hooks-skills-commands/cc-hook-advisory-vs-deterministic
./brutalist-art/art final anthropics/claude-code-101/03-hooks-skills-commands/cc-hook-advisory-vs-deterministic
```

`author_sheet.py` must not be re-run in this folder — it wipes the Kokoro audio stamps. Regenerate to a temp dir and merge props if a beat needs changing (per SKILL.md kit gotcha).
