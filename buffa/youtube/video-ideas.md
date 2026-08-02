# buffa Video Ideas

## Candidate 1 — An over-protective Rust bound blocked the code it meant to guard

- Source: `docs/investigations/e0477-owned-view-send/README.md`
- Topic: Defensive trait bounds that can't protect unconstructible types
- Hook: A manual `Send` impl used `V: 'static` to block `OwnedView<FooView<'short>>`, but this type is unconstructible by design, and the bound breaks legitimate async code
- Key case: Writing `async fn say(req: OwnedView<SayRequestView>)` in a service trait hits E0477 "does not fulfill the required lifetime," even though the rejected type can never be constructed
- The Question: If the guarded-against type is unconstructible (all constructors gate on `V: MessageView<'static>`), why does adding a `'static` bound exist — and why does removing it permit the async code that was blocked?
- Core idea: The `'static` bound was defensive against a pattern that the type system already makes impossible. Removing it allows auto-trait derivation; the prevented-against value can't exist anyway.
- Visual object: Type signature transformation showing manual impl with `V: 'static` constraint → auto-trait `Send` derivation without the bound
- Manim move: morph
- Example seed: Six cross-boundary patterns (borrow across await, helper fns by value/ref, generic helpers, nested impls) all fail with manual bound, all pass with auto-traits
- Length band: 3–5 min
- Still lanes: c2v with compiler error messages, trait impl syntax
- Prerequisites: Rust trait bounds, Send/Sync, async fn in traits
- Exclusions: Compiler internals; return-type-notation detours; broader E0477 surface area beyond trait bounds
- Score: 9/10

## Candidate 2 — Caching avoids the exponential traversal that size calculation requires

- Source: `README.md`, `buffa/README.md`, `benchmarks/charts/README.md` (methodology notes)
- Topic: How cached encoded sizes prevent re-traversal during nested message encoding
- Hook: Computing a message's encoded size requires traversing the whole tree, and if you encode nested messages, you traverse multiple times — quadratic work hidden in linear-looking code
- Key case: A message with five nesting levels and `repeated` fields forces the encoder to walk the tree once per parent to know the header size; each level doubles the traversals
- The Question: Both the size-calculation and encode phases must traverse the tree; what prevents you from calculating size once and amortizing it across all parents that need it?
- Core idea: A dedicated size-caching pass walks the tree once and annotates each node with its encoded size, then the encode phase consumes the cache in a single linear traversal
- Visual object: Message tree diagram accumulating size annotations as a first pass, then encode phase following the cached sizes
- Manim move: accumulate
- Example seed: Illustrative nested+repeated message: `{ repeated { nested { nested { int_field } } } }` showing O(n²) traversals without cache collapsing to O(n) with cache
- Length band: 2–3 min
- Still lanes: c2v with tree structure and pseudo-code
- Prerequisites: Message serialization, protobuf varint encoding, recursion
- Exclusions: Low-level codec details; alternative approaches like arena allocation or capacity hinting
- Score: 8/10

## Candidate 3 — Code placement in memory determines cache behavior independent of the source

- Source: `benchmarks/charts/README.md`, `benchmarks/history/README.md`
- Topic: CPU cache line effects reveal that binary layout is a performance lever
- Hook: Identical source code produces 10–20% performance variance between builds with different codegen-unit counts because function placement in memory changes, moving a hot loop relative to CPU cache boundaries
- Key case: A JSON serialization benchmark shifts ±12% when split into 16 codegen units vs 1 unit; a loop that lands at offset 0 within a 64-byte DSB boundary runs fast, but straddling it forces µop-cache misses
- The Question: Why does partitioning the generated binary into more codegen units slow down a benchmark when the source code and compiler flags are identical — and how do alignment flags stabilize it?
- Core idea: Codegen units cause a function-placement lottery. Adding block and loop alignment flags forces the hot loop to land on cache-friendly boundaries, collapsing variance from ±12% to ±2%.
- Visual object: Binary memory layout before/after alignment, showing loop placement relative to 64-byte DSB cache lines; variance measurement bands narrowing
- Manim move: collapse
- Example seed: Illustrative loop: 32 bytes long, lands at byte offset 32 (straddles DSB boundary, slower) vs offset 0 (cache-aligned, faster) — same loop, 10% throughput swing
- Length band: 3–5 min
- Still lanes: geo with memory layout and cache boundaries; raster with variance graphs
- Prerequisites: CPU caches, codegen-units, basic performance measurement
- Exclusions: BOLT and PGO; full CPU microarchitecture; thermal and frequency variance (separate problem)
- Score: 8/10

## Candidate 4 — Newtypes bridge the orphan rule, enabling pluggable storage per field category

- Source: `examples/custom-types/README.md`, `examples/buffa-smolstr/README.md`
- Topic: How thin wrappers in your crate let you substitute allocation-optimized types into generated schema
- Hook: You want generated fields to use `flexstr::SharedStr` or `smallvec::SmallVec` instead of `String`/`Vec`, but the orphan rule forbids impl'ing buffa's trait on a foreign type from a crate you don't own
- Key case: Replacing all `Vec<T>` fields with `SmallVec<T, [T; 4]>` for stack allocation; neither buffa nor smallvec owns the other, so you can't impl the bridge directly
- The Question: The orphan rule says "crate A can't impl crate B's trait on crate C's type" when A doesn't own B or C. If you own none of {buffa, smallvec, your codebase}, how do you wire them?
- Core idea: A `#[repr(transparent)]` newtype in your crate wraps the foreign type, letting you impl buffa's trait on the wrapper. Trait derives auto-generate the forwarding impl; compile-time guards verify the wrapper stays zero-cost.
- Visual object: Five independent configuration knobs (string, bytes, repeated, map, box) each substituting a custom type from default → specialized
- Manim move: rotate
- Example seed: Record struct with all five knobs wired—`id: FlexStr, payload: SmallBytes, samples: SmallVec<i64>, tags: SmallVec<FlexStr>, attributes: IndexMap<i64, FlexStr>`—verified at compile time
- Length band: 2–3 min
- Still lanes: c2v with newtype wrapper pattern and trait impl; raster with build.rs configuration
- Prerequisites: Rust orphan rule, newtype pattern, #[repr(transparent)], trait derive macros
- Exclusions: Memory layout of small-vector internal structure; serde derive complexity table; other allocation strategies
- Score: 7/10

## Candidate 5 — Owned buffer + borrowed view pair enables zero-copy in async contexts

- Source: `README.md` (OwnedView description), `docs/guide.md` (usage patterns)
- Topic: Pairing zero-copy views with owned buffer to get 'static semantics for async
- Hook: A zero-copy view borrows from a buffer, tying its lifetime to the buffer; passing this view to an async fn requires the view to be `'static`, but a borrowed view can't be
- Key case: Decoding returns `MyMessageView<'a>` with reference lifetime to the backing bytes; calling `async fn process(req: MyMessageView)` fails because the lifetime doesn't satisfy `Send + 'static`
- The Question: If views are genuinely zero-copy (transparent pointers into the wire data), why can't you pass them directly to async functions — and what two-component structure solves it?
- Core idea: `OwnedView<V>` wraps a view together with its `Bytes` buffer; the owned buffer is `'static` and `Send`, so the bundle is too, and `Deref` transparently reaches view fields
- Visual object: View type unwrapping or deref chain to show owned Bytes buffer beneath, keeping it alive while view pointers are used
- Manim move: unwrap
- Example seed: Async service method `async fn process(req: OwnedView<MyMessageView<'static>>)` — caller constructs from owned bytes, passes to async fn across multiple awaits
- Length band: 2–3 min
- Still lanes: c2v with type nesting and Deref trait; raster with async fn signature
- Prerequisites: Rust lifetimes, zero-copy patterns, Send/Sync trait bounds, async
- Exclusions: E0477 compiler bug history; broader async Rust theory; MessageField and other container types
- Score: 7/10

## Candidate 06 — Back-to-front arena encoding accumulates three copies of every byte

- Source: `benchmarks/charts/README.md`
- Topic: How upb's encode-backward-then-copy strategy multiplies memory traffic
- Hook: upb encodes protobuf fields in reverse order into a growing arena and then copies the result forward into a `Vec` — so a large `bytes` field is written three times before reaching the caller, and ~55–60% of encode self-time is just moving bytes around
- Key case: MediaFrame encode benchmark: `perf` shows 55–60% of self-time in `memcpy`/`memmove` plus arena alloc/free, producing roughly three times the memory traffic of buffa's single pre-sized forward write
- The Question: Both encoders produce identical wire bytes on identical input; why does back-to-front arena encoding consume three times the memory bandwidth of forward in-place encoding — before any encoding logic differs?
- Core idea: Back-to-front encoding cannot pre-size the output before the first byte is written. The arena starts small; each overflow `memmove`s all already-written bytes forward into a doubled block; the final arena slice is then boundary-copied into a Rust-owned `Vec`. Pre-computing encoded size (buffa's cached-size pass from Candidate 2) eliminates every redundant copy: one `Vec::with_capacity` and one forward write
- Visual object: Arena growing in stages — bytes shifting right on each doubling — versus a single pre-sized buffer filled left-to-right in one pass
- Manim move: accumulate
- Example seed: Illustrative 100-byte payload: upb starts with a 64-byte arena block → writes 64 bytes → memmove 64 bytes into 128-byte block → writes remaining 36 bytes → copies 100-byte arena slice into `Vec`. Bytes moved: 64 + 64 + 36 + 100 = 264. Buffa: size-cache says 107 → allocate 107 → write 107. Total: 107.
- Length band: 2–3 min
- Still lanes: geo with arena block layout and shift arrows; c2v with `Vec::with_capacity` and encode call; raster with `perf` self-time breakdown
- Prerequisites: Memory allocation, `Vec` growth, protobuf varint encoding basics
- Exclusions: upb mini-table dispatch overhead (separate architectural cost covered by table-driven vs monomorphized encoder distinction); FFI boundary design choices; BOLT/PGO; buffa's own size-caching mechanism (Candidate 2)
- Score: 9/10
