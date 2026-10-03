# REBUILD-LOG.md — nbb-vox-bystander-effect

Rebuild ran under `skills/make/rebuild/SKILL.md`.

## Locked (verbatim carry-over)
- `narration_text` for all body beats B01..B11 — the July-16 script (26–47 words each, ink-clean prose).
- Beat order and act structure (B00 cold open · B01..B11 body · BVDT verdict · BHTF your-turn · BOUT title outro).
- Shot INTENT per beat: Manim `scene_class` names, still `image_description`, GRAPHIC/DOCUMENT/CARD types — all preserved.
- Metadata identity: title, slug, topic, source pointer, `body_duration_s`.
- Bookend narrations (kokoro mp3 already existed) — kept verbatim, only `props` metadata swapped.

## Rebuilt
1. **Voice envelope** — engine `kokoro`, voice `am_onyx` stamped on metadata + every beat. Legacy ElevenLabs body mp3 references (`../vox-bystander-effect/mp3/beat-B0X.mp3`) will be REPLACED with fresh local Kokoro renders (24 kHz) at `mp3/beat-B0X.mp3` in Phase 2. `actual_duration_s` will be re-measured from the new mp3s after regen.
2. **Bookends** — dropped the empty scaffold beats (`B00`, `BVDT`, `BHTF`, `BOUT` with `narration_text: ""` and `Key finding one/two/three` placeholder verdict lines) that duplicated the already-authored `NBB00`-`NBB03` set. Renamed the filled NBB set to canonical ids so the sheet has exactly one authoritative bookend at each slot.
3. **Verdict (BVDT)** — placeholder `Key finding one/two/three` + placeholder heading `Key findings` replaced by a three-line verdict built from body nouns and numbers, plus a specific heading (`bystander effect: the payload, not the antibody`).
4. **Spark lines** — `B00.greeting = "Konnichiwa, Liam"` (world-language hello; rotated across the batch — abraxane=Portuguese, nanoparticle-char=Hindi, light-ceiling=Maori, none had Japanese); `BHTF.greeting = "Your turn."`; segments normalized to `"bystander effect · T-DXd vs T-DM1"` (was mid-word truncation `"Why Two Identical Anti-HER2 Drugs Kill Completely…"`).
5. **Card content (B01)** — placeholder FormBCard items (`Key point one / two / three` with empty `sub`) replaced with real ones drawn from the body: the patient (HER2-low breast cancer), the paradox (one approved, one not), the clue (identical antibody).
6. **BOUT subline** — placeholder `"that is why t-dxd, not t-dm1, treats her2-low breast cancer"` (all lowercase, echoed B11 verbatim) replaced with a compressed tag `"same antibody — different payload, different tumor"`.
7. **Fable-5 labels dropped** — `modelLabel: "Fable 5"` / `effortLabel: "High"` removed from bookends: this is an nbb Kokoro reel, not a Claude model-branded cut.

## Datable-claim edits
- None. The body's numbers ("five HER2-positive cells", "roughly forty surrounding cells", "eight times more kills") are mechanism illustrations, not versioned figures. No model / tool version strings, no dated prices.

## Dropped fields
- Every body beat: `source_audio`, `source_clip` (ElevenLabs-era pointer into `../vox-bystander-effect/mp3/` and `../vox-bystander-effect/clips/` — the clips never existed as per-beat mp4s).
- Body beats: `actual_duration_s` values reflect legacy ElevenLabs measurement; will be re-measured after Kokoro regen.
- Metadata: `body_beats`, `old_outro_beats` (redundant with the beats array).
- Bookends: `modelLabel`, `effortLabel`.

## Renamed
- `NBB00` → `B00` (cold-open ClaudeComposerAsk)
- `NBB01` → `BVDT` (verdict ClaudeVerdictArtifact)
- `NBB02` → `BHTF` (your-turn ClaudeComposerAsk)
- `NBB03` → `BOUT` (title outro ClaudeTitleOutro)
- `mp3/beat-NBB0X.mp3` renamed on disk to match new ids.
