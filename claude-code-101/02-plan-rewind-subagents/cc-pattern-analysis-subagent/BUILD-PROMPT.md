# BUILD-PROMPT — cc-pattern-analysis-subagent

The prompt an operator would paste into a fresh Claude Code session to rebuild
this reel from scratch, given the same evidence.

```
Build a cc-explainer reel that shows how to deploy a pattern-analysis subagent
for a grading tool with Claude Code. The reel is a build film: same ask,
executed twice — once inline (no subagent) and once with .claude/agents/pattern-analyzer.md
deployed. The subject is what changes in the main session's tool sequence when the
deployment is in place.

Inputs, in ./evidence/ (already prepared by the human):
  ask.txt                          the one-sentence ask
  rubric.md                        five criteria for a binary-search writeup
  submissions/01..05.md            student submissions (deliberately weak in
                                   overlapping ways)
  pattern-analyzer.md              the subagent's .claude/agents/ file
  run-inline.jsonl                 raw stream-json of the inline run
  run-sub.jsonl                    raw stream-json of the subagent run
  feedback_focus.{inline,sub}.md   the two produced files
  subagent-return.txt              the subagent's return, verbatim
  liam-verify.txt                  the operator's plain-shell VERIFY

Method:
  1. Read the cc-explainer SKILL.md whole. Do not paraphrase product strings.
  2. Author beat_sheet.json via a Python author script that traces every
     CCSession block back to run-*.jsonl or the produced files. Persona Liam,
     Kokoro am_onyx, in for Bear on B00 and BOUT.
  3. Spine: B00 cold open (inline session) → BIDEA (BrutalistHesitantWriter,
     'prompt' → 'subagent') → BDEFS (CCDefinitions, 4 terms) → cycle 1 VERIFY
     (B01) → the deployment (B02, CCPlainShell — outside any session) →
     cycle 2 SUBAGENT RUN (B03) → cycle 2 VERIFY (B04) → BFLOW (FlowDiagram
     claude skin: MAIN → TASK → SUBAGENT with BATCH → SUMMARY → MAIN → WRITE)
     → BSHOW (CCPlainShell cat of feedback_focus.sub.md) → CONDUCT (B05,
     CCBoondoggleScore, dangerousMiddle = the deployment) → HUMAN (B06,
     CCHumanLedger) → BVDT → BHTF → BOUT.
  4. Every CCSession text block ≤ 44 chars. Every CCHumanLedger row ≤ 30 chars.
     Every CCBoondoggleScore step ≤ 46 chars. CCPlainShell ≤ 14 lines.
     ClaudeVerdictArtifact = 4 lines (never 5). mascot: 'off' on full stacks.
     tokens strings without leading ↓.
  5. Kokoro all beats (generate_audio_kokoro.py). After the mp3s are stamped,
     never rerun the author script inside this folder — regenerate to a temp
     directory and merge props if props must change.
  6. FACTCHECK every claim against evidence/. Then art run → art final.
     BUILD-SHOW LAW satisfied by BFLOW + BSHOW.
```

## Delegation contract

- **Never publish.** The master stays at
  `anthropics/claude-code-101/02-plan-rewind-subagents/cc-pattern-analysis-subagent/cc-pattern-analysis-subagent.mp4`.
  TOPOST is not the destination of this build.
- **Never edit** the cc-explainer skill, its components, or another reel.
- **Never spend beyond the two `claude -p` runs** already executed against the
  operator's own API balance. Kokoro is free; nothing else is paid.
- **One reel per invocation.** Write `CC-BUILT.txt` in the concept folder and
  stop.
