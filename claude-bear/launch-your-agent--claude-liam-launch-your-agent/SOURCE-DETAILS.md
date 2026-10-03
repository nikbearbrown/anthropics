# Source Details — launch-your-agent--claude-liam-launch-your-agent

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Launch Your Agent.
- Family: launch-your-agent
- Source sheet: /Users/nik/Documents/books/anthropics/launch-your-agent/youtube/claude-liam-launch-your-agent/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/launch-your-agent/.claude/skills/launch-your-agent/SKILL.md
- Name: launch-your-agent
- Description: Help a technical founder build whatever they want on Claude Managed Agents — an internal worker, a piece of their product, a customer-facing agent. Find out what they want to build, scope a v0, launch it in their account, grade it, iterate, and (if it should run on a clock) put it on a scheduled deployment, with everything bigger laid out as v1/v2. Use when a founder says "launch my agent", "/launch-your-agent", "build me a managed agent", or wants to build something on CMA. Keywords: managed agents, CMA, founder, launch, scheduled deployment, outcome rubric.

## Capabilities To Name On Screen
- Help a technical founder build whatever they want on Claude Managed Agents — an internal worker
- a piece of their product
- a customer-facing agent
- Find out what they want to build
- launch it in their account

## Constraints / Failure Modes
- Interview iteratively, and prefer choices over essays. One question cluster at a time, never the whole questionnaire upfront. Whenever the answer space is enumerable…
- Build what they need, scoped into versions. The starting point is one agent, newest Opus-class model, full toolset, cloud env, outcome kickoff with max_iterations: 3…
- Never stop to wait — but give a heads-up early. Do everything that doesn't need their API key — the full build kit, validated payloads, the staged launch sequence…
- Connectors are part of the conversation — and mockable. When an input or output lives in a SaaS (Slack, Gmail, Linear, Notion, GitHub…), name the MCP connector route…
- Key hygiene. Check the shell env for ANTHROPIC_API_KEY first — if it's already there (many founders will have exported it themselves), use it without printing it.…
- Honesty about capability — without underselling. If the idea needs something CMA truly can't do (live phone calls, sub-second real-time reaction), say so plainly and…
- Their problem, their words. Anywhere the founder's problem or goal is written down — the brief, the build sheet problem field, the overview page header — use what they…
- No timings you can't stand behind. Don't promise phase durations, don't ask the founder to estimate how long their task takes, and only quote run lengths you've verified…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: references/examples-bank.md
- Referenced: references/interview.md
- Referenced: max_iterations: 3
- Referenced: .env
- Referenced: always_ask
- Referenced: references/mock-connectors.md
- Referenced: input_schema
- Referenced: ANTHROPIC_API_KEY
- Referenced: ./my-agent/.env
- Referenced: .gitignore

## Source Sections
- Ground rules
- Voice — how to talk to the founder
- Working folder
- Phase 1 — Interview → plan (no key needed)
- Phase 2 — Stage, then launch
- Phase 3 — Grade, iterate, eval
- Phase 4 — Make it run without them
- Fallbacks (move down one rung after two failures on a step; tell them in one sentence)
- References

## Batch Log Match
- Row: 81
- Canonical path: anthropics/launch-your-agent/.claude/skills/launch-your-agent/SKILL.md
- MP4 path: anthropics/launch-your-agent/youtube/claude-liam-launch-your-agent/mp4/claude-liam-launch-your-agent.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
