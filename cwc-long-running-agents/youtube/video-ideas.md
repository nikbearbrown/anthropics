# Harness Primitives for Long-Running Claude Agents Video Ideas

## Candidate 1 — Why agents mark features done without proof, and how to make it structural

- Source: `claude-code-config/.claude/hooks/track-read.sh` + `claude-code-config/.claude/hooks/verify-gate.sh`
- Topic: Default-FAIL contract with evidence gating
- Hook: Agents claim tests pass after a unit test succeeds even when the UI is visibly broken.
- Key case: Agent runs `npm test` (green), tries to write `"passes": true` to `test-results.json`. A `PreToolUse` hook intercepts and denies the write.
- The Question: Asking nicely in the prompt should stop agents from claiming success without observation, but it doesn't—so what mechanism prevents false positives?
- Core idea: A hook checks whether the agent has already opened a screenshot or console log (using Read) before allowing a write to the results file. The gate doesn't verify the content—only that evidence was opened first in that session.
- Visual object: `test-results.json` being written and the hook blocking it; the agent's denied write attempt
- Manim move: compare
- Example seed: Feature "dark mode toggle." Agent runs test suite (passes), tries `"passes": true`. Hook: denied. Agent opens a screenshot showing the toggle working. Hook: now allowed to write.
- Length band: ~1 min
- Still lanes: raster
- Prerequisites: git, Bash hooks, JSON results file
- Exclusions: JSON schema design; multi-test granularity; how to extend the hook to track per-test evidence
- Score: 9/10

## Candidate 2 — How agents survive context-window boundaries by writing their own state

- Source: `claude-code-config/.claude/CLAUDE.md` + `claude-code-config/.claude/hooks/commit-on-stop.sh`
- Topic: Agent-maintained handoff through PROGRESS.md and structured commits
- Hook: A context window fills up and summaries lose detail; the next fresh session has no memory of what was built before.
- Key case: Session 1 works 20 turns on form validation. At the end, the agent writes to `PROGRESS.md` (marking items Done, current work In Progress) and commits to git. Session 2 wakes up cold, reads the file, resumes exactly where Session 1 stopped.
- The Question: How can an agent maintain continuity through context restarts without relying on Claude's summarization?
- Core idea: The agent treats `PROGRESS.md` as a living handoff with four sections (Done, In Progress, Next, Notes), reads it first thing each session, and commits meaningful checkpoints to git so `git log` becomes a second timeline. The structure is simple enough that future sessions parse it reliably.
- Visual object: `PROGRESS.md` accumulating Done checkboxes; `git log` extending with structured commit messages
- Manim move: accumulate
- Example seed: Session 1: "## In progress: Multi-select checkbox logic"; commits "Add multi-select event handlers." Session 2 reads PROGRESS.md, sees checkbox work incomplete, picks it up and commits "Complete multi-select with tests."
- Length band: 2–3 min
- Still lanes: raster
- Prerequisites: git, understanding of context-window summarization, understanding of session boundaries
- Exclusions: Git workflow details (cherry-pick, rebase); PROGRESS.md schema beyond the four sections; how to scope exactly one feature per session
- Score: 8/10

## Candidate 3 — Why single-pass delivery fails where iterated feedback succeeds

- Source: `README.md#running-the-loop` (the loop pattern) + `claude-code-config/.claude/agents/evaluator.md`
- Topic: Build → Evaluate → Rebuild feedback cycle with convergence
- Hook: A single build-and-pass cycle often stops too early, but if the evaluator's findings feed back as the next prompt, the agent iterates toward correctness.
- Key case: Feature "login flow." Build 1: agent implements form. Evaluator finds password not masked. Build 2: agent adds masking. Evaluator finds no "forgot password" link. Build 3: agent adds link. Evaluator: PASS. Loop exits with 3 iterations.
- The Question: A builder shouldn't grade its own work (confirmation bias) so why does a fresh evaluator reviewing the same code find what the builder missed?
- Core idea: Each cycle is isolated: builder works, evaluator (in a separate fresh context with no Write/Edit) checks the diff and evidence, returns `PASS` or a bulleted list of specific findings. Findings become the builder's next session prompt. The contract file starts all tests `false`; loop exits when all are `true`.
- Visual object: The cycle loop (builder → evaluator → decision diamond → findings feed back → builder again); state accumulating (test counts, findings list)
- Manim move: morph
- Example seed: Start: 5 tests, all false. Iter 1: builder works, evaluator says "2 issues"; 0 tests pass. Iter 2: builder reads findings, fixes them, evaluator says "1 issue"; 2 tests pass. Iter 3: final fix applied; evaluator says PASS; all 5 tests pass; loop exits.
- Length band: 3–5 min
- Still lanes: geo
- Prerequisites: understanding of /goal command or wrapper loops, understanding of fresh-context evaluation, understanding of default-fail contract
- Exclusions: /goal vs. wrapper-script trade-offs; specific completion conditions; budget limits and exit strategies
- Score: 8/10

## Candidate 4 — How a separate agent's clean context catches what the builder is blind to

- Source: `claude-code-config/.claude/agents/evaluator.md`
- Topic: Fresh-context evaluator as a second pair of eyes
- Hook: The builder agent has been inside the context the whole session, mentally committed to the build being done and visually desensitized to problems.
- Key case: Builder claims "landing page is complete" and marks tests passing. Evaluator wakes in a separate process, reads `git diff`, opens the screenshot. The footer is misaligned. Evaluator returns `NEEDS_WORK: footer column alignment broken.`
- The Question: The diff looks correct and the builder is confident, so why does the evaluator (seeing the exact same code and screenshot) spot a gap the builder is blind to?
- Core idea: The evaluator agent runs in a separate `claude` process with context that never saw the build history—no accumulated commit messages, no prior Read tools showing "I built this." It reads the diff cold, opens evidence, and grades from a skeptical frame. No Write/Edit tools; it returns only a verdict (`PASS` or `NEEDS_WORK`) plus findings.
- Visual object: Two context windows side-by-side—one thick with build history (builder), one blank (evaluator)
- Manim move: split
- Example seed: Builder works 4 turns on "notification dismiss button," marks it done. Evaluator reads diff, opens screenshot. Button text is black on dark blue background—unreadable. Evaluator returns `NEEDS_WORK: dismiss button text fails contrast ratio.` Builder's next session reads this and fixes the color.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: understanding of context pollution and mental commitment bias, understanding of multi-agent workflows, understanding that fresh eyes catch blind spots
- Exclusions: Tool restrictions for evaluator (no Write/Edit); specific prompt tuning for skepticism; handling ambiguous evidence
- Score: 7/10

## Candidate 05 — Why stopping a headless agent mid-execution is dangerous and how a file prevents it

- Source: `claude-code-config/.claude/hooks/kill-switch.sh` (described in `claude-code-config/README.md`)
- Topic: Sentinel-file halt at tool-call boundaries
- Hook: Killing an autonomous process mid-execution can leave files half-written, but the agent has no interactive input to receive a graceful-stop signal.
- Key case: Iteration 4 of a build loop; the agent is about to overwrite a hand-edited config file. The operator runs `touch AGENT_STOP`. On the very next tool call, `kill-switch.sh` fires, returns non-zero, and blocks it. The config file is never touched.
- The Question: The operator must stop the agent right now, but killing the process could corrupt state mid-write—so where is the one moment it is always safe to pause?
- Core idea: A `PreToolUse` hook checks for the sentinel file before every tool call. A non-zero exit blocks the call without terminating the process. The tool boundary—where no write has started yet—is the only guaranteed safe pause point in an agent loop. Remove the file to resume; no restart, no lost context.
- Visual object: A horizontal timeline of tool-call boxes with a vertical red bar appearing mid-sequence and all boxes to the right grayed out
- Manim move: trace
- Example seed: Loop writing 5 config files. After file 2 is committed, operator touches `AGENT_STOP`. Files 3–5 are never touched. Operator inspects, finds file 2 correct, removes the sentinel. Loop resumes from file 3.
- Length band: ~1 min
- Still lanes: raster
- Prerequisites: PreToolUse hooks, headless agent operation, tool-call atomicity
- Exclusions: SIGTERM / graceful shutdown protocols; checkpoint-restart systems; how to resume a killed (not paused) process
- Score: 8/10

---

## Candidate 06 — How to deliver one directive to a running agent and guarantee it is read exactly once

- Source: `claude-code-config/.claude/hooks/steer.sh` + `claude-code-config/.claude/CLAUDE.md` (described in `claude-code-config/README.md`)
- Topic: One-shot operator message injection via file-rename protocol
- Hook: You need to redirect a headless agent mid-session, but you cannot type into it, and waiting for the next fresh session discards the current context.
- Key case: Session is building a sidebar. Designer Slack-messages: "Kill the sidebar, just ship the main form." Operator writes this to `STEER.md`. On the next tool call, `steer.sh` finds the file, emits its content as `OPERATOR STEERING:` into the agent's context, and renames the file to `STEER.md.used`. The agent pivots this session; the hook never fires again because `STEER.md` is gone.
- The Question: The agent loop has no stdin; injecting content into the next session prompt loses current progress—so how does a human directive enter the live context window, guaranteed exactly once?
- Core idea: The hook emits-and-renames (not deletes) on first find. Rename is the delivery receipt: subsequent tool calls see no `STEER.md`, so the message is never re-emitted. The `.used` file remains as a log. CLAUDE.md instructs the agent to treat `OPERATOR STEERING:` lines as higher priority than its current plan, so receipt reliably causes a pivot.
- Visual object: Three-state file icon: `STEER.md` (pending) → hook reads it → `STEER.md.used` (consumed), with the message flowing into the agent context bubble between states
- Manim move: transform
- Example seed: 3-iteration loop. Mid-iteration 2, operator writes "skip sidebar, ship the form first." Hook fires on next call, agent notes the pivot in `PROGRESS.md`, continues as the form builder. Iteration 3 sees only `.used`; no re-injection. `.used` is readable audit trail.
- Length band: ~1 min
- Still lanes: raster
- Prerequisites: PreToolUse hooks, headless agent operation, agent context as an append-only message stream
- Exclusions: Queuing multiple steers; STEER.md content schema; steer vs kill-switch priority ordering; interactive Claude Code mode where you can simply type

- Score: 7/10
