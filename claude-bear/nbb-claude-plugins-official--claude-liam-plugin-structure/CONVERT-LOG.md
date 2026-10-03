# CONVERT-LOG — claude-plugins-official--claude-liam-plugin-structure (NBB)

Source: `anthropics/claude-bear/claude-plugins-official--claude-liam-plugin-structure/beat_sheet.json`
Target: `anthropics/claude-bear/nbb-claude-plugins-official--claude-liam-plugin-structure/beat_sheet.nbb.json`

## What changed

- **Rewrote all seven original narrations in the Teardown register.** Facts unchanged — every path, variable name, folder name, filename, field, and count survives. Voice shifted from Plain to Feynman × MKBHD: name the machinery, expose the design choice, price the trade-off. "It works if you value install-anywhere and you can live with a silent no-op when you forget. It fails if you need a loud crash when a path is wrong" (B03) is the register in one line.
- **B00 cold open** now opens with "Liam here, in for Bear" per IN-FOR-BEAR LAW. Word count held to 35 so BrutalistHesitantWriter TIMING LAW window (>=8s, correction visible on a late frame) still clears with the 0.8s `lead_silence_s`.
- **B01 / B02 / B03** rewritten to reveal the design philosophy explicitly. B01: "they optimized for zero boilerplate at the cost of one thing — any path that leaves the plugin's own folder tree is your problem to write." B02: names the compromise — "no build step and no import graph, in exchange for one small ceremony you have to remember." B03: prices the failure mode — "the price runtime resolution charges" and the "silent no-op vs. loud crash" trade. No new facts introduced.
- **BCRY** narration adjusted only to spell "installed" instead of the contraction "installed" (already flat Teardown). On-screen `WantQuote.quote` and `sparkLine` preserved verbatim — the carry-out sentence is already a design principle the register accepts as-is.
- **BHTF** kept as the your-turn handoff (beat_id and full `shot` block preserved, including `folderLabel: "@HumanitariansAI"`). Narration re-cast in Teardown ("this is how you check whether the design's ceremony was actually observed"; "any hardcoded path is a silent fail on the next install") and still signs off "Liam, in for Bear."
- **NEW beat `B_LLM`** inserted second-to-last. Contains the required `llm_exercise` object: a paste-ready prompt for any frontier LLM (Claude / ChatGPT / Gemini) that asks the model to name the runtime-variable-resolution trade-off, the class of bugs it creates for plugin authors, and one concrete mitigation. Produces a useful output on its own without the video. `dig_deeper` follow-up pushes the viewer to design a loader that crashes loudly at load-time on missing paths, instead of silently failing at hook-run time. Shot: `CARD / own / hold` per SKILL.md §Step 3.
- **BOUT** replaced with the NikBearBrown outro. `OutroCTA.handle` changed to `@NikBearBrown` (from AUTHOR.MD :: NikBearBrown per SKILL.md §Step 4). Narration adds "Find more at Nik Bear Brown on YouTube." `OutroCTA.line`, `tail_silence_s`, and pattern preserved.
- **Metadata:** `_variant_todo` removed. Scaffold fields (`audience=NikBearBrown`, `engine=kokoro`, `voice_kokoro=am_onyx`, `palette=teardown`, `register=Teardown`, `typography`, `outro_source`, `derived_from`) left exactly as the scaffold set them.

## Judgement calls

1. **Two your-turn beats back-to-back (BHTF + B_LLM).** The source's BHTF was already a paste-ready prompt for Claude Code specifically (a build-and-audit task). SKILL.md §Step 3 requires a *separate* LLM-exercise beat second-to-last that produces useful output on its own with any frontier LLM. Chose to keep BHTF unchanged in slot (preserve beat_id + shot per instructions) and insert a new distinct B_LLM — a design-analysis prompt, not a build prompt. They complement rather than duplicate: BHTF says "build one and audit whether CLAUDE_PLUGIN_ROOT was used"; B_LLM says "explain the runtime-variable trade-off and the silent-failure bug class it creates." A merge would have lost the shot-block preservation rule and cost the video its Claude-Code-specific hands-on beat. Same call the sibling `nbb-claude-code--claude-liam-plugin-structure` conversion made.
2. **BHTF's `folderLabel: "@HumanitariansAI"` kept** even though the audience is now NikBearBrown. Instructions say preserve shot blocks exactly; the BHTF shot is not the outro. The mismatch (voiced as NBB, on-screen chip @HumanitariansAI) is inherited from the scaffold and shows up in every nbb- variant of a hai-simple reel — flagging for downstream, not fixing here.
3. **BOUT handle changed to `@NikBearBrown`.** Step 4 explicitly replaces the outro with the NikBearBrown outro, so the handle in `OutroCTA` props is fair game. `nbb.md` names `www.brutalist.art` as the *default* channel, but per SKILL.md §Step 4 the outro content comes from `AUTHOR.MD :: NikBearBrown`, and that section's YouTube handle is `@NikBearBrown`. Went with AUTHOR.MD, matching the sibling conversion.
4. **B01 length inflated modestly.** Source B01 was 26 estimated seconds; Teardown pass added the "they optimized for zero boilerplate at the cost of one thing" line to plant the design-trade axis that B02 and B03 later pay off. Kept `estimated_duration_s: 26` — the actual will be re-measured on Kokoro pass, per audio-first rule.
5. **`CLAUDE_PLUGIN_ROOT` left as one token, not spelled letter-by-letter.** Source narration already uses "CLAUDE_PLUGIN_ROOT slash scripts slash check dot sh" — Kokoro handles the underscore-cap-cap-cap env-var pattern acceptably in am_onyx tests; only the punctuation gets spelled ("slash", "dot sh"). Kept that convention throughout the rewrite.
6. **BCRY carry-out sentence kept semantically identical.** The source line is already a flat Teardown principle ("Never hardcode X. Write it through Y, so it survives Z"). Only replaced the contraction "plugin's installed" → "plugin is installed" in the narration so the on-air read is unambiguous; on-screen `quote` and `sparkLine` preserved verbatim so the card matches the source reel.

## Ending order verified

`B00 → B01 → B02 → B03 → BCRY → BHTF → B_LLM (LLM EXERCISE) → BOUT (outro)` — LLM exercise is second-to-last, NikBearBrown outro is last.

## Not done (out of scope per supervisor)

No audio generated, no compile, no render. Deliverable is `beat_sheet.nbb.json` only.
