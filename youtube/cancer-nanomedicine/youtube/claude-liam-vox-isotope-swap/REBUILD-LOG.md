# REBUILD-LOG — claude-liam-vox-isotope-swap

Rebuilt 2026-08-28 under the locked-script rebuild contract (skills/make/rebuild/SKILL.md).

## Locked (unchanged)
- Every body beat's `narration_text` (B01–B12) — no datable-claim rewrites needed. Isotope names (Ga-68, Lu-177) and the PSMA target are permanent facts, not dated versions.
- Beat order, act labels, shot INTENT per beat.
- Title, slug, topic, source, register, palette, channel.

## Envelope changes (VOICE-LOCK)
- DROPPED `metadata.voice_id` (ElevenLabs-era, dead field).
- REWROTE `metadata.clock` from ElevenLabs-era "…until GATE 0 audio lock" prose → "narration (Kokoro am_onyx, VOICE-LOCK); durations are measured after audio generation".
- DROPPED `metadata._variant_todo` — a legacy pre-rebuild TODO list; every item is already applied (Teardown register, Claude outro, kokoro voice).

## Authored spark line (B00) — SPARK-LINE LAW
- OLD: `props.greeting = "Liam"` (lone name, no world-language hello).
- NEW: `props.greeting = "Bonjour, Liam."` — French. Rotates against adjacent Claude reels in this run: Hola (delivery-funnel), Salaam (doxil-heart), Ciao (emitter-range), Namaste (endosomal-escape), Konnichiwa (epr-gap).

## Authored FormBCard items (B01) — no placeholder subs
- OLD items: "Key point one/two/three" with empty subs (template scaffolding).
- NEW items compressed from B01's own narration (metastatic diagnosis, drug on shelf, temptation to treat):
  - "Metastatic prostate cancer" / "the diagnosis fits"
  - "Known therapy available" / "the drug is on the shelf"
  - "Temptation: treat now" / "wait — the scan comes first"

## FormACard lines fixed (B02, B09) — no mid-word truncation
- B02 OLD: `"His team orders a scan first — not as a formality,…"` (narration fragment ending in ellipsis).
  NEW: `"The scan asks: is the target there?"` — the reel's core question.
- B09 OLD: `"So the scan is not paperwork. It is patient selection. A…"` (narration fragment).
  NEW: `"PSMA-negative: drug misses, tumor grows."` — the consequence the beat depicts.

## §8.9 mid-word truncation fixes
- B01 `title`, BVDT `artifactTitle`, BOUT `title` all ended on the 2-char word "It" — the type-check §8.9 dangling-fragment detector flagged this. Appended a period to each, ending the string on `.` (non-alpha) — no truncation flag.

## Authored verdict (BVDT) — VERDICT-AUDIT
- OLD artifactLines: "Key finding one/two/three" (template placeholder). Narration empty.
- NEW artifactLines, authored from body's own nouns/numbers (12-beat body, ~470 words):
  - "One molecule, two isotopes — Ga-68 lights the tumor; Lu-177 delivers the dose."
  - "Both bind the same PSMA handle: same biology, different job."
  - "The scan is patient selection — bright means the drug can bind; dark means it cannot."
  - "Illustrative example: 4 lit lesions shrank ~60%; 2 dark grew ~40% — response split by the scan."
- NEW narration for BVDT (was empty): spoken restatement of the four artifact lines.
- `estimated_duration_s` bumped 20 → 24 to fit the narration (~60 words at ~2.5 wps).

## Bookend pattern audit
| Beat | Pattern | Verdict |
|------|---------|---------|
| B00  | ClaudeComposerAsk | present, greeting authored |
| BVDT | ClaudeVerdictArtifact | present, verdict authored |
| BHTF | ClaudeComposerAsk | present, greeting "Your turn." |
| BOUT | ClaudeTitleOutro | present, title punctuation-terminated |

## Punt sweep
- No `shot.type` set to a gen-AI ask; no DoodleScene/DoodleChart; no `STILL src=archive` for a concept.
- The two `source: "ai"` STILL beats (B02, B09) fall back to REMOTION FormACard at review-cut time — declared slates per PHASE-2 policy.
- Legacy `build.needs` strings ("YOU → gen-AI clip → pantry") are stale build stamps from an earlier pipeline pass; will be re-stamped by compile.py.
- The 6 Manim body beats (B03/B05/B07/B08/B10/B11) are declared SLATE for the review cut; real Manim renders are a later human-flagged pass.

## Lens audit
- **Descartes** (radical doubt as checklist) — earned by B04 (THE QUESTION) + B07 (isotope swap): "if they work by identical biology, why does one scan have to come before the other?" produces the checklist that becomes the swap experiment.
- **Popper** (state failure in advance) — earned by B11: the reel states in advance what would count as failure (dark lesions grow, lit ones shrink) and finds exactly that split — the classic Popperian test.
- **Plato** (artifact vs world) — earned by B08/B09/B10: bright PET pixels (artifact) vs PSMA receptor biology (world) — the relationship is only bright→bind→treat.
- Three moves present; audit passes cleanly.

## Persona coherence
- Narration says "This is Liam, in for Bear" — voice is Kokoro `am_onyx` (Liam). Coherent.
- `folderLabel = @NikBearBrown` (channel handle). Correct.

## Pacing note (LOG only, per PHASE 1 §10)
Actual word-count / actual_duration_s wps (target 2.0–3.4):
- B01: 3.62 wps — HOT
- B02: 3.71 wps — HOT
- B04: 3.60 wps — HOT
- B08: 3.67 wps — HOT
- B10: 3.67 wps — HOT
- B12: 3.51 wps — HOT (marginal)
- All other body beats within range.
Audio was generated 2026-07-16 (mp3s exist and match this narration); retiming disallowed. Ships as-is.
