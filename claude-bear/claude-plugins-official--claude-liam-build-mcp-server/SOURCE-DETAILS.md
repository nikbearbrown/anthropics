# Source Details — claude-plugins-official--claude-liam-build-mcp-server

Generated: 2026-09-05T11:09:00

## Reel
- Question: Build MCP Server
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-build-mcp-server/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md
- Name: build-mcp-server
- Description: This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

## Capabilities To Name On Screen
- This skill should be used when the user asks to "build an MCP server"
- "create an MCP"
- "make an MCP integration"
- "wrap an API for Claude"
- "expose tools to Claude"

## Constraints / Failure Modes
- Do not start scaffolding until you have answers to the questions in Phase 1. If the user's opening message already answers them, acknowledge that and skip straight to…
- Anyone who installs it → Remote HTTP (strongly preferred) or MCPB (if it must be local)
- Choose this unless the server must touch the user's local machine
- Choose this when the server must run on the user's machine — it reads local files, drives a desktop app, talks to localhost services, or needs OS-level access
- A script launched via npx / uvx on the user's machine. Fine for personal tools and prototypes. Painful to distribute: users need the right runtime, you can't push…
- Recommend this only as a stepping stone. If the user insists, scaffold it but note the MCPB upgrade path
- Tools are one of three server primitives. Most servers start with tools and never need the others, but knowing they exist prevents reinventing wheels:
- Run the pre-submission checklist — read/write tool split, required annotations, name limits, prompt-injection rules. →…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: https://claude.com/docs/llms-full.txt
- Referenced: references/elicitation.md
- Referenced: @modelcontextprotocol/ext-apps
- Referenced: build-mcp-app
- Referenced: references/auth.md
- Referenced: references/deploy-cloudflare-workers.md
- Referenced: references/remote-http-scaffold.md
- Referenced: clientCapabilities.elicitation
- Referenced: build-mcpb
- Referenced: references/tool-design.md

## Source Sections
- Phase 1 — Interrogate the use case
- 1. What does it connect to?
- 2. Who will use it?
- 3. How many distinct actions does it expose?
- 4. Does a tool need mid-call user input or rich display?
- 5. What auth does the upstream service use?
- Phase 2 — Recommend a deployment model
- ⭐ Remote streamable-HTTP MCP server (default recommendation)
- Elicitation (structured input, no UI build)
- MCP app (remote HTTP + interactive UI)

## Batch Log Match
- Row: 31
- Canonical path: anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-build-mcp-server/claude-liam-build-mcp-server.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
