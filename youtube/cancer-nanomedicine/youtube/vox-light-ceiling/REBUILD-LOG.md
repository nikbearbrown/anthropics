# REBUILD-LOG — vox-light-ceiling

Run: 2026-08-28 filmloop pass.

## Locked script (no narration edits)

Zero narration text changed in this pass. All 12 beats' `narration_text` fields
carry forward byte-identical from `beat_sheet.pre-rebuild.json`. All `actual_duration_s`
values preserved (audio locked 2026-07-08, mp3s under `mp3/beat-B*.mp3`).

## Envelope changes (VOICE-LOCK normalize)

| Field | Old | New | Reason |
|---|---|---|---|
| metadata.voice_id | "TyW6NH39JcFb5M3xdIIk" | *(dropped)* | ElevenLabs-era dead field per VOICE-LOCK contract |
| metadata.clock | "narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock" | *(dropped)* | ElevenLabs-era clock prose; audio is already locked |
| metadata.engine | *(missing)* | "kokoro" | describes the audio engine used for existing mp3s and any regeneration |
| metadata.voice | *(missing)* | "am_onyx" | describes the Kokoro voice used by the file-loop supervisor |
| metadata.folderLabel | *(missing)* | "@NikBearBrown" | channel handle matches B12 OutroCTA `handle` |

## Shot metadata cleanup

- **B02**: removed the `shot.remotion.FormACard` block. This scaffold contradicted
  the beat's declared identity (`shot.type: STILL`, `shot.source: ai`,
  `image_prompt` describing an endoscopy photograph). FormACard is a text card
  pattern; the beat is an AI photo slot. The block was scaffold leftover from an
  earlier rebuild pass and had no downstream effect (vox_compile resolves slots
  by file existence in media/ or manim/). Kept only `{type: STILL, source: ai,
  motion: kenburns}`. B02 remains a declared slate for this review cut.

## Pre-rebuild backup

`beat_sheet.pre-rebuild.json` — 13855 B, byte-exact copy of the incoming sheet
taken before any edit this run.
