# REBUILD-LOG — rewind-not-fix-forward

## Contract
- `beat_sheet.pre-rebuild.json` created byte-exact before any edit.
- Narration LOCKED for inner body beats. Bookend narration authored where empty.
- No datable-claim edits required (no versions/models/prices in body).

## Narration edits
- **BVDT** narration_text: `""` → *"The quiet signal is two rewinds on one row for the same failure. If it fires, stop typing new prompts. Open the handoff condition next to the SDD and ask which one is missing the constraint. The fix is upstream — in the document, not in the next attempt."*
  Source: authored from B04's own narration (verdict body beat) — nouns/numbers only.
- **BHTF** narration_text: `""` → *"Your turn. Open your last failed Claude Code session. Was your instinct to paste a correction, or to Esc-Esc? Copy the failed prompt in. Add one sentence that closes the spec gap you now see. Rewind, then rerun with the tighter spec."*
  Source: authored from B02/B03 method (Esc-Esc + one-sentence respec).

## Prop edits
- B00 `props.greeting` "Liam" → "Zdravo, Liam" (metadata already Zdravo; §3 spark line contract).
- B01 FormBCard: template `Key point one/two/three` → real items authored from B01 narration.
- B04 shot: added `remotion.pattern: FormBCard` with real items (was `motion: stagger` only, no pattern — would have slated).
- BVDT artifactLines: template `Key finding one/two/three` → three artifact lines authored from body verdict.
- BHTF command: template `Take what you learned from [ ... ]` → real exercise using B02/B03 method; empty `output` filled with three real next-step lines.

## Scene edits (scenes_std.py — §5b chart-text rule)
- **Scene_B01_RewindNotFix**: unused (Remotion FormBCard now renders B01); stub retained.
- **Scene_B02_RewindNotFix**: rewritten from truncated `Text(narration[:50])` labels to
  short category nouns: two-column "Fix-forward" (adds context) vs "Rewind" (Esc-Esc / /rewind),
  one complete bottom caption "Rewind restores state to before the last prompt."
- **Scene_B03_RewindNotFix**: rewritten to three-stage pipeline "Rewind → Add one sentence → Rerun"
  with terracotta accent on the middle (respec) stage. Bottom caption: "Shorter context, tighter
  spec, better output." No mid-word truncation, no narration fragments.

## VOICE-LOCK
- Metadata already `engine: kokoro`, `voice_kokoro: am_onyx`. No dead ElevenLabs fields present.

## Not changed
- Beat order, act labels, all inner narration (B01-B06).
- Metadata (title, slug, brand, folderLabel `@NikBearBrown`).
