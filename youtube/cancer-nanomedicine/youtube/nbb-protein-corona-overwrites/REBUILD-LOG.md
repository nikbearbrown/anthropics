# REBUILD-LOG.md — nbb-protein-corona-overwrites

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.
Pattern mirrors sibling `nbb-lnp-endosomal-escape` (Liam Claude wrapper of a Nik Bear Brown source reel), 2026-08-30.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-30 before any edit (22,868 B).

## LOCKED (unchanged from pre-rebuild or source reel)

- Body B01–B08 `narration_text` — verbatim from pre-rebuild sheet.
- Body B02 (`NikBearBrownTerminalAsk` claude command), B03 (`NikBearBrownCodeBlock` code), B04 (Manim intent), B05 (`NikBearBrownTerminalAsk` claude command) — verbatim.
- Wrapper narration verbatim from pre-rebuild `NBB01` recap prose ("Let's recap with Claude…" + summary content) → now voiced by `BVDT`.
- Metadata identity: title, slug, topic, register, palette, source pointer.

## REBUILT (regenerated per doctrine)

1. **Voice envelope** — `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx` stamped on metadata + every beat. Dropped legacy `body_beats`/`body_duration_s`/`old_outro_beats` metadata (redundant with beats array).
2. **Bookend surgery** (matches nbb-lnp-endosomal-escape rebuild §2):
   - `NBB00` → `B00` (Liam ClaudeComposerAsk cold open).
   - `NBB01` → `BVDT` (Liam ClaudeVerdictArtifact).
   - `NBB02` → `BHTF` (Liam ClaudeComposerAsk your-turn).
   - `NBB03` → `BOUT` (Liam ClaudeTitleOutro).
   - Dropped the empty placeholder `BVDT/BHTF/BOUT` scaffolds at the tail (they had `narration_text: ""` and placeholder `Key finding one/two/three` verdict lines, template-bracket `Take what you learned from [...]` your-turn command, and empty outro subline).
   - Dropped source `B00` (`NikBearBrownOpen`; "Nik Bear Brown. The body overwrites your design in thirty seconds.") — the Liam ClaudeComposerAsk cold open now plays the opening role, per lnp pattern.
3. **Body clip + mp3 inheritance** — copied `../protein-corona-overwrites/clips/{B01..B08}.mp4` → `media/{B01..B08}.mp4` and `../protein-corona-overwrites/mp3/beat-{B01..B08}.mp3` → `mp3/beat-{B01..B08}.mp3`. Parent reel is a fully-rendered Cohort-A build; using its measured clips/audio directly preserves the locked shot list.
4. **Body FormBCard authoring** — pre-rebuild B01 had placeholder `Key point one/two/three` labels with empty `sub` strings; B06/B07/B08 had `shot.source: null` slate holes. Authored real FormBCards from each beat's own narration (nouns, numbers):
   - B01 "The 30-Second Overwrite" — months of engineering, 30-second overwrite, two different particles.
   - B06 "Two Strategies, One Ceiling" — albumin pre-coat, apoA-I pre-coat, zwitterionic surfaces.
   - B07 "The Corona Is the Product" — body's first-pass editing, decade of fighting, design WITH it.
   - B08 "Your Move — Three Benchtop Checks" — DLS in 50% serum, zeta potential, competitive binding.
5. **Kokoro audio regeneration (4 bookends)** — `beat-NBB00.mp3` old was 5.78 s against 90+ words (impossible pacing, ~15 wps); regenerated as `beat-B00.mp3`. `BVDT` narration expanded from pre-rebuild NBB01 (added Vroman C3 line and zwitterionic clinical status), regenerated. `BHTF` narration rewritten to match the specific rubric-bearing prompt (was the generic "pick any cancer type" ask), regenerated. `BOUT` = title only, regenerated. Body B01–B08 mp3s inherited from source (already measured against locked narration).
6. **Spark line fix** — B00 `props.greeting` was `"Your turn."` (that slot belongs to BHTF; B00 cold-open needs a world-language hello). Set to `"Salaam, Liam."` (Arabic peace, 2 words) — not adjacent-reel duplicate (nearby nbb reels use "Sawubona, Liam.", "Bonjour, Liam", "Namaste, Liam.", "Olá, Liam", "Konnichiwa, Liam", "Annyeong, Liam", "Vanakkam, Liam", "Ni hao, Liam", "Kia ora, Liam"; the closest topical neighbor `nbb-vox-protein-corona` uses "Ni hao"). BHTF greeting `"Your turn."` retained.
7. **Verdict artifact lines (BVDT)** — placeholder truncated body-sentence ellipsis fragments (`"Pre-coating with albumin reduces but does not eliminate corona formation — and the albu…"`, etc.) REPLACED with four real verdict lines authored from body nouns/numbers:
   - "Serum overwrites design in 30 s — Vroman succession albumin → apoE → C3."
   - "The macrophage sees the corona, not your ligands — MPS clearance follows."
   - "Zwitterionic: ~90% in vitro, ~50% in vivo, zero phase-2 hits."
   - "Escape: design WITH the corona — apoA-I coat routes to hepatocytes."
   `artifactHeading` `"Research the Protein Corona: How the Body Immediately"` (mid-sentence truncated title) → `"protein corona: your design meets biology"` (matches lnp `"lnp escape: 1–2% is the floor, not the ceiling"` pattern).
8. **BHTF (your-turn) command** — old command was the generic bracketed-title ask-Claude-about-your-case template (`Explain how [Research the Protein Corona: How the Body Immediately Overwrites Your ] applies to a specific cancer type…` — a placeholder wearing brackets, mid-word truncated). Replaced with a specific rubric-bearing prompt drawn from B08's next-steps content (`Pick a nanoparticle you're studying. Look up: (1) its surface chemistry; (2) its PEG density; (3) any published in-vivo half-life…`) plus an evaluation rubric that requires naming, predicting three specific corona proteins, and stating one falsifiable prediction with the DLS/zeta refutation criterion. Narration rewritten (33 words) to match the more specific prompt.
9. **BOUT subline** — the old had NO subline (only title). Added `"The corona is the product — design with it, not against it."` (verdict headline, matches lnp pattern). Added `"handle": "@NikBearBrown"`.
10. **Fable-5 labels dropped** — `modelLabel: "Fable 5"` / `effortLabel: "High"` removed from ClaudeComposerAsk props on B00 and BHTF. Same rationale as lnp §10 / nano-char §9: this is a Kokoro nbb reel, not a Claude model-branded cut.

## Datable-claim edits

None to narration text. All quantitative claims (30-second overwrite, ~90% in vitro / ~50% in vivo zwitterionic reduction, apoA-I hepatocyte routing, Vroman-effect protein sequence albumin → apolipoprotein → complement C3, DLS >30 nm hard-corona threshold) are drawn from the source-reel FACTCHECK.md and remain valid.

## Dropped fields

- Metadata: `body_beats`, `body_duration_s`, `old_outro_beats` (redundant with beats array).
- Every wrapper beat: legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` from `ClaudeComposerAsk` props (nbb Kokoro reel, not Claude-branded).
- Old empty `BVDT/BHTF/BOUT` scaffolds at end of beats array (empty `narration_text`, placeholder `Key finding one/two/three` verdict lines, template-bracket your-turn command).
- Source `B00` (`NikBearBrownOpen`; "Nik Bear Brown. The body overwrites your design in thirty seconds.") beat entry — replaced by Liam ClaudeComposerAsk wrapper bookend per nbb-lnp pattern.
- Legacy `source_clip`/`source_audio` pointers per beat — parent reel clips now live in `media/` locally; the pointers are redundant.
- Legacy `locked: true` flags per body beat (the narration lock is enforced by the rebuild contract, not by a per-beat field).
- Stale `NBB01.lead_silence_s: 0.5` (not carried; audio-first pacing handles this).
- Stale `NBB03.silent: true` / `silence_s: 6.0` (BOUT now speaks the title line, matches lnp pattern).

## Reel-level notes

- Persona coherence: Liam narrates the wrapper (`am_onyx` speaking Claude cold-open / verdict / your-turn / outro cards); Bear's body narration is voiced by the same `am_onyx` engine here (parent reel is a Kokoro-am_onyx cut, no separate Bear recording exists). Skin does the persona work — ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro for Liam, NikBearBrownTerminalAsk / NikBearBrownCodeBlock / FormBCard for Bear's body.
