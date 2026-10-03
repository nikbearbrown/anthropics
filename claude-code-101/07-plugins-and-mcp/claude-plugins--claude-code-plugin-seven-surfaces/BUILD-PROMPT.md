# BUILD-PROMPT — Seven Surfaces, One Manifest

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** claude-plugins
**Source:** `anthropics/claude-code/plugins/plugin-dev`

## One idea
A plugin manifest bundles up to seven distinct extension surfaces, each with a different trigger model and blast radius, and knowing which slot a capability belongs in is the craft.

## The question (cold open)
If commands, skills, agents, hooks, and MCP servers all extend Claude, what makes them different slots instead of one, and when does a capability belong in each?

## Key case
The plugin-dev toolkit is itself a plugin, shipping skills, agents, and a /create-plugin command — proving the anatomy by being made of it.

## Acts
1. The manifest and structure
2. Two ways to trigger: commands vs skills
3. Agents: an isolated context window
4. Hooks: deterministic lifecycle interception
5. MCP, settings, and the build workflow

## Worked example (illustrative)
A db-migrations plugin ships one /migrate command, one skill that auto-triggers on "add a column", one migration-reviewer agent with a clean context, one PreToolUse hook that blocks a DROP TABLE, and one MCP server exposing the staging database.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
