# Source Details — claude-plugins-official--claude-liam-build-mcpb

Generated: 2026-09-05T11:09:00

## Reel
- Question: Build MCPB
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-build-mcpb/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md
- Name: build-mcpb
- Description: This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

## Capabilities To Name On Screen
- This skill should be used when the user wants to "package an MCP server"
- "bundle an MCP"
- "make an MCPB"
- "ship a local MCP server"
- "distribute a local MCP"

## Constraints / Failure Modes
- description: This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local…
- Use MCPB when the server must run on the user's machine — reading local files, driving a desktop app, talking to localhost services, OS-level APIs. If your server only…
- The host reads manifest.json, launches server.mcp_config.command as a stdio MCP server, and pipes messages. From your code's perspective it's identical to a local stdio…
- "required": true
- Vendor dependencies into a subdirectory and prepend it to sys.path in your entry script. Native extensions (numpy, etc.) must be built for each target platform — avoid…
- Unlike mobile app stores, MCPB does NOT enforce permissions. The manifest has no permissions block — the server runs with full user privileges.…
- If your server's only job is hitting a cloud API, stop — that's a remote server wearing an MCPB costume. The user gains nothing from running it locally, and you're…
- Widget authoring is covered in the build-mcp-app skill; it works the same here. The only difference is where the server runs

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: build-mcp-server
- Referenced: manifest.json
- Referenced: server.mcp_config.command
- Referenced: server.type
- Referenced: mcp_config
- Referenced: server.mcp_config
- Referenced: ${__dirname}
- Referenced: ${user_config.<key>}
- Referenced: user_config
- Referenced: references/manifest-schema.md
- Signal: code block: json
- Signal: code block: typescript
- Signal: code block: bash

## Source Sections
- What an MCPB bundle contains
- Manifest
- Server code: same as local stdio
- Build pipeline
- Node
- Python
- MCPB has no sandbox — security is on you
- MCPB + UI widgets
- Testing
- Reference files

## Batch Log Match
- Row: 32
- Canonical path: anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-build-mcpb/claude-liam-build-mcpb.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
