# REBUILD-LOG — nbb-vox-light-ceiling

Rebuild pass 2026-08-27. Locked-script contract observed (rebuild SKILL §Locked): no narration_text edits in body beats B01–B10.

## LOCKED (carried over verbatim)
- All body narration_text (B01–B10) — byte-for-byte.
- Beat order, act labels, t_start hints.
- shot intent (pattern/props/manim scene refs).
- metadata identity: title, slug (updated to `nbb-vox-light-ceiling`), topic, source pointer, register=Teardown.

## REBUILT
1. VOICE-LOCK: engine=kokoro, voice=am_onyx, voice_kokoro=am_onyx uniformly. Persona "Liam (in for Bear)" added.
2. Bookends: B00 spark line, canonical BVDT/BHTF/BOUT (renamed from NBB01/2/3, mp3 files renamed to match, three placeholder bookends deleted).
3. Metadata: added folderLabel + channel_title @NikBearBrown; dropped `old_outro_beats`; refreshed built_at.
4. Verdict body: BVDT.artifactHeading, artifactLines authored from body content.
5. Card content: B01 FormBCard items (real labels/subs/icons); B02 FormACard lines (three full-phrase replacements for the truncated narration fragment).
6. Audio: reused existing per-beat mp3s. No re-generation; kokoro Liam voice unchanged. Bookend mp3s renamed only (contents preserved).
7. Renders: Remotion (6 patterns) + Manim (6 scenes via ../vox-light-ceiling/vox_scenes.py).
8. Gates: content_check + frame_check + lane_check + CARD LINT + audio ≥ −40 dB — all PASS.

## Datable-claims pass
- No model/version/price strings in the narration. No edits triggered.

## Narration edits
- None to any body beat.
- Bookend narration_text (BVDT/BHTF/BOUT) unchanged from the NBB01/2/3 original — they carried authored recap/handoff/outro copy already.

## Envelope drops
- voice_id (ElevenLabs-era) — dropped.
- voice_env — dropped.
- clock prose fields — dropped.
- `old_outro_beats: [B11, B12]` — dropped from metadata (dangling; no such beats present).
