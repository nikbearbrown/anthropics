# CCC — Claude's C Compiler Video Ideas

## Candidate 1 — Why does one type system die before codegen, but backends get different one?
- Source: `src/common/README.md`
- Topic: Dual-type IR translation
- Hook: CType preserves every C semantic distinction (long vs. long long stay separate), but the backend can only work with flat, machine-level types; the bridge is a one-way transformation that's irreversible.
- Key case: A struct field declared `long` and another `long long`; they're distinct types for type-checking but collapse to the same 64-bit integer at the IR level on LP64 targets.
- The Question: Why can't the C parser emit IrType directly, and why does the lowering phase need to read CType information if it's going to throw most of it away anyway?
- Core idea: CType is semantic and architecture-independent (27 variants preserve C-level distinctions); IrType is flat and target-specific (14 variants collapse to machine primitives). Lowering computes ABI classification once, then IrType is sufficient for all downstream passes.
- Visual object: Two parallel type tables, left showing CType `Int` / `Long` / `LongLong` as separate variants, right showing all three becoming `I64`; arrows flowing left-to-right through lowering.
- Manim move: morph
- Example seed: `struct point { long x; long long y; int flags; }` — fields are semantically distinct in type-checking, but lowering flattens to `[I64, I64, I32]` in IR, collapsing the long/long-long distinction.
- Length band: 2–3 min
- Still lanes: c2v, geo
- Prerequisites: compiler pipeline phases, type theory basics
- Exclusions: detailed ABI rules, struct layout bitfield handling, floating-point precision differences
- Score: 9/10

## Candidate 2 — How does assembly shrink from 13 sequential filters, not 1?
- Source: `src/backend/README.md`
- Topic: Multi-stage peephole optimization
- Hook: The backend generates raw assembly, then runs 13 separate peephole passes (8 local + 1 global + 4 cleanup) before emitting machine code; each pass finds patterns the previous one made invisible.
- Key case: A dead register-move `mov %eax, %ebx; mov %ebx, %eax` is eliminated only after pass 7 (dead-store elimination) removes a store that earlier made the move appear live.
- The Question: Why is the same peephole pattern not caught in a single pass? What does pass N produce that enables pass N+1 to see a pattern it couldn't before?
- Core idea: Peephole passes form an iterative dependency chain — local passes find simple patterns, global pass fuses across blocks, cleanup passes handle tail-call optimization and frame-pointer elimination that earlier passes enable.
- Visual object: A sequence of assembly code boxes, each downstream box smaller and simpler than the one before, with labeled annotations showing which pass eliminated which instruction type.
- Manim move: filter
- Example seed: `(void) x; mov %rax, %rbx; call foo; mov %rbx, %rax;` → pass 1 sees move as live, pass 5 (call-result dead-code) kills the call's side effects, pass 7 (dead-move) kills the register moves because result unused.
- Length band: 2–3 min
- Still lanes: raster, c2v
- Prerequisites: machine assembly syntax (x86 is fine), control flow graph intuition
- Exclusions: specific x86 instruction encodings, register allocation details, full list of 13 pass names
- Score: 9/10

## Candidate 3 — What makes a stack slot reusable only in one block but not across blocks?
- Source: `src/backend/stack_layout/` (structured as `mod.rs`, `analysis.rs`, `alloca_coalescing.rs`, `copy_coalescing.rs`, `slot_assignment.rs`)
- Topic: Three-tier stack slot allocation
- Hook: Stack frame layout is not one big pool; it's split into three semantic zones (parameter slots, escaping-alloca slots, block-local temporaries), and only zone 3 can reuse space because zones 1–2 have longer lifetimes.
- Key case: A 1MB temporary array allocated inside a loop's single iteration can't reuse the same stack address across loop iterations using naive allocation, but escape analysis + per-block reuse allows it.
- The Question: Why doesn't the compiler allocate all stack slots in one pass, and why do block-local temporaries get their own tier when they could theoretically share the escaping-alloca zone?
- Core idea: Tier 1 (parameters/return, fixed by ABI) → Tier 2 (allocas that escape scope, liveness-packed) → Tier 3 (temporaries live only within a block, reused per-block). Each tier has different lifetime semantics.
- Visual object: A stack frame diagram with three colored horizontal bands; annotation showing which temporaries live in each; gray hatching showing space reused in zone 3 across multiple loop iterations.
- Manim move: accumulate
- Example seed: Function with `int tmp[256]` allocated in a single-block scope inside a loop; tier 3 reuses same stack address each iteration instead of allocating 256 bytes × 100 iterations = 25KB.
- Length band: 2–3 min
- Still lanes: geo, raster
- Prerequisites: stack frames, function scope, basic escape analysis intuition
- Exclusions: liveness computation algorithm details, register allocation interaction, calling convention details
- Score: 8/10

## Candidate 4 — When does one optimization pass set up the next pass to succeed?
- Source: `src/passes/` (compiler design notes mention 15 passes + shared loop analysis)
- Topic: Optimization pass ordering and enabling chains
- Hook: Running all 15 optimization passes once isn't enough — passes interact, each one creating opportunities for the next; the order is not arbitrary.
- Key case: A loop that first needs loop-invariant-code-motion to hoist `10 + 20` outside, then constant-fold to simplify `10 + 20` → `30`, then dead-code elimination if the constant is unused.
- The Question: If you run all passes once, why don't you hit a fixed point? Can you predict when to stop, or do you need to detect convergence?
- Core idea: Pass ordering forms a dependency DAG where each pass may enable (or disable) subsequent passes; dead-code removal enables constant-folding; constant-folding enables more dead-code removal.
- Visual object: A directed graph of pass boxes (15 nodes) with edges showing "enables" relationships, plus a timeline showing a loop's IR shrinking through successive pass iterations.
- Manim move: spread
- Example seed: Expression `for (i=0; i<100; i++) sum += (5 + 0);` → LICM hoists `5+0` outside loop → const-fold simplifies to `5` → dead-code kills if `sum` unused.
- Length band: 1–2 min
- Still lanes: geo
- Prerequisites: loop optimization, dataflow analysis basics, IR instruction structure
- Exclusions: full pseudocode of any single pass, fixed-point convergence proofs, iterative-analysis algorithms
- Score: 6/10

## Candidate 05 — Why the same IR comparison emits four assembly lines or two depending on what comes next?
- Source: `src/backend/README.md`
- Topic: Pre-scan use-count analysis enabling cmp-branch fusion
- Hook: The optimal machine encoding for an IR comparison depends on whether its result feeds a branch or a general use — information the code generator structurally lacks at the moment it processes the compare.
- Key case: `if (x > 0) foo();` — the IR compare produces a boolean. Without lookahead, codegen emits `cmp; setg; testb; jne` (4 instructions). With a pre-scan use-count map recording that the compare feeds exactly one branch: `cmp; jg` (2 instructions).
- The Question: IR should predict optimal assembly; this compare did not emit optimal code without a forward scan. Why can a one-instruction-at-a-time code generator fail to find the best encoding even for a single, simple comparison?
- Core idea: x86 conditional branches consume CPU flags directly — no boolean register is needed. A compare whose result is consumed by exactly one branch can suppress `setcc` + `test`; the branch absorbs the flags. The pre-scan runs one forward pass first, recording each IR value's use count and consumer type. When the compare is later processed, it queries the map: "sole consumer = branch?" If yes, it emits nothing; the branch instruction handles the flag test itself.
- Visual object: Two side-by-side assembly listings for `if (x > 0)` — left: 4-instruction naive sequence; right: 2-instruction fused sequence — with a highlighted use-count map entry (count=1, consumer=branch) as the bridge between columns.
- Manim move: collapse
- Example seed: `int x = 5; if (x > 0) return 1; return 0;` — naive: `mov $5,%eax; cmp $0,%eax; setg %cl; testb %cl,%cl; jne .ret1`. Pre-scan fused: `mov $5,%eax; cmp $0,%eax; jg .ret1`. (illustrative)
- Length band: 2–3 min
- Still lanes: raster, c2v
- Prerequisites: x86 FLAGS register, conditional branch instructions, IR instruction model
- Exclusions: GEP address-mode folding, GlobalAddr folding, full pre-scan pass structure, register allocation interaction with fusion
- Score: 8/10
