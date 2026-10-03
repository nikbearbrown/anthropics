# REBUILD-LOG.md — hai-vox-endosomal-escape

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild sheet, made 2026-08-30 before any edit.

## LOCKED (unchanged)

- Every body `narration_text` (B01–B13) is verbatim from the pre-rebuild sheet.
- Beat order: B01/B02 COLD OPEN → B03 THE QUESTION → B04/B05 THE PROBLEM → B06/B07 THE MECHANISM → B08 THE IMPLICATION → B09/B10 THE EXAMPLE → B11 RECAP → B12/B13 OUTRO. Act labels were already present on every beat in the pre-rebuild sheet; nothing added or moved.
- Metadata identity: title, topic, source pointer, color semantics, style bible, audience, register, palette, HAI outro source.
- Non-Claude channel skins retained: OutroSeries (B12) and OutroCTA (B13) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) — legit per rebuild contract for a non-claude channel.
- Every GRAPHIC beat's `graphic.production_viz.mechanic` (the shot-list intent) preserved verbatim; only the pattern that carries the render changed.
- B10 DOCUMENT quote text, attribution, highlight_words preserved verbatim.

## REBUILT (regenerated)

- Metadata voice envelope normalized: `engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`. ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with OutroCTA `handle: "@humanitariansai"`).
- Metadata `short_title: "The Charge Flip Is the Drug"` added — drawn from B11 endcard copy, itself compressed from the locked B11 narration. §8.5 pull-quote limit; the full title runs 12 words.
- Metadata `total_estimated_duration_seconds` corrected from `189.5` to `164.67` — sum of measured `actual_duration_s` per beat from `mp3/timings.json`.
- Metadata `_variant_todo` block DROPPED — legacy pragmatist/HAI variant migration checklist; all four items were already reflected in the pre-rebuild sheet (register: Pragmatist, palette: humanitarians, outro_source: HAI, HAI audio measured on disk).
- Metadata `build` block (top-level) DROPPED — claimed `filled: 2/13` at 2026-07-16 with slates for B01–B11 and VIDEO for B12/B13, but zero per-beat mp4 renders exist on disk. Fresh compile re-stamps.
- Per-beat `build.at` stamps blanked to `null`; `build.status` set to VIDEO (renders about to happen) or SLATE (declared review-cut placeholder). B12/B13 kept status VIDEO — OutroSeries/OutroCTA render deterministically at compile time from their props. Fresh compile re-stamps `at`.
- Every Remotion `rendered.at` blanked.
- B12 `remotion.props` reshaped: pre-rebuild used `seriesTitle` / `tagline` / `githubSlug`, but the current `OutroSeries.tsx` schema (`runtime/remotion/src/scenes/OutroSeries.tsx`) is `{eyebrow, line}`. Reshaped to `eyebrow: "CANCER NANOMEDICINE"`, `line: "Part of the Cancer Nanomedicine series from Humanitarians AI."` — narration line preserved. Stale props would have failed zod.
- B13 `remotion.props` reshaped: pre-rebuild used `authorName` / `handle` / `ctaText`, but the current `OutroCTA.tsx` schema is `{line, handle}`. Reshaped to `line: "Find more at humanitarians.ai."`, `handle: "@humanitariansai"`.

## Routing decisions (GRAPHIC → REMOTION)

GRAPHIC beats had `graphic.manim` scene names (`B04_Endocytosis`, `B05_pHDrop`, `B06_ChargeFlip`, `B07_MembraneCrack`, `B08_EscapeFraction`, `B09_LNPComparison`) but no `scenes.py` in-folder — that made them pipeline-owned SLATES which the lane check refuses. Reshaped each to a real Remotion pattern per rebuild contract (props reshaped, mechanic intent locked and preserved verbatim under `graphic.production_viz`):

- B04 → `FormBCard` "Endocytosis — The Trap Forms" (3 items: Membrane wraps / Vesicle pinches off / Default fate)
- B05 → `FormBCard` "The Endosome Acidifies" (3 items: Proton pumps fire / pH 7.4 → 5.5 / Digestion primed)
- B06 → `FormBCard` "The Charge Flip" (3 items: Amine head group / pH 7.4 — neutral / pH 5.5 — cationic) — THE KEY BEAT
- B07 → `FormBCard` "Membrane Rupture — RNA Escapes" (3 items: Opposites attract / Bilayer destabilizes / RNA reaches cytosol)
- B08 → `FormACard` (4 lines: illustrative escape-fraction beat)
- B09 → `FormBCard` "Neutral vs Ionizable (Illustrative)" (3 items: LNP-A / LNP-B / One variable — with 8% and 84% carrying the word "illustrative" as the source card requires)

B02 kept its pre-rebuild `STILL src=ai` intent as `image_prompt` for a future full-render pass but routes to `FormACard` for the review cut — this is the shipping render; the image_prompt is a scripting-gap flag, not a pipeline-owned slate.

## Datable-claim edits

None. Narration cites biology mechanism (endocytosis, proton pumps, amine protonation, electrostatic bilayer disruption, RNAi machinery) and one illustrative comparison block (B09) that is explicitly labeled `illustrative` in the reshaped card and in `graphic.production_viz.note`. No model names, prices, or "as of" phrasing anywhere.

## Card-copy tightens (shot reshapes, intent locked)

Title/section/endcard `copy`/`sub` shortened where the pre-rebuild copy would have overflowed the safe box or violated §8.5. Every reshape preserves the beat's teaching intent; the narration_text (the locked script) is untouched.

- B01 title CARD: `copy "The pH-Triggered Lock That Lets RNA Drugs Escape the Cell's Trash" / sub "why a drug that works in a dish fails in a body"` → `copy "The Charge Flip Is the Drug" / sub "why an siRNA that works in a dish fails in a mouse."` (matches new `short_title`; full title stays as metadata `title`; sub sharpened from "body" → "mouse" to match the narration's own contrast — dish vs mouse).
- B01 title CARD: `eyebrow "CANCER NANOMEDICINE"` added (present on abraxane-solvent sibling; consistent with topic).
- B03 question CARD: `copy "How does the ionizable lipid solve the endosomal trap?" / sub "the gap formula: siRNA works in a dish but not in a mouse — why?"` → `copy "How does the ionizable lipid open the trap?" / sub "the siRNA gap — works in a dish, fails in a mouse."` (compressed to fit safe box; question intent locked).
- B11 endcard CARD: `copy "Neutral in blood. Cationic in the endosome. That charge flip is the drug." / sub "CANCER NANOMEDICINE"` → `copy "The charge flip IS the drug." / sub "Neutral in blood. Cationic in the endosome."` (compressed; the topic reveal moved to `eyebrow` for the endcard convention on siblings; the poster-verdict claim promoted to `copy`).
- B11 endcard CARD: `eyebrow "CANCER NANOMEDICINE"` added.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (`mp3/timings.json` + per-beat `actual_duration_s`).
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build.at` stamp — same stale claim.

## Reel-level notes

- Persona coherence: narration is third-person explainer voice with no persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- Verdict is authored, not templated: B11 endcard "The charge flip IS the drug. / Neutral in blood. Cationic in the endosome." is drawn from B11's own locked narration and would not be true of any other reel.
- Fresh compile re-stamps per-beat `build.at` and Remotion `rendered.at`.
