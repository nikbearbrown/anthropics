# AUDIT.md — lnp-endosomal-escape

**Reel:** `anthropics/youtube/cancer-nanomedicine/youtube/lnp-endosomal-escape`
**Channel:** @NikBearBrown · **Register:** Teardown · **Style:** CLI
**Audited:** 2026-08-30 · **Overall:** FIXED — building slate cut

## Phase 0 — REBUILD contract

- **PASS** — `beat_sheet.pre-rebuild.json` created (byte-exact copy of prior sheet, taken FIRST).
- **PASS** — narration is LOCKED across body beats (B00–B09); no paraphrase.
  Datable-claim pass turned up nothing — no model versions or "as of" strings to correct.
- **FIXED** — VOICE-LOCK envelope: dropped dead `voice_id` (ElevenLabs banned);
  set `voice=am_onyx`, `engine=kokoro`, `voice_kokoro=am_onyx` in metadata.
- **PASS** — shot.form derives from locked pattern per beat (no TEMPLATE-MISSES beyond
  the B04 Manim scene that lives in `vox_scenes.py` and remains available for a later
  full-render pass — the review slate uses the FormBCard fallback the sibling used).
- **PASS** — non-Claude channel skins preserved: NBBOpen (B00) and NBBOutro (B09) kept;
  Claude bookends (BVDT verdict + BHTF your-turn) inserted BEFORE B09 without displacing
  the channel identity.

## Phase 1 — Audit checklist

1. **Stale renders — PASS.** No `.mp4` files under the reel folder; nothing to purge.
2. **Bookends — FIXED.** Kept `B00 NikBearBrownOpen` and `B09 NikBearBrownOutro`
   (channel-native, per rebuild rule). Kept `BVDT ClaudeVerdictArtifact` and
   `BHTF ClaudeComposerAsk` as the closing block (sibling pattern). **DELETED** the
   duplicate `BOUT ClaudeTitleOutro` — B09 is already the outro; two outros is a
   defect AND a Claude-wash of a non-Claude channel.
3. **Spark lines — FIXED / PASS.** B02 and B05 `NikBearBrownTerminalAsk` beats carry
   `greeting: "The ask,"` (2 words). BHTF carries `Your turn.` No inner
   `ClaudeComposerAsk` in the body (this is a CLI reel, uses NBBTerminalAsk instead).
   `NikBearBrownOpen` renders the title lines from `props.lines`, not a spark.
4. **Verdict — AUTHORED.** Body qualifies (10 beats, well over the 5-beat / 180-word
   threshold). Placeholder `Key finding one/two/three` replaced with four artifact lines
   compressed from the body's own nouns and numbers; narration authored to state the
   finding aloud.
5. **BHTF your-turn — AUTHORED.** Placeholder template
   `"Take what you learned from [Research LNP Endosomal Escape…]…"` REMOVED. Real
   video-specific exercise authored: pick an LNP formulation, pull the ionizable lipid,
   check pKa against 6.2–6.5, check PEG-shedding kinetics — with a rubric stub in
   `output` the viewer can paste back.
5b. **Chart text — N/A.** No Manim/D3 chart renders in this slate cut (B04 falls back to
    FormB); no axis-label truncation possible.
6. **Card text — FIXED.** B01 FormBCard placeholders (`Key point one/two/three`, empty
   subs) replaced with real title + three items authored from the narration
   (1–2% escape, 98–99% degraded, cellular-defense bottleneck). B06/B07/B08 were
   `shot.source: null` bare holds — authored full FormBCards for each from the locked
   narration (three approaches, three summary lines, three viewer probes).
7. **Punt sweep — FIXED.** Zero gen-AI asks, zero unfilled slates, zero DoodleScene,
   zero STILL archive stubs. B04's Manim fallback maps to nopunt catalog row
   "static flow / labeled stack" → FormB, which the reel now renders.
8. **Card-only reel — PASS.** B02, B03, B05 draw NBB terminal / code-block skins (real
   artifacts). Not card-only.
9. **Lens audit — PASS.** Runs at least two of the four moves:
   - **Popper (falsifiability):** the reel states an in-advance criterion for success
     — the 1–2% cytoplasm-escape fraction is the measurable failure mode of every LNP
     formulation, and B08 hands the viewer a pKa window (6.2–6.5) and a PEG-shedding
     check they can go looking for.
   - **Plato (artifact vs world):** B03 explicitly frames "read the code before
     trusting it" — the script is the artifact, the endosome is the world, and the
     narration insists on interrogating the relationship before accepting the
     mechanism. B04's `# lnp_escape.py — Claude Code output` header is on-screen so the
     viewer can distinguish LLM-generated code from a measured value.
10. **Brand fields — PASS.** `folderLabel: "@NikBearBrown"` on BHTF (channel handle,
    not brand key). `engine=kokoro` / `voice=am_onyx` matches what will be generated
    (Liam-voice); narration does not falsely claim Bear.
11. **Pacing — PASS (advisory).** Word counts × est duration:
    - B00 12 words / 5s → 2.4 wps ✓
    - B01 65 words / 20s → 3.25 wps ✓
    - B02 42 words / 15s → 2.8 wps ✓
    - B03 62 words / 15s → 4.1 wps ← FLAG (fast side of range; recompile will conform
      to measured audio and expand the beat window automatically).
    - B04 89 words / 27s → 3.3 wps ✓
    - B05 46 words / 15s → 3.1 wps ✓
    - B06 74 words / 22s → 3.4 wps ✓ (edge)
    - B07 66 words / 20s → 3.3 wps ✓
    - B08 63 words / 20s → 3.15 wps ✓
    - BVDT 55 words / 20s → 2.75 wps ✓
    - BHTF 40 words / 18s → 2.2 wps ✓
    - B09 20 words / 7s → 2.86 wps ✓
    Only B03 is outside 2.0–3.4 wps. Audio-first will re-clock everything.
12. **type_check.py — PASS.** GATE T PASS · 0 FAILs across 12 beats. One §8.10 advisory
    on B00 (narration recites the two-word title lines — expected for a brand-open beat);
    one §8.6 advisory on B09 headline length (canonical title is long). Neither blocks.

## Deliverable

Building slate-with-audio cut: `<slug>-slate.mp4` (or `<slug>.mp4` if every beat renders
real).
