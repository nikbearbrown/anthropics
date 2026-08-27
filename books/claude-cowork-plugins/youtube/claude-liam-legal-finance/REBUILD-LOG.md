# REBUILD-LOG.md — claude-liam-legal-finance
## Session: 2026-08-26

This log records every change made to beat_sheet.json during the rebuild.
Pre-rebuild backup: `beat_sheet.pre-rebuild.json`.

---

## Narration edits (datable claims)

None. No datable model names, pricing, or "as of" claims found.

---

## Structural / envelope changes

### BVDT — narration_text (was empty)
**Old:** `""`
**New:**
> "Here is what those two plugins actually deliver. Every contract you touch goes through a filter before you sign — standard, attention, or concern — not because you became a lawyer but because the machine did the first read. Every financial scenario you've been putting off gets modeled before you commit — where the cash ends, how long the runway holds, what the hiring decision costs in three cases. Neither plugin is the professional. Both are the screen that tells you when to call one."

**Source:** Authored from reel body content (legal plugin = green/yellow/red flags; finance plugin = burn rate / runway / scenario modeling). Not a datable claim edit.

### BVDT — artifactHeading
**Old:** `"Key findings"`
**New:** `"Two plugins. One purpose."`

### BVDT — artifactLines
**Old:** `["Key finding one","Key finding two","Key finding three"]`
**New:**
```json
[
  "Legal reads the contract before you sign — green, yellow, red",
  "Finance models burn rate, runway, and the what-if before you commit",
  "Both accelerate the analysis; neither is the lawyer or the CFO",
  "A red flag from either means one thing: call the professional"
]
```

### BHTF — folderLabel
**Old:** `"@claude-liam"`
**New:** `"@NikBearBrown"`
**Source:** VOICE-LOCK.md / brand spec — folderLabel must be @NikBearBrown for claude-liam channel reels.

---

## Shot / pattern fixes

### B06 — scene + remotion.pattern
**Old scene:** `"code-block"` / pattern `"ClaudeCodeBeat"`
**New scene:** `"ClaudeComposerAsk"` / pattern `"ClaudeComposerAsk"`
**Why:** B06 shows what the user types into Claude's interface. ClaudeCodeBeat is for real code/terminal. ClaudeComposerAsk is the correct skin per ASK→RESULT LAW.

### B15 — scene + remotion.pattern + sparkLine in props
**Old scene:** `"code-block"` / pattern `"ClaudeCodeBeat"`
**New scene:** `"ClaudeComposerAsk"` / pattern `"ClaudeComposerAsk"`
**Also:** `shot.remotion.props.sparkLine` corrected from `"Point it at your data."` to `"Aim at your data."` (kept in sync with beat-level spark_line fix).

### B22 — pattern change (SlateCard → VRChipGrid)
**Old:** `SlateCard` with truncated caption (mid-sentence cut-off at 80 chars)
**New:** `VRChipGrid` with items `["Routine, not occasional","Escalate the red flags","Organized documents"]`, sparkLine `"Three habits."`
**Why:** SlateCard with truncated prose is a nopunt violation. Content is a short list of named practices — VRChipGrid is the catalog mapping.

---

## Spark-line fixes

### B14 — spark_line
**Old:** `"Do it, don't mean to."`
**New:** `"Actually do it."`
**Why:** Spark lines must be ≤4 words per SPARK-LINE LAW; old line was 5 words. Note: `scenes.py` B14Doodle still shows old headline (cosmetic Manim label only; logged in AUDIT.md).

### B15 — spark_line
**Old:** `"Point it at your data."`
**New:** `"Aim at your data."`
**Why:** "Point it at your data" is 5 words; reduced to 4.

---

## New scene classes authored (scenes_std.py)

6 Manim scene classes written and rendered to fill pipeline-owned SLATE beats:

| Class | Beat | Content |
|---|---|---|
| Scene_B04_ClaudeLiamLegal | B04 | Two-bar: No review vs Plugin first-pass |
| Scene_B07_ClaudeLiamLegal | B07 | Three-color flag bars (green/yellow/red) |
| Scene_B09_ClaudeLiamLegal | B09 | Two-bar: Hours vs Minutes review time |
| Scene_B13_ClaudeLiamLegal | B13 | Two-column triage: Routine / High-stakes |
| Scene_B21_ClaudeLiamLegal | B21 | Two-column: Plugin analysis / Human decision |
| Scene_B23_ClaudeLiamLegal | B23 | Rising cost curve over time |

These are not narration edits — they are scene implementations of existing locked shots.

---

## Fields dropped (dead ElevenLabs-era fields)

None found — sheet was already clean of voice_id / voice_env fields.
