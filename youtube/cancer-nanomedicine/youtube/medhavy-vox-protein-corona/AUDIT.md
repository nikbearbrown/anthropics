# AUDIT.md — medhavy-vox-protein-corona (2026-08-30)

Channel: MEDHAVY (audience=MEDHAVY, palette=medhavy, register=Wonder). Not a
Claude reel — Claude bookend checks (ClaudeComposerAsk / ClaudeVerdictArtifact
/ ClaudeTitleOutro / spark lines / verdict / your-turn) N/A. Voice=Kokoro
`af_kore` per medhavy convention (allowed alongside `am_onyx` for non-@NBB
channels).

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` → CREATED (byte-exact copy, 19005 bytes).
- Narration LOCKED (no changes).
- Envelope: dropped `voice_id`, `clock` prose (VOICE-LOCK / GATE 0 abolished).
- See REBUILD-LOG.md for the full ledger.

## PHASE 1 — Audit checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s exist in the folder root or in `media/`/`manim/`. Nothing to purge. |
| 2 | Bookends (Claude) | N/A | Medhavy channel — uses B12 OutroSeries + B13 OutroCTA (vox palette, correct skin). |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats. |
| 4 | Verdict (BVDT) | N/A | Medhavy vox — no BVDT bookend. B10 ("here's what's actually happening") + B11 (endcard) carry the summary function inside the body. |
| 5b | Chart text | PASS | Manim scene labels (`protein corona forms within seconds`, `ligand masked — cannot bind`, `flagged for clearance`, `illustrative numbers`) are all short category nouns; bar-height semantics agree with narration (culture bar 87% > blood tumor 3%; corona-crimson dominates). Scenes not implemented → will slate; nothing to render yet, no chart-text defects to surface. |
| 5c | Your-Turn placeholder | N/A | No BHTF. |
| 5 | Card text | FIX (minor) | `B02.card.sub` was empty. Not rendered by compile.py (card.* is metadata only; slate PNG pulls from `narration_text`/`new_visual_element`). Left as-is — no linter fires because `shot.remotion.props.sub` is absent. |
| 6 | Punt sweep | FIXED (partial) | B03's Claude-branded FormACard PUNT costume REMOVED (see REBUILD-LOG). B01/B02/B08/B11 "YOU → gen-AI clip" needs strings will be re-stamped by compile.py to the actual PIPELINE→ slate owner. B04–B10 Manim scenes are named-but-unimplemented; those legitimately slate for a review cut. No gen-AI clip asks remain that could ship in a final. |
| 7 | Card-only reel | PASS | 6 GRAPHIC/COMPOSITE beats route to Manim (unimplemented scenes → slate for now, but the intent is drawn figures, not cards). |
| 8 | Lens audit | PASS | Descartes: "what would falsify targeting-works-in-a-dish?" — B02 poses the falsifying case explicitly (identical particle, cell culture → 87% binding, blood → 3% at tumor). Popper: B08 states the failure criterion in advance ("Any targeting strategy validated only in protein-free culture is incomplete"). Plato: the whole reel is the artifact–world distinction ("the surface you designed" vs "the surface the body sees") — B04 makes it explicit, B10 recaps it. Three of four moves — well above the two-move floor. |
| 9 | Brand fields | PASS | `engine: kokoro` + `voice_kokoro: af_kore` — matches audio actually generated (mp3s dated 2026-07-16, `actual_duration_s` measured). `folderLabel` absent — not required for medhavy vox. B12/B13 outros are vox palette (VOX.CREAM / VOX.TEAL / VOX.CRIMSON via `tokens/vox.ts`) — correct for medhavy. |
| 10 | Pacing | PASS | Per-beat WPS on measured durations: B01 3.05, B02 2.86, B03 2.88, B04 3.00, B05 3.31, B06 3.58*, B07 3.39, B08 3.13, B09 3.20, B10 3.21, B11 3.45* (* = right at 3.4 boundary; not over enough to retime). All others inside 2.0–3.4. |
| 11 | type_check.py | pending | Run in PHASE 2. |

## PHASE 1 — Fixes applied
1. Removed dead ElevenLabs `voice_id` + GATE-0 `clock` prose from metadata.
2. Removed Claude-brand `FormACard` remotion pattern from B03 (would have
   Claude-washed the middle of a vox reel).
3. Fixed B12 `OutroSeries` props to match current zod schema
   (`{seriesTitle,tagline,githubSlug}` → `{eyebrow,line}`).
4. Fixed B13 `OutroCTA` props to match current zod schema
   (`{authorName,handle,ctaText}` → `{line,handle}`).

## Status entering PHASE 2
- Not blocked. All checks PASS/N/A/FIXED.
- Expected fill: 2 real (B12, B13 via remotion_scenes.py) + 11 vox slates
  (B01–B11 — 4 cards + 7 mechanism/graphic beats whose Manim scene classes
  are named-but-unimplemented).
- Cut type: **review slate cut** (`<slug>-slate.mp4`).
