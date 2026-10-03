# PROMPTS — cc-pattern-analysis-subagent

Every prompt this reel shows on screen or reads aloud, traced to its origin.

## What Liam typed at Claude Code (the ask, both runs)

`evidence/ask.txt`, verbatim:

```
For the binary-search rubric in rubric.md, look at every file under
submissions/ and tell me the top three misconceptions the batch is showing,
most severe first. Write your findings to feedback_focus.md as a numbered
list, most severe first, each item one sentence.
```

The CCSession block in B00/B03 renders a paraphrased short form for CCSession
block width; the semantic content and the runs are identical.

## What the pattern-analyzer subagent was prompted with (`evidence/pattern-analyzer.md`)

The subagent's system prompt is the body of `.claude/agents/pattern-analyzer.md`
after the YAML frontmatter — 34 lines directing it to Read the rubric, Glob
`submissions/`, Read each submission, mark each rubric criterion per submission,
and return three sections (`COMMON_MISCONCEPTIONS`, `SEVERITY_BY_CRITERION`,
`RECOMMENDED_FOCUS`). Full text in `evidence/pattern-analyzer.md`.

When Claude Code dispatches the subagent, it passes a per-invocation prompt
alongside the system prompt. That prompt, as it appeared in the tool_use for
the Agent call (`evidence/run-sub.jsonl`), is:

```
Scan every file under submissions/ (relative to the current working directory)
against the criteria in rubric.md. Identify the top three misconceptions the
batch is showing, ordered most severe first.

Write your findings to feedback_focus.md as a numbered list (1., 2., 3.), most
severe first, each item exactly one sentence. No preamble, no headers, no
trailing commentary — just the three numbered sentences.

Do not return submission contents to me; just confirm the file was written and
give a very brief (under 40 words) summary of what you found.
```

The subagent read that prompt and, once it hit its whitelist boundary (no
`Write` in `tools:`), wrote nothing — it returned the summary for the main
session to write.

## What Liam wrote at the plain shell (Liam's VERIFY, `evidence/liam-verify.txt`)

```
> wc -l submissions/*.md rubric.md
> wc -l feedback_focus.md
> cat .claude/agents/pattern-analyzer.md | head -6
```

The B01/B04 CCSession beats stylize these commands as `!wc -l feedback_focus.md`,
`!grep -c '^Read' history.txt`, `!grep -oE 'Task|Write' history.txt`, and
`!jq .usage.cache_creation_input_tokens`. The last three are convenience
renderings of information the JSONL already carries — the numbers they return
are the real numbers (35572, 31942, 8 Reads inline, Task/Write only in sub).
BSHOW's `$ cat feedback_focus.md` is a real command against
`evidence/feedback_focus.sub.md`.

## The BHTF prompt Liam reads aloud to the viewer

`ClaudeComposerAsk.command`:

```
Write me a subagent for triage. Ask me what the batch is, what the rubric or
criterion file is, and what three-section structured summary I want back. Then
write .claude/agents/triage.md — YAML frontmatter, a Read-Grep-Glob whitelist,
and the prompt. Don't dispatch it yet.
```

This is a paste-into-Claude-Code prompt — the scaffolded task for the viewer.
It matches the ledger row in B06: writing the whitelist yourself is what
cannot be delegated.
