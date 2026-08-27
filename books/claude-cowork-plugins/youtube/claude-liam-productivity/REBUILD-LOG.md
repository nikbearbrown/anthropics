# REBUILD-LOG.md — claude-liam-productivity
Date: 2026-08-26

## Backup
`beat_sheet.pre-rebuild.json` — byte-exact copy of original sheet, created before any edit.

---

## LOCKED (carried verbatim)
- All `narration_text` fields (24 body beats + segment cards + bookend beats B00/V01/H01/O01)
- Beat order and act labels
- Shot intent, patterns, props, spark lines (except H01 spark_line — see below)
- Metadata: title, slug, topic, source, channel, register, palette

---

## REBUILT / FIXED

### 1. H01 spark_line
- **Old**: `"Make it run your day."` (5 words — over 4-word limit)
- **New**: `"Paste. Run. Watch."` (3 words)
- **Reason**: SPARK-LINE LAW mandates ≤4 words for inner beats. Compressed from H01 narration: "Run it, and watch which questions it asks before it answers."

### 2. BVDT verdict — placeholder content → real verdict
- **Old heading**: `"Key findings"`
- **New heading**: `"The verdict"`
- **Old lines**: `["Key finding one", "Key finding two", "Key finding three"]`
- **New lines**:
  1. `"Five moves, no setup — tasks, meetings, email, schedule, notes"`
  2. `"Add a calendar; tell it your method once — it adopts and compounds"`
  3. `"Its plan is a model of what you told it, not what actually needs doing"`
  4. `"The test: what breaks when urgent work arrives that Claude never saw?"`
- **Old narration**: `""` (empty)
- **New narration**: `"That's the reel. Five moves, no setup, compounds with use. Two things to hold: the plan it surfaces is a model of what you told it, not what actually needs doing — the model's confidence is the model's, not the world's. And the test to run: what breaks when an unscheduled urgent thing arrives that Claude never saw? Name that failure mode in advance. The plugin is the tool. The judgment is yours."` (73 words)
- **Reason**: Placeholder verdict (verdict_audit.py flagged). Body is 24+ beats, 1000+ words — authoring required. Lines 3–4 embed Hume (model confidence ≠ world confidence) and Popper (falsifying condition stated in advance) per LENS-NOTES.md.

### 3. BHTF folderLabel
- **Old**: `"@claude-liam"` (brand key — not a channel handle)
- **New**: `"@NikBearBrown"` (channel handle)
- **Reason**: ai-explainer SKILL.md rule: `folderLabel` is always a channel handle (`@NikBearBrown`), never a brand key.

---

## Datable claims — none found
No model version numbers, pricing, or "as of" claims in narration. No DOUBLE-CHECK LAW edits required.

---

## Dead ElevenLabs fields — none found
No `voice_id`, `voice_env`, or ElevenLabs `clock` prose in sheet. VOICE-LOCK fields already clean (`engine: "kokoro"`, `voice: "am_onyx"`).
