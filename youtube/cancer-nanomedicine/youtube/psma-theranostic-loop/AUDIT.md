# psma-theranostic-loop · AUDIT

Reel: `cancer-nanomedicine/youtube/psma-theranostic-loop`
Auditor: unattended film-factory pass
Date: 2026-08-28

## PHASE 0 — pre-rebuild backup + envelope

- **beat_sheet.pre-rebuild.json** — CREATED (byte-exact copy of the 2026-08-19 sheet made before any edit).
- **VOICE-LOCK envelope** — normalized. Metadata now `engine: kokoro`, `voice: am_onyx`,
  `voice_kokoro: am_onyx`, `folderLabel: @NikBearBrown`, `channel_title: @NikBearBrown`,
  `persona: "Liam (in for Bear)"`, `audience: NikBearBrown`.
- **Dead ElevenLabs-era fields DROPPED** — metadata `voice_id: TyW6NH39JcFb5M3xdIIk` removed;
  metadata `voice: nbbhuman` replaced.
- **Old NBB channel skins RETAINED** (per rebuild doctrine: non-claude channels keep their own
  opens/outros). B00 `NikBearBrownOpen`, B02/B05 `NikBearBrownTerminalAsk`,
  B03 `NikBearBrownCodeBlock`, B09 `NikBearBrownOutro`. Claude-side bookends BVDT/BHTF/BOUT
  appended in current pattern.

## PHASE 1 — audit results

| # | Check                                    | Result       | Notes |
|---|------------------------------------------|--------------|-------|
| 1 | Stale renders (mp4 older than sheet)     | PASS         | No mp4 in reel folder — nothing to delete. |
| 2 | Bookends (B00 / BVDT / BHTF / BOUT)      | PASS         | All four present with canonical patterns. Non-claude channel — B00 stays `NikBearBrownOpen`. |
| 3 | Spark lines (composer greetings ≤ 4 wds) | FIXED        | B02 `"The ask,"` → `"PSMA pair, please."`; B05 `"The ask,"` → `"Compare the pairs."`; BHTF `"Your turn."` retained. |
| 4 | Verdict (BVDT)                            | AUTHORED     | Body has 9 body beats and ~460 narrated words — meets the 5+ / 180+ threshold. Placeholder lines ("Key finding one/two/three") replaced with four real lines drawn from the body's own nouns and numbers (PSMA-617 scaffold; VISION 15.3 vs 11.3 mo mCRPC; DOTATATE / NETTER-1; the loop rule). BVDT narration authored to say it aloud. `artifactHeading` moved off the "Key findings" default to "What two validated pairs prove". |
| 5b| Chart text (Manim B04)                    | PASS         | `B04_TheranosticLoop` box labels are short category nouns (Ga-68 PSMA / SELECT / Lu-177 / ASSESS). VISION annotation is a complete sentence. Return-arrow escalation label is 4 words. `Ac-225` alpha/beta callout is a single line. No narration-slice text. |
| 5 | Card text (Form* items)                   | FIXED        | B01 FormBCard placeholder labels/subs ("Key point one/two/three", empty subs) replaced with real content (Ga-68 image / Lu-177 treat / VISION OS 15.3 vs 11.3). B06 and B08 authored with real content (see punt sweep). |
| 6 | Punt sweep (unfilled slates / gen-AI)     | FIXED        | Original B06/B07/B08 had `shot.source: null` (punts in slate costume). B06 → `FormBCard` two-pair comparison. B07 → `FormACard` three-line rule. B08 → `FormBCard` three-check candidacy list. Zero remaining unfilled slates in the body. |
| 7 | Card-only reel                            | PASS         | B04 is a Manim scene (`B04_TheranosticLoop`); B02/B03/B05 are terminal skins. Not a card-only reel. |
| 8 | Lens audit (Descartes / Hume / Popper / Plato) | PASS  | (a) Descartes — B01/B04/BVDT bind the claim to falsifiable numbers: OS 15.3 vs 11.3 months from VISION (NEJM 2021). What would falsify: an OS delta that vanishes or flips sign in an independent trial. (b) Popper — B08 states in advance what disqualifies a tumor from the loop: no membrane-facing overexpressed target, or no imaging isotope on the same scaffold. That is the failure condition, stated before the search. Two moves cleared; ≥ 2 required. |
| 9 | Brand fields                              | FIXED        | `folderLabel: @NikBearBrown` (channel handle, not brand key). `engine: kokoro`, `voice: am_onyx` — matches the audio the pipeline will actually generate. Persona `Liam (in for Bear)` is coherent with `am_onyx`. |
|10 | Pacing (2.0–3.4 WPS)                      | LOGGED       | B02 was 24 wds / 15 s = 1.6 WPS (slow) — tightened `estimated_duration_s` to 12. B04 was 87 wds / 20 s = 4.35 WPS (fast) — extended to 28. B01 was 66 wds / 10 s = 6.6 WPS — extended to 22. Others fall in-window. Kokoro measurement will overwrite `actual_duration_s` at audio time. |
|11 | `type_check.py` (GATE T)                  | DEFERRED     | Runs after compile — `TYPECHECK.md` will be written by the pipeline. Content-side fixes above are the prerequisite. |

## What was written in this pass

- `beat_sheet.pre-rebuild.json` — byte-exact backup.
- `beat_sheet.json` — full rewrite: envelope normalized; B01 items authored; B06/B07/B08 punt beats
  authored as real Remotion patterns; BVDT verdict + narration authored from body content;
  BHTF prompt made specific and actionable; BOUT title-restate wired to `ClaudeTitleOutro`.
- `AUDIT.md` — this file.

## Datable-claims log (per REBUILD-LOG.md contract)

No datable-claim edits were required. VISION (NEJM 2021, OS 15.3 vs 11.3 mo) and NETTER-1 are
carried verbatim from the original sheet; both remain current as of 2026-08-28. Ac-225 remains
"Phase I/II ongoing" — accurate. No model names, versions, or prices in this reel.

## Status

- PHASE 1: PASS — no blockers logged; not adding this reel to `youtube/BLOCKED.md`.
- Proceeding to PHASE 2 (audio → render → compile → Gate V).
