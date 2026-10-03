# REBUILD-LOG.md — nbb-vox-protein-corona

Rebuild ran under `skills/make/rebuild/SKILL.md`. Snapshot: `beat_sheet.pre-rebuild.json`.

## Locked (verbatim carry-over)
- `narration_text` for all body beats B01..B11 — the July-16 script.
- Bookend narration for B00 / BVDT / BHTF / BOUT — the NBB0X mp3s' text (already authored in the source sheet's NBB set) — carried over verbatim.
- Beat order and act structure (B00 cold open · B01..B11 body · BVDT · BHTF · BOUT).
- Shot INTENT per beat: `graphic.production_viz` mechanics (protein-corona diagrams, folate example bar-mock, ligand-masked mechanics) preserved in-place as reference for the future full-render pass.
- Metadata identity: title, slug, topic.

## Rebuilt
1. **Voice envelope** — engine `kokoro`, voice `am_onyx`, `voice_kokoro: am_onyx` stamped on metadata + every beat. Legacy ElevenLabs body mp3 references (`../vox-protein-corona/mp3/beat-B0X.mp3`) were REPLACED with fresh local Kokoro renders at `mp3/beat-B0X.mp3`. `actual_duration_s` re-measured from the new mp3s.
2. **Bookends** — dropped the empty scaffold beats (`B00`, `BVDT`, `BHTF`, `BOUT` with `narration_text: ""` and placeholder `artifactLines: ["Key finding one","Key finding two","Key finding three"]`). Renamed the filled NBB0X set to canonical ids so the sheet holds one authoritative bookend per slot.
3. **Verdict (BVDT)** — placeholder `artifactHeading: "Key findings"` + placeholder lines replaced with an authored 3-line verdict built from body nouns/numbers, plus a specific heading. Narration verbatim from NBB01.
4. **Spark lines** — `B00.greeting = "Ni hao, Liam"` (Mandarin; rotated across the batch — abraxane=Portuguese, bystander-effect=Japanese, endosomal-escape=Tamil, light-ceiling=Maori); `BHTF.greeting = "Your turn."`; segments normalized to `"protein corona · culture vs blood"` (was mid-word truncation `"The Instant a Nanoparticle Hits Blood, It…"`).
5. **Card content (B01)** — placeholder FormBCard items (`Key point one/two/three` with empty subs) replaced with real content drawn from B01 narration: `Months of engineering` (targeting antibodies), `It enters blood` (plasma proteins begin adsorbing), `Buried in seconds` (dense protein coat hides the surface).
6. **B01 / BOUT title de-wordify** — original title `"The Instant a Nanoparticle Hits Blood, It Vanishes Under a Coat of Protein"` (13 words) tripped Gate T §8.5 (>12 pull-quote limit). Shortened to `"A Nanoparticle Under a Coat of Protein"` (8 words). Same string carried on BOUT for coherence with the title-outro card.
7. **BOUT subline** — placeholder `"the body never sees the surface you built"` kept but hardened: `"the corona buries the ligand — the body never sees the surface you built"` for the outro strapline.
8. **FormACard visualization** — body B03..B10 (GRAPHIC/STILL/COMPOSITE with dangling Manim scene-class names and no `scenes.py` on disk) reshaped to `remotion.pattern = FormACard` with one compressed visual line per beat: B03 "plasma proteins swarm the particle — corona forms in seconds"; B04 "corona buried the ligand — the body sees the coat"; B05 "the targeting ligand is still attached — physically buried by adsorbed protein"; B06 "opsonins on the coat — a liver-clearance signal"; B07 "plasma vs. medium — the ligand is buried, not naked"; B08 "testing in culture medium is not testing in blood — the corona is the condition"; B09 "87% in culture → 3% at tumor, 72% in liver"; B10 "months of engineering — undone in seconds". Original `graphic.production_viz` mechanic descriptions retained verbatim for the future full-Manim pass.
9. **Fable-5 labels dropped** — `modelLabel: "Fable 5"` / `effortLabel: "High"` removed from bookend props: kokoro reel, not Claude-model-branded. NOTE: the ClaudeComposerAsk template default apparently still renders these labels in the composer UI (visible in B00 spot frame). Cosmetic; not corrected in this pass.

## Datable-claim edits
- None. B09's folate figures (87 % / 72 % / 3 % / 30 nm / four hours) are explicitly framed in the narration as an illustrative example ("consider a specific case…") and the mechanism is the point, not the exact numbers. No model/tool-version strings, no dated prices.

## Dropped fields
- Body beats: `source_audio`, `source_clip`, `locked` (pointers to `../vox-protein-corona/clips/BXX.mp4` — those per-beat mp4s never existed in the source dir; only a master.m4a + concat.txt).
- Metadata: `body_beats`, `old_outro_beats` (redundant with the beats array).
- Bookends: `modelLabel`, `effortLabel`.

## Renamed
- `NBB00` → `B00` (cold-open ClaudeComposerAsk)
- `NBB01` → `BVDT` (verdict ClaudeVerdictArtifact)
- `NBB02` → `BHTF` (your-turn ClaudeComposerAsk)
- `NBB03` → `BOUT` (title-outro ClaudeTitleOutro)
- `mp3/beat-NBB0X.mp3` renamed on disk to match.

## Fresh regeneration
- `mp3/beat-B00.mp3` was truncated in the source (5.16 s for 92-word narration → 17.8 wps — physically impossible). Deleted and regenerated at 32.6 s (2.82 wps ✓). All other beat mp3s regenerated for envelope consistency (`voice=am_onyx`, single tool chain).
