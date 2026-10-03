# REBUILD-LOG.md — nanoparticle-characterization

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B00–B09) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B00 INTRO · B01 PROBLEM · B02 ASK · B03 CODE · B04 OUTPUT · B05 CHANGE · B06 OUTPUT · B07 SUMMARY · B08 NEXT STEPS · B09 OUTRO.
- Metadata identity: title, slug, topic, register, palette, source pointer.
- B00 `NikBearBrownOpen` + B09 `NikBearBrownOutro` skins (non-Claude channel — kept per contract).

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice_kokoro: am_onyx`); ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk` DROPPED.
- Metadata `short_title: "The Characterization Cascade"` added (used for FormBCard/outro card titles so they stay inside the 12-word §8.5 pull-quote limit).
- B01 FormBCard: items rewritten from placeholder `Key point one/two/three` + empty subs to three real card items compressed from B01 narration.
- B04, B06, B07, B08: `shot.source: null` (slate punts) → routed to `FormBCard` written from each beat's own narration and `visual_intent`.
- B04 card title shortened from full reel title to `"Seven Together Define the Product"`.
- B09 `NikBearBrownOutro` `title` prop shortened from full reel title (14 words) to `"The Characterization Cascade"` — de-wordify per §8.5.
- BOUT `ClaudeTitleOutro` `title` prop shortened same way.
- BVDT: placeholder `Key finding one/two/three` REPLACED with four real verdict lines authored from the body's own claims. `artifactHeading: "Key findings"` → `"Verdict"`. BVDT `narration_text` written to speak the verdict aloud (was empty).
- BHTF `segment` shortened; `command` prompt rewritten from the your-turn scaffolder default to a specific next-action drawn from B08 (corona-delta measurement).

## Datable-claim edits

None. Narration cites regulatory thresholds (PDI, zeta, EE, release, endotoxin) that are FDA / USP baselines, not versioned; no model names, prices, or "as of" phrasing.

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.

## Reel-level notes

- Persona coherence: narration says "Nik Bear Brown" — voice is Kokoro `am_onyx` per current VOICE-LOCK (`nbbhuman` maps to `am_onyx`); consistent.
- Non-Claude cold open and outro retained; bookend recap slot uses Claude artifacts (already in the sheet at snapshot time).
