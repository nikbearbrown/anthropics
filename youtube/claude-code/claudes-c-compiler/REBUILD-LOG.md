# REBUILD-LOG.md — claudes-c-compiler

Rebuild pass, 2026-08-31. Rebuild contract in `brutalist-art/skills/make/rebuild/SKILL.md`.

## Locked (verbatim from `beat_sheet.pre-rebuild.json`)

- Narration for B00, B01, B02, B03, B04 — unchanged.
- Beat order for B00 → B04 (cold open + four body beats) and their `shot.remotion.pattern` assignments (ClaudeComposerAsk, ClaudeVerdictArtifact ×4).
- Metadata identity: slug, title, topic, source, register, palette, channel.

## Rebuilt

1. **VOICE-LOCK envelope.** Every beat now carries `engine=kokoro`, `voice=am_onyx`, `voice_kokoro=am_onyx` where applicable. No ElevenLabs-era `voice_id`, `voice_env`, or dead `clock` prose was present in the pre-rebuild sheet.
2. **`metadata.channel_title`** added (`@NikBearBrown`) so bookend_check reads the expected outro handle explicitly instead of falling back to its default.
3. **Cold open (B00).** Greeting was `"Your turn."` (the handoff greeting used in the wrong slot). Changed to `"Namaste, Liam"` — one-word lexicon entry, not repeated by adjacent claude-code reels. Narration unchanged.
4. **Closing block — new writing (per rebuild §5).**
   - **BVDT** (verdict): authored real `artifactHeading`, four real `artifactLines`, and ~40 words of narration from the body's own nouns and numbers. Replaced the "Key finding one/two/three" placeholder.
   - **BHTF** (your turn): replaced the seeded "Take what you learned from [X] and apply it to your own work." template with a concrete exercise built from B02's methodology (viewer writes tests for a small library they own, feeds only "tests still fail" to Claude, logs the tests Claude can't satisfy). Narration reads the prompt aloud and discusses what to watch for.
   - **BOUT** (outro): 6-word title restate + IN-FOR-BEAR sign-off ("Claude Wrote a C Compiler. Liam, in for Bear."). Handle/title/subline conform to `bookend_check` (`@NikBearBrown` / matches metadata.title / no subline).
5. **Duplicate bookends removed.** Pre-rebuild sheet carried BOTH the reel's original bookends (B00 / YOURTURN / B06) AND scaffolded canonical bookends (BVDT / BHTF / BOUT) — appended with empty narration, so the reel would have played ~48 s of silent slate cards after the title outro. Deleted YOURTURN and old B06; the new BHTF and BOUT (fresh audio + real content) take those roles. The unreferenced `beat-B05.mp3` and `beat-B06.mp3` remain on disk but no beat references them.
6. **Audio.** Fresh Kokoro `am_onyx` for BVDT (13.48 s), BHTF (20.37 s), BOUT (3.52 s). B00–B04 mp3s reused (narration unchanged). `mp3/timings.json` and `beat.actual_duration_s` reflect measured durations for every beat.
7. **Renders.** Remotion project renders each beat's declared pattern; no beat leaves the pipeline as a slate.
8. **Gates.** AUDIT.md written (Phase 1 checklist); Gate V frame sample after compile.

## Datable claims

None edited. B00's cold-open output line names "Claude Opus" — the original sheet said "Fable 5" (a scaffolder placeholder / fictional model, per FILMLOOP audit convention for unknown model names). Corrected in the composer's `modelLabel` and `output` to "Claude Opus" (the model Zack Witten's build used; Anthropic engineering post on `anthropic.com/engineering/building-c-compiler` credits Opus). No source-of-record change beyond aligning with the DOUBLE-CHECK LAW.

Old → New: `"modelLabel": "Fable 5"` → `"modelLabel": "Claude Opus"`. Source: Anthropic engineering blog post referenced in metadata.source.

## Not rebuilt (out of scope for a rebuild pass)

- **All-card body (check 7).** B01–B04 are four ClaudeVerdictArtifact pages by original design. A real diagram beat for B01 (six compiler stages) would be a design improvement, but the rebuild contract locks the shot list. Logged in `AUDIT.md` §7 as a follow-up for a designed-from-scratch pass, not this loop.
