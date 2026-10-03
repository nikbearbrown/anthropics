# REBUILD-LOG — lnp-endosomal-escape (@NikBearBrown / Teardown / CLI)

**Date:** 2026-08-30
**Source:** `beat_sheet.pre-rebuild.json` (byte-exact copy of the prior sheet).
**Channel decision:** Non-Claude channel — the NikBearBrown open (B00) and
outro (B09) are preserved (rebuild rule: "non-claude channels keep their own
skins — never Claude-wash an open or outro"). Verdict + your-turn Claude
bookends (BVDT, BHTF) are inserted BEFORE the outro so the locked B09
narration and NBB channel identity survive.

## LOCKED (carried over verbatim)
- All body-beat `narration_text` (B00, B01, B02, B03, B04, B05, B06, B07, B08, B09).
- Beat order and act labels for the CLI spine.
- Metadata title, slug, topic, register, style ("cli"), style_preset, palette,
  ground, color_semantics.
- NikBearBrown open + outro (channel identity, unchanged).
- NBB TerminalAsk commands for B02 and B05 (the actual Claude prompts).
- NBB CodeBlock code payload for B03.
- B04 Manim intent (LNP → endosome → 98/2 split) is preserved in narration and
  `visual_intent`; the render fallback is FormBCard while the Manim scene
  `B04_LNPEscape` remains outside this pipeline's build (TEMPLATE-MISSES).

## REBUILT / EDITED (envelope + punt fills, no narration paraphrase)

### Envelope (VOICE-LOCK)
- **DROPPED:** `metadata.voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs
  field; ElevenLabs is BANNED per VOICE-LOCK.
- **CHANGED:** `metadata.voice: "nbbhuman"` → `"am_onyx"` (Kokoro default).
- **ADDED:** `metadata.engine: "kokoro"`, `metadata.voice_kokoro: "am_onyx"`.
- **ADDED:** `metadata.derived_from`, `metadata.outro_source` (per rebuild).
- Per-beat `voice`/`engine`/`voice_kokoro` for BOOKEND lanes retained.

### Bookend surgery
- **REMOVED:** trailing `BOUT` beat (ClaudeTitleOutro) — B09 is already the
  channel outro (NikBearBrownOutro). A ClaudeTitleOutro after NBBOutro is a
  double outro AND a Claude-wash of a non-Claude channel; deleted.
- **KEPT:** `BVDT` (ClaudeVerdictArtifact) and `BHTF` (ClaudeComposerAsk) —
  inserted between B08 and B09 (the closing-block pattern used by every
  rebuilt sibling in this book).

### Datable-claim edits (narration)
None. No model versions, prices, or "as of" claims in the body script needed
correction. Facts (1–2% escape, Sahay et al., ALC-0315, SM-102, Onpattro 2018,
pKa 6.2–6.5) match the source chapter and the existing FACTCHECK.md.

### Verdict authored (BVDT)
Body qualifies for a real verdict: 10 body beats (B00–B09), well over the
5-beat / 180-word floor. Wrote a four-line artifact from the body's own
nouns and numbers (1–2%, pKa 6.2–6.5, endosomal pH 5.5, 5–10× best gain,
COVID vaccines as baseline, no phase 2 for cancer). Narration authored to
speak the artifact aloud without repeating it verbatim.

### Your Turn authored (BHTF)
Removed the placeholder template ("Take what you learned from
[Research LNP Endosomal Escape…] and apply it to your own work"). Authored a
real, video-specific prompt: pick an LNP, pull the ionizable lipid, check
pKa against the 6.2–6.5 window, check PEG-shedding kinetics. Output stub
gives a two-line rubric the viewer can paste back.

### Punt fills (body)
- **B01** was FormBCard with three "Key point one/two/three" placeholder labels
  and empty subs. Authored real title ("The 1–2% ceiling") and three items
  compressed from the narration (1–2% escape, 98–99% degraded, the bottleneck).
- **B04** had `source: "manim"` pointing at `B04_LNPEscape` in vox_scenes.py,
  which imports the legacy `vox_graphics` module and is not on this
  pipeline's Manim path. Fallback: FormBCard with five items enumerating the
  mechanism (endocytosis → pH drop → membrane disruption → 98/99 lysosome →
  1–2% cytoplasm). Logged as TEMPLATE-MISS for a future Manim port.
- **B06** was `shot.source: null` (bare SLATE hold). Authored FormBCard of
  three approaches (ionizable-lipid screening 5–10×, fusogenic peptides,
  disruptive polymers).
- **B07** was `shot.source: null`. Authored FormBCard of three summary lines
  (evolved defense, pH exploit, vaccines vs cancer split).
- **B08** was `shot.source: null`. Authored FormBCard of three viewer probes
  (pKa 6.2–6.5, PEG shedding, Onpattro baseline).

## Renders
No stale mp4s in the reel folder — `media/` holds only SVG text and a manim
partial cache; no B-level cuts yet. All body beats will render fresh from
these props on the next compile.
