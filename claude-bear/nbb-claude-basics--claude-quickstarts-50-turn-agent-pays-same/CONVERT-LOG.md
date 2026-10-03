# CONVERT-LOG — nbb cut

Source: `claude-bear/claude-basics--claude-quickstarts-50-turn-agent-pays-same/beat_sheet.json` (hai-simple, Plain register)
Target: this dir · `beat_sheet.nbb.json` (Teardown register, Liam am_onyx)

## What changed

- **Narration on every beat rewritten in Teardown register.** Feynman × MKBHD:
  "here's what's actually happening", "they optimized for X at the expense of
  Y", "this works if you value X; it fails if you need Y". Voice only —
  every number, API name, and file-level fact intact (50 turns, 5 states,
  2,000 tokens/screenshot, 100,000 → 10,000 tokens, `cache_control` /
  `{"type":"ephemeral"}`).
- **BHTF converted to the LLM EXERCISE beat** (second-to-last). Same
  ClaudeComposerAsk visual (kept — it's the correct "paste this into a
  frontier LLM" scene). `act` renamed to `LLM EXERCISE`. Added the
  `llm_exercise` block with a paste-ready `prompt` and a
  `dig_deeper` follow-up on similarity-aware caching over exact-hash caching.
  Narration extended to read the dig-deeper line out loud, so viewers hear
  the follow-up even if they don't pause on the card.
- **Outro consolidated to one beat (BOUT).** Dropped the original
  `BOUTCTA` (`OutroCTA` with `humanitarians.ai` / `@HumanitariansAI`) and
  merged it into `BOUT`, now the single last beat with NikBearBrown
  content per `AUTHOR.MD :: NikBearBrown` — `line: "Find more at
  nikbearbrown.com"`, `handle: "@NikBearBrown"`, `folderLabel` on the
  BHTF composer also swapped to `@NikBearBrown`. Kept `OutroCTA`
  (not `OutroSeries`) — matches the working `nbb-claude-basics--
  screenshot-prompt-caching` sample in the same book and gives a clean
  single-beat close.
- **`_variant_todo` removed** from metadata (all five items addressed).

## Judgment calls

- **Kept `channel`/`channel_title`/`folderLabel` metadata as `@HumanitariansAI`.**
  These trace the source reel's provenance; the scaffold didn't touch them and
  the SKILL.md doesn't call for a change. The visible outro handle (`@NikBearBrown`)
  and the composer folderLabel on the LLM exercise beat (`@NikBearBrown`) are
  what the viewer actually sees — those are aligned to NBB.
- **Kept the `FormBCard` `label:` values largely intact** on S01–S07 —
  they're tight, factual, and already fit the Teardown register. Rewrote
  the `sub:` fields where they echoed the source narration verbatim, so
  the on-card prose stays in step with the new narration without duplicating
  entire sentences.
- **Beat count 12 → 11.** The consolidation drops one outro beat; every
  other id (B00, S01–S07, BCRY, BHTF, BOUT) survives. `metadata.build.filled`
  / `of` left at `12` — they are the source's build snapshot, not a live
  count of the new sheet, and this pass does not render.
- **Estimated durations bumped** on the beats whose narration got longer
  (B00, S01, S02, S03, S04, S05, S06, S07, BCRY, BHTF). These are advisory
  only; the audio pass will overwrite `actual_duration_s` from measured
  MP3s and is the master clock.

## Voice

Kokoro `am_onyx` — Liam, in for Bear. No paid engine; ElevenLabs is gone.
`engine` and `voice_kokoro` left exactly as the scaffold set them.
