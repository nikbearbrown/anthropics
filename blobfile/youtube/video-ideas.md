# blobfile Video Ideas

## Candidate 1 — Implicit directory inference in flat storage
- Source: `README.md` (Paths section, commented-out example)
- Topic: Directory semantics in key-value stores
- Hook: GCS and Azure store files as a flat list with "/" as part of the filename, yet code assumes directories exist—but when?
- Key case: Upload "models/gpt/weights.bin" to GCS. Call `isdir("models/gpt")`. No marker file was created, only the file itself. Should it return True?
- The Question: When storage backends erase directories and flatten them to string prefixes, how do you decide whether an inferred directory counts as real?
- Core idea: Implicit directories are inferred from file prefixes alone; explicit directories require marker files like "dir/". The code must choose one semantics and be consistent across walk, listdir, and isdir.
- Visual object: A tree diagram on the left (hierarchy of "models/gpt/weights.bin") beside a flat list notation on the right (single string entry), with arrows showing how prefixes become directories.
- Manim move: split (tree flattens to list), scan (extracting directory structure by prefix)
- Example seed: Upload three files—"data/train.csv", "data/test.csv", "output/model.pkl"—to a bucket. Walk the tree. The directories "data" and "output" exist only as prefixes; no metadata marker was ever created.
- Length band: 2–3 min
- Still lanes: c2v (directory-existence state machine), raster (tree vs. flat list notation)
- Prerequisites: GCS/Azure basics (key-value store model, no true directories)
- Exclusions: prefix-matching implementation, glob pattern efficiency, walk/listdir sorting behavior
- Score: 9/10

## Candidate 2 — Chunk-based retry state for large uploads
- Source: `README.md` (azure_write_chunk_size, google_write_chunk_size); `CHANGES.md` ("Use block blobs instead of append blobs")
- Topic: Resilience through granular retry units
- Hook: Uploading a 10 GB file as a single atomic operation fails on transient network errors. Chunking it into retry units lets you survive—but now you must track which chunks succeeded and which remain.
- Key case: Azure block blob upload of 16 GB file with `azure_write_chunk_size=8MB`. Blocks 0–127 upload; block 128 fails (network cut). On reconnect, only retransmit block 128, not all 128 before it.
- The Question: If you divide a large upload into chunks to make failures survivable, how do you know which chunks are committed and which are still pending after a break?
- Core idea: Each chunk becomes an uncommitted block; the server tracks which blocks have been committed to the blob. Resume from the first uncommitted block, not the file start. This transforms upload failure from "start over" to "continue from here."
- Visual object: A file split into colored blocks; some green (committed), one red (failed), rest gray (pending). A commit list visible on the side, growing over time.
- Manim move: split (file into blocks), scan (blocks becoming green as they commit), trace (commit list accumulating)
- Example seed: Upload a 32 MB file with 8 MB chunks. Blocks 0–3: block 0 succeeds, block 1 fails mid-transmission. On retry, send only block 1 again, not blocks 0–1.
- Length band: 2–3 min
- Still lanes: c2v (block state machine—pending/committed/failed), raster (file with block coloring)
- Prerequisites: large file uploads, transient network failures
- Exclusions: Azure block blob API details, exponential backoff/jitter, cross-account copy optimization
- Score: 9/10

## Candidate 3 — Authentication fallback cascade across environments
- Source: `README.md` (Authentication sections for Google Cloud Storage and Azure Blobs)
- Topic: Context-aware credential discovery
- Hook: Code must run on a laptop (local gcloud login), in CI (JSON service account), and on GCP/Azure (managed identity). One credential method works in one environment and fails in the other two. Yet the user writes the same code in all three.
- Key case: A script calls `bf.BlobFile("gs://bucket/file", "rb")` from three places: (1) local macOS, with GOOGLE_APPLICATION_CREDENTIALS pointing to a service account JSON; (2) GitHub Actions runner, no env var, but DefaultAzureCredential available; (3) GCP Cloud Run, neither, but metadata server available. All three execute the same code path.
- The Question: How do you design credential discovery that tries multiple sources in order, succeeds when any one works, and requires no manual selection?
- Core idea: Try methods in sequence—env vars, application defaults, metadata server, CLI cache, anonymous—and use the first one that succeeds. Each method fails fast if unavailable, unblocking the next. The system is environment-agnostic.
- Visual object: A waterfall diagram with five credential methods, each with a pass/fail gate. Flow stops at first success, or proceeds down to the next failure.
- Manim move: scan (checking each method top to bottom), morph (successful branch highlighted and flows left), collapse (other branches fade)
- Example seed: Same script, three runs: (1) laptop has GOOGLE_APPLICATION_CREDENTIALS → uses that; (2) CI has none → tries app defaults → fail → tries metadata → unavailable → fail → tries CLI → success; (3) prod → skips env/CLI → metadata server → success.
- Length band: 2–3 min
- Still lanes: c2v (decision tree of auth attempts), raster (environment icons: dev/CI/prod)
- Prerequisites: credential types (env var, service account, workload identity, CLI), multi-environment deployment
- Exclusions: OAuth token refresh, OIDC federation details, credential file format/parsing
- Score: 9/10

## Candidate 4 — Streaming vs. buffered read mode tradeoff
- Source: `README.md` (BlobFile streaming parameter)
- Topic: I/O strategy tradeoff between latency and seeking
- Hook: Reading a 100 GB ML model from GCS—you can fetch the first byte instantly and read incrementally (streaming), or wait for the full download and then seek freely (buffered). You cannot have both with the same file.
- Key case: Load a large transformer checkpoint. With `streaming=True`, the constructor returns immediately and you read 8 MB chunks on demand. With `streaming=False`, the constructor blocks for a 10-minute download, then seeks and re-reads are instant.
- The Question: Why does streaming latency exclude efficient seeking? Can you build a mode that gives you fast-first-byte *and* instant seeks?
- Core idea: Streaming reads directly from remote; buffering downloads to local disk first. These are antipathetic: streaming avoids download latency but makes seeking expensive (must re-download from start), buffering eats startup latency but enables instant seeks. The library exposes the choice because no single strategy dominates.
- Visual object: Two timelines side by side. Top timeline: streaming (instant start, then linear byte arrivals). Bottom timeline: buffered (long download block, then instant seek operations).
- Manim move: split (two timelines diverge), trace (bytes arriving over wall-clock time)
- Example seed: Train a model from a 50 GB checkpoint on GCS. With streaming=True, training begins immediately, but seeking backward (restart from epoch 2) requires re-download. With streaming=False, 5-minute download block, then instant seeks and restarts.
- Length band: 2–3 min
- Still lanes: c2v (latency vs. seek cost curve), raster (timeline of bytes arriving)
- Prerequisites: file I/O basics, network latency, remote storage costs
- Exclusions: buffer size tuning, TCP congestion, GCS read consistency, caching headers
- Score: 8/10

## Candidate 5 — Topological ordering for parallel tree copy
- Source: `docs/parallel_examples.md` (copytree example with topdown=False)
- Topic: Extracting parallelism from sequential dependency structures
- Hook: Copying a 1000-file directory tree in parallel is fast—unless a copy tries to write to a file before its parent directory exists. Serial copy is safe but slow. Can you parallelize safely by reordering?
- Key case: Copy `gs://src/a/b/c.txt`, `gs://src/a/b/d.txt`, `gs://src/a/e.txt` to `gs://dst/`. If the copy processor encounters them in random order, it may try to write "a/b/c.txt" before creating "a/b/". The walk with `topdown=False` collects all ops in an order where all parents appear before their children.
- The Question: If a sequential task has implicit dependencies (directories must exist before files), can you extract a parallel execution schedule that respects them without serializing everything?
- Core idea: Use a bottom-up tree walk (`topdown=False`) to collect operations in dependency order: all mkdir ops first, then all copy ops. Serialize mkdirs (few, fast), parallelize copies (many, slow). Within each phase, no task depends on another.
- Visual object: A directory tree with numeric walk order (bottom-up direction). Below it, a Gantt chart: yellow bars for mkdir tasks (sequential block), blue bars for copy tasks (parallel block).
- Manim move: rotate (tree rotated bottom-up), scan (numbering walk order), split (mkdirs vs. copies into two bands), accumulate (parallel copy bars grow)
- Example seed: Copy a 500-file tree (50 directories, 450 files). Walk yields mkdirs for 50 dirs (20 ms serial), then 450 copy ops (parallel, finish in ~100 ms). Total ~120 ms instead of 450× file latency.
- Length band: 3–5 min
- Still lanes: c2v (dependency graph as DAG), raster (tree with walk-order numbers, Gantt chart)
- Prerequisites: tree traversal, directed acyclic graphs, multiprocessing
- Exclusions: ProcessPoolExecutor internals, GCS cross-region remote copy, individual file retry logic
- Score: 7/10

## Candidate 06 — A write that reads its own past: optimistic concurrency via version tags
- Source: `CHANGES.md` (v2.0.2: "Support a `version` parameter for writing files to Azure, if the `version` doesn't match the remote version, a `VersionMismatch` error will be raised")
- Topic: Optimistic concurrency control for shared blob state
- Hook: Two workers both read the same blob, compute independent updates, and write back — the second write silently erases the first unless each writer carries proof of what it last saw.
- Key case: Two training jobs read `"config.json"` at version `"abc123"` and both compute updated hyperparameters. Job A writes first, bumping the blob to version `"def456"`. Job B then writes with expected version `"abc123"` — the backend raises `VersionMismatch`, forcing B to re-read the now-updated config and recompute.
- The Question: If two concurrent workers read the same version of a file and both submit writes, how does the second writer know its read-compute-write cycle was invalidated — without any lock ever being held?
- Core idea: Each write carries the version tag the writer last observed. The backend atomically checks: if remote version ≠ expected version, reject with `VersionMismatch`. This converts a silent lost-update into a detectable conflict; the loser retries from a fresh read rather than overwriting silently.
- Visual object: A version tag badge on a blob, two parallel timelines converging at a single write gate — one passes through, one bounces back to the read step with the new tag.
- Manim move: split (parallel timelines diverge at read), morph (version badge changes on first commit), collapse (second writer's path redirected back to start with updated tag)
- Example seed: Two workers share `"counter.txt"` containing `5` at version `v1`. Both read, both compute `6`. Worker A writes with expected `v1` — succeeds, blob is now `6` at `v2`. Worker B writes with expected `v1` — `VersionMismatch`; re-reads `6` at `v2`, computes `7`, writes successfully at `v3`.
- Length band: 2–3 min
- Still lanes: c2v (read-check-write state machine with retry loop), raster (two timelines with version badge annotations)
- Prerequisites: concurrent processes, read-modify-write cycles, blob storage basics
- Exclusions: Azure ETag wire format, pessimistic locking alternatives, MVCC in relational databases, CAS instruction semantics
- Score: 8/10
