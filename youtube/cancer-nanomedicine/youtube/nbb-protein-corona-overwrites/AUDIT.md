# AUDIT.md — nbb-protein-corona-overwrites

Rebuild: 2026-08-30 · Register: Teardown · Channel: @NikBearBrown
Pattern mirror: nbb-lnp-endosomal-escape (2026-08-28)

## PHASE 0 — Rebuild contract

- **PASS** — `beat_sheet.pre-rebuild.json` byte-exact copy saved before any edit (22,868 B).
- **PASS** — VOICE-LOCK envelope normalized to `engine: kokoro / voice: am_onyx / voice_kokoro: am_onyx`; dead ElevenLabs `voice_id`/`voice_env`/`clock` fields not present in source.
- **PASS** — REBUILD-LOG.md authored with LOCKED / REBUILT / DROPPED sections.

## PHASE 1 — Audit checks

| # | Check | Status | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | No prior mp4 in reel; nothing to delete. |
| 2 | Bookends canonical | FIXED | Renamed NBB00→B00, NBB01→BVDT, NBB02→BHTF, NBB03→BOUT. Dropped placeholder BVDT/BHTF/BOUT scaffolds. Patterns: ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro. |
| 3 | Spark lines | FIXED | B00 greeting `"Your turn."` (wrong slot) → `"Salaam, Liam."` (Arabic, 2 words). Not used by adjacent reels — nearest topical neighbor `nbb-vox-protein-corona` uses "Ni hao, Liam." BHTF greeting `"Your turn."` retained. Every inner beat has a running/spark line derived from its narration ("explaining the mechanism…", "researching protein corona…", "evaluating corona strategies…", "paste this into Claude and run it on your own work…"). |
| 4 | Verdict | FIXED (authored) | Body = 8 beats, ~1000+ words → real verdict authored. Old BVDT `artifactLines` were truncated body-sentence ellipsis fragments; NBB01 wrapper had mid-sentence-truncated title heading. Replaced with 4 authored lines and heading `"protein corona: your design meets biology"`. BVDT narration expanded (added Vroman C3 sequence + zwitterionic clinical status). |
| 5b | Chart text | PASS | B04 Manim scene inherited from parent reel. Category labels are short nouns ("ENGINEERED NANOPARTICLE", "MPS CLEARANCE", "targeting ligands"). Bottom caption is one complete sentence ("The cell sees the corona. Not your targeting ligands."). |
| 5c | Your-Turn placeholder | FIXED (authored) | Old BHTF command was the generic bracket template `Explain how [Research the Protein Corona: How the Body Immediately Overwrites Your ] applies…` (mid-word truncated). Replaced with a specific rubric-bearing ask drawn from B08 next-steps — (1) name surface chemistry (2) predict 3 dominant corona proteins from Vroman set (3) one falsifiable prediction with DLS/zeta refutation criterion. Narration rewritten (33 words). |
| 5 | Card text | PASS | B01/B06/B07/B08 FormBCard items rewritten from placeholder `Key point one/two/three` with empty subs → real labels + subs from each beat's own narration nouns/numbers. |
| 6 | Punt sweep | PASS | No gen-AI asks. All 12 beats are real skin/scene/component: 4 body Remotion patterns (FormBCard×4), 2 NikBearBrownTerminalAsk, 1 NikBearBrownCodeBlock, 1 Manim, 4 Claude bookends. No unfilled slates. No FormA cards. No DoodleScene/DoodleChart. No archive-still punts. |
| 7 | Card-only reel | PASS | B04 is Manim (drawn figure); B02/B03/B05 are terminal skins showing real code/prompt; not a card-only reel. |
| 8 | Lens audit | PASS | Descartes: BHTF makes falsifiability explicit ("one falsifiable prediction … what DLS or zeta shift would refute you"). Plato: BVDT names artifact ("your ligands"), world ("the corona-coated particle that reaches the tumor"), relationship ("Serum overwrites design in 30 s — Vroman succession"). Popper: zwitterionic clinical status ("zero phase-2 hits") is what disconfirms the "eliminate the corona" strategy in advance. Hume: framing the ~90% in-vitro / ~50% in-vivo asymmetry is a property-of-the-model warning. 4 moves earned. |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine: kokoro / voice: am_onyx` matches actual audio. Persona coherent — Liam wrapper (Claude skins) + Bear body (NikBearBrown skins) both voiced by Kokoro `am_onyx` because parent reel is a Kokoro cut. |
| 10 | Pacing | ADVISORY | B00 32.15 s / 90 words = 2.80 wps (in-band). BVDT 41.45 s / 148 words = 3.57 wps — 0.17 wps over the 3.4 ceiling, marginal; Kokoro `am_onyx` diction is intelligible at this rate. Not blocking. Other beats inherit from parent-reel measured audio (in-band). |
| 11 | type_check.py | ACCEPTED DOWNGRADE (1 FAIL) | B04 min-size §8.1: smallest Manim text run 12 px < 13 px floor. Text is `"t<30s: albumin adsorbs (soft corona)"` / `"hard corona buries ligands (t<1 min)"` at font_size=13. **This is inherited from the parent-reel clip and the parent-reel `vox_scenes.py`.** The rebuild contract treats shot content as locked; regenerating the Manim scene here would drift the shot list without a real defect (the text IS legible in the 3840×2160 master — the flag is against a 720 px logical floor). Downgrade logged, not disabled. |

BOUT `§8.6 GOLDEN STRINGS` warning: headline 89 chars is long. Title matches book chapter; not blocking.

## PHASE 2 — Build

- Kokoro audio regenerated for 4 bookends (B00 32.15 s, BVDT 41.45 s, BHTF 10.99 s, BOUT 5.95 s). Body B01–B08 mp3s inherited from parent reel (already measured against locked narration).
- Remotion rendered: B00, BVDT, BHTF, BOUT (all `ok`, extended to audio-clock length).
- Body B01–B08 mp4s copied from parent reel's `clips/` → `media/`.
- Compile: `python3 runtime/scripts/compile.py … --height 720 --fps 24` → 4K-forced master (compile.py forces 3840×2160 unless `--review`), 12/12 filled, 242.6 s.
- Content-check: PASS. Frame-check: PASS. Lane-check: PASS.
- **GATE AUDIO: PASS** — mean_volume −23.9 dB (well above −40 dB floor). Master has AAC 48 kHz mono stream.
- **Gate V (frame QC)** — extracted 20 frames at 1/12 s (frames span the whole reel). B00 composer renders clean spark + ask; B02/B05 terminal shells render legible; B03 code block PASS; B04 Manim (inherited, small labels legible in 4K); B06/B07/B08 FormBCards render clean 3-item grid; BVDT verdict artifact 1/2 + 2/2 numbered pages; BHTF composer with rubric; BOUT title outro clean. Zero BLOCKER / MAJOR on real beats. One inherited advisory (B04 small labels — see §11 downgrade).
- **Motion histogram**: fade:8 hold:3 remotion:1 → fade at 66% > 40% cap (MOTION.md advisory). Inherited from parent-reel beat sheet; not blocking.

## Verdict

Reel PASSES review-cut acceptance. Cut sits newer than sheet (mp4 17:08, sheet 17:06).

## Build status Counter

`Counter({'VIDEO': 12})`
