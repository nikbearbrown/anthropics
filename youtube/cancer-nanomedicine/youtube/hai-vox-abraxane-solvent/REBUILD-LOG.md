# REBUILD-LOG.md — hai-vox-abraxane-solvent

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-28 before any edit.

## LOCKED (unchanged)

- Every body `narration_text` (B01–B17) is verbatim from the pre-rebuild sheet.
- Beat order: B01 COLD OPEN → B02 COLD OPEN → B03 THE PROBLEM → B04 THE QUESTION → B05/B06 THE MECHANISM → B07/B08 THE FIX → B09 THE PAYOFF → B10/B11 IN PRACTICE → B12/B13 THE FRAME → B14 THE EXAMPLE → B15 RECAP → B16/B17 OUTRO. Act labels added where the pre-rebuild sheet omitted them; act sequence itself is derived from the locked narration and shot-list intent.
- Metadata identity: title, topic, source pointer, color semantics, style bible, audience, register, palette, HAI outro source.
- Non-Claude channel skins retained: OutroSeries (B16) and OutroCTA (B17) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) — legit per rebuild contract for a non-claude channel.
- Every GRAPHIC beat's `production_viz.mechanic` (the shot-list intent) preserved verbatim; only the pattern that carries it changed.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with OutroCTA `handle: "@humanitariansai"`).
- Metadata `short_title: "The Solvent Was the Danger"` added (§8.5 pull-quote limit; the full title is 12 words).
- Metadata `slug` corrected from `vox-abraxane-solvent` → `hai-vox-abraxane-solvent` (matches folder).
- Metadata `source` added, mirrors the source pointer already in `purpose`.
- Metadata `_variant_todo` block DROPPED — legacy pragmatist/HAI variant migration checklist; all four items were done (register, tangent, outro, audio) prior to this pass.
- Metadata `build` block (top-level) DROPPED — claimed `filled: 2/17` at 2026-07-16 with slates for B01–B15 and VIDEO for B16/B17, but no per-beat mp4 renders exist on disk. Fresh compile re-stamps.
- Per-beat `build` stamps DROPPED on all 17 beats — every SLATE stamp was from 2026-07-16 and B16/B17 claimed `VIDEO src: media/B##.mp4` with no `media/` directory on disk. Fresh compile re-stamps.
- Remotion `rendered.at` timestamps blanked on all beats with a `remotion` block.

## Routing decisions (GRAPHIC → REMOTION)

GRAPHIC beats had `graphic.manim` scene names (`B03_InsolubilityProblem`, `B05_CremophorCascade`, `B07_AlbuminBinding`, `B08_SolventDrain`, `B09_ComparisonBars`, `B11_TwoBagComparison`, `B13_TimelineSummary`, `B14_ExampleSideBySide`) but no `scenes.py` in-folder — that made them pipeline-owned SLATES which lane_check refuses. Reshaped each to a real Remotion pattern per rebuild contract (props reshaped, intent locked):

- B03 → `FormBCard` "Paclitaxel Won't Dissolve in Water" (2 items: Nearly insoluble / Needs a solvent)
- B05 → `FormBCard` "How Cremophor Triggers Reactions" (3 items: Surfactant / Mast cells fire / The cascade)
- B07 → `FormBCard` "Abraxane: Protein Instead of Solvent" (3 items: Albumin / Binds paclitaxel / ~130 nm particle)
- B08 → `FormBCard` "Solvent Gone, Trigger Gone" (2 items: No Cremophor / Familiar protein)
- B09 → `FormACard` (4 lines: illustrative payoff numbers)
- B11 → `FormBCard` "Bag B — Abraxane" (3 items: Albumin-bound / No filter / Same molecule)
- B13 → `FormBCard` "Two Eras, One Drug" (2 items: Taxol era / Abraxane era)
- B14 → `FormBCard` "Same Patient, Two Bags (Illustrative)" (2 items: Bag A — Taxol / Bag B — Abraxane, each with illustrative % chip)

B02 and B10 kept their pre-rebuild `STILL src=ai` intent as `image_prompt` for a future full-render pass but route to `FormACard` for the review cut — this is the shipping render; the image_prompt is a scripting-gap flag, not a pipeline-owned slate.

## Datable-claim edits

None. Narration cites biology mechanism (surfactant, mast-cell activation, histamine, albumin, ~130 nm nanoparticle) and one illustrative comparison block (B09/B14) that is explicitly labeled `illustrative` in the narration and in `graphic.production_viz.note`. No model names, prices, or "as of" phrasing.

## Card-copy tightens (shot reshapes, intent locked)

Title/section/endcard `copy`/`sub` shortened where the pre-rebuild copy would have overflowed the safe box or violated §8.5. Every reshape preserves the beat's teaching intent; the narration_text (the locked script) is untouched.

- B01 title CARD: `copy "The Cancer Drug Where the Solvent, Not the Drug, Was the Danger" / sub "why the IV bag itself was the hazard"` → `copy "The Solvent Was the Danger" / sub "For decades, Taxol's hazard was the IV bag itself."` (matches new `short_title`; full title stays as metadata title)
- B04 question CARD: `copy` compressed from the full four-sentence narration snippet to `"The drug didn't change." / sub "What did — and why did the reactions stop?"` (question intent locked)
- B12 section CARD: `copy "A formulation fix — not a tumor-targeting story" / sub ""` → `copy "A formulation fix" / sub "Not a tumor-targeting story."` (empty sub filled from own copy)
- B15 endcard CARD: `sub "Abraxane's benefit: albumin dissolved paclitaxel without Cremophor — the hypersensitivity disappeared."` → `sub "Cremophor was the hazard. Albumin removed it."` (compressed to fit safe box; both are drawn from the locked narration)

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (`mp3/timings.json` + per-beat `actual_duration_s`).
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is third-person explainer voice with no persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- Fresh compile re-stamps `metadata.build` and per-beat `build.status`.
