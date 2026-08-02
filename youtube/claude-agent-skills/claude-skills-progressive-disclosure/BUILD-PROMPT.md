# BUILD-PROMPT — Unlimited Knowledge, A Hundred Words of Context

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** claude-agent-skills
**Source:** `anthropics/claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md`

## One idea
A skill is three-level lazy loading — metadata always resident, body on trigger, resources on demand — where the trigger is a token-economy decision made from the description alone.

## The question (cold open)
If most of a skill never loads, what decides which tier reveals when, and why does the description field end up doing more work than the instructions?

## Key case
A PDF skill's 100-word description is all that's resident; the moment a user says "rotate this PDF" the body loads and rotate_pdf.py runs without ever entering the context window.

## Acts
1. The anatomy of a skill
2. Tier 1: the always-on metadata
3. Tier 2: the body loads on match
4. Tier 3: three fates for resources
5. Proving the description actually fires

## Worked example (illustrative)
A finance skill carrying a 12k-word schema reference and a dcf.py costs ~100 words idle; asked for a DCF, the ~3k-word body loads, one schema section is grepped (+400 words), and dcf.py runs deterministically adding zero words.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
