# REBUILD-LOG.md — vox-trial-failure-tree (nbb variant)

Rebuild date: 2026-08-28
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`

## Pre-rebuild snapshot

`beat_sheet.pre-rebuild.json` — byte-exact copy of the incoming sheet, made first.

## Locked (carried over verbatim)

- All body-beat narration (B01–B13) — no wording changes.
- All body-beat act labels, order, `production_viz` intents, `graphic.manim`
  scene ids, chart mechanics, document quotes.
- Metadata identity (slug, title, topic, audience, palette, register).
- The four bookend narrations (former NBB00 cold-open ask, NBB01 verdict,
  NBB02 your-turn, NBB03 title-restate) — carried into the new B00/BVDT/BHTF/BOUT
  slots verbatim.

## Rebuilt (regenerated per current doctrine)

### Bookend consolidation (dedupe)

Incoming sheet carried BOTH a modern skeleton (`B00`, `BVDT`, `BHTF`, `BOUT` —
empty narration, placeholder-only) AND the legacy `NBB00`/`NBB01`/`NBB02`/`NBB03`
bookends (real narration + measured audio). The two sets duplicated the
canonical four-bookend roles. Resolution:

- Deleted: empty `B00`, `BVDT`, `BHTF`, `BOUT` placeholders.
- Renamed: `NBB00` → `B00`, `NBB01` → `BVDT`, `NBB02` → `BHTF`, `NBB03` → `BOUT`.
- Renamed corresponding mp3 files (`beat-NBB0*.mp3` → `beat-B00.mp3` /
  `beat-BVDT.mp3` / `beat-BHTF.mp3` / `beat-BOUT.mp3`).
- Updated `remotion.rendered.out` paths (`media/NBB0*.mp4` → matching canonical
  ids).

Result: exactly one instance of each canonical bookend id, each carrying real
narration and real audio, in the pattern order ClaudeComposerAsk →
ClaudeVerdictArtifact → ClaudeComposerAsk → ClaudeTitleOutro.

### Spark-line fixes (display only, no narration change)

- `B00.props.greeting`: `"Your turn."` → `"Konnichiwa, Liam"`. Reason: B00 is
  the cold-open composer; the audit requires a `<world-language hello>, Liam`
  greeting there, not the your-turn handoff cue. Adjacent nbb reels used
  Vanakkam / Bonjour / Namaste — Konnichiwa is unused in the immediate run.
- `BHTF.props.greeting`: already `"Your turn."` — kept.

### Placeholder card fixes (display only)

- `B01`: was `FormBCard` with three placeholder items (`"Key point one"`,
  `"Key point two"`, `"Key point three"`) and empty subs. Simplified to
  `shot.type=CARD` / `card.kind=title` — matches the pattern the sibling
  `nbb-vox-batch-distribution` reel uses for its title bookend. No content
  invented — copy/sub taken verbatim from the reel's own title.
- `B02`, `B11`: were `STILL` beats with a stray embedded `FormACard` whose
  `lines` were mid-sentence narration truncations
  (`"The particle was elegant — a polymeric nanoparticle with a targeting…"`,
  `"Building delivery measurement into the trial — an imaging tracer cohort,…"`).
  Removed the vestigial `shot.remotion` FormACard from both — a STILL beat
  renders as an image (via the AI-still slot), not as a text card. The
  narration is spoken; the still speaks the picture.

### Verdict authored (BVDT artifactLines)

Incoming NBB01 artifactLines were four mid-sentence truncations that would
render with ellipses. Verdict body is 13 beats / ~213 spoken seconds — well
past the 5-beat / 180-word threshold for an authored verdict. New
`artifactLines`, drawn from the body's own nouns and structure:

    - "Response-only endpoints report failure without diagnosis."
    - "Three failure modes look identical on a binary readout."
    - "Delivery, payload, biology — each demands a different fix."
    - "A tracer cohort converts a negative into a diagnosable result."

`artifactHeading` set to `"Why the trial couldn't diagnose itself"` (was:
truncation of the title).

### Dead ElevenLabs-era fields dropped

- `modelLabel: "Fable 5"` and `effortLabel: "High"` on the ClaudeComposerAsk
  bookends (both B00 and BHTF). These are dead fields from an older Anthropic
  UI screenshot and were being carried forward for no reason. Dropped.

### Audio (VOICE-LOCK)

Fresh Kokoro generation for every beat, `voice=am_onyx`, VOICE-LOCK compliant.
Measured `actual_duration_s` written back to the sheet as the clock. Total
spoken length: 239.5 s.

## Datable-claim edits

None. The narration contains no model names, prices, versions, or "as of"
phrasing that has rotted since the source was written.

## Body-beat rendering plan

Body beats B02–B13 carry `shot.type` of GRAPHIC / STILL / DOCUMENT / CARD but
no `shot.remotion.pattern` — those render as author-slates in this review-slate
cut. Each beat's `production_viz` (mechanic + colors) and `graphic.manim`
scene id remain authored intents; a future full-render pass will draw them.

## Envelope preserved

`metadata.source_reel` and `metadata.source_video` unchanged — pointer to the
original vox cut is preserved for provenance.
