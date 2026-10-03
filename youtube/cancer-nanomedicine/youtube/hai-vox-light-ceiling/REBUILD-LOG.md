# REBUILD-LOG — hai-vox-light-ceiling

Rebuild pass 2026-08-30. Pre-rebuild snapshot saved to `beat_sheet.pre-rebuild.json`.

## LOCKED (carried verbatim)

- All narration_text across B01–B12 — no edits. No datable claims to correct.
- Beat order, act labels, estimated_duration_s.
- All measured `actual_duration_s` from the July 16 audio pass.
- Metadata identity: slug, title, topic, source, register (Pragmatist), palette
  (humanitarians), outro_source (Humanitarians AI), audience (HAI).
- Manim graphic intent (B04–B09) — production_viz mechanic and colors kept as
  the shot list; they render as slates in this cut.

## REBUILT (envelope + machinery only)

1. **Dead ElevenLabs fields DROPPED** from metadata:
   - `voice_id: "qdEb53HLreRBCD1FQE30"`  → removed (ElevenLabs id, not in use)
   - `clock: "narration (Kokoro (VOICE-LOCK)) — durations below are word-count …"` → removed (dead prose)
   - `_variant_todo` array → removed (rebuild done, no longer applicable)
   - `build` metadata block from the July 16 slate cut → removed (stale)
2. **VOICE-LOCK per beat.** Every beat now carries `engine: kokoro`,
   `voice_kokoro: am_onyx`, `voice: am_onyx` — the sheet-level lock, echoed
   per-beat so nothing can drift.
3. **`folderLabel: @HumanitariansAI`** added at metadata level (HAI channel).
4. **`shot.form` derived** per beat from the locked pattern/intent
   (title-card / contrast-card / question-card / manim-* / endcard / outro-*).
5. **Punt costumes rewritten to real Remotion patterns**:
   - B01 was `SLATE, needs: YOU → 5–10s gen-AI clip → pantry` — a card-in-a-punt-hat.
     Rewritten to `FormACard` with the title + subtitle text from the locked `card.copy/sub`.
   - B02 was `SLATE, needs: YOU → gen-AI endoscopy still` — the narration is a stat
     contrast, not a photo. Rewritten to `FormACard` with three compressed lines
     built from the locked narration ("10× drug concentration. Reached both tumors.
     Only one cleared.").
   - B03 was `SLATE, needs: YOU → gen-AI clip` — narration is a question. Rewritten
     to `FormACard` with the surface/deep/delivery/why lines compressed from the
     locked narration.
   - B10 was `SLATE, needs: YOU → gen-AI endcard` — narration is a recap. Rewritten
     to `FormACard` with the endcard copy from the locked `card.copy/sub`.
6. **B04–B09** kept as declared Manim slates — they need real Manim scenes
   before final; slate is honest for a review cut. (PIPELINE-CARD RULE: allowed
   only for the review-slate cut; a `-slate.mp4` name is required.)
7. **B11 OutroSeries / B12 OutroCTA** kept intact — these are the HAI channel's
   own outro skin (`@humanitariansai`, humanitarians tagline). Per rebuild
   contract, "Non-claude channels keep their own skins — never Claude-wash an
   open or outro." No BVDT/BHTF/BOUT Claude bookends added; the HAI outros are
   the reel's own bookends.

## Narration edits — datable claims

None. Every narration line carried over byte-for-byte. The reel uses no model
names, no versions, no prices, no "as of" dates.
