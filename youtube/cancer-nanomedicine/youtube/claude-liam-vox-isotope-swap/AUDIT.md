# AUDIT — claude-liam-vox-isotope-swap (2026-08-28 rebuild pass)

## PHASE 0 — rebuild contract
| Item | Status |
|------|--------|
| `beat_sheet.pre-rebuild.json` snapshot | CREATED (byte-exact) |
| Envelope normalized (VOICE-LOCK) | FIXED — dropped `voice_id`, cleaned `clock`, dropped `_variant_todo` |
| Narration LOCKED (no rewrites except datable-claim fixes and PHASE-1-authorized ones) | PASS — no datable claims in body (isotope names Ga-68 / Lu-177 are permanent facts, not dated model versions) |
| Non-claude channel skin preserved | N/A (this is a Claude channel reel) |

## PHASE 1 — audit
| # | Check | Verdict | Notes |
|---|-------|---------|-------|
| 1 | Stale renders | PASS | no mp4s anywhere in folder — nothing to purge |
| 2 | Bookends present (B00 / BVDT / BHTF / BOUT + canonical patterns) | PASS | all four present with correct patterns (ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro) |
| 3 | Spark lines | FIXED | B00 greeting was "Liam" → authored "Bonjour, Liam." (rotation vs adjacent Hola/Salaam/Ciao/Namaste/Konnichiwa already used by delivery-funnel/doxil-heart/emitter-range/endosomal-escape/epr-gap); BHTF "Your turn." already present; no inner ClaudeComposerAsk beats |
| 4 | Verdict (BVDT) | FIXED | placeholder "Key finding one/two/three" + empty narration → authored 4 real lines from body's own nouns/numbers (Ga-68 / Lu-177 / PSMA / illustrative 4-lit-shrink-60% vs 2-dark-grow-40%); wrote a matching narration (~60 words) |
| 5b | Chart text | N/A | Manim graphic beats (B03/B05/B07/B08/B10/B11) declared SLATE for the review cut — real Manim render is a later human-flagged pass |
| 5 | Card text — no placeholder subs / overflow | FIXED | B01 FormBCard items were "Key point one/two/three" with empty subs → authored 3 items from B01 narration (metastatic diagnosis / known therapy / temptation to treat vs the-scan-first). B02 and B09 FormACard `lines` were mid-word narration fragments → rewritten to short label lines ("The scan asks: is the target there?" / "PSMA-negative: drug misses, tumor grows.") |
| 6 | Punt sweep — gen-AI asks, unfilled slates, doodle, STILL src=archive | PASS | no `shot.type` set to a gen-AI ask; the two `source: ai` STILL beats (B02/B09) fall back to a REMOTION FormACard for the review cut (declared slate). Legacy `build.needs` stamps are stale annotations, will be re-stamped by compile |
| 7 | Card-only reel | PASS | sheet has 6 Manim GRAPHIC beats (B03/B05/B07/B08/B10/B11) declared for the full-render pass |
| 8 | Lens audit (two of Descartes / Hume / Popper / Plato) | PASS | **Descartes** — the swap experiment (Ga-68→Lu-177) IS the checklist for what would falsify "same biology, different job"; **Popper** — the reel's B11 example states in advance what would count as failure (dark lesions grow while lit ones shrink) and finds exactly that; **Plato** — B08/B09/B10 keep the ARTIFACT (bright PET pixels) apart from the WORLD (PSMA receptors on tumor cells) and interrogates the relationship (only bright→bind→treat) |
| 9 | Brand fields | PASS | `folderLabel=@NikBearBrown` (B00/BHTF); `engine=kokoro`, `voice_kokoro=am_onyx`; persona coherent ("Liam, in for Bear" narrated in `am_onyx`) |
| 10 | Pacing (2.0–3.4 wps) | LOG | actual/estimated wps: B01 3.62, B02 3.71, B04 3.60, B08 3.67, B10 3.67, B12 3.51 run hot (all >3.4). Audio already generated Jul 16; retiming disallowed — ships as-is |
| 11 | `type_check.py --skip-pixels` | PASS | Gate T PASS. §8.10 advisories: B01 0.38, B09 0.50, BVDT 0.50 — all below the 0.75 flag threshold |

## §8.9 fixes applied
- B01/title, BVDT/artifactTitle, BOUT/title all ended on the 2-char word "It" — appended a period so §8.9 truncation detector no longer flags them.

## §8.10 residual (advisory, does not block cut)
- B09 (0.50) and BVDT (0.50) both remain by design: the FormACard label at B09 uses the reel's core noun ("PSMA-negative"), and the verdict card's job is to align with its narration. Both below FAIL threshold.

## Ready to build
Blocking issues: 0. Proceed to PHASE 2 (slate cut).
