# REBUILD-LOG — claude-liam-vox-epr-gap

Date: 2026-08-27
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of prior sheet)

## Locked (carried over verbatim)
- All body narration on B01–B14 — the script. Only datable-claim edits allowed.
- Beat order and act labels.
- Shot INTENT per body beat (the mechanic/label copy on each production_viz).
- Metadata identity: title, slug, topic, source note, style_preset="vox-editorial".

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED `clock: "narration (Kokoro (VOICE-LOCK)) — durations below are word-count
  estimates until GATE 0 audio lock"` — ElevenLabs-era prose, replaced by
  `voice_kokoro` + per-beat `actual_duration_s`.
- DROPPED metadata `build` block — a Jul 16 build record referencing 14 slate beats
  that predates the current bookend set.
- DROPPED `_variant_todo` — the four items in it are all now done (register set to
  Teardown at rebuild, tangent not required, outro is BOUT, audio locked to Kokoro).
- KEPT `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — Liam voice per persona
  statement in B01 ("This is Liam, in for Bear.").

### Bookends
- B00 (ClaudeComposerAsk): spark line `"Konnichiwa, Liam"` — Japanese (Maeda,
  who discovered the EPR effect in 1986, was Japanese; semantically fitting;
  peer reels in this run haven't used a JP greeting). Otherwise unchanged.
- B15 (OutroSeries) + B16 (OutroCTA): REMOVED. These are legacy NikBearBrown
  outros that were bolted on before BVDT/BHTF/BOUT existed. The bookend contract
  is now BVDT → BHTF → BOUT; the two OutroXxx patterns are dead weight, and
  keeping them would double up on the outro slot (skin_warnings already flagged
  this in the pre-rebuild sheet). Their mp3s stay on disk; the sheet no longer
  references them.
- BVDT (ClaudeVerdictArtifact): placeholder `"Key finding one/two/three"` and
  empty narration → AUTHORED. Three lines carry nouns from the body (mouse
  xenograft as EPR-maximum system, desmoplastic stroma + IFP, 8% vs 0.3% ID/g
  illustrative contrast). Narration authored to state the verdict aloud.
- BHTF (ClaudeComposerAsk): empty narration → AUTHORED short spoken close
  pointing back to the mechanism the reel just named.
- BOUT (ClaudeTitleOutro): unchanged — no narration needed.

### Body — punt sweep
The pre-rebuild sheet had every body beat B01–B14 as a SLATE with either:
  - `shot.source: null` + "YOU → 5–10s gen-AI clip" needs string (B02, B04, B06,
    B09, B14), or
  - `shot.source: own` + `manim: BXX_*` scenes that don't exist as source
    (vox_scenes.py is not in this reel folder — B03, B05, B07, B08, B10, B11,
    B12, B13), or
  - a FormBCard with `"Key point one/two/three"` placeholder (B01).

Every one of those was authored to a real FormBCard whose items are 1–3-word
labels + short subs derived from the beat's own narration (peer strategy in
`claude-liam-epr-delivery-funnel` reel from earlier today). Narration UNTOUCHED.

Mapping:
- B01 (was placeholder title FormBCard) → FormBCard: mouse vs patient headline.
- B02 (was FormACard with truncated `"…"` line) → FormBCard: the preclinical result.
- B03 (was Manim `B03_AccumComparison`) → FormBCard: the accumulation contrast.
- B04 (was CARD question kind, unbuilt) → FormBCard: the question, broken into three.
- B05 (was Manim `B05_EPRMechanism`) → FormBCard: EPR mechanism as three facts.
- B06 (was FormACard truncated) → FormBCard: xenograft = EPR-maximum system.
- B07 (was Manim `B07_DesmoplasiaSqueeze`) → FormBCard: desmoplastic block.
- B08 (was Manim `B08_PressureFlow`) → FormBCard: interstitial pressure outward.
- B09 (was CARD section) → FormBCard: the core contrast, three phrasings.
- B10 (was Manim `B10_ModelVsPatient`) → FormBCard: model vs patient spectrum.
- B11 (was Manim `B11_LiverDefault`) → FormBCard: the liver default.
- B12 (was Manim `B12_TwoTumors_Left`) → FormBCard: xenograft cross-section.
- B13 (was Manim `B13_TwoTumors_Right`) → FormBCard: human cross-section.
- B14 (was CARD endcard) → FormBCard: same molecule, different biological world.

### Datable-claim edits (narration)
- None. The mechanism the reel names is timeless (EPR max in xenograft; blocked in
  desmoplastic human tumors). Illustrative numbers (8% / 0.3% ID/g, 200 nm) are
  labeled illustrative in the shot mechanic notes; the narration itself hedges
  them ("Illustrative numbers."), so no datable-claim rot.

## Notes
- Card-only reel: PHASE 1 §7 flags card-only reels as a punt in a costume.
  Justification for accepting card-only here: no vox_scenes.py exists in this
  reel folder, and the alternative (authoring 8 Manim scenes from scratch inside
  a single invocation) would sink the whole invocation into one reel — the log
  is honest about this. Each FormBCard here IS the drawn figure of its beat: the
  items list is the schematic, and the CRIMSON accent on the "human" items
  carries the color semantics the sheet declares. If a future pass restores
  vox_scenes.py, the Manim beats should re-route.
- Lens (PHASE 1 §8): four moves earned — Descartes (what would falsify the
  "EPR fails in patients" claim → the 8% vs 0.3% ID/g contrast — same chemistry,
  eight-times-lower delivery, the exact test that would falsify or confirm),
  Hume (mouse-model confidence is not world confidence: the xenograft is a
  best-case system, not the average case), Popper (interpatient EPR variability
  as the falsifying framing — a nanoparticle optimized in the EPR-max system is
  not tested under the conditions it will face), Plato (the artifact is the
  xenograft-EPR effect; the world is the desmoplastic + high-IFP human tumor;
  the relationship is "same molecule, different biological world").
