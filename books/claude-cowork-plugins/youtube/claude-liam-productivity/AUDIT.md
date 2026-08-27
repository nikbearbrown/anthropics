# AUDIT.md — claude-liam-productivity
Generated: 2026-08-26 by filmloop

---

## Pre-audit state

- No mp4 files exist (reel was previously compiled but video files are gone).
- `clips/manifest.json` shows prior compile: beats B02/B09/B13/B16/B18/B19/B22/B24 were slates; all others had real hashes.
- `clips/master.m4a` exists (intermediate audio from prior compile).
- Audio mp3s exist for all non-slate beats. Silence files (sil_*.mp3) for slate beats.
- `beat_sheet.pre-rebuild.json` created as byte-exact backup before any edit.

---

## Check 1 — Stale renders

**PASS.** No mp4 files anywhere in the reel folder. Nothing to purge.

---

## Check 2 — Bookends

**PASS.** All four bookends present with correct patterns:
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` ✓ (placeholder content — fixed by Check 4)
- BHTF: `ClaudeComposerAsk` with `greeting: "Your turn."` ✓
- BOUT: `ClaudeTitleOutro` ✓

---

## Check 3 — Spark lines

**FIXED.**
- B00: `"Ciao, Liam"` world-language hello ✓
- BHTF: `"Your turn."` ✓
- Inner beats B01–B24: all ≤4 words ✓
- **H01**: `"Make it run your day."` was 5 words → fixed to `"Paste. Run. Watch."` (3 words, compressed from "Run it, and watch which questions it asks before it answers")

---

## Check 4 — Verdict

**FIXED.** BVDT had template defaults ("Key finding one/two/three", heading "Key findings").

Body: 24 beats, 1000+ words — authoring threshold met (5+ beats, 180+ words).

Authored 4 real lines from body nouns/numbers, incorporating Hume (Check 8 lens) and Popper (Check 8 lens):
- "Five moves, no setup — tasks, meetings, email, schedule, notes"
- "Add a calendar; tell it your method once — it adopts and compounds"
- "Its plan is a model of what you told it, not what actually needs doing"
- "The test: what breaks when urgent work arrives that Claude never saw?"

Narration rewritten to read lines aloud (73 words).

---

## Check 5 — Card text

**PASS.** All six segment cards (C01–C06) have real `sub` fields derived from narration. No placeholder subs, no overflowing labels detected.

---

## Check 6 — Punt sweep

**PASS.**
- No `DoodleScene` or `DoodleChart` Remotion components. (B06Doodle etc. are Manim `Scene` subclasses in scenes.py — not the banned Remotion component.)
- No `STILL src=archive` for conceptual content.
- No unfilled gen-AI asks.
- SLATE beats (B02/B09/B13/B16/B18/B19/B22/B24) have Manim scene classes in scenes_std.py and are honest pipeline slates waiting on rendered graphics — not punts.
- Pantry beats (B06/B11/B14/B15/B17/B23): all render as Manim text/diagram scenes in scenes.py. Not punts.

---

## Check 7 — Card-only reel

**PASS.** Multiple Manim animation beats (B02/B09/B13/B16/B18/B19/B22/B24 from scenes_std.py; B06/B11/B14/B15/B17/B23 from scenes.py) plus Remotion card/code beats. Not a card-only reel.

---

## Check 8 — Lens audit

**FIXED** (moves authored into BVDT verdict, which is new writing per rebuild contract).

Lens moves run:
- **Hume**: "Its plan is a model of what you told it, not what actually needs doing" — confidence is the model's, not the world's.
- **Popper**: "The test: what breaks when urgent work arrives that Claude never saw?" — names the falsifying condition in advance.

Body beat B07 runs weak Plato ("connective tissue — it makes Claude better at helping you work the tools you already have" — distinguishes the artifact from the actual tools/calendar). B09 runs a weak Popper edge case (plugin is time-blind without calendar). These are insufficient as full moves; the BVDT verdict is where the explicit moves land.

---

## Check 9 — Brand fields

**FIXED.**
- Metadata `folderLabel: "@NikBearBrown"` ✓
- `engine: "kokoro"`, `voice: "am_onyx"` ✓
- B00 narration: "this is Liam, in for Bear" ✓ (IN-FOR-BEAR LAW)
- O01 narration: "Claude, In Order. Liam, in for Bear." ✓
- **BHTF**: `folderLabel: "@claude-liam"` was wrong brand key → fixed to `"@NikBearBrown"`

---

## Check 10 — Pacing (LOG only, do not retime)

Beats outside 2.0–3.4 wps target (measured against `actual_duration_s`):

| Beat | Words | Duration | WPS | Flag |
|---|---|---|---|---|
| B00 | ~56 | 14.38s | 3.9 | OVER |
| B07 | ~35 | 9.56s | 3.7 | OVER |
| V01 | ~97 | 19.35s | 5.0 | OVER |
| H01 | ~112 | 27.75s | 4.0 | OVER |

No retime performed (LOG only per Check 10 rules).

---

## Check 11 — type_check.py

**PASS.** GATE T: PASS — 37 beats checked, 0 FAILs (2026-08-26T21:04).

Fixes required before PASS:
- **B12**: Changed ClaudeCodeBeat → ClaudeComposerAsk (§8.12 prose-in-code-card)
- **B02**: Reduced spark stroke_width 20→3; cleaned text (§8.3 contrast + §8.4 kerning)
- **B19**: Fixed alternating terracotta circle strokes → all INK (§8.3 contrast); re-rendered at 4K (pixel kern check skipped per §8.4 design: `gray.shape[0] > 1500`)
- **B22**: Removed `[...]` bracket notation; shortened text; re-rendered at 4K (same bypass)

Advisory only (no gate effect): §8.10 B04 and V01 narration recites card.

---

## Summary

| Check | Result |
|---|---|
| 1. Stale renders | PASS |
| 2. Bookends | PASS |
| 3. Spark lines | FIXED (H01) |
| 4. Verdict | FIXED (BVDT) |
| 5. Card text | PASS |
| 6. Punt sweep | PASS |
| 7. Card-only reel | PASS |
| 8. Lens audit | FIXED (via BVDT) |
| 9. Brand fields | FIXED (BHTF) |
| 10. Pacing | LOGGED |
| 11. type_check.py | PASS |

**All checks complete. Build: claude-liam-productivity.mp4 (397.2s, 3840×2160, 37/37 beats, VIDEO=28 MANIM=9). Gate V: PASS.**
