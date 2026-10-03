# Source Details — skills--claude-liam-claude-api

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude API
- Family: skills
- Source sheet: /Users/nik/Documents/books/anthropics/skills/youtube/claude-liam-claude-api/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/skills/skills/claude-api/SKILL.md
- Name: claude-api
- Description: |-

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- TRIGGER — read BEFORE opening the target file; don't skip because it "looks like a one-liner" — whenever: the prompt names Claude/Anthropic in any form (Claude…
- SKIP only when another provider is being worked on (overrides all triggers): OpenAI/GPT/Gemini/Llama/Mistral/Cohere/Ollama named in the query; OR grep -rE…
- Scan the target file (or, if no target file, the prompt and project) for non-Anthropic provider markers — import openai, from openai, langchain_openai, OpenAI(, gpt-4…
- When the user asks you to add, modify, or implement a Claude feature, your code must call Claude through one of:
- Raw HTTP (curl, requests, fetch, httpx, etc.) — only when the user explicitly asks for cURL/REST/raw HTTP, the project is a shell/cURL project, or the language has no…
- Never mix the two — don't reach for requests/fetch in a Python or TypeScript project just because it feels lighter. Never fall back to OpenAI-compatible shims
- Never guess SDK usage. Function names, class names, namespaces, method signatures, and import paths must come from explicit documentation — either the {lang}/ files in…
- If WebFetch or repository access fails (network restricted, timeouts, clone blocked): do not keep retrying — write code from the patterns and namespace/package tables in…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: @anthropic-ai
- Referenced: claude-*
- Referenced: us.anthropic.*
- Referenced: langchain_openai
- Referenced: gpt-4
- Referenced: gpt-5
- Referenced: agent-openai.py
- Referenced: *-generic.py
- Referenced: @anthropic-ai/sdk
- Referenced: com.anthropic.*
- Signal: code block: python

## Source Sections
- Before You Start
- Output Requirement
- Defaults
- ⚠️ API Drift — Your Training Prior May Be Stale
- Subcommands
- Language Detection
- Language-Specific Feature Support
- Which Surface Should I Use?
- Decision Tree
- Should I Build an Agent?

## Batch Log Match
- Row: 4
- Canonical path: anthropics/skills/skills/claude-api/SKILL.md
- MP4 path: anthropics/skills/youtube/claude-liam-claude-api/claude-liam-claude-api.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
