# CONVERT-LOG — nbb-claude-for-legal--claude-liam-matter-intake

Converted from `../claude-for-legal--claude-liam-matter-intake/beat_sheet.json`
into the NikBearBrown cut (`beat_sheet.nbb.json`). Voice-only rewrite; facts
unchanged.

## Changed

- **Every beat's `narration_text` rewritten in the Teardown register**
  (Feynman × MKBHD). Each beat now names the mechanism, points at the design
  choice, and marks the trade-off:
  - **B00** (cold open) — reframed as "misreads the machinery / the actual job
    is narrower" and added the Liam-in-for-Bear "let's take it apart" tag, in
    the same pattern as `nbb-…-client-intake` / `-legal-finance`. Keeps the
    `decide → log` correction so the BrutalistHesitantWriter typing beat still
    lands on the same visual pivot.
  - **B01** (stakes) — reframed as "here's the natural first read of the name"
    and pulled apart the two words that mislead ("intake" implies a gate,
    "skill" implies judgment; combined they suggest AI that picks the cases).
    Same claim as the source; explanation of *why* the wrong read is natural.
  - **B02** (wrong guess, broken) — "now watch it break": feed the skill an
    obvious conflict, see it complete unchanged, close on the MKBHD-style
    verdict "what looked like a gate is a form." Facts identical.
  - **B03** (ANCHOR PLANTED) — same nine questions in the same order, added
    the design-choice line "they optimized for uniformity at the expense of
    cleverness: no branching, no skipping, no matter-type-specific detours."
    The list is preserved verbatim so B06 can call the anchor back.
  - **B04** (mechanism) — kept every named artifact (SKILL.md, matter.md,
    history.md, _log.yaml) and the "no branching, top to bottom" claim; added
    the one-line semantics of each file (matter.md = human summary,
    history.md = interview transcript, _log.yaml = machine-readable index).
    Facts preserved; jargon stripped.
  - **B05** (payoff + limit) — kept the payoff/limit framing from source, ended
    on the explicit Teardown formula "this works if you value X; it fails if
    you need Y." — auditability vs. AI-does-the-picking.
  - **B06** (ANCHOR PAYOFF) — nine questions returned verbatim; closing line
    reframed as the honest verdict on scope: "a shape enforced on the record,
    not a decision automated out of your hands."
  - **B07** (both directions) — opens with "the design is honest about its own
    limits in both directions" and closes with the Feynman-style handoff:
    "read it as evidence that the interview happened, not as a verdict on what
    was said." Both failure modes (clean-doesn't-prove-clean,
    flagged-doesn't-prove-broken) survive intact.
  - **BCRY** — carry-out kept exactly as the source wrote it. It is already the
    Teardown thesis in one sentence; rewriting for its own sake would have
    made it worse. `WantQuote.props.quote` matches the narration verbatim.
- **BHTF repurposed as the LLM EXERCISE beat (second-to-last).** `act` changed
  from `your turn handoff` to `LLM EXERCISE`. Added the `llm_exercise` object
  with a paste-ready three-part prompt derived from the video's whole subject
  (write a SKILL.md for a recurring decision; name the two output files + the
  log row; mark what the skill *cannot* decide) plus a real "Go deeper"
  follow-up (is the checklist you already trust enforcing shape, or quietly
  making the decision?). `ClaudeComposerAsk.props.command` updated to match
  the new prompt; the composer's `segment` already read
  "Claude, Matter Intake." from the source. `estimated_duration_s` bumped
  21 → 55 to fit the expanded read; real duration will be re-measured by
  audio-first compile.
- **BOUT (outro) kept as last beat, unchanged.** Already the Liam / in-for-Bear
  OutroCTA closer ("Claude, Matter Intake. Liam, in for Bear.") — matches
  the sibling `nbb-claude-for-legal--claude-liam-client-intake` and
  `-legal-finance` outros.
- **Metadata:** `_variant_todo` removed; `register` (Teardown), `palette`
  (teardown), `audience` (NikBearBrown), `outro_source`, `typography`,
  `engine` (kokoro), `voice_kokoro` (am_onyx) left exactly as the scaffold
  set them. `purpose` string updated from "in the Plain register" to
  "in the Teardown register" — the only substantive metadata change; every
  other field carried over.

## Ending order verified

body (B00 → B07) → **BCRY** (carry-out) → **BHTF** (LLM EXERCISE, second-to-last)
→ **BOUT** (outro, last). ✓

## Judgement calls

- **BCRY left verbatim.** Same call as `-client-intake` / `-legal-finance` —
  the carry-out is already the Teardown thesis in one sentence, and the
  on-screen `WantQuote` mirrors it word for word. Rewriting to prove I
  rewrote it would have broken that mirror.
- **@HumanitariansAI kept in outro handle, composer folderLabel, and
  channel_title.** Matches the sibling nbb Legal reels: audience metadata is
  `NikBearBrown` (register + palette + voice discipline), but the on-screen
  frame stays `@HumanitariansAI` because this reel lives in the
  claude-bear/HAI content tree and is hosted by Liam-in-for-Bear on that
  channel. The nbb SKILL says outro *content* comes from
  `AUTHOR.MD :: NikBearBrown`; the outro sting itself is a Liam / in-for-Bear
  CTA, which is what the sibling reels ship.
- **B01 lengthened deliberately.** Source B01 was one sentence naming the
  misread. Teardown wants the *mechanism* of the misread — so the rewrite
  splits "intake" and "skill" and shows why each word individually implies
  something more than the machinery does. Word count nearly doubled; that is
  intentional. Audio-first compile is the clock, not `estimated_duration_s`.
- **`estimated_duration_s` bumped on every rewritten beat** to reflect new
  word counts (B00 13→18, B01 10→17, B02 15→21, B03 14→22, B04 15→24,
  B05 15→23, B06 12→22, B07 17→23, BHTF 21→55). Informational only; the
  compile pass measures the real MP3 and uses it as the master clock. `BCRY`
  and `BOUT` unchanged because their narration didn't change.
- **Facts unchanged.** Every named artifact (SKILL.md, matter.md, history.md,
  _log.yaml), the nine-question list (identification, conflicts, source,
  risk, materiality, outside counsel, owners, legal hold, key dates), the
  no-branching mechanism, and the "skill can't decide accept/decline" thesis
  all survive verbatim in substance. No new file, no invented cite, no
  fabricated matter type. Voice changed; report did not.
