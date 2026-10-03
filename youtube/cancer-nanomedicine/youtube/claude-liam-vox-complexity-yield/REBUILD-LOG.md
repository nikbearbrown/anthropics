# REBUILD-LOG — claude-liam-vox-complexity-yield
_2026-08-28_

Locked-script rebuild per `skills/make/rebuild/SKILL.md`. `beat_sheet.pre-rebuild.json`
captured byte-exact BEFORE any edit (cksum verified).

## Narration changes (locked script)

All body narration (B01–B11, B12, B13) unchanged. Bookend-lane narration authored where
the sheet was empty; that is not a script edit — the locked-script rule protects existing
narration from paraphrase, it does not forbid authoring new bookend content that the
original sheet left blank.

| Beat | Change | Source |
|------|--------|--------|
| B00 | greeting: `"Liam"` → `"Guten tag, Liam."` | props.greeting spark-line rotation; no adjacent reel uses German |
| BVDT | narration_text: `""` → 55-word verdict | authored from body's own numbers (0.9^6, 90%, 53%, 11/12, 7/12) |
| BVDT | artifactLines: template `Key finding one/two/three` → 3 real lines | authored from body |
| BVDT (round 2) | artifactLines[0]: `"0.9^6 = 53%. …"` → `"Six functions at 90% reproducibility multiplies to 53% batch pass."` | ClaudeVerdictArtifact renderer stripped the leading `0.` as ordered-list ordinal; rewritten to avoid the collision |
| B01 | FormBCard items: `Key point one/two/three` + empty `sub` → 3 authored items with subs | from B01's own narration |

## Envelope edits
- Dropped dead `voice_id` (ElevenLabs era) and legacy `clock` prose.

## Shot-form derivation
Every beat's `shot.remotion.pattern` or `shot.type=GRAPHIC` derives from its declared
pattern/production_viz. Six Manim scenes authored in `scenes_std.py` from the beat's
`graphic.production_viz.mechanic` prose. Newsprint palette (#F3EBDD ground / #2F2A26 ink
/ #1F6F5C teal / #BF3339 crimson / #F5D061 gold) matches metadata.color_semantics.

## Compile order (mp4 must be newest)
1. Sheet edits (Phase 0 + Phase 1) — first.
2. Audio: `generate_audio_kokoro.py --only BVDT` (stamps sheet).
3. Manim: 6 scenes → `manim/Bxx.mp4`.
4. Remotion: 8 patterns → `media/Bxx.mp4` (stamps sheet).
5. compile.py --review → `vox-complexity-yield-slate.mp4`.
6. Post-compile BVDT fix required → re-rendered BVDT + recompiled so the mp4 mtime
   remains newer than the sheet mtime (verified: mp4 15:54:50, sheet 15:54:41).
