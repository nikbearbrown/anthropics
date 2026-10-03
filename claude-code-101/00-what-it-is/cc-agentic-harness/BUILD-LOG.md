# BUILD-LOG — cc-agentic-harness

cc-explainer · Claude Code 101 · tier `00-what-it-is`, **film 00** (Bear, 2026-09-08:
"film 00 should be Claude code is an Agentic harness. What is that?") · Liam, in for
Bear (Kokoro `am_onyx`) on every beat — LIAM LAW · Teardown · 16:9 · built 2026-09-08.

## What this reel is

Bear pointed at a third-party YouTube explainer on "harness engineering" as the
concept reference. Its idea — prompt engineering → context engineering → harness
engineering; the loop with a fresh context per pass — is shown here from six real
Claude Code runs. Nothing from the video is quoted or paraphrased; its history and
product claims are not repeated (`FACTCHECK.md` → Not used). Anthropic's own
engineering posts on agents, harnesses and context engineering are named in
`SOURCES.md` as the public background for the terms.

## The runs (REAL-SESSION LAW)

All headless `claude -p`, Claude Code 2.1.150, one scratch git repo. The same ask
("Create a file named hello.txt … containing exactly one line: hello") three ways,
then a loop:

| Run | Flags | What happened |
|---|---|---|
| A2 | `--tools "" --strict-mcp-config` | `"tools": []`. Claude: "Creating the file now." One turn, 48 output tokens, **no file**. |
| A | `--tools ""` (connectors still attached) | 140 `mcp__…` tools, no `Write`. Claude called `mcp__claude_ai_Google_Drive__create_file` → permission not granted; then `Write` → "No such tool available"; then explained what it had. Unplanned; kept. |
| B | `--allowedTools Read,Write,…` | One `Write`, "Created `hello.txt` with the single line `hello`.", two turns. The init event is the harness manifest (B01). |
| C | `for i in 1 2 3; do claude -p "$(cat LOOP.md)" …` | three fresh sessions; each Read → Write one file → Edit one box; `tasks.md` the only memory; 3 for 3; six session files on disk. |

Transcript: `SESSION.md`; raw stream-json for all six runs and the loop's files in
`evidence/`. The SKEPTIC beat audits run A2's "Creating the file now." — four fails
— and the narration says why the loop's ticks pass the same four moves.

## Components

`CCSkepticAudit`, `CCBoondoggleScore`, `CCHumanLedger` (from the first cc-explainer),
`CCPlainShell` (from the second), and **`CCHarnessMap`** — built for this reel:
concentric rings on the CC page, model at the core, PROMPT → CONTEXT → HARNESS →
YOUR LOOP landing inside out, each ring carrying strings from the runs, a caption
last. Registered under `CC`, indexed, RENDERABLE, `tsc` clean.

## Gates and compile record

| Pass | What happened |
|---|---|
| 1 | Full render 14/14. **Gate V: 2 BLOCKERs** — `CCHarnessMap` edge-bleed: the outer ring sat 60 px from the frame edge, inside the 5% title-safe band. Fixed in the component (margin 100 px, caption raised). Frame reads also found a `CCBoondoggleScore` step text clipping and one ledger row at the budget — shortened at the source. |
| 2 | Re-render of B07/B09/B10 started while a stale `run.sh` from pass 1's chain was still alive on the same reel (my `pkill` matched the wrapper, not `run.sh`/`remotion_scenes.py`); the two fought over `.render.lock`. Killed everything, cleared the lock, one clean run: Gate V 0/0/0, GATE T PASS, BOOKEND PASS, −24.09 LUFS → `final`. **But** the run writes build stamps back into `beat_sheet.json` from its own copy, which reverted a prop edit made while it was running: B07's CONTEXT chips rendered with the long strings and clipped. |
| 3 | B07 chips shortened in the sheet again (no process running this time), B07 alone re-rendered, `run` → all gates PASS → `final`. |

**Lesson for the skill (recorded in SKILL.md):** never edit `beat_sheet.json` while
`art run` is alive — it stamps the sheet back at the end from its own copy; and kill
`run.sh` / `remotion_scenes.py`, not just the `art` wrapper, before restarting a reel.

**Final:** `cc-agentic-harness.mp4` · 3840×2160 · ~302 s (5:02) · Liam on every beat ·
every beat a real render.

## Restructure (Bear, 2026-09-08 evening)

"Remove the skepticism beat … Hume, Plato etc is just confusing. Add a Hesitant
writer at beat two describing what the idea of the film is … a definitions card."
Done on all three films and in the skill: the SKEPTIC beat (B08) removed with
its audio and render; `BIDEA` (BrutalistHesitantWriter, CC palette — the idea of
the film, one word reconsidered) and `BDEFS` (`CCDefinitions`, built for this:
headless · tools list · connector (MCP) · permission mode · stream-json) inserted after the cold open. Existing beats kept their audio and
renders (stamps restored after an accidental sheet regenerate); only the two new
beats were voiced and rendered, then `run` → `final`.

**Not published.** Master stays here; TOPOST only via `post`, only on ask.
