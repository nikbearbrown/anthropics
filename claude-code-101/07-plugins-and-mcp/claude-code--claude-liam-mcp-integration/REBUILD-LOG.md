# REBUILD-LOG — claude-liam-mcp-integration

**Run:** 2026-08-20  
**Pre-rebuild backup:** beat_sheet.pre-rebuild.json (byte-exact copy made before any edit)

---

## Datable-claim edits (narration LOCKED; props edited)

### 1. B00 — modelLabel
- **Old:** `"modelLabel": "Opus 4.8"`
- **New:** `"modelLabel": "Opus 4.7"`
- **Source:** System context: most recent Opus model is claude-opus-4-7 as of 2026-08-20. Opus 4.8 does not exist.

### 2. BHTF — modelLabel
- **Old:** `"modelLabel": "Opus 4.8"`
- **New:** `"modelLabel": "Opus 4.7"`
- **Source:** Same as above.

## Doctrine fixes (OUTRO-LOCK / HANDOFF-LAW)

### 3. BHTF — greeting
- **Old:** `"greeting": "Your Turn"` (capital T, no period)
- **New:** `"greeting": "Your turn."` (lowercase t, period)
- **Rule:** HANDOFF LAW specifies exactly `"Your turn."` — period required, title-case is wrong.

### 4. BOUT — subline removed
- **Old:** `"subline": "mcp-integration · Claude Code Skills"`
- **New:** (prop removed)
- **Rule:** OUTRO-LOCK: "@NikBearBrown outro card is locked — NO subline; claude-liam reels only."

---

## Locked (not changed)

- All narration_text values: verbatim from original
- Beat order and act labels: verbatim
- Shot patterns and props (except the prop edits above): locked
- Metadata identity: title, slug, topic, source_skill, register, channel: locked
- McpIntAnatomy, McpIntPatterns, McpIntTell: patterns confirmed on disk — no change needed
