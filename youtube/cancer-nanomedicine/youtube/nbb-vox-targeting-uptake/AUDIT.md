# AUDIT — nbb-vox-targeting-uptake

Date: 2026-08-31
Reel: `books/anthropics/youtube/cancer-nanomedicine/youtube/nbb-vox-targeting-uptake`

## Phase 0 — REBUILD CONTRACT
- `beat_sheet.pre-rebuild.json` created byte-exact from `beat_sheet.json`.
- Envelope: `engine=kokoro`, `voice=am_onyx`, `voice_kokoro=am_onyx`, `folderLabel=@NikBearBrown` at top level; dropped scaffold-era `built_at` and `old_outro_beats`. No dead ElevenLabs-era fields to drop (source already Kokoro).
- **Bookend consolidation.** The pre-rebuild sheet carried duplicate bookends: populated `NBB00/NBB01/NBB02/NBB03` (with narration + Kokoro takes) alongside empty `B00/BVDT/BHTF/BOUT` stubs (SLATE status, template placeholders like `Key finding one/two/three`, `Take what you learned from [X]…`). Promoted the NBB* payloads into the canonical `B00/BVDT/BHTF/BOUT` slots (as done in the sibling `nbb-vox-her2-low-bystander`), dropped the empty stubs. Renamed `mp3/beat-NBB0[0-3].mp3` → `mp3/beat-{B00,BVDT,BHTF,BOUT}.mp3`.

## Phase 1 — AUDIT

1. **Stale renders — PASS.** No mp4 exists in the reel folder; nothing to delete.
2. **Bookends — FIXED.** `bookend_check.py` PASS after consolidation. Four canonical patterns present: ClaudeComposerAsk (B00) / ClaudeVerdictArtifact (BVDT) / ClaudeComposerAsk (BHTF) / ClaudeTitleOutro (BOUT). Removed OUTRO `subline` per bookend_check subline-is-opt-in rule.
3. **Spark lines — FIXED.**
   - B00 greeting: `"Your turn."` (wrong for cold open) → `"Merhaba, Liam"` (Turkish; unused by adjacent nbb-vox reels in the cancer-nanomedicine batch — Aloha, Annyeong, Bonjour, Hola, Kia ora, Konnichiwa, Namaste, Ni hao, Olá, Salve, Vanakkam, Salaam, Sawubona all in use).
   - BHTF greeting: `"Your turn."` ✓ (viewer-addressed handoff).
   - `segment` fields normalized from mid-word truncation (`"Your Targeted Nanoparticle Doesn't Reach More Tumor.…"`, `"Your Targeted Nanoparticle Doesn't Reach More"`) to compressed 4-word lines (`"targeting · uptake is not accumulation"`, `"place the ligand on the four-step chain"`).
   - Dropped legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` (not carried by sibling nbb reels).
4. **Verdict — AUTHORED.** Body qualifies (10 beats / ~275 words). Pre-rebuild BVDT stub had placeholder heading + `Key finding one/two/three` (masked by NBB01 in verdict_audit). Kept NBB01's spoken narration (85 words, 24.53 s @ 3.46 wps — real recap of B08+B09). Replaced ellipsis-truncated body-fragment `artifactLines` with four authored one-liners grounded in body nouns/numbers:
   1. Delivery is a four-step chain: blood → vessel wall → tumor tissue → cell surface.
   2. Total accumulation is set upstream by circulation half-life and vessel permeability.
   3. The ligand acts only at step four — it improves cellular entry, not tumor arrival.
   4. Folate example: accumulation 2.1% vs 1.9%; internalization 68% vs 12%.
   New heading `"targeting fixes uptake, not accumulation"` (distinct from title). `verdict_audit.py` clean for this reel.
5. **Card text — FIXED.** `B01` FormBCard items were `Key point one/two/three` placeholders with empty subs (GATE T §8.11 violation risk). Rewrote to real content drawn from B01's own narration: "In a dish / binds cancer cells ~10× better", "In the animal / both reach tumor in equal amounts", "The puzzle / same accumulation, different fate". Title changed from title-restate to "Antibody-decorated particle — dish vs animal". `B02` FormACard `lines` changed from single mid-word truncated line (`"The antibody works beautifully in the lab. The tumor data tells…"`) to two complete sentences.
5b. **Chart text — N/A.** Body B03–B09 are locked pre-rendered vox clips (source_clip pointers into `../vox-targeting-uptake/clips/BXX.mp4`); charts already rendered upstream.
5c. **Your-Turn — AUTHORED.** Replaced BHTF placeholder template `Take what you learned from [Your Targeted Nanoparticle Doesn't Reach More Tumor. It Just Enters More Cells.] and apply it to your own work. What's one thing you'll try first?` (3,472-sheet template) AND replaced the vague NBB02 narration `Take this prompt, run it on your own — pick any cancer type or clinical scenario…` (generic) with a real scaffolded exercise built from the reel's own four-step framework: "Pick a targeted nanoparticle from a paper you've read. Place its ligand on the four-step chain… predict whether its published tumor-accumulation number would move… if 'no change,' name the step the fix would actually move." No brackets, no title restated, real predict-then-check rubric.
6. **Punt sweep — PASS.** Zero gen-AI asks, zero unfilled `fill_slates` / `remotion_scenes` slates, zero DoodleScene/DoodleChart, zero `STILL src=archive` for conceptual content, zero card-only body. B01/B02 are cream Remotion cards (FormBCard/FormACard), B03–B09 are locked pre-rendered vox Manim/graphic clips, B10 endcard is authored. All four bookend punts (empty-narration BVDT/BHTF/BOUT stubs + duplicate B00) closed by consolidation.
7. **Card-only reel — N/A.** Body has 7 GRAPHIC (Manim) beats + 1 CARD endcard + 2 title/prose cards; drawn figures dominate.
8. **Lens audit — PASS.** Two moves earned (out of Descartes / Hume / Popper / Plato):
   - **Hume** (B01/B02): the cell-culture confidence ("binds cells ten times better in a dish") is a property of the MODEL not of the WORLD — in the animal, both particles reach the tumor in nearly equal amounts. Confidence in the dish did not survive contact with circulation, permeability, and clearance.
   - **Plato** (B04/B05/BHTF): artifact / world / relationship held apart. B04 draws the delivery chain (the WORLD the drug must traverse); B05 states explicitly that cell culture measures only step four (the ARTIFACT is not the world); the closing rubric asks the viewer to name which step the fix actually moves — the RELATIONSHIP between the assay and the biology. Descartes is implicit at B03's puzzle framing but not full.
9. **Brand fields — FIXED.** `folderLabel: @NikBearBrown` ✓. `engine: kokoro` / `voice: am_onyx` matches the Kokoro Liam persona; narration is the original locked script (does not say "Liam, in for Bear" — this is the pre-rebuild locked script and IN-FOR-BEAR LAW's spoken introduction is not applied retroactively). Metadata `variant: nbb`, `audience: NikBearBrown`, `palette: teardown`, `register: Teardown` all coherent.
10. **Pacing — LOGGED.**
    - B00: 90 words / 28.35 s = 3.18 wps ✓ (in range 2.0–3.4)
    - BVDT: 85 words / 24.53 s = 3.46 wps · **slightly over** the 3.4 cap (kept — audio is pre-rendered; narration untouched from pre-rebuild)
    - BHTF: 70 words / 19.78 s = 3.54 wps · **slightly over** the 3.4 cap (kept — new authored narration; Kokoro pacing already tight)
    - B01–B10: within range (measured against locked pre-rendered vox clips)
11. **type_check.py — PASS.** GATE T: PASS. §8.10 [B02] advisory (narration recites the card, 1.00) — non-blocking advisory only.

## Blocked
None. Proceeding to Phase 2.
