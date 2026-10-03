# Source Details — claude-for-legal--claude-liam-integration-management

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Integration Management.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-integration-management/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/integration-management/SKILL.md
- Name: integration-management
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- owner: "finance" # always finance — legal tracks date only
- required_consent: true # true = named in PA Required Consents schedule
- pa_deadline: "[YYYY-MM-DD]" # only for required_consent: true
- assignment_mechanism: "[auto-assign / consent-required / coc-provision / silent]"
- tier: 1 # 1=Required Consent, 2=material+consent-required, 3=CoC, 4=auto-assign
- A full purchase agreement produces the most complete tracker. The PA's Required
- > the post-closing covenants, Required Consents schedule, survival periods, escrow

## Procedure / Sequence
- Load deal context: Read ~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md. If not found: ask for deal…
- Read deal inputs: A full purchase agreement produces the most complete tracker. The PA's Required Consents schedule and post-closing…
- Build the phased workplan: Generate standard workplan items for each phase. Add PA obligations extracted in Step 2. Items inherited from the…
- Get the contract list: Two paths — use whichever applies: Path A: Connected repository > Is your contract repository connected? (Google Drive…
- Determine assignment mechanism: For each contract, classify the assignment mechanism: | Mechanism | Definition | Tier | |---|---|---| |…
- Tier assignment: Show tier 3 separately and prominently. A change of control clause may have already triggered on the close date…
- Generate status entries: For each contract, create a tracker entry with: - All extracted fields (counterparty, type, value, mechanism, tier)…

## Supporting Files And Signals
- Referenced: deal-context.md
- Referenced: integration-tracker.yaml
- Referenced: --init
- Referenced: --contracts
- Referenced: --report
- Referenced: --update
- Referenced: --export
- Referenced: /corporate-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Signal: code block: yaml

## Source Sections
- Matter context
- Purpose
- Tracker file
- Mode 1: Initialize
- Step 1: Load deal context
- Step 2: Read deal inputs
- Step 3: Build the phased workplan
- Mode 2: Contract Assignment
- Step 1: Get the contract list
- Step 2: Determine assignment mechanism

## Batch Log Match
- Row: 266
- Canonical path: anthropics/claude-for-legal/corporate-legal/skills/integration-management/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-integration-management/mp4/claude-liam-integration-management.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
