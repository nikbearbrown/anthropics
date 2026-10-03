# AUDIT — one-sentence-problem-statement

Date: 2026-08-31
Auditor: unattended film-factory pass
Reel: `books/anthropics/youtube/claude-code/one-sentence-problem-statement`

## Phase 0 — Rebuild contract
| Step | Result |
|---|---|
| `beat_sheet.pre-rebuild.json` created (byte-exact) | PASS |
| Envelope normalized (dropped `clock`, `total_estimated_duration_seconds`) | PASS |
| `palette=claude`, `channel=claude-liam`, `folderLabel=@NikBearBrown` set (was absent) | FIXED |
| Legacy duplicate bookends `YOURTURN` / `OUTRO` dropped (superseded by `BHTF` / `BOUT`) | FIXED |
| `shot.form` derived for every beat | PASS |
| No `TEMPLATE-MISSES` | PASS |

## Phase 1 — Audit checks
| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders (mp4 older than sheet) | PASS | `media/videos/` and `mp3/` carry no `.mp4`; nothing to delete. |
| 2 | Bookends (B00 / BVDT / BHTF / BOUT canonical patterns) | FIXED | All four present. `YOURTURN` / `OUTRO` legacy duplicates removed. |
| 3 | Spark lines | FIXED | B00 was `"Liam"` → `"Namaste, Liam"` (world-language rotation; adjacent claude-code reels use Ciao / Sawadee — Namaste is unused). BHTF: `"Your turn."` (the handoff exception). No other inner ClaudeComposerAsk beats need sparks. |
| 4 | Verdict (BVDT) | FIXED | Was three placeholders (`Key finding one/two/three`) + empty narration. Body is 4 body beats + ~223 words → authored real verdict from body's own nouns/numbers. `verdict_audit.py` no longer flags this reel. |
| 5b | Chart text | N/A | No Manim/D3 chart beats in this reel. |
| 5c | Your-Turn placeholder (BHTF) | FIXED | Was the seeded `"Take what you learned from [ ... ] and apply it to your own work"` template (3,472-sheet placeholder caught 2026-08-30). Authored a real 3-step exercise from the video's own method: draft your one sentence, circle every 'and,' check the three questions (system / user / done-condition). |
| 5 | Card text (FormA / FormB placeholders / overflow) | FIXED | B01 was FormBCard with `Key point one/two/three` + empty subs → converted to FormACard driven by the beat's own `on_screen` lines. B03 FormBCard items now use real labels + subs (no placeholders, no overflow — 3–4 word labels, ~55-char subs). |
| 6 | Punt sweep (gen-AI asks, unfilled slates, DoodleScene/Chart, archive stills, empty on_screen visual) | PASS | Zero of any of these. |
| 7 | Card-only reel | FIXED | Original sheet had B01/B02/B04 as CARD + B03 as GRAPHIC (Manim scenes with mid-word-truncated text — unrenderable). Rebuild routes B03 to a two-up FormBCard comparison (`with 'and'` vs `without 'and'` with `circle-x` / `circle-check` icons) — a schematic drawing, not a text card. B01/B02/B04 remain FormACard text cards, but B03 satisfies the "at least one drawn figure" rule. |
| 8 | Lens audit (Descartes / Hume / Popper / Plato — need ≥2 moves) | PASS | **Popper move (falsifiability):** B03 defines what a valid sentence must look like (one system, one user, one done-condition, no ands) — an in-advance measurable failure condition (`refused`). The `/v0` gate IS the Popperian test written into the tool. **Plato move (artifact/world):** B01 makes the artifact (the sentence Seth types) and the world (the four different systems it disguises) explicit and interrogates the relationship — the sentence LOOKS like one project (fluent artifact); the WORLD is four projects; the relationship is that fluency masked hidden decisions. Two moves earned. |
| 9 | Brand fields (folderLabel is a handle; engine/voice describe actual audio) | FIXED | `folderLabel=@NikBearBrown` (handle, not `@claude-liam`). Every beat has `engine=kokoro / voice=am_onyx / voice_kokoro=am_onyx` matching what Kokoro will generate. Narration is Liam-in-for-Bear via Kokoro `am_onyx` — persona coherent. |
| 10 | Pacing (2.0–3.4 wps against estimated duration) | LOG-ONLY | B01 68w/27s ≈ 2.5 wps ✓. B02 30w/11s ≈ 2.7 wps ✓. B03 75w/29s ≈ 2.6 wps ✓. B04 50w/21s ≈ 2.4 wps ✓. BVDT 42w/16s ≈ 2.6 wps ✓. BHTF 34w/14s ≈ 2.4 wps ✓. All within band. |
| 11 | `type_check.py` | PASS | GATE T: PASS. §8.10 advisories on B01 (1.00) / B04 (0.86) / BVDT (0.92) are ADVISORY only, not blockers. Narration is LOCKED (rebuild contract §Locked) so B01/B04 recite scores cannot be reduced without breaking the lock; BVDT is a verdict beat where the artifact IS the compressed narration. Gate passes. |

## Verdict: PROCEED to Phase 2 (build review slate).
