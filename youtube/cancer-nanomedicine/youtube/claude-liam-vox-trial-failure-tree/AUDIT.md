# AUDIT — claude-liam-vox-trial-failure-tree — 2026-08-31

## PHASE 0 — rebuild contract
- `beat_sheet.pre-rebuild.json` created byte-exact before any edit — PASS.
- Envelope normalized: dropped ElevenLabs `voice_id` and `clock` prose; added top-level `folderLabel: "@NikBearBrown"`. VOICE-LOCK confirmed (kokoro/am_onyx). See REBUILD-LOG.md.
- shot.form derivation: implicit per pattern — no TEMPLATE-MISSES row required (all patterns are in the registry: ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeTitleOutro, FormACard, FormBCard).

## PHASE 1 — audit checks
1. **Stale renders** — PASS. No mp4 existed before this pass.
2. **Bookends** — PASS. B00 ClaudeComposerAsk / BVDT ClaudeVerdictArtifact / BHTF ClaudeComposerAsk / BOUT ClaudeTitleOutro all present.
3. **Spark lines** — FIXED. B00 `greeting: "Liam"` → `"Habari, Liam"` (Swahili — unused by adjacent claude-liam / nbb-vox cancer-nanomedicine reels; log shows Bonjour, Ciao, Habari [now claimed], Kia ora, Konnichiwa, Marhaba, Merhaba, Namaste, Ni hao, Olá, Salaam, Salve, Sawubona, Vanakkam, Yassou in use). `BHTF.greeting = "Your turn."` unchanged. Only two composers in the reel.
4. **Verdict** — FIXED (AUTHORED). Body ≥ 5 beats, ≥180 words → real verdict authored from body nouns/numbers: heading `"diagnosable failure vs unattributable failure"`, four artifactLines (one-signal-three-modes, three-different-fixes, tracer-cohort-diagnoses, Program-B 7→21% PEG redesign). BVDT narration rewritten to say the finding aloud (60 words, 20.59 s @ ~2.9 wps).
5c. **Your-Turn placeholder** — FIXED (AUTHORED). Replaced 3,472-sheet template `Take what you learned from [X] and apply it to your own work` with real 4-step scaffolded exercise built on the reel's own three-failure-modes framework; `output` populated with 4-line rubric for the composer artifact.
5b. **Chart text** — PASS. Manim body scenes inherited from parent `vox-trial-failure-tree` build (Aug 28) — B04 binary endpoint, B06 three-failure split, B07/B08/B09 per-mode branches, B10 full tree with CRIMSON branches + TEAL fix chips + "RESPONSE ONLY — CANNOT SEE BELOW THIS LINE" gap block, B12 two-program illustrative comparison (LIVER 75% > TUMOR <3% bar heights match narration). Short category labels; illustrative numbers explicitly labeled.
5. **Card text** — FIXED. B01 FormBCard: `Key point one/two/three` + empty subs → three real items (`Elegant particle · Targeting ligand, chemo payload` / `6% response · Worse than standard of care` / `Program closed · No one can say why it failed`). B02 FormACard: mid-word-truncated single line → two complete sentences. B11 FormACard: same fix, two complete sentences.
6. **Punt sweep** — FIXED. Five stale `YOU → 5–10s gen-AI clip → pantry` costumes on B02, B03, B05, B11, B13 rewritten to point at the actual pipeline renderer (FormACard / CARD / DOCUMENT). Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero `STILL src=archive` for concepts. Bookend punts closed by real authoring (see checks 4, 5c).
7. **Card-only reel** — PASS. Seven Manim body beats (B04, B06–B10, B12) plus one DOCUMENT quote beat (B05) plus one endcard CARD (B13); not a card-only reel.
8. **Lens audit** — PASS, two moves earned:
   - **Popper** (B04–B10, whole reel): the naive claim "a response-only endpoint is enough to interpret a trial" is stated in advance as failing when the same negative signal has ≥ 2 mechanistically distinct causes — and the failure tree in B06/B10 makes that condition concrete (three modes, one signal). "State in advance what would count as failure" is the reel's spine.
   - **Plato** (B04, B10, B11): artifact / world / relationship held apart — the response endpoint is the artifact (a number the trial produces), the biology is the world (delivery + payload + biology cascade), and B10's RESPONSE-ONLY block draws the line explicitly. B11 proposes the operative fix — a tracer cohort — as measuring the world the artifact cannot see.
   Descartes implicit at B05 ("cannot be attributed" — a highlighted checklist item that reads Cartesian).
9. **Brand fields** — FIXED. `folderLabel: "@NikBearBrown"` at metadata top level (channel handle, not brand key). `engine=kokoro`, `voice=am_onyx`, `voice_kokoro=am_onyx` consistent. B00 narration "This is Liam, in for Bear" persona matches Kokoro am_onyx voice.
10. **Pacing** — LOGGED. Kokoro measured durations: B00 3.36 wps (44 words / 13.12 s), BVDT 2.91 wps (60 words / 20.59 s), BHTF 3.49 wps (55 words / 15.77 s — slightly over 3.4 cap, kept), BOUT 2.41 wps (15 words / 6.23 s). Body B01–B13 within range against Jul-16 measured mp3s.
11. **type_check.py** — GATE T PASS. §8.10 [B02] advisory only (0.82 narration-recites-card) — non-blocking.

## PHASE 2 — build
- **Legacy outros stripped** — B14 OutroSeries + B15 OutroCTA REMOVED. Aug-19 metadata `skin_warnings` had already flagged B15 wrong for a claude palette; BVDT → BHTF → BOUT is now the close. mp3/beat-B14.mp3 and mp3/beat-B15.mp3 kept on disk (not referenced by sheet).
- **Audio** — B00 / BVDT / BHTF / BOUT generated via Kokoro `am_onyx` (VOICE-LOCK). Body B01–B13 mp3s from Jul-16 measured takes reused (narration unchanged).
- **Renders** — 7 Remotion beats (B00, B01, B02, B11, BVDT, BHTF, BOUT) rendered via `remotion_scenes.py --force`. Body B03–B10, B12, B13 media/ symlinks → `../../vox-trial-failure-tree/clips/BXX.mp4` (parent's Aug-28 rebuild — same narration, same measured durations).
- **Compile** — `compile.py --review --force`. content-check PASS · frame-check PASS · lane-check PASS (17/17 real VIDEO, zero slates) · GATE AUDIO PASS (mean_volume −23.8 dB · 17/17 beats have audio streams).
- **Gate V** — sampled B00 (composer, Habari greeting, real ask), B01 (FormB three real items with icons), B02 (FormACard two complete sentences), B10 (full failure tree — three CRIMSON branches, TEAL fix chips, "CANNOT SEE BELOW THIS LINE" gap block), B12 (two-program illustrative comparison — bar heights match narration), BVDT (verdict artifact, real heading + numbered findings, terracotta asterisk, no placeholders), BHTF (Your Turn composer, real 4-step scaffolded prompt, output rubric), BOUT (title serif with terracotta period, @NikBearBrown, pixel mascot). All clean — no overflow past SAFE inset, no dark-mode regression, one terracotta accent per beat.
- **Motion histogram** — `drawon` 41% (7/17, over 40% pantry cap) — inherited from parent's 7 Manim body beats; non-blocking for review cut, logged for future.

## build.status Counter
`Counter({'VIDEO': 17})`

## Deliverable
`vox-trial-failure-tree-slate.mp4` — 228.9 s @ 1920×1080 (4K rendering internally, review cut is 1080p per --review). Cut mtime 03:59 > sheet mtime 03:56. Post-compile sheet edits: NONE.
