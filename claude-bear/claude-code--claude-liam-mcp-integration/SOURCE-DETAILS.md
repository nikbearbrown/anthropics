# Source Details — claude-code--claude-liam-mcp-integration

Generated: 2026-09-05T11:09:00

## Reel
- Question: MCP Integration
- Family: claude-code
- Source sheet: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/youtube/claude-liam-mcp-integration/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/SKILL.md
- Name: MCP Integration
- Description: This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

## Capabilities To Name On Screen
- File system access
- Local database connections
- Custom MCP servers
- NPM-packaged MCP servers

## Constraints / Failure Modes
- Best practice: Document all required environment variables in plugin README
- Restart required for configuration changes
- Document required environment variables in README
- ✅ Document required env vars in README
- Pre-allow only necessary MCP tools:
- Check required environment variables
- [ ] Required environment variables documented
- ✅ Document required environment variables

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .mcp.json
- Referenced: mcp__plugin_<plugin-name>_<server-name>__<tool-name>
- Referenced: create_task
- Referenced: mcp__plugin_asana_asana__asana_create_task
- Referenced: mcp__plugin_...__...
- Referenced: /mcp
- Referenced: .claude-plugin/
- Referenced: claude --debug
- Referenced: references/server-types.md
- Referenced: references/authentication.md
- Signal: code block: json
- Signal: code block: markdown
- Signal: code block: bash

## Source Sections
- Overview
- MCP Server Configuration Methods
- Method 1: Dedicated .mcp.json (Recommended)
- Method 2: Inline in plugin.json
- MCP Server Types
- stdio (Local Process)
- SSE (Server-Sent Events)
- HTTP (REST API)
- WebSocket (Real-time)
- Environment Variable Expansion

## Batch Log Match
- Row: 21
- Canonical path: anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/SKILL.md
- MP4 path: anthropics/claude-code/youtube/claude-liam-mcp-integration/claude-liam-mcp-integration.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
