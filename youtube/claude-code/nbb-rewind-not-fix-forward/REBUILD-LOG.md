# REBUILD-LOG — nbb-rewind-not-fix-forward

## Contract
- `beat_sheet.pre-rebuild.json` created byte-exact before any edit.
- Inner narration LOCKED (B00–B05 already locked to source; NBB00 / NBB01 kept).
- Placeholder narration authored where the template was clearly wrong.
- No datable-claim edits required (no versions/models/prices in the fixed text).

## Narration edits
- **NBB02** narration_text (Cancer/medical template — INVALID for this topic):
  old: `"Take this prompt, run it on your own — pick any cancer type or clinical scenario you know about and ask how this mechanism applies there."`
  new: `"Your turn. Open your last failed Claude Code session. Was your instinct to paste a correction, or to Esc-Esc? Copy the failed prompt in, add one sentence that closes the spec gap you now see, then rewind and rerun with the tighter spec."`
  Source: authored from B02 (Esc-Esc mechanics) + B03 (respec-one-sentence). Mirrors
  the source reel's BHTF narration for the same audience.
- **BVDT** narration_text: `""` → STRIPPED (redundant with NBB01 verdict).
- **BHTF** narration_text: `""` → STRIPPED (redundant with NBB02 your-turn).
- **BOUT** narration_text: `""` → STRIPPED (redundant with NBB03 outro).

## Prop edits
- **NBB00** `props.greeting`: `"Your turn."` → `"Guten Tag, Liam"` (cold open needs
  world-language hello; source used Croatian "Zdravo, Liam" — German is a rotation).
- **B00** `props.greeting`: `"Liam"` → `"Bonjour, Liam"` (bare "Liam" is not a spark;
  cold-open composer needs world-hello, rotating away from source's "Zdravo").
  Top-level `remotion.props.greeting` (already "Zdravo, Liam") kept as the shot's
  intended visual on the source clip; local B00 uses "Bonjour, Liam".
- **NBB01** `artifactLines[1]`: truncated mid-word at "…is not in Cla…"
  → `"Two rewinds on one row for the same failure — fix the spec, not the prompt."`
- **B01 FormBCard**: template `Key point one/two/three` (empty subs)
  → three authored items (Correction appends / Conditioned on both / Symptom moves),
  mirroring the source reel's B01 items (which were themselves authored from B01
  narration in the source's rebuild).
- **BVDT / BHTF / BOUT** beats: removed (see narration edits — empty-narration
  placeholders duplicating NBB01/NBB02/NBB03).

## Body asset routing
- B02/B03 originally referenced local `media/B02.mp4` / `media/B03.mp4` (never
  rendered here) via broken `Scene_B02_NbbRewindNot` / `Scene_B03_NbbRewindNot`
  scenes with `Text([:50])` truncation defects. Rerouted to the source reel's
  fresh, audit-passing manim renders at `../rewind-not-fix-forward/manim/B02.mp4`
  and `../rewind-not-fix-forward/manim/B03.mp4`.
- B00 / B01 / B04 / B05 already reference `../rewind-not-fix-forward/clips/*.mp4`
  as `source_clip` — those are freshly built (16:51). Local shot slots left as
  Remotion props; compile picks up source_clip.

## VOICE-LOCK
- Metadata already `engine: kokoro`, `voice: am_onyx`. No dead ElevenLabs fields
  present. Kokoro is the sole engine; no gates.

## Not changed
- Beat order for the retained beats.
- Narration for B00–B05 (source-locked), NBB00 (locked ask), NBB01 (locked verdict body),
  NBB03 (title-only).
- Metadata (title, slug, topic, palette, folderLabel `@NikBearBrown`).
