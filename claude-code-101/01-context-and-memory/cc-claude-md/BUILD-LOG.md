# BUILD-LOG — cc-claude-md

cc-explainer · Claude Code 101 · tier `01-context-and-memory`, film 01 · Liam, in for Bear · built 2026-09-08/09 · spine: cold open → THE IDEA → DEFINITIONS → loop → CONDUCT → HUMAN → your-turn.

**Sessions.** Three real headless runs on a tiny `gradebook` repo: `/init` (17-line CLAUDE.md, right about the code, wrong about the machine — `pytest` not installed), the correction (tests rewritten on `unittest`; the file fixed twice; "I was not able to verify… please run one to confirm"), and a fresh session that followed the file to the letter and, blocked from running the file's own `python` command by the session's `python3`-only fence, asked, got no answer, and handed back. Liam's by-hand `sed` to `python3` closes it.

**Compile.** Pass 1: all gates green (Gate V 0/0/0, GATE T PASS, BOOKEND PASS) but frame reads found the `AskUserQuestion` tool row's long arg wrapping over the next line (B03) and B07's stack clipping its last output under the footer. Fixed at the source (short arg; one-line diff stat; display-shortened diff lines), B03/B07 re-rendered, pass 2 green → `final`. Master 298.9 s (4:59), 3840×2160.

**Not published.** TOPOST only via `post`, only on ask.
