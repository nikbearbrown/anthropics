# AUDIT — claude-liam-ifp-pressure-barrier
_Rebuilt 2026-08-30 by nopunt / audit pass. Deliverable: review-slate cut._

Pre-rebuild backup: `beat_sheet.pre-rebuild.json`.  Rebuild details:
`REBUILD-LOG.md`.

## Phase 1 — checks

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 in folder pre-audit; nothing to delete. |
| 2 | Bookends B00/BVDT/BHTF/BOUT | FIXED | B00 converted from `NikBearBrownOpen` → `ClaudeComposerAsk`; BVDT/BHTF/BOUT already Claude patterns; content authored below. |
| 3 | Spark lines | FIXED | B00 greeting `"Bonjour, Liam."` (rotates; not adjacent-repeated). B02 greeting `"Research the IFP problem."` (was `"The ask,"`). B05 greeting `"The normalization window."` (was `"The ask,"`). BHTF `"Your turn."` All inner composers now ≤4 words compressed from beat narration. |
| 4 | Verdict (BVDT) | AUTHORED | Was placeholder `"Key finding one/two/three"` + empty narration. Now three lines drawn from the body (IFP reverses convection; leaky vessels are the same cause on both sides; mouse window 2–6 days, human window unclear, no survival benefit). Narration speaks the finding. Body is 8 beats / ~482 words → author, don't strip. |
| 5 | Card text (subs/labels) | FIXED | B01 FormBCard: 3 items with real short labels + real subs from B01 narration. |
| 5b | Chart text | FIXED | B04 BarChart uses 1-word categories (`Normal`, `Solid tumor`, `Pancreatic`), unit `mmHg`, short title. Accent on `Pancreatic` (worst-case tissue) per key-finding rule. |
| 5c | Your-Turn (BHTF) | AUTHORED | Was template `"Take what you learned from [X]…"`. Now a real exercise sourced from B08: pull IFP for viewer's tumor type, check orthotopic vs subcutaneous, check for normalization/losartan pretreatment. `output` slots populated with a real worksheet. |
| 6 | Punt sweep | FIXED | B04/B06/B07/B08 were pipeline/gen-AI SLATE punts. All redirected per nopunt catalog: B04 → FormBCard "IFP by tissue" (see rule 7 note); B06/B07/B08 → FormBCards with real labels + subs from their own narration. Zero `YOU → gen-AI clip → pantry`, zero unfilled slates for animatable content. |
| 7 | Card-only reel | PARTIAL | Body drawn figures are the FormBCards (5 body FormB's) plus the terminal + code interface skins (B02/B03/B05, real code/composer artifacts, not text cards). B04 was originally routed to a `BarChart` (a genuinely drawn figure) but the BarChart Remotion component is broken at 3840×2160: bars render invisible, category and value labels crushed against the top edge; reproduced on every timestamp of the raw B04.mp4. Fixing the component is out of scope for a single-reel rebuild pass; leaving B04 as an unfilled pipeline slate would restore a punt costume. Routed B04 to FormBCard instead — logged here as a partial concession. |
| 8 | Lens (Descartes / Hume / Popper / Plato) | PASS | Popper (falsifiability stated in advance): "no survival benefit has been demonstrated yet" — delivery is the surrogate; the survival endpoint is the pre-declared falsifier still open. Plato (artifact ≠ world): B08 separates the model (subcutaneous mouse tumor with low IFP) from the world (orthotopic / clinical tumor). |
| 9 | Brand fields | FIXED | `folderLabel: "@NikBearBrown"` (channel handle) in composer beats. Metadata voice/engine (kokoro, am_onyx) match every beat carrying voice fields. Narration says "This is Liam, in for Bear" — voice is Kokoro `am_onyx` (Liam): persona coherent. |
| 10 | Pacing (2.0–3.4 wps) | PASS | All body beats 2.40–3.25 wps. BOUT is 0 wps (silent title outro by design — ClaudeTitleOutro takes no narration). |
| 11 | `type_check.py` GATE T | PASS | After dropping the extra `title` prop from B09 `NikBearBrownOutro` (not in its schema), GATE T = PASS, 0 FAILs. |

## Phase 2 — build

Delivered: `ifp-pressure-barrier.mp4` — a full-render master (13/13 beats
rendered, no slates). 216.7s at 3840×2160, per-beat narration muxed.

Audio: pre-existing Kokoro `am_onyx` (Liam) mp3s for B00–B09 retained; BVDT
and BHTF freshly generated (Kokoro, `am_onyx`) for the newly-authored
narration. Timings written back to sheet. BOUT is a silent title outro (its
mp4 carries its own audio).

Gate LANE: PASS (0 pipeline slate, 0 gen-AI-in-master; 13/13 filled).
Gate AUDIO: PASS mean_volume −24.0 dB, max_volume −3.0 dB (AAC stream present).

Gate V (frames read at 1/6 fps → 36 QC frames):
- B00 ClaudeComposerAsk: greeting "Bonjour, Liam." with terracotta spark;
  full ask visible in composer; folder chip `@NikBearBrown`; running text
  "physics before biology…". Clean.
- B01 FormBCard "The pressure barrier": three panels, real labels + subs,
  ruler / crosshair / zap icons. Legible, no overflow.
- B03 NikBearBrownCodeBlock: full `ifp_gradient.py` code visible, monospace,
  cream ground.
- B04 FormBCard "IFP by tissue (mmHg)": three tissues with ranges (0–3 /
  20–60 / up to 80), circle-check / shield-alert / circle-x icons.
- B05 NikBearBrownTerminalAsk: dark terminal with the vascular-normalization
  ask; running text "evaluating normalization window…". Clean.
- B06 FormBCard "What the revision returned": mouse window / losartan /
  trial status; snowflake / layers / clipboard-list icons.
- BVDT ClaudeVerdictArtifact: real verdict lines; paginated (2 lines
  visible plus a 2/2 spillover for the third — component pagination, not
  content loss).
- BHTF ClaudeComposerAsk: real Your-Turn ask with the worksheet
  (`IFP range for your tumor: ____ mmHg` etc.) visible.
- BOUT ClaudeTitleOutro: full title on dark ground with mascot; clean.

No BLOCKER, no MAJOR on any real beat. Terracotta accents held one per
frame (spark asterisks in the composer beats; icon accents in FormBs).

## Rules held

- Narration was NOT rewritten except for the newly-authored bookend
  narrations (BVDT, BHTF) that were previously empty strings. Every B00–B09
  narration is byte-identical to the pre-rebuild sheet.
- No datable-claim edits were required (IFP ranges, mouse window duration,
  losartan mechanism, Jain NCT trial status remained accurate).
- No validator was loosened; type_check FAIL was fixed by removing an
  out-of-schema prop, not by weakening the check.
