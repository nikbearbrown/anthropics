# CONVERT-LOG — nbb-claude-plugins-official--claude-liam-build-mcp-app

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Teardown register, LLM
exercise second-to-last, NikBearBrown outro last). Facts unchanged: every API
name, MIME type, file path, and count survives from the source.

## What changed

- **All 5 body narrations rewritten in Teardown register** (B00, NB01, NB02,
  NB03, BCRY). Explained the machinery (what the tool declares, what the
  resource serves, how the iframe is wired), named design choices ("they
  optimized for a clean split between data and rendering at the cost of making
  you learn the two-part registration up front"), judged trade-offs on the
  silent-blank failure mode ("that's the cost of the design's silence: it fails
  safely instead of loudly").
- **BHTF transformed from "your turn handoff" → "LLM EXERCISE"**. Added the
  `llm_exercise` object with `prompt` (paste-ready for Claude / ChatGPT /
  Gemini, produces a useful walkthrough of a two-part MCP app on its own) and
  `dig_deeper` (why the designers put data on the tool and HTML on the
  resource — what would break, and for whom, if a tool were allowed to return
  HTML directly). Narration reads the prompt aloud and lands the go-deeper.
  Kept `ClaudeComposerAsk`; refreshed `command` prop with the paste-ready
  prompt.
- **BOUT outro pattern switched `OutroSeries` → `OutroCTA`** with
  `handle: "@HumanitariansAI"` to match the NikBearBrown outro spec + the
  completed sibling reels (e.g. `nbb-books--claude-liam-building-plugins`,
  `nbb-claude-quickstarts--claude-liam-first-run`). `line` folded the sign-off
  into the CTA line ("Return Data. Serve HTML. Liam, in for Bear.") so `OutroCTA`
  gets both the title callback and the IN-FOR-BEAR LAW sign-off.
- **BCRY on-screen quote lightly sharpened** ("just a server with an extra
  resource" → "a server with one extra resource") to match the tightened
  narration; on-screen chips + captions on NB01/NB02/NB03 preserved verbatim.
- **`register` metadata**: `Plain` → `Teardown`. `purpose` line updated to
  match the register.
- **Removed** `_variant_todo` from metadata (scaffold's TODO block).

## Judgement calls

- **Kept `ground: "#F3EBDD"` and `style_preset: "humanitarians"`.** The
  scaffold left these as the source's cream/humanitarians values even though
  `palette: teardown` was set. Sibling completed nbb reels
  (`nbb-books--claude-liam-*`) preserved the same combination, so I did not
  retint. If the intent is flat-white teardown ground per `brands/nbb.md`, a
  follow-up pass can flip `ground` + `style_preset`; I did not, since
  precedent points the other way.
- **B00 BrutalistHesitantWriter on-screen text left verbatim.** The 44-char
  three-line prompt with the tool→resource correction still lands the same
  cold-open question and passes the TIMING LAW window per the beat's note; the
  Teardown rewrite lives in the narration.
- **BHTF: kept the beat_id and `ClaudeComposerAsk` pattern** rather than
  inserting a new beat between BCRY and BOUT. `BHTF` was already the
  second-to-last "your turn" beat — repurposing it as the LLM exercise keeps
  the ordering law (body → [LLM exercise] → [outro]) and matches the completed
  sibling `nbb-books--claude-liam-building-plugins`, which also transformed
  its existing "your turn" beat rather than injecting a new one.
- **Duration estimate on BHTF raised 26 → 44s** to account for the longer
  paste-ready prompt read aloud plus the go-deeper follow-up.

## Not done (out of scope for this pass)

No audio, no render, no compile — per the factory contract. The scaffold's
`_variant_todo` build step (`generate_audio_kokoro.py` → compile) is left for
the next pass.
