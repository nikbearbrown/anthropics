# Source Details — knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Build Zoom Meeting Sdk App.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-meeting-sdk-app/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md
- Name: build-zoom-meeting-sdk-app
- Description: Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, auth and join flows, waiting room issues, or meeting bot patterns.

## Capabilities To Name On Screen
- Reference skill for Zoom Meeting SDK
- Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins
- platform-specific SDK behavior
- auth and join flows
- waiting room issues

## Constraints / Failure Modes
- Do not switch to REST-only meeting link flow unless the user explicitly asks for meeting resource management or browser join_url links
- ### 2. Backend Required for Production
- Never expose SDK Secret in client code. Generate signatures server-side:

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: build-zoom-meeting-app
- Referenced: build-zoom-bot
- Referenced: join_url
- Referenced: zoom-meeting-{ver}.min.js
- Referenced: @zoom/meetingsdk
- Referenced: .env
- Referenced: android/
- Referenced: electron/
- Referenced: ios/
- Referenced: linux/
- Signal: code block: html
- Signal: code block: javascript
- Signal: code block: css

## Source Sections
- Hard Routing Guardrail (Read First)
- Prerequisites
- Quick Start (Web - Client View via CDN)
- Critical Notes (Web)
- 1. CDN vs npm - Different APIs!
- 2. Backend Required for Production
- 3. CSS Conflicts - Avoid Global Resets
- 4. Client View Toolbar Cropping Fix
- 5. Hide Your App When Meeting Starts
- UI Options (Web)

## Batch Log Match
- Row: 119
- Canonical path: anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-meeting-sdk-app/mp4/claude-liam-build-zoom-meeting-sdk-app.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
