# SOURCES — cc-pattern-analysis-subagent

## Primary — the runs themselves

- `SESSION.md` — the operator's narrative of the two headless runs, with tool sequences and numbers.
- `evidence/run-inline.jsonl` — the inline run's raw `--output-format stream-json --verbose` output. Session `48aef3a3-…`, Claude Code 2.1.150, 2026-09-09.
- `evidence/run-sub.jsonl` — the subagent run's raw stream-json. Session `94b04c7b-…`, same date and CLI.
- `evidence/ask.txt` — the ask, verbatim, executed against both runs.
- `evidence/pattern-analyzer.md` — the deployed subagent file (`.claude/agents/pattern-analyzer.md`) — the deployment that made the second run behave differently.
- `evidence/rubric.md` — the five-criterion binary-search rubric the runs judged against.
- `evidence/feedback_focus.inline.md` and `evidence/feedback_focus.sub.md` — the two produced files, byte-exact copies of what the runs wrote.
- `evidence/subagent-return.txt` — the summary the subagent returned to the main session, verbatim.
- `evidence/liam-verify.txt` — the operator's post-run plain-shell commands and their outputs.
- `scratch/` and `scratch-sub/` — the two starting-state folders (identical except for `.claude/agents/pattern-analyzer.md`); the runs were executed with these as `cwd`.

## Doctrine referenced by the closing block

- `skills/make/cc-explainer/SKILL.md` (this tree) — TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERIFY-IS-A-COMMAND, VERBATIM-PRODUCT-STRINGS, LIAM LAW, BUILD-SHOW LAW.
- `skills/make/cc-explainer/reference/three-beats.md` — CONDUCT and HUMAN doctrine.
- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — programming as conducting; supervisory capacities (PF, TO, PA, IJ, EI); handoff conditions between AI-solved steps.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — Tier 4 metacognitive and supervisory framing behind the HUMAN ledger.

## Sibling reels — the boundary

- `cc-subagent-context/` (same tier) — the *inline vs subagent* frame under the "context isolation" lens, with its failure mode ("Claude re-reads the batch after the summary returns"). This reel takes a different angle: *deployment as configuration* (`.claude/agents/pattern-analyzer.md`, three-tool whitelist, structured return) as the disciplined form of pattern analysis. The two reels' evidence is separate — different scratch, different runs, different failure modes. The falsifiability line in BVDT explicitly names cc-subagent-context's failure as the test that would falsify this reel's premise.
- `cc-writer-reviewer-pattern/` (same tier) — the *second subagent as reviewer* pattern, distinct from *first subagent as batch triager*.
