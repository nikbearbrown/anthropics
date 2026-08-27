# CC-COWORK-SIM-SCAN — beat sheets buildable with the Claude Code / Cowork simulators

Scanned: 769 reels under `books/anthropics/youtube/<topic>/<slug>/beat_sheet.json` · 2026-08-09

**Method.** Per reel: bookend beats (ClaudeComposerAsk / Verdict / TitleOutro / SegmentCard) counted separately; body beats scored on narration keywords for the Claude Code simulator (terminal, tool call, diff, plan mode, subagent, slash, context window…) vs the Cowork simulator (composer, task stream, connector, side rail, settings, artifact…). Score ≈ fraction of body carryable by the kits. `slt` = beats not yet filled (build.status != VIDEO).

**The finding that matters: NO reel in this tree uses any CC* or Cowork* scene yet.** The kits (brutalist-art `runtime/remotion/src/scenes/CC*`, `Cowork*`, per `CC-TEMPLATES.md`/`CODEX-TEMPLATES.md`) post-date these beat sheets. Every high scorer below is a slate-heavy sheet whose narration already describes interface actions — the exact beats the simulators exist to fill. Standard intro/outro is already in place on the scaffolded sheets (ClaudeComposerAsk cold open, verdict, Your Turn, title outro).

**Dedupe warning.** Most concepts exist 2–5× (base + `claude-liam-*` + `nbb-*` + `cowork-*` variants). Build ONE per concept (claude-liam variant recommended — free Kokoro), and let brand_variant.py derive the rest.

## Tier A — build first (score ≥80, one row per CONCEPT; variants listed)

| Concept | Topic | Kit | Score | Slates | Variants on disk |
|---|---|---|---|---|---|
| feature-list-checkpoint-persistence | claude-basics | CC | 100 | 11/11 | 1 |
| command-development | claude-code | CC | 100 | 1/7 | 1 |
| hook-development | claude-code | CC | 100 | 1/7 | 1 |
| mcp-integration | claude-mcp-connectors | CC | 100 | 1/7 | 3 |
| claude-automation-recommender | claude-plugins | CC | 100 | 1/7 | 1 |
| claude-md-improver | claude-plugins | CC | 100 | 1/7 | 1 |
| config-guide | claude-plugins | CW | 100 | 1/7 | 1 |
| debug-plugins | claude-plugins | CC | 100 | 1/7 | 1 |
| google-drive-api | claude-plugins | CW | 100 | 1/7 | 1 |
| playground | claude-plugins | CC | 100 | 1/7 | 1 |
| plugin-settings | claude-plugins | CC | 100 | 1/7 | 2 |
| plugin-structure | claude-plugins | CC | 100 | 1/7 | 3 |
| project-artifact | claude-plugins | CW | 100 | 1/7 | 1 |
| example-skill | claude-skills | CC | 100 | 1/7 | 1 |
| pdf | claude-skills | CC | 100 | 1/7 | 1 |
| web-artifacts-builder | claude-skills | CW | 100 | 1/7 | 1 |
| access-ladder-explained | claude-cowork | CW | 98 | 11/11 | 3 |
| cowork-access-ladder | claude-cowork | CW | 98 | 11/11 | 2 |
| access-ladder | claude-cowork | CW | 98 | 11/11 | 1 |
| independent-verification-protocol | behind-the-model | CW | 96 | 11/16 | 3 |
| writer-reviewer-pattern | claude-code | CC | 88 | 10/10 | 3 |
| plan-mode-interruption | claude-code | CC | 86 | 13/13 | 3 |
| math-olympiad | claude-for-education | CW | 83 | 1/7 | 1 |
| command-development | claude-plugins | CC | 83 | 1/7 | 1 |
| example-command | claude-plugins | CC | 83 | 1/7 | 1 |
| pptx | claude-skills | CC | 83 | 1/7 | 1 |
| skill-creator | claude-skills | CC | 83 | 1/7 | 1 |
| claude-for-excel | claude-cowork | CW | 81 | 14/14 | 1 |

## Tier B — strong candidates (60–79)

| Concept | Topic | Kit | Score | Slates | Variants |
|---|---|---|---|---|---|
| stop-prompting-claude | claude-cowork | CW | 78 | 15/15 | 1 |
| vox-subagent-context | claude-code | CC | 74 | 14/14 | 2 |
| subagent-context | claude-code | CC | 74 | 6/14 | 1 |
| seven-field-brief | claude-cowork | CW | 72 | 12/12 | 3 |
| slash-context-window-check | claude-code | CC | 70 | 13/13 | 3 |
| nondelegation-checklist | claude-cowork | CW | 70 | 11/11 | 3 |
| plan-review-checklist | claude-cowork | CW | 70 | 11/11 | 3 |
| synthesis-vs-deciding | claude-cowork | CW | 70 | 11/11 | 3 |
| claude-connectors | claude-cowork | CW | 68 | 15/15 | 1 |
| engineering-partner-loop | claude-code | CC | 66 | 9/13 | 2 |
| be-good-at-claude | claude-cowork | CW | 65 | 15/15 | 1 |
| privacy-classification-scanner | claude-cowork | CW | 65 | 10/14 | 3 |
| vox-agentic-irreversible | claude-prompting | CW | 64 | 19/19 | 2 |
| agentic-irreversible | claude-prompting | CW | 64 | 19/19 | 1 |
| silent-omission-signal | behind-the-model | CW | 63 | 10/14 | 1 |
| build-mcpb | claude-mcp-connectors | CW | 63 | 1/7 | 1 |
| risk-tiered-verification | behind-the-model | CW | 62 | 11/16 | 3 |
| hook-advisory-vs-deterministic | claude-code | CC | 62 | 10/10 | 2 |
| tests-pass-user-fails | claude-code | CC | 60 | 14/14 | 2 |
| vox-agentic-loop | claude-code | CC | 60 | 20/20 | 1 |
| cowork-task-packet | claude-cowork | CW | 60 | 11/11 | 2 |
| extraction-schema-first | claude-cowork | CW | 60 | 11/11 | 3 |
| task-packet | claude-cowork | CW | 60 | 11/11 | 1 |
| claude-quickstarts-agent-fresh-memory-every-session | claude-prompting | CC | 60 | 11/11 | 1 |

## Topic rollup (concepts scoring ≥60, deduped)

- **claude-cowork**: 15 concepts
- **claude-code**: 11 concepts
- **claude-plugins**: 11 concepts
- **claude-skills**: 5 concepts
- **behind-the-model**: 3 concepts
- **claude-prompting**: 3 concepts
- **claude-mcp-connectors**: 2 concepts
- **claude-basics**: 1 concepts
- **claude-for-education**: 1 concepts

## How to fill (the conversion recipe)

1. Pick a Tier-A concept, ONE variant (claude-liam).
2. Map each slated body beat by what its narration DESCRIBES: a command running → `CCToolCall`/`CCSession`; a change landing → `CCDiff`; plan mode → `CCPlanCard`; thinking/status → `CCStatusVerb` (mascot 'think'); a whole coding session → `CCSession` with `mascot:'auto'`; a Cowork task → `CoworkTaskView`/`CoworkComposer`; settings/toggles → `CoworkSettings`/`CoworkMenu`; progress/files → `CoworkSideRail`. Bookends stay as-is.
3. Strings law: everything the chrome says must be verbatim product strings (see CC-TEMPLATES.md editorial law).
4. Run the standard flow: audio (Kokoro) → remotion_scenes.py → compile → VISUAL QC → GATE T. Never publish.
