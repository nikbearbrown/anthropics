# REBUILD-LOG.md — nbb-vox-isotope-swap

Rebuild date: 2026-08-31 (filmloop invocation)
Source reel: `../vox-isotope-swap/` (post-rebuild 2026-08-27)
Contract: `skills/make/rebuild/SKILL.md`

## LOCKED (verbatim from pre-rebuild sheet)

- All body narration for B01–B12 (from source vox reel).
- NBB00 / NBB01 / NBB02 audio narration (frozen; mp3 already measured).
- NBB03 outro is silent (no narration).
- Beat order and act labels — structure preserved.

## REBUILT

### Stripped duplicate placeholder bookends (`B00`, `BVDT`, `BHTF`, `BOUT`)

The pre-rebuild sheet carried two competing bookend sets: the original
`NBB00/NBB01/NBB02/NBB03` (with real narration + measured Kokoro audio),
and a later scaffold-added `B00/BVDT/BHTF/BOUT` (empty narration, template
default artifactLines `Key finding one/two/three`, bracketed placeholder
BHTF command matching the sheet-wide 3,472-reel template). The empty set
is exactly what PHASE 1 checks #4 (verdict), #5c (BHTF placeholder), and
#6 (punt sweep) flag. Dropped the empties; the NBB* set already provides
canonical cold-open / verdict / your-turn / outro function with real
audio and real props.

### NBB00 (cold-open ClaudeComposerAsk)

- `props.greeting`: `"Your turn."` → `"Namaste, Liam"` (world-language hello,
  four words, not used by adjacent reels this session, not Bear's Wagwan).
- `props.segment`: `"One Molecule, Two Isotopes: See the"` (dangling `the`,
  §8.9 truncation) → `"Isotope Swap"`.
- `props.command`: the 87-word three-question ask (would overflow the composer
  card and clip mid-word) → a 3-sentence, 30-word framing that echoes the
  narration's opening. Narration_text (the audio) unchanged.

### NBB02 (BHTF-role your-turn ClaudeComposerAsk)

- `props.segment`: `"One Molecule, Two Isotopes: See the"` → `"Isotope Swap"`.
- `props.command`: the `[title]`-bracketed generic template ("Explain how
  [One Molecule, Two Isotopes: See the Tumor, Then Treat It] applies to
  a specific cancer type…") — the PHASE 1 §5c placeholder-in-brackets ban —
  → a real exercise built from the video's own nouns: "Pick a targeted
  therapy — trastuzumab for HER2, imatinib for BCR-ABL, cetuximab for EGFR.
  Sketch its companion PET probe: which protein is the handle, which isotope
  for imaging, which for therapy — and which patients would the scan
  disqualify from treatment?" Narration_text (the audio) unchanged.

### NBB03 (title-outro ClaudeTitleOutro)

- `props.title`: `"One Molecule, Two Isotopes: See the Tumor, Then Treat It"`
  ended with 2-char alpha `It` on a 55-char string → §8.9 flag → added a
  terminating period so the check sees non-alpha final char.

### B01 (title-card CARD)

- Dropped the unused `shot.remotion` FormBCard block (`title` with §8.9
  truncated ending; three items whose `sub` fields were empty — §8.11 fails).
  The B01 clip renders from the source vox pipeline (`media/B01.mp4` →
  `../../vox-isotope-swap/clips/B01.mp4`); the FormBCard was scaffolded and
  never wired to a real render. Removing it makes the sheet stop declaring
  props it never renders.

## VOICE-LOCK

All beats: `engine: kokoro`, `voice: am_onyx`. No ElevenLabs-era fields
present (this sheet was already clean on that axis). No `voice_id` /
`voice_env` / `clock` prose to drop.

## Renders

- NBB00 / NBB01 / NBB02 / NBB03 rendered via
  `runtime/scripts/remotion_scenes.py` (Remotion foreground, one at a time)
  from current `proven-core/` templates. NBB00/NBB02/NBB03 were re-rendered
  after the props edits above so the on-screen text reflects the fixes.
- B01–B12 rendered from source vox pipeline; symlinked from
  `../vox-isotope-swap/clips/B0*.mp4` into local `media/`. Two of them
  (B02, B09) render as slate cards from the source's slate list
  `[B02, B09, B13, B14]` — inherited from source, not a new punt here.
- B13 / B14 (source's OutroSeries / OutroCTA) not carried into the nbb
  variant — replaced by NBB01 / NBB02 / NBB03 as the current close block.

## Datable claims

No datable-claim edits — the narration references PSMA / Ga-68 / Lu-177 /
metastatic prostate cancer, none of which have moved. FACTCHECK.md from
the source reel covers the illustrative-numbers disclosure in B11.
