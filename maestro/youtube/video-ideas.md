# Get started Video Ideas

## Candidate 1 — Why virtual threads enable millions of concurrent tasks without memory overhead

- Source: `maestro-flow/README.md`
- Topic: Parallel task progression via virtual threads
- Hook: Maestro needs to run millions of concurrent tasks, but traditional OS threads would exhaust memory.
- Key case: A workflow with 100,000 parallel subtasks; using OS threads would require 100,000 threads (multi-GB memory), but virtual threads allow a few OS threads to multiplex the load.
- The Question: How can a system execute millions of concurrent tasks without the memory and scheduling overhead of traditional OS threads?
- Core idea: Java virtual threads (lightweight, kernel-scheduled) allow one virtual thread per task without the memory cost of OS threads; the flow engine orchestrates these to progress parallel lists of tasks.
- Visual object: A narrow worker pool (few OS threads) with virtual threads spreading through it, each progressing a task.
- Manim move: spread
- Example seed: A parallel foreach loop with 5,000 subtasks; the flow engine creates 5,000 virtual threads, each running one subtask; the OS schedules these onto 8 physical cores by switching between virtual threads as needed.
- Length band: 3–5 min
- Still lanes: geo (worker pool), c2v (virtual threads enable parallelism), raster (task stream)
- Prerequisites: thread pools, concurrency basics, Java's virtual-thread concept
- Exclusions: advanced DAG patterns (conditional branching, subworkflow, foreach—these build atop the flow engine), Java virtual-thread internals
- Score: 8/10

## Candidate 2 — Why workflows pause and wait for asynchronous signals instead of polling

- Source: `maestro-signal/README.md`
- Topic: Signal-triggered workflow coordination and dependencies
- Hook: Workflows need to wait for external asynchronous events (e.g., a data table is ready), but polling or hardcoding delay is inefficient.
- Key case: Workflow `process_sales` waits for signal `db/sales/2025-07-15`. The upstream ETL finishes, posts the signal. The waiting workflow unblocks and runs. Meanwhile, 49 other daily aggregations also waiting for the same signal all resume simultaneously.
- The Question: How can workflows depend on external asynchronous events without polling, timeouts, or hardcoded retry logic?
- Core idea: Workflows register signal dependencies; when a signal with matching keys is posted, all waiting workflows for that signal unblock simultaneously.
- Visual object: A timeline showing workflows paused at a "wait for signal" gate, external system posting the signal, then all workflows resuming together.
- Manim move: scan
- Example seed: 50 different daily-aggregation workflows all wait for signal `data/loaded/2025-07-15`; at 2:30 AM the ETL posts this signal; all 50 workflows unblock and run in parallel.
- Length band: 2–3 min
- Still lanes: geo (timeline, workflow states), c2v (signal unblocks waiting workflow)
- Prerequisites: workflow orchestration basics, asynchronous coordination concepts
- Exclusions: signal parameter schema, output signals and re-triggering (advanced patterns built atop this), signal archival
- Score: 8/10

## Candidate 3 — Why job queues buffer spikes and distribute work fairly across workers

- Source: `maestro-queue/README.md`
- Topic: Job buffering and distributed parallel execution
- Hook: 50,000 jobs submitted at once but only 20 workers available to execute them; how do you buffer the spike and distribute work fairly?
- Key case: Spike of 50,000 jobs at 2:00 PM; instead of overwhelming the system, they queue up in the database; over the next 2 hours, workers pull batches from the queue and execute in parallel.
- The Question: How do you buffer and fairly distribute millions of jobs to distributed workers without becoming a bottleneck or cascading under load spikes?
- Core idea: Hybrid queue (database-backed for durability, in-memory for speed) decouples job creation from execution; workers dequeue and execute jobs in parallel, absorbing spikes.
- Visual object: A queue (line of jobs) with workers pulling from both ends and executing.
- Manim move: split
- Example seed: 10,000 jobs submitted instantly; they queue. 20 workers each pull 500 jobs and execute them over time; the queue buffers and smooths the spike.
- Length band: 2–3 min
- Still lanes: geo (queue and worker pool), c2v (job flow through queue to workers), raster (queue accumulating jobs)
- Prerequisites: job scheduling, producer-consumer pattern, distributed systems basics
- Exclusions: specific queue data structures, signal/time-trigger queue variants, fairness/prioritization strategies
- Score: 7/10

## Candidate 4 — Why parameters can be computed dynamically instead of hardcoded

- Source: `netflix-sel/docs/lang-guide/example.md`
- Topic: Dynamic parameter generation via expression language
- Hook: Workflow parameters are usually static, but sometimes a step needs to generate a different set of parameters (like all month boundaries in a year) based on inputs.
- Key case: A workflow receives `start_date=2025-01-01` and `end_date=2025-12-31`; it needs to generate a list of all month boundaries [2025-01-01, 2025-02-01, ..., 2025-12-01] for a parallel foreach loop; hard-coded, this would require 12 branches.
- The Question: How can a workflow generate different outputs (arrays, computed values) based on input parameters without branching or hardcoding?
- Core idea: SEL evaluates parameter expressions at execution time; workflows use SEL to compute arrays, transform dates, apply math, and parametrize downstream steps dynamically.
- Visual object: A parameter input flowing into an expression box, then emerging as a computed array.
- Manim move: morph
- Example seed: SEL expression `Util.dateIntsBetween(20250101, 20251231, 30)` generates [20250101, 20250131, 20250303, ...], one date per month; a foreach loop then processes each month in parallel.
- Length band: 2–3 min
- Still lanes: c2v (input → compute → output), raster (array accumulating)
- Prerequisites: parameter systems, expression evaluation, basic date/math concepts
- Exclusions: SEL grammar details, permission/security controls, specific supported classes (Math, DateTime, Util—examples only)
- Score: 7/10

## Candidate 05 — Why a finished step can simultaneously unblock fifty downstream workflows without a coordinator

- Source: `maestro-signal/README.md`
- Topic: Output signals as broadcast inter-workflow triggers
- Hook: A critical ETL step finishes, but 50 consumer workflows are waiting—no central orchestrator can afford to poll all of them for completion.
- Key case: Step `job.1` completes, then emits output signals `db/test/table1` and `db/test/table2`. Every workflow whose trigger configuration matches either signal unblocks simultaneously. One matching workflow is the workflow itself, so the same signal mechanism drives a perpetual re-execution chain without any cron or external scheduler.
- The Question: X (a step finishing) should notify its N downstream workflows to start; the system has no polling loop or central coordinator; why does each consumer wake up exactly once at the right moment?
- Core idea: Output signals are ordinary signal posts emitted by a step; the same matching engine that handles external events handles them—step completion broadcasts to N waiting workflows atomically through the shared signal table, not through a separate notification bus.
- Visual object: A single step box that completes and then emits two signal arrows fanning out to a row of sleeping workflow boxes, which all light up at once.
- Manim move: spread
- Example seed: Step `etl-job` finishes and posts signal `data/sales/ready`; 6 downstream workflows waiting on that signal all start; one of those 6 also emits `data/sales/ready` after its own step finishes, creating an indefinite self-sustaining chain.
- Length band: 2–3 min
- Still lanes: geo (step → signal → fan-out to N workflows), c2v (output signal unblocks N simultaneously)
- Prerequisites: signal dependency concept (Candidate 2), DAG workflow basics
- Exclusions: signal join-key semantics, comparison-operator conditions on signal parameters, time-trigger coordination with output signals
- Score: 7/10

## Candidate 06 — Why parallel foreach iterations produce an indexed array the parent step reads without a reduce step

- Source: `netflix-sel/docs/lang-guide/class-function.md`
- Topic: Cross-iteration output aggregation via indexed parameter collection
- Hook: A foreach loop ran 12 monthly ETL steps in parallel, each computing a row count—but the summary step needs all 12 values without writing a custom aggregator.
- Key case: A foreach with 12 iterations runs `monthly-etl` steps in parallel; each writes output param `row_count`; after all 12 finish, a summary step calls `params.getFromForeach('foreach-job1', 'monthly-etl', 'row_count')` and receives a 12-element Long array, with element 0 from iteration 0, element 1 from iteration 1, and so on.
- The Question: N parallel steps each write the same param name; the parent step expects an ordered array; who is accumulating those writes into index positions as each iteration finishes, and in what order?
- Core idea: The foreach engine appends each iteration's output params to a slot keyed by iteration index as steps complete (in any order); `getFromForeach` reads the completed index and materializes an array in iteration order—turning N asynchronous writes into one deterministically ordered array with no explicit reduce.
- Visual object: Twelve parallel step boxes, each emitting a single value into a numbered slot in a growing array, until all 12 slots are filled and the parent step reads the complete array.
- Manim move: accumulate
- Example seed: Foreach with 5 iterations; steps finish in order 3, 1, 4, 0, 2 and write row counts 950, 800, 1100, 1200, 700; `getFromForeach` returns `[1200, 800, 950, 1100, 700]` (iteration-indexed); summary step sums to 4750 rows.
- Length band: 2–3 min
- Still lanes: geo (fan-out and indexed fan-in), c2v (asynchronous writes collapse into ordered array)
- Prerequisites: foreach pattern, output parameters, SEL expression evaluation (Candidate 4)
- Exclusions: `getFromSubworkflow`, `getFromSignalDependency`, `getFromStep` for non-foreach contexts, SEL type coercion rules
- Score: 7/10
