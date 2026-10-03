# Source Details — healthcare--claude-liam-clinical-trial-protocol-skill

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Clinical Trial Protocol Skill.
- Family: healthcare
- Source sheet: /Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-clinical-trial-protocol-skill/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/healthcare/plugins/healthcare/skills/clinical-trial-protocol/SKILL.md
- Name: clinical-trial-protocol-skill
- Description: Generate clinical trial protocols for medical devices or drugs. This skill should be used when users say "Create a clinical trial protocol", "Generate protocol for [device/drug]", "Help me design a clinical study", "Research similar trials for [intervention]", or when developing FDA submission documentation for investigational products.

## Capabilities To Name On Screen
- Generate clinical trial protocols for medical devices or drugs
- This skill should be used when users say "Create a clinical trial protocol"
- "Generate protocol for [device/drug]"
- "Help me design a clinical study"
- "Research similar trials for [intervention]"

## Constraints / Failure Modes
- Do NOT pre-read subskill files - Subskills are loaded on-demand only when their step executes
- Subskills should only load when actually needed during execution
- 🔬 Research Only Mode (Steps 0-1):
- ### 1. clinical trials MCP Server (Required)
- ### 4. Python Dependencies (Required for Step 2)
- 🔬 Research Only Mode:
- Select "Research Only" from the main menu
- 🔬 Research Only - Run clinical research analysis (Steps 0-1)

## Procedure / Sequence
- Select "Research Only" from the main menu
- Provide intervention information
- Receive comprehensive research summary as formatted .md artifact
- Option to continue with full protocol generation or exit
- Select "Full Protocol" from the main menu
- Guide you through all steps sequentially (Steps 0-5)
- Pause after Step 4 to review the draft protocol
- Generate the final protocol document when ready

## Supporting Files And Signals
- Referenced: waypoints/
- Referenced: intervention_metadata.json
- Referenced: initial_context
- Referenced: references/
- Referenced: .mcpb
- Referenced: search_clinical_trials
- Referenced: get_trial_details
- Referenced: .md
- Referenced: assets/
- Referenced: execution_mode = "research_only"
- Signal: code block: bash
- Signal: code block: markdown

## Source Sections
- ⚠️ EXECUTION CONTROL - READ THIS FIRST
- Overview
- What This Skill Does
- Architecture
- Waypoint-Based Design
- Modular Subskill Steps
- Utility Scripts
- Prerequisites
- 1. clinical trials MCP Server (Required)
- 2. FDA Database Access (Built-in)

## Batch Log Match
- Row: 150
- Canonical path: anthropics/healthcare/plugins/healthcare/skills/clinical-trial-protocol/SKILL.md
- MP4 path: anthropics/healthcare/youtube/claude-liam-clinical-trial-protocol-skill/mp4/claude-liam-clinical-trial-protocol-skill.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
