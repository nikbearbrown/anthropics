# Source Details — claude-for-legal--claude-liam-demand-received

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Demand Received.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-demand-received/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/demand-received/SKILL.md
- Name: demand-received
- Description: Triage an inbound demand letter — extract fields, cross-check the portfolio, assess merit, present response options with a recommendation, and hand off to matter-intake or demand-intake if escalation is warranted. Use when the user says "we got a demand letter", "triage this demand", or shares an incoming demand to evaluate.

## Capabilities To Name On Screen
- Triage an inbound demand letter — extract fields
- cross-check the portfolio
- assess merit
- present response options with a recommendation
- and hand off to matter-intake or demand-intake if escalation is warranted

## Constraints / Failure Modes
- Legal basis — are the cited provisions/statutes actually applicable? (Flag cites for user verification — do not attempt to validate law autonomously.)
- Tradeoff: settlement-communication posture required — research the applicable rule (FRE 408 or state equivalent) and structure the response so the substance, not just…
- Tradeoff: silence can be used against us in some contexts (e.g., account stated); legal hold still required
- Our internal deadline — when we must decide (often: stated deadline minus 5 business days to draft + approve)
- No silent supplement. If the inbound demand cites rules, cases, or statutes that require verification, and a research query to the configured legal research tool…
- Source attribution. Tag every citation carried into the triage — including the sender's cited authorities, our response-option rationales, and any research pulled for…
- [citations — each inline-flagged with [SME VERIFY: applicability / currency / jurisdiction] — do not rely on any citation here without independent check]

## Procedure / Sequence
- Read the demand: Extract from the incoming: - Sender — entity, signer, counsel (if signed by outside firm) - Recipient — which…
- Portfolio cross-check: Search _log.yaml for: - Direct match — matter with same counterparty (their slug matches the sender) - Type match…
- Merit assessment: Not a legal opinion — a structured read: - Facts — do the alleged facts align with what we know? Where's the…
- Response options: Present 3-4 options with tradeoffs: Option A — substantive response - When: their demand has merit or is at least…
- Deadline triage: - Their stated deadline — note it, but it doesn't bind us - Our internal deadline — when we must decide (often: stated…
- Write triage: Output: ~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[slug]/triage.md. `markdown [WORK-PRODUCT…
- Hand off: Based on recommendation and user confirmation: - Matter creation → hand off to /matter-intake with: counterparty, type…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: . Copy or link incoming to
- Referenced: matter-intake
- Referenced: demand-intake
- Referenced: related_matters
- Referenced: _log.yaml
- Referenced: /demand-intake
- Referenced: type: settlement-response
- Referenced: /legal-hold --issue
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Workflow
- Step 1: Read the demand
- Step 2: Portfolio cross-check
- Step 3: Merit assessment
- Step 4: Response options
- Step 5: Deadline triage
- Step 6: Write triage
- The demand

## Batch Log Match
- Row: 204
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/demand-received/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-demand-received/mp4/claude-liam-demand-received.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
