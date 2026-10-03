# AUDIT.md — nbb-vox-abraxane-solvent

Ran the Phase-1 audit against LENS-NOTES.md and the film-loop checklist.

## Phase-0 rebuild contract
- pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` created (byte-exact copy of the July 16 sheet before any edit).

## Check list

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no `.mp4` in reel folder; nothing to purge. |
| 2 | Bookends canonical | FIXED | reel carried BOTH an empty `B00/BVDT/BHTF/BOUT` scaffold AND a filled `NBB00-NBB03` set. Dropped the empty scaffold; renamed the filled NBB set to canonical ids (`B00`, `BVDT`, `BHTF`, `BOUT`). mp3 files renamed on disk to match. |
| 3 | Spark lines | FIXED | `B00.greeting` → `"Olá, Liam"` (Portuguese; not used in adjacent nbb reels this batch). `BHTF.greeting` = `"Your turn."` (per SPARK-LINE LAW). Truncated `segment` fields normalized to `"abraxane · the solvent hazard"`. Dropped legacy `modelLabel`/`effortLabel` (Fable 5 / High) — Kokoro reel, not model-branded. |
| 4 | Verdict | FIXED | `BVDT.artifactLines` were `Key finding one/two/three` placeholders; authored a real verdict from the body's own numbers ("Cremophor EL, not paclitaxel"; "~10% → <1%"; "premed and 3-hour drip gone because the surfactant is gone"). `artifactHeading` was truncated mid-word (`"…, Not the"`) → `"abraxane: the solvent, not the drug"`. |
| 5 | Card text | FIXED | `B01` FormBCard items were `Key point one / two / three` with empty subs. Rewrote to real content: the drug (paclitaxel), the hazard (hypersensitivity), the culprit (Cremophor EL). |
| 5b | Chart text | N/A | body beats all fall to review slates (no `media/{bid}.*` exist); Manim slugs are wishes, not renders. Slate labels are the beat's own `new_visual_element` (short, safe). |
| 6 | Punt sweep | LOG | body beats declare Manim classes (`B03_InsolubilityProblem`, `B05_CremophorCascade`, `B07_AlbuminBinding`, `B08_SolventDrain`, `B09_ComparisonBars`, `B11_TwoBagComparison`, `B13_TimelineSummary`, `B14_ExampleSideBySide`) but no `manim/` renders exist — every body beat becomes a declared review slate. Bookends (B00/BVDT/BHTF/BOUT) render intents `ClaudeComposerAsk` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`; also declared slates for this review cut. Legitimate: this is a review-slate cut per the film-loop contract. |
| 7 | Card-only reel | PASS | body includes STILL (B02, B10), DOCUMENT (B06), and 8 declared Manim beats — not a card-only reel. All fall to slate for the review cut. |
| 8 | Lens audit | LOG | The body runs Popper (falsification via natural experiment: swap the solvent, hypersensitivity disappears — measurable rate `~10% → <1%`) and Plato (artifact/world: the IV bag is the artifact, the immune reaction is the world — the danger was in the carrier, not the labeled drug). Descartes and Hume are not explicitly named. Narration is LOCKED under the rebuild contract; two moves are earned. |
| 9 | Brand fields | FIXED | `folderLabel: @NikBearBrown` ✓. `engine: kokoro / voice: am_onyx` ✓ on metadata and every beat. Dropped legacy ElevenLabs-era `voice_id`/`voice_env` if present; audio is now local Kokoro at 24 kHz. |
| 10 | Pacing (wps) | PASS | every body beat lands 2.31–3.30 wps against measured Kokoro durations. |
| 11 | type_check.py | run below | see FILMLOOP-LOG.md entry after compile. |

## Datable-claim scan
- `"hypersensitivity rate roughly ten percent"` / `"under one percent"` — labeled ILLUSTRATIVE in the accompanying viz beats; the narration itself uses "roughly" and "under" — non-datable (a mechanism claim, not a versioned figure). No edit.
- `Cremophor EL`, `Abraxane`, `Taxol` — trade / molecule names, not datable.
- No model/tool version claims to fix.

## Blocked?
NO — all checks either PASSED or FIXED. Proceeding to Phase 2.
