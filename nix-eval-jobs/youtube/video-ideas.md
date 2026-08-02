# nix-eval-jobs Video Ideas

## Candidate 1 — Why Nix GC might delete derivations you're still building

- Source: `README.md`
- Topic: Garbage collection root creation preventing deletion races
- Hook: The garbage collector doesn't know your evaluation will use a derivation—it sees an unused .drv file and deletes it mid-build
- Key case: `nix-eval-jobs` discovers patchelf-coverage-0.18.0.drv and registers it; before the build starts, Nix's GC sweep deletes it thinking nobody claimed it; build fails with "file not found"
- The Question: Why anchor each individual derivation with a GC root instead of creating one global root protecting all derivations at once?
- Core idea: Per-derivation roots let the GC forget about that derivation once its build completes; a single global root would keep *all* derivations alive forever, leaking disk space until the tool exits
- Visual object: A directed graph of Nix store files, with GC attempting to traverse and delete unreferenced nodes, stopping when it encounters an anchor (root) blocking deletion
- Manim move: trace
- Example seed: Evaluate 5 derivations → attach 5 roots → GC runs → marks 2 derivations safe to delete → 3 roots remain holding 3 derivations
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Nix store, garbage collection, derivations
- Exclusions: Nix's full GC algorithm; implementation of root files; Hydra's integration
- Score: 8/10

## Candidate 2 — How restarting worker threads prevents memory bloat

- Source: `README.md`
- Topic: Worker process recycling to reclaim memory mid-evaluation
- Hook: A single evaluator thread consuming 3.9GB of your 4GB RAM doesn't return it when that evaluation finishes—it stays allocated and blocks the next job
- Key case: Worker A evaluates a large NixOS system, balloons to 3.5GB; Worker B starts and uses 0.8GB; system OOMs instead of recycling Worker A's memory
- The Question: Why kill and restart a worker when it hits the memory threshold instead of just capping each worker's initial heap size?
- Core idea: Capping initial heap starves legitimate large evaluations; monitoring + restarting lets each job consume what it needs, then releases the memory back to the pool for the next job and the subsequent build phase
- Visual object: A timeline showing one worker's memory usage bar climbing toward a threshold line, hitting it, collapsing to zero, then climbing again for the next job
- Manim move: accumulate → collapse
- Example seed: 4 jobs each needing 2.2GB, 4GB worker cap; Job 1 uses 2.2GB → restart → Job 2 uses 2.2GB → restart; all finish vs. OOM on Job 2
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Process memory, multi-worker parallelism, evaluation cost in NixOS
- Exclusions: Kernel memory management; Nix evaluation internals; setting the threshold heuristic
- Score: 8/10

## Candidate 3 — Why evaluation should report cache status before builds start

- Source: `README.md`
- Topic: Binary cache lookup during evaluation to defer build decisions
- Hook: After evaluating 1000 derivations, you don't know which ones are already built and cached in your binary substituter
- Key case: Evaluate a large flake → discover 1000 derivations; naive CI queues all 1000 for building; informed CI checks `cacheStatus` → 920 are cache hits → queue only 80 for building
- The Question: Why check the binary cache during evaluation instead of letting each builder discover cache misses on demand?
- Core idea: Checking at evaluation time means downstream tools (Hydra, CI) get a status field immediately; they filter build jobs before queueing, so builders never process cache hits, freeing compute for real work
- Visual object: A table or grid of evaluated derivations with a `cacheStatus` column showing hit, miss, or unknown per row
- Manim move: scan → morph
- Example seed: 5 jobs evaluate; cache check returns [hit, miss, hit, miss, hit] → builder receives 2 jobs instead of 5
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Binary caches, substituters, derivation hashing, CI pipelines
- Exclusions: How binary caches compute or check hashes; NAR format; substituter redundancy
- Score: 7/10

## Candidate 4 — Why individual job failures don't stop the whole evaluation

- Source: `README.md`
- Topic: Isolation of evaluation failures across worker threads
- Hook: One broken Nix expression in a jobset causes the entire evaluation to fail, blocking all downstream results
- Key case: Hydra evaluates 100 NixOS configs; config #47 has a syntax error in a module; all 100 jobs fail to evaluate; users see no results and cannot triage
- The Question: Why let broken jobs fail silently instead of halting evaluation immediately?
- Core idea: Early halt saves compute but loses information; continuing means you learn which jobs succeeded *and* which failed; CI tools see a mixed result (99 passing + 1 error log) instead of a blanket "error"
- Visual object: A grid of job squares, one red (failed evaluation), the rest green (succeeded), all completed in a single pass
- Manim move: split → highlight
- Example seed: 10 jobs, job 5 has a syntax error; jobs 1–4 and 6–10 complete anyway → downstream tool sees 9 derivations + 1 error report
- Length band: 1–2 min
- Still lanes: c2v
- Prerequisites: Parallel computing, error isolation models
- Exclusions: Nix-specific syntax errors; partial evaluation recovery; error aggregation strategies
- Score: 7/10

## Candidate 05 — Why the first build starts before the last derivation is evaluated

- Source: `README.md`
- Topic: Streaming newline-delimited JSON to pipeline evaluation and building in parallel
- Hook: Batch output forces every derivation to be evaluated before any build can start, serializing two phases that could overlap
- Key case: CI evaluates 3 NixOS configs with one worker (5s each); batch mode holds all output until 15s and the first build finishes at 25s; the streaming consumer starts build #1 at second 5, so the first result is in hand at second 15
- The Question: If the end goal is a list of derivations, why emit each one the moment it is evaluated rather than collecting all results and printing them at the end?
- Core idea: Newline-delimited JSON lets any process reading stdout treat each line as an independent event; a downstream builder (nix-fast-build, CI) consumes derivations as a stream, so evaluation and building run as a pipeline — the two phases overlap in wall time instead of running end-to-end
- Visual object: Two horizontal timelines stacked vertically — top row: evaluation slots completing one by one; bottom row: build slots starting as arrows land from above, not waiting for the top row to finish
- Manim move: trace
- Example seed: 3 derivations, 5s eval each, 10s build each; batch → first result at second 25; streaming → first result at second 15; third result: both at second 25 but system is 10s more utilized *(illustrative)*
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Producer-consumer pipelines, evaluation vs build phases in Nix
- Exclusions: JSON parsing mechanics; specific CI integrations; nix-output-monitor internals; how workers are assigned attribute paths
- Score: 7/10
