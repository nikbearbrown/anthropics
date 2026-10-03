# REBUILD-LOG — claude-liam-vox-delivery-funnel

Date: 2026-08-28
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of prior sheet)

## Locked (carried over verbatim)
- All body narration on B01–B11 — the script. No datable-claim rot present.
- Beat order and act labels (COLD OPEN / THE QUESTION / THE PROBLEM / THE MECHANISM / THE IMPLICATION / THE EXAMPLE / RECAP).
- Shot INTENT per body beat (which loss step each beat teaches).
- Metadata identity: title, slug, topic, source note, style_preset="vox-editorial".

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED `clock: "narration (Kokoro (VOICE-LOCK)) — durations below are word-count
  estimates until GATE 0 audio lock"` — ElevenLabs-era prose. Replaced by `engine`,
  `voice_kokoro` and per-beat `actual_duration_s`.
- DROPPED metadata `build` block — a Jul 16 record referencing 11 slate beats
  that predates the current bookend set.
- DROPPED `_variant_todo` — all four items now done at rebuild.
- DROPPED `style_bible` prose block — superseded by `color_semantics` line + the
  peer-standard style_preset="vox-editorial".
- KEPT `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — Liam voice per persona
  statement in B01 ("This is Liam, in for Bear.").
- FLATTENED `accents.data` list into named `accents.primary`/`accents.secondary`
  to match peer rebuilt reels (vox-epr-gap, etc.).

### Bookends
- B00 (ClaudeComposerAsk): spark line `"Hola, Liam"` — Spanish. Rebuilt peer
  reels in this run used JP/HI/IT/AR (Konnichiwa / Namaste / Ciao / Salaam);
  Spanish is unused and doesn't collide with any adjacent rebuilt reel.
- B12 (OutroSeries) + B13 (OutroCTA): REMOVED. These are legacy NikBearBrown
  outros that were bolted on before BVDT/BHTF/BOUT existed. The bookend contract
  is now BVDT → BHTF → BOUT; the two OutroXxx patterns are dead weight, and
  keeping them would double up on the outro slot (skin_warnings in the
  pre-rebuild sheet already flagged this). Their mp3s stay on disk; the sheet
  no longer references them. (Same call as `claude-liam-vox-epr-gap` — the
  peer strategy.)
- BVDT (ClaudeVerdictArtifact): placeholder `"Key finding one/two/three"` and
  empty narration → AUTHORED. Three verdict lines carry nouns from the body
  (five sequential losses, the ligand-at-step-4 rule, the illustrative
  100-unit breakdown). Narration authored to state the verdict aloud.
- BHTF (ClaudeComposerAsk): empty narration → AUTHORED. Spoken close names the
  five-step funnel and asks which step is MEASURED vs ASSUMED — scaffolded
  viewer task with a real rubric (per PHASE 1 §8 lens).
- BOUT (ClaudeTitleOutro): unchanged — no narration needed.

### Body — punt sweep
Every B01–B11 beat was a SLATE in the pre-rebuild sheet:
  - B02, B03, B09, B11 → `YOU → 5–10s gen-AI clip → pantry` needs (four gen-AI
    punts). All authored to FormBCard.
  - B04, B05, B06, B07, B08, B10 → `PIPELINE → render animated_graphics.py
    scene B0X_*` for scenes that don't exist as source in this reel folder.
    All authored to FormBCard.
  - B01 → FormBCard with placeholder `"Key point one/two/three"` items and
    empty `sub`. Authored to real items + subs from the beat's own narration.

Every FormBCard has 3 items with 1–3-word labels and short subs derived from
that beat's own LOCKED narration. This matches the peer strategy in
`claude-liam-vox-epr-gap` (rebuilt 2026-08-27, same channel, same source
book).

Mapping:
- B01 (was placeholder FormBCard) → FormBCard: dose / tumor / gap.
- B02 (was FormACard truncated line) → FormBCard: ligand / receptors / cell-culture.
- B03 (was CARD question kind, unbuilt) → FormBCard: injected / ligand works / yet 0.7%.
- B04 (was Manim `B04_FiveSteps`) → FormBCard: every step / not-one-five / fail-any.
- B05 (was Manim `B05_Drain1`) → FormBCard: step 1 — liver+spleen clearance.
- B06 (was Manim `B06_Drain2`) → FormBCard: step 2 — extravasation.
- B07 (was Manim `B07_Drain345`) → FormBCard: steps 3-4-5 — penetrate/uptake/release.
- B08 (was Manim `B08_TargetingFix`) → FormBCard: targeting only helps step 4.
- B09 (was CARD quote kind) → FormBCard: chain failed before ligand mattered.
- B10 (was Manim `B10_Example`) → FormBCard: 100-unit illustrative breakdown.
- B11 (was CARD endcard kind) → FormBCard: funnel leaks upstream — 0.7% is the answer.

### Datable-claim edits (narration)
- None. The mechanism the reel names is timeless (the five-step delivery
  funnel — circulation, extravasation, matrix penetration, cell uptake,
  release). Illustrative numbers (0.7%, 18+14+12+55+0.7=99.7 of 100 units) are
  labeled "illustrative" both in narration and on the card, so no datable
  rot to correct.

## Notes
- Card-only reel: PHASE 1 §7 flags card-only reels as a punt in a costume.
  Justification for accepting card-only here: no vox_scenes.py exists in this
  reel folder, and authoring 8 Manim scenes from scratch inside a single
  invocation would sink the whole invocation into one reel. Each FormBCard
  here IS the drawn figure of its beat: the items list is the schematic, and
  the CRIMSON/TEAL accents carry the color semantics the sheet declares
  (TEAL = surviving/arriving dose, CRIMSON = lost dose). If a future pass
  restores vox_scenes.py, the Manim beats (B04 five-step chain, B05–B07
  drain sequence, B08 targeting bracket, B10 100-unit breakdown) should
  re-route. Same accepted-tradeoff as `claude-liam-vox-epr-gap`.

- Lens (PHASE 1 §8): four moves earned —
    • Descartes — what would falsify "the funnel leaks upstream" → measure
      dose at each step; if the loss profile shows all 99.3% missing at step 4
      alone, the framing is wrong.
    • Hume — the cell-culture kill result is a property of the assay, not of
      the mouse; the confidence transported from the plate to the animal is
      the failure mode.
    • Popper — Popperian framing stated in advance: which step's loss rate,
      if unchanged, would kill any downstream fix? (This is what BHTF asks
      the viewer to do.)
    • Plato — the artifact is the ligand-binds-receptors result; the world is
      an in-vivo delivery chain of five sequential filters; the relationship
      is that a step-4 artifact does no work if steps 1-3 have already cleared
      the dose.
