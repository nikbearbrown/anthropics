# ACTS.md — Agents and Frameworks (Film 8 of 12)

**Exact title:** Agents and Frameworks

**Core promise:** By the end, the viewer can drop Muse into the agent tools
they already use — the Anthropic agent SDK, LangChain, and even Claude Code —
and tell the difference between "compatible" and "native".

**Structure:** hook + key terms + three acts (9 body beats) + recap + your
turn + outro. 14 beats, ~280 s (~4m40s).

- **Hook (BIDEA):** drop Muse into the tools you already use.
- **Key terms (BDEFS):** Agent SDK · Framework · Harness · Wrapper.
- **Act 1 — The agent SDK (3 beats):** B01 the Anthropic agent SDK,
  Muse-style (plan, call tools, iterate); B02 the coding task (tic-tac-toe
  in Ruby: game state, win checking, game loop); B03 the result — a finished
  game, from a description.
- **Act 2 — LangChain (3 beats):** B04 LangChain in TypeScript via the
  OpenAI-compatible integration; B05 the one config block (base URL, API
  key, model name); B06 debugging with the agent SDK's help — the loop reads
  as well as writes.
- **Act 3 — Claude Code on Muse (3 beats):** B07 the wrapper script
  (Meta API key via env, launching Claude Code on Muse Spark 1.2); B08 the
  launch and the small refactor task; B09 the honest verdict — it works,
  but it looks odd.
- **BVDT:** exactly 3 lines, one per act.
- **BHTF:** point one tool you already use at the Muse base URL; run the
  smallest real task; ask whether it just worked or looked odd.
- **BOUT:** "Muse, in for Bear. Thanks for watching." + teaser for Film 9
  (Muse Code, the Harness).

**Tone:** workshop-like, builder-to-builder. The film celebrates what
compatibility unlocks and is honest about where it stops.

**What this film is not:** not an agent-SDK tutorial; not a LangChain
tutorial; not a verdict on which framework is best. It is about the move —
pointing tools you already know at a new model — and its limits.

**Cast per act (one look):** white cards with ink borders carry every label;
loop nodes (B01) are small cards with arrows; the tic-tac-toe grid (B03) is
ink lines with blue X / terracotta O marks; the config card (B05) fills row
by row; act 3 is terminal cards and the two-verdict split ("it works" /
"it looks odd", tilted).

**Source facts:**
- The Anthropic agent SDK drove a coding task: tic-tac-toe in Ruby.
  (transcript §10)
- LangChain in TypeScript, via the OpenAI-compatible integration; env
  config; debugging with the agent SDK's help. (transcript §11)
- A wrapper script injected the Meta API key via env and launched Claude
  Code on Muse Spark 1.2; the task was a small refactor. (transcript §12)

**LEFT OUT (with reasons):**
- The exact env-var names and config syntax — not in the outline; the film
  shows the three fields (base URL, API key, model name) as a card, not a
  copy-paste recipe.
- Any version numbers for LangChain or the SDKs — unverifiable from the
  outline; cut.
- The full tic-tac-toe game — the film shows five marks, enough to read
  "finished"; a whole game adds nothing.
- Muse Code itself — that's Film 9's subject; here Claude Code is the
  contrast case.
