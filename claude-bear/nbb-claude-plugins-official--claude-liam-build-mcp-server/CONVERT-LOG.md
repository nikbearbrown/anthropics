# CONVERT-LOG — nbb cut of `claude-plugins-official--claude-liam-build-mcp-server`

Converted the scaffold into the NikBearBrown cut. Facts unchanged; register
rewritten; LLM exercise slotted in second-to-last; NikBearBrown outro last.

## What changed

- **All seven `narration_text` fields rewritten in the Teardown register.**
  Feynman × MKBHD — take the skill apart, explain what each deployment path
  optimizes for and what it costs, name the trade-off between the two
  tool-design patterns as a function of action-space size, and land the
  description-decides subtlety with the actual failure mode ("no stack trace
  to tell you which one lost"). Every fact in the source survives verbatim in
  substance: three deployment paths ranked with remote HTTP as default, the
  MCPB definition and use cases, stdio's distribution weakness, the seven-scenario
  decision matrix, the ~15-operation cutover, search-plus-execute mechanics
  (search-actions + execute-action), the 3–5 hybrid promotion, the four MCP
  primitives (tools, resources, prompts, elicitation), and the description-over-name
  dispatch rule.
- **BCRY quote sharpened** in the same register. Original: "…you're not tweaking
  the server later, you're rewriting it." New: "…you don't get to tweak the
  server later. You rewrite it." Also normalized "how many actions" → "action
  count" so the four-question list reads as four parallel nouns. The
  `WantQuote.quote` prop was updated to match so the on-screen and spoken lines
  agree; `sparkLine` ("Decide first. Code second.") kept.
- **BHTF converted from "your turn handoff" to the LLM exercise beat**
  (SECOND-TO-LAST). Act renamed to `LLM EXERCISE`. Added the required
  `llm_exercise` object with `prompt` + `dig_deeper`. The prompt is a
  paste-ready block for Claude / ChatGPT / Gemini that produces a real,
  useful artifact on its own — the four decisions worked out against the
  GitHub API as the concrete target, plus a draft of tool definitions and a
  self-critique of the vaguest description. The dig-deeper is a genuinely
  next question: work out where the search-plus-execute cutover sits for
  GitHub, design the hybrid, name what breaks when a promoted tool changes
  shape. Narration reads the prompt in full and closes with the
  "Go deeper: …" follow-up. The on-screen `ClaudeComposerAsk.command` prop
  was rewritten as a tightened, numbered version of the same prompt so the
  composer card doesn't overflow.
- **BOUT switched from `OutroSeries` to `OutroCTA`** (matches the standard
  NBB outro pattern used by the sibling nbb reels). Props: `line` (title +
  "Liam, in for Bear.") and `handle: "@NikBearBrown"`. Outro narration line
  updated from the source "Build MCP Server. Liam, in for Bear." to
  "Decide First. Liam, in for Bear." so the closing line names the reel's
  title-of-record (which the source metadata already sets to "Decide First.")
  instead of the skill's raw name.
- **`folderLabel` and `channel_title` metadata switched from
  `@HumanitariansAI` to `@NikBearBrown`** — this is the NBB cut, so the
  channel chip and title live under the NikBearBrown handle. The BHTF
  composer's `folderLabel` prop was updated the same way.
- **`_variant_todo` removed** from metadata. `purpose` reworded to the
  Teardown framing (take apart the skill, evaluate the two tool-design
  patterns against action-space size, name the cost of a vague description)
  so the metadata line no longer reads as a Plain-register summary. Carry-out
  wording aligned to the sharpened BCRY.
- **Stale `actual_duration_s` fields left as the scaffold left them (absent).**
  `estimated_duration_s` values were nudged up on the rewritten body beats
  (NB01 → 42s, NB02 → 44s, NB03 → 24s, BCRY → 11s, BHTF → 90s) to reflect the
  longer Teardown prose and the long paste-ready LLM prompt at BHTF; these
  are only estimates — audio-first regeneration is a separate render pass
  and will overwrite the real durations.

## Judgment calls

- **Rebrand to `@NikBearBrown` on the metadata + composer chips.** The scaffold
  left the source `@HumanitariansAI` labels in place. Following the
  properly-converted sibling
  `nbb-claude-plugins-official--claude-liam-agent-development` (which changed
  both). Brand spec at `brands/nbb.md` and the NBB `SKILL.md` outro rule both
  point at the NikBearBrown channel as the default, so the labels match the
  destination channel.
- **Kept the `BrutalistHesitantWriter` on-screen text verbatim** (`code` →
  `decide` correction, seed `hai-build-mcp-server`, all timing knobs). It is
  the entire visual mechanic of the cold open and the corrected question
  ("What do I decide first for an MCP server?") still lands the reel's real
  subject in the Teardown rewrite. The narration around it was reworked to
  Teardown voice while landing on the same final question the writer types.
- **Kept the graphic `production_viz` labels, chips, captions, and Manim scene
  IDs (`BDNB01Scene`/`BDNB02Scene`/`BDNB03Scene`) unchanged.** Those are
  on-screen card copy that already reads cleanly in the Teardown register
  ("remote HTTP default · unless local machine required", "large surface:
  search-plus-execute keeps context lean", "a vague description blurs similar
  tools together") and re-labeling them would force a re-render of the Manim
  scenes without changing anything the viewer sees differently. The
  `#F3EBDD` ground color inside the viz colors array is a legacy from the
  source hai palette; the metadata `palette` field is authoritatively
  `teardown` and the render pipeline is expected to resolve the token there.
- **Outro line changed to the reel's title ("Decide First.")** rather than
  the skill's file name ("Build MCP Server"), following the sibling
  agent-development reel's OutroCTA pattern ("Describe When, Not What. Liam,
  in for Bear."). The reel's title is what the viewer just watched; the file
  name is the source citation.
- **Left `playlist: "Extending Claude — Skills, Plugins & Connectors"`
  unchanged.** The scaffold set it and it is a plausible playlist on the NBB
  channel too; this reel fits that playlist cleanly.
- **Left `style_preset: "humanitarians"` and `ground: "#F3EBDD"` as the
  scaffold set them.** The palette field is already `teardown`, which is the
  color law of record; the `style_preset` / `ground` fields appear to be used
  by the source hai-simple compositions and don't conflict with the teardown
  palette at runtime (same pattern in the sibling nbb sheet).

## Not done here (deliberate)

Rendering, audio generation, and compilation. Per the supervisor's brief, this
pass is beat-sheet-only. `generate_audio_kokoro.py` and `compile.py` are a
separate render pass.
