# Claude Code Video Ideas

## Candidate 1 — Consensus scoring filters false positives in code review automation

- Source: `plugins/code-review/README.md`
- Topic: Consensus-based filtering in code review
- Hook: Four independent agents score the same issue with different confidence levels — and most are wrong.
- Key case: Agent 1 flags "missing null check" (confidence: 75). Agent 2 flags it (confidence: 90). Agents 3 and 4 don't flag it. System calculates average 82.5 → issue posts. One agent thought it was important; two had doubts; consensus narrowly says include it.
- The Question: Why run four separate agents instead of one strong agent? Shouldn't one expert review be enough?
- Core idea: Consensus scoring. Each agent independently scores issues 0–100. Issues requiring inter-agent agreement (≥80 confidence) separate true bugs from false alarms. Low-confidence issues — where agents disagree — are automatically suppressed. This mechanism turns redundancy into a confidence oracle.
- Visual object: A scoring table showing four agents rating the same three issues, with each agent's column, a final average, and a threshold line at 80 separating posted from suppressed issues.
- Manim move: accumulate (agents' scores add and average), compare (four scores side-by-side for each issue), split (issues split into two groups at the threshold)
- Example seed: Four agents review a PR. Issue A gets scores [75, 90, 70, 85] → average 80 → posted. Issue B gets [50, 45, 60, 55] → average 52.5 → filtered. Issue C gets [95, 92, 98, 96] → average 95 → posted.
- Length band: 2–3 min
- Still lanes: c2v (confidence as height), raster (agents as columns, issues as rows)
- Prerequisites: code review basics, confidence metrics
- Exclusions: CLAUDE.md guideline checking, GitHub CI integration, types of false positives
- Score: 10/10

## Candidate 2 — Terraform provisions infrastructure but stops before image building, splitting deploy into three sequential steps

- Source: `examples/gateway/gcp/terraform/README.md`
- Topic: Sequencing infrastructure provisioning around external build steps
- Hook: Terraform's first apply creates the Artifact Registry — then stops, waiting for something it cannot build.
- Key case: Deploy Claude Gateway on GCP. User runs `terraform apply -target=artifact_registry_repository`. Terraform creates the repo and exits. Then user runs `docker build` and `docker push` manually outside Terraform. Then `terraform apply` runs again to create Cloud Run and reference the pushed image digest.
- The Question: Why three separate invocations instead of one? Why can't Terraform handle the entire deployment end-to-end?
- Core idea: Terraform manages cloud infrastructure as code but deliberately has no Docker execution engine. The workflow must sequence: (1) provision infrastructure (Terraform), (2) build and push image externally (Docker), (3) deploy services that reference the artifact (Terraform again). Infrastructure-as-code is not a complete build pipeline.
- Visual object: A timeline showing three sequential boxes — [Terraform: provision Artifact Registry], [Docker: build and push], [Terraform: deploy Cloud Run] — with arrows showing dependency and a shaded boundary between Terraform-managed (gray) and external tooling (colored).
- Manim move: split (one goal splits into three steps), trace (the image flows from build → registry → Cloud Run reference), transform (infrastructure progresses from empty → provisioned → fully deployed)
- Example seed: Deploy gateway on GCP. Step 1: `terraform apply -target=artifact_registry`. Repo exists, no image. Step 2: `docker build` and `docker push` Claude binary. Step 3: `terraform apply`. Cloud Run service created, points to image by digest.
- Length band: 2–3 min
- Still lanes: geo (GCP services: Artifact Registry, Cloud Run, VPC), c2v (sequential time steps)
- Prerequisites: Terraform basics, Docker image concepts, infrastructure-as-code fundamentals
- Exclusions: GCP networking (Private Services Access, VPC peering), detailed Terraform syntax, deletion guard rails
- Score: 9/10

## Candidate 3 — Configuration precedence stacks so enterprise settings override and lock out local changes

- Source: `examples/settings/README.md`
- Topic: Configuration precedence hierarchies and policy immutability
- Hook: Developer sets a permission locally — but the change has no effect. Something higher up is immutably blocking it.
- Key case: Developer adds `settings.json: {"disableBypassPermissionsMode": false}` to allow manual permission bypasses. Enterprise has pushed `managed-settings.json: {"disableBypassPermissionsMode": true}` via MDM. Developer's setting is silently ignored. Enterprise policy wins and cannot be overridden by any layer below it.
- The Question: I explicitly configured this in my local settings file, so why is my change being ignored entirely?
- Core idea: Configuration forms a locked precedence stack: user settings → project settings → enterprise-managed settings. Higher layers override and supersede lower layers. Once set at a higher level, lower layers cannot override that decision — the precedence order is immutable. This creates a policy hierarchy where enterprise can enforce constraints that users cannot escape.
- Visual object: A vertical stack of three overlapping rectangles labeled user, project, and enterprise (top locked with a padlock icon), showing the same setting property at each level with conflicting values, with a downward arrow indicating which value "wins."
- Manim move: accumulate (settings stack into layers), collapse (lower-layer settings are absorbed into the winning precedence layer), duplicate (show the same setting property at three different levels)
- Example seed: Three configuration levels set `"allowWebFetch": true/false`. Enterprise: true (locked with ⛓️). Project: false (ignored). User: false (ignored). Result: true propagates everywhere. User re-applies their false → no effect because enterprise is higher.
- Length band: ~1 min
- Still lanes: geo (vertical stack and hierarchy), c2v (precedence strength as visual height or opacity)
- Prerequisites: configuration basics, multi-level settings systems
- Exclusions: MDM platform-specific syntax (Jamf, Intune, Group Policy), detailed settings field reference, workarounds
- Score: 8/10

## Candidate 04 — A Stop hook converts Claude's exit signal into another iteration

- Source: `plugins/README.md`
- Topic: Stop-hook interception turns AI exits into forced re-entry
- Hook: Claude finishes and tries to stop — a hook catches that signal and sends it back to work.
- Key case: Developer runs /ralph-loop on a failing test suite. Claude analyzes, writes a fix, runs tests, gets partial results, and emits Stop — it's done what it can. The Stop hook fires, checks whether tests are fully passing, finds they aren't, and re-queues the same task. Claude runs again with no human intervention. Repeat until /cancel-ralph.
- The Question: Claude emitted Stop — why is it running again? Shouldn't "stop" be a terminal signal?
- Core idea: Stop is a hook event, not a final state. The hook intercepts between "Claude decides to stop" and "Claude actually stops," evaluates an external condition, and can re-enter the task loop. Claude's stopping condition is governed by the hook, not by Claude. This converts a linear AI call into an externally-governed iteration loop.
- Visual object: A circular diagram: [Task] → [Claude] → [Stop event] → [Hook: done?] → [No: re-queue → Claude] / [Yes: exit]. The "No" arrow wraps back, forming a visible loop.
- Manim move: trace (follow the loop through each iteration), accumulate (each cycle adds progress), split (exit path vs re-queue path at the hook decision point)
- Example seed: Bug-fix loop. Iteration 1: Claude patches auth.ts, tests run, 2/5 pass — Stop fires, hook re-queues. Iteration 2: Claude patches session.ts, 4/5 pass — Stop fires, hook re-queues. Iteration 3: Claude patches middleware.ts, 5/5 pass — /cancel-ralph ends the loop. (illustrative)
- Length band: 2–3 min
- Still lanes: c2v (Stop event as a node in a flow graph), geo (loop as spatial cycle)
- Prerequisites: Claude Code hooks basics, event-driven programming concepts
- Exclusions: specific completion-criteria definition, how /cancel-ralph mechanically breaks the loop, non-iterative hook use cases
- Score: 8/10

## Candidate 05 — PreToolUse hooks fire in the gap between Claude's decision and tool execution

- Source: `plugins/README.md`
- Topic: Hook interception gates AI tool calls before execution
- Hook: Claude plans a shell command — then something fires before the command runs and may change the outcome.
- Key case: Claude generates `eval(user_input)` as a Python helper and calls the Bash tool to execute it. Before any process spawns, the PreToolUse hook pattern-matches the command string against 9 security signatures. `eval` matches pattern 3. A warning fires in the developer's terminal. No code has run yet.
- The Question: Claude already decided to run the command — why does a pre-execution hook change anything?
- Core idea: PreToolUse hooks occupy the gap between Claude's intent and actual execution. Claude decides what tool to call; that decision is an event the hook system intercepts before the tool runs. The hook doesn't rewrite Claude's plan — it inserts a warning into the developer's view, changing human behavior before execution. The window between "Claude decides" and "tool executes" is the exploitable interval.
- Visual object: A timeline with a visible gap: [Claude decides: call Bash] — gap — [PreToolUse fires: 9 checks] — [Warning? yes/no] → [Tool executes]. The gap zone is highlighted as the hook's exclusive domain.
- Manim move: split (the gap between decision and execution widens to reveal the hook layer), scan (9 patterns sweep the command string sequentially, matched cells light up)
- Example seed: Three tool calls. (1) `cat README.md` — 9 patterns checked, none match, passes. (2) `eval(user_cmd)` — pattern 3 fires, warning displayed, developer stops execution. (3) `pickle.loads(data)` — pattern 5 fires, second warning. Two vulnerabilities caught before any code ran. (illustrative)
- Length band: 2–3 min
- Still lanes: c2v (decision-to-execution timeline with gap), raster (9 patterns as a grid, matched cells highlighted)
- Prerequisites: Claude Code hooks basics, common injection vulnerability types
- Exclusions: the specific 9 patterns listed in full, hook configuration syntax, remediation steps for flagged vulnerabilities
- Score: 7/10

## Candidate 06 — Rebuilding a Docker image under the same tag leaves Cloud Run silently unchanged

- Source: `examples/gateway/gcp/terraform/README.md`
- Topic: Mutable image tags and the moment Cloud Run resolves them to immutable digests
- Hook: Developer rebuilds and pushes a new binary under the same tag — and production keeps running the old code.
- Key case: Gateway v1.2 is deployed via Terraform with `image_tag = "gateway:latest"`. A bug is found. Developer rebuilds the binary, pushes a new image still tagged `gateway:latest`. Runs `terraform apply`. Terraform compares the `image` attribute: string unchanged. No plan diff. No new Cloud Run revision. Old buggy binary continues serving traffic.
- The Question: The image was rebuilt and pushed — why is production still running the old code?
- Core idea: Cloud Run resolves a tag (mutable string) to a digest (immutable SHA256) only at revision creation time. Terraform tracks the image attribute string, not the underlying digest. Same tag string → no Terraform diff → no new revision. The mutable/immutable boundary is invisible to the toolchain: the tag looks the same to Terraform, but the image it points to has changed. Only bumping the tag string forces a re-resolve and a new revision.
- Visual object: Two columns — [Mutable: tag name] and [Immutable: digest]. At t1: tag = "gateway:latest" → digest abc123. At t2: tag = "gateway:latest" (same string) → digest def456 (different image). Terraform sees only the left column; Cloud Run resolves from right.
- Manim move: split (mutable tag column vs immutable digest column rendered side by side), compare (same tag string at t1 and t2, different digests behind it)
- Example seed: Three deploys. Deploy 1: tag "v1" → digest abc → new revision. Deploy 2: rebuild under "v1" → digest def → Terraform diff: none → no revision. Deploy 3: tag "v2" → digest def → Terraform diff: image changed → new revision created. Buggy binary from Deploy 1 runs until Deploy 3. (illustrative)
- Length band: ~1 min
- Still lanes: c2v (tag-to-digest resolution as two-column transform), raster (Terraform plan output showing empty diff)
- Prerequisites: Docker image tagging basics, Terraform plan/apply cycle
- Exclusions: GCP Cloud Run service mechanics in depth, digest pinning as a systematic fix, the two-pass Terraform apply sequence (covered in Candidate 2)
- Score: 7/10
