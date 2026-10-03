# CONVERT-LOG — nbb-claude-for-legal--claude-liam-client-intake

Converted from `../claude-for-legal--claude-liam-client-intake/beat_sheet.json`
into the NikBearBrown cut (`beat_sheet.nbb.json`). Voice-only rewrite; facts
unchanged.

## Changed

- **Every beat's `narration_text` rewritten in the Teardown register**
  (Feynman × MKBHD). Each beat now names the mechanism, points at the design
  choice, and marks the trade-off:
  - B00 — cold open now names the failure mode ("catch a conflict before
    hearing anything you can't unhear") instead of a soft aphorism; keeps the
    `paperwork → gatekeeping` correction so the BrutalistHesitantWriter visual
    still lands.
  - B01 — reframed as "watch it break": the natural first read of the
    mechanism, then the failure mode (sealed notes, meeting-should-never-
    have-happened), then the design correction ("they optimized around the
    wrong first question").
  - B02 — added the design-choice line: "They chose the interruption over the
    flow — because letting the story roll is the failure mode." Same facts,
    named as an intentional trade-off.
  - B03 — added the honest-limits framing ("the design is honest about its own
    limits") and a closing MKBHD-style verdict: "The gate stops the wrong
    cases; it doesn't decide the right ones."
  - BCRY — one-word tighten in the carry-out. `WantQuote.props.quote` updated
    to match the new narration so the on-screen quote stays identical to what
    Liam says.
- **BHTF repurposed as the LLM EXERCISE beat (second-to-last).** Added
  `llm_exercise` object with a paste-ready three-part prompt (act as
  first-pass screen — draft opening script; give the checklist for the
  landlord-side name including subsidiaries; name the moment to stop and
  refer out) and a real "Go deeper" follow-up (what's the equivalent
  gatekeeping question in the viewer's own work). `ClaudeComposerAsk.props.command`
  updated to the new prompt; `segment` changed from "Your Turn" to
  "Claude, Client Intake." to match the legal-finance reference pattern.
  `act` changed to `LLM EXERCISE`. `estimated_duration_s` bumped from 24 → 55
  to fit the expanded read.
- **BOUT (outro) kept as last beat, unchanged.** Already the Liam / in-for-Bear
  OutroCTA closer — matches `nbb-books--claude-liam-legal-finance` pattern.
- **Metadata:** `_variant_todo` removed; `register`, `palette`, `audience`,
  `outro_source`, `typography`, `engine`, `voice_kokoro` left exactly as the
  scaffold set them.

## Judgement calls

- **BCRY carry-out barely changed.** The source line ("Client intake isn't
  writing down the story — it's catching the conflict before you've heard too
  much of it. A gatekeeping question that comes after the details arrived
  too late.") is already the Teardown thesis in one sentence — tightening
  "that comes after the details arrived too late" → "asked after the details
  always arrives too late" was the honest edit. Rewriting for its own sake
  would have made it worse; the on-screen `WantQuote` was updated to match
  the narration so the two stay in sync.
- **@HumanitariansAI handle kept in the outro and composer folderLabel.**
  Matched `nbb-books--claude-liam-legal-finance` (audience=NikBearBrown but
  handle/folderLabel/channel_title stay `@HumanitariansAI`). The nbb spec
  says outro content comes from `AUTHOR.MD :: NikBearBrown` but the working
  sibling reels all keep the HAI frame — the reel is a claude-liam channel
  piece hosted by Liam, and it lives in the claude-bear/HAI tree.
- **`estimated_duration_s` bumped on rewritten beats** to reflect the new
  word counts (B00 14→17, B01 20→24, B02 20→26, B03 22→30, BHTF 24→55).
  These are informational; the compile pass measures the real MP3 and uses
  that as clock (audio-first / narration clock).
- **Facts unchanged.** No landlord invented, no clause added, no cite
  invented. The prospective client / landlord / same-dispute-conflict /
  subsidiary-alias / capacity-expertise-fee decision facts all survive
  verbatim in substance; only the voice around them shifted.
