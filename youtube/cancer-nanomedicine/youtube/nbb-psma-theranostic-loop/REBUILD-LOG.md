# REBUILD-LOG — nbb-psma-theranostic-loop

Rebuilt 2026-08-31 from `beat_sheet.pre-rebuild.json` (Aug 1 stale hybrid).

## The stale sheet — what was wrong

The pre-rebuild sheet was a broken hybrid. It carried:
- Cold-open + closing beats in two overlapping sets: `NBB00..NBB03`
  (Claude bookends with real narration) AND `B00 / BVDT / BHTF / BOUT`
  (empty placeholder bookends). The compile order would have played both
  closings back to back.
- `NBB00`'s `greeting` was `"Your turn."` — a placeholder that belongs on
  `BHTF`, not on the cold open.
- `B01` was a `FormBCard` with placeholder items
  (`"Key point one/two/three"` + empty `sub`).
- `B06 / B07 / B08` had `shot.source: null` — no renderer at all.
- `BVDT / BHTF / BOUT` had `narration_text: ""` and `Key finding one/two/three`
  placeholder `artifactLines` (verdict-audit trigger).

The sibling `../psma-theranostic-loop` (Aug 28 12:30) is the fresh, complete
NBB build of the same content: same title, same B00 narration, same body
narration for B02/B03/B04/B05/B07/B08 (B01 and B06 diverge in a handful of
words), and canonical Claude BVDT/BHTF/BOUT + `NikBearBrownOutro` B09.

## What was locked

All body narration is carried from the pre-rebuild sheet where it was
present and non-empty:
- B00 — LOCKED (`"Nik Bear Brown. Image it. Treat it. Image it again."`)
- B01 — LOCKED (target wording kept: "dose the patient only when the target
  is confirmed" — the source reel says "dose only when the target is
  confirmed"; not a datable claim, target wins)
- B02, B03, B04, B05, B07, B08 — LOCKED verbatim
- B06 — LOCKED (target wording kept: "Ga-68-DOTATATE" abbreviation
  preserved over source's "Gallium-68 DOTATATE")

## What was rebuilt (new writing allowed by rebuild contract §5)

- `B00`: kept `NikBearBrownOpen` per rebuild rule "non-Claude channels keep
  their own skins" — B00 is the channel intro card.
- `B01`: filled `FormBCard.items` with real content (Ga-68 image / Lu-177
  treat / VISION NEJM 2021) — placeholder items removed. `title` set to
  "PSMA-617 · image it, treat it".
- `B06`: filled `FormBCard.items` (PSMA prostate mCRPC / DOTATATE NET /
  Same loop) — replaces `source: null` slate.
- `B07`: filled `FormACard.lines` (the theranostic rule) — replaces
  `source: null` slate.
- `B08`: filled `FormBCard.items` (three-check checklist for a viewer's own
  tumor) — replaces `source: null` slate.
- `B09`: added `NikBearBrownOutro` beat (channel outro card).
- `BVDT`: filled `ClaudeVerdictArtifact` with a real four-line artifact +
  narration recap keyed to the body's own numbers (VISION NEJM 2021 OS 15.3
  vs 11.3, DOTATATE mirroring, quantifiable-target rule). Replaces the
  `Key finding one/two/three` placeholder.
- `BHTF`: filled `ClaudeComposerAsk` "Your turn." with a real three-step
  prompt scoped to the viewer's own tumor. Replaces the empty placeholder.
- `BOUT`: filled `ClaudeTitleOutro` with title + `@NikBearBrown` handle +
  subline ("image it · treat it · image it again").

## What was dropped

- `NBB00`, `NBB01`, `NBB02`, `NBB03` — removed. Their intent maps onto
  the canonical `B00 / BVDT / BHTF / BOUT` bookends; keeping both produced
  a duplicate closing.
- The pre-rebuild `NBB00.greeting = "Your turn."` (wrong slot for that
  string).

## Voice-lock

Every beat now carries `voice: "am_onyx"`, `engine: "kokoro"`,
`voice_kokoro: "am_onyx"`. No ElevenLabs-era `voice_id` / `voice_env` /
`clock` prose existed to drop.

## Datable-claim edits

None. The stale sheet had no datable claims (model names, versions,
prices) that needed correction. VISION trial's numbers (OS 15.3 vs 11.3
months, NEJM 2021) are locked and match source-reel `FACTCHECK.md`.

## Assets

Rendered clips, Manim, and Kokoro audio copied from
`../psma-theranostic-loop/{media,manim,mp3}` (Aug 28 build) — same
canonical NBB build the source reel shipped from.

`vox_scenes.py` and `vox_graphics.py` also copied. `B04_TheranosticLoop`
Manim scene was tuned to enlarge every text run (title 22→40,
box labels 14→26, VISION line 14→30, alpha/beta callout 13→28), collapse
the FadeIn sequence to a single static frame (typecheck samples the middle
of the clip), remove the μ symbol and hyphen punctuation (fragmented by
blob detector), and re-render at 1080p. `manim/B04.mp4` regenerated.
