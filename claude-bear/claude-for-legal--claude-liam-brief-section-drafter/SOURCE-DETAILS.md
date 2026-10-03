# Source Details — claude-for-legal--claude-liam-brief-section-drafter

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Brief Section Drafter.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-brief-section-drafter/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/brief-section-drafter/SKILL.md
- Name: brief-section-drafter
- Description: Draft a brief section in house style, consistent with the case theory — every fact cited, every case checked, every argument tied to the theory. Use when the user says "draft the [section]", "write the statement of facts", "argument section on [issue]", or needs a first draft of a brief section.

## Capabilities To Name On Screen
- Draft a brief section in house style
- consistent with the case theory — every fact cited
- every case checked
- every argument tied to the theory
- Use when the user says "draft the [section]"

## Constraints / Failure Modes
- If the user's jurisdiction includes England & Wales and they're asking for a trial witness statement for the Business & Property Courts (or any CPR-governed proceeding)…
- Verbatim quotes from the record must be verbatim. Never put quotation marks around words attributed to opposing counsel, a witness, the court, or any record document…
- Never fill the gap. An invented quote, even one word, is a fabrication. The reviewer note must flag every [verify exact quote] in the output
- Pinpoint cites must support the whole proposition. If the argument is "opposing counsel said X, Y, and Z" and you're citing one pinpoint, verify the pinpoint supports X…
- Asserting a weak argument without flagging it erodes the lawyer's credibility with the tribunal and creates a candor problem (MR 3.1 — a lawyer must have a basis in law…
- When this draft is cite-checked — by you, by another skill, or by a reviewer running through what you produced — the check must be exhaustive, not selective:
- When source text is unavailable, say "could not check," never "confirmed." A false positive ("this cite is fine" when you couldn't read the source) is worse than…
- Do not proceed on an unintaken matter. Intake is what runs conflicts, sets up matter.md / history.md, and writes the _log.yaml row this skill reads from. Skipping it…

## Procedure / Sequence
- Which section?: | Section | What it does | Inputs needed | |---|---|---| | Statement of facts | Tells the story, in our frame, cited to…
- Theory check: Before writing: what does this section need to accomplish for the theory? - Statement of facts: Frame the story so our…
- Draft in house style: Research the forum's local rules and the judge's standing orders for length, formatting, citation, and filing…
- Cite everything: Every fact → record cite (Bates, depo page:line, exhibit). Every legal proposition → case cite with pincite. Marker…
- Output: Before the brief is filed (the consequential act — this skill drafts, but the gate runs at the filing step regardless…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
- Referenced: CLAUDE.md
- Referenced: [verify against record — Tr. p. __]
- Referenced: ~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml
- Referenced: _log.yaml
- Referenced: /litigation-legal:matter-intake
- Referenced: matter.md
- Referenced: history.md
- Referenced: [CITE NEEDED: specific cite — fact/rule believed but cite not yet pinned]
- Signal: code block: markdown

## Source Sections
- Witness statements for England & Wales — PD 57AC
- Purpose
- Written or oral?
- Record fidelity — quotes and pinpoints
- Candor about weak arguments
- Citation extraction coverage
- Echo vs repeat
- Load context
- Workflow
- Step 1: Which section?

## Batch Log Match
- Row: 113
- Canonical path: anthropics/claude-for-legal/litigation-legal/skills/brief-section-drafter/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-brief-section-drafter/mp4/claude-liam-brief-section-drafter.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
