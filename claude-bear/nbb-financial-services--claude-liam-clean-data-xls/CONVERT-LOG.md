# CONVERT-LOG — financial-services--claude-liam-clean-data-xls

Source register: **Plain** (per source `beat_sheet.json` metadata; scaffold said Teardown, but source narration was Plain).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: clean-data-xls runs six fixed steps in order — trim whitespace, fix inconsistent casing, convert numbers stored as text, standardize dates, remove duplicates, flag mixed-type columns; the anchor is one Revenue column holding a padded '1,200', a bare '1300', an 'N/A', and a padded '1,400.00' traveling raw → trimmed → converted → flagged (N/A blocks conversion), then stopping; the currency-confusion example (one dollar sign, two different currencies) is not on the checklist so the column comes out as ambiguous as it went in; B03 both-directions — a clean conversion isn't accuracy (a typo that dropped a zero converts just as cleanly), and a mixed-type flag isn't a broken-column verdict (an ID column that mixes letters and numbers on purpose gets the same flag).
- **B00**: added the IN-FOR-BEAR line ("Liam here, in for Bear") in the cold open so the persona is spoken up front, matching sibling nbb-audit-xls. 30 words — inside the WRITER-LAW 20–35 window; typing visual + `lead_silence_s: 0.8` unchanged.
- **B01**: explicit design-critic line added — "They optimized for a mechanical pass that runs the same way every time at the expense of the human eye that would look at 'dollar sign' and ask 'which dollar?'" Currency example sharpened to name USD vs CAD instead of the source's generic "two different currencies" — same fact (same symbol covers different currencies, not on the checklist), one concrete beat viewers can picture.
- **B02**: added the order-matters aside ("you can't dedupe rows that look different only because one has extra whitespace, so trim comes first") — mechanism-first Teardown, doesn't change the six steps or their order. Kept the anchor's four values as literal strings.
- **B03**: kept both-directions structure; sharpened to "Reformatted is not correct. Flagged is not broken." — the design-critic form of the source's paired claim. Cited concrete IDs ('A47' / '1500' / 'X001') the source note referenced but the source narration didn't spell out.
- **BCRY**: on-screen `WantQuote.quote` re-synced to the new narration; `sparkLine` "Reformatted, not fact-checked." kept — already Teardown-shaped.
- **BHTF**: converted from "your turn handoff" to an **LLM EXERCISE** beat (SKILL.md §Step 3). Added `llm_exercise: { prompt, dig_deeper }` with a paste-ready six-row Revenue column (padded, bare, N/A, comma-decimal, USD, CAD) plus a mixed ID column — designed so any frontier LLM can walk exactly which rows the six-step checklist transforms, which columns get flagged, and (the punch line) which of the viewer's problems the checklist does nothing about. Narration now names the exercise, walks the paste-ready ask, closes with the "Go deeper:" follow-up, then "Liam, in for Bear." `ClaudeComposerAsk.command` rewritten to mirror the paste-ready prompt so the on-screen composer shows what the viewer would paste. Second-to-last position preserved.
- **BOUT**: NikBearBrown outro. Narration reads the URL ("Brutalist dot art."), OutroCTA `handle` → `@NikBearBrown`, `line` → `"What Does Claude Actually Do When You Say \"Clean This Data\"? Liam, in for Bear. www.brutalist.art"`. `estimated_duration_s` bumped 6 → 8 for the added URL.

## Judgement calls

- **Kept `metadata.folderLabel` / `channel_title` = `@HumanitariansAI`** and left the BHTF `ClaudeComposerAsk.folderLabel` at `@HumanitariansAI`. SKILL.md is explicit only about the *outro* handle → NikBearBrown. The composer chip is on-screen source-context copy for a body beat; preserving it matches the sibling nbb-audit-xls conversion. Only BOUT's rendered chrome moves to `@NikBearBrown`.
- **Preserved graphic color hexes** on B01–B03 (`#F3EBDD` / `#E4572E` / `#1F4E5F`). These are shot-planning reference colors, not the render palette; the render palette is set by `metadata.palette: "teardown"`. Sibling reel handled the same way — no palette-hex edit inside the graphic blocks.
- **Named USD/CAD explicitly in B01 and in the LLM exercise.** The source's "two different currencies" is the true fact — I picked USD/CAD because they concretely share the dollar symbol on the page, which is the whole point of the beat. Not a fact change; a concretization the Teardown register calls for ("Here's what's actually happening…" beats "two different currencies").
- **Bumped `estimated_duration_s` on the rewrites that grew.** B01 25 → 50 (added design-critic clause + a concrete USD/CAD line), B02 22 → 40 (added the order-matters aside and made the anchor values literal), B03 27 → 50 (added the '12,000' typo example and named IDs), BHTF 27 → 55 (paste-ready prompt + dig-deeper materially lengthen the read), BOUT 6 → 8 (added the URL). Clock is measured audio (`clock: narration`), so these are loose planning hints that get overwritten by real durations when `generate_audio_kokoro.py` runs; kept them honest so they don't lie by tens of seconds.
- **BHTF `act`** relabelled `"your turn handoff"` → `"LLM EXERCISE"` per SKILL.md schema.
- **No new beat inserted.** BHTF already occupied the "paste this into Claude" second-to-last slot with the right `ClaudeComposerAsk` shot; adding a separate LLM card would have been redundant. Converted the existing beat in place — same call the sibling nbb-audit-xls made.

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
