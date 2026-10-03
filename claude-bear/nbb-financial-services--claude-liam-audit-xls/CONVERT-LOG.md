# CONVERT-LOG — financial-services--claude-liam-audit-xls

Source register: **Plain** (per source_note; scaffold said Teardown but source narration was Plain).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: audit-xls audits for formula accuracy, errors, and common mistakes; scopes to a range, a single sheet, or the whole model; checks BS balance first because everything downstream is suspect if it's off; the anchor is a balance sheet off by $1,200 traveling scope-set → BS-checked-first → mismatch-found → cited/reported, then stopping; clean BS pass ≠ error-free (formula errors elsewhere audited separately); BS-imbalance flag ≠ every downstream number wrong (unverified, not confirmed incorrect); nothing in the sheet is ever rewritten.
- **B00**: added the IN-FOR-BEAR line ("Liam here, in for Bear") in the cold open so the persona is spoken up front, matching sibling nbb-3-statement-model. 32 words — inside the WRITER-LAW 20–35 window; typing visual + `lead_silence_s: 0.8` unchanged.
- **B01**: explicit design-critic line added — "They optimized for a traceable finding at the expense of the fix itself." Facts identical to source.
- **B02**: added scope enumeration ("a range, one sheet, or the whole model") that the source note flagged as a preserved fact but the source B02 narration omitted; kept the anchor cash figure at $1,200 to match the graphic.
- **B03**: kept both-directions structure; sharpened to "Balanced isn't right. Off isn't wrong." — the design-critic form of the same claim.
- **BCRY**: on-screen `WantQuote.quote` re-synced to the new narration; `sparkLine` "Flagged and cited, not fixed." kept — already Teardown-shaped.
- **BHTF**: converted from "your turn handoff" to an **LLM EXERCISE** beat (SKILL.md §Step 3). Added `llm_exercise: { prompt, dig_deeper }` with a paste-ready toy model (broken `SUM` on gross profit + a $5,000 BS gap) that will produce concrete audit output on its own. Narration now names the exercise, walks the paste-ready ask, closes with the "Go deeper:" follow-up, then "Liam, in for Bear." `ClaudeComposerAsk.command` rewritten to mirror the paste-ready prompt so the on-screen composer shows what the viewer would paste. Second-to-last position preserved.
- **BOUT**: NikBearBrown outro. Narration reads the URL ("Brutalist dot art."), OutroCTA `handle` → `@NikBearBrown`, `line` → `"When Claude Audits a Spreadsheet, Does It Fix Anything? Liam, in for Bear. www.brutalist.art"`. `estimated_duration_s` unchanged at 7.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` = `@HumanitariansAI`** and left the BHTF `ClaudeComposerAsk.folderLabel` at `@HumanitariansAI`. SKILL.md is explicit only about the *outro* handle → NikBearBrown. The composer chip is on-screen source-context copy for a body beat; preserving it matches the sibling nbb-3-statement-model conversion. Only BOUT's rendered chrome moves to `@NikBearBrown`.
- **Preserved graphic color hexes** on B01–B03 (`#F3EBDD` / `#E4572E` / `#1F4E5F`). These are shot-planning reference colors, not the render palette; the render palette is set by `metadata.palette: "teardown"`. Sibling reel handled the same way — no palette-hex edit inside the graphic blocks.
- **Bumped `estimated_duration_s` on the rewrites that grew.** B01 24 → 30, B02 18 → 28, B03 24 → 30, BHTF 23 → 40 (the paste-ready prompt + dig-deeper materially lengthen the read). Clock is measured audio (`clock: narration`), so these are loose planning hints that get overwritten by real durations when `generate_audio_kokoro.py` runs; kept them honest so they don't lie by ~10s.
- **BHTF `act`** relabelled `"your turn handoff"` → `"LLM EXERCISE"` per SKILL.md schema.
- **No new beat inserted.** BHTF already occupied the "paste this into Claude" second-to-last slot with the right `ClaudeComposerAsk` shot; adding a separate LLM card would have been redundant. Converted the existing beat in place — same call the sibling nbb-3-statement-model made.
- **B01's original `shot` block did not carry a nested `graphic`** (source had it as a sibling of `shot` at the beat level). A first draft here accidentally duplicated the `graphic` object inside `shot`; corrected — the beat now has one `graphic` at the top level, matching B02/B03 and the source.

## Ending order (verified)

```
B00  hesitant writer cold open
B01  wrong guess, falsified
B02  mechanism / anchor planted
B03  anchor payoff / both directions
BCRY carry-out
BHTF LLM EXERCISE            ← second-to-last
BOUT outro (NikBearBrown)    ← last
```

## Not done (out of scope)

- No audio regenerated. No render. No compile. Downstream `generate_audio_kokoro.py` + `compile.py` still needs to run.
