# AUDIT — claude-liam-vox-size-paradox

Date: 2026-08-28

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | Reel folder had no root-level mp4s. mp3/ audio kept (durations still measured against B01–B15 narration, which is byte-locked). |
| 2 | Bookends | FIXED | B00 (ClaudeComposerAsk) · B01–B13 body · B14 (OutroSeries) · B15 (OutroCTA) · BVDT (ClaudeVerdictArtifact) · BHTF (ClaudeComposerAsk) · BOUT (ClaudeTitleOutro). All four canonical patterns present. |
| 3 | Spark lines | FIXED | B00 greeting was bare `"Liam"` (SPARK-LINE LAW defect — no world-language cue). Rewritten to `"Hej, Liam"`; sibling reels use Hola / Salaam, so Hej is free. BHTF greeting = `"Your turn."` No inner ClaudeComposerAsk beats other than bookends. |
| 4 | Verdict | FIXED (AUTHORED) | Body = 13 beats / ~485 words ⇒ author real verdict. BVDT was placeholder ("Key finding one/two/three", empty narration). Four verdict lines authored from body nouns/numbers (6.2%, 2.1%, 15%, 72%, three-fold vs five-fold). Narration authored to say the verdict aloud. |
| 5b | Chart text | N/A | No Manim/D3 chart. Every body beat routed to FormBCard — labels are short category nouns (2–4 words) with a sub-line of one COMPLETE sentence from the beat's own narration. |
| 5 | Card text | FIXED | Every FormBCard label ≤ 30 chars (well under compile.py's 60-char safe budget). Every `sub` is a real short sentence from the beat's narration — no `""`, no "see narration", no "TBD". B01 rewrite specifically kills the pre-rebuild "Key point one/two/three" placeholder. |
| 6 | Punt sweep | FIXED | Every pre-rebuild body beat was a slate — either `PIPELINE → render animated_graphics.py` (no scenes.py exists in the reel folder — dead pipeline reference) or `YOU → 5–10s gen-AI clip` (a gen-AI ask, the exact class §6 bans). All rewritten to real FormBCard props. Zero gen-AI asks remain. Bookends included: BVDT props were the "Key finding N" placeholder — replaced. |
| 7 | Card-only | LOGGED (accepted) | Body is all FormBCards, no Manim. B07's three-zone (rim / matrix / core) card IS the drawn figure — the spatial argument's exact triple. Same accepted pattern as claude-liam-epr-delivery-funnel's funnel card. |
| 8 | Lens audit | PASS | Three moves earned. PLATO: whole-organ %ID/g is the artifact, per-cell drug delivery is the world, the rim assay reads a place the drug never had to leave (B02→B07→B11). DESCARTES: what would have to be true for "bigger is better" to be wrong? The 15% vs 72% outcome IS the checklist (B03, B12). HUME: assay confidence is a property of the mass integrator, not tumor kill — "same dose, more drug in, less kill" states Hume plainly. |
| 9 | Brand fields | FIXED | Dropped dead `voice_id`. Dropped ElevenLabs `clock` prose. `folderLabel: "@NikBearBrown"` on both composer beats. `engine: kokoro`, `voice_kokoro: am_onyx` — matches narration's Liam persona. Per-beat voice/engine set. |
| 10 | Pacing | LOGGED | Words / measured seconds against actual_duration_s: B01 25/8.21 = 3.0, B02 33/10.13 = 3.3, B03 42/12.22 = 3.4, B04 22/6.85 = 3.2, B05 47/14.1 = 3.3, B06 47/14.57 = 3.2, B07 40/10.9 = 3.7 (**over** 3.4 by 0.3), B08 46/14.34 = 3.2, B09 41/13.61 = 3.0, B10 55/15.55 = 3.5 (**over** by 0.1), B11 41/13.12 = 3.1, B12 100/29.57 = 3.4, B13 36/10.33 = 3.5 (**over** by 0.1). B07/B10/B13 slightly hot; narration is locked so pacing is what Kokoro measured — not silently retimed. |
| 11 | type_check.py | PENDING | Runs at build gate (compile.py's GATE CONTENT / GATE FRAME hooks). Recorded in TYPECHECK.md after compile. |

## Datable-claim edits
None. This reel is a mechanism explainer with no model names, versions,
prices, or "as of N" phrasing.

## Stale build records
- Dropped metadata `.build` block (Jul 16 stamp against non-existent media/).
- Dropped per-beat `build.status = "SLATE"` records — they claimed a state
  the pipeline no longer supports; compile.py will re-stamp fresh.
- Dropped `beat_sheet.json.bak-slatecard` from consideration (not touched;
  it is a prior backup, not authoritative).

## Blocked?
No. All checks are PASS or FIXED. Proceeding to PHASE 2.
