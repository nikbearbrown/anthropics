# SOURCES — show-tell-choosing-the-right-claude-model

**What this is.** The sources behind every claim in the film, and how each was read. **Why.** Bear sent six screenshots of Anthropic's "Choosing the right Claude model" guide as the source and the visual inspiration; anything beyond them had to come from a live Anthropic page, fetched raw and attributed. **Found.** The guide and the live pages agree on everything the film uses. The live developer docs add the one piece of practical advice the film gives beyond the cards (start efficient and upgrade, or start strong and move down), attributed aloud. The docs also say "Most workloads start with Claude Opus 5.5" for API workloads, so the film does not turn the guide's "Sonnet … can handle most problems" into "start with Sonnet".

## 1. Anthropic's guide (primary; attributed as "the guide" / "Anthropic's guide")
`SOURCE-SCREENSHOTS.md` transcribes the six PNGs in `source/` (sha256 prefixes: 01 cover `c2ec24f0`, 02 summary `8119e859`, 03 Fable `7d64cca5`, 04 Opus `c267401b`, 05 Sonnet `5b4260b7`, 06 Haiku `0bcd66d5`). The PNGs were looked at directly; the transcription matches them. The screenshots carry no URL or date, so the film says "Anthropic's guide" and never says where or when it was published. Used: each model's tagline, one-line description and "Best for" list; the cover's tabbed folders and pointer as the visual motif.

## 2. Live Anthropic pages (fetched raw with curl on 2026-09-27, HTTP 200, saved in `sources/`)
- `live_2026-09-27_docs_choosing_a_model.md`, from https://docs.claude.com/en/docs/about-claude/models/choosing-a-model.md (redirected to platform.claude.com, `text/markdown`, sha256 `ea49c730…`). Used, attributed as "Anthropic's developer docs": Option 1 (start efficiency-first, "Upgrade only if necessary") and Option 2 (start capability-first with "the strongest starting point for your task", then move to more efficient models "over time"). Also read for context, not quoted: the selection matrix and the step-5 line that points to Fable when Opus falls short on long-horizon work (supports B06 without being spoken).
- `live_2026-09-27_docs_models_overview.md`, from https://docs.claude.com/en/docs/about-claude/models/overview.md (sha256 `404372e6…`). Read for context only.
- `live_2026-09-27_anthropic_claude_{fable,opus,sonnet,haiku}.html` from https://www.anthropic.com/claude/{fable,opus,sonnet,haiku}, with the visible text extracted beside each as `.txt`. Used only to confirm that all four model families are current and which plans list Fable and Opus (the "if you can" in the Your Turn check). Nothing from them is quoted.

No WebFetch summary was used for any claim.

## Left out, on purpose
- Every price, cache-read figure and "costs x% less" line on the model pages.
- Benchmark numbers (e.g. the Haiku page's SWE-bench figure), speed and latency figures, fast mode, context windows.
- Version numbers (Fable 5.1, Opus 5.5, Sonnet 5, Haiku 4.5): the guide uses bare names and so does the film.
- Mythos (not in the guide).
- The effort parameter (in the docs; not needed to choose among the four).
- The small four-circle rows on each card (unreadable in the screenshots).
- The guide's sage and lilac card colours (off the Claude palette).

## Cast and patterns reused
The ISO KIT, the midpoint guard (`ST`/`guard`, 0.22 s margin), `done()`, the grey "you" figure, the slip, the lens and the cursor shape, and `build_srt.py`, from `show-tell-what-is-claude-code/`. The four standing file folders with staggered tabs, the travelling spark, the email page, the study stack, the step chain and the step arrows are new.
