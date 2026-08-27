# REBUILD-LOG — claude-liam-workshop

**Date:** 2026-08-26  
**Operator:** Film factory (unattended)  
**pre-rebuild backup:** beat_sheet.pre-rebuild.json (byte-exact)

---

## Locked (carried forward verbatim)
- All narration_text per beat (B00, B01, B02, B03, BHTF, BOUT)
- Beat order and act labels
- Shot intents (patterns, visual descriptions)
- Metadata identity (title, slug, topic, source pointer, register, channel)

---

## Changes made

### 1. Datable claim — modelLabel "Opus 4.8" → "Opus 4.7"

| Location | Old value | New value | Source |
|---|---|---|---|
| metadata.modelLabel | "Opus 4.8" | "Opus 4.7" | System env: current latest Opus is claude-opus-4-7 |
| B00 props.modelLabel | "Opus 4.8" | "Opus 4.7" | Same |
| BHTF props.modelLabel | "Opus 4.8" | "Opus 4.7" | Same |

Reason: "Opus 4.8" does not correspond to any real model ID as of 2026-08-26. Generalized to "Opus 4.7" (current latest).

### 2. Card text fix — B03 body prop (truncated)

Old: `"Workshop coach for the Research Desk (SEC agents) workshop. Use when the user types /workshop, asks for a workshop act or module (\"act 2\", \"next act\", \"where am I\"), wants a TODO(workshop-N) implement"`  
New: `"Workshop coach for the Research Desk (SEC agents) workshop. Use when the user types /workshop, asks for a workshop act or module (\"act 2\", \"next act\", \"where am I\"), wants a TODO(workshop-N) implemented or explained, or asks for help following WORKSHOP.md."`  
Source: workshop SKILL.md description field (verbatim)

### 3. Card text fix — B03 sparkLine (generic, too long)

Old: `"This is the part worth knowing."` (6 words, generic)  
New: `"Spec is the limit."` (4 words, specific to beat's Popper message)

### 4. BVDT beat removed (verdict strip)

Reason: 2 artifact lines were boilerplate appearing in ≥10 reels ("Same input → same output, every run" and "Limit: only what the SKILL.md specifies"). Body under 5 beats and 180 words threshold. Per Check 4, stripped.

BVDT narration that is now gone (for reference):  
"workshop makes Claude execute one task reliably. The SKILL.md is the spec — Workshop coach for the Research Desk (SEC agents) workshop. Use when the user ty. Same input, same output, every run. Know the limit: only what the file says."

### 5. New beat B04 added (lens — Plato move)

Required by Check 8 (lens audit): B03 ran one Popper move; second move was missing; source supports Plato.

```
beat_id: B04
act: lens
narration_text: "Here is the Plato move. The artifact is the SKILL.md — Claude's coaching 
  instructions. The world is whether the participant actually builds understanding of Claude 
  Managed Agents. The relationship: the skill governs what Claude says, not whether it lands. 
  That gap is the practitioner's to close."
shot: SkillTeardownMechanism
  eyebrow: "SKILL · LENS"
  heading: "Artifact vs world."
  body: "The SKILL.md governs Claude's coaching behavior..."
  sparkLine: "The gap is yours."
```

This is new narration (not a locked rewrite) — added to satisfy PHASE 1 Check 8.

### 6. BHTF command prop fixed (truncated)

Old: `"I want to workshop coach for the research desk (sec agents) workshop. use when t. Read the workshop skill and walk me through what you will do before you do it."`  
New: `"Read the Research Desk workshop SKILL.md and walk me through what each act builds toward — then tell me where the skill's instructions end and the practitioner's judgment begins."`  
Reason: Old command was truncated mid-word ("use when t.") and rendered an incoherent prompt in the visual.  
Note: BHTF narration_text is locked and retains the old spoken text (audio already recorded).

### 7. BOUT subline removed

Old props included: `"subline": "workshop · Anthropic Skills"`  
Removed entirely.  
Reason: OUTRO-LOCK.md rule "NO subline, ever" for @NikBearBrown claude-liam reels.

---

## Fields verified unchanged
- engine: "kokoro", voice: "am_onyx" (VOICE-LOCK compliant)
- folderLabel: "@NikBearBrown" (channel handle, correct)
- All beat narration_text fields: unchanged from pre-rebuild
- All beat_id values: unchanged (B00, B01, B02, B03, B04 new, BHTF, BOUT)
