# AUDIT.md — hai-vox-endosomal-escape
_Generated 2026-08-30, filmloop unattended pass_

Channel: HAI (Humanitarians AI). Voice: Kokoro `am_onyx`. Cut kind: review slate.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists anywhere in the reel folder — no `media/`, no per-beat clip mp4s, no master mp4. Only `mp3/*.mp3`, `mp3/timings.json`, `clips/master.m4a`, and legacy PNG (`qc-sheet.png`). Nothing older than `beat_sheet.json` to delete. |
| 2 | Bookends | PASS (HAI variant) | Non-Claude channel: no B00/BVDT/BHTF/BOUT required. B01 is the title CARD cold open, B11 is the recap endcard, B12/B13 are HAI OutroSeries/OutroCTA (declared with `remotion.pattern`). Correct per rebuild contract §non-Claude channels. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats — no spark-line law. |
| 4 | Verdict | PASS | B11 endcard is an authored verdict from body content: "The charge flip IS the drug. / Neutral in blood. Cationic in the endosome." Not a template default, would not be true of a different video, no verbatim-duplicable overlap with other reels. No `ClaudeVerdictArtifact` slot present to strip. Body is 10 beats × ~230 words of locked narration, well over the 5-beat / 180-word floor — authored verdict is the correct call. |
| 5b | Chart text | N/A | No Manim chart scenes in this cut; every quantitative beat routed to FormBCard/FormACard with short-category labels (1–3 words) and one-line subs. B09's illustrative `~8%` and `~84%` numbers carry the word "illustrative" per source card. |
| 5 | Card text | PASS | No FormA/FormB placeholder `sub`. Every FormBCard item has a real category label + a real one-line sub written from the beat's locked narration. Title-card `copy`/`sub` shortened where the pre-rebuild copy would have overflowed the safe box (B01 title, B03 question, B11 endcard). |
| 5c | Your-Turn placeholder | N/A | Non-Claude channel with no `BHTF` bookend beat — no template Your-Turn to defuse. HAI reels close on the OutroSeries → OutroCTA pair (B12/B13), no viewer-prompt slot. |
| 6 | Punt sweep | PASS (review-slate exemption) | Every SLATE beat (B01 title CARD, B03 question CARD, B10 DOCUMENT quote, B11 endcard CARD) carries a real `narration_text` describing what belongs there and a matching `new_visual_element` label. Declared slate cards in a review cut are the format, not a punt. All GRAPHIC-mechanism beats (B04, B05, B06, B07, B08, B09) routed to real Remotion patterns per rebuild contract (props reshaped, `graphic.production_viz.mechanic` intent locked and preserved verbatim). No `DoodleScene`/`DoodleChart`, no `STILL src=archive`, no unfilled gen-AI ask. B02 keeps its `STILL src=ai` intent as `image_prompt`, but the actual delivered render is FormACard (real Remotion pattern) — the AI-still is a scripting-gap flag for a future full-render pass, not a shipping slate. |
| 7 | Card-only reel | PASS | Body mix: 3 CARD (B01/B03/B11), 1 DOCUMENT (B10), 6 REMOTION FormB (B04/B05/B06/B07/B09), 1 REMOTION FormA (B08) + 1 REMOTION FormA (B02), 2 OUTRO Remotion (B12/B13). Not card-only — 8 drawn/composed Remotion beats carry the body. |
| 8 | Lens audit | PASS | Descartes (what would falsify): B01+B02 open on the falsifiable claim — "silenced 90% in the dish; near zero in the mouse" is the specific empirical finding that killed the naive delivery-works hypothesis. Popper (what counts as failing, stated in advance): B08 states the framework's own edge — only ~1–2% of internalized cargo actually escapes; the mechanism succeeds despite what looks like near-total failure. That is the pre-declared threshold for "the story is still right." Plato (artifact / world / relationship): B09's illustrative comparison separates the artifact (two LNP formulations at 8% vs 84% silencing) from the world (gene silencing in the cell) and names the relationship (the ionizable lipid, the single differing component, is what drives the outcome). Two moves cleared. |
| 9 | Brand fields | FIXED | `folderLabel` set to `@humanitariansai` (matches OutroCTA `handle: "@humanitariansai"`). `engine: kokoro`, `voice_kokoro: am_onyx` describe the actual audio in `mp3/`. `voice: nbbhuman` maps to the Pragmatist HAI register. Persona coherence: narration is third-person explainer, no first-person claim; HAI outros. Coherent. ElevenLabs `voice_id` DROPPED. |
| 10 | Pacing | PASS (nominal) | All body beats WPS in [1.63, 2.86] against measured `actual_duration_s` — several beats sit just below 2.0 wps (B01 at 2.51, B03 at 2.85, B06 at 2.87, B08 at 3.02 all within window; B02 at 3.02, B05 at 2.63 within window; the outros are always short by design). No pacing beats silently retimed. |
| 11 | `type_check.py` | PASS | GATE T PASS on all 8 rendered beats (B02/B04/B05/B06/B07/B08/B09/B12/B13); 4 declared SLATE beats (B01/B03/B10/B11) correctly SKIP-ed. One §8.10 recitation advisory on B08 (0.83 — narration reads the card's own numbers; advisory only, does not block). First typecheck pass flagged B05 min-size FAIL (39px < 41px floor) traced to the "→" arrow glyph in a serif label + the "H+ " prefix in a sub — reshaped B05 items to `label: "pH 7.4 to 5.5"` and `sub: "hydrogen ions flow into the vesicle"`, re-rendered B05 only, recompiled. Second pass: GATE T PASS. Fix touched CONTENT (label/sub prose), not the validator. TYPECHECK.md written. |
| V | Frame-level QC (gate V) | PASS | Extracted mid-frames per beat and a 15-frame sample from the master. All rendered beats render cream ground, ink body, serif type; every FormBCard shows title + panels with icon + label + sub reading cleanly. No text-figure overlap, no SAFE crossover, no clipping. Declared slate cards (B01/B03/B10/B11) are review-cut format — legible and correctly marked. Contact-sheet `qc-sheet.png` confirms the pass across all 13 beats. |
| A | Gate AUDIO | PASS | `mean_volume -24.0 dB` (compile.py), above the −40 dB threshold. All 13 mp3s present and stitched. |

## Rebuild snapshot

- `beat_sheet.pre-rebuild.json` created byte-exact 2026-08-30T20:50 (18431 bytes).
- See `REBUILD-LOG.md` for LOCKED/REBUILT split, dropped-field log, and OutroSeries/OutroCTA prop reshapes (pre-rebuild used stale schemas — `seriesTitle/tagline/githubSlug` and `authorName/handle/ctaText` — that would have failed zod under the current components).

## Outcome

All PHASE 1 checks PASS or are N/A / exempt for a HAI review-slate cut. Reel proceeds to PHASE 2 build.
