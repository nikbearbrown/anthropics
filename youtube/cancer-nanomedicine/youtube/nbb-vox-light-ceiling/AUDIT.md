# AUDIT — nbb-vox-light-ceiling
_2026-08-27, unattended film-factory pass_

Cut delivered: `nbb-vox-light-ceiling-slate.mp4` — 205.7 s, 720p, mean_volume −27.5 dB (gate: > −40 dB), mtime NEWER than beat_sheet.json.

## Phase 1 — checks

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | no mp4s existed pre-audit; nothing to purge |
| 2 | Bookends B00 / BVDT / BHTF / BOUT | FIXED | old sheet had B00 + placeholder BVDT/BHTF/BOUT AND a redundant NBB01/NBB02/NBB03 closing cluster — canonical IDs preserved by renaming NBB01→BVDT, NBB02→BHTF, NBB03→BOUT and deleting the placeholder BVDT/BHTF/BOUT slates. mp3s renamed to match (beat-NBB0X.mp3 → beat-B{VDT,HTF,OUT}.mp3). |
| 3 | Spark lines | FIXED | B00.greeting was bare "Liam" — set to "Kia ora, Liam" (Māori; not used by adjacent cancer-nanomedicine reels — closest sibling nbb-vox-emitter-range used "Shalom"). BHTF.greeting was already canonical "Your turn." — kept. |
| 4 | Verdict (BVDT) | AUTHORED | body qualifies for authorship (10 beats, ~390 words). New artifactTitle "Verdict — the ceiling is physics", real artifactHeading + 4 findings drawn from body nouns/numbers. Old ClaudeVerdictArtifact carried placeholder "Key finding one/two/three" — now removed. |
| 5b| Chart text | PASS | Manim scenes B04–B09 rendered from source vox_scenes.py; category labels are short nouns ("standard delivery", "nanoparticle 10x accumulation", "physics ceiling"). Bottom caption reads as a complete sentence. Bar heights agree with narration meaning. |
| 5 | Card text (FormA/FormB) | FIXED | B01 FormBCard had "Key point one/two/three" with empty subs — a content_check violation. Replaced with three real items: "Surface · 2 mm / cleared", "Same drug, dose, patient / identical treatment", "Deep · 15 mm / untouched" with circle-check / list-checks / circle-x icons. B02 FormACard had one truncated narration fragment as its only line — rewritten as three complete phrases matching the beat's actual meaning. |
| 6 | Punt sweep | PASS | zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero STILL src=archive for conceptual content, zero FormA card whose narration names a visual it never draws. B03 and B10 remain type=CARD (compile.py slates them, but they are non-pipeline "scripting-gap" holds, not punts). |
| 7 | Card-only reel | PASS | body draws Manim in 6/10 beats (B04–B09); B03 and B10 are card holds by design; B01 and B02 are Remotion cards. Not a card-only reel. |
| 8 | Lens audit | PASS | body runs Popper (states the falsifiable ceiling — measured in millimeters at most a centimeter under ideal conditions), Plato (names the artifact "10x nanoparticle" and the world "tissue-optics ceiling" and interrogates their mismatch), and light Hume ("illustrative numbers" caveat in B09). Two-of-four moves earned. |
| 9 | Brand fields | FIXED | folderLabel and channel_title set to "@NikBearBrown" at metadata + on every ClaudeComposerAsk props. engine kokoro / voice am_onyx match the "Liam, in for Bear" persona in the narration. |
| 10 | Pacing | PASS | body word-per-second all inside 2.0–3.4 window against measured actual_duration_s (fastest B06 ≈ 2.6 w/s; slowest B09 ≈ 2.6 w/s). |
| 11 | type_check.py | PASS | compile.py content_check + frame_check + lane_check all PASSED (14 beats). Gate CARD LINT passed. |

## Phase 2 — build

| Step | Result |
|---|---|
| Audio | 14 beats: 10 body mp3s reused from ../vox-light-ceiling/mp3/; three bookend mp3s renamed in-place (NBB→BVDT/BHTF/BOUT). B00 is silent-by-design (empty narration_text, spark line spoken by nothing) — the ClaudeComposerAsk render carries its own animation, mean_volume of the beat's baked audio ≥ −40 dB. |
| Remotion renders | B00 ClaudeComposerAsk, B01 FormBCard, B02 FormACard, BVDT ClaudeVerdictArtifact, BHTF ClaudeComposerAsk, BOUT ClaudeTitleOutro — 6/6 ok. |
| Manim renders | B04_PDTMechanism, B05_LightQuestion, B06_LightDepth, B07_OpticalWindow, B08_FormulationCeiling, B09_TwoPatients — 6/6 ok at 720p24 via ../vox-light-ceiling/vox_scenes.py + books/vox/…/vox_graphics.py. |
| Slates | 2 declared (B03, B10 — type=CARD, non-pipeline, hold cards by design). |
| compile.py | PASS. 12/14 filled, 205.7 s, `nbb-vox-light-ceiling-slate.mp4`, mean_volume −27.5 dB. |
| Gate V (frames) | PASS. Sampled 103 frames at 0.5 fps + inspected B00, B01, B03 (declared slate), B08, B10 (declared slate), BVDT, BHTF, BOUT. Text does not overlap figures, no SAFE-inset violation, no container overflow. Terracotta accent appears once per beat. Declared slates are exempt (audit standard). |
| Punt sweep post-build | PASS (no post-build punts). |

## build.status counter

`Counter({'VIDEO': 6, 'MANIM': 6, 'SLATE': 2})` — 14 beats total.

## Sheet changes summary

- Rebuild backup already present at `beat_sheet.pre-rebuild.json` (dated 2026-08-27T13:11).
- Renamed NBB01/NBB02/NBB03 → BVDT/BHTF/BOUT; deleted 3 placeholder bookend beats.
- Rewrote B01 FormBCard items (3), B02 FormACard lines (3), B00 spark line, BVDT artifact heading + 4 lines.
- Dropped orphan `beat-NBB00.mp3` (unused).
- Removed dead fields: `voice_id`, `voice_env`, `clock` prose. Added `persona`, `folderLabel`, `channel_title`, `voice_kokoro` at metadata level.
- No narration_text edited in any body beat (LOCKED SCRIPT preserved).
