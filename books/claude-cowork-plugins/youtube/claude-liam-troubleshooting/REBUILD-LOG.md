# REBUILD-LOG — claude-liam-troubleshooting

Rebuild session: 2026-08-26  
Pre-rebuild backup: `beat_sheet.pre-rebuild.json` (byte-exact copy made before any edit)

---

## LOCKED (carried over verbatim)

- All `narration_text` fields except BVDT (which was empty — new narration is new writing, not a locked change)
- Beat order and act structure (COLD OPEN → ACT I → II → III → IV → CLOSE)
- Metadata: title, slug, topic, channel, register, palette
- SparkLine intent per beat

---

## REBUILT / FIXED

### 1. BVDT — verdict authored from body content (was template placeholder)

**Old narration_text:** `""` (empty)  
**New narration_text:** `"The findings from Claude, Unstuck. When a plugin breaks, don't chase the surface — return to what it's for. Failures trace to five durable causes. Four steps clear most of them. And the interface will keep changing — verify the specifics in the docs. The screen dates; the mental model persists."`

**Old artifactHeading:** `"Key findings"` (generic)  
**New:** `"Troubleshooting and staying current"`

**Old artifactLines:**
- "Key finding one"
- "Key finding two"  
- "Key finding three"

**New artifactLines (authored from V01 body):**
- "Return to the concept, not the screen — the surface changes; the durable layer holds"
- "Five failure causes: not active · stale creds · generic defaults · external scope · needs restart"
- "Four-step fix loop: active? authorized? simpler request? restart."
- "The interface dates — verify specifics in docs; the mental model persists"

**Source:** V01 narration_text and artifactLines in the body of this reel.  
**Why:** Template lines ("Key finding one") would fail verdict_audit; body has 16 beats and 200+ words, qualifying for authored verdict.

---

### 2. BHTF — folderLabel corrected

**Old:** `"folderLabel": "@claude-liam"`  
**New:** `"folderLabel": "@NikBearBrown"`  
**Why:** folderLabel must be the channel handle (@NikBearBrown), never the brand key.

---

### 3. B05, B11, B12, B15, B16 — DoodleScene → FormACard (punt removal)

All five beats had `shot.manim.scene_class: "BXXDoodle"` (DoodleScene pattern).  
All converted to `shot.remotion.pattern: "FormACard"` using the beat's spark_line as the card text.

| Beat | Old | New | Spark line |
|------|-----|-----|------------|
| B05 | B05Doodle (still: expired key) | FormACard | "Credentials go stale." |
| B11 | B11Doodle (still: thread/knot) | FormACard | "Isolate by shrinking." |
| B12 | B12Doodle (still: stacked plates) | FormACard | "Nothing sits still." |
| B15 | B15Doodle (still: calendar) | FormACard | "A monthly habit." |
| B16 | B16Doodle (still: foundation) | FormACard | "The model persists." |

Top-level `"engine": "manim"` field removed from each beat.  
`lane` changed from "MANIM" to "REMOTION".  
`build.status` changed to "NEEDS-RENDER".  
Narration locked — unchanged.

---

### 4. B08 — ClaudeCodeBeat → FormACard (type_check §8.12 fix)

**Old pattern:** `ClaudeCodeBeat` with `code: "/\n/plugins"` and `title: "Cowork"`  
**New pattern:** `FormACard` with lines `["Type slash, look.", "/ → all commands", "/plugins → active list"]`  
**Why:** §8.12 flags ClaudeCodeBeat when content has no code tokens. Slash CLI commands are not code. FormACard is the correct pattern for enumerating commands. Narration unchanged.

---

### 5. scenes_std.py — chart label and ACT-space fixes

All three scenes (B01, B06, B07):
- "ACT I" / "ACT II" → "ACT  I" / "ACT  II" (doubled space per font-rasterize rule)
- Labels changed from `narration_text[:30]` fragments to 1–3 word category nouns
- Bar heights corrected so the favored outcome is the taller bar
- Captions changed from 60-char narration slices to complete sentences

| Scene | Old lbl1 | New lbl1 | Old lbl2 | New lbl2 | Heights fixed |
|-------|----------|----------|----------|----------|---------------|
| B01 | "Things will go wrong" (narration) | "Diagnose" | "Plugins won't behave…"[:30] (narration truncated) | "Abandon" | bar1=75 (Diagnose), bar2=25 |
| B06 | "Plugin works, but…"[:30] (narration truncated) | "Broad default" | "Feed it your context…"[:30] | "Your context" | bar1=35, bar2=75 (Your context) |
| B07 | "Slow operations…"[:30] (narration truncated) | "Everything" | "The fix is scope" | "One slice" | bar1=35, bar2=75 (One slice) |

---

## DATABLE CLAIMS — no changes needed

No model names, version numbers, prices, or rotted "as of" phrasing found in narration_text fields. All narration describes concepts and procedures, not versioned specifics.

---

## VOICE-LOCK status

- `engine: "kokoro"` ✓  
- `voice: "am_onyx"` ✓  
- No dead ElevenLabs fields (no `voice_id`, `voice_env`, ElevenLabs `clock` prose) ✓
