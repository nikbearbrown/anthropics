# REBUILD-LOG — agentic-loop-not-chatgpt

Rebuild pass performed under the FILMLOOP-PROMPT (locked-script contract).

## Locked (carried over verbatim)
- `narration_text` for B00, B01, B02, B03, B04, B05, B06 — unchanged.
- Beat order and act labels for B00–B06 — unchanged.
- Metadata identity (slug, title, topic, register, audience, brand, palette).

## Rebuilt / normalized (envelope, not script)

### B00 — cold-open remotion consolidated
- Was: two conflicting `remotion` blocks (`shot.remotion.props.greeting: "Liam"` +
  a top-level `remotion.props.greeting: "Bula, Liam"` with a different command).
- Now: single `shot.remotion.ClaudeComposerAsk` with
  `greeting: "Bula, Liam"` (matches metadata; Fijian one-word hello, none of the
  adjacent reels in this run used it), `command: "add a contact form to my class
  website"` (matches the teacher story in the narration), and a real `output` list
  showing five actions Claude Code performed unattended (the ask must land answered
  — COLD OPEN LAW).

### B01 — FormBCard fallback items authored
- Was: `items[0]` label `"gather"` sub `"gather"` (dup); `items[1]` label
  `"verify. That entire loop can"` sub `"verify. That entire loop can run for many
  iterations before reporting back. The loop is Claude. Wrong actions accumul…"`
  (truncated narration passed off as labels — punt-in-a-costume).
- Now: three real-noun items on the "gather, act, verify" cycle the narration
  explicitly names — icons `clipboard-list`, `zap`, `circle-check`; cueFrames
  spread across the beat span. Manim `Scene_B01_AgenticLoopNot` remains primary.

### B04 — remotion pattern added
- Was: `shot.type: REMOTION, motion: stagger` with NO pattern. Would not render.
- Now: `FormACard` with three lines pulled from the beat's own narration
  ("Ask before act." / "Read before execute." / "Calibrate before build.").

### B05 — HANDOFF composer topic
- Was: `topic: "CLAUDE CODE · @NikBearBrown"` — did not satisfy the BHTF check
  (which looks for "YOUR TURN" in topic/segment when no beat has beat_id=BHTF).
- Now: `topic: "YOUR TURN · CLAUDE CODE"` so B05 serves as the BHTF bookend.
  Prompt and narration unchanged (LOCKED).

### Empty duplicate bookends stripped
Three empty-envelope bookends (BVDT, BHTF, BOUT) were present-but-empty, which
the audit rule calls out as invalid ("present-and-empty is not" legal). Their
roles are already carried by the LOCKED beats:
- BHTF role → satisfied by B05 (ClaudeComposerAsk, topic edit above).
- BOUT role → satisfied by B06 (already `ClaudeTitleOutro` with correct props).
- BVDT role → stripped legally per the amendment ("BVDT may be legitimately
  ABSENT if a previous pass stripped a placeholder verdict"). Added
  `metadata.bookend_exempt: ["bvdt"]` so `bookend_check.py` treats it as intended.

The template default BVDT lines (`"Key finding one" / "two" / "three"`) and the
template BHTF command with square brackets (`"Take what you learned from [ ... ]
and apply it to your own work"`) were the specific placeholders the audit rule
targets — deleted with the empty beats.

### Dead ElevenLabs-era fields
None found in this sheet — it was already Kokoro-only.

## Datable claims audit
Full narration re-read against the DOUBLE-CHECK LAW. No datable claim landed in
the script — no model version numbers, no prices, no "as of" phrasing, no counts
that drift. Nothing to fix.

## Not rebuilt
- Body Manim scenes (`Scene_B01_/B02_/B03_AgenticLoopNot` in `scenes_std.py`)
  were not re-authored — they are carried and will render at compile time.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-edit sheet.
- `beat_sheet.json` — the rebuilt sheet (this pass).
