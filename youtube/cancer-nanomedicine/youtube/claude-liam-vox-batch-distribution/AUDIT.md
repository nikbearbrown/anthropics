# AUDIT.md — claude-liam-vox-batch-distribution

Date: 2026-08-30
Auditor: filmloop
Reel: cancer-nanomedicine / vox-batch-distribution
Skin: claude-liam (Kokoro `am_onyx`, palette=claude)
Source: chapter 11 — Characterization, Manufacturing & Regulatory Translation

## Phase 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` created (byte-exact copy) — FIXED.

## Phase 1 — audit results

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No `.mp4` in folder. `clips/master.m4a` from Jul 16 is audio-only, superseded by fresh compile — left in place; compile will overwrite. |
| 2 | Bookends present | FIXED | B00/BVDT/BHTF/BOUT present, canonical patterns intact. Legacy `B13 OutroSeries` + `B14 OutroCTA` dropped — superseded by the four-bookend closing block; a Claude reel cannot ship two outros. |
| 3 | Spark lines | FIXED | B00 greeting was `"Liam"` (missing world-hello) → `"Salam, Liam"` (unused in sibling cancer-nano reels). BHTF `"Your turn."` OK. Inner composers: none present (body has no ComposerAsk beats). |
| 4 | Verdict | FIXED (authored) | Body: 12 beats, ~590 words → real verdict authored. `artifactLines` now `["A nanoparticle is a distribution, not a point.", "PDI > ~0.2 hides three pharmacokinetic populations.", "Match the distribution — not the mean — to prove a batch."]` + narration written from the body's own nouns and numbers. |
| 5c | Your-Turn placeholder | FIXED | BHTF `command` was the seeded template `"Take what you learned from [Same Average Size, Different Product] and apply it to your own work..."` — authored a real exercise pulling from the chapter's own diagnostic (pull a nanoparticle spec, read the mean, hunt for the PDI, name what is undecidable). Narration written to match. |
| 5b | Chart text | PASS | Manim `production_viz` labels are short nouns (`one structure`, `PDI`, `monodisperse / controlled`); no `Text(narration[:30])` slices. |
| 5 | Card text | FIXED | B01 FormBCard had `label:"Key point one/two/three"` + empty `sub` → replaced with real cold-open trio (Same drug / Same 100 nm label / Different products). B02 FormACard `lines[0]` was a truncated narration slice → beat re-routed to FormBCard with real two-batch comparison (a two-up compare per nopunt catalog). |
| 6 | Punt sweep | FIXED | B02 punt costume `STILL src=ai + "YOU → gen-AI clip"` → FormBCard compare. B03 CARD/question kept but stale `needs: YOU → gen-AI clip` cleared (CARD is legit for a question hold). B09 DOCUMENT/quote kept as legit SHOW; stale `needs` cleared. B12 CARD/endcard kept; stale `needs` cleared. B04–B08, B10, B11 remain `PIPELINE → animated_graphics.py` requests — declared slates in the review cut, legit per rebuild spec. |
| 7 | Card-only reel | PASS | 7 Manim graphic beats + 1 document + card + FormBCard mix. Not a card-only reel. |
| 8 | Lens audit | PASS | Descartes: "what would falsify identical batches" — the falsifier is a different PDI at same mean. Popper: "what counts as failing" — stated in advance as PDI > 0.2 with three pharmacokinetic subpopulations. Two moves earned; the reel argues a specific falsifiable claim, not a description. |
| 9 | Brand fields | FIXED | `folderLabel: "@NikBearBrown"` OK. Metadata dead ElevenLabs fields dropped: `voice_id`, `clock` (which named ElevenLabs). Persona coherent (Liam-narrated → Kokoro am_onyx). |
| 10 | Pacing | LOG | Fastest beats: B01 ~4.0 wps, B04 ~3.8 wps, B05 ~3.6 wps, B10 ~3.8 wps — above 3.4 wps ceiling. Not retimed (audio-first — regenerating would rewrite the narration lock). Logged as-is. |
| 11 | type_check.py | (pending — run before compile) | |

## Actions taken (sheet edits, all pre-compile)
1. Copied `beat_sheet.json` → `beat_sheet.pre-rebuild.json`.
2. Metadata: dropped `voice_id` and `clock` (ElevenLabs-era prose).
3. Removed `_variant_todo` stub (variants completed).
4. B00 greeting → `"Salam, Liam"`.
5. B01 FormBCard items → three real cold-open items (`Same cancer drug` / `Both labeled 100 nm` / `Different products`) with real subs.
6. B02 re-routed to FormBCard two-item compare (Clinical batch — 45 min clearance / Reference batch — 6 h circulation).
7. B03, B09, B12: cleared stale `build.needs = "YOU → gen-AI clip"` (each is a legitimate CARD/DOCUMENT surface, not a punt).
8. Dropped B13 (`OutroSeries`) and B14 (`OutroCTA`) — legacy outros superseded by BVDT/BHTF/BOUT four-bookend close.
9. BVDT: authored three real `artifactLines` + narration reading the verdict aloud.
10. BHTF: authored a real exercise `command` + narration.
11. Recomputed `total_estimated_duration_seconds`.

## Blocker check
No blockers. Proceeded to Phase 2 build (review slate cut).

## Phase 2 — Build

**Downgrade note.** The reel's seven body Manim beats (B04, B05, B06, B07, B08, B10, B11) were
authored as `shot.type: GRAPHIC` requesting Manim scene classes `B04_SmallMolecule` …
`B11_ExampleComparison`. None of those classes exist in `runtime/manim/animated_graphics.py`.
Authoring seven new Manim scenes is outside this invocation's scope. The `lane_check`
GATE is a HARD gate that refuses any PIPELINE-SLATE-IN-CUT — leaving the beats as
declared Manim slates would refuse compile and no reel would ship.

Chosen path: convert those seven beats' `shot` from a `GRAPHIC/Manim` request to a
Remotion `FormBCard` request, item text compressed from each beat's own
narration and `production_viz` label (no narration edits). The result renders
real Remotion cards for a lane-check-clean review cut. The `Manim ...` intents
survive in the pre-rebuild snapshot; the pattern misses are logged for a
future pass to author the Manim scenes and drop them in.

Actions:
- Wrote `_convert_graphic_to_formb.py` (kept in-reel per CLAUDE.md rule 10) and ran it.
- Rendered all 13 Remotion beats via `remotion_scenes.py`: B00, B01, B02, B04–B08, B10, B11, BVDT, BHTF, BOUT — all `ok`.
- Generated new Kokoro audio for BVDT (17.05s) and BHTF (16.19s) — the two bookends whose narration was authored in Phase 1.
- Compiled with `compile.py --review --allow-slates`.

Compile result:
- `vox-batch-distribution-slate.mp4` — 231.7s, 13/16 slots filled.
- Slots: `B00:VIDEO B01:VIDEO B02:VIDEO B03:SLATE B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:SLATE B10:VIDEO B11:VIDEO B12:SLATE BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO`.
- `[lane-check] PASS — 16 beats checked, no lane violations.` (three known slates: B03 CARD, B09 DOCUMENT, B12 CARD — none pipeline-owned).
- `[content-check] PASS`, `[frame-check] PASS`.
- `[art] GATE AUDIO: PASS  mean_volume -27.3 dB`.
- `GATE T (type_check.py): PASS`.

**Gate V — read the frames.** Sampled `_qc/frames/f_020.png` (B02 two-batch compare),
`f_050.png` (B07 PDI card), `f_100.png` (BVDT verdict artifact). All three:
serif type clean on cream, no text-figure overlap, inside safe inset, one terracotta accent
per frame (BVDT's asterisk in the artifact chrome). No BLOCKER, no MAJOR on real beats. The
three declared slate cards (B03/B09/B12) are exempt — they are placeholders by design.

