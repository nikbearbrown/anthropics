# BUILD-PROMPT — Two Objects, One Runtime

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** claude-cowork
**Source:** `anthropics/skills/skills/claude-api/shared/managed-agents-overview.md`

## One idea
Managed Agents is a two-tier object graph — an immutable versioned Agent config that sessions point to — and every advanced feature hangs off that one separation.

## The question (cold open)
If the model, prompt, and tools all live on the Agent, what is left for the Session to be, and why is that leftover the entire runtime?

## Key case
One persisted Agent config (version 4) sits still while three Sessions bud off it, each with its own container, event stream, and pinned version.

## Acts
1. Agent once, Session every run
2. The container and the event stream
3. Vaults and tools on the session
4. Coordinator and context-isolated threads
5. Outcomes and scheduled deployments

## Worked example (illustrative)
A Costco DCF agent is created once; Monday's session pins version 3 and streams 12 events, Tuesday's prompt edit makes version 4 and only the new session gets it; a define_outcome rubric has a grader score the output, feed back one gap, and the agent revises once and passes.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
