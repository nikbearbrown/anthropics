# AUDIT — medhavy-vox-dar-optimum (Phase 1)

Channel: MEDHAVY (Kokoro `af_kore`, Okabe-Ito-adjacent teal/crimson, OutroSeries + OutroCTA).
This is a medhavy-vox reel, not a Claude/Liam reel — Claude-only bookend rules do NOT apply.

## 1. Stale renders — PASS
No mp4 in reel folder root. `clips/master.m4a` (Jul 16) is older than sheet (Aug 26)
but not an mp4 output — the audio pipeline regenerates it. Nothing to purge.

## 2. Bookends — PASS (non-Claude channel)
Rebuild rule: non-claude channels keep their own skins. Present:
- B01 title CARD (kind: title, eyebrow "CANCER NANOMEDICINE", copy + sub).
- B12 endcard CARD (kind: endcard, copy "DAR is an optimum, not a maximum.").
- B13 OutroSeries (Remotion, pattern present, rendered).
- B14 OutroCTA (Remotion, pattern present, rendered).
No `ClaudeComposerAsk` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro` — correct for medhavy.

## 3. Spark lines — N/A
No `ClaudeComposerAsk` beats in this reel; the spark-line law targets the Claude cold
open + inner composer beats. Medhavy title cards use `card.copy` / `card.sub` (populated).

## 4. Verdict — PASS
`verdict_audit.py` did not flag this reel (medhavy reels don't carry a BVDT slot; the
endcard B12 states the compressed claim — "DAR is an optimum, not a maximum. Past the
sweet spot, more warheads means less delivery." — reel-specific, not template).

## 5. Card text — PASS
Every card / document / graphic slot has a real `copy`/`sub`/`quote` — no "see narration",
"TBD", or placeholder subs. Labels within card typography-safe budget (checked visually
in `qc-sheet.png` from the prior slate pass). Manim scene labels are short category
strings from `production_viz` (`antibody + payload accumulation`, `DAR scale 0 to 10,
sweet spot 4-8`, etc.) — 1–8 words each, no narration-fragment truncation.

## 5b. Chart text — PASS
B10 bars: DAR-4 vs DAR-8 (short nouns), "24 hours" annotation, 68% / 11% values with
"illustrative" caption in small MONO — meaning agrees with narration (teal DAR-4 taller
than crimson DAR-8, matching "68% vs 11% plasma"). B09 optimum curve: axes DAR / tumor
drug delivery (short nouns). B11 document: complete-sentence quote with attribution.

## 5c. Your-Turn placeholder — N/A
Medhavy reels have no BHTF Your-Turn beat; OutroCTA points to medhavy.com. No square-
bracket placeholder present.

## 6. Punt sweep (pre-build) — LOG, review-slate cut
12 body beats slated in the build metadata (B01–B12). Each has a real intent:
- 4 CARDs (B01, B03, B08, B12) — legitimate FormA-equivalent text cards, compile.py
  renders each as a slate PNG with the request line for now.
- 6 GRAPHIC/Manim beats (B02, B04, B06, B07, B09, B10) — mapped to nopunt catalog
  (Data & quantity + Structure & relationship rows). Machine-buildable, but the reel
  has NO `scenes.py` yet, so run.sh refuses to render (guard against slotting another
  reel's graphics). LOGGED as scenes.py authoring gap — not a punt costume.
- 1 STILL (B05) — carries `shot.remotion.pattern: FormACard` fallback with real props,
  compile will render the FormA card, not a gen-AI ask.
- 1 DOCUMENT (B11) — quote card with highlight, compile.py native.
None of these are gen-AI ask slates in disguise; each is a review-slate placeholder
with a concrete authoring target. Scenes.py author-pass is queued for a later
invocation (out of scope for a single unattended review-slate build).

## 7. Card-only reel — PASS
Six body beats intend Manim graphics (B02, B04, B06, B07, B09, B10). Not a card-only
reel; the drawn figures carry the mechanism.

## 8. Lens audit — PASS
Not an anthropics-topic reel (cancer nanomedicine, hosted under anthropics/youtube/
tree), so the four-moves lens applies only if the story earns it. This one does:
- POPPER (falsifiability): B03 states the failure counter-intuition ("loading more
  warheads makes it clear faster"); B09 states both failure modes in advance
  ("under-kill... over-aggregate... fail from either direction").
- PLATO (artifact vs world): B10–B12 name the artifact (DAR-8 batch with more drug
  per molecule) and the world (0.3 vs 2.4 ug/g in tumor tissue) and the mismatched
  relationship ("more drug per molecule... delivered less drug per gram of tumor").
Two moves earned. No rewrite needed.

## 9. Brand fields — PASS
`audience: MEDHAVY`, `palette: medhavy`, `outro_source: AUTHOR.MD :: Medhavy.com`,
`engine: kokoro`, `voice_kokoro: af_kore`. No `folderLabel` field present (not a
Claude reel; folderLabel is a Claude-channel field). Persona coherence OK — narration
is neutral third-person, no "Liam, in for Bear" claim.

## 10. Pacing — PASS
All 14 beats within 2.0–3.4 wps against `actual_duration_s`:
B01 2.56, B02 3.04, B03 2.37, B04 2.54, B05 2.75, B06 2.58, B07 2.69, B08 2.68,
B09 2.61, B10 2.38, B11 2.48, B12 2.62, B13 2.56, B14 2.40.

## 11. type_check.py — deferred (run at Phase 2)

## Envelope changes (Phase 0)
- Removed `metadata.voice_id` (dead ElevenLabs field).
- Removed `metadata.clock` (dead ElevenLabs-era prose).
See REBUILD-LOG.md.

## Decision
No blockers. Proceed to Phase 2: fresh kokoro `af_kore` audio, compile a review slate
cut (`<slug>-slate.mp4`), Gate V frames + audio-presence check.
