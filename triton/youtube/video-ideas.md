# Triton Video Ideas

## Candidate 1 — Why block-level parallelism unlocks automatic compiler optimizations
- Source: `docs/programming-guide/chapter-1/introduction.rst`
- Topic: Block-level iteration representation and compiler visibility
- Hook: Moving parallelism from thread-level (millions of serial tasks) to block-level (hundreds of vector tasks) flips what the compiler can see statically.
- Key case: Matrix multiply: CUDA threads each compute 1 scalar, requiring the compiler to infer tiling and coalescing; Triton programs each compute a 128×128 block, making the iteration structure visible.
- The Question: When parallelism is defined over blocks instead of threads, why can the compiler automatically optimize memory coalescing, prefetching, thread swizzling, and tensor-core dispatch without either programmer hints or expensive polyhedral analysis?
- Core idea: Block-level iteration structure is a statically-analyzable intermediate form. Data-flow analysis on the block-iteration graph reveals memory access patterns and reuse; this enables automatic scheduling of locality and parallelism optimizations that would be invisible at the thread level.
- Visual object: Side-by-side loop pyramids: CUDA shows deep trees of scalar operations with implicit parallelism; Triton shows shallow trees of block iterations with explicit vector operations.
- Manim move: split
- Example seed: 4096×4096 matmul. CUDA: 256 threads each iterate 16,384 times computing one element per iteration. Triton: 8 programs, each iterating 64 times to compute a 128×128 block per iteration.
- Length band: 3–5 min
- Still lanes: c2v, raster
- Prerequisites: Basic GPU parallelism (blocks, threads, warps), memory coalescing concept
- Exclusions: Polyhedral compilation details, tensor-core ISA specifics, register allocation strategies
- Score: 9/10

## Candidate 2 — Why hardware tensor operations create unexpected performance asymmetries
- Source: `docs/meetups/10-25-2023/notes.md`
- Topic: Layout mismatches between hardware operations and downstream consumers
- Hook: Flash Attention on H100 runs forward at 450 TFLOPS but backward at 250 TFLOPS—the 2× asymmetry reveals a hidden cost.
- Key case: WGMMA (wide matrix multiply-accumulate) produces output in a specific layout optimized for the operation itself, not for what comes next in the computation graph.
- The Question: When new hardware operations (like WGMMA) enable fused kernels, why do datatype format mismatches between the operation output and downstream gradient computation create a bottleneck, and how does the iteration structure of Triton IR expose where to inject layout conversions?
- Core idea: Hardware tensor operations output data in fixed layouts optimized for throughput, not compatibility. Layout mismatches between operation output and downstream consumers force expensive transpositions. Triton IR can schedule format conversions as separate passes in the iteration space, amortizing cost.
- Visual object: Timeline showing forward-pass WGMMA throughput (450 TFLOPS), then a "conversion barrier" drop, then backward-pass throughput at 250 TFLOPS.
- Manim move: morph
- Example seed: Flash Attention on H100: forward pass uses WGMMA in native column-major FP8 layout (450 TFLOPS); backward pass needs row-major FP8, requiring format conversion that reduces effective throughput to 250 TFLOPS.
- Length band: 2–3 min
- Still lanes: raster (TFLOPS timeline), c2v (FP8 format declarations)
- Prerequisites: Flash Attention overview, what tensor cores do, TFLOPS as throughput metric
- Exclusions: WGMMA instruction encoding, full linear algebra of backpropagation, numerical precision analysis of FP8
- Score: 8/10

## Candidate 3 — Why block-level analysis enables automatic memory optimization
- Source: `docs/programming-guide/chapter-1/introduction.rst`
- Topic: Data-flow analysis on block iterations reveals optimization opportunities
- Hook: A simple Triton loop written like NumPy automatically becomes coalesced, prefetched, tensor-core-routed machine code—without explicit programmer directives.
- Key case: Matmul kernel with block iteration and no optimization hints produces code rivaling hand-tuned CUDA.
- The Question: What information becomes accessible when iteration is structured at the block level that allows automatic inference of memory optimizations (coalescing, prefetching, thread swizzling) at lower computational cost than full polyhedral analysis?
- Core idea: Block-level iteration has static, affine structure. Data-flow analysis on the block-iteration graph (which blocks access which memory ranges, which blocks share data) is cheaper than full polyhedral machinery but sufficient to discover locality opportunities and schedule optimizations automatically.
- Visual object: Dependency graph of iteration blocks with arrows labeled by memory access patterns; subgraphs highlighted to show discovered optimizations (coalescing within rows, prefetch edges between blocks).
- Manim move: accumulate
- Example seed: 2D grid of 8×8 iteration blocks, each accessing a stripe of a 1024-element array. Compiler analysis discovers that blocks in row i access contiguous elements [1024*i, 1024*(i+1)), enabling coalescing.
- Length band: 2–3 min
- Still lanes: raster (iteration graph with annotations), c2v (before-and-after kernel code)
- Prerequisites: Memory coalescing concept, why compilers need to infer it for performance
- Exclusions: Polyhedral mathematics, affine-loop theory, LLVM lowering details
- Score: 7/10

## Candidate 4 — Why narrower datatypes enable superlinear throughput gains
- Source: `docs/meetups/08-22-2023/notes.md`
- Topic: Datatype size as a determinant of arithmetic throughput ceiling
- Hook: H100 FP8 matmuls hit 1.2 petaflops, but FP16 caps at 670 teraflops on the same hardware—the 2× gap suggests the hardware's throughput isn't the bottleneck.
- Key case: Same tensor core throughput (operations per cycle), half the datatype size → double the arithmetic operations per unit memory.
- The Question: When GPU hardware supports narrow-datatype (FP8) operations with the same throughput as wider datatypes (FP16), why does arithmetic throughput scale superlinearly, and what constraint prevents always using the narrowest datatype?
- Core idea: Arithmetic throughput is bounded by memory bandwidth divided by bytes-per-operation. Narrowing the datatype (FP8 vs. FP16) halves bytes-per-element while keeping tensor-core throughput constant, effectively doubling arithmetic throughput. The constraint is numeric precision: FP8 has lower dynamic range and resolution, breaking downstream layers.
- Visual object: Stacked or scaling bar chart showing TFLOPS vs. datatype bit-width, with FP16 at 670, FP8 at 1200, and an annotation showing the precision loss tradeoff.
- Manim move: accumulate
- Example seed: Dense C = A @ B matmul. A, B ∈ FP16 → 670 TFLOPS. A, B ∈ FP8 → 1200 TFLOPS. Downstream layers or gradients require FP16 precision, so FP8 is confined to inference.
- Length band: ~1 min
- Still lanes: raster (TFLOPS bars with datatype labels)
- Prerequisites: Matrix-multiply operation count (O(N³)), floating-point bit-width basics
- Exclusions: Quantization-aware training, mixed-precision strategies, numerical stability analysis
- Score: 6/10

## Candidate 05 — Why polyhedral compilers collapse when GPU kernels gain one irregular branch
- Source: `docs/programming-guide/chapter-2/related-work.rst`
- Topic: Transformation space explosion as the ceiling of polyhedral GPU optimization
- Hook: Polyhedral compilation matches cuBLAS on simple dense matmul — yet GPU programmers don't use it, because every additional statement multiplies the legal-schedule search space exponentially.
- Key case: A dense matmul SCoP can be fully optimized via polyhedral tiling; adding a single non-affine conditional (e.g., a sparse mask selecting which blocks to compute) exits the SCoP entirely, collapsing optimization back to zero — not a graceful degradation.
- The Question: If polyhedral compilation is mathematically complete for loop transformations, why does one irregular conditional destroy optimization for the entire kernel rather than just that branch?
- Core idea: A SCoP is a maximal contiguous region where every loop bound and array subscript is an affine function of surrounding indices. One violation breaks the region boundary, resetting it. Even within a valid SCoP, checking each candidate schedule for legality requires solving an integer linear program; the candidate space Ω is a product over per-statement transformation lattices and grows combinatorially with statement count. Triton's block-iteration DAG replaces ILP legality checks with reachability checks: polynomial cost, no region collapse.
- Visual object: Two parallel columns — left: a schedule lattice branching exponentially as statement count grows from 3 to 10; right: a 10-node block DAG with 12 edges and a single O(n²) traversal marking legal orderings.
- Manim move: accumulate
- Example seed: 3-statement kernel (load A, multiply, store): 6 schedule orderings to check, each an ILP. 9-statement fused softmax-matmul: ~360K orderings. Adding one non-affine mask index: SCoP region resets to 0 statements. Triton block DAG: 9 nodes, 11 edges, reachability in ~50 comparisons.
- Length band: 2–3 min
- Still lanes: raster (log-scale ordering-count bar chart), c2v (SCoP constraint equations beside a Triton block-iteration graph)
- Prerequisites: What loop tiling is, what affine means for array indices
- Exclusions: Farkas' lemma and ILP solver internals, Triton's actual MLIR pass sequence, integer linear programming algorithms

- Score: 7/10
