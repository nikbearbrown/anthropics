# AUDIT — vox-protein-corona (2026-08-30 filmloop pass)

Legacy vox-editorial reel (Cohort C) on @NikBearBrown. Not a Claude cut — the
claude-bookend / spark-line / verdict checks that name Claude components are N/A;
they are marked as such. The vox equivalents are audited in their place.

## PHASE 0 — REBUILD CONTRACT

- `beat_sheet.pre-rebuild.json` written (byte-exact snapshot of the pre-edit sheet).
- Envelope: dropped ElevenLabs-era `voice_id` and `clock` prose; added
  `channel`, `folderLabel=@NikBearBrown`, `engine=kokoro`, `voice=am_onyx`.
- All narration LOCKED — no rewrites; see REBUILD-LOG.md for details.

## PHASE 1 — CHECKS

1. **Stale renders** — PASS. No mp4s exist in the reel folder; nothing to delete.

2. **Bookends** — N/A. Vox-editorial reel keeps its own skin; the B00/BVDT/BHTF/BOUT
   Claude bookends are not applicable (Phase 0 contract: "Non-claude channels keep
   their own skins — never Claude-wash an open or outro"). Outros B12 (OutroSeries)
   and B13 (OutroCTA) are present.

3. **Spark lines** — N/A. No `ClaudeComposerAsk` beats in this reel.

4. **Verdict** — PASS. B11 endcard carries a real, reel-specific verdict:
   card "The protein corona buries the targeting ligand. The body sees the corona,
   not the particle you designed." Narration matches: "The corona forms. The ligand
   is buried. The body never sees the surface you built." Not a template; would not
   be true of another video. Body has 8 substantive beats (B03–B10, 280+ narration
   words) — verdict is authored, not stripped.

5. **Your-Turn placeholder** — N/A. No BHTF beat in this reel.

5b. **Chart text (B09)** — PASS. Bar sub-labels are short category nouns
    ("binding", "liver", "tumor"); title "Folate-targeted nanoparticle --
    illustrative numbers"; bar heights match the narration's meaning; illustrative
    marker present bottom-left.

5. **Card text** — PASS. B01, B02, B08, B11 all carry real copy and sub-lines
   authored from the beat's own narration.

6. **Punt sweep** — FIXED. B03 was `STILL/AI` with a `FormACard` prop whose only
   line was a truncated slice of narration ending in an ellipsis — a punt costume
   under Amendment 6 ("FormA card whose narration names a visual it never draws").
   Re-routed to `GRAPHIC/own` with a new `B03_ProteinsSwarm` Manim scene that
   actually shows the four named proteins (albumin, IgG, fibrinogen, apolipoprotein)
   arriving in narration order and settling on the particle.

7. **Card-only reel** — PASS. 7 drawn GRAPHIC beats (B03–B07, B09–B10) + 4 CARDs
   + 2 outros.

8. **Lens audit (LENS-NOTES.md)** — PASS.
   - Plato (artifact/world) — B04: "The corona is not the surface you designed.
     It is the surface the body now sees." Names the artifact (designed surface)
     and the world (body's view) and inverts the relationship.
   - Popper (state failure in advance) — B08: "Any targeting strategy validated
     only in protein-free culture is incomplete... You need to test in full
     plasma — at minimum — before drawing any conclusions." Explicitly names
     the falsifying condition.
   - Descartes (what would falsify) — B07: two-panel contrast (culture vs blood)
     that makes visible what would have to be true for the culture claim to hold
     in blood, and shows it does not.

9. **Brand fields** — FIXED. Metadata now carries `channel=@NikBearBrown`,
   `folderLabel=@NikBearBrown`, `engine=kokoro`, `voice=am_onyx`. Kokoro `am_onyx`
   matches the Jul-8 mp3s (Bear/Liam house voice on this channel). No persona
   incoherence.

10. **Pacing** — FLAG. B01 word-rate = 32 words / 9.2 s ≈ 3.48 wps, marginally
    over the 3.4 ceiling; every other beat sits inside 2.0–3.4 wps. Not retimed
    (narration is LOCKED); logged per house rule and left as-is.

11. **type_check.py** — PASS. GATE T: PASS (see TYPECHECK.md).

## AUTHORED CHANGES

- Fixed one punt (B03) by adding `B03_ProteinsSwarm` to `vox_scenes.py`.
- Dropped 2 dead envelope fields (`voice_id`, `clock` prose).
- Added 4 metadata fields (`channel`, `folderLabel`, `engine`, `voice`).

## BLOCKED

None. Proceeding to PHASE 2 build.
