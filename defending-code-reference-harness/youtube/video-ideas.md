# Defending Code Reference Harness Video Ideas

## Candidate 1 — Temporal desync: validate once, write forever
- Source: `targets/drlibs/README.md`
- Topic: Two-pass parsing desynchronization
- Hook: A count field is validated in one pass but written unconditionally in another—the buffer overflow waits between them.
- Key case: WAV `smpl` chunk parser validates `sampleLoopCount` in the count-prediction phase, then loops `sampleLoopCount` times in the read phase without re-checking. Attacker sends count=2000; only 512-item heap buffer allocated.
- The Question: If you validate a safety-critical field in an early pass, will a second pass always re-validate it before using it, or will the code diverge as the phases become temporal and forgotten?
- Core idea: Two-phase parsing creates a temporal window where a field validated in one phase is re-used unchecked in another. The second phase consumes the field from the input stream again, assuming the first phase validated it. If the two phases don't share the same validation point, the check is forgotten and the field flows through unconstrained.
- Visual object: Two side-by-side code blocks. Left: `if (sampleLoopCount > MAX_SAMPLES) return error; alloc_heap(sampleLoopCount * 16)`. Right: `for (i = 0; i < sampleLoopCount; i++) heap[i] = read_next_struct()`. An arrow labeled `sampleLoopCount` flows from input to left (checked), and a separate arrow flows from input to right (unchecked).
- Manim move: split
- Example seed: RIFF/WAV file with a `smpl` (sample loop) chunk. Count-pass reads the first 4 bytes as `loop_count`, checks `if (loop_count > 512) error`, allocates `512*16` bytes. Read-pass reads the same field again and loops `loop_count` times. Attacker sends `loop_count=2000`. Count-pass never executes (conditional branch). Read-pass loops 2000 times into 8192 bytes → 32000-byte write → heap overflow. *Illustrative*.
- Length band: ~2 min
- Still lanes: c2v
- Prerequisites: memory safety, buffer overflow, parsing concepts
- Exclusions: timing-based races (logic desync, not race condition); use-after-free by delayed validation (different pattern)
- Score: 10/10

## Candidate 2 — Determinism as a gate: the 3/3 reproducibility rule
- Source: `harness/README.md`, `docs/pipeline.md`
- Topic: Reproducible crash verification via repeated execution
- Hook: The pipeline doesn't trust a single crash—it runs the same PoC three times and advances only if all three abort. Static noise becomes deterministic signal.
- Key case: dr_libs find-agent crafts a malformed RIFF/WAV file triggering a heap OOB write. Grade agent runs the PoC in three separate containers with identical input. All three: ASAN abort. Grade: 5/5. Contrast: fuzzer artifact crashing once due to malloc randomization; grade: 1/3, discarded.
- The Question: If you run an instrumented binary three times with identical input, will a real memory-corruption bug crash all three times, while false positives (fuzzer artifacts, malloc timing) crash only 1–2 times?
- Core idea: ASAN-instrumented binaries deterministically detect real memory errors. Randomized allocators or timing-dependent artifacts produce inconsistent crashes. The 3/3 rule acts as a filter: only crashes that occur in all three isolated runs advance to reporting. This decouples true bugs from fuzzer noise.
- Visual object: Three parallel containers, each with an ASAN-instrumented binary and the same input file. Each outputs either a crash symbol (✓) or no-crash (✗). Below, a gate: only if all three are ✓ does the result emerge as a graded finding.
- Manim move: duplicate
- Example seed: A crafted PNG file designed to trigger an integer-overflow heap allocation. Run 1 in container A: ASAN detects heap-buffer-overflow, process aborts. Run 2 in container B: same crash, same ASAN report. Run 3 in container C: same crash. Grade: 3/3, advance. Compare: malloc behavior depends on system state. Run 1: malloc(huge) fails, exits. Run 2: malloc succeeds, process continues. Run 3: malloc fails. Grade: 1/3, discarded. *Illustrative*.
- Length band: ~2 min
- Still lanes: c2v
- Prerequisites: ASAN, reproducibility testing, memory instrumentation
- Exclusions: race conditions in allocators; resource-limit enforcement (cgroups, RLIMIT); OOM killer behavior
- Score: 9/10

## Candidate 3 — Independent agents, shared source, separate crashes
- Source: `targets/alsa/README.md`, `targets/drlibs/README.md`
- Topic: Convergence and deduplication in parallel agent discovery
- Hook: Fifteen agents read the same source code in isolation. Most find different bugs, but some converge on the same one—and the judge agent has to decide if that's confidence or duplication.
- Key case: alsa CVE-2026-25068 found by run_13, but parallel runs produced 14 other distinct crashes. Judge dedup grouped crashes by stack-trace signature, revealing that multiple agents had hypothesized different angles to the same vulnerability class (heap OOB in the mixer control parser).
- The Question: If N agents work in parallel with no shared state, reading the same source and crafting independent inputs, will they converge on the same bugs (signaling high-signal code paths), or diverge and explore the surface in parallel?
- Core idea: Agents form independent hypotheses from different reading angles ("integer overflow in sample count" vs. "unchecked loop bound"). Each crafts inputs to test their hypothesis. Crashes emerge independently. Judge dedup compares stack traces and root-cause signatures; crashes from the same function with the same ASAN type are grouped. Convergence suggests high-signal code paths; divergence suggests broad attack surface.
- Visual object: Three agent processes in parallel bubbles, each with its own hypothesis-→-input-craft-→-crash loop. Below, a judge agent merging crash signatures: three separate crashes overlap on a Venn diagram, grouped as one root cause.
- Manim move: collapse
- Example seed: FLAC decoder with vulnerability in sample-count multiplication. Agent A reads allocation logic and hypothesizes "integer overflow in `samples * channels`". Agent B reads bitstream parser and hypothesizes "unchecked field boundary in STREAMINFO". Agent C reads codec dispatch and hypothesizes "missing bounds in per-codec buffer". All three craft FLAC inputs. All three crash in the same allocation function at different input vectors. Judge dedup groups them as one bug: "integer overflow in allocation sizing". Convergence signals the code path is obvious and high-confidence. *Illustrative*.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: parallel execution, crash deduplication, signal vs. noise
- Exclusions: multi-agent resource contention; agent-to-agent communication protocols; distributed fault tolerance
- Score: 8/10

## Candidate 4 — DoS is not memory corruption: the allocator_may_return_null triage flip
- Source: `targets/drlibs/README.md`
- Topic: Distinguishing denial-of-service from memory-corruption crashes
- Hook: An attacker sends input that causes a massive memory allocation. The binary crashes. Is it a memory corruption bug or just running out of memory? Running the same input with one ASAN flag changes everything.
- Key case: dr_flac CVE-2025-14369 (integer overflow in frame count). Agents craft FLAC files with `totalPCMFrameCount=2^63`. Computation: `alloc_size = frameCount * channels * bytes_per_sample` → overflow → malloc(huge_size) → abort. Agents ran `ASAN_OPTIONS=allocator_may_return_null=1`, saw the process exit cleanly, determined: DoS, not memory corruption. They moved on to hunt for real corruption instead.
- The Question: If an attacker sends input that triggers a massive allocation request, will the crash be a real memory-corruption vulnerability, or just a resource-exhaustion (DoS) bug? And how do you tell the difference with only sandboxed execution?
- Core idea: ASAN's `allocator_may_return_null` flag makes malloc return NULL instead of aborting on over-allocation. If the code is robust (checks for NULL), the process exits cleanly. If the code is vulnerable (dereferences NULL without checking), the crash persists. Running the same PoC twice—once with and once without the flag—reveals whether the crash is real corruption or just resource exhaustion.
- Visual object: An allocation request (malloc size=huge). Two branches: (1) with `allocator_may_return_null=0`: malloc aborts, process exits (DoS-only path). (2) with `allocator_may_return_null=1`: malloc returns NULL, code either checks and exits cleanly, or dereferences and crashes (real corruption). A triage agent runs both and compares outcomes.
- Manim move: compare
- Example seed: FLAC decoder reads `totalPCMFrameCount=2^63`. Code computes `buffer_size = frame_count * channels * 8`. Overflow wraps to tiny size. malloc(tiny) succeeds. Code writes frame_count items into undersized buffer → heap overflow. Different scenario: code checks `if (overflow) return error;` and exits cleanly before malloc. Attacker sends same input. Run 1 with normal ASAN: crash at malloc(huge). Run 2 with `allocator_may_return_null`: malloc returns NULL, code exits cleanly. Triage outcome: code is robust; the bug is benign or DoS-only. *Illustrative*.
- Length band: ~2 min
- Still lanes: c2v
- Prerequisites: ASAN options, memory allocation semantics, NULL checking
- Exclusions: race conditions in allocators; actual resource-limit enforcement (cgroups); OOM killer behavior
- Score: 8/10

## Candidate 5 — Five stages, one oracle: the vulnerability pipeline as feedback loop
- Source: `harness/README.md`, `docs/pipeline.md`
- Topic: Multi-stage vulnerability discovery pipeline with autonomous agents
- Hook: One command triggers five sequential stages: agents read source and partition the attack surface, parallel finders craft inputs, a grader verifies each crash, a judge deduplicates and ranks, and a reporter analyzes exploitability. Each stage feeds the next.
- Key case: `bin/vp-sandboxed run drlibs --auto-focus --runs 15 --parallel --stream`. Recon identifies 14 focus areas in 6 min. Find agents distribute round-robin and land CVE-2026-29022 in 5.6 min. Grade verifies 3/3. Judge confirms not a known bug. Reporter grades exploitability 5/5. Results appear in `/reports/bug_NN/` as judge completes each finding.
- The Question: How do you orchestrate five independent agent roles so that each stage's output becomes the next stage's input, and the system never wastes a token on a false positive or duplicate?
- Core idea: The pipeline is a state machine where each stage outputs a signal that gates the next. Recon generates focus areas (attack-surface partitions) → Find agents search those areas in parallel and produce PoCs → Grade verifies reproducibility (3/3 rule) → Judge groups by root-cause signature and filters known bugs → Reporter produces exploitability analysis. Each output is consumed by the next stage; failures are terminal (bad PoC → no grade, no report). Parallelization at Find amplifies coverage; dedup at Judge prevents duplicate reports.
- Visual object: A flow diagram with five boxes (Recon, Find, Grade, Judge, Report) connected by arrows. Find has multiple agent instances spreading out, then converging back through Grade. Known bugs list flows into Judge. Final reports emerge from Report.
- Manim move: split
- Example seed: 30k-LOC C library with four parsing subsystems. Recon reads source and outputs: "JPEG header parsing", "PNG chunk decoding", "GIF frame dispatch", "WebP bitstream reading". Four find agents assigned round-robin. Agent A targets JPEG, crafts malformed JFIF after 3 min. PoC crashes binary when fed to Grade. Grade runs it 3 times in isolated containers; 3/3 abort with heap-buffer-overflow. Judge receives crash, checks known_bugs.jsonl, doesn't match, assigns exploitability score. Reporter analyzes stack trace, determines attacker can control frame_idx via file bytes, reports as memory-corruption vulnerability. Result lands in `/reports/bug_001/report.json` in 10 minutes. *Illustrative*.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: autonomous agents, vulnerability discovery, reproducibility testing
- Exclusions: agent-to-agent communication beyond state handoff; cross-run learning (agents don't update prompts based on prior runs); manual triage workflows
- Score: 8/10

## Candidate 06 — Format structure is the moat: same agent, same runs, 14× find-time gap

- Source: `targets/drlibs/README.md`, `targets/htslib/README.md`
- Topic: Input format complexity as an automated find-time determinant
- Hook: The same agent, the same run count, two parsing paths in the same binary. One path yields a confirmed heap overflow in 5.6 minutes. The other yields zero crashes after a full wave, takes 80 minutes in a dedicated second wave—and the vulnerability isn't deeper, just harder to reach through the format.
- Key case: drlibs wave 1. WAV `smpl` chunk is flat struct-packed with no checksum: run_4 directly corrupts a length field and crashes in 5.6 min. FLAC STREAMINFO is a CRC-protected bitstream: 5 FLAC-focused agents craft ~40 inputs, every one rejected by the CRC gate before the vulnerable parser runs. Zero crashes. Wave 2 focuses only on FLAC with a single focus area; 4/5 agents land crashes in ~70 min after learning to compute valid CRCs before corrupting semantic fields. The corpus confirms the pattern a second time: BGZF `.gzi` (8-byte count header, trivially simple) crashes in ~5 min; CRAM (multi-stage container → slice → codec dispatch → per-record bytes) takes 15–40 min with the same agent.
- The Question: If two parsing paths contain vulnerabilities of equivalent severity and call depth, will automated agents find them at similar rates, or does input format structure create an asymmetric find-time gap that has nothing to do with the vulnerability itself?
- Core idea: Automated agents craft inputs by modifying format bytes. Checksum/CRC gates reject malformed inputs before the vulnerable parser runs—the agent must produce a structurally valid file, then corrupt a semantic field inside it. Multi-layer container formats require reverse-engineering each layer (container header, slice, codec, record) before getting a byte to the vulnerable code. Flat struct-packed formats are directly craftable: modify one field, run the binary. Format structure complexity is a moat that scales find time independently of vulnerability depth or severity.
- Visual object: Two format path diagrams side by side. Left: WAV smpl chunk—four flat labeled fields, a direct red corruption arrow pointing to the heap-OOB site, "5.6 min" label. Right: FLAC frame—CRC gate (red barrier), bitstream decoder layer, then the vulnerable allocation; "70 min" label. Identical vulnerability icons at the end of each path; the only difference is what's between the input bytes and the bug.
- Manim move: compare
- Example seed: Library with two parsers: format A (flat length-prefixed records, no checksum) and format B (binary frames with CRC32 trailer). Both have heap OOB bugs at the same call depth. Agent on A: modifies the length field directly, crashes binary in 8 min. Agent on B: first 25 crafted inputs rejected by CRC check before reaching the parser; agent must learn to recompute CRC over the modified payload before the vulnerable code runs; find lands in 55 min. Same vulnerability class, same agent budget, 7× find-time difference from format structure alone. *Illustrative*.
- Length band: ~2 min
- Still lanes: c2v
- Prerequisites: heap buffer overflow, binary file formats, CRC/checksum basics
- Exclusions: specific FLAC CRC polynomial internals; why checksums exist for integrity; agent prompting strategies for learning new formats; DoS-vs-corruption triage (Candidate 4)
- Score: 8/10

---

## Candidate 07 — Source crosses the air gap at build time, not at run time

- Source: `harness/README.md`, `targets/drlibs/README.md`
- Topic: Container image as a temporal isolation handoff artifact
- Hook: Agents need to read the vulnerable source code. The source lives on GitHub. Agents are not allowed to touch the internet. This sounds like a contradiction—but the solution is not a filter or a proxy. It is a time split.
- Key case: `dr_wav.h` and `dr_flac.h` are not checked into the repository. `setup_sandbox.sh` runs `docker build`, which fetches both headers from GitHub at a pinned commit using outbound HTTPS—during the build phase. The resulting image contains the source at `/work/dr_wav.h` on the container filesystem. When find agents run inside gVisor, egress is restricted to `api.anthropic.com:443`. Agents `cat` the source from disk, craft inputs, and run the ASAN binary. No network request for source is possible or needed; it was frozen into the image before isolation began.
- The Question: If you want agents to read third-party vulnerable source code but deny them all internet access during the attack, where does the source live, and what prevents the isolation boundary from being violated?
- Core idea: The container image is the carrier. Build phase runs with network access: `docker build` fetches source from GitHub at a pinned commit, compiles it with ASAN, and freezes both source and binary into the image layer. Attack phase runs without network access: agents start inside gVisor with egress locked to the Claude API. The source is already on the filesystem; no network request is needed. The isolation is not a filter (blocking certain hosts) but a temporal separation—network access ends before agents start, so there is nothing to filter. The image is the designed handoff artifact that moves source across the boundary.
- Visual object: A horizontal timeline split into two colored zones. Left zone "Setup" (network-open): a `docker build` arrow reaches out to GitHub, source enters the image. Right zone "Attack" (gVisor sandbox): one narrow egress arrow to `api.anthropic.com`, all other egress crossed out; source reads happen from the container filesystem. The container image sits on the boundary between zones as the carrier.
- Manim move: split
- Example seed: Researcher wants agents to audit a CVE-vulnerable C library without agents having internet access. `Dockerfile` runs `wget https://github.com/vendor/lib/commit.tar.gz` during build; source lands at `/work/lib.c`. Image is built locally. Agent container starts under gVisor with `--network=none` except `api.anthropic.com`. Agent issues `Read /work/lib.c`—reads from disk. Agent crafts malformed input bytes, runs `/work/entry testcase.bin`, triggers ASAN abort. Agent never resolves a DNS name beyond the Claude API. The source crossed the air gap 20 minutes earlier, at build time. *Illustrative*.
- Length band: ~2 min
- Still lanes: c2v
- Prerequisites: Docker image layers, gVisor isolation, network egress controls
- Exclusions: gVisor syscall filtering internals; egress allowlist YAML configuration; why agents need to read source at all (covered by Candidate 5); ASAN compilation flags
- Score: 7/10
