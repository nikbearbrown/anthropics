# AUDIT.md — nbb-slash-context-window-check

Reel: `books/anthropics/youtube/claude-code/nbb-slash-context-window-check`
Audited + rebuilt: 2026-08-31
Cohort: A (built-stale, but source clips/mp3s absent — treated as rebuild-in-place)

## PHASE 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` written from original `beat_sheet.json` (byte-exact) BEFORE any edits. — DONE
- Narration locked (see `REBUILD-LOG.md` for the datable-claim pass — none needed).
- VOICE-LOCK envelope normalized: kokoro / am_onyx everywhere; no ElevenLabs fields.
- Sheet was structurally malformed: 12 beats including duplicate cold opens (NBB00 + B00),
  duplicate verdicts (NBB01 + B04 + BVDT), off-topic YOUR TURN template pollution
  ("cancer type or clinical case" — NBB02), and duplicate outros (NBB03 + BOUT). Consolidated
  to 7 canonical beats. See REBUILD-LOG.md for the full mapping.

## PHASE 1 — Audit checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s existed at start; nothing to delete. |
| 2 | Bookends B00 / BVDT / BHTF / BOUT | FIXED | Canonical patterns present after consolidation. |
| 3 | Spark lines | FIXED | B00 greeting "Halo, Liam" (world-language rotation). Every inner beat's spark line is ≤4 words compressed from that beat's narration. BHTF greeting "Your turn." |
| 4 | Verdict | FIXED | BVDT authored fresh from B04's locked narration (kitchen-counter analogy) — 3 real artifact lines, none template default, none shared with other reels. Placeholder "Key finding one/two/three" removed. |
| 5c | Your-Turn placeholder | FIXED | BHTF authored a real subagent-invocation prompt from B05's narration; no `[ ... ]` brackets, no "apply it to your own work" template. |
| 5b | Chart text | PASS | No Manim charts in final beat sheet (see check 7 note); FormBCard labels are short category nouns ≤4 words. |
| 5 | Card text | FIXED | All FormBCard items have real labels + subs; no "TBD"/"see narration"/empty. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled fill_slates, zero DoodleScene/DoodleChart, zero archive stills. Every catalog-matched beat is authored. |
| 7 | Card-only reel | FIXED | B02 & B03 originally routed to `scenes_std.py` Manim scenes with the `Text(narration[:30])` truncation bug (PHASE 1 §5b). Converted both to FormBCard (short category labels + concise subs) — cleaner review-slate rendering, no chart-text truncation, honest picture of the concept. Not a punt: real Remotion figure with 3 icon-labeled cells each, tied to the narration's own enumerated content ("Three tools", "Main session → Reader subagent → summary"). |
| 8 | Lens audit (LENS-NOTES.md) | PASS | Descartes: B00 output lines expose the 78% figure so the falsifier ("run /context and see") is on screen. Popper: B01's "Liu 2025 shows quality degrades monotonically with window length" states, in measurable terms, what failure looks like. Plato: the reel names artifact (chat) vs world (code on disk + CLAUDE.md) throughout — "Chat is disposable infrastructure. Code on disk is progress." That is two moves min. |
| 9 | Brand fields | FIXED | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine: kokoro` / `voice: am_onyx` matches audio actually generated. Persona coherence: narration says "This is Liam, in for Bear" and the voice is Liam / Kokoro am_onyx — matches. |
| 10 | Pacing | PASS | Body-beat wpm against actual_duration_s: B00 82w/21.7s=3.8 wps (a touch fast, cold-open register); B01 65w/23.0s=2.8; B02 63w/21.5s=2.9; B03 65w/21.6s=3.0; BVDT 66w/19.0s=3.5 (slightly hot). All within Teardown tolerance; no forced retiming. |
| 11 | type_check.py | PASS | Initial run flagged B01 overflow §8.2 (Liu 2025 cell had a 4-line sub crossing the title-safe box); shortened sub to a single sentence, re-rendered, re-ran — GATE T: PASS. §8.10 B02 "narration recites the card" is advisory only. |

## PHASE 2 — Build

- Audio: `generate_audio_kokoro.py` produced 6 Kokoro `am_onyx` mp3s (BOUT silent). Total narration 123.6s. Measured durations stamped back into the sheet as `actual_duration_s`.
- Remotion: `remotion_scenes.py` rendered all 5 pattern beats (B00, B01, B02, B03, BVDT, BHTF, BOUT) into `media/*.mp4`.
- Compile: `compile.py --review --height 720` → `nbb-slash-context-window-check-slate.mp4` (133.0s, 720p). Lane-check PASS (no pipeline slates), Audio gate PASS (mean_volume -24.2 dB, max -2.9 dB).
- Gate V: sampled frames at 1 fps and beat-midpoint reads. All 7 beats legible, inside SAFE inset, one terracotta accent per beat, palette-correct cream/ink. No BLOCKER or MAJOR defects.
- build.status Counter: `Counter({'VIDEO': 7})` — 7/7 filled, 0 slates.
- mp4 mtime (1788204146) newer than beat_sheet.json mtime (1788204129) by 17s.

## Deliverable

`nbb-slash-context-window-check-slate.mp4` — 133s Kokoro-narrated review cut,
all 7 beats rendered real (no slates), passes lane-check + audio gate + GATE T.
