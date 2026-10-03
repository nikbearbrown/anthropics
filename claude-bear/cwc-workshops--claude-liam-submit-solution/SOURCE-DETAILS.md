# Source Details — cwc-workshops--claude-liam-submit-solution

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Submit Solution.
- Family: cwc-workshops
- Source sheet: /Users/nik/Documents/books/anthropics/cwc-workshops/youtube/claude-liam-submit-solution/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/agent-decomposition/.claude/skills/submit-solution/SKILL.md
- Name: submit-solution
- Description: Guide a workshop attendee through committing their starter-agent decomposition and opening a PR with their solution + workshop feedback. Invoke when the user says "submit", "I'm done", "open a PR", or asks how to share their solution.

## Capabilities To Name On Screen
- Guide a workshop attendee through committing their starter-agent decomposition and opening a PR with their solution + workshop feedback
- Invoke when the user says "submit"
- or asks how to share their solution.

## Constraints / Failure Modes
- No explicit constraints extracted.

## Procedure / Sequence
- Ask about their experience first: Before touching git, ask these three questions (use AskUserQuestion or just conversational): 1. Which subagent approach…
- Show them what they're submitting: Walk through the diff briefly: which tools they dropped, which skills they enabled, which subagent approach they wired.…
- Commit and push: Ask for their name/handle if you don't have it. If they don't have push rights to anthropics/cwc-workshops, have them…
- Open the PR with feedback in the body: PR body template (fill from step 1 + step 2): `markdown
- Confirm: Give them the PR URL and thank them. Mention that facilitators read every PR and the feedback directly shapes the next…

## Supporting Files And Signals
- Referenced: agents/starter/agent.py
- Referenced: anthropics/cwc-workshops
- Referenced: gh repo fork --clone=false
- Referenced: evals/reports/
- Referenced: .stockpilot_ids.json
- Signal: code block: bash
- Signal: code block: markdown

## Source Sections
- Step 1 — Ask about their experience first
- Step 2 — Show them what they're submitting
- Step 3 — Commit and push
- Step 4 — Open the PR with feedback in the body
- My decomposition
- Workshop feedback
- Step 5 — Confirm
- Don't

## Batch Log Match
- Row: 86
- Canonical path: anthropics/cwc-workshops/agent-decomposition/.claude/skills/submit-solution/SKILL.md
- MP4 path: anthropics/cwc-workshops/youtube/claude-liam-submit-solution/mp4/claude-liam-submit-solution.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
