# REBUILD-LOG — agents-that-remember-memory-store

**Rebuilt:** 2026-08-26 (film factory, unattended)

---

## What was LOCKED (carried verbatim)
- All narration_text for B00–B10 — unchanged
- Beat order and act labels — unchanged
- Shot intent / pattern / props for B00–B10 — unchanged (props may be re-shaped; ideas locked)
- Metadata identity: title, slug, channel, source, register — unchanged

## What was REBUILT / FIXED

### 1. BVDT — verdict authored (Check 4 + Check 2)
**Old narration_text:** `""` (empty)  
**New narration_text:** "Sessions are stateless by design — each starts blank. Attach a memory store and the agent writes structured facts in session A and reads them in session B: key-value pairs, confidence-scored, per user. The Dreaming Service runs between sessions — not during — reads past transcripts, and writes structured memory back automatically. Zero latency impact on your conversation. Memory is infrastructure you wire in. It is not a property of the model."  
**Source:** Derived from body beats B02 (session isolation), B05 (key-value schema with confidence), B06 (Dreaming Service between-session behavior), B04 (three-layer progression)  
**Why:** Template defaults ("Key finding one/two/three") fail verdict validity check; narration was blank. Body has 5+ beats and 180+ words so author threshold is met.

**Old artifactHeading:** "Key findings"  
**New artifactHeading:** "The three-layer model"  
**Source:** Derived from B04 narration: "The progression is isolation, then persistence, then self-improvement."

**Old artifactLines:**
- "Key finding one"
- "Key finding two"
- "Key finding three"

**New artifactLines:**
- "Sessions are stateless by design — each starts with a blank context window."
- "A memory store adds persistence: key-value records, confidence-scored, survive across sessions."
- "The Dreaming Service runs between sessions — reads transcripts, writes structured memory back. Zero in-session latency."
- "Memory is infrastructure you wire in. It is not a property of the model."

**Source:** B02 (isolation), B05 (key-value + confidence), B06 (Dreaming Service, zero latency), B04 (memory as infrastructure lever)

### 2. BHTF — folderLabel corrected (Check 9)
**Old:** `"folderLabel": "@claude-liam"`  
**New:** `"folderLabel": "@NikBearBrown"`  
**Why:** `@claude-liam` is a brand key, not a channel handle. The ai-explainer SKILL.md table and the OUTRO-LOCK specify `@NikBearBrown` for the claude-liam channel.

---

## Datable claim edits to narration
None. No model version numbers, prices, or "as of" claims found in B00–B10 narration that required correction.

---

## beat_sheet.pre-rebuild.json
Created at 2026-08-26 as byte-exact copy of beat_sheet.json before any edit.
