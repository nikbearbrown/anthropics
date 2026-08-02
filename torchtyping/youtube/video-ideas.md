# Please use jaxtyping instead Video Ideas

## Candidate 1 — Ellipsis expands to match variable batch depths
- Source: `FURTHER-DOCUMENTATION.md#More-Examples`
- Topic: Pattern matching for variable-depth tensor structures
- Hook: Most tensors have leading batch dimensions, but nesting depth varies—how do you type "any number of leading dims"?
- Key case: `TensorType["batch": ..., "channels"]` matches shape `(8, 3, 256)` or `(2, 4, 3, 256)` equally
- The Question: How should type annotations handle dimensions that vary in count while pinning other dimensions fixed?
- Core idea: Ellipsis (`...`) captures zero or more dimensions and binds them as a unit, letting you separate arbitrary leading batch structure from fixed trailing dimensions
- Visual object: Stacked grids of varying height (2D vs 3D batch inputs) under one `TensorType` annotation
- Manim move: spread
- Example seed: A function `process(x: TensorType["batch": ..., "channels"])` accepting both shape `(12, 64)` and shape `(4, 3, 64)` without modification
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: tensor shapes, dimension counting
- Exclusions: multiple ellipsis (advanced), str:int slicing syntax
- Score: 9/10

## Candidate 2 — Dimension name binding accumulates consistency checks
- Source: `README.md#Usage`
- Topic: Named dimensions as runtime constraints across function arguments
- Hook: You label the same logical dimension in multiple arguments; that shared name should mean "must be the same size"—but type annotations don't enforce it
- Key case: `func(x: TensorType["batch"], y: TensorType["batch"])` where calling with `rand(3), rand(1)` fails: `TypeError: Dimension 'batch' of inconsistent size. Got both 3 and 1.`
- The Question: When two arguments use the same dimension name, what enforcement mechanism ensures they actually match at runtime?
- Core idea: String names bind to observed sizes on first occurrence; every subsequent use checks consistency—creating an accumulated constraint that feeds back into validation
- Visual object: Two tensors side-by-side with dimension labels, error message showing which dimension diverged and by how much
- Manim move: compare
- Example seed: `func(rand(5), rand(5))` succeeds; swap second arg to `rand(3)` and watch the error pin the mismatch to dimension `"batch"`
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic tensor shapes, string annotations
- Exclusions: str:str aliasing (variant), str:... multi-dim binding (advanced variant)
- Score: 8/10

## Candidate 3 — Typeguard patching activates enforcement at function entry
- Source: `README.md#Usage`, `FURTHER-DOCUMENTATION.md#FAQ`
- Topic: Bridging the gap between static annotations and runtime checking
- Hook: Python ignores type hints by default; they're just syntax. How do you make annotations actually fail before the function body runs?
- Key case: Calling `patch_typeguard()` then `@typechecked` on a function—now every call is intercepted to inspect argument tensors against their annotations
- The Question: How do you retrofit enforcement onto Python's type annotations, which are normally silent?
- Core idea: `typeguard` library introspects function signatures; `torchtyping.patch()` extends it to understand `TensorType`; decorators or import hooks trigger inspection before code executes
- Visual object: Call stack frame showing argument inspection happening before function body, then error raised with mismatched shape details
- Manim move: accumulate
- Example seed: Same function called twice: once without decorator (silent fail), once with `@typechecked` (TypeError thrown at call site before any tensor operations)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Python decorators, basic type hints
- Exclusions: pytest integration flag (orthogonal), mypy/flake8 workarounds (static-checker config), import-hook internals
- Score: 7/10

## Candidate 4 — Shape documentation shifts from comments to executable code
- Source: `README.md` (introduction)
- Topic: Transforming unverified documentation into checkable specifications
- Hook: Developers write `# x has shape (batch, hidden)` to document tensors, but comments never fail when the code drifts
- Key case: README before/after: comments like `# x has shape (batch, x_channels)` become `TensorType["batch", "x_channels"]`—same intent, now verifiable
- The Question: Why embed shape information in comments when it could be code and automatically enforced?
- Core idea: Type annotations convert documentation from inert text into executable specifications; divergence between intent and reality surfaces as runtime errors, not silent bugs
- Visual object: Before/after code split-screen, with annotation text morphing from comment to type signature, then error highlighting a shape mismatch
- Manim move: morph
- Example seed: Developer changes tensor creation from `(batch, features)` to `(features, batch)` by accident; with annotations, `@typechecked` catches it immediately; with comments, the code silently breaks downstream
- Length band: 1–2 min
- Still lanes: c2v
- Prerequisites: Python type hint syntax, tensor shapes
- Exclusions: mypy limitations, flake8 false positives, syntax details (slicing)
- Score: 7/10

## Candidate 05 — Named ellipsis binds a whole dimension sequence, not just a count
- Source: `FURTHER-DOCUMENTATION.md`
- Topic: Sequence-level binding for named variable-depth dimension groups
- Hook: A named `...` group can appear in multiple arguments—but does "the same name" mean the same number of dims, or the same sizes in the same order?
- Key case: `func(x: TensorType["dim1": ..., "dim2": ...], y: TensorType["dim2": ...])` where `x` has shape `(2, 3, 4, 5)` with `dim2 = (4, 5)`—calling with `y` of shape `(4, 6)` fails because the second size differs even though the count matches
- The Question: When a named `...` spans several dimensions, what exactly is stored at first binding and what is compared on reuse?
- Core idea: The binder records the full ordered tuple of sizes matched by a named `...`; every subsequent appearance checks the entire tuple element-by-element—extending the point-binding of single-dimension names to sequence-binding
- Visual object: Two tensors with colored brackets enclosing named groups; `"dim2"` brackets must align size-for-size, not just length-for-length
- Manim move: compare
- Example seed: `x` shape `(2, 3, 4, 5)` with `dim1 = (2, 3)`, `dim2 = (4, 5)`; `y` shape `(4, 5)` passes; `y` shape `(4, 6)` fails with a mismatch on the second element of the `"dim2"` sequence
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: tensor shapes, Candidate 1 (single ellipsis), Candidate 2 (name binding)
- Exclusions: the function body logic (the `sum_dims` computation in the FAQ example), mypy slice crash workaround
- Score: 7/10

## Candidate 06 — Custom TensorDetail slots a new check into the annotation pipeline
- Source: `FURTHER-DOCUMENTATION.md`
- Topic: Extending type annotations to verify arbitrary tensor properties
- Hook: Shape and dtype are built-in checks, but tensors can carry custom metadata—how do you make the annotation system understand an invariant the library has never heard of?
- Key case: `FooDetail("good-foo")` subclasses `TensorDetail` with a `check()` method verifying `tensor.foo == "good-foo"`; passed as `TensorType[float, FooDetail("good-foo")]`, it fires at every decorated call site without touching the core library
- The Question: What is the minimum contract a new check must satisfy to be treated identically to built-in shape and dtype checks at runtime?
- Core idea: `TensorDetail` defines a three-method interface (`check`, `__repr__`, `tensor_repr`); typeguard iterates every slot in `TensorType[...]` in sequence, calling `check()` on each; satisfying the interface is the entire cost of entry
- Visual object: `TensorType[...]` bracket rendered as a row of labeled check slots—shape, dtype, then a new custom slot lighting up in sequence
- Manim move: split
- Example seed: `TensorType[float, FooDetail("good-foo")]` on a `rand(3)` tensor: shape slot passes, dtype slot passes, FooDetail slot fails and prints the mismatch using `tensor_repr`
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Python subclassing, Candidate 3 (typeguard integration)
- Exclusions: the `None: str` and `is_named` detail variants, mypy compatibility workarounds, the three-arg `check` signature internals
- Score: 6/10

## Candidate 07 — `is_named` reveals two coexisting dimension-naming systems
- Source: `FURTHER-DOCUMENTATION.md`
- Topic: Annotation string labels vs PyTorch named tensor `.names`—two systems, one flag
- Hook: String names in annotations already label dimensions—so why does a flag called `is_named` suddenly matter?
- Key case: `TensorType["a": 3, "b", is_named]` on a tensor with `.names = (None, None)` raises an error even though the shape `(3, any)` is correct; the same annotation without `is_named` would pass silently
- The Question: When you write `"a"` in an annotation, what does the system actually check—and what does it deliberately ignore unless told otherwise?
- Core idea: Without `is_named`, string labels are consistency keys for cross-argument size binding only; `is_named` activates a second, orthogonal check: the tensor's PyTorch `.names` attribute must match the annotation strings exactly—two distinct namespaces sharing the same syntax
- Visual object: Split diagram showing annotation labels on the left and tensor `.names` attribute on the right; without the flag the two columns are disconnected; the flag draws an arrow bridging them
- Manim move: trace
- Example seed: `func(x: TensorType["batch", "features", is_named])` called with `rand(4, 8).rename("batch", "features")` passes; called with `rand(4, 8)` (unnamed) fails with a names mismatch, not a shape mismatch
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: Candidate 2 (name binding), PyTorch named tensors basics
- Exclusions: `None` dimension (must-not-be-named variant), `None: str` pairs, named tensor performance overhead
- Score: 6/10
