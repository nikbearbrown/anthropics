# FACTCHECK — claude-liam-the-missing-feedback-loop

_Pass run 2026-08-30 against the primary source (Anthropic's MHS research-preview
post, fetched live). "CHECKED" = independently read in the primary source this
session. "COMPANY-REPORTED" = appears only in Anthropic's own announcement; no
peer review or independent replication exists as of 2026-08-30 — the film says
this out loud (B25, BVDT)._

| # | Claim (as used in the film) | Beat | Verdict | Evidence / note |
|---|---|---|---|---|
| 1 | MHS previewed as a standard for AI agents to discover/operate physical equipment; "MCP for hardware" is the popular gloss, MHS is a separate standard accessible VIA MCP | B05 | PASS | Primary: model-agnostic, accessed via standard protocols "such as MCP"; driver + read/write primitives |
| 2 | Driver layer + manifest (measurable / adjustable / safety limits), natural-language authored, machine-readable | B07 | PASS | Primary describes exactly this incl. agent-interviews-the-human authoring |
| 3 | Safety limits enforced at driver level, below the model | B10 | PASS | Primary + researcher quote ("don't need to worry about excess laser power") |
| 4 | Manifest is human-authored → the floor is only as strong as its author | B10 | EXEMPT (framed as inference, not fact) | Follows directly from #2/#3; framed as fine print, not fact |
| 5 | Integration: weeks → 8 hours (CMU dose-response); new camera in minutes (HHMI Janelia) | B09 | PASS (company-reported) | Both figures verbatim in primary |
| 6 | QuEra baseline: linear script, four engineers, several months, 58%, ~150 s/attempt | B14 | PASS (company-reported) | Verbatim in primary (laser-systems eng, software eng, algorithms specialist, tester) |
| 7 | Overnight run: four Claude instances in roles; induced failures = beam blocked, power cut, frequency pushed; unattended | B15 | PASS (company-reported) | Primary lists exactly these three disturbance types. Brief's "seven failure classes" NOT in primary — not used |
| 8 | Claude compiled a deterministic decision-tree script; production runs with no AI in the loop | B16 | PASS | Primary: "deterministic, fully inspectable script capable of running in production without an AI agent controlling it" |
| 9 | Blind trial: 695/700 = 99.3%; simple 0.9–5.4 s, hard 10–14 s; human 5–10 min | B17 | PASS (company-reported) | Verbatim in primary; reconciles the secondary-press latency confusion |
| 10 | PID result: 15.7 mV → 1.55 mV; 363 experiments, 16 unattended hours; 19 h hold, zero unlocks (expert tune ~1.6 unlocks/hour) | B18 | PASS (company-reported) | Verbatim in primary |
| 11 | Genentech bubbles: retry-same-well instinct made foam worse; needed human redirect; "physical, not software" | B23 | PASS | In primary's own limitations section. "One pharma lab" used in narration (name in description, not narration — strip-the-datable) |
| 12 | "Understanding of the rig was programmatic rather than physical" | B24 | PASS (verbatim quote) | Near-verbatim from primary ("its understanding of the rig was programmatic rather than physical"); attributed on screen to Anthropic |
| 13 | No peer review, no independent replication, not open-sourced yet | B25 | PASS | Primary: "more work to do on the standard before we open-source it"; no independent replication found in searches 2026-08-30 |
| 14 | "Claude adjusted the laser and checked through a camera" (brief's framing) | — | CORRECTED (conflation dropped from film) | QuEra loop read instrument telemetry; cameras belong to the Janelia/Tetsuwan cases. Film says "read the instruments" |
| 15 | Development-run figures (96%, ~6 s) vs final blind-trial figures | B17 | PASS (dev vs blind runs kept separate) | Film quotes only the blind-trial numbers to avoid mixing the two runs |
| 16 | EU Machinery Regulation / "AI Kill Switch Act" threads from the brief | — | CORRECTED (cut from film) | Off-thesis; not independently checked; excluded from the film |

## Standing cautions
- Single-source story: everything traces to one vendor post. The film's own
  thesis requires saying so — B25 and the verdict line "every number here is
  company-reported" are load-bearing and must survive edits.
- The 5 failures out of 700 are shown (B17 terracotta cells) but the primary
  does not explain WHY those five failed; the film does not invent a reason.
