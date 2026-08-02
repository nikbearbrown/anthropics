# cargo-nix-plugin Video Ideas

## Candidate 1 — Non-obvious that a rustc drop-in replacement preserves Nix store hashes
- Source: `README.md`
- Topic: Clippy-driver caching architecture
- Hook: Linting a 100-crate workspace should be slow; it isn't, because dependencies compiled once are cached across both paths
- Key case: 5 workspace members + 145 dependencies; rustc compiles deps once, clippy-driver re-checks only the members, both write to identical store paths
- The Question: If workspace members use clippy-driver and dependencies use rustc, why don't they resolve to different Nix store hashes and lose the cache?
- Core idea: clippy-driver is a rustc drop-in—identical flags, identical artifacts; when passed as the `rust` override for workspace members only, dependencies still hash identically (same inputs, same output hash = same store path = reused)
- Visual object: Dependency tree with two colors: deps in gray (compiled once with rustc), workspace members in accent color (re-checked with clippy-driver); both point to the same store path
- Manim move: split
- Example seed: Workspace has 3 binaries, 30 internal libs, 140 transitive deps; deps compile once (~5 min); then each binary re-runs clippy (~30 sec each); total ~6.5 min vs ~30 min if all 173 were linted (illustrative: realistic workspace)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: buildRustCrate, Nix store hash model, rustc artifact semantics
- Exclusions: clippy lint passes, rustc flag details, Nix module system
- Score: 8/10

## Candidate 2 — Replacing a checked-in 50K–100K line generated file with a single Nix function call
- Source: `README.md`
- Topic: Primop-based Cargo workspace resolution
- Hook: Codegen tools bloat repositories; this one eliminates the entire generation step and checked-in artifact
- Key case: crate2nix generates `Cargo.nix` (~80K lines for 200-crate workspace); plugin replaces it with one line: `cargo-nix-plugin.lib { src = .; }`
- The Question: Without a pre-generated metadata file, how can Nix evaluate a Cargo workspace at eval time without a `cargo` binary?
- Core idea: A Nix plugin (C++ primop) reads `Cargo.lock` and sparse registry index directly during evaluation, resolving the graph in-place; no generation, no checked-in artifact
- Visual object: Split screen—Cargo.nix scrolling (80K lines, minutes to render) vs function call (one line); collapse transition
- Manim move: collapse
- Example seed: Workspace with 180 crates, 1,200 Cargo.lock entries; crate2nix generates 94K lines; plugin replaces with function that reads lock at eval time (illustrative: mid-size monorepo)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: crate2nix, Nix evaluation model, primop concept
- Exclusions: C++ implementation, CMake build, plugin loading mechanism
- Score: 8/10

## Candidate 3 — Sparse registry caching makes offline evaluation work without pre-fetching all crate sources
- Source: `README.md`
- Topic: Index metadata caching and incremental fetching
- Hook: Offline evaluation usually requires all inputs present upfront; this resolver fetches metadata incrementally and reuses it
- Key case: First eval of 100-dependency workspace fetches ~30 KB total (~200 bytes per crate's index entry) into `$CARGO_HOME`; second eval reuses cache, avoiding network
- The Question: Why can the resolver work offline without pre-downloading all crate sources—only metadata?
- Core idea: Cargo resolution needs only metadata (version, features, deps) from the sparse registry, not source; metadata is small (~200 bytes per crate); cached in `$CARGO_HOME` on first fetch, reused on subsequent evals
- Visual object: `$CARGO_HOME` directory tree; first run fills with one file per dependency; second run shows directory unchanged (cache hits shown as light)
- Manim move: accumulate
- Example seed: Workspace with 80 unique deps; first eval fetches ~30 KB and takes ~2 sec; second eval is instant (illustrative: modest first-run overhead, zero on reruns)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: sparse registry concept, Cargo.lock structure, `$CARGO_HOME` role
- Exclusions: cargo mirror configuration, cargo-nix-prefetch tool, git sources (different mechanism)
- Score: 8/10

## Candidate 4 — All-features flag makes feature-gated code visible to clippy
- Source: `README.md`
- Topic: Feature-flag accumulation for comprehensive linting
- Hook: Code behind `#[cfg(feature = "...")]` is invisible to clippy on default features; enabling all features brings it into view
- Key case: Crate with 3 features (async, serde, vendored); code under `#[cfg(feature = "async")]` skipped by default clippy; with `clippyAllFeatures = true`, all features enabled, code is linted
- The Question: If you lint with default features only, you miss all code behind feature gates—how do you catch bugs in those paths?
- Core idea: Wrapper accumulates all workspace features into one set, passes to each member; cfg() conditions evaluate true for every flag; previously dead code becomes compiled and linted
- Visual object: Source code with `#[cfg(feature = ...)]` blocks; lines grayed out (inactive) by default, then highlighted (active) as features toggle on
- Manim move: morph
- Example seed: Member crate has `#[cfg(feature = "async_runtime")] fn use_tokio() { ... }`; default features leave it grayed; clippyAllFeatures=true makes it active and linted (illustrative: single gate, shows principle)
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: Rust feature flags, cfg() macro
- Exclusions: clippy findings, feature interaction graphs, cargo feature resolution
- Score: 7/10

## Candidate 05 — Git dependencies block Nix evaluation on the network; registry dependencies do not
- Source: `README.md`
- Topic: Eval-time source fetching for git dependencies
- Hook: Resolving a registry crate needs 200 bytes from the sparse index; one `git+` entry in `Cargo.lock` forces a full repository clone before Nix evaluation can continue
- Key case: Workspace with 80 registry deps and one `git+https://github.com/Byron/gitoxide#abcdef` dep; registry deps resolve from cached index entries in milliseconds; the git dep triggers `builtins.fetchGit { allRefs = true; submodules = true; }` at eval time, blocking until the clone completes, so the resolver can read its `Cargo.toml` and find the workspace member subdirectory
- The Question: Registry resolution works offline after a first warm-up; a single git dep restores the network dependency at every evaluation — what does the sparse index store that git history fundamentally cannot provide?
- Core idea: The sparse registry index encodes metadata (version, features, dep list) for every published crate; a git repo is unstructured source — no such index exists, so the resolver must fetch the tree to read `Cargo.toml`, discover workspace membership, and map the subdirectory before it can emit a `buildRustCrate` call; the `gitSources` override substitutes a local path to break the network dependency
- Visual object: Two parallel resolution paths side by side — registry (tiny index entry → attrset, one step) and git (fetchGit → Cargo.toml parse → member locate → attrset, three steps) — with the extra fetch step pulsing to show where eval stalls
- Manim move: split
- Example seed: Workspace with 50 registry deps and 1 git dep; eval warm = 80 ms; add git dep = eval stalls ~4 s on clone; add `gitSources` pointing at a local bare clone = back to 80 ms (illustrative: mid-sized workspace)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Nix evaluation model, sparse registry concept, Cargo.lock `git+` format
- Exclusions: submodule recursion edge cases, `gitSources` narHash pinning, private repository authentication
- Score: 8/10

## Candidate 06 — UBSan can be bundled into a dlopen'd plugin; ASan physically cannot
- Source: `cpp/CMakeLists.txt`
- Topic: Sanitizer selection under shared-library constraints
- Hook: AddressSanitizer and UBSan both catch memory bugs, but the same property that makes a Nix plugin possible — being loaded with `dlopen` into an uninstrumented host — makes ASan impossible and forces a specific `--whole-archive` linker trick just to keep UBSan alive
- Key case: `ENABLE_SANITIZERS=ON` compiles with `-fsanitize=undefined` but omits `-fsanitize=function,vptr`; the UBSan minimal runtime is linked via `--whole-archive` so every handler symbol is resolved at `dlopen` time; ASan is not attempted at all — it would require wrapping the entire `nix` process at launch with `LD_PRELOAD`, which the plugin cannot control
- The Question: ASan and UBSan are both LLVM sanitizers compiled into the same binary — why can one live entirely inside a `.so` and the other cannot?
- Core idea: ASan intercepts `malloc`, `free`, and `mmap` globally via `LD_PRELOAD`; when a plugin is `dlopen`'d into an uninstrumented host those hooks are absent and ASan's shadow memory is never initialized, causing immediate crashes; UBSan only emits inline trap checks at suspicious call sites plus a small reporting runtime — both fit inside the `.so`; `--whole-archive` on the static UBSan runtime forces every handler symbol into the final shared library so none are left unresolved when the linker's lazy resolution would be too late
- Visual object: Process address space divided into host (gray, uninstrumented) and plugin `.so` (accent, UBSan-instrumented) with a dashed `dlopen` boundary; an `LD_PRELOAD` arrow attempts to wrap the whole process, hits the boundary, and is rejected; the bundled UBSan runtime shown as a small block inside the `.so` only
- Manim move: split
- Example seed: Plugin function performs unchecked array index; UBSan inline check fires → handler in bundled runtime → `stderr` message → process continues; same scenario with ASan requires relaunching `nix` as `LD_PRELOAD=libasan.so nix ...`, crashing if the host wasn't compiled with ASan (illustrative: single out-of-bounds access)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: AddressSanitizer, UndefinedBehaviorSanitizer, `dlopen` / shared library loading model
- Exclusions: specific UBSan sub-checks excluded (`-fsanitize=function,vptr` rationale), CMake build configuration details, Nix plugin compatibility versioning
- Score: 8/10
