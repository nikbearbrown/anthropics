# REBUILD-LOG — nbb-vox-epr-gap

Date: 2026-08-28
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of prior sheet)

## Locked (verbatim carry-over)
- `narration_text` on body B01..B14 (July-16 script; datable-claim edits: none).
- Beat order and act structure.
- Metadata identity: title, slug, topic, source pointers, register=Teardown, palette=teardown.

## Rebuilt

### Bookends — the empty-scaffold cleanup
Pre-rebuild sheet carried BOTH an empty `B00 / BVDT / BHTF / BOUT` scaffold
(`narration_text: ""`, placeholder `Key finding one/two/three` on BVDT, placeholder
`greeting: "Liam"`) AND a filled `NBB00 / NBB01 / NBB02 / NBB03` set that was the
real cold-open / verdict / your-turn / title-outro. Duplication would have shipped
two of every bookend. Fixed as in the sibling `nbb-vox-abraxane-solvent` rebuild:

- DROP the four empty-scaffold bookends.
- RENAME the filled NBB set to canonical ids:
  - `NBB00` → `B00`   (ClaudeComposerAsk cold open)
  - `NBB01` → `BVDT`  (ClaudeVerdictArtifact recap)
  - `NBB02` → `BHTF`  (ClaudeComposerAsk your-turn)
  - `NBB03` → `BOUT`  (ClaudeTitleOutro)
- RENAME `mp3/beat-NBB0X.mp3` files on disk to match.

### Bookend content edits
- `B00.props.greeting`: `"Your turn."` → `"Bonjour, Liam"` (French — world-language
  hello; not used in adjacent nbb reels this batch: Olá, Namaste, Konnichiwa, Annyeong,
  Vanakkam, Kia ora, Ni hao already spoken for; French is open).
- `B00.props.segment`: `"Why the Tumor That Shrank in"` (mid-word truncation) →
  `"epr gap · mouse vs patient"`.
- `B00 / BHTF.props`: DROPPED `modelLabel: "Fable 5"` and `effortLabel: "High"` — this
  is a Kokoro reel, not a Claude-model-branded cut (per sibling policy).
- `BVDT.props.artifactHeading`: `"Why the Tumor That Shrank in Mice Won't"` (truncated
  mid-title) → `"why the mouse tumor shrank and the patient's didn't"`.
- `BVDT.props.artifactLines`: was four narration snippets (three truncated with `…`).
  AUTHORED three real verdict lines from body nouns/numbers:
  1. Subcutaneous mouse xenograft = EPR maximum — thin walls, no stroma, no IFP.
  2. Human desmoplastic tumor = EPR blocked — fibrous stroma, high interstitial pressure.
  3. Same nanoparticle: ~8% ID/g in mouse vs ~0.3% in patient (illustrative).
- `BOUT.props`: added `handle: "@NikBearBrown"` and `subline: "same molecule, different world"`.

### Body — punt sweep (card-only rebuild)
Every body beat B01..B14 in the pre-rebuild sheet was either a placeholder FormBCard
(B01: `Key point one/two/three`), a truncated FormACard (B02, B06), or `type: GRAPHIC`
with a `graphic.manim: BXX_*` scene that does not exist as source (there is no
`vox_scenes.py` in this reel folder — same problem the sibling `claude-liam-vox-epr-gap`
rebuild encountered), or a plain CARD kind (B04 question / B09 section / B14 endcard)
with no drawable spec.

Every body beat rewritten to a `FormBCard` (reel-local Remotion pattern) with a
title and 3 items derived from the beat's own locked narration. To avoid re-authoring
identical narration twice, the FormBCard shots are borrowed verbatim from the sibling
`claude-liam-vox-epr-gap` (same narration, same author decisions, already validated
by GATE T there). B01 items authored fresh:

- B01: In mice / In patients / Same molecule.

Every other body beat B02..B14: FormBCard shot copied from sibling reel.

### Envelope
- Metadata: added `voice_kokoro: "am_onyx"` top-level. Dropped `body_beats` and
  `old_outro_beats` (redundant with the beat list).
- Every beat: `engine: "kokoro"`, `voice: "am_onyx"`, `voice_kokoro: "am_onyx"`.
- Body beats: DROPPED `source_audio`, `source_clip` fields (ElevenLabs-era pointers
  to `../vox-epr-gap/mp3/beat-B0X.mp3`). Audio regenerated locally with Kokoro at
  24 kHz. `actual_duration_s` re-measured.

### Datable-claim edits
- None. Mechanism is timeless (mouse xenograft is EPR-maximum; desmoplastic + IFP is
  EPR-blocked). Illustrative numbers (8% / 0.3% ID/g, 200 nm) are labeled illustrative
  in the FormBCard subs and the narration hedges ("Illustrative numbers.").

### Bookend audio regenerated
- The July-16 NBB00 mp3 was 3.88s (mismatch: the current bookend narration is 87 words,
  which needs ~33s at 2.6 wps). Re-generated `beat-B00.mp3`, `beat-BVDT.mp3`,
  `beat-BHTF.mp3`, `beat-BOUT.mp3` with fresh Kokoro at their current narration texts.

## Notes
- Lens (PHASE 1 §8): four moves earned — Descartes (the 8% vs 0.3% ID/g contrast is
  the exact falsifier for the EPR delivery mechanism when applied to human tumors);
  Hume (mouse-model confidence is not world confidence — the xenograft is a best-case,
  not the average case); Popper (interpatient EPR variability is the falsifying framing —
  a drug optimized in max-EPR was never tested under desmoplastic + high-IFP conditions);
  Plato (xenograft-EPR is the artifact, the desmoplastic + high-IFP human tumor is the
  world, "same molecule, different biological world" names the relationship).
- Card-only reel is accepted per §7 with the same rationale as the sibling: no
  `vox_scenes.py` exists, and each FormBCard's items IS the drawn figure for its beat.
