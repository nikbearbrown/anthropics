# REBUILD-LOG.md — nanoparticle-characterization

Rebuilt 2026-08-30 per PHASE 0 REBUILD CONTRACT.
Byte-exact backup: `beat_sheet.pre-rebuild.json`.

## Envelope (REBUILT)
- Dropped ElevenLabs-era `voice`=`"nbbhuman"` and `voice_id`=`"TyW6NH39JcFb5M3xdIIk"` from metadata; VOICE-LOCK is kokoro/am_onyx.
- Kept metadata `engine`/`voice_kokoro`/audience/palette.
- Removed stale `metadata.build` block (no longer accurate after rebuild).

## Narration (LOCKED)
All beat narration carried verbatim from pre-rebuild. Exceptions logged below.

- B00: NARRATION KEPT VERBATIM ("This is Liam, in for Bear. Nik Bear Brown. A nanoparticle is a distribution. Not a molecule.").
- BVDT: NARRATION AUTHORED (was empty; body>180 words → PHASE 1 check 4 requires an authored verdict). New narration: "Verdict. A nanoparticle is a population, not a molecule. Seven measurements — DLS, PDI, zeta, encapsulation, release, stability, sterility — each with its own artifact; all seven together define the product. Buffer is not plasma; PBS is not blood. The corona delta is the number that predicts the patient."
  - Source: body of this reel, B01–B08.
- BHTF: NARRATION AUTHORED (was empty; template placeholder command). New narration: "Your turn." (spark line). Real exercise authored into command props.
- BOUT: NARRATION EMPTY (outro mascot; ClaudeTitleOutro provides its own text).

## Skin swaps (REBUILT — claude channel)
- B00: `NikBearBrownOpen` → `ClaudeComposerAsk` (COLD OPEN LAW).
- B09: `NikBearBrownOutro` → `FormACard` (BOUT owns the outro; B09 becomes a body colophon card carrying the closing brand line without duplicating a mascot outro).
- BVDT artifactLines: template "Key finding one/two/three" → three authored findings from body.
- BHTF command: template "Take what you learned from [X]…" → real exercise built from B08's "Your move" content.

## Spark lines authored (≤4 words each, compressed from that beat's narration)
- B00 greeting: `Sawubona, Liam` (Zulu hello — rotation).
- B02 greeting: was `The ask,` → `Ask Claude,` (compressed from "In the terminal: ask Claude to research…").
- B05 greeting: was `The ask,` → `Now iterate,` (compressed from "Now iterate: ask Claude why…").
- BHTF greeting: `Your turn.`

## Datable claims
None. Source (`cancer-nanomedicine/chapters/11`) is time-invariant biology/regulation.

## VOICE-LOCK / engine
- metadata: engine=kokoro, voice=am_onyx (was voice_kokoro=am_onyx + dead nbb fields).
- Per-beat voice fields normalized to kokoro/am_onyx.
