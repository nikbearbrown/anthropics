# CONVERT-LOG — claude-for-legal--claude-liam-cease-desist → nbb

Source: `../claude-for-legal--claude-liam-cease-desist/beat_sheet.json` (Plain register, hai-simple)
Target: `beat_sheet.nbb.json` (Teardown register, NikBearBrown cut)

## What changed

- **Every narration rewritten in Teardown register** (B00, NB01, NB02, NB03, BCRY, BOUT). Feynman × MKBHD lens: explain the machinery (SKILL.md is a folder of plain-text steps), name the design choice (auditability over cleverness), name what the choice costs (verbosity, no branching), name the trade-off in the attorney-work-product step (the header follows the audience, not the topic).
- **Facts preserved verbatim**: SKILL.md is one file, plain language, no hidden logic; instructions live under a Steps heading; linear execution with per-step branching only; three internal artifacts (draft, pre-send brief, triage memo) get the attorney-work-product label; the outgoing letter does not, because it is written for the other side.
- **B00 timing preserved**: rewrite is 32 words → fits the 20-35 word window for the >=9s writer typing gag. Trigger word `deciding` retained; correction `following steps` retained. The visual gag lands unchanged.
- **BCRY WantQuote synced**: both the on-screen `quote` prop and the narration carry the same rewritten carry-out sentence; `sparkLine` updated to "Executes the file. Only the file."
- **BHTF repurposed into the LLM EXERCISE beat** (SECOND-TO-LAST). `act` → `LLM EXERCISE`. Added `llm_exercise` object with a paste-ready prompt for any frontier LLM (Claude / ChatGPT / Gemini) plus a "go deeper" follow-up. The prompt is answerable without the video — it asks the model to teach a well-formed cease-and-desist and route which artifacts get the attorney-work-product header. Composer `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…".
- **BOUT switched to `OutroCTA`** (`line` + `handle` props), matching the mainline nbb pattern in this batch (see `nbb-books--claude-liam-building-plugins`). Narration is the "Liam, in for Bear" signoff with the subtitle folded in.
- **`_variant_todo` removed** from metadata (scaffold checklist retired).

## Judgement calls

- **LLM exercise prompt scope.** The Anthropic cease-desist Skill is not something a frontier LLM (Claude.ai / ChatGPT / Gemini) has installed. The prompt is written so the model can produce a genuinely useful output from its own legal-writing training — teach what a well-formed cease-and-desist does, route the artifacts to the right privilege header — instead of trying to invoke a skill it doesn't have. That is the point of the LLM-exercise beat per `skills/make/nbb/SKILL.md` §Step 3.
- **`_variant_todo` items not applied here**: audio regeneration + compile (excluded — conversion pass only, no render).
- **Metadata channel kept as `@HumanitariansAI`**, not switched to `www.brutalist.art`. The source reel and the sibling nbb reels in this batch (`nbb-books--claude-liam-*`) all publish under `@HumanitariansAI`; `brands/nbb.md`'s "default channel: `www.brutalist.art`" is a fallback for reels that don't already carry a channel. Not changing what the batch has already established.
- **NB01–NB03 durations grew** vs source (14/13/17s → 16/18/22s estimated). Teardown expansion — naming the design choice adds words — but each rewrite stays under the ~19s ceiling seen in the reference `nbb-books--claude-liam-building-plugins` conversion.
