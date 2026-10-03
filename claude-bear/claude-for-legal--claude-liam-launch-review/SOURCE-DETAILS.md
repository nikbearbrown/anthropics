# Source Details — claude-for-legal--claude-liam-launch-review

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Launch Review.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-launch-review/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/product-legal/skills/launch-review/SKILL.md
- Name: launch-review
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's…
- ensures it's never skipped even if the PRD is vague
- | 3 | Security | New attack surface, new data at rest, new access patterns? | UI-only, no backend change |
- > No silent supplement. If a research query to the configured legal research tool (Westlaw, CourtListener, regulator sites, or firm platform) returns few or no results…
- > Tool-retrieved citations keep their source tag ([Westlaw], [CourtListener], [regulator site], or the MCP tool name); web-search citations remain [web search — verify]…
- > [platform policy — verify against live docs] — platform rules (Apple App Store Review Guidelines, Google Play policies, Meta / Snap / TikTok creator rules, ESRB / PEGI…
- > Do not proceed past this gate to a "Clear to ship" or "Ship with conditions" call without an explicit yes. "Blocked pending X" and "Needs escalation" do not require…

## Procedure / Sequence
- Get the inputs: - PRD — from file, Drive, or the launch tracker ticket - Spec/design doc — if separate - Marketing plan — if there is…
- Understand what's launching: Before the checklist, answer in plain English: - What does this thing do? - Who uses it — existing users, new users, a…
- Walk the framework: For each category in ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md → Review framework. If the team…
- Calibrate severity: For each finding, check against the calibration table in ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.…
- Assemble the review: Format per ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md → Launch review process → output format.…
- Produce BOTH outputs — the privileged memo AND the redacted ticket comment: ⚠️ Privilege warning: Posting the full privileged memo to a Jira/Linear ticket that is widely shared with engineering…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md
- Referenced: /product-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/product-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: /ai-governance-legal:use-case-triage [feature]
- Referenced: [verify-pinpoint]
- Referenced: ---
- Referenced: ## SAFE TO POST TO TRACKER (non-privileged)
- Signal: code block: markdown

## Source Sections
- Matter context
- Destination check
- Purpose
- Load calibration
- Workflow
- Step 1: Get the inputs
- Step 2: Understand what's launching
- Step 3: Walk the framework
- [N]. [Category]
- Step 4: Calibrate severity

## Batch Log Match
- Row: 288
- Canonical path: anthropics/claude-for-legal/product-legal/skills/launch-review/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-launch-review/mp4/claude-liam-launch-review.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
