# Source Details — claude-plugins-official--claude-liam-build-mcp-app

Generated: 2026-09-05T11:09:00

## Reel
- Question: Build MCP App
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-build-mcp-app/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md
- Name: build-mcp-app
- Description: This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

## Capabilities To Name On Screen
- This skill should be used when the user wants to build an "MCP app"
- add "interactive UI" or "widgets" to an MCP server
- "render components in chat"
- build "MCP UI resources"
- make a tool that shows a "form"

## Constraints / Failure Modes
- | visibility: ["app"] | tool | Hide a widget-only helper tool (e.g. geometry/image fetcher called via callServerTool) from Claude's tool list. |
- Directory submission requires OAuth or authless (none) — static bearer is private-deploy only and blocks listing — plus tool annotations and 3–5 PNG screenshots; see…
- | User must pick from a list Claude can't rank (files, contacts, records) | Picker / table |
- The URI scheme ui:// is convention. The mime type MUST be RESOURCE_MIME_TYPE ("text/html;profile=mcp-app") — this is how the host knows to render it as an interactive…
- The /__EXT_APPS_BUNDLE__/ placeholder gets replaced by the server at startup with the contents of @modelcontextprotocol/ext-apps/app-with-deps — see…
- sendMessage is the typical "user picked something, tell Claude" path. updateModelContext is for state that Claude should know about but shouldn't clutter the chat.…
- What widgets cannot do:
- For local-only widget apps (driving a desktop app, reading local files), swap the transport to StdioServerTransport and package via the build-mcpb skill

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: build-mcp-server
- Referenced: _meta.ui.*
- Referenced: ui://
- Referenced: csp.{connectDomains, resourceDomains, baseUriDomains}
- Referenced: hostContext.safeAreaInsets: {top, right, bottom, left}
- Referenced: references/directory-checklist.md
- Referenced: ../build-mcp-server/references/elicitation.md
- Referenced: build-mcpb
- Referenced: _meta.ui.resourceUri
- Referenced: RESOURCE_MIME_TYPE
- Signal: code block: typescript
- Signal: code block: html
- Signal: code block: bash
- Signal: code block: json
- Signal: code block: ts

## Source Sections
- Claude host specifics
- When a widget beats plain text
- Widgets vs Elicitation — route correctly
- Architecture: two deployment shapes
- Remote MCP app (most common)
- MCPB-packaged MCP app (local + UI)
- How widgets attach to tools
- Widget runtime — the App class
- Scaffold: minimal picker widget
- Design notes that save you a rewrite

## Batch Log Match
- Row: 30
- Canonical path: anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-build-mcp-app/claude-liam-build-mcp-app.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
