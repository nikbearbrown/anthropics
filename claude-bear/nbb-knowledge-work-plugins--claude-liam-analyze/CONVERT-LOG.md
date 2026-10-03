# CONVERT-LOG — nbb-knowledge-work-plugins--claude-liam-analyze

Source: `knowledge-work-plugins--claude-liam-analyze/beat_sheet.json` (Plain register, @HumanitariansAI)
Output: `beat_sheet.nbb.json` (Teardown register, @NikBearBrown)

## What changed

**Narration — rewrote all seven beats in the Teardown register.**
- B00 (cold open): kept BrutalistHesitantWriter timing law (32 words, in the 20–35 window); reframed from "step by step" hand-hold to "hides the mechanism / we're going to take it apart" — same fact, sharper design lens.
- B01 (stakes / wrong guess): "Here's what's actually happening" opener; named the design choice explicitly ("optimized for a predictable procedure over adaptive judgment") and its cost ("no procedure tailored to reach for"). Four question shapes preserved verbatim.
- B02 (mechanism / anchor planted): reframed pipeline description as "Watch the machinery"; anchor ("weekly signups drop twelve percent" → "organic search fell") preserved verbatim; added Teardown emphasis ("Not a probability, not a range, not an interpretation. The single specific driver the steps were designed to find.")
- B03 (anchor payoff / both directions): both directions of the trade-off named as Teardown formula — "This works if you value repeatability. It fails if you need judgment the procedure was never designed to make." Anchor return preserved.
- BCRY (carry-out): unchanged. Already Teardown-cadenced ("written procedure", "one of four shapes", "only covers question shapes the file defines"); on-screen WantQuote copy preserved verbatim per SKILL.md's "on-screen card copy that still fits the register" rule.
- BHTF (see below).
- BOUT (see below).

**LLM EXERCISE beat — repurposed BHTF (was "your turn handoff") into the LLM EXERCISE slot.**
Following the sibling-nbb precedent (`nbb-books--claude-liam-data/beat_sheet.nbb.json`), BHTF stays as the second-to-last beat and is upgraded — act renamed to `LLM EXERCISE`, `llm_exercise` object added with a `prompt` + `dig_deeper`. Kept `ClaudeComposerAsk` as the render pattern; updated the `command` to a condensed on-screen version of the paste-ready prompt, `runningText` to "paste this into Claude, ChatGPT, or Gemini…", and `folderLabel` to `@NikBearBrown`. The prompt itself is deliberately skill-independent (no `analyze` skill install required — viewer can run it in any frontier LLM today and get useful output).

**Outro — BOUT preserved as the last beat, handle re-pointed to @NikBearBrown.**
Kept the `OutroCTA` line ("How Does Claude Analyze Data? Liam, in for Bear.") since it already satisfies the IN-FOR-BEAR LAW. `handle` changed from `@HumanitariansAI` to `@NikBearBrown`.

**Metadata**
- `register`: `Teardown` (was already set by scaffold — retained).
- `folderLabel` / `channel_title`: both re-pointed from `@HumanitariansAI` to `@NikBearBrown`.
- `topic`, `title`, `slug`, `playlist`, `palette`, `engine`, `voice_kokoro`, `ground`, `style_preset`: **unchanged.** Scaffold's palette=`teardown` retained per "Do not re-scaffold."
- `purpose`: rewrote to describe the Teardown angle (machinery + design trade-off) rather than the Plain "answer whether…" framing.
- `source_note`: appended a paragraph noting the register re-registration and BHTF repurposing.
- `_variant_todo`: **removed** (all items addressed).
- `estimated_duration_s`: bumped on beats whose narration grew (B01, B02, B03, BHTF); left unchanged where the rewrite kept close to the original length. Real durations will be re-measured on the next audio pass — the pipeline treats these as hints.

## Judgement calls

- **Where to insert the LLM EXERCISE beat.** The scaffold left BHTF (a "your turn" handoff whose prompt required the ANALYZE skill installed) in the second-to-last slot. Two options: (a) repurpose BHTF into the LLM EXERCISE beat, or (b) keep BHTF and insert a new B_LLM before BOUT. Chose (a), matching the sibling `nbb-books--claude-liam-data` precedent. Rationale: BHTF and B_LLM both occupy the "second-to-last audience-facing prompt" slot; keeping both would double-handoff the viewer. Repurposing preserves the existing render pattern (`ClaudeComposerAsk`) and the beat_id, and the source's "your turn" narration was largely a wrapper around a paste-ready prompt anyway — the difference is the prompt is now skill-independent instead of requiring the ANALYZE skill install.
- **Playlist name.** Kept the source's `Extending Claude — Skills, Plugins & Connectors`. The sibling nbb reel used `Claude Cowork`, but that's a different book (Cowork plugins vs knowledge-work-plugins), and I don't have authoritative guidance to invent a different NBB-side playlist for this one.
- **`palette: teardown` vs `ground: #F3EBDD`.** The teardown palette per SKILL.md is flat white (`#FFFFFF`), but the scaffold left `ground: #F3EBDD` (cream) — matching how the sibling nbb reel is set up. Left both as scaffolded ("Do not re-scaffold"). Rendering-side reconciliation is out of scope for this pass.
- **Kept `note` on B00 verbatim.** The BrutalistHesitantWriter TIMING LAW note describes on-screen correction behavior that still applies. New narration is 32 words, inside the 20–35 window it prescribes.

## Facts unchanged (spot-check)

- Four question shapes: metric lookup / trend or drop / segment compare / formal report ✓
- Anchor: weekly signups drop 12% → asked → matched → stepped → returned "organic search fell" ✓
- Both directions: run twice = same driver; cut marketing budget = no shape to match ✓
- Carry-out sentence (WantQuote): preserved verbatim as the on-screen quote ✓

## Not done (out of scope per supervisor instructions)

- Audio regeneration (`generate_audio_kokoro.py`) — will re-measure `actual_duration_s`.
- Manim / Remotion re-render — visuals still reference source `manim/*.mp4` and `media/*.mp4`.
- Compile — no review cut, no final master.
