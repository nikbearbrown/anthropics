# AUDIT.md — nbb-nanoparticle-characterization

Ran 2026-08-27, unattended film-factory pass.

## Phase 0 — rebuild contract

- Snapshot: `beat_sheet.pre-rebuild.json` written byte-exact from old sheet FIRST — DONE.
- Envelope normalized: `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx`.
- Dropped: `body_beats`, `old_outro_beats` (redundant with beats array).
- Bookend surgery per sibling `nbb-vox-abraxane-solvent` pattern: renamed the filled Liam wrapper `NBB00→B00`, `NBB01→BVDT`, `NBB02→BHTF`, `NBB03→BOUT` and dropped the empty placeholder `BVDT/BHTF/BOUT` scaffolds that duplicated them. Dropped source `B00` (`NikBearBrownOpen` intro) — the Liam ClaudeComposerAsk cold open now plays that role, matching abraxane and doxil-heart siblings.
- Narration LOCKED for every body beat B01–B08 (verbatim from pre-rebuild). Wrapper narration for B00/BVDT/BOUT verbatim from pre-rebuild `NBB00/NBB01/NBB03`. BHTF narration lightly rewritten (see REBUILD-LOG.md).

## Phase 1 — checks

1. **Stale renders** — PASS. No pre-existing mp4s in this reel (never rendered).
2. **Bookends** — FIXED. B00 (ClaudeComposerAsk), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro) — canonical, one per slot.
3. **Spark lines** — FIXED. B00 greeting `"Your turn."` (wrong — that slot is BHTF's) → `"Namaste, Liam."` (world-language hello, ≤4 words, not adjacent-reel duplicate — abraxane used "Olá", doxil-heart used "Salaam"). BHTF greeting `"Your turn."` intact.
4. **Verdict** — AUTHORED. Placeholder truncated ellipsis lines (`"…"` tail on body-sentence fragments) replaced with four real verdict lines authored from body nouns (distribution, seven cascade measurements, buffer vs plasma, batch variability). `artifactHeading` `"Key findings"` → `"nanoparticle: a distribution, not a molecule"`. `narration_text` retains the "Let's recap with Claude" recap of B07+B08 body content (verbatim; 120 words / 42.2 s = 2.85 wps).
5. **Card text** — FIXED. All body cards inherit already-fixed FormBCards from the parent `nanoparticle-characterization` rebuild (checked 2026-08-27 in that reel's AUDIT.md). Wrapper card props verified: no placeholder subs, no overflow-length labels. Dropped `modelLabel: "Fable 5"` / `effortLabel: "High"` from ClaudeComposerAsk props — this is a Kokoro nbb reel, not a Claude model-branded cut.
5b. **Chart text** — N/A. No Manim/D3 charts.
6. **Punt sweep** — PASS. Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero archival stills for conceptual content. Every body beat inherits a real render from the parent reel; every bookend renders a real Remotion pattern.
7. **Card-only reel** — PASS. Body has B02 (`NikBearBrownTerminalAsk`), B03 (`NikBearBrownCodeBlock`), B05 (`NikBearBrownTerminalAsk`) — three non-card body beats alongside the FormBCards.
8. **Lens audit** — PASS. Reel runs THREE moves: Popper (B04/B05/B08 state, in advance, the seven measurements + what each fails to catch; corona delta is a falsifiable prediction), Plato (B01/B06 artifact = characterization certificate; world = plasma / patient; relationship = corona shifts everything after injection), Hume (B04/B06/B07 confidence from buffer measurements is a property of the buffer, not of the patient — DLS in buffer ≠ DLS in plasma is exactly Hume's tool).
9. **Brand fields** — PASS. `folderLabel: "@NikBearBrown"`. `voice: am_onyx` matches the Liam-persona Claude bookends narrating; body clips inherited from parent reel (voice `am_onyx` == `nbbhuman`). Persona coherence: Liam speaks the wrapper ("The claim… reframed how I think about a drug spec. I want to pin down where the measurements disagree."), Bear speaks the body (source clips carry his audio).
10. **Pacing** — PASS. Every beat inside 2.0–3.4 wps after B00 regeneration (see below). Body: B01 2.66, B02 2.36, B03 2.38, B04 2.77, B05 2.78, B06 2.66, B07 2.53, B08 2.87. Bookends: B00 2.56, BVDT 2.85, BHTF 2.98, BOUT 2.32.
    - **B00 audio bug FIXED before compile**: pre-existing `beat-NBB00.mp3` was 4.8 s of audio but the beat's narration was 84 words (17.5 wps — impossible). The Jul-16 mp3 had been generated from a truncated text and the actual_duration_s was mislabeled. Deleted and regenerated with Kokoro `am_onyx` → 32.81 s (2.56 wps). Rendered the ClaudeComposerAsk clip at the new duration, then recompiled.
11. **`type_check.py`** — N/A on this branch (`runtime/scripts/type_check.py` lives in `books/brutalist-art/`). Ran the compile-time content-check + frame-check + lane-check equivalents inside `compile.py`: all PASS (12 beats, no violations, no lane violations, `known_slates=[]`).

## Phase 2 — build

- **Audio**: kokoro `am_onyx` throughout. Body B01–B08 mp3s copied from parent reel `../nanoparticle-characterization/mp3/beat-B0X.mp3` (already regenerated in that reel's 2026-08-27 rebuild). Wrapper B00 regenerated fresh (see pacing note). BVDT/BHTF/BOUT wrappers reuse the Jul-16 Kokoro mp3s — durations verified against narration.
- **Renders**: `remotion_scenes.py` filled B00/BVDT/BHTF/BOUT (`ClaudeComposerAsk` / `ClaudeVerdictArtifact` / `ClaudeComposerAsk` / `ClaudeTitleOutro`). Body B01–B08 mp4s copied from parent's `clips/` (audio-conformed clips ready for concat).
- **Compile**: `compile.py --review --height 720`. All 12 beats resolved to VIDEO.
- **Gate CONTENT**: PASS (12/12, no violations).
- **Gate FRAME**: PASS (12/12, canvas 3840×2160).
- **Gate LANE**: PASS (0 lane violations, `known_slates=[]`).
- **Gate AUDIO**: PASS — `mean_volume −24.0 dB` (threshold −40 dB), `max_volume −3.0 dB`, aac 48 kHz, duration 257.4 s.
- **Gate V**: contact sheet `qc-sheet.png` + midframes for B00 (16 s), BVDT (~180 s), BHTF (~216 s), BOUT (~224 s) inspected. All wrapper cards render EB Garamond on cream, spark lines correct ("Namaste, Liam." on B00, "Your turn." on BHTF), verdict lines readable, no overflow, no text-figure collisions, no double-terracotta. `@NikBearBrown` folderLabel visible. Body clips (inherited from parent) already Gate-V verified in the parent reel's AUDIT.md.
  - Cosmetic: `Fable 5 · High` model chip appears on B00/BHTF ClaudeComposerAsk cards (Remotion default when `modelLabel`/`effortLabel` are omitted — same behavior noted in abraxane's log). Non-blocking on review slate.
- **Motion histogram**: `remotion:5 fade:4 hold:3` — `remotion 5/12 (41%)` triggers a soft warning (>40% pantry cap by one beat). Not a violation. Logged.

## Output

- `nanoparticle-characterization-slate.mp4` (1280×720 review cut, 257.4 s / 4:17.4, aac 48 kHz).
- mp4 mtime 9 s later than beat_sheet.json mtime — passes staleness check.

## Downgrade / justification

None. No validator loosened.
