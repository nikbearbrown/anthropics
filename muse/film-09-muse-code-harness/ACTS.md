# ACTS.md — Film 9: "Muse Code, the Harness"

## Title
Muse Code, the Harness

## Core promise
By the end, the viewer can install Muse Code, configure it for a project,
and use sessions, reasoning effort, approval modes, and headless mode —
knowing exactly where the guardrails are.

## Acts
- **Hook (BIDEA, BDEFS):** Meta built the models, then built the harness to
  run them in. Muse Code is Meta's own coding harness, speaking Muse
  natively. Four terms: Harness, agents.md, Reasoning effort, Session.
- **Act 1 — Install and first contact (B01–B03):** a single-line install;
  first launch as a terminal prompt; skills loaded from everywhere
  (project, home, community).
- **Act 2 — Context and configuration (B04–B06):** `agents.md` as project
  context written by `muse init`; `settings.json` for global defaults and
  trust files; reasoning effort's four stops (low / medium / high /
  extra high), per-session or default.
- **Act 3 — Sessions and power modes (B07–B10):** sessions that resume;
  status (tokens, context %), compact, clear; YOLO mode (full permissions,
  no sandbox) only on disposable machines; headless mode (`-p`, JSON out,
  prompt files) turning the agent into a Unix tool.
- **Recap (BVDT):** one line per act. **Do today (BHTF):** install it,
  launch it, ask it one question about your own code — and watch what it
  reads first. **Outro (BOUT):** "Muse, in for Bear. Thanks for watching."
  + teaser "Next film: Memory, Skills, and Guardrails".

## Tone
Teardown register: flat, practical, no hype. The harness is presented as
infrastructure, not magic. Caution about YOLO mode is firm and plain.

## What this film is not
- Not a film about prompting the model (Films 2–6) or calling the API from
  code (Film 7) or third-party frameworks (Film 8).
- Not an endorsement of YOLO mode; the film's judgment is that it belongs
  only on machines you can lose.
- Not a skills/memory deep dive — that's Film 10.

## Source facts (from transcript-outline.md §13)
- Muse Code: Meta's own coding harness; works with Muse Spark-class models.
- Install: a single-line install command (exact line not recorded in the
  source; the film says the docs carry it and never invents it).
- Sandbox: bubblewrap.
- Skills load from everywhere (project, home, community).
- `muse init` writes `agents.md` — project context the agent reads.
- `settings.json`: global settings, trust files, reasoning effort default.
- Reasoning effort: low / medium / high / extra high; per-session or default.
- Sessions: resume, status (tokens, context %), compact, clear.
- Model switching via CLI (not dramatized in this film — mentioned only in
  SOURCES as a cut thread).
- YOLO mode: full permissions, no sandbox.
- Headless mode: `-p`, JSON output, prompts from files.

## LEFT OUT (with reasons)
- The Goal feature / backend build (belongs to Film 11's capstone).
- Custom skills, project memory, approval modes, MCP servers, DuckDuckGo VQD
  lesson (all belong to Film 10: Memory, Skills, and Guardrails).
- Exact install command text: not recorded in the source; inventing it would
  risk a wrong command. The film is explicit that the docs carry the line.
- Exact per-token cost of reasoning effort levels: unverifiable from the
  source; the film says "more effort costs more tokens and more time" only.
- Model switching via CLI: recorded but cut for time; one claim can't carry
  a beat.
