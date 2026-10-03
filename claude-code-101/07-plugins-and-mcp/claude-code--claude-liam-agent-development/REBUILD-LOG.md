# REBUILD-LOG.md — claude-liam-agent-development

**Rebuild date:** 2026-08-25  
**Session:** Film-factory invocation — audit + build pass

---

## Pre-rebuild backup

`beat_sheet.pre-rebuild.json` created as byte-exact copy before any edit.

---

## LOCKED (unchanged)

- All `narration_text` per beat — no rewriting
- Beat order: B00 → B01 → B02 → B05 → BVDT → BHTF → BOUT
- Act labels unchanged
- Shot patterns: ClaudeComposerAsk, AgentDevAnatomy, AgentDevDescription, AgentDevTell, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro
- BVDT `artifactLines` unchanged (real verdict, not placeholder)

---

## CHANGED — all prop edits (not narration)

### Datable claim: modelLabel "Opus 4.8" → "Opus 4.7"

| Beat | Old | New | Source |
|---|---|---|---|
| B00 | `modelLabel: "Opus 4.8"` | `modelLabel: "Opus 4.7"` | System context Aug 2026: latest Opus is 4.7 (`claude-opus-4-7`); 4.8 does not exist |
| BHTF | `modelLabel: "Opus 4.8"` | `modelLabel: "Opus 4.7"` | Same |

### Spark line length: SPARK-LINE LAW ≤4 words

| Beat | Old | New | Word count |
|---|---|---|---|
| B01 | `"Frontmatter triggers. Body becomes the system prompt."` | `"Two parts. Body speaks."` | 7→4 |
| B02 | `"Examples teach triggering. No examples, no trigger."` | `"No examples, no trigger."` | 7→4 |
| B05 | `"Description field nailed. Decision tree missing."` | `"No decision tree."` | 6→3 |

All new lines are derived from each beat's own narration (B01: "An agent file has two parts … body becomes the system prompt"; B02: "no example blocks, Claude cannot learn when to fire"; B05: "there is no agent-versus-command decision tree").

### Bookend greeting: HANDOFF LAW

| Beat | Old | New |
|---|---|---|
| BHTF | `greeting: "Your Turn"` | `greeting: "Your turn."` |

HANDOFF LAW requires `"Your turn."` (lowercase t, period). The original had Title Case and no period.

---

## Audio

No audio regeneration required — all narration_text locked, all props changes are visual-only. Existing mp3 files (Jul 18 15:59–16:00) remain valid. actual_duration_s values carried from the measured sheet.
