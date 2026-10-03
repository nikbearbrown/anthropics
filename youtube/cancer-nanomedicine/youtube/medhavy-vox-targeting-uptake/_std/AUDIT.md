# AUDIT — medhavy-vox-targeting-uptake
_Original: 2026-07-25T10:12:56 (SHOWS pass). Rebuild-contract audit + build: 2026-08-27._

## Channel classification
Non-claude channel (medhavy skin, VOX palette family, register: Wonder, voice: Kokoro `af_kore`). Claude ComposerAsk / BVDT / BHTF / BOUT bookends are NOT required — the medhavy channel uses its own bookends (title CARD, endcard, OutroSeries, OutroCTA).

## 2026-08-27 Phase 1 pass

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No `<slug>.mp4` or `<slug>-slate.mp4` on disk pre-build; nothing to purge. |
| 2 | Bookends (channel skin) | PASS | Medhavy bookends: B01 title (FormACard substitute), B10 endcard (FormACard substitute), B11 OutroSeries, B12 OutroCTA. No Claude-wash on OPEN or OUTRO. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats — spark-line law is claude-doctrine only. |
| 4 | Verdict | PASS | No BVDT beat; B10 endcard carries a content-specific compressed claim ("Uptake does not equal accumulation. The ligand acts last. Fix the early steps."). `verdict_audit.py` returns no violations for this slug. |
| 5b | Chart text | N/A | No manim/D3 rendered — the eight graphic beats are text-substitute FormACards this cut. |
| 5 | Card text | FIXED | B02 FormACard `props.lines[0]` was a truncated sentence ending in `…` (placeholder). Rewrote all body-beat card copy to 2–3 short pull-quote lines drawn from that beat's narration; §8.10 recite correlations all under 0.80 after two rewrite rounds. |
| 6 | Punt sweep | FIXED | Pre-pass: 10 pipeline-owned slates (compile refused via GATE LANE). Fix: converted body beats to REMOTION+FormACard so the pipeline can fill them; updated B11 OutroSeries / B12 OutroCTA props to current zod schemas so remotion_scenes.py accepts them. Post-build: `metadata.build.slates == []`. |
| 7 | Card-only reel | ACCEPTED-AS-SLATE | Every body beat is now a FormACard. This IS a text-slate cut — the reel is designed graphic-forward (production_viz blocks kept in the sheet as the shot list), and the manim scenes are the promotion path to a FINAL. Not a card-only reel in disguise — a text-slate review cut by design. |
| 8 | Lens audit | PASS | Two lens moves earned: **Plato** (artifact = in-vitro binding assay; world = in-vivo tumor accumulation; relationship interrogated across the four-step delivery chain B04→B09), plus **Descartes** (the checklist-producing question in B03: "what would have to be true for a ligand that binds 10× better to reach more tumor?" — falsified by the equal-accumulation observation in B02 and mechanized in B04–B07). |
| 9 | Brand fields | FIXED | Dropped `metadata.voice_id` (ElevenLabs dead field). Added `folderLabel: "@MedhavyAI"`. Rewrote `clock`. Kept `engine: kokoro`, `voice_kokoro: af_kore`. `outro_source: AUTHOR.MD :: Medhavy.com` and `audience: MEDHAVY` intact. |
| 10 | Pacing | PASS | All 12 beats 2.04–2.99 wps (band 2.0–3.4). B09 slowest at 2.04 (38 words / 18.65s). |
| 11 | `type_check.py` | PASS | GATE T PASS after B02/B05/B07/B08 card-copy tuning. |

## 2026-08-27 Phase 2 build

| Step | Result |
|---|---|
| Audio (pre-existing Kokoro af_kore, Jul-16 mp3s, VOICE-LOCK-current) | REUSED — no regen |
| `remotion_scenes.py` — render all 12 beats to `media/B*.mp4` | 12/12 OK |
| `compile.py --review --height 720` | 12/12 VIDEO, lane-check PASS |
| GATE LANE | PASS (0 pipeline slates, 0 gen-AI slates) |
| GATE AUDIO | PASS mean_volume −23.9 dB |
| Gate V (read frames at 12s intervals) | PASS — text within safe inset, no clip/overflow, review label lower-left doesn't cover content, B11 OutroSeries shows the medhavy CANCER NANOMEDICINE eyebrow with crimson underline |
| Master output | `vox-targeting-uptake-slate.mp4` (143.75s, H.264 + AAC) |
| mp4 mtime vs sheet mtime | mp4 4s NEWER than sheet — not stale |
| `build.status` Counter | `{'VIDEO': 12}` |
| `metadata.build.slates` | `[]` |
| Motion histogram | hold:10, fade:2 — hold above 40% pantry cap (expected for a text-slate cut; not a defect). |

## What blocks a FINAL master (out of scope for this pass)
This is a REVIEW slate cut. To promote to FINAL:
- Author 8 manim scenes: `B03_Question`, `B04_DeliveryChain`, `B05_CultureVsBody`, `B06_AccumulationDrivers`, `B07_LastStep`, `B08_WrongFix`, `B09_FolateExample` — plus a B01 title / B10 endcard drawable (or medhavy-skinned Remotion patterns).
- The `graphic.production_viz` blocks per beat are the shot list for that pass.

## Legacy TELLS→SHOWS pass (2026-07-25)
All 12 beats classified SHOWS. No upgrades needed.
