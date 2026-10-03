# AUDIT — protein-corona-overwrites
_2026-08-27, unattended film-factory pass_

Cut delivered: `protein-corona-overwrites-slate.mp4` — 241.7 s, 720p, mean_volume −24.0 dB (gate: > −40 dB), mtime NEWER than beat_sheet.json (+8.3 s).

## Phase 1 — checks

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | no stale mp4s in reel (stale_check.py at anthropics root: 0 stale, this reel among 34 fresh) |
| 2 | Bookends B00 / BVDT / BHTF / BOUT | PASS | canonical set present. B00 uses NikBearBrownOpen (channel-native, not Claude-washed per rebuild §Non-claude channels keep their own skins). BVDT/BHTF/BOUT stay Claude-branded bookends. |
| 3 | Spark lines | FIXED | B00 uses NikBearBrownOpen (no greeting field). B02/B05 greeting was "The ask," → replaced with 3-word cues compressed from narration ("Research the corona." / "Iterate the ask."). BHTF greeting already "Your turn." |
| 4 | Verdict (BVDT) | AUTHORED | body qualifies (13 beats, ~430 words). Placeholder "Key finding one/two/three" replaced with 4 real findings drawn from body nouns/numbers. artifactTitle now "Verdict — the corona is the product". BVDT narration authored (was empty) — spoken recap saying the verdict aloud. |
| 5 | Card text (FormA/FormB) | FIXED | B01 FormBCard had "Key point one/two/three" placeholders with empty subs — content_check violation. Rewrote all 3 items with real labels + real sub lines drawn from the beat's narration. B06/B07/B08 were `shot.type: GRAPHIC, source: null` — pipeline-slate lane violation. Upgraded to FormBCard patterns with real 3-item content authored from each beat's narration. Every icon resolved to available public/form-b-icons/ svg (shield, shield-alert, target, layers, clipboard-list, ruler, list-checks, zap, circle-x). |
| 5b| Chart text | PASS | only Manim beat is B04 (B04_ProteinCorona) rendered from vox_scenes.py. Vox_scenes.py path resolution was broken (parents[3] resolved to a non-existent path); patched to auto-discover books/vox/aspects/explainer/vox-explainer/manim via a small loop. Category labels are short nouns ("ENGINEERED NANOPARTICLE", "targeting ligands"). |
| 6 | Punt sweep | PASS | zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero STILL src=archive, zero FormA card whose narration names a visual it never draws. Every body beat renders a real component. |
| 7 | Card-only reel | PASS | B04 draws Manim; B00/B02/B03/B05/B09 draw NikBearBrown terminal/code/open/outro components; B01/B06/B07/B08 draw FormBCard; bookends draw Claude patterns. Not a card-only reel. |
| 8 | Lens audit | PASS | body earns Descartes (what would falsify — the B08 benchtop checks: DLS >30 nm, zeta neutralization, competitive binding); Plato (artifact = the nanoparticle you engineered; world = the corona-coated particle actually delivered; relationship = "not the same thing"); light Popper (falsifiable ceiling — "no zwitterionic NP has cleared phase 2"). Three of four moves. |
| 9 | Brand fields | FIXED | Dropped ElevenLabs-era `voice_id: TyW6NH39JcFb5M3xdIIk` and top-level `voice: nbbhuman`. Added engine=kokoro, voice=am_onyx, voice_kokoro=am_onyx uniformly; persona "Liam (in for Bear)"; folderLabel + channel_title "@NikBearBrown"; variant "nbb-cli". PERSONA-COHERENCE NOTE: narration says "Nik Bear Brown" (self-intro) but voice is Kokoro Liam — the review slate cut generates in Liam per pipeline convention (VOICE-LOCK.md, all review-slate cuts). A future Bear-voice production pass would rebuild audio with generate_audio_nbb.py; the narration is unchanged (locked script). |
| 10 | Pacing | PASS | body words-per-second all within 2.0–3.4 window against measured actual_duration_s (fastest ≈ 3.0 w/s; slowest ≈ 2.6 w/s). |
| 11 | type_check.py | PASS | GATE T passed with `--skip-pixels`. B00 §8.10 advisory (narration recites card — expected for the intro); B01/BVDT §8.10 below 0.7 (well within tolerance). content_check + frame_check + lane_check all PASSED (13 beats). |

## Phase 2 — build

| Step | Result |
|---|---|
| Audio | 13 beats, kokoro am_onyx. All mp3s written. Total 240.7 s of narration. Sheet stamped with actual_duration_s per beat. |
| Remotion renders | B00 NikBearBrownOpen, B01/B06/B07/B08 FormBCard, B02/B05 NikBearBrownTerminalAsk, B03 NikBearBrownCodeBlock, B09 NikBearBrownOutro, BVDT ClaudeVerdictArtifact, BHTF ClaudeComposerAsk, BOUT ClaudeTitleOutro — 12/12 ok. |
| Manim renders | B04_ProteinCorona at 720p24 via vox_scenes.py (path patched). WARNING: 7 s of manim animation stretched 3.1× into 21.4 s beat — extreme slow-mo, flagged in replace_log.md for future replacement with a longer generation. |
| Slates | 0 declared. |
| compile.py | PASS. 13/13 filled. `protein-corona-overwrites-slate.mp4` 241.7 s. mean_volume −24.0 dB. |
| Motion warning | fade carries 9/13 beats (69%, > 40% pantry cap). Advisory only — every fade beat is a Remotion pattern with its own internal motion; the outer transition being "fade" is a compile default, not a scene design defect. |
| Gate V (frames) | PASS. 121 frames extracted at 0.5 fps + spot-check on B00 / B01 / B04 / B06 / B08 / BVDT / BHTF / BOUT full-res PNGs. Text within SAFE inset, no container overflow, no label overlap. Terracotta accent restrained (BVDT asterisk, BOUT logo mark) — one focal moment per beat. B04 Manim is sparse due to slow-mo stretch (already logged) — acceptable for review slate, not for final. |
| Audio presence | ffprobe: master carries aac audio, per-beat mp4s all carry audio EXCEPT B04 (Manim was rendered without an audio track — the compile step muxes the mp3 into the master, which is why master mean_volume −24.0 dB is correct). |
| Punt sweep post-build | PASS. build.status Counter: `{'VIDEO': 12, 'MANIM': 1}`. Zero SLATE. |

## build.status counter

`Counter({'VIDEO': 12, 'MANIM': 1})` — 13 beats total.

## Sheet changes summary

- `beat_sheet.pre-rebuild.json` created (byte-exact copy) BEFORE any edit.
- Dropped `metadata.voice_id` (ElevenLabs) and old top-level `voice: nbbhuman`.
- Added metadata: engine=kokoro, voice=am_onyx, voice_kokoro=am_onyx, persona="Liam (in for Bear)", folderLabel="@NikBearBrown", channel_title="@NikBearBrown", variant="nbb-cli".
- Stamped voice/engine on every body beat (B00-B09).
- B01: rewrote 3 FormBCard items (real label/sub/icon, from narration).
- B02/B05: rewrote greeting to 3-word cue compressed from narration.
- B06/B07/B08: upgraded from `shot.type: GRAPHIC, source: null` to real FormBCard patterns (3 items each, drawn from narration, icons within available set).
- BVDT: authored real narration (was empty); replaced 3 placeholder artifactLines with 4 real findings + real artifactTitle.
- BHTF: authored narration (was empty) — viewer-facing prompt handoff.
- BOUT: authored narration (was empty) — title restate.
- vox_scenes.py: patched path resolution to auto-discover books/vox library (was hard-coded to a non-existent parents[3]).
- No body narration_text (B01-B08) was edited — locked script preserved.

## Advisory / follow-ups (not blockers)

- B04 Manim animation is 7 s stretched to 21.4 s — production pass should regenerate B04_ProteinCorona at a duration closer to the measured audio (or loop the sequence). Logged in `replace_log.md`.
- Persona coherence: for a Bear-voiced final ship, regen audio with generate_audio_nbb.py once cluster access is available. Narration ("Nik Bear Brown") is authored for Bear; review slate uses Liam per house convention.
- fade transition histogram 69% — over the 40% pantry cap. Motion cap is a compile-side advisory; no scene-design change needed.
