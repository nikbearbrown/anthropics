# AUDIT — claude-liam-vox-targeting-uptake

Date: 2026-08-28

## PHASE 0 — pre-rebuild snapshot
- `beat_sheet.pre-rebuild.json` created (byte-exact copy of the Jul-16-era sheet).

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No mp4s in reel folder; `media/` doesn't exist. Old `mp3/*.mp3` (Jul 16) are stale versus the new sheet — will be regenerated in Phase 2. |
| 2 | Bookends | FIXED | B00 ClaudeComposerAsk kept (with new greeting). BVDT `ClaudeVerdictArtifact` authored (was placeholder). BHTF `ClaudeComposerAsk` narration authored (was empty). BOUT `ClaudeTitleOutro` unchanged. Legacy B11 `OutroSeries` + B12 `OutroCTA` DROPPED — Claude closing block (BVDT → BHTF → BOUT) is the doctrine and the reel had no rendered B11/B12 mp4s. |
| 3 | Spark lines | FIXED | B00 greeting was `"Liam"` (missing world-language hello) → `"Ni hao, Liam."` — unused among adjacent claude-liam-* reels in this book. BHTF greeting = `"Your turn."` ✓. No inner-body ClaudeComposerAsk beats. |
| 4 | Verdict | FIXED (AUTHORED) | Body = 10 beats, ≈ 350 words → authored real verdict from body's own nouns (10× dish binding, delivery chain, step 4, circulation half-life, vessel permeability). Rewrote BVDT narration to state the verdict aloud. BVDT `artifactLines` are three specific claims — not placeholders, not generic. |
| 5b | Chart text | N/A | No Manim/D3 chart rendered here — every body beat routes to a Remotion `FormBCard` or `FormACard` whose labels are short category nouns and subs are complete phrases. B09's illustrative bar-chart intent is preserved as a labeled `FormBCard` (`illustrative` marked in each sub). |
| 5 | Card text | FIXED | B01 placeholders (`"Key point one/two/three"` + empty subs) rewritten from B01 narration. Every body beat now has real `label`+`sub` copy authored from its own narration. |
| 6 | Punt sweep | FIXED | Removed every `SLATE` with `source:null` + `"YOU → 5–10s gen-AI clip"` needs string. B02 (was STILL/ai gen-AI ask) rerouted to `FormBCard`. B03–B10 (were `GRAPHIC` pointing at Manim scenes that don't exist in this reel) rerouted to `FormBCard`/`FormACard`. Zero gen-AI asks; zero unfilled slates; zero DoodleScene/DoodleChart; zero `STILL src=archive`. |
| 7 | Card-only | ACCEPTED (review-slate cut) | All body beats are Remotion cards (`FormBCard`, `FormACard`). This is a REVIEW SLATE cut per the pipeline — declared cards are the format. B04 (delivery chain, 4 items) and B09 (illustrative bar comparison) carry the drawn-figure INTENT via structured multi-item cards. When Manim is later authored for `B04_DeliveryChain` and `B09_FolateExample`, the reel re-routes at that time — the pre-rebuild sheet keeps the manim scene refs. |
| 8 | Lens audit | PASS | Four moves earned: **Descartes** — B03 poses the falsifier as a question ("The ligand is working. Why doesn't it help?"). **Hume** — B05 flags that a plate-assay's confidence is a property of the assay, not of the animal (culture removes circulation/vessels/clearance). **Popper** — B09 states in advance what would count as the ligand failing to move accumulation (equal accumulation, different uptake). **Plato** — B01/B02 name the artifact (10× binding in a dish), the world (tumor delivery in vivo), and the relationship (they don't track). |
| 9 | Brand fields | FIXED | Dropped dead ElevenLabs fields (`voice_id`, `voice_env`, `clock`). Dropped stale `.build` metadata block and `_variant_todo` remnant. Kept `engine: kokoro`, `voice_kokoro: am_onyx` at metadata level and on every beat. `folderLabel: "@NikBearBrown"` ✓ (was already correct). Narration "This is Liam, in for Bear" is consistent with `am_onyx` (Liam-Claude voice). |
| 10 | Pacing | LOGGED | Word/sec vs `estimated_duration_s`: B01 37w/12s = 3.1, B02 30w/10s = 3.0, B03 27w/10s = 2.7, B04 34w/11s = 3.1, B05 37w/11s = 3.4, B06 30w/11s = 2.7, B07 27w/10s = 2.7, B08 30w/10s = 3.0, B09 32w/15s = 2.1, B10 32w/11s = 2.9, BVDT 75w/28s = 2.7, BHTF 38w/14s = 2.7. All inside the 2.0–3.4 window. |
| 11 | type_check.py | (run at build time; results in `TYPECHECK.md`) | |

## Datable-claim edits
- None. Narration contains no model names, versions, prices, or "as of" phrasing. B09 "2.1% / 1.9% / 68% / 12%" are illustrative teaching numbers (per the pre-rebuild `production_viz.note`: "illustrative numbers per card — must be labeled ILLUSTRATIVE in FACTCHECK"), preserved as-is and labeled `illustrative` in the card subs.

## Structural changes (LOCKED-body-preserving)
- B11 (`OutroSeries` — "Part of the Cancer Nanomedicine series.") dropped. The Claude closing block (BVDT → BHTF → BOUT) supersedes the legacy series-outro pair. Old B11 mp4 does not exist on disk.
- B12 (`OutroCTA` — "Like and subscribe for more.") dropped for the same reason.
- Narration for B01–B10 is UNCHANGED (verbatim from the pre-rebuild sheet).

## Blocked?
No. All checks either FIXED or PASS. Proceeding to PHASE 2.
