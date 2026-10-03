# Source Details — knowledge-work-plugins--claude-liam-build-zoom-video-sdk-app

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Build Zoom Video Sdk App.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-video-sdk-app/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md
- Name: build-zoom-video-sdk-app
- Description: Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

## Capabilities To Name On Screen
- Reference skill for Zoom Video SDK
- Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom…

## Constraints / Failure Modes
- "audio-only room"
- Do not switch to REST meeting endpoints for Video SDK join flows
- // IMPORTANT: getMediaStream() ONLY works AFTER join()
- // Must use .default property
- Get stream: stream = client.getMediaStream() ← ONLY AFTER JOIN
- The SDK is event-driven. You must listen for events and render videos accordingly
- ### Required Events
- | Pre-creation | NOT required | Create meeting via API first |

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: plan-zoom-product
- Referenced: join_url
- Referenced: source.zoom.us
- Referenced: .env
- Referenced: android/
- Referenced: flutter/
- Referenced: ios/
- Referenced: linux/
- Referenced: macos/
- Referenced: react-native/
- Signal: code block: javascript
- Signal: code block: bash
- Signal: code block: html
- Signal: code block: nginx

## Source Sections
- Hard Routing Guardrail (Read First)
- Meeting SDK vs Video SDK
- UI Options (Web)
- Prerequisites
- Quick Start (Web)
- NPM Usage (Bundler like Vite/Webpack)
- CDN Usage (No Bundler)
- ES Module with CDN (Race Condition Fix)
- SDK Lifecycle (CRITICAL ORDER)
- Video Rendering (Event-Driven)

## Batch Log Match
- Row: 123
- Canonical path: anthropics/knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-video-sdk-app/mp4/claude-liam-build-zoom-video-sdk-app.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
