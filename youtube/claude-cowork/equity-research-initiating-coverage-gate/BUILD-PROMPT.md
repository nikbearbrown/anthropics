# BUILD-PROMPT — It Won't Value What It Hasn't Modeled

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** claude-cowork
**Source:** `anthropics/financial-services/plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md`

## One idea
Initiating coverage is a five-task dependency chain where each task verifies its predecessor's artifact before running, so the report is auditable and never contains invented intermediate values.

## The question (cold open)
An analyst report looks like one document; this workflow treats it as five deliverables where later ones can't start until earlier ones exist on disk. Why hard-gate a report on its own prerequisites?

## Key case
A user asks for the valuation task first; the agent verifies the model file does not exist, refuses to fabricate a placeholder valuation, and sends them back to build the model.

## Acts
1. Company research
2. Financial model
3. Valuation gated on the model
4. Chart generation
5. Report assembly

## Worked example (illustrative)
Task one finds 3 growth drivers and 4 risks; a user tries to skip to charts, the input check finds no valuation tabs and halts; after the valuation fills them, 34 charts render and a six-page initiation assembles.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
