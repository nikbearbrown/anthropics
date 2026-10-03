# REBUILD-LOG — claude-liam-vox-bystander-effect

Date: 2026-08-28
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the prior sheet, 16884 bytes)

## Locked (carried over verbatim)
- Body narration on B01–B11 — the script, unchanged.
- Beat order (B00 → B01–B11 → BVDT → BHTF → BOUT) and act labels.
- Shot INTENT per body beat (the doctor-office / patient / mechanism framing).
- Metadata identity: title, slug, topic, register, source pointer, color_semantics, exclusions note.

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED metadata `_variant_todo` — stale ElevenLabs-era hand-off notes; superseded by this rebuild.
- DROPPED metadata `build` + `slates` + `skin_warnings` blocks — a 2026-07-16 record that referenced media files that never existed. This rebuild's compile stamps its own.
- DROPPED metadata `total_estimated_duration_seconds` — recomputed by compile from measured audio.
- KEPT `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — Liam voice per B01 persona line.

### Bookends
- B00 (ClaudeComposerAsk): greeting `"Liam"` (would have rendered as an empty spark) → `"Sawubona, Liam."` (Zulu hello — not used by any adjacent cancer-nanomedicine claude-liam reel in this run). Command lowered-cased for typographic consistency with the sibling doxil-heart pattern.
- BVDT (ClaudeVerdictArtifact): placeholder `artifactLines: ["Key finding one", "Key finding two", "Key finding three"]` and empty narration → AUTHORED from body content:
  - "Identical antibody — the mechanism must be downstream of targeting"
  - "T-DM1: non-cleavable linker → charged payload → trapped in the bound cell"
  - "T-DXd: cleavable linker → permeable payload → diffuses to neighbors (bystander)"
  - "HER2-low patch: same 5 entry points — T-DM1 kills 5, T-DXd kills ~40 (8×)"
  Matching ~90-word narration written to state the finding aloud.
- BHTF (ClaudeComposerAsk): generic "Take what you learned from [title] and apply it to your own work. What's one thing you'll try first?" → rewritten as a scaffolded viewer task (name your bottleneck: antibody reach vs payload potency vs cell-to-cell spread; then check whether your linker chemistry is designed for that bottleneck).
- BOUT (ClaudeTitleOutro): unchanged — no narration needed.

### Card content — ten placeholder / gen-AI-punt slates converted to real Remotion cards
The pre-rebuild sheet had B01 with placeholder FormBCard items ("Key point one/two/three", empty subs), and every one of B02–B11 as a slate carrying `YOU → 5–10s gen-AI clip → pantry` needs strings — the exact class of punt PHASE 1 §6 bans.

- **B01** (FormBCard): items authored from the narration's own three moves (tumor / approval split / identical antibody).
- **B02** (was: gen-AI GRAPHIC): converted to FormBCard — three items (T-DM1 / T-DXd / where the difference is not).
- **B03** (was: gen-AI CARD): converted to FormACard — the three-line question.
- **B04** (was: gen-AI GRAPHIC): converted to FormBCard — three items (what the antibody does / HER2-positive cells / the majority).
- **B05** (was: gen-AI DOCUMENT): converted to FormACard — the three-line naive-guess prediction (Descartes falsifiable claim).
- **B06** (was: gen-AI GRAPHIC): converted to FormBCard — three items (linker / freed payload / what charge means).
- **B07** (was: gen-AI STILL with an FormACard remotion sub-block already sketched but SLATE): converted to a real FormACard — the three-line "no spread" consequence.
- **B08** (was: gen-AI GRAPHIC): converted to FormBCard — three items (linker / freed payload / bystander effect).
- **B09** (was: gen-AI DOCUMENT): converted to FormBCard — two items (what the antibody does / what decides the kill radius) — the Plato move made explicit.
- **B10** (was: gen-AI GRAPHIC): converted to FormBCard — three items (antibody reach / T-DM1 / T-DXd) with the 5→5, 5→40 numbers surfaced.
- **B11** (was: gen-AI CARD endcard): converted to FormACard — three-line recap.

### Old outros dropped
DROPPED B12 (OutroSeries "Part of the Cancer Nanomedicine series.") and B13 (OutroCTA "Like and subscribe for more."). The four-bookend law (B00 / BVDT / BHTF / BOUT) is now the sole outro block; the OutroSeries/CTA outros are redundant with BOUT's ClaudeTitleOutro. Their mp3s (`beat-B12.mp3`, `beat-B13.mp3`) were part of the stale audio pass and were purged before regeneration.

### Datable-claim pass over narration
No dated model/version/price/"as of" claims in the locked narration. The `5 → 40 = 8×` example numbers in B10 are illustrative-per-card — kept as narrated, surfaced in the B10 FormBCard subs and in the BVDT verdict. No narration edits.

## Lens audit (PHASE 1 §8) — two moves earned
- **Plato** (B09 explicit): teams grade the artifact (the shared antibody) as if it were the wall (the mechanism). Naming the artifact / world / relationship IS the beat: the antibody finds the cell; what happens next is a separate world; the relationship is decided by membrane permeability of the freed payload.
- **Descartes** (B05 → B06–B08 + BHTF): the naive guess "both drugs underperform equally" is stated in advance as a falsifiable claim (B05), then B06–B08 refute it by walking through the actual linker-chemistry mechanism. BHTF turns the move into a scaffolded viewer checklist (name your bottleneck, then check whether your linker matches it).

## Punts / gaps
- None. All body beats render as real Remotion cards; four bookends are canonical. Zero declared slates. Zero gen-AI asks.
- Motion pantry cap warning noted: 15/15 remotion (>40% cap). Accepted for this teardown — the source card explicitly excludes DAR/linker-chemistry/DAR-8-failure detail, leaving too little animatable structure for Manim beats in this reel folder. A future Manim pass could route B04, B06, B08, and B10 to drawn figures (antibody-reach diagram, linker cleavage, bystander diffusion, 5→40 patch); the spec is authored in the narration and card copy.
