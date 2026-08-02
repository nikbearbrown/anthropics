# Claude Code Action Video Ideas

## Candidate 1 — Why does a single comment show 5-step progress without generating 5 separate messages?
- Source: `README.md` (progress tracking features) + `docs/capabilities-and-limitations.md`
- Topic: Real-time progress rendering in a single immutable comment
- Hook: Claude updates one comment with checkboxes that fill as work progresses—no comment spam.
- Key case: User sees `☐ Read file` → `✓ Read file`, then `☐ Implement changes` → `✓ Implement changes` all within the same comment post.
- The Question: GitHub comments are immutable once posted; how do you display multi-step execution progress without posting after each step?
- Core idea: Single tracking comment with embedded checkbox state variables that the action re-renders on each update, collapsing multiple logical steps into one rendered artifact.
- Visual object: Progress comment showing three checkboxes transitioning from empty → filled over time.
- Manim move: accumulate
- Example seed: Step 1: ☐ Analyze PR → ✓ Analyze PR / Step 2: ☐ Implement fix → ✓ Implement fix / Step 3: ☐ Test changes (in progress).
- Length band: ~1 min
- Still lanes: c2v, raster
- Prerequisites: GitHub comment API, state-serialization in comment text
- Exclusions: doesn't cover how Claude decides what to do; focuses only on progress visibility.
- Score: 9/10

## Candidate 2 — Why do two approval methods (review vs. comment) disagree about whether a commit is still approved?
- Source: `agent-approval-check/README.md` (Approving + threat model sections)
- Topic: Dual approval channels and SHA-based staleness
- Hook: An agent pushes a new commit. A human's `/approve <old-sha>` comment becomes stale, but their GitHub review-based approval somehow stays valid.
- Key case: Human approves commit abc123 via `/approve abc123` comment. Agent pushes commit def456. The SHA-based approval comment is now explicitly stale, but a formal review approval from the same human is still in effect for the PR.
- The Question: Two approval methods, two different invalidation rules—why doesn't stale SHA-based approval logic also apply to review-based approvals?
- Core idea: Comments embed a commit SHA (explicit staleness on push); review approvals target the PR itself (implicit refresh on new commits). The check treats them as separate channels.
- Visual object: Approval timeline showing `/approve` comment with SHA, then new commit arriving, the comment labeled stale, but review checkbox persisting.
- Manim move: morph
- Example seed: Approve comment `/approve abc123def` added at 14:32. New commit pushed at 14:45 with SHA `def456789abc`. The older comment is flagged in the UI as pointing to an outdated commit; the review checkbox does not flag.
- Length band: 2–3 min
- Still lanes: c2v, geo
- Prerequisites: Git commit SHAs, GitHub review API, GitHub comment API
- Exclusions: doesn't cover why approval is needed; focuses only on the mechanism that invalidates one approval type but not the other.
- Score: 8/10

## Candidate 3 — Why doesn't one passing approval status unlock two independent PRs that point to the same commit?
- Source: `agent-approval-check/README.md` (Sibling-PR guard in threat model)
- Topic: Commit-status scope and sibling PR leakage prevention
- Hook: Commit statuses attach to a SHA, not to a PR. Two separate PRs can share the same head commit. One status could theoretically unlock both. It doesn't.
- Key case: PR#100 (to main) and PR#101 (to main) both have head commit abc123. PR#100 reaches approval threshold, status turns green. Does PR#101 also become mergeable? No—the action withholds success while a sibling PR exists.
- The Question: Commit statuses are keyed by SHA, not PR ID; why doesn't a green status for one PR automatically unlock another PR that shares the head commit?
- Core idea: Before posting a `success` status, the action checks for other open PRs to the same protected base with the same head commit. If a sibling exists, the status stays `pending` even if approval criteria are met.
- Visual object: Two PR cards fanned upward from a single commit SHA, with one status indicator beneath—stuck in pending.
- Manim move: compare
- Example seed: PR#42 and PR#43, both head commit e5f8a1b2, both targeting main. Approvals come in on #42; status posts but remains `pending` while #43 is open; only after #43 closes does #42's status flip to `success`.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: GitHub statuses API, branch protection, PR listing/comparison
- Exclusions: doesn't cover approval thresholds themselves; focuses on the gate that prevents multi-PR unlocking.
- Score: 8/10

## Candidate 4 — Why does granting one GitHub permission create three entirely new tools?
- Source: `docs/configuration.md` (Additional Permissions for CI/CD Integration)
- Topic: Permission-scoped tool availability
- Hook: Base action has file + comment + basic GitHub tools. Add `actions: read` permission—suddenly three CI-specific tools materialize.
- Key case: Workflow without `actions: read` → user tags `@claude` → tools available: `Edit`, `Read`, `Comment`, `git` commands. Workflow grants `actions: read` → same `@claude` command → `get_ci_status`, `get_workflow_run_details`, `download_job_log` now exist.
- The Question: Adding a GitHub permission doesn't unlock hidden tool code; it creates new tool capabilities. How does the permission system map to tool availability?
- Core idea: Tools are registered conditionally on token scope. The action's MCP layer checks the GitHub token's permissions and populates tool inventory before Claude sees them.
- Visual object: Two side-by-side tool palettes, before and after permission grant; three new tools glow/fade-in.
- Manim move: spread
- Example seed: Permissions vector (contents:write, pull_requests:write) → tools: [Edit, Read, Comment]. New vector (contents:write, pull_requests:write, actions:read) → tools: [Edit, Read, Comment, get_ci_status, get_workflow_run_details, download_job_log].
- Length band: ~1 min
- Still lanes: raster, c2v
- Prerequisites: MCP protocol, GitHub token scopes, conditional registration
- Exclusions: doesn't cover what the CI tools do; focuses on why the permission creates them.
- Score: 8/10

## Candidate 5 — Why does the same "commit and push" action sometimes create a new branch and sometimes push to an existing one?
- Source: `docs/capabilities-and-limitations.md` (Smart Branch Handling)
- Topic: Context-aware push routing
- Hook: User types `@claude`, the action receives the request, and decides in real time whether to create a new branch or push to the current branch. No config toggle.
- Key case: Tag `@claude` on a **closed PR**—creates new branch. Tag `@claude` on an **open PR**—pushes to the PR's branch. Tag `@claude` on an **issue**—creates new branch.
- The Question: The same action invocation (commit + push) routes to different destinations based on PR state. How does the action auto-detect context and change behavior?
- Core idea: Context detection on trigger: if the trigger is a `pull_request` event and PR is open, push to PR branch; if `pull_request` event and PR is closed, or if `issues` event, create new branch.
- Visual object: Decision tree: [open PR] → push to branch; [closed PR or issue] → new branch.
- Manim move: split
- Example seed: User comments `@claude fix the logging` on issue#50 → action creates `feature/fix-logging` branch. Same comment on PR#50 (open) → action commits to PR#50's branch. Same comment on closed PR#50 → action creates new branch, posts link.
- Length band: ~1 min
- Still lanes: geo, c2v
- Prerequisites: GitHub event context, PR state detection
- Exclusions: doesn't cover why the action should have different behavior; focuses on the routing mechanism.
- Score: 8/10

## Candidate 06 — Why does using the "right" trigger event hand a PR author control over the check that's supposed to gate them?
- Source: `agent-approval-check/README.md` (Tamper-proof triggers section of threat model)
- Topic: GitHub event type → workflow ref selection → tamper resistance
- Hook: The approval check deliberately never triggers on `pull_request_review`, even though reviews are exactly what it counts.
- Key case: A PR author modifies `.github/workflows/agent-approval-check.yml` to set `required_approvals: 0`. If the workflow triggered on `pull_request_review`, GitHub would execute the *attacker's modified file* from the merge ref. Triggering on `pull_request_target` and `issue_comment` instead always runs the base-branch version—the one the attacker cannot touch.
- The Question: `pull_request_review` is the natural trigger for a check that counts reviews; why does using it let the PR author bypass the check they're supposed to be gated by?
- Core idea: GitHub selects which branch provides the workflow file based on event type. `pull_request_review` runs from the merge ref (PR head merged into base), which the PR author controls. `pull_request_target` and `issue_comment` run from the default branch, requiring push access to modify. The action catches review approvals *indirectly*: they are counted the next time a `synchronize` or `issue_comment` event fires the workflow from the safe ref.
- Visual object: Forked path from one PR: left branch labeled `pull_request_review → merge ref (attacker-controlled)`, right branch labeled `issue_comment → base ref (locked)`; workflow file icon switches between the two.
- Manim move: split
- Example seed: PR#88 sets `required_approvals: 0` in the workflow. Scenario A: trigger = `pull_request_review` → runs attacker's modified file → gate passes immediately with 0 approvals. Scenario B: trigger = `/approve` comment → `issue_comment` fires → runs base-branch file with `required_approvals: 2` → correctly blocks.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: GitHub Actions ref selection, `pull_request` vs `pull_request_target` distinction, merge ref concept
- Exclusions: doesn't cover what the approval count does once computed; leaves out CODEOWNERS and branch-protection as complementary defenses; omits `pull_request_review` as a safe read-only data source vs. unsafe trigger.
- Score: 9/10
