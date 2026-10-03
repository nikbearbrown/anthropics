# REBUILD-LOG — claude-liam-psma-theranostic-loop
_Rebuild pass: 2026-08-28_

## What was locked (carried verbatim)
- Narration_text on B00, B01, B02, B03, B04, B05, B06, B07, B08, B09 — every word preserved
- Beat order and act labels (INTRO → PROBLEM → ASK → CODE → OUTPUT → CHANGE → OUTPUT → SUMMARY → NEXT STEPS → OUTRO)
- Metadata identity: title, slug, topic, source pointer, register, channel
- Locked shot intents (visual_intent field values consumed as internal notes then dropped from JSON to keep sheet lean)

## What was rebuilt / dropped

### Metadata — dead ElevenLabs field DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `voice` | `"nbbhuman"` | `"am_onyx"` |

Fields `engine: "kokoro"` and `voice_kokoro: "am_onyx"` retained (already correct VOICE-LOCK).

### B00 — NikBearBrownOpen → ClaudeComposerAsk
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `NikBearBrownOpen` | `ClaudeComposerAsk` |
| `shot.remotion.props` | `{topic, lines: ["Nik Bear Brown", "Image it. Treat it. Image it again."]}` | `{greeting, topic, segment, command, runningText, folderLabel}` |

Reason: build.skin_warnings flagged this — palette=claude but cold open was NikBearBrownOpen (COLD OPEN LAW wants ClaudeComposerAsk). Narration LOCKED. Greeting: `"Zdravo, Liam."` (Serbo-Croatian hello) — not used by adjacent reels; alphabetical neighbors are protein-corona (empty greeting) and vox-abraxane-solvent ("Aloha").

### B01 — FormBCard placeholder items authored
| Field | Old | New |
|-------|-----|-----|
| `props.title` | reel title (76 chars, would overflow) | `"Same scaffold, two isotopes"` |
| `props.items[0].label/sub` | `"Key point one"` / empty | `"Ga-68-PSMA-617"` / `"Images every PSMA-positive metastasis."` |
| `props.items[1].label/sub` | `"Key point two"` / empty | `"Lu-177-PSMA-617 (Pluvicto)"` / `"Delivers targeted beta radiation to the same cells."` |
| `props.items[2].label/sub` | `"Key point three"` / empty | `"VISION trial (NEJM 2021)"` / `"OS 15.3 vs 11.3 mo in mCRPC."` |
| `lane` | `"BOOKEND"` | Removed (B01 is a body beat, not a bookend) |

Reason: Check 5 placeholder items violation. Content drawn from locked narration_text (PSMA-617 pair, Ga-68 imaging, Lu-177 therapy, VISION result).

### B02 / B05 — greeting spark lines fixed
| Beat | Old greeting | New greeting |
|------|-------------|--------------|
| B02  | `"The ask,"` | `"Research the pair."` (3 words, from beat narration) |
| B05  | `"The ask,"` | `"Compare the pairs."` (3 words, from beat narration) |

Reason: Check 3 — inner composer needs a spark line ≤4 words compressed from that beat's own narration, never a generic label.

### B04 — SLATE Manim scene (never authored) → FormBCard
| Field | Old | New |
|-------|-----|-----|
| `shot.source` | `"manim"` with `scene_class: "B04_TheranosticLoop"` in `vox_scenes.py` | `"own"` with FormBCard pattern |
| `build.needs` | `"PIPELINE → render animated_graphics.py scene B04_*"` | Removed |
| `props.items` | none | 4 items: IMAGE / TREAT / ASSESS / REPEAT-or-ESCALATE |

Reason: Check 6 punt sweep — B04_TheranosticLoop was a phantom Manim scene (no `vox_scenes.py`/`scenes_std.py` in this reel, no rendered mp4). Rather than author a one-off Manim scene, the 4-stage loop is delivered as an enumerated FormBCard following the pattern of `her2-low-bystander` and `nanomedicine-translation-gap` (accepted reels). Nopunt catalog: "A ladder / tiers / hierarchy → ladder built rung by rung" — an enumerated 4-stage loop is a close match to FormB enumerated named things.

### B06 / B07 / B08 — SLATE gen-AI ask punts → FormBCard × 3
| Beat | Old `build.needs` | New |
|------|------------------|-----|
| B06  | `"YOU → 5–10s gen-AI clip → pantry"` | FormBCard: DOTATATE mirror (Ga-68-DOTATATE / Lu-177-DOTATATE / NETTER-1) |
| B07  | `"YOU → 5–10s gen-AI clip → pantry"` | FormBCard: theranostic rule (confirm target / treat only confirmed / confirm response) |
| B08  | `"YOU → 5–10s gen-AI clip → pantry"` | FormBCard: is your tumor a candidate (membrane-facing target / low in normal tissue / imaging isotope on same scaffold) |

Reason: Check 6 punt sweep — `YOU → gen-AI clip → pantry` is the canonical punt costume. Each maps to an enumerated named-things beat → FormBCard per nopunt catalog. Content authored from locked narration_text of each beat.

### BVDT — verdict authored from body
Old `artifactLines`: `["Key finding one", "Key finding two", "Key finding three"]` (placeholder)  
Old `narration_text`: `""` (empty)

New `artifactLines` (4 lines, drawn from B01/B04/B06/B08):
1. "PSMA-617: Ga-68 for imaging, Lu-177 for therapy — one scaffold, two isotopes."
2. "VISION trial (NEJM 2021): Lu-177-PSMA-617 improved OS by ~4 months in mCRPC."
3. "DOTATATE mirrors it in neuroendocrine tumors — two validated pairs, one rule."
4. "The loop works when a quantifiable membrane target shares its scaffold with an imaging isotope."

New `narration_text`: "Two isotopes, one scaffold. Gallium sixty-eight images the tumor; lutetium one seventy-seven treats it. The VISION trial added four months of overall survival in metastatic castration-resistant prostate cancer. DOTATATE mirrors the pattern in neuroendocrine tumors — two validated pairs, one rule: image to confirm the target, treat only what you can see, then image the response."

Source: locked narration of B01 (Ga-68/Lu-177 pair), B04 (VISION +4 mo OS), B06 (DOTATATE mirror / NETTER-1), B08 (membrane target + imaging scaffold criteria).

`artifactTitle` shortened from the full reel title (76 chars) to `"PSMA Theranostics: Image, Then Treat"` (36 chars) — reel title would overflow the card frame at typecheck golden-string LONGEST width.

### BHTF — kept per accepted precedent
Command / rubric left as accepted her2-low-bystander pattern (generic scaffolded prompt). Segment display shortened to `"PSMA Theranostics: Image, Then Treat…"`.

### BOUT / B09 — title displays shortened
| Beat | Field | Old (76 chars) | New (36 chars) |
|------|-------|---------------|----------------|
| BOUT | `props.title` | reel title | `"PSMA Theranostics: Image, Then Treat"` |
| B09  | `props.title` | reel title | `"PSMA Theranostics: Image, Then Treat"` |

Reason: Golden-strings LONGEST-width overflow risk. Same fix as sibling `vox-emitter-range` reel.

## Datable claims checked
- VISION trial year (2021) and OS numbers (15.3 vs 11.3 mo) — verified against NEJM 2021 (Sartor et al., NEJM 385:1091–1103, PSMA-Radioligand Therapy in Metastatic Castration-Resistant Prostate Cancer).
- Isotope names (Ga-68, Lu-177, Ac-225) unchanged — chemistry doesn't rot.
- Trade names (Pluvicto for Lu-177-PSMA-617; Lutathera for Lu-177-DOTATATE) verified current.
- No `Opus 4.8`-style stale model claims present.

No corrections needed.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of old sheet, created 2026-08-28T14:32 before any edit
- `beat_sheet.json` — rebuilt sheet (this pass)
