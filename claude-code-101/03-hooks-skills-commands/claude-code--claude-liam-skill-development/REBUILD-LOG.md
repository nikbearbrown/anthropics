# REBUILD-LOG.md — claude-liam-skill-development

Rebuild date: 2026-08-25
Operator: film-factory (unattended)

---

## LOCKED (carried over verbatim)

- All `narration_text` per beat — no changes to script.
- Beat order and act labels — unchanged.
- Shot intent per beat — patterns/props/sparkLines preserved.
- Metadata identity: title, slug, topic, source pointer, register, channel.

---

## REBUILT

### VOICE-LOCK normalize
All beats already had `engine: "kokoro"`, `voice: "am_onyx"`. No ElevenLabs fields present. No changes needed.

### shot.form derivation (per SHOT-FORM-SYSTEM.md)

| Beat | Pattern | form assigned | Rationale |
|---|---|---|---|
| B00 | ClaudeComposerAsk | `claude-code` | Canonical composer ask — cold open |
| B01 | SkillDevAnatomy | `mechanism-plate` | Labeled anatomy of 3-level progressive disclosure system |
| B02 | SkillDevProcess | `step-sequence` | 6-step creation process (ordered steps, one active) |
| B05 | SkillDevTell | `comparison-table` | 2-column teardown: gets-right vs where-it-bites |
| BVDT | ClaudeVerdictArtifact | `claude-code` | Verdict artifact — canonical bookend |
| BHTF | ClaudeComposerAsk | `claude-code` | Handoff composer — canonical bookend |
| BOUT | ClaudeTitleOutro | `claude-code` | Title outro — canonical bookend |

---

## DATABLE CLAIMS FIXED (narration lock exception)

### Fix 1 — B00 props.modelLabel
- **Old:** `"modelLabel": "Opus 4.8"`
- **New:** `"modelLabel": "Opus 4.7"`
- **Source:** Anthropic model line as of 2026-08-25: claude-opus-4-7 is the current maximum (CLAUDE.md / environment context). Opus 4.8 does not exist.
- **Note:** This is a UI prop, not narration text. The narration text is unchanged.

### Fix 2 — BHTF props.modelLabel
- **Old:** `"modelLabel": "Opus 4.8"`
- **New:** `"modelLabel": "Opus 4.7"`
- **Source:** Same as Fix 1.
- **Note:** UI prop only. Narration text unchanged.

---

## GATES

- TYPECHECK.md: GATE T PASS (2026-08-25, skip-pixels; pixel checks run post-render)
- beat_sheet.pre-rebuild.json: created 2026-08-25 (byte-exact copy before edits)
