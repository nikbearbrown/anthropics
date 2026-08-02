# Terragrunt Video Ideas

## Candidate 1 — Why same dependencies produce different safe execution orders
- Source: `docs/src/data/commands/find.mdx`
- Topic: Dependency-aware sorting for infrastructure orchestration
- Hook: Two deployment modes, identical infrastructure graph, but the order reverses completely.
- Key case: VPC must deploy before DB; DB before EC2. Running `plan` yields [VPC, DB, EC2]. Running `destroy` yields [EC2, DB, VPC]. Same dependency relationships, opposite traversal.
- The Question: If dependency relationships are static, why does `find --queue-construct-as=plan` and `find --queue-construct-as=destroy` output the same units in reversed order?
- Core idea: Topological sort of the same DAG yields different orders depending on traversal direction—forward (create dependencies first) vs. reverse (destroy dependents first)—each respecting safety.
- Visual object: A directed graph duplicated side-by-side; one instance flows left-to-right, the other flows right-to-left; node positions physically swap to reflect causality.
- Manim move: split (duplicate graph), then rotate and reorder nodes, arrows flip direction.
- Example seed: [dev/vpc] has no deps, [dev/db→vpc], [dev/ec2→vpc,db]. Plan order: vpc,db,ec2. Destroy order: ec2,db,vpc.
- Length band: 2–3 min
- Still lanes: c2v (config parsing), raster (graph visualization before and after)
- Prerequisites: Directed acyclic graphs, topological sort intuition
- Exclusions: Cycle detection, cross-team dependencies, apply/refresh modes
- Score: 9/10

## Candidate 2 — Why flaky tests reveal themselves only in aggregate
- Source: `test/flake/README.md`
- Topic: Detecting intermittent failures through CI run aggregation and ranking
- Hook: A test fails 70% of the time but might pass in a single run; across 20 CI executions, it becomes the obvious culprit.
- Key case: TestIntegrationCatalog fails 6 out of 8 failed runs (75% failure rate), but in isolation you might see noise from other tests and miss the pattern.
- The Question: How can aggregating failures across many CI executions surface which tests are chronically flaky, when individual runs show scattered failures?
- Core idea: Fetch failed CI runs → parse logs for test names → accumulate failure counts across runs → rank by frequency → worst offenders surface automatically.
- Visual object: A ranked table or bar chart of test names sorted by failure count, with failure rates; row height or color intensity reflects how often it failed.
- Manim move: accumulate (columns of failures pile up), then sort (rows slide into descending order).
- Example seed: 8 CI runs, 5 with failures. TestAwsS3Backend appears in 3 runs (62%). TestSSHClone in 3 runs (37%). TestIntegrationCatalog in 5 runs (62%). Sorted: Catalog first, then AWS and SSH.
- Length band: 2–3 min
- Still lanes: raster (log tables and analysis output), c2v (parsed logs becoming ranked lists)
- Prerequisites: CI logs, failure parsing, basic ranking/statistics
- Exclusions: Root cause investigation, retry strategies, environment-specific flakiness patterns
- Score: 8/10

## Candidate 3 — Why discovering modules shouldn't require a central registry
- Source: `docs/src/data/commands/catalog.mdx`
- Topic: Automatic discovery of infrastructure modules from configuration
- Hook: All your Terraform modules exist scattered across includes and subdirectories; one command finds them and presents them interactively without a registry.
- Key case: A new engineer joins the team and needs to deploy a Kubernetes auth module. It exists, referenced in a parent config, but they don't know which file or directory holds it.
- The Question: How can a tool automatically surface all available modules to developers without maintaining a hand-curated registry or separate module documentation?
- Core idea: Parse the root Terragrunt configuration → follow includes recursively → discover all module references → accumulate into a browsable, interactive catalog without human curation.
- Visual object: A TUI (terminal user interface) presenting a menu or tree of discovered modules; developer scrolls, browses, and selects.
- Manim move: scan or spread (configuration files fan outward as they're read) → collapse (many files reduce to a single ranked list of modules).
- Example seed: Root config includes prod.hcl, dev.hcl. prod.hcl references vpc, db, auth. dev.hcl references vpc, db, monitoring. Catalog discovers ~6 unique modules and presents them together.
- Length band: 2–3 min
- Still lanes: c2v (configuration becoming a menu), raster (TUI screenshots)
- Prerequisites: Terragrunt includes, Terraform module references
- Exclusions: TUI keybinding mechanics, module deployment, registry alternatives
- Score: 7/10

## Candidate 04 — Why writing a file "next to your config" drops it in the wrong directory
- Source: `test/fixtures/docs/01-quick-start/step-05.1/README.md`
- Topic: Cache isolation and the get_terragrunt_dir() escape hatch
- Hook: Your Terraform code writes output files "into the module directory," but they silently land in a hidden cache folder instead.
- Key case: A hi.txt file is supposed to appear beside terragrunt.hcl in foo/, but without get_terragrunt_dir() it appears under .terragrunt-cache/foo/hash/.../hi.txt — invisible to the user and wrong for downstream scripts.
- The Question: If path.module points to the module directory, why does the output file appear in .terragrunt-cache rather than the source directory where terragrunt.hcl lives?
- Core idea: Terragrunt copies modules to a temp cache directory before executing; path.module resolves to the copy, not the source. get_terragrunt_dir() bypasses the copy by returning the directory of the original terragrunt.hcl file, anchoring file creation to the real source tree.
- Visual object: Two parallel directory trees — one with .terragrunt-cache/foo/.../hi.txt lit up, one with foo/hi.txt lit up — a traced path showing which function produces which destination.
- Manim move: split (two directory trees appear side by side), trace (path arrows follow the file to each destination)
- Example seed: foo/terragrunt.hcl creates hi.txt via a local_file resource. Without get_terragrunt_dir(): file lands at .terragrunt-cache/foo/abc123/hi.txt. With get_terragrunt_dir(): file lands at foo/hi.txt beside the config.
- Length band: 2–3 min
- Still lanes: c2v (HCL function call resolving to a path), raster (directory tree annotated with before/after)
- Prerequisites: Terraform path.module variable, local_file resource basics
- Exclusions: Remote module download mechanics, --download-dir flag customization, workspace isolation
- Score: 7/10

## Candidate 05 — Why Terragrunt can inject configuration into commands that are not Terraform
- Source: `docs/src/data/commands/exec.mdx`
- Topic: Input injection — Terragrunt as a general configuration-injection layer
- Hook: Terragrunt resolves HCL inputs and serializes them as TF_VAR_ environment variables before handing control to a subprocess — so any command, not just Terraform, can consume your infrastructure configuration.
- Key case: Running `terragrunt exec -- env | grep TF_VAR_message` shows a resolved HCL input available to a plain shell command, with no Terraform invocation involved.
- The Question: If Terragrunt exists to wrap Terraform, how does an arbitrary shell command read the same resolved inputs that Terraform would receive?
- Core idea: Terragrunt's input resolution is a pipeline stage independent of Terraform invocation. exec decouples these stages: HCL inputs are resolved, serialized as TF_VAR_ key-value pairs, and injected into the subprocess environment — making Terragrunt a general configuration-injection layer for any executable.
- Visual object: A two-stage pipeline: HCL block on the left, resolved TF_VAR_ env vars in the middle, subprocess on the right — first shown with Terraform, then swapped for an arbitrary command.
- Manim move: transform (HCL input block morphs into env var key-value pairs), spread (env vars fan into the subprocess)
- Example seed: inputs = { region = "us-east-1", env = "dev" }. terragrunt exec -- printenv outputs TF_VAR_region=us-east-1 and TF_VAR_env=dev. Swap in a Python script reading os.environ — same values, no Terraform.
- Length band: ~1 min
- Still lanes: c2v (HCL → env vars), raster (terminal output showing TF_VAR injection)
- Prerequisites: Environment variables, Terraform input variable convention
- Exclusions: Dependency resolution, before/after hooks, IAM role assumption via exec
- Score: 6/10
