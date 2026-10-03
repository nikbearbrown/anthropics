# REBUILD-LOG — nbb-vox-dar-optimum

Rebuild pass: 2026-08-30. Locked-script rebuild + bookend consolidation.

## Backup
- `beat_sheet.pre-rebuild.json` — byte-exact snapshot of pre-rebuild sheet.

## Structural change — bookend consolidation
Sheet carried BOTH old-style NBB00-NBB03 bookends (populated, with measured audio)
AND empty B00 / BVDT / BHTF / BOUT scaffold beats added by a later pass but never
authored. `bookend_check.py` walks the beats in order and would resolve NBB01 as
BVDT (first ClaudeVerdictArtifact) — leaving the empty BVDT + BHTF + BOUT as
dead structural noise. Consolidated to a single populated bookend set:

- Deleted empty `B00` scaffold.
- Renamed `NBB00` → `B00`; moved `mp3/beat-NBB00.mp3` → `mp3/beat-B00.mp3`.
- Deleted empty `BVDT` scaffold (with placeholder "Key finding one/two/three").
- Renamed `NBB01` → `BVDT`; moved `mp3/beat-NBB01.mp3` → `mp3/beat-BVDT.mp3`.
- Deleted empty `BHTF` scaffold (with template "Take what you learned from [...]").
- Renamed `NBB02` → `BHTF`; moved `mp3/beat-NBB02.mp3` → `mp3/beat-BHTF.mp3`.
- Deleted empty `BOUT` scaffold (missing `handle`, missing `subline`).
- Renamed `NBB03` → `BOUT`; moved `mp3/beat-NBB03.mp3` → `mp3/beat-BOUT.mp3`.

Beat order is now: B00 · B01–B12 · BVDT · BHTF · BOUT.

## Narration
LOCKED — no narration_text changed. All body narration (B01–B12) still matches
the byte-exact pre-rebuild sheet. All four bookend narrations were already
authored and measured; they carry over verbatim to their renamed beat_ids.

## Props edits (non-narration; authorized fixes)

### B00 — spark line
- `greeting`: `"Liam"` (bare, would render as lone asterisk on cold-open)
  → `"Namaste, Liam"` (world-language hello, not used by adjacent sibling
  `claude-liam-vox-dar-optimum` which uses "Szia, Liam").

### BVDT — real verdict (was 3/3 placeholder lines)
- `artifactHeading`: `"Key findings"` → `"DAR is an optimum, not a maximum."`
- `artifactLines`:
  - was: `["Key finding one", "Key finding two", "Key finding three"]`
  - now:
    - `"At 72h: DAR-4 delivered 2.4 µg/g tumor. DAR-8 delivered 0.3."` (B11)
    - `"Hydrophobic payload past four flags the conjugate for liver clearance."` (B06/B07)
    - `"More warheads per molecule ≠ more drug at the target."` (B12)
- Narration (NBB01) already stated the finding; kept verbatim.

### BHTF — real Your-Turn task
- `topic`: `"CANCER NANOMEDICINE"` → `"YOUR TURN · CANCER NANOMEDICINE"`
  (required so `bookend_check.py` resolves this beat as BHTF).
- `command`: replaced the `Fable 5` placeholder ADC prompt with a specific
  task naming three current ADCs (T-DXd, sacituzumab govitecan, T-DM1), the
  actual physical property (logP), and a concrete comparison (predicted vs
  published clinical PK). No `[bracketed title]` placeholder; the exercise
  uses the video's own mechanism (hydrophobicity → clearance) as its rubric.
- Dropped stale `modelLabel: "Fable 5"` / `effortLabel: "High"` props.

### BOUT — outro fields per `bookend_check.py`
- Added `handle: "@NikBearBrown"` (was missing → would fail outro gate).
- Set `subline: ""` (was auto-generated fragment `"loading more warheads did
  not improve the weapon — it made the weapon undelivera"` — a mid-word
  truncation; per outro rules subline must be empty).
- Kept `title: "Load More Warheads on a Cancer Drug and It Gets Cleared Faster"`
  matching `metadata.title` exactly.

## Datable-claim edits
- Dropped `modelLabel: "Fable 5"` from BHTF props (stale placeholder from
  the 2026-07-16 scaffold; there is no "Fable 5" product).

## Envelope
- Added `metadata.channel_title: "@NikBearBrown"` (bookend_check expects it).
- Dropped `metadata.old_outro_beats: ["B13","B14"]` (dead — those beats never
  existed in this sheet).
- Dropped `voice_kokoro` mirror fields on beats where `engine: "kokoro"` /
  `voice: "am_onyx"` already lock it.
- Dropped `lane: "BOOKEND"` labels (no longer used by any current runtime).
- Dropped the FormBCard remotion block on B01 that carried placeholder
  "Key point one/two/three" items with empty subs — B01 renders from
  `source_clip` (the source reel's title card), so the FormBCard was dead
  data and would trip a lint if it ever rendered. B01 now uses its
  `card` (kind: title) block, matching the source reel's B01.

## Audio
Audio LOCKED (measured). Body audio is the source vox reel; bookend audio
sits in this reel's `mp3/` folder, renamed to match new beat_ids. No new
Kokoro generation needed.
