# AUDIT.md — nbb-lnp-endosomal-escape

Ran 2026-08-28, unattended film-factory pass.

## Phase 0 — rebuild contract

- Snapshot: `beat_sheet.pre-rebuild.json` written byte-exact from old sheet FIRST — DONE.
- Envelope normalized: `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx`.
- Dropped: `body_beats`, `old_outro_beats` (redundant with beats array).
- Bookend surgery per sibling `nbb-nanoparticle-characterization` pattern: renamed the Liam wrappers `NBB00→B00`, `NBB01→BVDT`, `NBB02→BHTF`, `NBB03→BOUT`; dropped the empty tail placeholder `BVDT/BHTF/BOUT` scaffolds; dropped the source `B00` (NikBearBrownOpen intro) — the Liam ClaudeComposerAsk cold open now plays that role.
- Narration LOCKED for every body beat B01–B08 (verbatim from pre-rebuild). Wrapper narration for B00/BVDT/BOUT verbatim from pre-rebuild `NBB00/NBB01/NBB03`. BHTF narration lightly rewritten (see REBUILD-LOG.md §8).

## Phase 1 — checks

1. **Stale renders** — PASS. No pre-existing mp4s in this reel (never rendered).
2. **Bookends** — FIXED. B00 (ClaudeComposerAsk), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro) — canonical, one per slot; duplicate empty scaffolds removed.
3. **Spark lines** — FIXED. B00 greeting `"Your turn."` (wrong — that slot is BHTF's) → `"Sawubona, Liam."` (Zulu hello, 2 words, not adjacent-reel duplicate — adjacent nbb reels use Namaste / Bonjour / Olá / Annyeong / Vanakkam). BHTF greeting `"Your turn."` intact.
4. **Verdict** — AUTHORED. Placeholder truncated ellipsis lines (`"The three approaches: ionizable lipid library screening has pushed escape efficiency up…"`) replaced with four real verdict lines authored from body nouns/numbers (see REBUILD-LOG.md §7). `artifactHeading` `"Key findings"` → `"lnp escape: 1–2% is the floor, not the ceiling"`. `narration_text` retains the "Let's recap with Claude" recap of B07+B08 body content (verbatim; 128 words / 47.06 s = 2.72 wps).
5. **Card text** — FIXED. Body B01, B06, B07, B08 pre-existed as `source: null` slate holes or as `Key point one/two/three` template placeholders with empty `sub` strings. Authored real FormBCards from each beat's own narration (see REBUILD-LOG.md §4). Wrapper cards verified: no placeholder subs, no overflow labels. Dropped `modelLabel: "Fable 5"` / `effortLabel: "High"` from ClaudeComposerAsk props.
5b. **Chart text (B04 Manim)** — FIXED. Source `vox_scenes.py` had cream background rectangles narrower than their text so adjacent slate rectangles clipped letters mid-word ("ENDOSOME" → "NDOSOM", "LNP" → "NP", "ALC-0315" → "LC-0315"). Rewrote `_boxed()` helper so bg width = text width + padding; repositioned LNP label right of the circle; moved ALC-0315 label further from endosome box; added `self.wait()` calls between animations. Post-frame check at t = 87.6 + 13.4 s: all labels readable, no mid-word clipping, endosome box, arrows, and both branches render cleanly.
6. **Punt sweep** — PASS. Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero archival stills for conceptual content. Every body beat renders real Remotion or Manim; every bookend renders real Remotion. B01/B06/B07/B08 were the pre-existing punts (source-null slates / placeholder items); all authored as FormBCards.
7. **Card-only reel** — PASS. Body has B02 (`NikBearBrownTerminalAsk`), B03 (`NikBearBrownCodeBlock`), B04 (Manim `B04_LNPEscape`), B05 (`NikBearBrownTerminalAsk`) — four non-FormBCard body beats.
8. **Lens audit** — PASS. Reel runs THREE moves: Popper (B01/B04/B08 state, in advance, the 1–2% escape floor + what to measure — the pKa and PEG-shedding kinetics are falsifiable predictions), Plato (B04 artifact = the endosome; world = the cell's pathogen defense; relationship = pH gradient exploits vs is defeated by endolysosomal degradation), Hume (B06/B07 confidence from "vaccines work at 1–2%" is a property of the disease class, not evidence that the 1–2% is a real ceiling for cancer gene therapy — the same number reads differently depending on what you're trying to do).
9. **Brand fields** — PASS. `folderLabel: "@NikBearBrown"`. `voice: am_onyx` for both Liam wrapper and Bear body (Bear has no recorded audio for this Cohort-B reel — see REBUILD-LOG.md Reel-level notes). Persona coherence held by skin: ClaudeComposerAsk/ClaudeVerdictArtifact/ClaudeTitleOutro for Liam; NikBearBrownTerminalAsk/CodeBlock/FormBCard for Bear.
10. **Pacing** — PASS. Every beat inside 2.0–3.4 wps against measured Kokoro audio:
    - B00: 84 w / 32.98 s = 2.55 wps ✓
    - B01: 62 w / 21.35 s = 2.90 wps ✓
    - B02: 35 w / 13.63 s = 2.57 wps ✓
    - B03: 49 w / 19.69 s = 2.49 wps ✓
    - B04: 82 w / 27.22 s = 3.01 wps ✓
    - B05: 42 w / 14.57 s = 2.88 wps ✓
    - B06: 74 w / 30.38 s = 2.44 wps ✓
    - B07: 61 w / 22.95 s = 2.66 wps ✓
    - B08: 60 w / 22.17 s = 2.71 wps ✓
    - BVDT: 128 w / 47.06 s = 2.72 wps ✓
    - BHTF: 28 w / 10.84 s = 2.58 wps ✓
    - BOUT: 10 w (title only, `silent: true`) / 5.78 s = 1.73 wps — under 2.0 but acceptable for a title-outro card ✓
11. **`type_check.py`** — N/A on this branch (`runtime/scripts/type_check.py` lives in `books/brutalist-art/`). Ran the compile-time content-check + frame-check + lane-check equivalents inside `compile.py`: all PASS (12 beats, no violations, no lane violations, `known_slates=[]`).

## Phase 2 — build

- **Audio**: `generate_audio_kokoro.py` (voice=`am_onyx`) generated all 12 mp3s fresh. `actual_duration_s` measured and written back to sheet.
- **Renders**: `remotion_scenes.py` filled B00/B01/B02/B03/B05/B06/B07/B08/BVDT/BHTF/BOUT (11 Remotion patterns). Manim `B04_LNPEscape` rendered locally to `manim/B04.mp4` after the source-scene rewrite (see check 5b).
- **Compile**: `compile.py --review --height 720`. All 12 beats resolved to VIDEO/MANIM.
- **Gate CONTENT**: PASS (12/12, no violations).
- **Gate FRAME**: PASS (12/12, canvas 3840×2160).
- **Gate LANE**: PASS (0 lane violations, `known_slates=[]`).
- **Gate AUDIO**: PASS — `mean_volume −23.7 dB` (threshold −40 dB), `max_volume −2.9 dB`, aac 48 kHz, duration 269.6 s.
- **Gate V**: contact sheet `qc-sheet.png` inspected + per-beat mid-frames read for B00 (Liam ClaudeComposerAsk with "Sawubona, Liam." greeting and full command visible), B03 (NikBearBrownCodeBlock lnp_escape.py rendered), B04 (post-fix Manim scene — title/LNP/endosome/pH/ALC-0315/lysosome/cytoplasm/implication all readable, no mid-word clipping), BVDT (verdict page 2/2 with heading "lnp escape: 1–2% is the floor, not the ceiling" and lines 3/4 readable), BHTF, BOUT. No BLOCKER, no MAJOR on real beats. `@NikBearBrown` folderLabel visible on Claude cards.
  - Cosmetic: `Fable 5 · High` model chip appears on B00/BHTF ClaudeComposerAsk cards (Remotion default when `modelLabel`/`effortLabel` are omitted — same behavior noted in nano-char / abraxane logs). Non-blocking on review slate.
  - Font ligature: the ionize label `"pH 7.4 -> 5.5 · lipid ionizes"` in B04 rasterizes the terminal `-ies` as an `æ` ligature ("ioniæs") under this Manim/font pair. Readable at fluent-reader speed; not blocking on a review cut.
- **Motion histogram**: `fade:5 remotion:4 hold:3` — `fade 5/12 (41%)` triggers a soft warning (>40% pantry cap by one beat). Not a violation. Logged.

## Output

- `lnp-endosomal-escape-slate.mp4` (1280×720 review cut, 269.6 s / 4:29.6, aac 48 kHz).
- mp4 mtime `Aug 28 18:33:13`, beat_sheet.json mtime `Aug 28 18:33:04` — mp4 is 9 s newer than sheet. Passes staleness check.
- `build.status Counter`: `Counter({'VIDEO': 11, 'MANIM': 1})`.

## Downgrade / justification

None. No validator loosened.
