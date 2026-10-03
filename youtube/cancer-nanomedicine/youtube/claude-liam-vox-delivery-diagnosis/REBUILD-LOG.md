# REBUILD-LOG — vox-delivery-diagnosis

Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (copied byte-exact before any edit).

## Narration edits

All body narration (B01–B12) is UNCHANGED — locked script.

BVDT narration_text was EMPTY (placeholder verdict beat, artifactLines were
"Key finding one/two/three"). Authored a real verdict from the body's own
nouns and numbers:

  OLD: "" (empty)
  NEW: "The verdict. A failed nanoparticle trial has two indistinguishable
       causes: the drug was too weak, or the particle never delivered it.
       The response endpoint cannot tell them apart — both look like no
       shrinkage. Biodistribution imaging can. Label the identical particle
       with a contrast agent — fluorescent dye, iron oxide, radiolabel — and
       read where it actually went. Particles in the liver and spleen mean
       the immune system cleared them; the fix is engineering — PEGylation,
       size, surface charge. Particles in the tumor mean delivery worked;
       the fix is pharmacology — change the drug. Measure delivery before
       changing the payload."
  Source: body of the reel (B01–B12); no new claims introduced.

## Spark line

B00 greeting placeholder "Liam" → "Kia ora, Liam."
  - Māori hello; not used by any adjacent reel in the current run
    (nearby adjacents in this book use Aloha, Sawubona, Hola, Salaam,
    Ciao, Namaste, Konnichiwa, Bonjour, Hej, Merhaba).

BHTF greeting is already "Your turn." — untouched.

## Verdict artifact lines

  OLD: ["Key finding one", "Key finding two", "Key finding three"]
  NEW: 4 real findings derived from the body's mechanism +
       implication acts; each specific enough that it would not be true
       of a different video.

## VOICE-LOCK envelope normalization / dead field drops

Dropped from metadata:
  - `voice_id`: "TyW6NH39JcFb5M3xdIIk"  (ElevenLabs — dead, VOICE-LOCK is Kokoro am_onyx)
  - `clock`: ElevenLabs-era prose  (no longer relevant; audio is Kokoro)
  - `isotype_mark`, `accents`, `ground`, `style_bible`   (unused legacy scaffold)
  - `total_estimated_duration_seconds`               (derived from audio, not authored)
  - `_variant_todo`                                   (rebuild is now the variant)

Kept: engine=kokoro, voice_kokoro=am_onyx, palette=claude, register=Teardown,
      color_semantics, source, note, purpose, aspect_ratio, style_preset,
      audience, outro_source, topic, title, slug.

## Beat lane / shot form derivation

Old sheet routed every body beat to CARD / GRAPHIC / STILL / DOCUMENT with
`build.status: SLATE` and a "PIPELINE → render animated_graphics.py" or
"YOU → gen-AI clip" needs string. NONE of those pipelines is wired for
this machine — every one of those beats would be a slate in the final cut,
so this was a card-only reel wearing a graphic costume (see PHASE 1 check 7).

For each body beat, derived shot.form from the locked narration's pattern
and intent (SHOT-FORM-SYSTEM contract):

  B01  cold-open setup with 3 discrete facts       → FormBCard (3 items)
  B02  method-intro with 3 steps                   → FormBCard (3 items)
  B03  THE QUESTION — 2 clauses, one question      → FormACard (3 lines)
  B04  two opposite causes under one outcome       → FormBCard (3 items)
  B05  opposite fixes + the wrong-fix penalty      → FormBCard (3 items)
  B06  hazard summary                              → FormACard (3 lines)
  B07  three modality labels for one particle      → FormBCard (3 items)
  B08  two outcomes + payoff                       → FormBCard (3 items)
  B09  three engineering levers                    → FormBCard (3 items)
  B10  short conclusion for the biology branch     → FormACard (3 lines)
  B11  two-program compare with illustrative n's   → FormBCard (3 items, "Illustrative" in title)
  B12  RECAP                                       → FormACard (3 lines)

All items use SHORT category-noun labels + narration-derived subs, one
COMPLETE sentence per sub. No `sub` is empty. No label is a placeholder.

## Dropped beats

Removed dead legacy outros B13 (OutroSeries) and B14 (OutroCTA) — both were
scaffolded before the four-bookend contract (B00 / BVDT / BHTF / BOUT) landed
and both duplicated what BOUT (ClaudeTitleOutro) now carries. The old
metadata.build.skin_warnings entry ("B14: palette=claude but the outro is
'OutroCTA'") is what flagged this; the fix is to drop the dead beats, not
paint over them. The Kokoro mp3 files for B13/B14 remain on disk but are
unreferenced.

## What was NOT changed

  - No body narration text (locked script)
  - No color semantics (TEAL / CRIMSON assignment intact)
  - No topic, no title, no source citation
  - No B00 / BHTF composer command intent (composer greeting on B00 only)
