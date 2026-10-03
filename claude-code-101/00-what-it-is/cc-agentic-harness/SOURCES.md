# SOURCES — cc-agentic-harness

## The runs (primary — everything on screen)

`SESSION.md` — six headless Claude Code 2.1.150 runs on 2026-09-08 in one scratch git repo: A (`--tools ""`, connectors attached), A2 (`--tools "" --strict-mcp-config`), B (`--allowedTools Read,Write,…`), and loop1–3 (`for i in 1 2 3`, `--allowedTools Read,Write,Edit --strict-mcp-config`). Raw stream-json for each in `evidence/`; the loop's files and diff in `evidence/`; `evidence/transcript.txt` is the harvested transcript.

Costs as reported by the CLI (recorded, not spoken): A $0.725, A2 $0.037, B $0.136, loop1 $0.144, loop2 $0.130, loop3 $0.130.

## The concept (what this reel is a cc-explainer *of*)

Bear's brief, 2026-09-08: film 00 of Claude Code 101 should be "Claude Code is an agentic harness. What is that?" — the three-layer idea (prompt engineering → context engineering → harness engineering) and the loop with fresh context per pass. Bear pointed at a third-party YouTube explainer as the concept reference; nothing from it is quoted or paraphrased (see `FACTCHECK.md` → Not used).

Public background for the terms, from Anthropic's engineering blog: *Building effective agents* (the augmented LLM; workflows vs agents; the agentic loop), *Effective context engineering for AI agents*, and *Effective harnesses for long-running agents* (fresh context per session, a feature list and progress file as the memory between sessions — the pattern the ten-line loop in B04 is a toy of). Cited as background; every on-screen fact is from the runs.

## Doctrine behind the two closing-block beats (SKEPTIC retired 2026-09-08)

| Beat | Course | Chapters used |
|---|---|---|
| B09 CONDUCT | `info-7375-conducting-ai` + the Gru consultant spec | `02-the-solve-verify-asymmetry.md`; the five capacities; the Boondoggle Score; the dangerous middle |
| B10 HUMAN | `info-7375-irreducibly-human` | `04-tier-4-metacognitive-and-supervisory.md` |

Distilled in `brutalist-art/skills/make/cc-explainer/reference/three-beats.md`.

## Interface

The Claude Code kit — `brutalist-art/runtime/remotion/src/scenes/CC*.tsx`, `tokens/claudecode.ts`, `scenes/CC-TEMPLATES.md`. `CCHarnessMap` was built for this reel (B07). B04's plain shell is `CCPlainShell` (a dark plain terminal, no Claude chrome — built while fixing the first GATE T failure on `cc-five-claudes-explained`).

## Media, assets, provenance

No pantry, no archive, no generated media, no real person depicted. Narration: Kokoro `am_onyx` (Liam, in for Bear) on every beat — LIAM LAW.

## Credits

Sessions and narration: Liam, in for Bear. Channel: @NikBearBrown. Playlist: Claude Code 101 (film 00).
