# AUDIT.md — vox-endosomal-escape

Ran 2026-08-27, unattended film-factory pass.

## Phase 0 — rebuild contract

- Snapshot: `beat_sheet.pre-rebuild.json` written byte-exact from old sheet — DONE.
- Dead ElevenLabs fields (`voice_id`, `clock` prose) — DROPPED.
- Metadata voice envelope normalized: `voice: nbbhuman`, `engine: kokoro`, `voice_kokoro: am_onyx`.
- `folderLabel: "@NikBearBrown"` + `short_title: "The pH-Triggered Lock"` added.
- Non-Claude channel skins retained: OutroSeries (B12) + OutroCTA (B13) — not Claude-washed.
- Stale build stamps (top-level + per-beat) claimed `filled 13/13` while zero mp4s exist on disk — DROPPED so fresh compile can re-stamp honestly.
- Narration is LOCKED. No datable claims found — pure biology mechanism.

## Phase 1 — checks

1. Stale renders — PASS. No mp4s on disk anywhere in this reel folder (never rendered).
2. Bookends — PASS (per amendment). No Claude bookends (B00/BVDT/BHTF/BOUT). This is the legacy vox-explainer format on the NikBearBrown channel; the rebuild contract keeps the channel's own skins (OutroSeries B12, OutroCTA B13). BVDT legitimately absent.
3. Spark lines — N/A. No `ClaudeComposerAsk` beats in the reel.
4. Verdict — N/A. No BVDT beat present. Body ends with B10 quote-lock + B11 recap-card ("Neutral in blood. Cationic in the endosome. That charge flip is the drug.") — the reel already carries a stated conclusion in its own idiom. Vox-explainer format does not run a Claude verdict artifact.
5. Card text — PASS. B01 title-card copy is the full reel title; B03 question-card copy is 8 words; B11 endcard is 12 words. B10 highlighter phrase "pH-sensitive lock" is legitimate. B02 FormACard `lines` is a 12-word line summarizing the narration (no placeholder). No `sub` = "TBD"/"see narration"/empty across the reel.
5b. Chart text — PASS. Chart axis labels in `vox_scenes.py` are short category nouns (`pH 7.4`, `pH 5.5`, `endosome`, `cytosol`, `LNP-A neutral lipid`, `LNP-B ionizable lipid`, `~1-2%`, `internalized`, `escapes`, `rate-limiting step`). Captions are complete phrases. Bar heights agree with narration meaning (B09: LNP-A crimson bar `height=0.6` for 8% vs LNP-B teal bar `height=4.5` for 84% — the favored thing is taller). No `Text(narration[:30])` truncations.
6. Punt sweep — PASS. Zero gen-AI asks in the sheet. Every body beat draws real content: B01 title-manim, B02 an AI-generated STILL (`FormACard` slate is the current pipeline slot; the reel's `image_prompt` carries the future gen brief), B03-B11 native Manim scenes, B12/B13 Remotion outros. No unfilled `fill_slates` or `remotion_scenes`. No DoodleScene/DoodleChart. No `STILL src=archive`. No FormACard names a visual it never draws.
7. Card-only reel — PASS. Nine drawn Manim beats (B01/B03-B11) plus two Remotion outros; only B02 is a still. Not a card-only reel.
8. Lens audit — PASS. Popper (state what would count as failing: "1-2% escape rate — still enough to act" states the failure threshold in advance, a Popperian claim about what the mechanism must clear). Descartes (the cold open runs radical doubt: "The siRNA worked. In the dish, it silenced its target 90 percent. In the mouse, it did almost nothing" — what would have to be true for the in-dish result to predict the in-body result? It doesn't). Plato/Cave (implicit throughout: the artifact is the siRNA silencing measurement, the world is the endosomal trap, the relationship is that the artifact measures cytosolic access, not delivery; the reel names the wrong-failure). Three moves earned.
9. Brand fields — FIXED. `folderLabel: "@NikBearBrown"` added (matches OutroCTA `handle`). `engine: kokoro` + `voice: nbbhuman` describe the actual audio. Persona coherence: narration is explainer voice with no first-person claim; NikBearBrown attribution appears only in the outros — voice-lock `nbbhuman`/`am_onyx` is coherent.
10. Pacing — LOG. WPS scan (words / actual_duration_s):
    - B01 2.85 · B02 2.73 · B03 2.72 · B04 2.71 · B05 2.44 · B06 2.58 · B07 **1.99** (below 2.0 floor by 0.01) · B08 2.61 · B09 **1.77** (below 2.0 floor) · B10 2.65 · B11 2.56 · B12 2.76 · B13 3.36.
    B07 is 0.01 below floor — effectively at the boundary; not retiming. B09 is genuinely slow (23.12s for 41 words); this is the LNP-A vs LNP-B illustrative comparison with numeric emphases — leaving as-is. LOGGED only; no silent retime.
11. `type_check.py` — N/A on this reel. The Brutalist type_check.py measures Remotion pattern typography (§8.1–§8.6 min-size / overflow / contrast / kerning / wordy-card / golden-strings) on rendered PNGs; this reel is Manim-driven with only two Remotion outros. Gate B (post-render pixel audit) inside `vox_run.sh` covers the Manim scenes at render time. Deferred to Gate V (post-compile frame read).

## Phase 2 — build

Proceeding to Kokoro audio refresh, Manim renders via `vox_run.sh`, and Brutalist `compile.py` for the slate-review cut.
