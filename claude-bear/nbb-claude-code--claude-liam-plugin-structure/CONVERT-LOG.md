# CONVERT-LOG — claude-code--claude-liam-plugin-structure (NBB)

Source: `anthropics/claude-bear/claude-code--claude-liam-plugin-structure/beat_sheet.json`
Target: `anthropics/claude-bear/nbb-claude-code--claude-liam-plugin-structure/beat_sheet.nbb.json`

## What changed

- **Rewrote all seven original narrations in the Teardown register.** Facts unchanged (every folder name, filename, field, and count survives). Voice shifted from Plain to Feynman × MKBHD: name the machinery, expose the design choice, price the trade-off. "Convention over configuration cuts both ways" (B03) is the register in one line.
- **B00 cold open** now opens with "Liam here, in for Bear" per IN-FOR-BEAR LAW. Length held to 33 words so the BrutalistHesitantWriter TIMING LAW window (>=8s, correction visible on a late frame) still clears.
- **B01 / B02 / B03** rewritten to reveal the design philosophy explicitly: "they split identity from behavior" (B01), "convention doing the work a config file would normally do" (B02), "the price the design charges at load time" (B03). No new facts introduced.
- **BCRY** narration and on-screen `WantQuote` copy left semantically identical (the carry-out sentence is already a flat design principle — Teardown accepts it verbatim). Only "dot-claude-plugin" said aloud in the narration; the on-screen quote preserves the literal filename.
- **BHTF** kept as the your-turn handoff (beat_id and shot preserved). Narration re-cast in Teardown ("this is how you check whether the layout was obeyed"; "any wrong answer is a silent fail") and still signs off "Liam, in for Bear."
- **NEW beat `B_LLM`** inserted second-to-last. Contains the required `llm_exercise` object: a paste-ready prompt for any frontier LLM (Claude / ChatGPT / Gemini) that asks the model to name the convention-over-configuration trade-off and the class of bugs it creates for plugin authors — a genuinely useful output on its own without the video. `dig_deeper` follow-up pushes the viewer to design a loader that flags "almost-right" filenames (skill.md → SKILL.md). Shot: `CARD / own / hold` per SKILL.md §Step 3.
- **BOUT** replaced with the NikBearBrown outro. Handle changed to `@NikBearBrown` (from AUTHOR.MD :: NikBearBrown), narration adds "Find more at Nik Bear Brown on YouTube." Line, tail_silence, and `OutroCTA` pattern preserved.
- **Metadata:** `_variant_todo` removed. Scaffold fields (audience=NikBearBrown, engine=kokoro, voice_kokoro=am_onyx, palette=teardown, register=Teardown, typography, outro_source, derived_from) left as the scaffold set them.

## Judgement calls

1. **Two your-turn beats back-to-back (BHTF + B_LLM).** The source's BHTF was already a paste-ready prompt for Claude Code specifically (a build-and-audit task). SKILL.md §Step 3 requires a *separate* LLM-exercise beat second-to-last that produces useful output on its own with any frontier LLM. Chose to keep BHTF unchanged in slot (preserve beat_id + shot per instructions) and insert a new distinct B_LLM — a design-analysis prompt, not a build prompt. They complement rather than duplicate: BHTF says "build one and audit the layout"; B_LLM says "explain the trade-off and the bug class it creates." A merge would have lost the shot-block preservation rule and cost the video its Claude-Code-specific hands-on beat.
2. **BHTF's `folderLabel: "@HumanitariansAI"` kept** even though the audience is now NikBearBrown. Instructions say preserve shot blocks exactly; the BHTF shot is not the outro. The mismatch (voiced as NBB, on-screen chip @HumanitariansAI) is inherited from the scaffold, not introduced here — flagging for downstream, not fixing.
3. **BOUT handle changed to `@NikBearBrown`.** Step 4 explicitly replaces the outro with the NikBearBrown outro, so the handle in `OutroCTA` props is fair game. `nbb.md` names `www.brutalist.art` as the *default* channel, but per SKILL.md §Step 4 the outro content comes from `AUTHOR.MD :: NikBearBrown`, and that section's YouTube handle is `@NikBearBrown`. Went with AUTHOR.MD.
4. **BCRY on-screen quote preserved verbatim.** Rewriting the on-screen `WantQuote.quote` would drift from the source card copy, and the source line already reads as flat Teardown ("only X, everything else Y, and only auto-loads if Z"). Narration spells "dot-claude-plugin" for Kokoro; on-screen keeps `.claude-plugin` for the reader.

## Ending order verified

`B00 → B01 → B02 → B03 → BCRY → BHTF → B_LLM (LLM EXERCISE) → BOUT (outro)` — LLM exercise is second-to-last, NikBearBrown outro is last.

## Not done (out of scope per supervisor)

No audio generated, no compile, no render. Deliverable is the beat sheet only.
