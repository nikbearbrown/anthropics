# REBUILD-LOG — nbb-vox-doxil-heart

Date: 2026-08-28. Snapshot before edits: `beat_sheet.pre-rebuild.json` (25,568 bytes, byte-exact).

## Sheet structure

**Before** — 19 beats, two overlapping bookend sets:
- `B00` (empty scaffold, ClaudeComposerAsk, `greeting: "Liam"`) — bookend
- `NBB00` (real cold-open Liam intro, ClaudeComposerAsk) — bookend
- `B01..B12` — body (audio pointing at ElevenLabs source `../vox-doxil-heart/mp3/`)
- `NBB01` (verdict, ClaudeVerdictArtifact) — bookend
- `NBB02` (your-turn handoff, ClaudeComposerAsk) — bookend
- `NBB03` (title outro, ClaudeTitleOutro) — bookend
- `BVDT` (empty scaffold, placeholder `Key finding one/two/three`) — bookend
- `BHTF` (empty scaffold, ClaudeComposerAsk) — bookend
- `BOUT` (empty scaffold, ClaudeTitleOutro) — bookend

**After** — 16 beats, canonical ID scheme:
- `B00` = former NBB00 (Liam cold open)
- `B01..B12` = body (fresh Kokoro am_onyx audio locally in `mp3/`)
- `BVDT` = former NBB01 (verdict), with authored 4-line verdict + rewritten narration
- `BHTF` = former NBB02 (your-turn handoff)
- `BOUT` = former NBB03 (title outro)

Empty scaffold beats (`B00-old`, `BVDT-old`, `BHTF-old`, `BOUT-old`) dropped as redundant.

## Envelope

Dropped from all `ClaudeComposerAsk` props:
- `modelLabel: "Fable 5"`  (stale — Remotion component defaults still render one, cosmetic-only)
- `effortLabel: "High"`     (same)

Normalised `segment` on B00 and BHTF from mid-word truncation (`"Doxil's Real Job Isn't Hitting the"`) to a short semantic subtitle (`"doxil · cardiac protection is the win"`).

Normalised `metadata`:
- Added `voice_kokoro: "am_onyx"` (was `voice: "am_onyx"` at metadata level; kokoro loader reads `voice_kokoro`)
- Dropped stale `body_duration_s: 188.547` and `total_estimated_duration_seconds`
- Added `rebuild_at: "2026-08-28"`

## Narration edits (LOCKED except for datable-claim / verdict-authoring exceptions)

| Beat | Old | New | Reason |
|---|---|---|---|
| B00 | (from NBB00, verbatim) | (unchanged) | narration locked; renamed from NBB00 to B00 |
| B01..B12 | (from source, verbatim) | (unchanged) | narration locked from `../vox-doxil-heart/beat_sheet.json` |
| BVDT | "Let's recap with Claude. Here's what the body just demonstrated. This is the distinction that gets lost. Teams learn about EPR — the way nanoparticles leak into tumors through abnormally porous vessels. They reach for a PEGylated liposome to load the tumor. But Doxil's win was never primarily about the tumor. It was about what never reached the heart. Confusing these two leads to bad decisions. A team with a drug that has no cardiac toxicity, but a solvent problem — they copied Doxil's approach. They built a PEGylated liposome. A year later, nothing. Because the problem they had wasn't the problem Doxil solves." | "The verdict. Doxorubicin's real dose ceiling is not tumor response — it is cumulative cardiac injury near 360 milligrams per square meter. Doxil seals the drug inside a PEGylated liposome, so the heart's tight microvasculature never lets it out. Cardiac tissue drug levels fall, and that is Doxil's best-documented clinical win. The EPR tumor-loading story was background — the cardiac protection is the mechanism." | old narration recited body verbatim; new says the verdict aloud, matched to the four authored artifact lines. Source: body beats B04/B05 (cardiac dose ceiling), B06/B07 (liposome + cardiac vessels), B08 (cardiac drug levels fall), B09 (EPR misread). |
| BHTF | (from NBB02, verbatim) | (unchanged) | narration locked; renamed from NBB02 to BHTF |
| BOUT | (from NBB03, verbatim: the title) | (unchanged) | narration locked; renamed from NBB03 to BOUT |

## Verdict authored (BVDT `artifactLines`)

Old (narration fragments):
1. "Doxil's answer: seal the drug inside a PEGylated liposome."
2. "The sealed particle circulates."
3. "This is the distinction that gets lost."
4. "Confusing these two leads to bad decisions."

New (drawn from body nouns/numbers):
1. "Doxorubicin's real dose ceiling is cardiac injury near 360 mg/m²." — from B05
2. "A PEGylated liposome seals the drug through the heart's tight vessels." — from B06 + B07
3. "Cardiac tissue drug levels fall — the clinical win." — from B08
4. "EPR tumor loading was the misread; cardiac protection is the mechanism." — from B09

`artifactHeading` changed from "Doxil's Real Job Isn't Hitting the Tumor —" (title fragment) to "doxil's win: less drug to the heart, not more to the tumor".

## B01 title-card items authored

Old:
- `Key point one` / (empty sub) / icon `target`
- `Key point two` / (empty sub) / icon `list-checks`
- `Key point three` / (empty sub) / icon `zap`

New (drawn from B01 narration):
- `Most famous cancer nanoparticle` / `celebrated for decades`
- `Approved 1995` / `ovarian cancer, then more`
- `Its best benefit isn't obvious` / `the win is the heart, not the tumor`

## Body-beat shot reshape (locked shot list preserved verbatim in `graphic.production_viz`)

For the review-slate cut only, the following beats' `shot.remotion` was reshaped from the intended Manim/COMPOSITE/DOCUMENT scene to a one-line `FormACard` naming the visual mechanic:

| Beat | Locked visual (preserved in `production_viz`) | Review-slate card line |
|---|---|---|
| B02 | STILL·ai — oncologist reviewing cumulative dose chart | "Standard doxorubicin — potent against ovarian cancer, quietly damages the heart." |
| B03 | CARD question | "Doxil was approved for tumor delivery — but the trial win was cardiac protection." |
| B04 | Manim `B04_DoxDistrib` — drug fans to tumor + heart | "Free doxorubicin fans to both tumor cells and cardiac muscle." |
| B05 | Manim `B05_DoseMeter` — cumulative bar to 360 mg/m² | "Cumulative cardiac dose near 360 mg/m² — the cap is the heart, not the tumor." |
| B06 | STILL·ai — PEGylated liposome cross-section | "Doxil seals the drug inside a PEGylated liposome — locked during circulation." |
| B07 | Manim `B07_HeartSpared` — particle through vessel, heart stays teal | "Tight cardiac vessels never let the particle open — the heart is spared." |
| B08 | DOCUMENT quote — gold highlighter on "less drug reaches the heart" | "Less drug reaches the heart — Doxil's best-documented clinical result." |
| B09 | Manim `B09_MisreadingDoxil` — EPR vs cardiac two-column | "EPR tumor loading is the misread — cardiac protection is Doxil's actual win." |
| B10 | Manim `B10_WrongTool` — mismatch between drug problem and Doxil solution | "Wrong tool for the wrong problem — a solvent issue is not a heart issue." |
| B11 | Manim `B11_Example` — Patient A vs Patient B illustrative bars | "Same dose, same tumor response — ~40% less drug to the heart with Doxil." |

B12 (endcard) kept as declared `type: CARD` slate — legit for a review-slate cut. Endcard content preserved: "Doxil's win: less drug to the heart — not more to the tumor."

## Audio

Regenerated all 16 mp3s fresh via Kokoro am_onyx (`generate_audio_kokoro.py`). ElevenLabs-era source mp3s at `../vox-doxil-heart/mp3/` (voice_id `TyW6NH39JcFb5M3xdIIk`) are NOT used — VOICE-LOCK bans ElevenLabs. New `actual_duration_s` values stamped back from ffprobe measurement (233 s total, matching the master).

The old `NBB03` mp3 was silent (−91 dB) — regenerated as `BOUT.mp3` (title read; 4.2 s).

## Datable claims

None. The source narration cites the 360 mg/m² threshold (verified in `../vox-doxil-heart/FACTCHECK.md`) and describes doxorubicin's mechanism — no model names, versions, or dated prices.
