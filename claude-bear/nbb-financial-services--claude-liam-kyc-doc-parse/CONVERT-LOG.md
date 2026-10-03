# CONVERT-LOG — nbb-financial-services--claude-liam-kyc-doc-parse

Source: `../financial-services--claude-liam-kyc-doc-parse/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Register: HAI Plain → **Teardown** (Feynman × MKBHD)
Voice: Kokoro `am_onyx` — Liam, in for Bear (unchanged; scaffold set this)
Date: 2026-09-03

## What changed

- **Rewrote every narration** (7 beats: B00, B01, B02, B03, BCRY, BHTF, BOUT)
  in the Teardown register per `runtime/prose/teardown/PROSE.md` +
  `brands/nbb.md`. Each beat now takes the piece apart, explains the machinery,
  and names the design trade-off. Facts unchanged (skill name, the five fields,
  the wrong-guess, missing-vs-flagged, downstream rules engine, determinism).
  - B00 — cold open contrasts the "approves" surface with the "extractor"
    mechanism; approving happens somewhere else. IN-FOR-BEAR sign-in.
    Kept the 20–35-word TIMING LAW window (34 words).
  - B01 — names the choice: extraction fidelity over judgment (the skill
    will never invent what isn't there, and never decide what isn't its job).
  - B02 — names the split: parsing is deterministic and auditable in the
    skill; deciding lives in the rules engine, where the rule is readable
    and changeable.
  - B03 — anchor payoff plus both-directions plus the works-if / fails-when
    verdict: works if you value repeatability; fails the moment you were
    hoping the skill itself would tell you the client is clean.
  - BHTF — enhanced in place into the LLM-exercise beat (see below).
  - BOUT — swapped to the NikBearBrown outro (see below).
- **BCRY narration kept verbatim.** The carry-out sentence — "kyc-doc-parse
  doesn't decide whether a client passes KYC — it turns a messy onboarding
  packet into five structured fields a rules engine can actually screen. A
  complete parse means the fields were captured, not that the client was
  cleared." — already reads Teardown (mechanism + design verdict in one
  breath), and it IS the on-screen `WantQuote.quote`, which the SKILL requires
  be preserved. `sparkLine "Captured, not cleared."` also already Teardown;
  left alone. Also hoisted the carry-out into `metadata.carry_out` to match
  the ic-memo pattern.
- **BHTF enhanced into the LLM-exercise beat in place.** Added an
  `llm_exercise` block (`prompt` + `dig_deeper`), folded a "Go deeper"
  question into the narration, rewrote `ClaudeComposerAsk.command` to match
  the new `llm_exercise.prompt`, and changed `runningText` to
  `"paste this into Claude, ChatGPT, or Gemini…"` (SKILL §Step 3 requires
  paste-into-any-frontier-LLM, not CLI). `folderLabel` flipped to
  `@NikBearBrown`; added `modelLabel: "Opus 4.8"` and `effortLabel: "High"`
  to match the ic-memo reference. The prompt produces useful output on its
  own — it asks the model to sort a document into five fields, quote source
  text per field, and write MISSING rather than guess — which is the whole
  extract-vs-decide split the video teaches.
- **BOUT swapped to the NikBearBrown outro.** Pattern stayed `OutroCTA`;
  `handle` → `@NikBearBrown`; line now names Nik Bear Brown +
  `nikbearbrown.com` (per `anthropics/youtube/ai-1/AUTHOR.MD :: Nik Bear
  Brown`), followed by the IN-FOR-BEAR sign-off. `act` renamed to
  `"outro — NikBearBrown"`. Narration reads the domain as "nikbearbrown dot
  com" so Kokoro speaks it as a domain, not a URL literal.
- **Metadata:** `brand` → `nbb`; `skill` → `nbb`; `channel_title` /
  `folderLabel` → `@NikBearBrown`; added `channel: "@NikBearBrown"` and
  `modelLabel: "Opus 4.8"` for consistency with the ic-memo NBB reference;
  `style_preset` → `claude`; `purpose` rewritten to describe the Teardown
  cut; `source_register` added as `Plain` (matches the source sheet's actual
  register); `source_sheet` corrected to the local absolute path;
  `source_note` amended to describe Plain → Teardown (was Teardown → Plain
  in the source). Scaffold-set fields (`audience`, `register`, `palette`,
  `engine`, `voice_kokoro`, `typography`, `derived_from`, `outro_source`)
  left as the scaffold wrote them.
- **`_variant_todo` removed** — all items done.

## Judgement calls

- **Enhanced BHTF, did not insert a new B_LLM beat.** The source already
  ended with a `your turn handoff` beat whose `ClaudeComposerAsk` is a
  paste-ready prompt — functionally the LLM exercise. SKILL §Step 3 says
  "insert one beat before the outro"; adding a second prompt beat would
  duplicate the same handoff. Kept `beat_id "BHTF"` and `act "your turn
  handoff"` (SKILL: "Preserve exactly: every beat_id … act structure"),
  added the `llm_exercise` structure §Step 3 requires, and left BHTF in
  the second-to-last slot. Same call as the reference reel
  `nbb-financial-services--claude-liam-ic-memo`.
- **Kept the `ClaudeComposerAsk` shot for the LLM beat** instead of
  swapping to the `type: "CARD"` shot §Step 3's schema example shows. The
  composer scene already renders the paste-ready prompt on-screen, which
  is stronger than a plain card for this beat, and it matches the ic-memo
  reference.
- **Left B00 hesitation prop copy alone.** `text` reads "What does the
  skill / do with a KYC packet — / approve it?" with `triggerWords:
  "approve"` → `parse it into fields`. The whole point of the shot IS the
  correction from surface to mechanism — SKILL says preserve on-screen
  card copy that still fits the register, and this one is Teardown by
  construction.
- **Left shot-block colors, `ground`, and Manim scene bindings alone.**
  `bg: "#F3EBDD"` on the Hesitant Writer and `ground` in metadata still
  carry the cream/warm ground from the source, and B01/B02/B03 still point
  at the existing `KDB0[123]Scene` Manim scenes rendered under the source
  reel. SKILL: "Preserve exactly … shot blocks." Any palette remap and any
  Manim re-render is a build-pass concern, not a register-conversion one.
- **Bumped `estimated_duration_s`** on beats whose narration grew — B00
  13→14, B01 25→34, B02 22→30, B03 23→36, BHTF 24→44, BOUT 6→9 — to keep
  the ledger honest. The compiled clock will be measured Kokoro audio
  anyway (the supervisor's build pass).

## Not done (out of scope)

Audio, deck, or compile — the supervisor runs a separate pass. This
deliverable is `beat_sheet.nbb.json` only.
