# BUILD-PROMPT — cc-cwc-how-we-claude-code

The prompt this reel answers, as a Claude Code operator would receive it — Liam, in for Bear.

> Build a cc-explainer reel for the Anthropic CWC internal workflow ("How We Claude Code"): the three phases in order — Brainstorm → Design → Verify. Do not lecture the workshop. Run the workflow, on a real small task, one phase at a time. Show the bare run first (no phases), then Brainstorm (a brief), then Design (four divergent mockups), then Verify (a fixture the machine can run). End on the two closing beats (CONDUCT, HUMAN) and the your-turn standard. Voice: Teardown. Liam, in for Bear.

## What was built

- **Task**: `Build workshop.html — a one-page landing for our Saturday intro-to-git workshop.`
- **Three runs**: `bare` (task only), `design` (four divergent HTML mockups), `verify` (brief.md + mock2.html + fixture.py → build to pass).
- **Correction cycle**: the verify run's own `python3 fixture.py` FAILed on a monospace check (Claude had used the CSS `font:` shorthand); Claude read the failure and edited, then passed at 153 lines. The revision is real, not staged.

## Where each beat comes from

| Beat | Source |
|---|---|
| B00 | `run-bare.jsonl` — the ask, the two Reads, Claude's summary sentence, the Write |
| BIDEA | authored — the idea of the film (`better` → `different`) |
| BDEFS | authored — jargon the viewer will hear |
| B01 | plain-shell verifies from `SESSION.md` VERIFY, rendered as bang-commands in a CC shell |
| B02 | `evidence/brief.md` — Liam's Phase 1 output |
| B03 | `run-design.jsonl` — the diverge ask, the four Writes, Claude's summary |
| B04 | `wc -l mock*.html` + `grep body{font:` from `evidence/mock*.html` |
| B05 | `evidence/fixture.py` — the `fail(...)` calls verbatim |
| B06 | `run-verify.jsonl` — the entire loop including the correction |
| B07 | plain-shell verifies against `workshop.three.html` |
| B08 | scored from the three runs; capacity labels per `reference/three-beats.md` |
| B09 | authored from what actually happened in the runs |
| BVDT / BHTF / BOUT | the your-turn standard (OUTRO-LOCK) |

## Rules honoured

TERMINAL-FIRST · REAL-SESSION · TYPES-NOT-NARRATES · VERBATIM-STRINGS · VERIFY-IS-A-COMMAND · IDEA + DEFINITIONS before the loop · CONDUCT + HUMAN before the recap · IN-FOR-BEAR (cold open + outro) · Kokoro-only voice · never publish.
