# REBUILD-LOG — claude-code-coding-assistant-deliberately-refuses-write

## Envelope (Phase 0)
- `beat_sheet.pre-rebuild.json` created byte-exact from `beat_sheet.json` before any edit.
- `metadata.design_version` bumped `v1` → `v2-rebuild`.
- Dropped legacy top-level metadata field `clock` (ElevenLabs-era master-clock prose;
  Kokoro measurement is the clock now).
- Consolidated duplicate closes: dropped legacy `YOURTURN` beat (its real narration and
  `command` migrated verbatim into the canonical `BHTF`) and legacy `OUTRO` beat (its
  title migrated into canonical `BOUT`, which already existed with the correct
  `ClaudeTitleOutro` pattern and mascotSeed).

## Narration edits (against the LOCKED contract)
| Beat | Old | New | Reason |
|---|---|---|---|
| `B00` | (locked) | (unchanged) | — |
| `B01` | (locked) | (unchanged) | — |
| `B02` | (locked) | (unchanged) | — |
| `B03` | (locked) | (unchanged) | — |
| `B04` | (locked) | (unchanged) | — |
| `B05` | (locked) | (unchanged) | — |
| `BVDT` | *(empty)* | Authored 4-sentence verdict from body content. | Check 4: empty narration is a violation. Body carries 6 beats / 213 words, well above the 5-beat / 180-word floor for AUTHOR. |
| `BHTF` | *(empty; canonical bookend was skeletal)* | Merged real narration from legacy `YOURTURN` verbatim. | Check 5c: canonical BHTF was empty; legacy `YOURTURN` beat carried a real prompt-based exercise. Locked script content, migrated slot. |
| `BOUT` | *(empty)* | "Why a coding assistant deliberately refuses to write the 6 lines that matter. Liam, in for Bear." | IN-FOR-BEAR LAW: outro signs off Liam. Title restate is the reel title verbatim. |

**No datable claims were changed** — this reel names the SessionStart hook mechanism, not
model versions or prices. Nothing to update.

## Shot / structural fixes (rebuilt, not locked)
| Beat | Old shot | New shot | Why |
|---|---|---|---|
| `B00` | ClaudeComposerAsk with `greeting: "Liam"`, empty output | ClaudeComposerAsk with `greeting: "Bonjour, Liam"` (rotated from "Konnichiwa" — sibling reel `claude-code-security-review-same-eval-real-bug-one` in the same batch holds Konnichiwa), 2-line real output, `modelLabel: "Claude Sonnet"` | Check 3 (spark line: greeting was persona-only; needed world-language hello + persona), Check 5 (output was empty) |
| `B01` | FormBCard with placeholder items ("Key point one/two/three", empty subs, generic icons) | FormACard with two real gap-form lines summarizing the tension the narration asks | Check 5 (placeholder subs / labels are template droppings), Check 6 (a card whose items are unfilled slots is a punt in a costume) |
| `B02` | *(no shot block — would have rendered as slate)* | FormBCard `"One file, two treatments"` with 2 real items (`Auto-filled — 34 lines of boilerplate` / `Held blank — 6 lines at the decision`) | Check 6 (an animatable beat left without a shot is a PUNT) |
| `B03` | *(no shot block)* | FormBCard `"How the plugin holds the six"` with 4 items enumerating the mechanism (SessionStart hook → reclassify → scaffold → blank) | Check 6, nopunt "Structure & relationship — a stack / architecture / N layers" row |
| `B04` | *(no shot block)* | ClaudeCodeBeat with a real 22-line rate-limiter carrying a 6-line held blank in `_refill()` at the token-bucket refill math (matches the narration exactly) | Check 6, nopunt "Code / app / interface → skin" row |
| `B05` | *(no shot block)* | FormACard with 2-line recap distilled from the mechanism | Check 6 |
| `BVDT` | ClaudeVerdictArtifact with placeholder `artifactLines: ["Key finding one", "Key finding two", "Key finding three"]` and empty narration | ClaudeVerdictArtifact with 3 authored artifactLines from body content + spoken narration reading the verdict aloud | Check 4 (placeholder verdict) |
| `BHTF` | ClaudeComposerAsk with template command `"Take what you learned from [X] and apply it to your own work. What's one thing you'll try first?"` | ClaudeComposerAsk with the real prompt migrated from legacy `YOURTURN` | Check 5c (the `[...]` template exercise is the seeded placeholder documented in the audit; belongs to the 3,472-sheet bug) |
| `BOUT` | ClaudeTitleOutro missing `handle` and `mascotSeed`; had stray `slug` prop | Added `handle: "@NikBearBrown"` + `mascotSeed`; removed `slug` (not a schema field) | Envelope normalization |

## VOICE-LOCK / dead field sweep (Phase 0)
- Every beat carries `voice: "am_onyx"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"`.
- No `voice_id`, `voice_env`, or ElevenLabs metadata anywhere.
- `metadata.clock` (prose) removed; `metadata.voice: "am_onyx"` added at the top level
  for parity with sibling reels.
- Every shot block now carries `form` (COMPOSER_ASK / FORM_A_CARD / FORM_B_CARD /
  CODE_BEAT / VERDICT_ARTIFACT / TITLE_OUTRO) per SHOT-FORM-SYSTEM.

## Pacing (Check 10 — LOG, do not silently retime)
Advisory 2.0–3.4 wps window. Since Kokoro measurement is the true clock, the
`estimated_duration_s` values below are advisory only; the actual master duration will
come from the mp3s.

| Beat | Words | est_s | wps | Note |
|---|---|---|---|---|
| B00 | 44 | 16 | 2.75 | ✓ |
| B01 | 26 | 10 | 2.60 | ✓ |
| B02 | 18 | 8 | 2.25 | ✓ |
| B03 | 51 | 18 | 2.83 | ✓ |
| B04 | 25 | 12 | 2.08 | ✓ (bumped from 16s — locked narration is short) |
| B05 | 51 | 18 | 2.83 | ✓ (bumped from 8s — narration is identical to B03; original 8s estimate would have forced 6.4 wps) |
| BVDT | 47 | 20 | 2.35 | ✓ |
| BHTF | 55 | 20 | 2.75 | ✓ |
| BOUT | 16 | 8 | 2.00 | ✓ |

## Nothing published
Never touched YouTube.
