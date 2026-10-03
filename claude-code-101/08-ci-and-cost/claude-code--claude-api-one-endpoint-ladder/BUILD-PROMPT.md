# BUILD-PROMPT — One Door, Four Tiers

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** claude-code
**Source:** `anthropics/skills/skills/claude-api/SKILL.md`

## One idea
The platform is a tier ladder over one Messages endpoint, single call to tool-use workflow to hosted agent loop to Managed Agents, and choosing right means locating your task on that ladder.

## The question (cold open)
If one endpoint absorbs tools, structured outputs, and server tools, where is the real seam — the line past which you stop controlling the loop?

## Key case
A team believes it needs a tool-use API, a JSON-mode API, and an agents API, and discovers the first two are flags on one request and only the third is a different surface.

## Acts
1. The one endpoint
2. Supporting endpoints orbiting it
3. The workflow tier: you own the loop
4. The agent seam: the four-question test
5. Crossing the wall to Managed Agents

## Worked example (illustrative)
A support tool starts as one classify call, adds tool use to look up an order, moves overnight triage to the Batches endpoint, then fails a cost-of-error test for an end-to-end sandbox refund and graduates to a Managed Agent.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
