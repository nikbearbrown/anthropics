# REBUILD-LOG — claude-liam-lnp-endosomal-escape

_Rebuild run 2026-08-30 (nopunt supervisor invocation)_

## Backup
- `beat_sheet.pre-rebuild.json` — byte-exact copy of the previous `beat_sheet.json` (mtime 2026-08-19).

## Doctrine call — non-Claude channel, keep NBB skin

Folder name has the `claude-liam-` prefix and metadata carries `palette: claude`, but the
locked narration is unambiguously NBB channel content: B00 opens with
"This is Liam, in for Bear. Nik Bear Brown." and B09 closes with
"At Nik Bear Brown, nikbearbrown dot com." Per rebuild SKILL rule #3
("Non-claude channels keep their own skins; don't Claude-wash them") and the narration
lock, B00 and B09 keep the NBB scenes (`NikBearBrownOpen`, `NikBearBrownOutro`).

Consequence — the two Claude bookends that had been scaffolded onto the sheet
(BVDT verdict, BHTF your-turn) are kept but repositioned to sit BEFORE B09 (the
NBB outro) so the reel reads open → body → verdict → your-turn → outro, not
open → body → outro → verdict. The third placeholder Claude bookend (BOUT,
`ClaudeTitleOutro`) was DROPPED as redundant with B09 — the NBB outro already
performs the title-restate role.

## Locked (verbatim from pre-rebuild sheet)
- All body narration (B01–B08).
- B00 and B09 narration.
- Beat order for B00–B08.
- Scene patterns for the NBB-skinned beats (NikBearBrownOpen / NikBearBrownTerminalAsk
  ×2 / NikBearBrownCodeBlock / NikBearBrownOutro) and the Manim scene reference
  (B04_LNPEscape in vox_scenes.py).

## Rebuilt (per current doctrine)
1. **VOICE-LOCK envelope**: metadata `voice: nbbhuman` → `voice: am_onyx`; `voice_id`
   (dead ElevenLabs field) DROPPED; `_variant_todo` and `build` snapshots removed
   (they were stale as of the empty media/ folder). `engine: kokoro` and
   `voice_kokoro: am_onyx` retained.
2. **B01 FormBCard** — placeholder labels "Key point one/two/three" with empty
   `sub` fields replaced with real content drawn from B01's narration:
   - "1–2% escape" · "the fraction of mRNA that reaches the cytoplasm and makes protein"
   - "98–99% degraded" · "the rest is trafficked to the lysosome and destroyed"
   - "The bottleneck" · "cellular defense, not formulation or tumor delivery"
   Title changed from the full reel title (which overflowed the card) to "The 1–2% ceiling."
3. **B06 / B07 / B08 slates → FormBCards** (nopunt sweep). All three body beats
   were `SLATE` with `needs: YOU → gen-AI clip` — a punt for animatable enumerated
   content per nopunt catalog "Enumerated concepts → FormB". Authored real FormB
   items from each beat's narration; nothing invented, all labels/subs sourced
   from the locked script.
4. **BVDT verdict** — placeholder heading "Key findings" + placeholder lines
   "Key finding one/two/three" + empty narration replaced with a real verdict
   built from body content:
   - `artifactTitle`: "LNP endosomal escape — the ceiling and how it moves"
   - `artifactHeading`: "What the reel showed"
   - `artifactLines`: four specific lines pulled from B01/B04/B06/B08.
   Narration authored to say the finding aloud (not "here is what the evidence shows").
5. **BHTF your-turn** — template command "Take what you learned from [ ... ] and apply
   it to your own work" (the seed-generated placeholder from 2026-08-30 catch) and
   empty `output` array replaced with a real exercise from B08's practical checks
   (pKa 6.2–6.5 window, PEG-lipid shedding). Narration authored to speak the ask.
6. **BOUT dropped** — redundant with B09 (NBB outro already restates title).
7. **Beat order** — repositioned BVDT + BHTF to sit BEFORE B09 so the reel closes:
   body → verdict → your-turn → NBB outro.

## Datable-claims audit (narration lock exception)
None applied — the narration's factual anchors (Onpattro 2018 first LNP; ALC-0315
in Pfizer BNT162b2; SM-102 in Moderna mRNA-1273; Sahay et al. ~1–2% escape;
Siegwart lab ionizable-lipid libraries; GALA fusogenic peptide) all remain current
as of 2026-08-30. No datable-claim edits made; no line changes to log.

## Audio
Existing `mp3/beat-B00.mp3` through `mp3/beat-B09.mp3` are Kokoro `am_onyx`
renders whose narrations match the (unchanged) locked script — reused as the
clock. Fresh Kokoro takes generated only for the newly-authored BVDT and BHTF
narrations.
