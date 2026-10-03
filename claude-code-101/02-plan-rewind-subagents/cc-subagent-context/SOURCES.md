# SOURCES — cc-subagent-context

Where each on-frame number, sentence, or doctrine came from.

## The runs (SESSION.md and evidence/)

- `evidence/run-inline.jsonl` — stream-json of the inline headless run
  (`claude -p ... --output-format stream-json --verbose`).
- `evidence/run-subagent.jsonl` — stream-json of the subagent run.
- `evidence/analyze3.py` — per-turn `cache_creation_input_tokens`
  attribution; the tables in B01, B05, B06, BVDT come from its output.
- `evidence/policies/*.md`, `evidence/ask.txt`,
  `evidence/grader.{inline,subagent}.py`, `evidence/test_grader.{inline,subagent}.py`
  — the byte-identical scratch inputs and the post-run outputs of the two
  builds. All four tests pass in both runs
  (`python3 -m unittest test_grader -v` → `OK`, 4 tests).

## Doctrine for CONDUCT (B07)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md`
  — the labor split, the five capacities (`PF`, `TO`, `PA`, `IJ`, `EI`),
  the dangerous-middle idea. Step 4 (Claude reads policies anyway) is the
  dangerous middle of this session — a plausibility-audit habit turned
  against the run.

## Doctrine for HUMAN (B08)

- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md`
  — Tier 4: the machine cannot reliably supervise its own boundary; the
  human sets the tool boundary. Applied here as: the subagent is the
  mechanism; the human enforces it.

## Kit / brand

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — spine, laws,
  component contracts, and the ruled interim on `ClaudeVerdictArtifact`
  when a purpose-built `CCBoondoggleScore` / `CCHumanLedger` is missing.
- `brutalist-art/runtime/remotion/src/tokens/claude.ts` — palette.
- `brutalist-art/runtime/voices/teardown/VOICE.md` — register.

## What is deliberately NOT sourced

- No published benchmarks. Every token count on frame is from this reel's
  own stream-json.
- No product names beyond "Claude Code" / "the Agent tool" — no model
  version, no price, no session id in narration or on-frame.
