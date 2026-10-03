# Source Details — skills--claude-liam-doc-coauthoring

Generated: 2026-09-05T11:09:01

## Reel
- Question: Doc Co-Authoring
- Family: skills
- Source sheet: /Users/nik/Documents/books/anthropics/skills/youtube/claude-liam-doc-coauthoring/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/skills/skills/doc-coauthoring/SKILL.md
- Name: doc-coauthoring
- Description: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

## Capabilities To Name On Screen
- Guide users through a structured workflow for co-authoring documentation
- Use when user wants to write documentation
- technical specs
- decision docs
- or similar structured content

## Constraints / Failure Modes
- Use str_replace to make edits (never reprint the whole doc)
- Never use artifacts for brainstorming lists - that's just conversation

## Procedure / Sequence
- Clarifying Questions: Announce work will begin on the [SECTION NAME] section. Ask 5-10 clarifying questions about what should be included…
- Brainstorming: For the [SECTION NAME] section, brainstorm [5-20] things that might be included, depending on the section's complexity.…
- Curation: Ask which points should be kept, removed, or combined. Request brief justifications to help learn priorities for the…
- Gap Check: Based on what they've selected, ask if there's anything important missing for the [SECTION NAME] section.
- Drafting: Use str_replace to replace the placeholder text for this section with the actual drafted content. Announce the [SECTION…
- Iterative Refinement: As user provides feedback: - Use str_replace to make edits (never reprint the whole doc) - If using artifacts: Provide…
- Predict Reader Questions: Announce intention to predict what questions readers might ask when trying to discover this document. Generate 5-10…
- Test with Sub-Agent: Announce that these questions will be tested with a fresh Claude instance (no context from this conversation). For each…

## Supporting Files And Signals
- Referenced: create_file
- Referenced: decision-doc.md
- Referenced: technical-spec.md
- Referenced: str_replace

## Source Sections
- When to Offer This Workflow
- Stage 1: Context Gathering
- Initial Questions
- Info Dumping
- Stage 2: Refinement & Structure
- Step 1: Clarifying Questions
- Step 2: Brainstorming
- Step 3: Curation
- Step 4: Gap Check
- Step 5: Drafting

## Batch Log Match
- Row: 5
- Canonical path: anthropics/skills/skills/doc-coauthoring/SKILL.md
- MP4 path: anthropics/skills/youtube/claude-liam-doc-coauthoring/claude-liam-doc-coauthoring.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
