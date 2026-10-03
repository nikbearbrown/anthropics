# CONVERT-LOG — nbb-financial-services--claude-liam-ic-memo

Source: `../financial-services--claude-liam-ic-memo/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Register: HAI Plain → **Teardown** (Feynman × MKBHD)
Voice: Kokoro `am_onyx` — Liam, in for Bear (unchanged; scaffold set this)
Date: 2026-09-03

## What changed

- **Rewrote every narration** (7 beats: B00, B01, B02, B03, BCRY, BHTF, BOUT)
  into the Teardown register per `runtime/prose/teardown/PROSE.md` +
  `brands/nbb.md`. Each beat now takes the piece apart, explains the machinery,
  and names the design trade-off:
  - B00 — cold open contrasts the "app" surface with the "skill" mechanism
    (folder Claude reads before it acts); IN-FOR-BEAR sign-in.
  - B01 — anatomy names the choice: legibility over cleverness (one plain
    2k SKILL.md, no hidden runtime).
  - B02 — pipeline names the trade: linear execution over inference (loses
    mid-run cleverness, gains pre-run predictability).
  - B03 — mechanism + scope names the trade: repeatable/auditable draft
    fails the moment the deal needs a section the SKILL.md doesn't name.
  - BHTF — enhanced into the LLM-exercise beat (see below).
  - BOUT — swapped to the NikBearBrown outro (see below).
- **BCRY narration kept verbatim.** The carry-out sentence — "A Skill doesn't
  make Claude smarter — it makes Claude follow your steps, in order, every
  time." — already reads Teardown (names what a skill actually does vs what
  the marketing implies), and it IS the on-screen `WantQuote.quote`, which
  SKILL requires be preserved. `sparkLine "Steps, not smarts."` also already
  Teardown; left alone.
- **BHTF enhanced into the LLM-exercise beat in place.** Added an
  `llm_exercise` block (`prompt` + `dig_deeper`), folded a "Go deeper"
  question into the narration, updated
  `ClaudeComposerAsk.runningText` to `"paste this into Claude, ChatGPT, or
  Gemini…"` (SKILL §Step 3 requires paste-into-any-frontier-LLM, not CLI),
  and rewrote `ClaudeComposerAsk.command` to match the new
  `llm_exercise.prompt`. `folderLabel` on the composer flipped to
  `@NikBearBrown` to match the new brand.
- **BOUT swapped to the NikBearBrown outro.** Pattern changed from
  `OutroSeries` to `OutroCTA`; `handle: "@NikBearBrown"`; line now names
  Nik Bear Brown + `nikbearbrown.com` (per
  `anthropics/youtube/ai-1/AUTHOR.MD :: Nik Bear Brown`), followed by the
  IN-FOR-BEAR sign-off. `act` renamed to `"outro — NikBearBrown"`.
- **Metadata:** `brand` → `nbb`; `channel` / `channel_title` /
  `folderLabel` → `@NikBearBrown`; `skill` → `nbb`; `purpose` rewritten to
  describe the Teardown cut; `source_register` corrected to `Plain`
  (matches the source sheet's actual register); `source_sheet` corrected
  to the local absolute path. Scaffold-set fields (`audience`, `register`,
  `palette`, `engine`, `voice_kokoro`, `typography`, `derived_from`,
  `outro_source`) left as the scaffold wrote them.
- **`_variant_todo` removed** — all four items done.

## Judgement calls

- **Enhanced BHTF, did not insert a new B_LLM beat.** The source already
  ended with a `your turn handoff` beat whose `ClaudeComposerAsk` is a
  paste-ready prompt — functionally the LLM exercise. SKILL §Step 3 says
  "insert one beat before the outro"; adding a second prompt beat would
  duplicate the same handoff. Kept `beat_id "BHTF"` and `act "your turn
  handoff"` (SKILL: "Preserve exactly: every beat_id … act structure"),
  added the `llm_exercise` structure §Step 3 requires, and left BHTF in
  the second-to-last slot. Same call as the reference reel
  `nbb-claude-for-legal--claude-liam-memo`.
- **Kept the `ClaudeComposerAsk` shot for the LLM beat** instead of
  swapping to the `type: "CARD"` shot §Step 3's schema example shows. The
  composer scene already renders the paste-ready prompt on-screen, which
  is stronger than a plain card for this beat.
- **Left B00 hesitation prop copy alone.** `text` reads "How does the /
  ic-memo app / write our memo?" with `triggerWords: "app"` → `skill`. The
  whole point of the shot IS the correction from surface to mechanism —
  SKILL says preserve on-screen card copy that still fits the register,
  and this one is Teardown by construction.
- **Left shot-block colors alone.** `bg: "#F3EBDD"` on the Hesitant Writer
  and `ground` in metadata still carry the cream/warm ground from the
  source, even though `palette` metadata is now `teardown`. SKILL:
  "Preserve exactly … shot blocks." Any palette remap is a render-time
  concern, not a register-conversion one.
- **Bumped `estimated_duration_s` on the four beats whose narration grew**
  (B00 14→16, B01 15→22, B02 10→18, B03 21→26, BHTF 22→32) to keep the
  ledger honest; the compiled clock will be measured Kokoro audio anyway.

## Not done (out of scope)

Audio, deck, or compile — the supervisor runs a separate pass. This
deliverable is `beat_sheet.nbb.json` only.
