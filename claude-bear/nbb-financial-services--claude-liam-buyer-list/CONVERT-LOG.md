# CONVERT-LOG — nbb-financial-services--claude-liam-buyer-list

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Plain → Teardown register). Voice-only rewrite; every fact, beat_id, act, shot block, and on-screen card copy preserved from source.

## Beat-by-beat changes

- **B00 cold open** — rewrote in Teardown, opening with "Liam, in for Bear" per IN-FOR-BEAR LAW (source had no explicit sign-in; cold open is the mandated place). Reframed "app vs skill" as machinery-first: the app-that-isn't-an-app / real question is what the file tells Claude to do. Card props (BrutalistHesitantWriter, "app" → "skill") preserved verbatim.
- **B01 anatomy** — rewrote to name the design choice: "readable to you, not just to Claude — because if you can't read it, you can't fix it." Machinery ("one folder, one file, plain English") preserved from source.
- **B02 pipeline** — rewrote with an explicit trade-off ("optimized for you being able to predict… at the expense of anything clever"). Linear-execution fact preserved.
- **B03 mechanism + scope** — rewrote as scope teardown: what the page covers exactly, and the direct consequence of "Claude follows the page exactly" — you get repeatability, you don't get judgment beyond the page. All source facts (sell-side M&A, strategic vs financial, outreach ordering) preserved.
- **BCRY carry-out** — narration LEFT VERBATIM. Judgement call: the WantQuote card renders this sentence on-screen; the narration must match the visible quote character-for-character or the audio and card fall out of sync. The sentence is already a MKBHD-style design-choice line ("doesn't make X, makes Y") — passes the Teardown register on its own terms.
- **BHTF (second-to-last)** — kept as the LLM exercise beat (this is how the source ended, and matches the deal-sourcing nbb precedent — beat_id and ClaudeComposerAsk props preserved so audio/card contract is intact). Added:
  - a structured `llm_exercise: { prompt, dig_deeper }` object per SKILL.md §Step 3 schema;
  - a real "Go deeper" follow-up (write a SKILL.md for a recurring task, hand it to a colleague, check whether they get the same result — a genuine next question, not a summary);
  - updated `act` from "your turn handoff" to "LLM exercise — your turn" to make the role explicit.
- **BOUT (last)** — narration and card props LEFT AS-IS (`"Claude, Buyer List. Liam, in for Bear."` / OutroSeries with the existing eyebrow). Judgement call: the scaffold did not rewire `channel` / `channel_title` / `folderLabel` / `playlist` away from @HumanitariansAI, and the deal-sourcing nbb precedent shipped the same way — @HAI channel receives a Bear-teardown episode. No AUTHOR.MD :: NikBearBrown was found under this book to source alternative outro copy from; metadata still records `outro_source: AUTHOR.MD :: NikBearBrown` per the scaffold contract.

## Metadata

- Removed `_variant_todo`.
- `source_register` corrected from "Teardown" (scaffold default, wrong for this source) to "Plain" — the source `metadata.register` was "Plain".
- `skill` changed from "hai-simple" (source) to "nbb" (this cut's skill).
- `purpose` rewritten to describe what THIS cut is (nbb teardown of buyer-list), not the source's hai-simple purpose.
- `audience`, `register`, `palette`, `engine`, `voice_kokoro`, `derived_from`, `outro_source`, `typography` left as the scaffold set them.
- Channel / folderLabel / playlist unchanged — see BOUT note above.

## Not done

- No audio, no render, no compile — per contract. Downstream: `generate_audio_kokoro.py` → `compile.py` on the nbb dir.
