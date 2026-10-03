# REBUILD-LOG — claude-liam-vox-doxil-heart

Date: 2026-08-27
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the prior sheet)

## Locked (carried over verbatim)
- Body narration on B01–B12 — the script.
- Beat order and act labels.
- Shot INTENT per body beat (Manim scene names, production_viz mechanics).
- Metadata identity: title, slug, topic, register, source pointer, style bible.

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED metadata `clock: "narration (Kokoro (VOICE-LOCK)) — durations…"` — dead prose.
- DROPPED metadata `_variant_todo` — stale hand-off notes; superseded by the rebuild.
- DROPPED metadata `build` block + `skin_warnings` — a 2026-07-16 record that referenced
  `media/*.mp4` files that never existed; this rebuild produces its own build stamp.
- DROPPED `total_estimated_duration_seconds` — recomputed by the compiler from measured audio.
- KEPT `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — Liam voice per B01 persona line.

### Bookends
- B00 (ClaudeComposerAsk): greeting was bare `"Liam"` → `"Salaam, Liam."` (world-language hello).
- BVDT (ClaudeVerdictArtifact): placeholder `artifactLines: ["Key finding one/two/three"]`
  and empty narration → AUTHORED from body content (cardiac ceiling, PEG mechanism, clinical
  result, misuse warning).
- BHTF (ClaudeComposerAsk): generic "Take what you learned…" command → rewritten as a
  scaffolded viewer task (name the bottleneck, then check whether the copied approach
  targets it).
- BOUT (ClaudeTitleOutro): unchanged — no narration needed.

### Card content — placeholder / gen-AI-punt slates converted to real Remotion cards
The pre-rebuild sheet had B01 with placeholder FormBCard items ("Key point one/two/three",
empty subs) and B02, B03, B06, B08, B12 as slates carrying `YOU → 5–10s gen-AI clip → pantry`
needs strings — the exact class of punt PHASE 1 §6 bans.

- **B01** (FormBCard): items authored from the narration's own three moves (reputation,
  assumption, reveal).
- **B02** (was: gen-AI STILL "oncologist reviews chart"): converted to FormBCard —
  three items keyed to the narration (disease, watched dose, hidden cost).
- **B03** (was: gen-AI CARD): converted to FormACard — three lines of THE QUESTION.
- **B06** (was: gen-AI STILL "liposome cross-section"): converted to FormBCard —
  the three layers of a PEGylated liposome (aqueous core / lipid bilayer / PEG coat).
- **B08** (was: gen-AI DOCUMENT quote): converted to FormACard with the three-line
  clinical finding.
- **B12** (was: gen-AI CARD endcard): converted to FormACard with three-line recap.

### Declared-slate beats (kept — reviewed as slates)
B04, B05, B07, B09, B10, B11 remain `GRAPHIC` with `manim: B*` scene names and
`production_viz` mechanics that describe what the built figure will show. The vox
`animated_graphics.py` scene file does not exist in this reel folder, so the beats
render as declared slates in this review cut. Each still names the target scene and
mechanic so the eventual Manim pass has a spec.

### Datable-claim pass over narration
No dated model/version/price/"as of" claims. `360 milligrams per square meter lifetime`
and the `40 percent lower cardiac exposure` figures are illustrative — labeled as such
in B11's production_viz. No narration edits.

### Old outro beats
DROPPED B13 (OutroSeries "Part of the Cancer Nanomedicine series.") and B14 (OutroCTA
"Like and subscribe for more."). The four-bookend law (B00 / BVDT / BHTF / BOUT) is
now the sole outro block; the old CTA outros are redundant with BOUT's ClaudeTitleOutro.

## Lens audit (PHASE 1 §8)
Two moves earned:
- **Plato** (B09, made explicit): teams grade the artifact (the EPR approval narrative)
  as if it were the wall (the actual mechanism, which was cardiac protection). Naming
  the artifact / world / relationship is the beat's job.
- **Descartes** (B10 + BHTF): what would falsify "copying Doxil for our drug will work"?
  If our drug has no cardiac problem, Doxil's mechanism has nothing to buy. BHTF makes
  this a checklist: name your bottleneck, then check whether the borrowed approach
  targets it.

## Punts / gaps
- Six declared Manim slates (B04, B05, B07, B09, B10, B11) — the mechanic is authored;
  the scene file for `animated_graphics.py` is not in this reel folder.
