# Source Details — knowledge-work-plugins--claude-liam-build-zoom-team-chat-app

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Build Zoom Team Chat App.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-team-chat-app/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md
- Name: build-zoom-team-chat-app
- Description: Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

## Capabilities To Name On Screen
- App Card Builder - Visual card designer
- ngrok - Local webhook testing
- Postman - API testing

## Constraints / Failure Modes
- > ⚠️ Do NOT use Server-to-Server OAuth - S2S apps don't have the Chatbot/Team Chat feature. Only General App (OAuth) supports chatbots
- ### Required Credentials
- Environment variables - Never hardcode credentials
- Use HTTPS - Required for production webhooks
- [ ] Add required scopes

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: authorization_code
- Referenced: /v2/chat/users/...
- Referenced: client_credentials
- Referenced: /v2/im/chat/messages
- Referenced: https://zoom.us/oauth/authorize
- Referenced: https://zoom.us/oauth/token
- Referenced: /oauth/token
- Referenced: POST https://api.zoom.us/v2/chat/users/me/messages
- Referenced: chat_message:write
- Referenced: chat_channel:read
- Signal: code block: javascript
- Signal: code block: bash

## Source Sections
- Read This First (Critical)
- Quick Links
- Quick Decision: Which API?
- Team Chat API (User-Level)
- Chatbot API (Bot-Level)
- Prerequisites
- System Requirements
- Create Zoom App
- Required Credentials
- Quick Start: Team Chat API

## Batch Log Match
- Row: 122
- Canonical path: anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-team-chat-app/mp4/claude-liam-build-zoom-team-chat-app.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
