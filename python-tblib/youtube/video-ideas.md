# Python Tblib Video Ideas

## Candidate 1 — Installation timing creates three different pickling coverage patterns
- Source: `README.rst`
- Topic: Exception definition vs. pickling support lifecycle
- Hook: Where you call `pickling_support.install()` determines which exceptions actually get pickled—same code can work or fail depending on order.
- Key case: Define a custom exception, call `install()`, then try to pickle the exception; doesn't work. Call `install()` first, define the exception after; now it works. Why?
- The Question: X (install-time) should predict Y (whether CustomException pickles); three different orderings exist with different outcomes; what's the dependency?
- Core idea: The monkey-patching mechanism walks already-defined exception classes at install time; classes born after install need a decorator or instance-time patching.
- Visual object: Timeline with three colored tracks (import, install, definition, usage) showing which orderings produce pickling vs. failure.
- Manim move: compare
- Example seed: Define custom `NetworkError(Exception)`, call `pickling_support.install()` later, pickle an instance—fails. Reverse the order—works.
- Length band: 3–5 min
- Still lanes: geo, c2v
- Prerequisites: exception inheritance, decorators, module import order
- Exclusions: the internals of the monkey-patching mechanism; security of unpickling untrusted data
- Score: 9/10

## Candidate 2 — Serialization makes tracebacks travel across process boundaries unchanged
- Source: `README.rst`
- Topic: Cross-process exception propagation
- Hook: Tracebacks are tied to the process where the error occurred; normally you can't send them to another process. tblib makes them commute.
- Key case: Worker process crashes with a traceback 12 frames deep. Parent process (multiprocessing, Celery, billiard) needs to see that exact traceback locally.
- The Question: X (exception + full traceback from worker) should transfer to parent unchanged; pickling should preserve it; how does a non-picklable object become picklable?
- Core idea: Monkey-patch the pickle protocol for traceback objects, encoding their frame data (code, line number, locals snapshot) into serializable form.
- Visual object: Two process boxes with an exception object and its traceback being serialized to bytes, crossing the process boundary, and deserializing on the other side.
- Manim move: split
- Example seed: Worker at `main.py:42` in function `fetch()` raises ValueError. Parent pickle-loads the bytes and can re-raise the same traceback.
- Length band: 2–3 min
- Still lanes: c2v, geo
- Prerequisites: pickle basics, multiprocessing or distributed task concepts
- Exclusions: security implications of unpickling untrusted objects; specific application frameworks (Celery, etc.)
- Score: 8/10

## Candidate 3 — Exception chains encode causality so `raise ... from ...` survives serialization
- Source: `README.rst`, `CHANGELOG.rst` (1.6.0)
- Topic: Chained exception preservation across process serialization
- Hook: When you `raise NewError from old_error`, Python links them; normally pickling loses this causal chain.
- Key case: Worker catches `ZeroDivisionError`, wraps it in a timeout exception, pickles and sends to parent. Parent unpickles and sees only the timeout, losing context.
- The Question: X (exception with `__cause__`) should pickle with the full chain intact; what data structure or code walk preserves the linked list?
- Core idea: Walk the `__cause__` chain at pickle time, recursively serializing each exception, then reconstruct the links at unpickle time.
- Visual object: Linked list of exception nodes, each with a `__cause__` pointer, accumulating as the walk traverses them.
- Manim move: accumulate
- Example seed: `ZeroDivisionError("div by 0")` → wrapped as `TimeoutError("query took too long") from original` → pickle → unpickle → both exceptions visible in chain.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: exception handling, `raise ... from ...` syntax, exception attributes
- Exclusions: exception groups (Python 3.11+); context suppression (`raise ... from None`)
- Score: 7/10

## Candidate 4 — Traceback reconstruction builds executable tracebacks from their string representation
- Source: `README.rst` (Traceback.from_string), `CHANGELOG.rst` (1.3.0)
- Topic: Parsing formatted tracebacks back into objects
- Hook: A traceback printed to a log or file is human-readable text; normally you can't turn it back into an object you can raise. `Traceback.from_string` does.
- Key case: Post-mortem debugging: retrieve error text from a log file (`File 'database.py' line 128 in query...`), reconstruct that traceback locally, re-raise it to debug.
- The Question: X (string representation of traceback) should become Y (executable traceback object); parsers normally can't recreate runtime objects; what's the trick?
- Core idea: Parse the formatted string to extract filenames, line numbers, function names, then construct Frame and Code objects that encode that location.
- Visual object: Formatted traceback text (with indentation, filenames, line numbers) morphing into a tree of frame/code objects.
- Manim move: morph
- Example seed: Log text `"File 'app.py' line 52 in process\n  result = db.query()"` → becomes traceback object pointing to that exact line.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: traceback format (file:line:function), frame and code objects
- Exclusions: whether source code files must exist; bytecode vs. source matching
- Score: 7/10

## Candidate 5 — Dict serialization strips tracebacks to a portable structure any language can read
- Source: `README.rst` (to_dict / from_dict)
- Topic: Language-agnostic exception serialization
- Hook: Pickling is Python-only; if you want a Go or Rust service to read your traceback, serialize to a dict instead.
- Key case: Python service raises an error, logs it as JSON, Go logging aggregator parses it and sends it to Slack with full context.
- The Question: X (traceback object with frame tree) should transform to Y (JSON-compatible dict); what information survives, and what's lost in exchange for portability?
- Core idea: Walk the traceback frame-by-frame, extract only JSON-serializable attributes (filename, line number, function name), and accumulate into nested dict/list.
- Visual object: Traceback tree being flattened and accumulated into a `{'frames': [{'file': ..., 'line': ..., 'name': ...}, ...]}` structure.
- Manim move: accumulate
- Example seed: Traceback with 3 frames → dict with `frames` list of 3 entries, each a dict with file, line, function name, local variables stripped.
- Length band: ~1 min
- Still lanes: c2v, raster
- Prerequisites: dict and list structures, JSON format
- Exclusions: which local variables are stripped and why; performance cost of walking frames
- Score: 7/10

Looking at the corpus for concepts not covered by the existing five candidates. The README's "local stack" section demonstrates a behavior none of the existing cards address: re-raising a deserialized traceback inside a new call stack causes Python to stitch the two frame chains into one continuous traceback. That's a distinct motion concept worth capturing.

# Python Tblib Video Ideas

## Candidate 06 — Re-raising a remote traceback in a new stack stitches two frame chains into one
- Source: `README.rst`
- Topic: Traceback frame-chain accumulation across process-boundary re-raise
- Hook: When you re-raise a deserialized remote traceback inside a local call stack, you don't get two separate tracebacks — Python appends your local frames to the remote chain to form one continuous trace.
- Key case: Worker crashes with frames `inner_0 → inner_1 → inner_2` (3 frames). Parent process re-raises that traceback inside `local_0`, called from `local_1`, called from `local_2`. Final printed traceback shows all six frames in a single unbroken chain.
- The Question: X (re-raise of remote traceback inside a new local stack) should produce Y (only the remote frames, or two separate outputs); instead it produces one merged chain; why does Python keep growing a traceback that originated elsewhere?
- Core idea: Python builds a traceback as a singly-linked list of frame nodes (each `tb_next` points inward); re-raising with an existing traceback sets that chain as the starting tail, then each new outer frame prepends itself as the new head — the remote frames are not replaced, they become the end of the chain.
- Visual object: Two separate frame-node chains (remote: 3 nodes; local: 3 nodes) being linked head-to-tail into one six-node linked list, then rendered as a single "Traceback (most recent call last)" block.
- Manim move: accumulate
- Example seed: Remote chain: `inner_0(line 2) → inner_1(line 2) → inner_2(line 2)`. Local re-raise in `local_0 → local_1 → local_2`. Output: six labeled frame nodes joined in order, exception printed once at the end.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: linked list structure, Python traceback object (`tb_next`), re-raising with three-argument `raise`
- Exclusions: the pickling mechanism that transported the remote traceback (covered in Candidate 2); exception chaining via `raise ... from ...` (covered in Candidate 3); `six.reraise` internals
- Score: 7/10
