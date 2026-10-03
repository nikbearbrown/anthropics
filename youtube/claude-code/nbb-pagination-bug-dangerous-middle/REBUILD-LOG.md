# REBUILD-LOG — nbb-pagination-bug-dangerous-middle

## Phase 0

- `beat_sheet.pre-rebuild.json` created as a byte-exact copy of the old sheet.

## What was locked

- The 10 body beat narrations (B01–B10) verbatim.
- Act structure, on_screen text, and Manim scene_class references for B02–B10.
- Title, slug, topic, source-reel pointer, channel (`@NikBearBrown`).

## What was rebuilt

### Bookend consolidation (double-bookend defect)

The old sheet carried TWO parallel bookend sets:

- `B00 / BVDT / BHTF / BOUT` — empty scaffolder skeletons with placeholder
  props (`"Key finding one"`, `"Take what you learned from [ … ]"`, etc.).
- `NBB00 / NBB01 / NBB02 / NBB03` — the actually-authored bookends from the
  original nbb variant.

Consolidated to the canonical four names. The NBB* content moved into the
canonical slots; the empty skeletons were dropped.

| Old slot | Old state | New slot | Fix |
|---|---|---|---|
| `B00` | empty skeleton, greeting `"Liam"` | dropped | superseded |
| `NBB00` | filled ClaudeComposerAsk, greeting `"Your turn."` (wrong for cold open) | `B00` | greeting → `"Hola, Liam"` (world-language hello + Liam persona per IN-FOR-BEAR LAW); command tightened; output lines added so the ask lands answered (COLD OPEN LAW) |
| `NBB01` | filled ClaudeVerdictArtifact with truncated artifactLines (mid-sentence ellipses) | `BVDT` | artifactLines rewritten as 3 complete summary sentences from body content (audit #4); narration rewritten as a real spoken verdict (audit #4 authorizes verdict narration rewrite) |
| `NBB02` | filled ClaudeComposerAsk your-turn — narration + command both about "cancer type or clinical scenario" (stale template from another reel) | `BHTF` | narration + command rewritten to a real pagination-boundary exercise from this reel's own content (audit #5c authorizes) |
| `NBB03` | filled ClaudeTitleOutro | `BOUT` | kept; added explicit `slug` prop |
| `BVDT / BHTF / BOUT` | empty skeletons | dropped | superseded |

### B01 shot cleanup

Old B01 carried both a locked CARD description (real on_screen text) AND a
scaffolded `FormBCard` with placeholder items (`"Key point one"`, empty `sub`).
The placeholder FormB was dropped; B01 now renders as `FormACard` with the
real locked lines.

### Envelope normalization (VOICE-LOCK)

- Every beat now carries `engine: "kokoro"`, `voice: "am_onyx"`,
  `voice_kokoro: "am_onyx"` — the working default per VOICE-LOCK.md.
- Dropped ElevenLabs-era fields: none were present in this sheet.
- Dropped `locked: true`, `source_clip`, `source_audio`, legacy `audio_file`
  pointers into the non-existent source-reel mp3s (the source reel has no
  mp3s of its own — only `timings.json`; carrying the pointers would leave
  the compiler chasing files that never existed).
- Dropped `actual_duration_s` from every beat — will be measured from freshly
  generated Kokoro audio (rule: "actual_duration_s from measurement, never
  carried from the old sheet").

## Datable-claim edits

- B00 (was NBB00) narration: spelled out numerals as spoken form for TTS —
  "50" → "fifty", "251st" → "two-hundred-fifty-first", "50, 51, 100, and 101"
  → "fifty, fifty-one, one hundred, and one hundred and one". Not a datable
  fix; a TTS-safety edit so Kokoro doesn't misread digits mid-clause. Meaning
  unchanged.

## What was NOT changed

- No body-beat narration was rewritten. All B01–B10 narration is byte-identical
  to the pre-rebuild sheet.
- No Manim scenes were regenerated — the existing `Scene_B02_...` through
  `Scene_B10_...` in `scenes_std.py` are the shot list, unchanged.
