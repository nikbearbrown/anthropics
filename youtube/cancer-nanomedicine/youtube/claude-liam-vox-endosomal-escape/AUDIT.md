# AUDIT — claude-liam-vox-endosomal-escape (2026-08-27 rebuild pass)

## PHASE 0 — rebuild contract
| Item | Status |
|------|--------|
| `beat_sheet.pre-rebuild.json` snapshot | CREATED (byte-exact) |
| Envelope normalized (VOICE-LOCK) | FIXED — dropped `voice_id`, cleaned `clock`, dropped `_variant_todo` |
| Narration LOCKED (no rewrites except datable-claim fixes and PHASE-1-authorized ones) | PASS — no datable claims in body |
| Non-claude channel skin preserved | N/A (this is a Claude channel reel) |

## PHASE 1 — audit
| # | Check | Verdict | Notes |
|---|-------|---------|-------|
| 1 | Stale renders | PASS | no mp4s in folder (nothing to purge) |
| 2 | Bookends present (B00 / BVDT / BHTF / BOUT + canonical patterns) | PASS | all four present with correct patterns |
| 3 | Spark lines | FIXED | B00 greeting was "Liam" → authored "Namaste, Liam." (rotation vs adjacent Salaam/Ciao/Konnichiwa); BHTF "Your turn." already present; no inner ClaudeComposerAsk beats |
| 4 | Verdict (BVDT) | FIXED | placeholder "Key finding one/two/three" + empty narration → authored 4 real lines from body nouns/numbers (1–2% escape, 7.4→5.5 pH, bilayer tear, 8% vs 84% swap-experiment); wrote a matching narration (~55 words) |
| 5b | Chart text | N/A | no Manim charts render in this slate cut (B04–B09 are declared slates) |
| 5 | Card text — no placeholder subs / overflow | FIXED | B01 FormBCard items were "Key point one/two/three" with empty subs → authored 3 items from B01 narration (dish 90% / mouse nothing / paradox) |
| 6 | Punt sweep — gen-AI asks, unfilled slates, doodle, STILL src=archive | PASS | every beat has a real shot pattern; legacy `build.needs` stamps are stale annotations, will be re-stamped by compile |
| 7 | Card-only reel | PASS | sheet has 6 Manim GRAPHIC beats (B04–B09) declared for the full-render pass |
| 8 | Lens audit (two of Descartes / Hume / Popper / Plato) | PASS | **Plato** — dish=artifact vs mouse=world at B01/B02; **Popper** — swap experiment at B09 (LNP-A vs LNP-B, same cargo, only variable = the ionizable lipid; null falsified 84% vs 8%) |
| 9 | Brand fields | PASS | `folderLabel=@NikBearBrown`; `engine=kokoro`, `voice_kokoro=am_onyx`; persona coherent ("Liam, in for Bear" narrated in `am_onyx`) |
| 10 | Pacing (2.0–3.4 wps) | LOG | B01 3.78 wps and B04 3.62 wps run hot; audio already generated, ships as-is |
| 11 | `type_check.py --skip-pixels` | PASS | Gate T PASS; two advisory §8.10 warnings (B02 recite → fixed; BVDT 0.84 is expected for a verdict beat) |

## Additional advisory §8.10 after fix
- B02: FormACard `lines` was verbatim narration fragment ("The team spent months looking for a better target. But they…") → rewritten to the summary label "The wrong failure diagnosed". No longer flagged.
- BVDT: 0.84 similarity remains — the verdict card and its narration are the reel's payload and are meant to align; below the FAIL threshold and expected for the pattern.

## Ready to build
Blocking issues: 0. Proceed to PHASE 2 (slate cut).
