# CONVERT-LOG — claude-tag-plugins--claude-liam-pagerduty-api → nbb

Source register: **Plain** (hai-simple). Target register: **Teardown** (Feynman × MKBHD).

## What changed

- **Every `narration_text` rewritten in Teardown register.** Facts, numbers, hostnames,
  headers, HTTP status codes, endpoint paths, script names, rate-limit numbers, and the
  visual/prop blocks are unchanged. Voice only.
- **Register moves added, one per beat, not multiple:**
  - **B00** — reframed as "Natural guess … fails silently. Why the split?" instead of
    "Someone assumes …". Keeps the >=20-word window for the WRITER LAW; the on-screen
    TOKEN → ROUTING KEY correction still lands.
  - **NB01** — named the design choice out loud: Events v2 optimized for volume
    (POST-from-anywhere, no long-lived credential); REST is the opposite bet
    (fewer callers, more sensitive operations). Underlying alert-service-escalation-
    incident mechanism preserved verbatim.
  - **NB02** — added one Teardown line: "They optimized error responses for machines,
    not for people staring at a terminal." Explains why the 401 comes back empty
    without smuggling in a fact.
  - **NB03** — three trade-offs made explicit: strongly-typed objects (boilerplate ↔
    ambiguity); plain-text errors (volume ingestion ↔ tidy parsing); REST vs Events v2
    rate-limit visibility. Numbers unchanged (960/min).
  - **BCRY** — opened with "Here's what's actually happening." Kept the two-API +
    empty-body carry-out sentence intact and mirrored it into the `WantQuote.quote`
    prop so the on-screen quote matches the narration.

## LLM exercise beat (second-to-last)

Reused **BHTF** as the LLM exercise beat rather than inserting a new one, because the
source beat already carried a paste-ready Claude/ChatGPT/Gemini prompt and its own
`ClaudeComposerAsk` rendering. Changes:

- `act` moved from `"your turn handoff"` to `"LLM EXERCISE"`.
- Added an `llm_exercise` block with `prompt` (unchanged from source) and `dig_deeper`:
  *"if you were designing a monitoring API from scratch, would you split reading and
  alerting the way PagerDuty did — and what would you give up either way?"* — a real
  next question about the design choice the video just took apart, not a summary.
- Narration now reads the prompt aloud with viewer, then delivers the "Go deeper" line.
  Removed the "Liam, in for Bear." trailing sign-off from BHTF to keep that sign-off
  unique to BOUT.
- `ClaudeComposerAsk.command` prop unchanged (still shows the paste-ready prompt).

## Outro (last)

**BOUT** kept as the final beat. Matches the reference nbb reels in this collection
(`nbb-cwc-workshops--claude-liam-reorder-policy`, `nbb-financial-services--claude-liam-
deal-sourcing`): "Title. Liam, in for Bear." sign-off on the existing `OutroSeries`
pattern, `@HumanitariansAI` eyebrow. Did **not** swap to `www.brutalist.art` — this reel's
`channel_title` is `@HumanitariansAI` and Liam is signing in for Bear on that channel; the
`outro_source: AUTHOR.MD :: NikBearBrown` metadata is preserved to record the register.

## Judgement calls

1. **BHTF as LLM exercise vs a new B_LLM beat.** Chose to repurpose BHTF because
   (a) it already renders a paste-ready Claude prompt with `ClaudeComposerAsk`, and
   (b) inserting a new beat would leave BHTF as a duplicate "your turn" beat with no
   fresh visual. The nbb SKILL.md's Step 3 schema is satisfied by adding the
   `llm_exercise` block and the "Go deeper" line to BHTF.
2. **Outro pattern.** Kept `OutroSeries` (source pattern) instead of switching to
   `OutroCTA`. Task rule: "Preserve exactly … `shot` blocks." The reference reels
   diverge on this — some use OutroCTA — but staying with the source honors the
   shot-block preservation rule.
3. **Graphic palette hex codes.** Left the manim `graphic.production_viz.colors`
   values as-is (`#F3EBDD` ground, `#E4572E` accent). Those hexes are baked into the
   already-rendered `manim/*.mp4` files; the nbb pass re-voices, it doesn't re-render.
   Palette is set to `"teardown"` at the metadata level, which is what future
   compilations read.
4. **Duration estimates.** NB01/NB02/NB03 rewrites run ~10-20% longer than the source
   estimates because the added trade-off sentences take real seconds. Actual durations
   come from re-running Kokoro; the estimates are informational only.

## Gates

- Valid JSON — ✅ (`python3 -c "json.load(...)"` clean).
- Every narration rewritten — ✅ (7/7).
- LLM exercise second-to-last — ✅ (BHTF, `act: "LLM EXERCISE"`, `llm_exercise` block present).
- NikBearBrown outro last — ✅ (BOUT, "Liam, in for Bear.").
- `_variant_todo` removed — ✅.
- `beat_id` / `shot` / `graphic` / on-screen card copy preserved — ✅.
