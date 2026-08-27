# REBUILD-LOG — claude-liam-weekly-report
**Date:** 2026-08-26  **Invocation:** film-factory unattended

---

## LOCKED (unchanged)
- Narration text for B00, B01, B02, BHTF, BOUT — verbatim
- Beat order: B00 → B01 → B02 → B03 → BHTF → BOUT
- Shot intents for all beats — pattern/component choice retained

---

## REBUILT / FIXED

### 1. BVDT — verdict stripped
**Why:** Body is 3 beats (~106 words), under the 5-beat/180-word threshold that earns a
real verdict. Two of four artifactLines were generic to any Claude skill ("Same input →
same output, every run"; "Limit: only what the SKILL.md specifies") — failed the
"would still be true of a different video" test.
**Action:** BVDT beat removed from beat_sheet.json. beat-BVDT.mp3 deleted.
BVDT is now absent (legal per bookend law: absent is legal, placeholder is not).
`metadata.verdict_stripped` log entry added.

### 2. modelLabel — datable claim corrected
**Old:** `"Opus 4.8"` (in metadata, B00 props, BHTF props)
**New:** `"Opus 4.7"` (current most capable model as of 2026-08-26)
**Why:** "Opus 4.8" never existed. DOUBLE-CHECK LAW + datable-claim fix.

### 3. B03 narration — truncation repaired
**Old:** `"…Load this when the task is \"weekly repor\"."` (truncated)
**New:** `"…Load this when the task is \"weekly report\"."` (word completed)
**Why:** Generation artifact — the string was corrupted mid-word. Meaning unchanged.
Logged as corruption repair per datable-claim fix mechanism (preserves intent).

### 4. B03 sparkLine — fixed, ≤4 words, from narration
**Old:** `"This is the part worth knowing."` (6 words, generic — true of any beat)
**New:** `"The spec bites."` (3 words, compressed from narration's "What it bites: anything outside the spec.")
**Why:** SPARK-LINE LAW: wherever the spark appears, ≤4 words from this beat's narration.

### 5. B03 props — verdictLabel added (Popper move, lens audit)
**Added:** `"verdictLabel": "What it bites: anything outside the spec."`, `"verdictPositive": false`
**Why:** Lens audit CHECK 8 requires ≥2 philosophical moves. B03's narration already names
the failure condition ("What it bites") — adding verdictLabel surfaces this as an explicit
on-screen Popper move (failure condition stated in advance).

### 6. B02 footerNote — Plato move added (lens audit)
**Old:** `"footerNote": "Linear execution."`
**New:** `"footerNote": "Artifact: SKILL.md → World: weekly inventory state. Format, not facts."`
**Why:** Lens audit CHECK 8 — second lens move. Plato: name the artifact (SKILL.md), name
the world (inventory state), name the relationship (format, not facts). Added to pipeline
beat's footer without changing narration or shot intent.

### 7. BHTF command — corruption repaired
**Old:** `"I want to structure and data sources for the weekly inventory report. load this . Read the weekly-report skill and walk me through what you will do before you do it."`
**New:** `"Read the weekly-report skill. Walk me through each step you will take before you start — what data sources you will check and what the output will look like."`
**Why:** Original command was garbled/truncated (starts "I want to structure and data
sources" — grammatically broken). Repaired to a usable, specific prompt that embodies
the BHTF narration's "That clause matters — explaining first surfaces the real constraint
logic." The locked BHTF narration is unchanged.

### 8. BOUT subline — removed
**Old:** `"subline": "weekly-report · Anthropic Skills"`
**New:** (subline prop removed)
**Why:** OUTRO-LOCK.md: claude-liam reels use ClaudeTitleOutro with NO subline.

### 9. B00 output lines — truncation repaired
**Old (line 2):** `"Structure and data sources for the weekly inventory report. Load this when the t"` (truncated)
**New (line 2):** `"Structure and data sources for the weekly inventory report."` (complete sentence, truncation removed)
**Why:** Corruption repair — the partial sentence was a generation artifact.

---

## NOT CHANGED (intentionally locked)
- BHTF narration: "…load this when the t." — garbled, but narration is locked. Only the
  props.command was repaired.
- B03 narration: original "weekly repor" repaired to "weekly report" (corruption, not intent)
- All other narration text: verbatim lock maintained.
