# SOURCES — cc-claude-skills--claude-liam-example-skill

## The subject (in-repo, verbatim)
- `anthropics/claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md` — 84-line reference template.
  Frontmatter fields it defines (from §Frontmatter Options):
  - `name` (required)
  - `description` (required — trigger conditions)
  - `version` (optional — semver)
  - `license` (optional)
  - Optional directory structure named in §Skill Structure: `references/`, `examples/`, `scripts/`.
  - Three-mode distinction in §Overview: skills (model-invoked) vs commands (user-invoked) vs agents (Claude-spawned).

## The reconstruction (this session)
- Three real headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, isolated in `/tmp` scratch trees:
  - `evidence/run-bare.jsonl` — no skill in folder
  - `evidence/run-full.jsonl` — 40-line SKILL.md + check_peek.py
  - `evidence/run-bare-front.jsonl` — 4-line SKILL.md + check_peek.py
- The two SKILL.md variants and the checker: `evidence/csv-peek.full.SKILL.md`, `evidence/csv-peek.bare-front.SKILL.md`, `evidence/csv-peek.check_peek.py`.
- The three `peek.md` outputs: `evidence/peek.bare.md`, `evidence/peek.full.md`, `evidence/peek.bare-front.md`.

## The closing block
- CONDUCT (Boondoggle Score, capacities `PF | TO | PA | IJ | EI`): `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md`.
- HUMAN (MUST/SHOULD × CAN/SHOULD, Tier 4 frame): `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md`.

## Sibling reels (for pattern)
- `cc-three-files` — the exemplar this reel's `author_sheet.py` copies wholesale.
- `cc-claude-skills` — the sibling reel that proved semantic routing; this reel takes the routing as verified and extends the argument to the body.
