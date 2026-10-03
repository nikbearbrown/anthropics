# AUDIT — claude-liam-epr-delivery-funnel

Date: 2026-08-27

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No mp4s in reel folder; nothing to purge. |
| 2 | Bookends | FIXED | B00 kept as NikBearBrownOpen (channel skin — rebuild contract §non-claude channels). BVDT authored (was placeholder). BHTF narration authored (was empty). BOUT unchanged. |
| 3 | Spark lines | PASS | B00 uses NikBearBrownOpen (has `topic`+`lines`, not `greeting` — not a ClaudeComposerAsk). BHTF greeting = "Your turn." B02/B05 use NikBearBrownTerminalAsk with greeting="The ask,"—no lonely asterisks. |
| 4 | Verdict | FIXED (AUTHORED) | Body >8 beats, >380 words → authored real verdict + rewrote BVDT narration. Three lines carry nouns and numbers from the body (0.7%, Wilhelm 2016 n=117 IQR 0.3–1.4%, Doxil cardiotoxicity, Abraxane SPARC/gp60, IFP + protein corona). |
| 5b | Chart text | N/A | No Manim/D3 chart in this rebuild — B04 routed to FormBCard (funnel-attrition table). |
| 5 | Card text | FIXED | B01 placeholder ("Key point one/two/three", empty subs) rewritten. B04/B06/B07/B08 authored FormBCards with real labels + subs from each beat's narration. |
| 6 | Punt sweep | FIXED | Removed every `SLATE` with `source:null` + "YOU → 5–10s gen-AI clip" needs string. Every body beat now maps to a Remotion pattern. |
| 7 | Card-only | LOGGED (accepted) | No vox_scenes.py in reel folder → all body beats are cards. B04's five-stage funnel-attrition table IS the drawn figure (numeric stages, crimson at the bottom-row semantic). If Manim is later restored, B04 re-routes to `B04_DeliveryFunnel`. See REBUILD-LOG.md. |
| 8 | Lens audit | PASS | Four moves earned. Descartes: the 0.7% is exactly the number that would falsify EPR-as-clinical-driver, and the reel names it. Hume: model confidence (mouse EPR) is not world confidence (human tumors). Popper: Wilhelm 2016 is the falsifying test the field had never organized. Plato: EPR-in-mice is the artifact; human tumor delivery is the world; the "clinical wins traced to non-EPR mechanisms" is the relationship. |
| 9 | Brand fields | FIXED | Dropped dead ElevenLabs `voice_id`. Dropped metadata `voice: "nbbhuman"` (inconsistent with Liam narration). Kept `engine: kokoro`, `voice_kokoro: am_onyx`. Per-beat voice/engine set. folderLabel `@NikBearBrown` ✓. |
| 10 | Pacing | LOGGED | Estimated word/sec vs estimated_duration_s: B01 66w/22s = 3.0, B03 46w/17s = 2.7, B04 68w/22s = 3.1, B05 47w/17s = 2.8, B06 54w/23s = 2.3, B07 53w/18s = 2.9, B08 57w/18s = 3.2, BVDT 66w/26s = 2.5. All inside 2.0–3.4 window. |
| 11 | type_check.py | (run at build time; results below) | |

## Datable-claim edits
- B05 command: `"in 2025?"` → `"today?"` — logged in REBUILD-LOG.md.

## Stale build records
- Removed metadata `.build` block from pre-rebuild sheet — it referenced Jul 16 mp4s that don't exist and now-obsolete slate list.
- Removed per-beat `build.*` blocks with `at: 2026-07-16T04:02:00` — they claimed VIDEO status against non-existent `media/*.mp4`.

## Blocked?
No. All checks either FIXED or PASS. Proceeding to PHASE 2.
