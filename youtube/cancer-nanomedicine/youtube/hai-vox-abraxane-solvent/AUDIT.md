# AUDIT.md — hai-vox-abraxane-solvent
_Generated 2026-08-28, filmloop unattended pass_

Channel: HAI (Humanitarians AI). Voice: Kokoro `am_onyx`. Cut kind: review slate.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists anywhere in the reel folder (no `media/`, no per-beat clip mp4s, no master). Only `clips/master.m4a` (audio) and PNG assets — nothing older than `beat_sheet.json` to delete. |
| 2 | Bookends | PASS (HAI variant) | Non-Claude channel: no B00/BVDT/BHTF/BOUT required. B01 is the title CARD cold open, B15 is the recap endcard, B16/B17 are HAI OutroSeries/OutroCTA (declared with `remotion.pattern`). Correct per rebuild contract §non-Claude channels. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats — no spark-line law. |
| 4 | Verdict | PASS | B15 endcard is an authored verdict from body content: "The drug never changed. The solvent did. / Cremophor was the hazard. Albumin removed it." Not a template default, would not be true of a different video, no verbatim-duplicable overlap with other reels. No `ClaudeVerdictArtifact` slot present to strip. |
| 5b | Chart text | N/A | No Manim chart scenes in this cut; every quantitative beat routed to FormBCard/FormACard with short-category labels (1–3 words) and a full-sentence sub. B09's illustrative `~10% → <1%` numbers carry the word "illustrative" per source card. |
| 5 | Card text | PASS | No FormA/FormB placeholder `sub`. Every FormBCard item has a real category label + a real one-line sub written from the beat's narration. Title-card `copy`/`sub` shortened where the pre-rebuild copy would have overflowed the safe box (B01 title, B04 question, B12 section, B15 endcard). |
| 6 | Punt sweep | PASS (review-slate exemption) | Every SLATE beat (B01 title CARD, B04 question CARD, B06 DOCUMENT quote, B12 section CARD, B15 endcard CARD) carries a real `narration_text` describing what belongs there and a matching `new_visual_element` label. Declared slate cards in a review cut are the format, not a punt. All GRAPHIC-mechanism beats (B03, B05, B07, B08, B09, B11, B13, B14) routed to real Remotion patterns per rebuild contract (props reshaped, intent locked). No `DoodleScene`/`DoodleChart`, no `STILL src=archive`, no gen-AI ask. B02 and B10 keep their `STILL src=ai` intent as `image_prompt`, but the actual delivered render is FormACard (real Remotion pattern) — the AI-still is a scripting-gap flag for a future full-render pass, not a shipping slate. |
| 7 | Card-only reel | PASS | Body mix: 4 CARD (B01/B04/B12/B15), 1 DOCUMENT (B06), 8 REMOTION FormB (B03/B05/B07/B08/B11/B13/B14 + FormA B02/B10), 1 REMOTION FormA (B09), 2 OUTRO (B16/B17). Not card-only — 9 drawn/composed Remotion beats. |
| 8 | Lens audit | PASS | Descartes (falsifier): B04 poses "the drug molecule never changed — what did?" as the falsifiable claim (something in the IV bag changed). Popper (what would count as failing): B12 states the framework's own failure mode — "not a tumor-targeting story"; the primary benefit is the formulation fix, not the leaky-vasculature hypothesis. Plato (artifact / world / relationship): B14's illustrative example separates the artifact (same paclitaxel molecule, two bags) from the world (patient hypersensitivity outcome) and names the relationship (the carrier is the variable). Two moves cleared. |
| 9 | Brand fields | FIXED | `folderLabel` set to `@humanitariansai` (matches OutroCTA `handle: "@humanitariansai"`). `engine: kokoro`, `voice_kokoro: am_onyx` describe the actual audio in `mp3/`. `voice: nbbhuman` maps to the pragmatist HAI register. Persona coherence: narration is third-person explainer, no first-person claim; HAI outros. Coherent. Slug corrected `vox-abraxane-solvent` → `hai-vox-abraxane-solvent` to match folder. |
| 10 | Pacing | PASS (nominal) | Every body beat WPS in [2.23, 2.93] — all within 2.0–3.4. B17 (5-word CTA "Find more at humanitarians.ai.") measures 1.65 wps due to OutroCTA's natural pause padding; not a delivery pacing issue and not silently retimed. |
| 11 | `type_check.py` | PASS | GATE T PASS on all 17 beats; no §8.1/§8.2/§8.3/§8.4/§8.5 fails. Five §8.10 recitation advisories (B02, B05, B09, B10, B11) — advisory only, do not block. TYPECHECK.md written. |

## Rebuild snapshot

- `beat_sheet.pre-rebuild.json` created byte-exact 2026-08-28T13:50.
- See `REBUILD-LOG.md` for LOCKED/REBUILT split and dropped-field log.

## Outcome

All PHASE 1 checks PASS or are N/A / exempt for a HAI review-slate cut. Reel proceeds to PHASE 2 build.
