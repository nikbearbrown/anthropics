# REBUILD-LOG — nbb-vox-delivery-funnel

_Started 2026-08-30 · rebuild contract per `skills/make/rebuild/SKILL.md`_

## Phase 0 — backup + normalize

- Wrote `beat_sheet.pre-rebuild.json` (byte-exact copy of pre-edit `beat_sheet.json`).
- Envelope: `voice=am_onyx, engine=kokoro, folderLabel=@NikBearBrown`. No ElevenLabs
  fields present, none carried forward.

## Structural changes (bookends canonicalized)

Beat sheet before: 18 beats — `B00, NBB00, B01…B11, NBB01, NBB02, NBB03, BVDT, BHTF, BOUT`.
`NBB00-03` were the legacy scaffolded bookend layer; `B00/BVDT/BHTF/BOUT` were later
canonical placeholders (empty slates). Both present at once = duplication.

Resolution: dropped `NBB00, NBB01, NBB02, NBB03`. Authored real content into the
canonical `B00/BVDT/BHTF/BOUT` slots so bookend_check + audit pass.

Beat sheet after: 15 beats — `B00, B01…B11, BVDT, BHTF, BOUT`.

## Narration edits (all logged; no unauthorized rewrites)

### B00.props.greeting

- old: `"Liam"` (missing world-language hello)
- new: `"Namaste, Liam."`
- source: PHASE-1 audit item 3; adjacent siblings use `Hola, Liam` / `Kia ora, Liam` so
  rotated to `Namaste` per no-repeat rule.

### BVDT.narration_text + props.artifactLines

- old narration: `""` (empty; beat was a slate)
- new narration: `"The verdict. Between the syringe and the tumor cell the dose is
  lost at five sequential steps: circulation clearance, vessel escape, matrix
  penetration, cell uptake, and payload release. The targeting ligand only helps
  at step four. A particle cleared by liver and spleen in the first hour never
  reaches step four. Only 0.7 percent arrives. The particle wasn't misbehaving —
  the delivery chain failed upstream."`
- old artifactLines: `["Key finding one", "Key finding two", "Key finding three"]`
  (template placeholder — flagged by verdict_audit rules)
- new artifactLines:
  - `"Five sequential losses: circulation → vessel → matrix → uptake → release"`
  - `"Targeting ligand only helps at step 4 (cell uptake) — upstream losses dominate"`
  - `"A particle cleared in the first hour never reaches step 4"`
  - `"0.7% arrives; upstream leaks kill the ligand's chance"`
- source: authored from B04–B11 body narration (five-step chain, ligand step 4 fix,
  0.7% funnel resolution). Body qualifies for real verdict (11 beats, ~350 words).

### BHTF.narration_text + props.command

- old narration: `""` (empty; beat was a slate)
- new narration: `"Your turn. Take a targeted nanoparticle you know — Doxil,
  Abraxane, an L-N-P — and walk it through the five-step funnel: circulation,
  extravasation, matrix penetration, cell uptake, release. For each step, is the
  loss measured or assumed? Which upstream step, if left alone, kills any
  downstream fix?"`
- old command: `"Take what you learned from [Why Only 0.7% of a Cancer Nanoparticle
  Reaches the Tumor] and apply it to your own work. What's one thing you'll try
  first?"` — the seeded bracket-placeholder template (PHASE-1 item 5c).
- new command: `"Walk a targeted nanoparticle formulation you know (Doxil,
  Abraxane, an LNP, or a design you're working on) through the five-step delivery
  funnel — circulation survival, extravasation, matrix penetration, cell uptake,
  payload release. For each step: is the loss MEASURED or ASSUMED? Estimate the
  arriving fraction by multiplying. Then rank the steps by dose lost and propose
  one design change that attacks the biggest leak — not the smallest."`
- source: authored from body content (five-step vocabulary, the "measured vs
  assumed" epistemic move that survives the reel). No square brackets, no title
  restate, real viewer exercise.

### B01.props.items

- old: `[{"label":"Key point one","sub":""},…]` scaffolded placeholder
- new: three real items with numbers/verbs from the body
- note: B01 renders from `media/B01.mp4` (inherited from source reel), so the
  Remotion metadata is fallback only. Fixed so future compiles don't ship a
  placeholder if the media slot is ever regenerated.

## Non-narration edits

- `metadata.body_beats` regenerated to `[B01…B11]` (was including NBB IDs)
- `metadata.old_outro_beats` removed (referred to dropped NBB* legacy)
- `metadata.channel_title` set to `@NikBearBrown` so bookend_check passes
- `BOUT.props`: stripped `slug` field, ensured `title` + `handle` present, no
  baked subline (bookend_check outro assertions).

## Sanity gates

- `type_check.py` → GATE T PASS
- `bookend_check.py` → PASS — four bookends correct
- kokoro audio generated for BVDT (21.18s) + BHTF (17.22s), voice=am_onyx
- Remotion rendered B00 / BVDT / BHTF / BOUT (ClaudeComposerAsk × 2,
  ClaudeVerdictArtifact, ClaudeTitleOutro)
- compile.py → 15/15 filled, 4K master 184.5 s, GATE AUDIO PASS (mean -27.7 dB)

## Known-source issues (NOT introduced by this rebuild)

- `B02` inherits a `PIPELINE → render vox_graphics.py scene B02_*` slate from the
  source reel's `../vox-delivery-funnel/clips/B02.mp4`. The nbb rebuild carries the
  source clip forward as-is (source_clip is locked); fixing B02 belongs to the
  source reel's own build, not this variant.
