# REBUILD-LOG — claude-liam-reorder-policy

**Rebuilt:** 2026-08-26  
**Operator:** filmloop  
**Backup:** `beat_sheet.pre-rebuild.json` created before any edit.

---

## LOCKED (unchanged)
- All beat `narration_text` values except truncation-corrections below
- Beat order and act labels
- Shot pattern/intent per beat (SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, bookend patterns)
- Metadata identity: title, slug, topic, source pointer, register, channel, persona

---

## REBUILT / CORRECTED

### 1. modelLabel — datable claim FIX
| Field | Old | New | Source |
|---|---|---|---|
| metadata.modelLabel | "Opus 4.8" | "Opus 4.7" | System env: current latest Opus as of 2026-08-26 |
| B00 props.modelLabel | "Opus 4.8" | "Opus 4.7" | Same |
| BHTF props.modelLabel | "Opus 4.8" | "Opus 4.7" | Same |

### 2. B03 narration — mechanical truncation-fix
Old: `"...Load this whenever a task involves reorder reco."`  
New: `"...Load this whenever a task involves reorder recommendations, purchase orders, or 'should we restock' questions."`  
Source: source_skill SKILL.md description field (exact text). Build artifact — `reco` is a truncated copy of `recommendations`.

### 3. BVDT narration — mechanical truncation-fix
Old: `"...Load this whenever a task i."`  
New: `"...Load this whenever a task involves reorder recommendations, purchase orders, or 'should we restock' questions."`  
Source: same SKILL.md description.

### 4. BVDT artifactLines[1] — mechanical truncation-fix
Old: `"How to decide whether and how much to reorder a SKU. Load this whenever a task involves re"`  
New: `"How to decide whether and how much to reorder a SKU. Load this whenever a task involves reorder recommendations, purchase orders, or 'should we restock' questions."`  
Source: same SKILL.md description.

### 5. BHTF narration + command prop — mechanical truncation/grammar fix
Old narration: `"Paste this into Claude: 'I want to how to decide whether and how much to reorder a sku. load this whenever a task i. Read the reorder-policy skill..."`  
New narration: `"Paste this into Claude: 'I need to decide whether and how much to reorder a SKU. Read the reorder-policy skill and walk me through what you will do before you do it.'"`  
Old command prop: `"I want to how to decide whether and how much to reorder a sku. load this wheneve. Read the reorder-policy skill and walk me through what you will do before you do it."`  
New command prop: `"I need to decide whether and how much to reorder a SKU. Read the reorder-policy skill and walk me through what you will do before you do it."`  
Reason: "I want to how to decide" is ungrammatical; "load this wheneve" is truncated. Both are build artifacts from a truncated SKILL.md description being prepended with "I want to". Fixed to a clean imperative matching the beat's intent. Narration updated to quote the corrected command; the clause "That clause matters — explaining first surfaces the real constraint logic." is unchanged.

---

## VOICE-LOCK
Engine: kokoro. Voice: am_onyx. No ElevenLabs fields present (none to drop). PASS.
