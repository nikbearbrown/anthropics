# CONVERT-LOG — claude-plugins-official--claude-liam-plugin-settings

Converted the scaffold at `beat_sheet.nbb.json` from the Plain / hai-simple
source into the NikBearBrown / Teardown cut. Voice: Liam (Kokoro `am_onyx`), in
for Bear. Sheet only — no render, no audio, no compile.

## What changed

- Removed `_variant_todo` from metadata; rewrote `purpose` in the Teardown
  register (names the design trade-off Anthropic actually made: project-scoped
  and git-safe at the cost of a live reload and any cross-project carryover).
- Rewrote all seven `narration_text` fields in the Teardown register — take
  apart the mechanism (one dot-local file, YAML frontmatter + markdown body,
  three readers, per-project scope), name the design philosophy underneath, and
  in NB03 explicitly call the "no plugin-wide switch" gap a *choice*, not a
  bug. No fabrication: every fact from the source survives — the file path
  spelling, the two parts, the three readers, the four things (schema first /
  sensible defaults / quick-exit hooks / manual gitignore), the no-carryover
  gap, and the "set it, save it, restart it" contract are all intact.
- **B00** cold open now opens with "Liam here, in for Bear." (IN-FOR-BEAR LAW,
  matches every other completed nbb reel's cold open). The
  BrutalistHesitantWriter visual (text, triggerWords, replacementWords, all
  timing params) is untouched — narration and visual are independent.
- **BCRY** carry-out narration rewritten; also updated the `WantQuote.quote`
  prop to the tightened Teardown carry-out line ("A plugin's settings file is
  per-project and needs a restart. Set it, save it, restart it — that's the
  whole contract."). Kept the `sparkLine` ("Per project. Restart required.") —
  already fits the register.
- **BHTF** promoted to the LLM EXERCISE beat per nbb SKILL.md §Step 3:
  - `act` changed from "your turn handoff" to "LLM EXERCISE".
  - Added `llm_exercise: { prompt, dig_deeper }` — a paste-ready prompt that
    has any frontier LLM draft the `.local.md` itself for a hypothetical
    plugin (enabled flag, validation_level enum, max_retries int), plus the
    quick-exit hook that reads it, the .gitignore line, and a two-line note
    on why the pattern requires a restart. Runs on its own without the video.
  - "Go deeper" follow-up: could the same pattern support a user-global
    override that per-project settings *extend* without breaking isolation —
    genuinely open, not a summary of the video.
  - Updated the ClaudeComposerAsk `command` prop to a shorter form of the
    same prompt (readable on the composer card) and the `segment` label to
    "Draft the .local.md yourself" (the previous "Restart Required." was a
    title echo, not a description of the beat).
  - Kept `folderLabel: @HumanitariansAI` — matches the closest completed
    nbb reels (including the sibling xml-changes reel) which keep the source
    handle on the composer card.
- **BOUT** narration tightened, added the subtitle recall so the outro names
  the pattern out loud: "Restart Required — the plugin settings pattern.
  Liam, in for Bear." OutroSeries `eyebrow` + `line` props unchanged (they
  already read correctly against the new narration).
- Bumped `estimated_duration_s` on B00 (13→16), NB01 (24→30), NB02 (26→34),
  NB03 (20→24), BCRY (8→12), BHTF (26→38) to reflect the new narration word
  counts. These are estimates only — Kokoro measures the actuals.

## Judgement calls

- **Where to put the LLM exercise.** The source's second-to-last beat (BHTF)
  was already a ClaudeComposerAsk paste-ready prompt — same shape as the
  enterprise-search reel. Promoted BHTF in place rather than inserting a new
  `B_LLM` beat and losing the composer shot, matching the precedent set by
  the completed 8-beat sibling reels.
- **New prompt subject.** The source's "your turn" prompt asked the viewer
  to *have* Claude add configurable settings to a plugin, then watch three
  things. That's a design-review exercise, not a paste-and-run LLM exercise.
  Rewrote it as: have the LLM draft the actual `.local.md` file, the hook,
  the gitignore line, and the restart note in one shot — produces a useful
  artifact you can drop in a repo without watching the video first, which
  is the §Step 3 test. The original three-thing checklist becomes the
  implicit acceptance criteria embedded in the prompt (per-project location,
  quick-exit guard, fail-open on missing file).
- **Kept `channel_title` / `folderLabel` = `@HumanitariansAI`.** Matches the
  sibling xml-changes reel and other completed nbb cuts in this book that
  keep the source channel handle rather than re-tagging to `@NikBearBrown`.
- **Kept `style_preset` and `ground` (`humanitarians` / `#F3EBDD`) intact.**
  The scaffold set `palette: teardown` but left the humanitarians preset and
  cream ground in place; the sibling completed nbb reels do the same, so
  the compositor knows which style to key off. Not touching those without
  a clearer signal to override.
- **Kept all `production_viz` labels, chips, captions, and colors unchanged**
  across NB01/NB02/NB03. They describe the Manim render, not the narration,
  and they already read correctly in the Teardown register — rewriting them
  would drift the picture.
- **NB01 grew most (24s → 30s estimated).** The Teardown rewrite adds one
  sentence naming the design choice under "never committed to git" — that's
  where the beat earns its keep as a mechanism-and-philosophy beat.

## Not done here

- No `python3 runtime/scripts/generate_audio_kokoro.py [dir]`.
- No `python3 runtime/scripts/compile.py [dir] --height 1080`.
- No render, no publish. Supervisor's next pass handles those.
