# Source Details — claude-for-legal--claude-liam-claim-chart

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Claim Chart.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-claim-chart/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/claim-chart/SKILL.md
- Name: claim-chart
- Description: Build or review an element chart — a patent claim chart (infringement, invalidity, or review) or a civil element chart for any cause of action or defense — with every cell pin-cited and gap detection as the priority output. Use when the user asks for a claim chart, element chart, proof chart, infringement or invalidity contention, element-by-element mapping, or asks "what are we missing to prove [claim]".

## Capabilities To Name On Screen
- Build or review an element chart — a patent claim chart (infringement
- or review) or a civil element chart for any cause of action or defense — with every cell pin-cited and gap detection as the priority output
- Use when the user asks for a claim chart
- element chart
- infringement or invalidity contention

## Constraints / Failure Modes
- England & Wales (CPR 31.22): Documents obtained through disclosure are subject to the implied undertaking — you may only use them for the purpose of the proceedings in…
- Put this at the top of every output. Do not drop it. Do not soften it
- > This chart is a draft for attorney analysis and verification, not a filed contention, an MSJ brief, an opening statement, or a legal opinion. Every mapping is a lead…
- Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills use practice-level…
- Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the _log.yaml row this skill reads from
- Dependent claims — reference parent; chart only the additional limitations. Execute, don't gesture. If asserted claims include dependents, produce the actual…
- | doe | Equivalent (function-way-result or insubstantial differences) | Infringement only |
- | anticipation | Every element in a single reference, arranged as claimed (Net MoneyIN, Inc. v. VeriSign, Inc., 545 F.3d 1359 (Fed. Cir. 2008)) | Invalidity only |

## Procedure / Sequence
- Parse the claims: Parse asserted independent claims into numbered elements. Handle: - Preamble. Note whether it's limiting — a question…
- Claim construction check: Flag disputed terms: - Coined terms or terms defined in the spec - Terms with prosecution history (amendments…
- Map: For each element, for each target: 1. Find evidence. Accused product: documentation, manuals, data sheets, source code…
- Dependent claims — execute, don't gesture: For each asserted dependent claim, produce an actual row (or set of rows) charting the additional limitation(s) against…
- 5: DOE supplements — execute, don't gesture: For every element charted as literal where the accused feature is structurally similar but not literally identical — or…
- Indirect, divided, willfulness (infringement only): Flag, don't opine: - Induced (§271(b)) — Commil USA, LLC v. Cisco Systems, Inc., 575 U.S. 632 (2015); Global-Tech…
- Invalidity thresholds (invalidity only): For §102: every element in a single reference. Partial across references is §103. For §103: primary reference +…
- (review sub-mode): Audit: For each row: is the mapping supported? Is the pin cite accurate? Is the element fully accounted for? What's the…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: matter.md
- Referenced: --patent
- Referenced: --infringement
- Referenced: --invalidity
- Referenced: --review
- Referenced: --civil
- Referenced: references/element-templates.md
- Referenced: _sources
- Referenced: claim-charts/
- Signal: code block: markdown

## Source Sections
- Disclosed-document use restrictions
- A CHART IS A DRAFT, NOT A FINDING OR A CONTENTION
- Matter context
- Load context
- Provisional mode
- Mode selection
- Sub-modes
- Additional patent-mode intake
- Patent-mode workflow
- Step 1: Parse the claims

## Batch Log Match
- Row: 141
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/claim-chart/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-claim-chart/mp4/claude-liam-claim-chart.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
