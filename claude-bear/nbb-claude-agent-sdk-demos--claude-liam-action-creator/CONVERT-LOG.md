# CONVERT-LOG — claude-agent-sdk-demos--claude-liam-action-creator

Conversion: source Plain (hai-simple) → NikBearBrown (Teardown register).

## What changed

- **All 7 narration_texts rewritten in Teardown register** (Feynman × MKBHD): take
  it apart, name the design choice, state the trade-off. Facts preserved
  exactly — same folder contents (SKILL.md + templates), same anchor
  (payment-reminder button, B02→B03), same carry-out shape, same handoff prompt.
  Added the design-critic frame in B01 ("optimized for a skill you can read,
  review, and change without touching code"), B02 ("the way you'd read a
  recipe"), and B03 ("a deliberate trade of range for consistency").
- **BCRY WantQuote `quote` prop updated** to match the rewritten BCRY narration
  verbatim, so the on-screen sentence and the spoken sentence stay identical.
- **BHTF promoted to the LLM exercise slot** (second-to-last, unchanged position).
  It was already a paste-ready `ClaudeComposerAsk` prompt, which is exactly what
  the SKILL.md §Step 3 schema calls for. Added an `llm_exercise` block with the
  paste-ready prompt (unchanged from source) and a "Go deeper" follow-up on how
  you'd change SKILL.md to swap archive→unsubscribe — a real next question that
  exposes where a Skill's limits live. Narration extended to read the "Go deeper"
  line aloud; `estimated_duration_s` bumped 22→26 to fit it.
- **BOUT kept as-is** — the source outro line already matches the NBB pattern
  (title + "Liam, in for Bear") observed in sibling nbb sheets. Rendering
  handled by `OutroCTA`.
- **`_variant_todo` removed** — all four listed items are done (rewrite, LLM
  exercise, outro verified last, ending order body → LLM exercise → outro).

## Judgement calls

1. **Reused BHTF instead of inserting a separate `B_LLM` beat.** The SKILL.md
   template shows a fresh `B_LLM` `CARD` beat between BCRY and BOUT, but the
   source's BHTF is already a paste-ready Claude prompt via `ClaudeComposerAsk`
   — visually and functionally the LLM exercise beat. Every sibling nbb sheet
   in this book (checked `nbb-claude-basics--screenshot-prompt-caching`) uses
   the same pattern: BHTF is the LLM exercise, BOUT is the outro. Adding a new
   B_LLM would produce a duplicate handoff. Precedent wins over template.
2. **`folderLabel` and `handle` switched from `@HumanitariansAI` to
   `@NikBearBrown`** on BHTF and BOUT. The scaffold left the HAI channel
   metadata in place at the top level (`folderLabel`, `channel_title`,
   `style_preset`), but the on-screen chip inside a Claude composer / outro card
   is the *host handle*, and the audience for this cut is NikBearBrown. The
   sibling nbb sheet left `@HumanitariansAI` on the card — treating that as
   sloppy carry-over from the scaffold rather than a rule, since the metadata
   explicitly says `audience: NikBearBrown` and `outro_source: AUTHOR.MD ::
   NikBearBrown`. Top-level metadata (channel_title, folderLabel) left untouched
   so nothing else the scaffold owns is disturbed.
3. **Kept `estimated_duration_s` in the ballpark of the source `actual_duration_s`
   +/- the words added.** B00 remained 14 (same word count as source). B01–B03
   stayed at their source estimates. BHTF grew from 22 to 26 to fit the
   Go-deeper sentence. Audio regeneration will measure real durations; these are
   estimates only, and are not the master clock.

## What was NOT changed

- `shot`/`graphic`/`remotion` blocks (visuals, props, manim scene names, seeds,
  colors) — preserved exactly.
- `build`, `audio_file`, `note`, `lead_silence_s`, `tail_silence_s`, all `beat_id`s.
- Metadata block set by the scaffold (`audience`, `register`, `palette`,
  `engine`, `voice_kokoro`, `typography`, `outro_source`, `derived_from`).
- The B02→B03 anchor pair.

Deliverable: `beat_sheet.nbb.json`, valid JSON, 7 beats, ending order
`… → BCRY (carry-out) → BHTF (LLM exercise) → BOUT (outro)`. No rendering,
no audio generation, no compile.
