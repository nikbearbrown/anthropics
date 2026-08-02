# Argo CD - Declarative Continuous Delivery for Kubernetes Video Ideas

## Candidate 1 — Why GitOps detects and corrects drift automatically
- Source: `docs/operator-manual/architecture.md`
- Topic: Continuous reconciliation and state correction
- Hook: Live cluster state constantly diverges from declared state, yet applications stay synchronized.
- Key case: A developer manually patches a Deployment from 3 replicas to 5; Argo CD detects the change, marks the app OutOfSync, and re-applies the desired state within seconds.
- The Question: Current state diverges from desired; how does a system detect this drift continuously and correct it without operator intervention?
- Core idea: The application controller runs a continuous control loop comparing live cluster state against the desired state from git, detects OutOfSync, and optionally takes corrective action.
- Visual object: Two parallel timelines—git (desired state) and cluster (live state)—with arrows showing continuous comparison and corrective re-syncs.
- Manim move: scan
- Example seed: A Deployment's CPU limits are edited to 500m in the cluster; Argo notices this doesn't match the 250m in git, marks OutOfSync, and reapplies the manifest within 30 seconds.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Kubernetes Deployments, git basics
- Exclusions: OutOfSync detection algorithms, specific sync timing tuning
- Score: 9/10

## Candidate 2 — Why rendering templates and committing to git creates an audit trail
- Source: `docs/proposals/manifest-hydrator/README.md`
- Topic: Manifest hydration and audit trail preservation
- Hook: Template transformations happen invisibly inside Argo—operators can't review what actually got deployed or trace it in git history.
- Key case: A Helm chart + values render into 30 concrete Kubernetes manifests; the hydrator commits these rendered manifests to a separate branch, creating a reviewable, versioned record.
- The Question: How do you create an immutable, auditable record when your deployment system transforms configuration sources?
- Core idea: Rather than keeping transformations internal, render sources to their final manifest form and commit the hydrated output to git—making the deployed state reviewable and fully versioned.
- Visual object: Pipeline flowing from Helm chart → rendering engine → concrete manifests → git commit, with git history timeline.
- Manim move: transform
- Example seed: A team uses Helm to parameterize 10 Service definitions; hydrator renders all 10 Services as YAML and commits to hydrated-manifests branch, creating a traceable deployment history.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: git, templating concepts, Helm familiarity helpful
- Exclusions: Helm value syntax, git workflow tooling, secret management patterns
- Score: 9/10

## Candidate 3 — Why hooks and waves make safe, ordered deployments possible
- Source: `docs/operator-manual/architecture.md`, `gitops-engine/agent/README.md`
- Topic: Ordered, validated synchronization with lifecycle hooks
- Hook: Deploying 50 manifests at once risks breaking dependencies—custom resources need CRDs first, smoke tests must run after.
- Key case: A Postgres operator deployment: PreSync validates RBAC, Sync wave 1 applies CustomResourceDefinitions, wave 2 applies the Operator Deployment, PostSync waits for the operator pod to be Ready.
- The Question: How do you enforce safe ordering and validation around batch manifest deployment when resources have hidden dependencies?
- Core idea: Lifecycle hooks (PreSync, Sync, PostSync) paired with numbered sync waves allow sequenced application and validation checks.
- Visual object: Timeline with three phases—PreSync, Sync (subdivided into waves), PostSync—showing execution order.
- Manim move: trace
- Example seed: Deploying an API with database migration: PreSync runs schema validation; Sync wave 1 applies the migration Job; wave 2 applies the Deployment; PostSync checks readiness.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Kubernetes Deployments, orchestration concepts
- Exclusions: hook implementation details, wave numbering algorithms
- Score: 8/10

## Candidate 4 — Why duck-typing lets you auto-generate applications from any resource
- Source: `applicationset/examples/clusterDecisionResource/README.md`
- Topic: Dynamic application generation via declarative duck-typing
- Hook: Cluster lists live in different CRD shapes across teams—some use Placement, others custom PlacementDecision—but you want ApplicationSet to work with all of them.
- Key case: A ConfigMap declares "read clusters from any resource's status.decisions[*].clusterName"; ApplicationSet finds a PlacementDecision with 5 entries and auto-generates 5 Applications.
- The Question: How do you allow dynamic application generation from arbitrary, pluggable resource types without hardcoding support for each CRD?
- Core idea: Duck-typing via ConfigMap—declare the resource's apiVersion, kind, and the path within status where cluster lists live; ApplicationSet treats any matching shape the same way.
- Visual object: ConfigMap pointing to a custom resource; ApplicationSet reading its status array and spawning Applications for each entry.
- Manim move: duplicate
- Example seed: Team A uses PlacementDecision CRDs; ApplicationSet reads a ConfigMap saying "read from status.decisions[*].clusterName", finds 3 decisions, creates 3 Applications automatically.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: ApplicationSet basics, Kubernetes custom resources
- Exclusions: open-cluster-management semantics, specific CRD policy logic
- Score: 8/10

## Candidate 5 — Why a local repository cache bridges git and instant manifest rendering
- Source: `docs/operator-manual/architecture.md`
- Topic: Cached repository serving and on-demand rendering
- Hook: Every manifest render request hitting git would add latency; pre-caching everything wastes disk and compute.
- Key case: Repository server clones the config repo on startup, pulls updates every 3 minutes; when the API requests rendered Helm manifests, the server renders from its cached copy in <50ms.
- The Question: How do you serve fresh manifests efficiently without hitting git on every API request?
- Core idea: Maintain a local git clone, refresh it on a schedule, serve all manifest renders from the cache—trades periodic background updates for instant API response.
- Visual object: Timeline showing periodic git pulls replenishing the cache, then incoming API requests being served from that cache.
- Manim move: accumulate
- Example seed: API receives 100 helm-render requests per minute; repo server pulls the chart repo once every 5 minutes and serves all 100 requests from its local copy without a single git call.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: git, caching patterns
- Exclusions: git-sync internals, polling interval tuning
- Score: 6/10

## Candidate 06 — Why push and pull credentials live in separate namespaces to limit compromise blast radius
- Source: `docs/proposals/manifest-hydrator/commit-server/README.md`
- Topic: Credential isolation through a minimal push-path service
- Hook: Granting Argo CD push-to-git access creates a single credential that, if stolen, lets an attacker rewrite your entire deployment history from inside the cluster.
- Key case: An attacker compromises Argo CD's main repo server; they can read all Helm charts and values but cannot push a backdoored manifest—push credentials exist only in the `argocd-push` namespace, accessible solely to the isolated commit server, which exposes a narrow gRPC API accepting pre-rendered manifests.
- The Question: How do you give Argo CD write-back capability without making a full compromise of the main system equivalent to owning the git repo?
- Core idea: Split the push path into a separate minimal service (commit server) whose only job is accepting rendered manifests over gRPC and pushing them—credentials for that service live in a distinct namespace so lateral movement from the main Argo CD components cannot reach them.
- Visual object: Two isolated boxes—main Argo CD cluster (pull credentials) and commit server (push credentials)—connected by a single narrow gRPC arrow, with credentials shown as locked stores inside their respective namespaces.
- Manim move: split
- Example seed: Three Argo CD components share pull credentials to clone charts; only the commit server, running in `argocd-push` with its own secret, can call `git push`—so a CrashLoop exploit in the repo server yields zero write access.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Kubernetes namespaces, manifest hydration (Candidate 2)
- Exclusions: TLS vs SSH key management, specific SCM permission models, secret rotation procedures
- Score: 7/10
