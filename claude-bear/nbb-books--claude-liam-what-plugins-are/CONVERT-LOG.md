# CONVERT-LOG — Plain → Teardown (nbb) for `books--claude-liam-what-plugins-are`

Converted `beat_sheet.json` (Plain, hai-simple) into `beat_sheet.nbb.json` (Teardown, NBB).
Voice, facts, beat IDs, shot blocks, on-screen cards preserved. `_variant_todo` removed.

## What changed

- **Every `narration_text` rewritten in Teardown register** (Feynman × MKBHD): each beat
  names the mechanism, names what the design optimized for, and where useful names the
  trade-off — "Here's what's actually happening…", "They optimized for X at the expense
  of Y", "The trade is transparency for tidiness." No facts moved.
- **BHTF turned into the LLM exercise beat** (already the second-to-last beat + already
  a paste-ready prompt). Added the structured `llm_exercise` field with `prompt` and
  `dig_deeper`, and appended a real "Go deeper: …" follow-up onto the narration.
  Broadened the ask surface to Claude / ChatGPT / Gemini (per SKILL.md §Step 3 —
  paste-into-any-frontier-LLM prompt, not a CLI command). Bumped
  `estimated_duration_s` from 22 → 30 to cover the added dig-deeper line.
- **BOUT tightened to the standard NBB outro line**: "Claude, Equipped. Liam, in for
  Bear." (was "Claude, Equipped — what a Cowork plugin actually gives you. Liam, in
  for Bear."). Matches the sibling nbb-* precedent — `nbb-financial-services--claude-liam-deal-sourcing`,
  `nbb-cwc-workshops--claude-liam-reorder-policy`, `nbb-claude-basics--screenshot-prompt-caching`
  all use "Claude, [Title]. Liam, in for Bear." as `line` + `narration_text`. Kept
  `pattern: OutroCTA` and `handle: @HumanitariansAI` as scaffolded.
- **BCRY narration kept verbatim.** The source carry-out sentence is already the exact
  line signed off in `CARRY-OUT.md` and already reads in the Teardown register — it
  names the design ("doesn't make Claude know more — it makes Claude equipped") and
  hands the judgment back to the reader. Rewriting it would just fabricate variance.
- **Metadata `purpose` field** updated from "Plain register" → "Teardown register" so
  the field reflects what the beat sheet is now.

## Judgement calls

1. **No new `B_LLM` beat inserted.** SKILL.md §Step 3 shows an idealised `beat_id:
   "B_LLM"` schema, but the invocation also says to "preserve every `beat_id`" and the
   source already has a second-to-last "paste this into Claude" beat (BHTF). Every
   sibling nbb-* sheet in `claude-bear/` follows the same pattern — BHTF *is* the LLM
   exercise beat, no separate B_LLM. I kept the beat_id BHTF and attached the
   `llm_exercise` structured field to it. Precedent + "preserve every beat_id" both
   pointed the same way.

2. **Kept the source's `folderLabel: @HumanitariansAI` and `handle: @HumanitariansAI`
   in the outro.** Every sibling nbb-* sheet in this book (`nbb-financial-services--*`,
   `nbb-cwc-workshops--*`, `nbb-claude-basics--*`) also carries `@HumanitariansAI` on
   the outro even though `audience: NikBearBrown`. This is the Cowork-plugins book
   series' established convention (channel + audience decouple: NBB register, HAI
   channel). Not touching it unilaterally.

3. **B00 cold-open narration keeps the pivotal `smarter → equipped` structure**, since
   `BrutalistHesitantWriter` has `triggerWords: "smarter"` / `replacementWords:
   "equipped"` hard-wired to the audio-visual sync. Rewrote around those two anchor
   words rather than through them.

4. **NB11 rewrite includes "This works if you value X; it fails if you need Y"** — a
   direct hit on the PROSE.md preferred-phrases list, applied to the "customize
   yourself vs. expect magic on install" trade-off. No new fact — just names the
   trade the source already implies.

## Order verified

```
B00 → NB01..NB14 → BCRY → BHTF (LLM exercise) → BOUT (NBB outro)
```

18 beats, matches source beat_ids one-for-one.

## Not done here

Not rendered. No audio regenerated, no compile, no publish. Deliverable is
`beat_sheet.nbb.json` only, per the register-conversion factory contract.
