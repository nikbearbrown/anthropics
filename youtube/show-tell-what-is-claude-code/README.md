# What Is Claude Code?

**What this is.** A show-tell explainer (3 min 42 s) that answers "What is Claude Code?" from Anthropic's own product page. It sets up the naive picture (a smarter autocomplete) and corrects it: Claude Code is an agent you hand a whole task to, and you direct and review. The film keeps one small cast throughout: a grey figure ("you"), a dark Claude Code block with a terracotta spark, the task ticket above it, a kraft tray of code pages, and a test lamp. One step per beat:
- the page's one line ("Hand Claude a bug fix, test, or multi-day migration … steer and review");
- what the work is (the docs: reads your codebase, edits files, runs commands);
- the plan and the clarifying questions;
- the page's own demo, the double-charge checkout bug, told in four beats: two clicks make two charges; it reads 3 files and reproduces the bug; the cause is a new idempotency key per call instead of per session; the fix is one key per session plus disabling the button, `charges.ts +9 −3`;
- agentic search on an unfamiliar codebase;
- issue → code → tests → pull request;
- long runs that follow imports and keep going when a test breaks;
- one engine behind many doors (terminal, editor, desktop, web, phone, Slack);
- your part (decide, answer, review; attributed to Notion's co-founder);
- manual mode versus auto mode;
- how to start (Pro and Max, Team, Enterprise or Console; usage limits; a one-line install; no prices).

Labels only; Liam's voice does the explaining.

**Why.** Bear's order of 2026-09-27: "use the show-tell skill in Brutalist to make a film on this using the Liam persona 'What is Claude code?'", with the product page pasted in (`SOURCE-PASTE.md`).

**Found.** The page and the live docs agree on everything the film uses except one point. The page says auto mode is "the default on Pro, Max, and Team plans", but the live permission-modes doc now says it is the starting mode for terminal and VS Code sessions on current versions. The film therefore describes manual and auto mode from the docs and makes no "default" claim (FACTCHECK row 46, CORRECTED). The double-charge story is narrated as the page's demo, not a real incident, and its sample names are not used.

- Your turn: open Claude Code in a repository you know well and paste `I'm new to this codebase. Can you explain it to me? List the files you read.` Then check two things yourself: open two files it named and see whether its description matches, and have it run the tests and read the result yourself.
- Built with the `show-tell` skill (`brutalist.art/skills/make/show-tell/`). `scenes.py` carries the pasted ISO KIT, the midpoint guard and the continuity carry-overs (`state(k)`). The raw docs the film was checked against are in `sources/`. No cards from the ShowTellCard family; the reason is in SHOTLIST.md.
- Master: `exports/landscape/show-tell-what-is-claude-code.mp4`, 3840×2160, 24 fps, 221.9 s, sha256 be658f14…e9297. All gates PASS (A, B, W, V, GATE T, F, bookend).
- Status: **built, not staged, not published.** Staging (`art post`) and publishing wait for Bear's word.
