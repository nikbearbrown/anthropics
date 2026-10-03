# CONVERT-LOG — claude-agent-sdk-demos--claude-liam-executive-briefing

Conversion: source Plain (hai-simple) → NikBearBrown (Teardown register).

## What changed

- **All 7 narration_texts rewritten in Teardown register** (Feynman × MKBHD): take
  it apart, explain the machinery, name the design choice and the trade. Facts
  preserved exactly — the file is still SKILL.md at ~4 KB, still one file, still
  the same six trigger words (executive, briefing, C-suite, board, leadership,
  presentation), same anchor memo (B02→B03), same "board presentation" vs
  "make this shorter for my boss" contrast, same carry-out shape, same paste-ready
  handoff. Added the design-critic frame in B01 ("optimized for … a skill you can
  read, review, and change without touching any code"), B02 ("the mechanism
  underneath is a lookup, not a judgment"), and B03 ("works if you value
  repeatable, auditable behavior; fails the moment you assumed the skill was
  reading intent").
- **BCRY WantQuote `quote` prop updated** to match the rewritten BCRY narration
  verbatim, so the on-screen sentence and the spoken sentence stay identical.
  The `sparkLine` ("The list decides, not the meaning.") already fit the new
  narration — kept.
- **BHTF promoted to the LLM exercise slot** (second-to-last, unchanged position).
  It was already a paste-ready `ClaudeComposerAsk` prompt — exactly what SKILL.md
  §Step 3 calls for. Added an `llm_exercise` block: `prompt` is the source
  command verbatim; `dig_deeper` asks what would have to be added to SKILL.md
  so the skill fires on "condense this for my boss" too — a real next question
  that exposes the scaling limit of the trigger-word design. Narration extended
  to read the "Go deeper" line aloud; `estimated_duration_s` bumped 21→28 to fit.
- **BOUT kept as-is** — the source outro line ("Claude, Executive Briefing.
  Liam, in for Bear.") already matches the NBB pattern (title + "Liam, in for
  Bear") observed in every sibling nbb sheet in this book. Rendering handled
  by `OutroCTA`.
- **`_variant_todo` removed** — all four listed items are done (rewrite, LLM
  exercise inserted, outro verified last, ending order body → LLM exercise →
  outro).

## Judgement calls

1. **Reused BHTF instead of inserting a separate `B_LLM` beat.** The SKILL.md
   template shows a fresh `B_LLM` `CARD` beat between BCRY and BOUT, but the
   source's BHTF is already a paste-ready Claude prompt via `ClaudeComposerAsk`
   — visually and functionally the LLM exercise beat. The sibling
   `nbb-claude-agent-sdk-demos--claude-liam-action-creator` sheet (same book,
   same shape) followed exactly this path. Adding a new B_LLM would produce a
   duplicate handoff. Precedent wins over template.
2. **`folderLabel` and `handle` switched from `@HumanitariansAI` to
   `@NikBearBrown`** on BHTF and BOUT. The scaffold left the HAI channel
   metadata in place at the top level (`folderLabel`, `channel_title`,
   `style_preset`), but the on-screen chip inside a Claude composer / outro card
   is the *host handle*, and the audience for this cut is NikBearBrown
   (`audience: NikBearBrown`, `outro_source: AUTHOR.MD :: NikBearBrown`).
   Matches the action-creator sibling. Top-level metadata (channel_title,
   folderLabel) left untouched — that is the scaffold's territory.
3. **B00 narration reshaped, correction pair preserved.** The typewriter visual
   corrects `judgment` → `list`. The rewrite keeps those two words as
   load-bearing anchors of the spoken line ("applies judgment"… "matches a
   fixed list of trigger words") so the on-screen mistake still tracks what
   the ear is hearing. Word count stays inside the WRITER-LAW 20–35 window
   (~39 words).
4. **`estimated_duration_s` bumped where words grew.** B01: 18→22 (added the
   design-choice sentence). B02: 21→22 (added the lookup-vs-judgment tag).
   B03: 21→22 (added the trade-off line). BHTF: 21→28 (Go-deeper line).
   Audio regeneration measures real durations — these are estimates only, and
   are not the master clock.

## What was NOT changed

- `shot`/`graphic`/`remotion` blocks (visuals, props, manim scene names, seeds,
  colors, `ClaudeComposerAsk` `command` text, `BrutalistHesitantWriter` props
  including the typed text and correction words) — preserved exactly.
- `build`, `audio_file`, `note`, `lead_silence_s`, `tail_silence_s`, every
  `beat_id`.
- Metadata block set by the scaffold (`audience`, `register`, `palette`,
  `engine`, `voice_kokoro`, `typography`, `outro_source`, `derived_from`).
- The B02→B03 anchor pair.

Deliverable: `beat_sheet.nbb.json`, valid JSON, 7 beats, ending order
`… → BCRY (carry-out) → BHTF (LLM exercise) → BOUT (outro)`. No rendering,
no audio generation, no compile.
