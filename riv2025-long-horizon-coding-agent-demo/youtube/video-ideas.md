# Long-Horizon Coding Agent Demo Video Ideas

## Candidate 1 — Why prompt language shapes full-stack completion, not frontend-only defaults
- Source: `CLAUDE.md` (issue #17, commit 8dfdae7)
- Topic: Prompt-driven phase sequencing in long-horizon agent tasks
- Hook: The agent wrote 220 tests but zero backend code — how does a single prompt change flip an agent from frontend-only to properly full-stack?
- Key case: Issue #17 produced zero infrastructure/shared/backend tests despite being in the BUILD_PLAN. Swapping "grade yourself on coverage" for "complete Phase 1 before beginning Phase 2" immediately fixed it.
- The Question: If two prompts describe the same work, why would one produce complete phases and the other skip 80% of the specification?
- Core idea: Explicit phase-state checkpoints and completion gates in prompts act as dependencies; replacing grading language with "mark done, then proceed" transforms completion from optional to mandatory.
- Visual object: BUILD_PLAN phases (Phase 1 Backend → Phase 2 Infrastructure → Phase 3 Frontend) with guard rails between them showing which must complete before next can start.
- Manim move: split (phases separating), then collapse (showing linear dependency chain)
- Example seed: Prompt A: "Grade yourself on frontend, infrastructure, and backend test coverage." Result: 40 frontend tests, 0 backend. Prompt B: "Phase 1: write backend tests, mark PHASE_1_COMPLETE. Do not begin Phase 2 until marked complete." Result: 15 backend tests, then 25 frontend tests. Same app, same tests, different prompt structure, different output ordering.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Agent task decomposition, prompt engineering concepts
- Exclusions: Don't detail BUILD_PLAN.md file structure; focus on how prompt language creates ordering constraints.
- Score: 9/10

## Candidate 2 — Why a test verification gate designed for screenshots blocks backend tests entirely
- Source: `CLAUDE.md` (issue #22, commits for backend-verify.cjs)
- Topic: Feedback loop correction through alternative verification paths
- Hook: Zero backend tests passed, but not because the agent couldn't write them — they couldn't be marked passing without screenshots.
- Key case: Issue #22 showed hardcoded Playwright screenshot requirement for test verification. Backend code produces no browser output. Agent rationally stops writing backend tests. Adding backend-verify.cjs (producing -result.txt artifacts) immediately unlocked 18 backend + 36 frontend tests across all layers.
- The Question: How does a test pass in reality but remain permanently failing until the verification format changes?
- Core idea: Verification gates pattern-match artifacts (screenshots, console dumps). Test categories with different artifacts (shell-command results vs. browser screenshots) silently fail until an alternative artifact pattern is accepted.
- Visual object: Two verification paths forking — Playwright branch (screenshots) and backend-verify branch (text results) — both converging to the same "test passes" decision.
- Manim move: split (two verification pathways), merge (converge on test-passes decision)
- Example seed: A rule says "tests pass if they produce a screenshot.txt file." A DynamoDB integration test runs locally, succeeds (table responds correctly), but produces no screenshot because it's not a browser. Agent sees "no screenshot" and marks it failing. Agent learns: don't write tests without screenshots. Months pass, zero backend tests. Fix: accept a second rule "tests also pass if result.txt contains VERIFIED_BY: backend-verify.cjs." Agent immediately writes 18 backend tests.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Test verification concepts, agent feedback loops
- Exclusions: Don't implement backend-verify.cjs internals; focus on the gate-pattern mechanism.
- Score: 9/10

## Candidate 3 — How missing one permission cascades into total invisibility
- Source: `LEARNINGS.md` (items #10, #11; the CloudWatch + Bedrock chain)
- Topic: Permission dependencies and observability collapse
- Hook: An agent session ran silently for hours, producing no code, no logs, no GitHub comments — completely invisible. The root cause was two missing permissions working in tandem.
- Key case: CloudWatch Logs permissions missing → OTEL exporter fails silently → no error telemetry appears anywhere. Simultaneously, Bedrock invoke permission for `us.anthropic.*` profiles missing → API calls fail silently. Double silence: no output, no way to see why.
- The Question: How does a system remain broken but produce absolutely no error signal anywhere?
- Core idea: Observability is a permission like any other. If both the service call (Bedrock InvokeModel) and the observability system (CloudWatch Logs) fail permissions silently, the failure becomes invisible — nothing runs, nothing logs, nothing appears.
- Visual object: Two layers of permission checks (API layer and Logs layer), both failing; the stacked failures erasing all visibility.
- Manim move: rotate (showing permission checks), then decay (showing visibility vanishing as layers fail)
- Example seed: A Lambda function has permission to invoke an API but not to write to CloudWatch Logs. The API call fails with "Access Denied." That error message is a string ready to log. But the Logs permission is also missing. So: API fails (silently, no output), error message tries to log (fails silently, no output), developer sees nothing. System appears to do nothing. Actually it's broken twice — once functionally, once observably.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: AWS IAM, CloudWatch Logs, observability concepts
- Exclusions: Don't detail OTEL exporter code; focus on the boundary between service and observability as a permission checkpoint.
- Score: 8/10

## Candidate 4 — Why decoupled polling with reaction voting distributes priority without a gatekeeper
- Source: `README.md` ("How It Works," steps 1–4; issue-poller.yml pattern)
- Topic: Asynchronous task prioritization via emergent voting
- Hook: How do you let a distributed team decide what an autonomous agent builds next without synchronous meetings, explicit labels, or a single maintainer bottleneck?
- Key case: GitHub issue created → any team member adds 🚀 reactions (voting) → every 5 minutes, poller counts reactions, sorts by vote total, finds one with authorized-user approval → agent invoked on highest-voted approved issue.
- The Question: Why does reaction-count sorting work better than a priority-label field?
- Core idea: Reactions are decentralized signals; each addition is an independent vote. A polling loop batches reactions over a 5-minute window, sorts by count (not by maintainer judgment), and uses vote total as the prioritization function. This distributes priority setting without a single gatekeeper.
- Visual object: A GitHub issue with reactions accumulating (🚀 🚀 🚀 counter rising), then a poller reading and sorting.
- Manim move: accumulate (reactions stacking), scan (poller reading the count)
- Example seed: Two priority systems: (A) Add a label "priority-high" (maintainer decides, one person, single point of veto). (B) Allow anyone to add 🚀; maintainer adds a separate 🚀 to approve. Poller counts. Top-voted approved issue goes to agent. Result: distributed voting, clear signal (emoji count), no single bottleneck, team feels heard.
- Length band: ~1 min
- Still lanes: geo
- Prerequisites: GitHub reactions, polling loop concepts
- Exclusions: Don't detail GitHub Actions workflow YAML; focus on the decoupling benefit of reaction voting.
- Score: 7/10

## Candidate 5 — Why infrastructure-as-code sometimes requires manual steps to bootstrap itself
- Source: `LEARNINGS.md` (item #5: IAM role / CDK chicken-and-egg)
- Topic: Circular dependency resolution in infrastructure provisioning
- Hook: CDK is supposed to be fully automated. But attaching policies to an external IAM role on the first deployment fails because the role doesn't exist yet.
- Key case: CDK stack attempts to attach policies to AgentCore execution role. Role is managed externally (by Bedrock), not created by CDK. First deploy fails and rolls back, orphaning ECR repo. Solution: Deploy without role ARN (skip policy attachment), manually create role, redeploy to attach policies.
- The Question: Why can automated provisioning require manual steps at system boundaries?
- Core idea: A conditional gate `if (agentCoreRoleName)` in CDK wraps the policy-attachment block. Phase 1 (role ARN empty): skip attachment, provision everything else. Manual step: create role. Phase 2 (role ARN provided): attach policies. This two-phase approach breaks the circular dependency.
- Visual object: Two CDK deployment runs with a conditional block gating policy attachment; the manual step in the middle.
- Manim move: split (showing conditional), duplicate (showing two deploy runs with manual step between)
- Example seed: Infrastructure-as-code tries to apply a policy to a third-party operator's IAM role. On first deploy, the operator doesn't exist, role doesn't exist, policy attachment fails. Solution: gate the attach behind `if (externalRoleProvided)`. Phase 1: create cluster, skip attach. Manual phase: operator initializes and reports its role ARN. Phase 2: re-deploy, attach policies. Automation + external dependency = two-phase bootstrap.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: IAM, CDK conditionals
- Exclusions: Don't detail CloudFormation rollback mechanics; focus on the gating pattern as a way to break circular dependencies.
- Score: 7/10

## Candidate 06 — Why writing correct code against undeployed infrastructure produces a frontend that silently falls back to localStorage
- Source: `CLAUDE.md` (Prompt Update: CDK-First Deployment Flow, commit `3744400`)
- Topic: Commit-poll-proceed synchronization between an agent and an external CI/CD pipeline
- Hook: The agent wrote Lambda handlers that called DynamoDB correctly — and the frontend never used any of them, defaulting silently to localStorage instead.
- Key case: Issues #17 and #22 showed the agent writing CDK + full handler implementations simultaneously, never polling SSM deploy-state, leaving `VITE_API_URL` blank. Fix (commit `3744400`): Phase 2a writes CDK + stub handlers only, commits and pushes to trigger CI/CD; Phase 2b enters a polling loop on SSM parameter `/claude-code/deploy-state` until value contains `"status":"succeeded"`; only then does the agent write full handlers. Phase 3 reads `apiUrl` from that same SSM value and writes `frontend/.env` → `VITE_API_URL=https://...`.
- The Question: If the handler code is correct and DynamoDB is correctly modeled, why does the frontend never reach the backend?
- Core idea: A CI/CD pipeline is a temporal dependency: code that references a resource (DynamoDB table, API Gateway endpoint) written before that resource is deployed compiles and tests fine but cannot connect at runtime. An SSM parameter acting as a deployment receipt converts an asynchronous pipeline into a synchronization point — the agent polls until the receipt flips, then and only then writes code that depends on deployed infrastructure.
- Visual object: SSM parameter state machine transitioning `deploying → succeeded` with the agent's polling loop visibly paused on it; the `apiUrl` value unlocking Phase 2b.
- Manim move: trace (polling loop), transform (SSM state flip), spread (Phase 2b handlers fanning out after unlock)
- Example seed: Agent writes `handler.js` → `dynamodb.scan('canopy-users')`. Table does not exist yet. Handler compiles, unit tests pass (mocked). Frontend looks for `VITE_API_URL`, finds nothing, defaults to `localStorage`. Fix: write stub handler with hardcoded `return []`, push, then poll: `aws ssm get-parameter --name /deploy-state` every 30 s until `status=succeeded` and `apiUrl` present. Write real handler. Write `frontend/.env` with `VITE_API_URL`. Frontend now routes to real API. Same code, different write order, different runtime behavior.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: CI/CD pipelines, SSM parameters, async dependency concepts
- Exclusions: Don't revisit prompt phase-ordering language from Candidate 1 — the distinction is waiting on an *external system's state change* vs. ordering the agent's own work; don't detail CDK stack internals or the deploy-infrastructure workflow YAML.
- Score: 8/10

## Candidate 07 — Why a wildcard that covers every Anthropic model still blocks every cross-region call
- Source: `LEARNINGS.md` (item #10: Bedrock cross-region inference profile)
- Topic: IAM resource-pattern prefix matching with dot-namespaced ARN variants
- Hook: The IAM policy explicitly grants access to Anthropic foundation models with a wildcard — and silently denies every single call to the default model.
- Key case: CDK-generated `AgentCoreBedrockInvokePolicy` allows `arn:aws:bedrock:<REGION>::foundation-model/anthropic.*`. Default model `us.anthropic.claude-opus-4-6-v1` has ARN suffix `us.anthropic.claude-opus-4-6-v1`. Wildcard `anthropic.*` requires the literal string to begin with `anthropic.` — `us.anthropic.` begins with `us.`, not `anthropic.`. All `InvokeModel` calls return Access Denied. Combined with missing CloudWatch Logs permissions (Candidate 3), first full session produced zero code output.
- The Question: If `*` matches anything, why doesn't `anthropic.*` match a string that contains `anthropic`?
- Core idea: IAM wildcards expand the *suffix* after their literal prefix — they do not perform substring search. `anthropic.*` matches any string whose first nine characters are exactly `anthropic.`; `us.anthropic.claude-opus-4-6-v1` starts with `us.`, so the prefix comparison fails at character one. AWS cross-region inference profiles prepend a regional namespace (`us.`, `eu.`, `ap.`) to the model family name, creating a new prefix that no existing `anthropic.*` pattern covers.
- Visual object: Two ARN suffix strings aligned character-by-character — `anthropic.claude-3-5-sonnet` (matches, green) and `us.anthropic.claude-opus-4-6-v1` (fails at `u`, red) — with the wildcard pattern highlighted above both.
- Manim move: scan (character-by-character prefix comparison), split (match vs. no-match branches diverging)
- Example seed: Policy resource pattern: `foundation-model/anthropic.*`. Model A — `anthropic.claude-3-5-sonnet-20241022`: prefix check `anthropic.` = `anthropic.` ✓ → allowed. Model B — `us.anthropic.claude-opus-4-6-v1`: prefix check `anthropic.` ≠ `us.anth` ✗ → denied. Fix: add `foundation-model/us.anthropic.*` alongside `foundation-model/anthropic.*`, or use `foundation-model/*anthropic*` to match both. Three characters (`us.`) block an entire model family.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: IAM policy resource patterns, AWS ARN structure
- Exclusions: Don't revisit the double-silence / observability-as-permission mechanism from Candidate 3 — this card is strictly the prefix-matching rule, not why the error was invisible; don't detail cross-region inference profile routing mechanics.
- Score: 8/10
