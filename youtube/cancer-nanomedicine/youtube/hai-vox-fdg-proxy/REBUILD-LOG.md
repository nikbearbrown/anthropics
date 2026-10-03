# REBUILD-LOG — hai-vox-fdg-proxy

Rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`. Old sheet is
treated as a LOCKED SCRIPT + SHOT LIST; only envelope + broken card text was
edited. `beat_sheet.pre-rebuild.json` is a byte-exact snapshot of the sheet
before this pass.

## LOCKED (verbatim carry-over)

- All 14 `narration_text` fields — no rewrites, no paraphrase.
- Beat order (B01–B14) and act labels (COLD OPEN, THE QUESTION, THE PROBLEM,
  THE MECHANISM, THE IMPLICATION, THE EXAMPLE, RECAP, OUTRO).
- Metadata identity: slug, title, topic, source pointer, palette=humanitarians,
  register=Pragmatist, audience=HAI.
- Shot INTENT per beat: pattern/props/scene descriptions preserved.

## REBUILT

### Envelope — VOICE-LOCK
- DROPPED `metadata.voice_id: "qdEb53HLreRBCD1FQE30"` (dead ElevenLabs field)
- DROPPED `metadata.clock: "narration (Kokoro (VOICE-LOCK)) — durations …"`
  (dead ElevenLabs GATE-0 prose)
- KEPT `engine: "kokoro"`, `voice_kokoro: "am_onyx"` — matches audio on disk

### Card text — truncated FormACard lines rewritten (not narration)
The three `shot.remotion.props.lines` fields on FormACard beats carried
placeholder ellipsis-truncated text ("...for…", "...cells…", "...surgery…")
that would render literally on screen. Rewritten as short editorial hooks
that paraphrase (not recite) the narration.

| Beat | Old (broken) | New | Source |
|---|---|---|---|
| B02 | "FDG-PET is the standard tool for staging cancer and checking for…" | "the standard cancer scan" | narration §1 |
| B06 | "And glucose metabolism is not unique to cancer. Activated immune cells…" | "cancer isn't the only thing that glows" | narration §1 paraphrase |
| B09 | "Here's an illustrative case. A 58-year-old patient — breast cancer surgery…" | "one patient — three flagged nodes" | narration paraphrase |

### Narration — datable-claim pass
Sheet contains no dated model/version/price claims. Scientific content
(Warburg effect, FDG mechanism, false-positive causes) is not a datable
claim in the SKILL sense. No edits to narration.

### Skin / open / close
- Non-claude channel: kept vox-editorial open (B01 title card) and HAI
  OutroSeries + OutroCTA close. Not Claude-washed per SKILL.md.

### Audio
- Kokoro `am_onyx` mp3s already present in `mp3/` from prior pass
  (2026-07-16). `actual_duration_s` measured and stamped in sheet.
- No re-generation needed this pass.

### Gates
- TYPECHECK.md — GATE T PASS (one advisory §8.10 at 0.50 for B06, below
  advisory-refusal threshold).
