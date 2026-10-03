# Source Details — claude-plugins-official--claude-liam-configure

Generated: 2026-09-05T11:09:00

## Reel
- Question: Configure
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-configure/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md
- Name: configure
- Description: Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

## Capabilities To Name On Screen
- Set up the Discord channel — save the bot token and review access policy
- Use when the user pastes a Discord bot token
- asks to configure Discord
- asks "how do I set this up" or "who can reach me," or wants to check channel status.

## Constraints / Failure Modes
- but that's not a substitute for locking the allowlist. Never frame pairing
- Developer Portal → Bot → Reset Token; only shown once
- Delete the DISCORD_BOT_TOKEN= line (or the file if that's the only line)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/channels/discord/.env
- Referenced: $ARGUMENTS
- Referenced: DISCORD_BOT_TOKEN
- Referenced: ~/.claude/channels/discord/access.json
- Referenced: /discord:configure <token>
- Referenced: /discord:access policy allowlist
- Referenced: /discord:access pair <code>
- Referenced: /discord:access allow <id>
- Referenced: mkdir -p ~/.claude/channels/discord
- Referenced: .env

## Source Sections
- Dispatch on arguments
- No args — status and guidance
- <token> — save it
- clear — remove the token
- Implementation notes

## Batch Log Match
- Row: 39
- Canonical path: anthropics/claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-configure/claude-liam-configure.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
