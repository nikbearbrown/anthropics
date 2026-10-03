# CONVERT-LOG — nbb :: claude-quickstarts--screenshot-prompt-caching

**Converted:** 2026-09-03
**Source:** `../claude-quickstarts--screenshot-prompt-caching/beat_sheet.json` (Plain register, hai-simple, 8 beats)
**Deliverable:** `beat_sheet.nbb.json` (Teardown register, LLM EXERCISE beat, NBB outro)

## What changed

- **All 8 `narration_text` rewritten in Teardown register** (Feynman × MKBHD). Machinery first, statelessness named as the design choice, `cache_control: {type:'ephemeral'}` explained as an opt-in trade — ninety-percent off on repeats, at the cost of a memory that dies with the key or the idle timer. Every number, API field, and file path from the source survives verbatim (50 turns, ~2000 tok/screenshot, 5 states A–E, 100k → 10k tokens, 90% saved).
- **Cold open (B00):** added "Liam, in for Bear." per IN-FOR-BEAR LAW.
- **BHTF converted into the LLM EXERCISE beat.** Kept `beat_id: BHTF` (preserve-rule); changed `act` → `"LLM EXERCISE"`; added `llm_exercise: {prompt, dig_deeper}` block; rewrote narration to read the paste-ready prompt aloud and land the "go deeper" question; updated ClaudeComposerAsk `command` to match the prompt on screen and `segment` → `"LLM Exercise"`.
- **BOUT rewritten as the NBB outro.** Teardown sign-off line, handle updated to `@NikBearBrown`, brutalist.art called out (default channel per SKILL). Duration bumped 6 → 9 s to fit the new line.
- **`folderLabel` / `channel_title` in metadata + on BHTF ClaudeComposerAsk:** `@HumanitariansAI` → `@NikBearBrown` (NBB cut belongs to the @NikBearBrown channel).
- **`_variant_todo` removed** from metadata (all five items done).
- **BCRY WantQuote left intact** — the carry-out already reads as Teardown (names the mechanism, admits the limit); on-screen quote matches narration, so no edit earned.

## Judgement calls

- **Kept `beat_id: BHTF`** rather than rename to the SKILL example's `B_LLM`. The task's preserve-rule on beat_id outweighed matching the schema example's slug. Function and `act` were changed to `"LLM EXERCISE"` per Step 3; the `llm_exercise` block is present in the shape the SKILL prescribes.
- **Left the Remotion palette props on B00 (BrutalistHesitantWriter: `bg #F3EBDD`, `ink #2F2A26`, `accent #E4572E`) unchanged**, and left the Manim `graphic.production_viz.mechanic` HAI color notes unchanged. `palette: "teardown"` is set in metadata; skinning to teardown white / ink / crimson is the render pass's job, not this conversion's. Touching individual prop colors would half-skin the sheet.
- **Left `metadata.ground: "#F3EBDD"` alone** for the same reason — it's a source-inherited hint, and `palette: "teardown"` is the authoritative signal downstream.
- **Left every `build.status / src` block untouched.** The scaffold carried through the source's rendered paths; per prompt ("You do NOT render, compile, or generate audio"), resetting them is the build pass's call, not this one.
- **Estimated durations bumped where narration grew** (B01 21→24 s, B02 18→21 s, B03 19→22 s, B04 22→26 s, B00 14→15 s, BHTF 22→30 s, BOUT 6→9 s). Kokoro will re-measure at build time; these are hints, not clocks.

## Ending order (verified)

```
… body …
BCRY  (6 CARRY-OUT)
BHTF  (LLM EXERCISE)   ← second-to-last
BOUT  (outro)          ← last
```

JSON validates (`python3 -m json.tool`).
