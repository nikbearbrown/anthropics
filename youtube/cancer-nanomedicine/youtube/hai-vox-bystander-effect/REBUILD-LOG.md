# REBUILD-LOG.md — hai-vox-bystander-effect

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-28 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B13) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06/B07/B08 THE MECHANISM · B09 THE IMPLICATION · B10 THE EXAMPLE · B11 RECAP · B12/B13 OUTRO.
- Metadata identity: title, topic, source pointer, color semantics, audience (HAI), register (Pragmatist), palette (humanitarians).
- Non-Claude channel skin retained: OutroSeries (B12) and OutroCTA (B13) — NOT Claude-washed. HAI reel: no Claude bookends (B00/BVDT/BHTF/BOUT) required per rebuild contract for a non-claude channel.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: qdEb53HLreRBCD1FQE30` DROPPED.
- Metadata `folderLabel: "@humanitariansai"` added (HAI channel handle, consistent with the OutroCTA `handle`).
- Metadata `short_title: "Same Antibody, Different Kill Radius"` added.
- Metadata `slug` corrected from `vox-bystander-effect` to `hai-vox-bystander-effect` (matches folder).
- Metadata `_variant_todo` block DROPPED — legacy migration checklist from the pragmatist/HAI variant rewrite; all items now done (register, tangent, outro, audio).
- Metadata `build` block (top-level) DROPPED — claimed `filled: 2/13` at 2026-07-16 with slates for B01–B11 and VIDEO for B12/B13, but no per-beat mp4 renders exist on disk. Fresh compile re-stamps.
- Per-beat `build` stamps DROPPED on all 13 beats — every SLATE stamp was from 2026-07-16 and B12/B13 claimed `VIDEO src: media/B##.mp4` with no `media/` directory on disk. Fresh compile re-stamps.
- Remotion `rendered.at` timestamps blanked on B02, B04, B06, B07, B08, B10, B11 (new Remotion patterns) and B12, B13 (OutroSeries/OutroCTA schema fix).

## Datable-claim edits

None. Narration cites biology mechanism (HER2-low expression, T-DM1/T-DXd, non-cleavable vs cleavable linker chemistry, membrane permeability, bystander effect) and one illustrative example block (B10) whose 5/40/8x numbers are the chapter's canonical illustrative sizing. No model names, no prices, no "as of" phrasing.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata._variant_todo` — legacy pragmatist/HAI variant migration checklist; all items done.
- `metadata.build` — stale 2026-07-16 stamp; zero per-beat mp4s on disk.
- Every `beats[].build` — same stale claim.

## Reel-level notes

- Persona coherence: narration is explainer voice with no first-person persona claim; outros carry Humanitarians AI attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent. HAI reel = HAI outros retained.
- The pre-rebuild sheet had SEVEN beats with `shot.type: "GRAPHIC"` and a `scene_class` referring to a Manim scene name (B02_TwoDrugs, B04_AntibodyOneStep, B06_TDM1Confined, B08_TDXdSpreads, B10_Example) or a `shot.type: "DOCUMENT"` (B05_NaiveGuess, B09_ImplicationQuote) or a `shot.type: "STILL"` (B07, but with a FormACard remotion slot). No `scenes.py` exists on disk, so all GRAPHIC beats were pipeline-owned SLATES lane_check would refuse in any master cut. Reshaped each GRAPHIC beat to a real Remotion pattern per rebuild contract (props may be re-shaped, intent locked):
  - B02 → `FormBCard` "T-DM1 vs T-DXd — identical antibodies, split outcomes" (3 items: T-DM1 / T-DXd / where the difference is not)
  - B04 → `FormBCard` "The antibody controls exactly one step" (3 items: what the antibody does / HER2-positive cells / the majority)
  - B06 → `FormBCard` "T-DM1 — non-cleavable linker traps the payload" (3 items: the linker / the freed payload / what charge means)
  - B07 → `FormACard` (3 lines: kills only the cell it entered / neighbors survive / one binding equals one kill)
  - B08 → `FormBCard` "T-DXd — cleavable linker frees a permeable payload" (3 items: the linker / the freed payload / the bystander effect)
  - B10 → `FormBCard` "HER2-low patch — same 5 entry points, different kill count" (3 items: antibody reach / T-DM1 / T-DXd)
  - B11 → `FormACard` (3 lines: same antibody different payload / T-DM1 confined by charge / T-DXd spreads by permeability)
- The `production_viz` mechanic + `graphic.manim` scene name are RETAINED alongside the Remotion routing — a future full-render pass can author these into a real Manim scenes file without another rebuild.
- Card beats (B01 title, B03 question) and DOCUMENT quote beats (B05, B09) render as slate request cards — legit for this review-slate cut, not pipeline-owned. Their `card`/`document` structs describe what a future full-render pass would bind.
- B12 `OutroSeries` and B13 `OutroCTA` props corrected to the current Root.tsx schema (`eyebrow`+`line` / `line`+`handle`). Old sheet passed `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` which Remotion silently fell back to Root.tsx defaults `CLAUDE COWORK` / `Part of the Claude Cowork series.` / `@nikbearbrown` — Claude-washing a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`. Props reshape only; intent (HAI series sign-off + HAI CTA) is locked.
