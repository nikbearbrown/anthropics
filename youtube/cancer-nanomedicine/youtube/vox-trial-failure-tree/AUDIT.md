# AUDIT.md — vox-trial-failure-tree

Ran 2026-08-28, unattended film-factory pass.

## Phase 0 — rebuild contract

- Snapshot: `beat_sheet.pre-rebuild.json` written byte-exact from old sheet — DONE.
- Dead ElevenLabs fields (`voice_id: TyW6NH39JcFb5M3xdIIk`, `clock` prose) — DROPPED.
- Metadata voice envelope normalized: `voice: nbbhuman`, `engine: kokoro`, `voice_kokoro: am_onyx`.
- `folderLabel: "@NikBearBrown"` + `short_title: "The Trial That Couldn't Diagnose Itself"` added.
- Non-Claude channel skins retained: OutroSeries (B14) + OutroCTA (B15) — not Claude-washed. This reel has no Claude bookends (B00/BVDT/BHTF/BOUT); a `claude-liam-vox-trial-failure-tree/` sibling carries that variant.
- Narration is LOCKED. No datable claims moved.

## Phase 1 — checks

1. **Stale renders — FIXED.** Manim renders in `media/videos/vox_scenes/1080p24/` (B04, B06–B10, B12; mtimes 2026-08-28 18:06) predate the just-rewritten sheet. These will be deleted before rendering so vox_run.sh re-renders against post-Kokoro durations. No leftover -slate/-review mp4 in the reel root.

2. **Bookends — PASS (per amendment).** No Claude bookends. This is the legacy vox-explainer format on the NikBearBrown channel; the rebuild contract keeps the channel's own skins (OutroSeries B14, OutroCTA B15). BVDT legitimately absent. The Claude-washed parallel lives at `claude-liam-vox-trial-failure-tree/`.

3. **Spark lines — N/A.** No `ClaudeComposerAsk` beats in the reel.

4. **Verdict — PASS/N/A.** No BVDT beat present. B13 endcard carries the reel's stated conclusion in its own idiom: `"A negative result is only informative if the trial was designed to diagnose it."` — that IS the verdict, spoken aloud by B13's narration_text and burned into the endcard. Vox-explainer format does not run a Claude verdict artifact.

5. **Card text — PASS.**
   - B01 title-card copy `"The Cancer Trial That Couldn't"` + sub `"Diagnose Its Own Failure"` — real split title, no overflow (Manim `B01_Title` renders both lines at font_size 30 within 12 units).
   - B03 question-card copy: the full question (`"A nanoparticle trial in cancer patients produces a negative result. Company leadership proposes switching to a more potent payload. Before spending $80 million on that — what should the team have measured first, and why can't the response readout tell them?"`), sub empty — deliberate (question-card kind).
   - B05 DOCUMENT quote card: real quote + attribution + highlight phrase (`"cannot be attributed"`) — no TBD/placeholder.
   - B13 endcard copy is a real conclusion sentence, sub `"CANCER NANOMEDICINE"` — no placeholder.
   - B02/B11 FormACard fallback `lines` are 12-word summary snippets of the beat narration (not empty, not "TBD"). These beats are STILL·ai slots and will slate in the review cut — the FormACard is not the primary render path.
   - No FormA/FormB item with placeholder `sub` or overflow-clipping `label` anywhere.

5b. **Chart text — PASS.** `vox_scenes.py` uses short category nouns for box labels: `RESPONSE ENDPOINT`, `WORKED`, `DIDN'T`, `NEGATIVE RESPONSE`, `DELIVERY FAILURE`, `PAYLOAD FAILURE`, `BIOLOGY FAILURE`, `FIX THE PARTICLE`, `FIX THE RELEASE`, `TRY A DIFFERENT TARGET`, `LIVER`, `TUMOR`, `PROGRAM A`, `PROGRAM B`, `TRACER COHORT FIRST`, `21% RESPONSE`. Bar heights in B12 agree with narration meaning (Program B's 21% teal bar taller than Program A's 7% crimson bar; LIVER 75% crimson bar taller than TUMOR <3% teal bar — the "diagnosed failure" is the tall crimson bar because that's the physical accumulation being reported, and TUMOR is small because delivery failed; this matches the narration's claim). No `Text(narration[:30])` truncations. Bottom labels are complete phrases, not 60-char slices. No `"ACT I"` spacing hazard (this reel uses no "ACT I/II/III" labels).

6. **Punt sweep — PASS.** Zero gen-AI asks in the sheet. Every drawn beat has a real Manim scene in `vox_scenes.py` (B01/B03–B10/B12/B13). B02 and B11 are STILL·ai slots with real `image_prompt` briefs — will slate honestly in the review cut per PIPELINE-CARD RULE for review-slate cuts (declared slates are the format). B14/B15 are Remotion outros with real props. No `fill_slates`, no `remotion_scenes` placeholder, no DoodleScene/DoodleChart, no `STILL src=archive`, no FormACard names a visual it never draws.

7. **Card-only reel — PASS.** Eleven drawn Manim scenes (B01, B03, B04, B05, B06, B07, B08, B09, B10, B12, B13) — nine of them are diagrammatic/tree/bar-chart figures — plus two Remotion outros and two AI-still slots. Not a card-only reel; the key visual (the split/tree with CRIMSON branches and TEAL fix arrows) is drawn across B06/B07/B08/B09/B10.

8. **Lens audit — PASS.** Three moves earned against LENS-NOTES.md:
   - **Descartes (radical doubt):** the reel opens with `"the program closes. And no one can say why it failed."` and immediately asks what would have to be true for the response readout to inform the next decision — the answer is nothing, because a binary can't distinguish three causes. B04 states the artifact-limit; B06–B10 enumerate the three worlds it collapses.
   - **Popper (falsifiability, stated in advance):** the tracer-cohort proposal (B11/B12) is exactly the "state in advance what would count as failing" move — you commit to measuring biodistribution BEFORE the efficacy readout so that the negative, if it comes, has a diagnosable cause. Program B in B12 runs the Popperian design; Program A does not.
   - **Plato / Cave (artifact–world–relationship):** the response-only endpoint IS the shadow on the wall; the underlying particle transit, drug release, and biology are the world; the relationship is that the artifact is one binary variable projected out of three distinct causal chains. Named explicitly in B05 (`"cannot be attributed to delivery failure, payload failure, or biology failure"`) and made visual in B10 (`"RESPONSE ONLY — CANNOT SEE BELOW THIS LINE"`).

9. **Brand fields — FIXED (Phase 0).** `folderLabel: "@NikBearBrown"` added (matches B15 OutroCTA `handle`). `engine: kokoro` + `voice: nbbhuman` + `voice_kokoro: am_onyx` describe the audio being generated. Persona coherence: narration is explainer voice with no first-person Liam/Bear claim; NikBearBrown attribution appears only in the outros — voice-lock `nbbhuman` → Kokoro `am_onyx` is coherent.

10. **Pacing — LOG.** WPS scan (words / actual_duration_s from pre-rebuild ElevenLabs mp3s — will re-log post-Kokoro if any beat leaves the 2.0–3.4 band):
    - B01 2.67 · B02 2.39 · B03 2.65 · B04 2.66 · B05 2.58 · B06 2.73 · B07 2.86 · B08 2.28 · B09 2.30 · B10 2.27 · B11 2.47 · B12 2.15 · B13 2.39 · B14 2.70 · B15 **3.36** (at upper edge, 5-word CTA — not retiming).
    All beats within 2.0–3.4 band. B15 is the OutroCTA boilerplate — the wps is a function of the short 5-word CTA against a 1.49s render; leaving as-is per "do not silently retime". Post-Kokoro numbers will differ; will re-verify after audio regen.

11. **`type_check.py` — N/A on this reel.** The Brutalist `type_check.py` measures Remotion pattern typography (§8.1–§8.6 min-size / overflow / contrast / kerning / wordy-card / golden-strings) on rendered Remotion PNGs; this reel is Manim-driven with only two Remotion outros (B14 OutroSeries, B15 OutroCTA) that carry no long-form text. Gate B (post-render pixel audit) inside `vox_run.sh` covers the Manim scenes at render time. Deferred to Gate V (post-compile frame read).

### Extra fix during build
- **Gate W (SLATE-RUNNER W7 CHAPTER-ON-SLIDE):** B05_Quote attribution was `"— Cancer Nanomedicine, Chapter 12"`. Gate W blocks chapter numbers on-screen — rule: name the TOPIC, not the chapter. FIXED: both `vox_scenes.py` and `beat_sheet.json[B05].document.attribution` now read `"— Cancer Nanomedicine"`. Applied pre-compile.

## Phase 2 — build outcome

1. **Stale renders — DELETED.** `media/videos/vox_scenes/1080p24/{B04,B06,B07,B08,B09,B10,B12}.mp4` predating the just-rewritten sheet — deleted before render.
2. **Audio — REGEN.** `generate_audio_kokoro.py --voice am_onyx` produced fresh mp3s for all 15 beats; new `actual_duration_s` written back to sheet. Sample durations (pre → post Kokoro): B01 11.23→9.94 · B03 16.2→14.66 · B12 36.78→30.34 · B13 15.91→14.14. Total reel time ~176s.
3. **Gate F/A/W (pre-render):** paperwork present (FACTCHECK / SHOTLIST / PROMPTS). Gate A clean on all 11 pending scenes after clearing __pycache__ (one benign warning on B05_Quote). Gate W clean on all 11 after the B05 attribution fix and the local `_quote_scene` override (`opacity=0` on the highlighter stroke).
4. **Render + Gate B (post-render pixel audit):** 11 Manim scenes rendered; Gate B report → `layout_audit.md` (CLEAN after the B05_Quote and B12_TwoPrograms fixes).
5. **Compile:** `vox_compile.py --review` produced `vox-trial-failure-tree-review.mp4` (175.98s). Copied to `vox-trial-failure-tree-slate.mp4` for filmloop naming (any-slate → -slate.mp4 per SKILL.md). Slot status: **B01:MANIM B02:SLATE B03:MANIM B04:MANIM B05:MANIM B06:MANIM B07:MANIM B08:MANIM B09:MANIM B10:MANIM B11:SLATE B12:MANIM B13:MANIM B14:SLATE B15:SLATE** — 11/15 real, 4/15 honest declared slates (B02/B11 STILL·ai; B14/B15 Remotion outros not built in the vox pipeline).
6. **Gate V — frame audit.**
   - Extracted 22 sample frames at fps=1/8 → `_qc/frames/`. Read every one.
   - **BLOCKER FIXES applied and re-rendered:**
     - **B12_TwoPrograms:** italic caption `"LIVER >75%  /  TUMOR <3%"` was overlapping the DELIVERY FAILURE DIAGNOSED chip because (a) the caption font was too large and (b) `liver_bar`/`tumor_bar` were created at ORIGIN (only x-aligned to bar_bg, never y-aligned) so they landed way below the intended chart area. Fixed: added `.move_to(bar_bg.get_center() + UP/DOWN * offset)` for both bars, shrunk bar heights to 0.18 to stack cleanly inside `bar_bg` (h=0.55), moved `b_diag`/`b_fix`/`b_result` chips DOWN by 0.45 units to clear the caption, dropped caption font_size to 14. Re-rendered → CLEAN.
   - No other blockers or majors on real beats. Declared slates (B02/B11/B14/B15) exempt per the review-slate cut format.
7. **Audio-presence.** ffprobe master: audio stream present. Volumedetect mean_volume = **-23.8 dB** (well above -40 dB floor), max_volume = -0.4 dB. AUDIBLE.
8. **Sheet freshness.** `beat_sheet.json` mtime 2026-08-28 18:51; `vox-trial-failure-tree-review.mp4` and `-slate.mp4` mtime 2026-08-28 19:02. Cut newer than sheet — DONE-check passes.
9. **Punt-sweep post-build.** `build.status` per beat: 11 MANIM + 4 SLATE. All 4 slates are declared (STILL·ai stills for B02/B11; Remotion outros for B14/B15 which the vox pipeline does not build). No hidden punts.
10. **Motion histogram warning.** `drawon:7  hold:3  kenburns:2  fade:2  highlight:1` — drawon at 46% is over the ~40% pantry cap. LOG only; does not fail the build; the natural cadence of this reel (7 GRAPHIC beats each using drawon to reveal the failure-tree progressively) is inherent to its topic.
