# Source Details — knowledge-work-plugins--claude-liam-legal-response

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Legal Response.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-legal-response/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/legal-response/SKILL.md
- Name: legal-response
- Description: Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

## Capabilities To Name On Screen
- Generate a response to a common legal inquiry using configured templates
- with built-in escalation checks for situations that shouldn't use a templated reply
- Use when responding to data subject requests
- litigation hold notices
- vendor legal questions

## Constraints / Failure Modes
- Identify required variables (recipient name, dates, specific details)
- ALWAYS requires counsel review (templates are starting points only)
- Stop: Do not generate a templated response
- Offer: Provide a draft for counsel review (clearly marked as "DRAFT - FOR COUNSEL REVIEW ONLY") rather than a final response
- Includes all required legal elements for the response type
- Required customization — Every templated response MUST be customized with:
- Subject: LEGAL HOLD NOTICE - {{matter_name}} - Action Required
- Effective immediately, you must preserve all documents and electronically stored information (ESI) related to:

## Procedure / Sequence
- Identify Inquiry Type: Accept the inquiry type from the user. If the type is ambiguous, show available categories and ask for clarification.
- Load Template: Look for templates in local settings (e.g., legal.local.md or a templates directory). If templates are configured…
- Check Escalation Triggers: Before generating any response, evaluate whether this situation has characteristics that should NOT use a templated…
- Gather Specific Details: Prompt the user for the details needed to customize the response: Data Subject Request: - Requester name and contact…
- Generate Response: Populate the template with the gathered details. Ensure the response: - Uses appropriate tone (professional, clear, not…
- Template Creation (If No Template Exists): If the user wants to create a new template, walk through the Template Creation Guide (see below) and present the…

## Supporting Files And Signals
- Referenced: data-subject-request
- Referenced: discovery-hold
- Referenced: vendor-question
- Referenced: nda-request
- Referenced: privacy-inquiry
- Referenced: legal.local.md
- Referenced: {{requester_name}}
- Referenced: {{response_deadline}}
- Referenced: {{matter_reference}}
- Signal: code block: markdown

## Source Sections
- Invocation
- Workflow
- Step 1: Identify Inquiry Type
- Step 2: Load Template
- Step 3: Check Escalation Triggers
- Step 4: Gather Specific Details
- Step 5: Generate Response
- Step 6: Template Creation (If No Template Exists)
- Response Categories
- 1. Data Subject Requests (DSRs)

## Batch Log Match
- Row: 293
- Canonical path: anthropics/knowledge-work-plugins/legal/skills/legal-response/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-legal-response/mp4/claude-liam-legal-response.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
