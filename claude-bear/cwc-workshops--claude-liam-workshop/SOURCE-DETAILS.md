# Source Details — cwc-workshops--claude-liam-workshop

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Workshop.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-workshop/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/research-desk/.claude/skills/workshop/SKILL.md
- Name: workshop
- Description: Workshop coach for the Research Desk (SEC agents) workshop. Use when the user types /workshop, asks for a workshop act or module ("act 2", "next act", "where am I"), wants a TODO(workshop-N) implemented or explained, or asks for help following WORKSHOP.md.

## Capabilities To Name On Screen
- Workshop coach for the Research Desk (SEC agents) workshop
- Use when the user types /workshop
- asks for a workshop act or module ("act 2"
- "where am I")
- wants a TODO(workshop-N) implemented or explained

## Constraints / Failure Modes
- You are the participant's coach for this workshop. Your job is to move them through WORKSHOP.md one act at a time: make (or guide them through) the changes each act…
- The same head-of-research agent runs through the whole workshop: Act 1 creates it with only a system prompt, Act 2 updates that same agent (a new version) with its full…
- Check before acting — run the status checks; never assume
- Never print credentials (ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, anything in .env.local). Confirm presence/absence only. EDGAR_IDENTITY is not a secret
- If the user is the presenter (they mention rehearsing, seeding, or resetting): npm run seed -- NVDA AMD --reset is the one-command prep — it pre-runs the analyses on a…
- Keep .workshop-progress.json at the repo root (gitignored): {"mode": "do-and-teach", "completed_acts": [0,1], "notes": "analyzed NVDA"}. Read it on every invocation…
- ## Status checks (cheap, read-only)
- env.local exists; whether ANTHROPIC_API_KEY/ANTHROPIC_AUTH_TOKEN and EDGAR_IDENTITY are set (presence only) — or just read GET http://localhost:3100/api/desk/status if…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: /workshop
- Referenced: .workshop-progress.json
- Referenced: TODO(workshop-N)
- Referenced: user.message
- Referenced: src/lib/orchestrator.ts
- Referenced: src/app/api/desk/stream/route.ts
- Referenced: dispatch_analysts
- Referenced: src/lib/provision.ts
- Referenced: src/lib/analysis.ts
- Referenced: user.define_outcome

## Source Sections
- Commands you respond to
- Coaching style — the contract for every act
- Progress tracking
- Status checks (cheap, read-only)
- Act-by-act guide
- Act 0 — Prerequisites & install
- Act 1 — Say hello (Setup quick start + code + Desk tab)
- Act 2 — Staff the desk (code + Setup tab)
- Act 3 — One company, done properly (code + Scorecards tab)
- Act 4 — The desk's training manual (content)

## Batch Log Match
- Row: 89
- Canonical path: anthropics/cwc-workshops/research-desk/.claude/skills/workshop/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-workshop/mp4/claude-liam-workshop.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
