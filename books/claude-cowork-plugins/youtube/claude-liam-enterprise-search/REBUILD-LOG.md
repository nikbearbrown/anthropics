# REBUILD-LOG — claude-liam-enterprise-search

Session: 2026-08-26

## Pre-rebuild backup
`beat_sheet.pre-rebuild.json` created before any edits (47898 bytes, matching the
Aug 1 22:42 sheet). The older `beat_sheet.json.bak` (Jul 23 11:39, 20781 bytes) is
a different snapshot — it predates this session and was not overwritten.

## LOCKED (carried over verbatim)
- All `narration_text` fields in body beats B00–B23, C01–C06, V01, H01, O01
- Beat order and act labels
- Shot intent: patterns, props, spark lines, visual descriptions
- Metadata identity: title, slug, topic, source pointer, register, channel

## REBUILT / FIXED this session

### 1. BVDT — verdict authored (was placeholder)
BVDT's `narration_text` was empty and `artifactLines` contained only template
defaults ("Key finding one", "Key finding two", "Key finding three").

Rule: "A verdict line is invalid if it is a template default ... a reel with 5+
beats and 180+ words must have a real verdict AUTHORED."

**Old narration_text:** `""`
**New narration_text:** `"Enterprise search doesn't give you new access — it gives you faster reach over the access you already hold. Knowledge buried in a drive, a wiki, a thread is now one question away. Five workflows unlock that: institutional memory, client context, policy lookup, meeting prep, contradiction checks. And the return compounds: the more you document as you decide, the more it can find."`

**Old artifactLines:**
- "Key finding one"
- "Key finding two"
- "Key finding three"

**New artifactLines** (drawn from body beats):
- "Knowledge doesn't vanish — it gets buried in drives, wikis, threads"
- "Content search reads inside files; filename search never could"
- "Five workflows: memory, context, policy, prep, no-contradictions"
- "Bounded by your existing access — faster reach, not new permissions"
- "Document decisions now: yesterday's choice becomes tomorrow's source"

Source: body beats B01 (buried knowledge), B04 (content vs filename), B11
(five workflows), B18 (access boundary), B23 (compound habit).

### 2. BHTF — folderLabel corrected
`folderLabel` was `"@claude-liam"` (brand key, not a channel handle).
Changed to `"@NikBearBrown"` per rule: "folderLabel is a channel handle
(@NikBearBrown), never a brand key (@claude-liam)."

## Datable claims examined
No narration was edited for datable claims. `model_chip.model: "Fable 5"` is
a fictional model name used intentionally in the UI chrome to avoid dating the
reel — not a real Anthropic model and not a claim about the world. Left unchanged.
