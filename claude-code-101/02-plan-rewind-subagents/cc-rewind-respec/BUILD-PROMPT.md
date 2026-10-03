# BUILD-PROMPT — cc-rewind-respec

Skill: `cc-explainer` (Claude Code 101, tier `02-plan-rewind-subagents`, concept film 03). Slug `cc-rewind-respec`. Operator: Liam, in for Bear. Voice: Kokoro `am_onyx` (free/local). Palette: `claude`. Aspect: 16:9.

## The idea, in one sentence

When a fix from Claude passes the tests but the diff has drifted, the move isn't to type "fix it again." Rewind to the checkpoint (git reset + a new `claude -p` — the SKILL rule: a new `claude -p` IS `/clear`), then respecify the original ask with the failure mode named as a negative constraint. Same model, different context, first-try right.

## The session the reel reconstructs

Four real headless runs on a scratch `dedupe(items)` module (`scratch/`, pinned at git commit `f5ef78b` "buggy start"):

1. **FF1** — vague ask "the dedupe tests are failing; fix dedupe.py." Claude wrote a linear scan. Tests pass.
2. **FF2** (`--resume`) — "That's O(n²). Speed it up." Claude wrote a two-branch fast path via `try/except`. Tests still pass.
3. **FF3** (`--resume`) — "Simpler. One data structure." Claude wrote `return list({repr(x): x for x in items}.values())`. Tests pass. But `dedupe([1, 1.0])` returns `[1, 1.0]` — the equality drifted from `==` to `repr`, and the tests didn't cover it. Claude even named the caveat in its reply.
4. **Respec** (fresh session, no `--resume` — /clear equivalent; scratch `git reset --hard f5ef78b`) — the same original ask **plus** the failure named as a constraint: "equality is `==`, not `repr` — so `dedupe([1, 1.0])` must return `[1]`". Claude wrote the two-branch equality-correct implementation. One turn, right.

All four are captured in `evidence/run-*.jsonl`; SESSION.md is the trimmed reconstruction.

## Spine

- **B00 COLD OPEN** — CCSession. FF3's `repr` one-liner + unittest OK + Liam's `dedupe([1, 1.0])` returning `[1, 1.0]`. Lands the tension in ~16 s.
- **BIDEA** — BrutalistHesitantWriter (CC palette). Four lines; one word reconsidered: "fix it again" → "respecify it".
- **BDEFS** — CCDefinitions. Five terms: fix-forward · `/rewind` · respecify · context pollution · negative constraint.
- **Cycle 1 · FF1** — B01 (ask + Reads + Write), B02 (Liam runs unittest → OK).
- **Cycle 2 · FF2** — B03 (`--resume` + Write two-branch + unittest OK + Claude's summary).
- **Cycle 3 · FF3 — the drift** — B04 (`--resume` "simpler" + Write repr one-liner + unittest OK), B05 (Liam's `[1, 1.0]` and `[True, 1]` checks — the verify the tests didn't have; the drift is legible).
- **Mechanism** — B06 (CCPlainShell, session-context log growing across three resumes).
- **The rewind** — B07 (CCPlainShell, `git reset --hard f5ef78b` + new session id + "a new `claude -p` is `/clear`").
- **Cycle 4 · Respec** — B08 (fresh session, the respec typed as four prompt fragments + Reads + Write), B09 (unittest OK + `[1]` + `[True]`).
- **CONDUCT** — B10 (CCBoondoggleScore, 7 steps, dangerous middle = step 4).
- **HUMAN** — B11 (CCHumanLedger, 4 MUST/SHOULD human · 4 CAN/SHOULD AI, closing lands last).
- **BVDT** — ClaudeVerdictArtifact, 4 lines, last line begins `FALSIFIABLE:`.
- **BHTF** — ClaudeComposerAsk, greeting "Your turn.", the recipe prompt read in full.
- **BOUT** — ClaudeTitleOutro, `@NikBearBrown`, `subline: ""`, "Liam, in for Bear."

## Compile

Build via the toolkit's entry point:

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books
./brutalist-art/art run   anthropics/claude-code-101/02-plan-rewind-subagents/cc-rewind-respec
./brutalist-art/art final anthropics/claude-code-101/02-plan-rewind-subagents/cc-rewind-respec
```

`author_sheet.py` runs from the reel folder and writes `beat_sheet.json`. Do NOT re-run `author_sheet.py` from inside the reel after audio has been generated — regenerate to a temp dir and merge props, or the mp3 durations are wiped.

## Nothing published

Master stays in the reel folder. TOPOST only via `post`, only on ask. No exception.
