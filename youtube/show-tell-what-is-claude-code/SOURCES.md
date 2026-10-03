# SOURCES — show-tell-what-is-claude-code

**What this is.** The sources behind every claim in the film, and how each was read. **Why.** Bear's order was a paste of the Claude Code product page; the film follows it, and anything beyond it comes from the live docs, attributed aloud ("the docs say"). **Found.** The page and the docs agree on everything the film uses except one line: the page's "auto mode by default on Pro, Max, and Team plans" is out of date against the live permission-modes doc, so the film describes the two modes from the docs and drops the "default" claim (FACTCHECK row 46).

## 1. The product page (primary)
`SOURCE-PASTE.md`: the text of https://claude.com/product/claude-code as Bear pasted it on 2026-09-27, cleaned (tracking parameters, navigation and footer lists removed). sha256 `52591caf…`. Used: the hero line, the plans line (no prices), the product mock (the double-charge session), "What Claude Code can take on" (plan, questions, hours or days; onboarding; issues to PRs; multi-hour refactors), "Meets you where you code", the Notion co-founder's quote, the auto-mode announcement line (attributed, and corrected by §2), the FAQ's first answer, and the install line.

## 2. The live docs (secondary, attributed as "the docs")
Fetched raw with curl on 2026-09-27 (HTTP 200, `text/markdown`), read in full, saved in `sources/`:
- `live_2026-09-27_docs_overview.md` from https://code.claude.com/docs/en/overview.md (sha256 `3d48da81…`): "an agentic coding tool that reads your codebase, edits files, runs commands"; the surfaces (terminal, IDE extensions, desktop app, web); "Each surface connects to the same underlying Claude Code engine"; the install and `cd your-project` / `claude` start; the "run them, and fix any failures" example.
- `live_2026-09-27_docs_permission-modes.md` from https://code.claude.com/docs/en/permission-modes.md (sha256 `796611b4…`): what a permission mode is, Manual mode ("stops and asks you before most actions that edit files, run shell commands, or reach the network"), auto mode ("a second model, the classifier, reviews actions instead of you"), and which mode a session starts in (the correction).

No WebFetch summary was used for any claim.

## Left out, on purpose
Prices and plan tiers, "in a few seconds", announcement dates, fast mode, the Ramp and Intercom quotes, the mock's sample names and footer chips, and the docs' MCP / CLAUDE.md / skills / hooks / subagents / routines sections (see FACTCHECK.md).

## Cast and patterns reused
The ISO KIT and the midpoint guard (`ST`/`guard`, 0.22 s margin) as pasted in `show-tell-claude-on-an-issue/`; its lens, key, check, cursor and PR-card shapes and `build_srt.py`. The grey figure, the Claude Code block with its ports and spark, the task and plan tickets, the codebase tray, the test lamp, the pay button, the gateway, charge slips and coins, the diff card, the doors, the command barrier and the plan tags are new.
