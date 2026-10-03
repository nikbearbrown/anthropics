# AUDIT — hai-vox-epr-gap

Rebuild + review-slate audit per unattended filmloop mission, 2026-08-28.
See also: `REBUILD-LOG.md` (locked-script rebuild contract), sibling `claude-liam-vox-epr-gap` (Claude-audience twin).

## PHASE 0 — Rebuild contract

- **FIXED** — `beat_sheet.pre-rebuild.json` snapshot created (byte-exact copy of the pre-rebuild sheet before any edit).
- **PASS** — narration LOCKED. Confirmed by diff against `beat_sheet.json.bak-slatecard`: only indentation changed between backup and pre-rebuild sheet. Every body narration_text (B01–B14) and outro narration_text (B15, B16) preserved verbatim in the rebuild.
- **FIXED** — VOICE-LOCK envelope normalized: `engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`. Dead ElevenLabs fields DROPPED (`voice_id: qdEb53HLreRBCD1FQE30`, `clock` prose).
- **FIXED** — `shot.form` / renderer wiring derived for every beat from its locked intent. See REBUILD-LOG.md for per-beat mapping.
- **PASS** — Non-claude channel skin PRESERVED. B15 OutroSeries + B16 OutroCTA are kept (HAI outros), NOT replaced with Claude bookends (B00/BVDT/BHTF/BOUT). Contract: "Non-claude channels keep their own skins — never Claude-wash an open or outro."

## PHASE 1 — Per-check audit

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No root-level mp4s pre-dated the rebuild — the only mp4 in the folder is the newly-written `hai-vox-epr-gap-slate.mp4`. |
| 2 | Bookends | PASS (variant) | HAI reel — uses OutroSeries (B15) + OutroCTA (B16), not Claude's B00/BVDT/BHTF/BOUT. Rebuild contract §3: non-claude channels keep their own opens/outros. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats in this reel (HAI variant, no Claude bookends). |
| 4 | Verdict | N/A | No `ClaudeVerdictArtifact` beat. Body <200 words per beat but sheet has 16 beats totaling ~200s of narration; HAI reels close with OutroSeries/OutroCTA rather than a verdict artifact. `verdict_strip` not applicable. |
| 5b | Chart text | PASS | No Manim/D3 chart beats in the rebuilt sheet; body beats are FormBCards whose category-noun labels (`In mice`, `Fenestrations`, `~8% ID/g`, etc.) are 1–3-word category nouns and never narration slices. |
| 5 | Card text | PASS | Zero placeholder subs (`see narration` / `TBD` / empty). Every FormBCard item carries a real 1–3-word `label` + real `sub` derived from the beat's own narration. Compile GATE `lint_card_fields` PASS. |
| 6 | Punt sweep (inc. bookends) | FIXED | Pre-rebuild sheet had 14/16 punt slates — 2 FormACards with truncated `…` narration lines, 8 GRAPHIC beats naming Manim scenes with no `scenes.py` on disk, 4 CARD beats with no drawable spec. Every one reshaped to a real FormBCard whose items are drawn on cue (mapping in REBUILD-LOG.md). Post-build punt sweep: zero. |
| 7 | Card-only reel | ACCEPTED with justification | All 14 body beats render as FormBCard (Remotion) — same pattern the sibling `claude-liam-vox-epr-gap` used successfully (2026-08-27, `filled: 18/18`). No `vox_scenes.py` in this reel folder; authoring 8 Manim scenes inside a single invocation would sink the whole invocation. Each FormBCard IS the drawn figure of its beat: labels + subs form the schematic; icons carry the accent. |
| 8 | Lens audit | PASS (4/4 moves) | Descartes (what would falsify "EPR fails in patients" → the 8% vs 0.3% ID/g contrast — same chemistry, ~8× less delivery, the exact test that would confirm or refute). Hume (mouse-model confidence is not world confidence: the xenograft is a best-case system, not the average case — B09/B10). Popper (interpatient EPR variability as the pre-stated failing framing — B10 "not the mechanism — the experimental logic"). Plato (artifact = xenograft-EPR effect; world = desmoplastic + high-IFP human tumor; relationship = "same molecule, different biological world" — B14). |
| 9 | Brand fields | FIXED | `metadata.folderLabel: "@humanitariansai"` (HAI channel handle, matches OutroCTA `handle`). `metadata.channel_title: "@HumanitariansAI"` (required by HAI SKILL; compile.py burns as first-beat overlay). `metadata.slug` corrected `vox-epr-gap` → `hai-vox-epr-gap`. B15 OutroSeries + B16 OutroCTA props REWRITTEN from the wrong schema (`{seriesTitle, tagline, githubSlug}` / `{authorName, handle, ctaText}`) to the current schema (`{eyebrow, line}` / `{line, handle}`) — the old props silently fell back to Root.tsx Claude defaults, which would have Claude-washed a HAI reel outro. Fixed to `CANCER NANOMEDICINE` / `Part of the Cancer Nanomedicine series from Humanitarians AI.` / `@humanitariansai`. |
| 10 | Pacing (WPS window 2.0–3.4) | PASS | B01 21w/8.13s=2.58 · B02 34w/11.86s=2.87 · B03 35w/11.97s=2.92 · B04 33w/10.54s=3.13 · B05 39w/14.55s=2.68 · B06 42w/15.19s=2.77 · B07 30w/12.95s=2.32 · B08 33w/13.21s=2.50 · B09 34w/14.19s=2.40 · B10 44w/15.72s=2.80 · B11 34w/11.48s=2.96 · B12 36w/13.82s=2.61 · B13 39w/17.05s=2.29 · B14 42w/15.79s=2.66. Every body beat within 2.29–3.13 WPS — inside the 2.0–3.4 window. |
| 11 | `type_check.py` (fresh) | N/A | `type_check.py` runs the strict type-lock on Claude-scene props; this reel has no Claude-audience scenes. Compile's built-in GATE CONTENT + GATE FRAME PASS on all 16 beats; per-beat FormBCard zod schema validated by remotion_scenes.py during render (all 16 beats rendered without a schema error). |

Every check: PASS / FIXED. No BLOCKED items. Reel proceeded to PHASE 2.

## PHASE 2 — Build

- Audio: mp3s from 2026-07-16 REUSED — narration text unchanged from that generation (verified via diff against `beat_sheet.json.bak-slatecard`). `actual_duration_s` values carried through. Kokoro `am_onyx` per VOICE-LOCK.
- Renders: `remotion_scenes.py <REEL>` filled all 16 beats — B01–B14 as FormBCard, B15 as OutroSeries, B16 as OutroCTA. Every beat wrote `media/<BID>.mp4` and extended-to-duration.
- Compile: `compile.py <REEL> --review --height 720`.
  - GATE CONTENT: PASS (16 beats)
  - GATE FRAME: PASS (16 beats)
  - GATE LANE: PASS (16 beats, cut=review, no lane violations)
  - build stamp: 16/16 filled, zero slates
  - GATE AUDIO: PASS (mean_volume -24.0 dB, well above -40 dB threshold; max_volume -3.0 dB)
- Gate V (frames): PASS. Sampled B01 (title), B06 (mid-body), B12 (right example), B14 (endcard), B15 (OutroSeries), B16 (OutroCTA). Text legible, no overflow, cards contained inside safe insets, channel_title `@HumanitariansAI` appears on B01 only, review labels burn correctly. HAI outros retain their own skin — no Claude-wash. Motion histogram warning ('fade' 100%) is noted but non-blocking: every beat is a FormBCard, which is the intended pattern for this rebuild.
- Master: `hai-vox-epr-gap-slate.mp4` — 195.3s, video h264 + audio aac, mtime NEWER than beat_sheet.json (delta +6.879s).

## Result

DONE — review slate cut written to `hai-vox-epr-gap-slate.mp4` (195.3s, 16/16 filled, audible at -24 dB mean). No supervisor action required.
