# PySvelte Video Ideas

## Candidate 1 — How does the library know what to load without explicit imports?
- Source: `README.md`
- Topic: Automatic component discovery and build from filesystem
- Hook: "Write a Svelte file in a folder and it's instantly a Python function—no npm command, no import statement"
- Key case: Create `src/Hello.svelte`. In a Jupyter notebook, import pysvelte and call `pysvelte.Hello(name="World")` on the first try. The component exists with tab-completion, no build step was run.
- The Question: "Component objects should require explicit registration; this case skipped the import; how does the library know when files appear?"
- Core idea: On Python import, pysvelte scans the `src/` directory, triggers builds for new components, and injects them into the module namespace using dynamic attribute lookup
- Visual object: The `src/` folder as an implicit registry feeding live objects into Python's namespace
- Manim move: scan + morph
- Example seed: Empty project. Developer writes `src/Counter.svelte` exporting `let count`. Notebook does `import pysvelte; pysvelte.Counter(count=5)` and it works first try. IDE shows Counter in completions.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: module `__getattr__`, dynamic build triggering, filesystem watching
- Exclusions: webpack/npm internals, TypeScript compilation, monorepo setup
- Score: 9/10

## Candidate 2 — Why move validation to Python when the bug appears in JavaScript?
- Source: `README.md`
- Topic: Validation at the language boundary before data crosses
- Hook: "Either language can validate; but validating first in Python means catching errors as TypeError, not as a broken visualization"
- Key case: `Hello.py` contains `assert len(name) > 0` and `assert name[0] == name[0].upper()`. Calling `pysvelte.Hello(name="alice")` fails immediately at the Python cell with a clear assertion, not silently in the browser where a renderer might break or produce wrong output.
- The Question: "Validation failures are more visible in the rendering layer; why check data in Python instead?"
- Core idea: Python's type annotations, assertions, and domain knowledge let you catch errors cheaply; debugging visual artifacts in the browser is much slower
- Visual object: Two parallel files—`Hello.svelte` and `Hello.py`—with data flowing through the Python validation gate first
- Manim move: split + trace
- Example seed: Component expects histogram bins between 2 and 100. `Helper.py` has `assert 2 <= bins <= 100`. Passing `bins=0` fails at the notebook cell with a useful message, not in a rendering loop.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Python assertions, companion-file patterns, why boundary validation matters
- Exclusions: pydantic/mypy/schema libraries, detailed error-handling frameworks
- Score: 6/10

## Candidate 3 — Why recompose visualizations with += instead of making a single bigger one?
- Source: `README.md`
- Topic: Component modular composition via accumulation
- Hook: "You could hand-wire three visualizations into one mega-component; instead, the library lets you glue them together with += like you're writing a list"
- Key case: Researcher creates a blank `Html`, then `html += AttentionLayer1`, `html += AttentionLayer2`, `html += AttentionLayer3`, calls `html.publish()`. Three separate components become one shareable page without editing any component code.
- The Question: "Why allow += composition rather than requiring all visualizations be bundled into a single new component?"
- Core idea: Small reusable components stay small and single-purpose; combining them via += is cheaper than engineering a larger component for every new layout
- Visual object: The `Html` object growing through repeated += operations, each adding a visualization block
- Manim move: accumulate
- Example seed: `viz = Html("<h1>Transformer Report</h1>"); viz += Attention(layer_weights); viz += Gradient(gradients); viz += Tokens(logits); viz.publish("~~/analysis.html")` creates a three-section page without modifying any component.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: operator overloading, container objects
- Exclusions: HTML/CSS layout, Slack publishing, styling
- Score: 6/10

## Candidate 04 — The same tensor arrives in JavaScript with a different name
- Source: `README.md`
- Topic: NumPy array serialization across the Python–JavaScript boundary
- Hook: "You hand a NumPy array into a Python function and pull it back out in JavaScript with `.get()`—nothing you wrote serialized it"
- Key case: A researcher passes `attention_weights` (shape `[12, 64, 64]`, dtype float32) to `pysvelte.AttentionMulti(weights=attention_weights)`. The Svelte component receives `weights` as a SciJS NdArray and reads a value with `weights.get(head, row, col)`. No serialization code was written anywhere the researcher can see.
- The Question: "Python's ndarray and JavaScript's NdArray are unrelated types; this case passed one through without explicit conversion; what crossed the boundary and how did shape survive?"
- Core idea: pysvelte encodes the numpy array's flat data, shape, and dtype into a format embeddable in HTML/JS; the client-side SciJS NdArray is reconstructed from that payload with the same shape and indexing semantics
- Visual object: A 3-D tensor block crossing a membrane labeled "Python | JavaScript", re-emerging with identical values but a new accessor syntax
- Manim move: transform
- Example seed: `w = np.ones((2, 3, 3))`. Python: `w[0, 1, 2] == 1.0`. JS: `w.get(0, 1, 2) === 1.0`. Same number, two syntaxes, one serialization boundary in between.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: numpy array structure, basic serialization concepts, what SciJS ndarray is
- Exclusions: JSON vs binary format internals, dtype promotion edge cases, full NdArray API
- Score: 7/10

## Candidate 05 — Positional args break silently; keyword args survive component edits
- Source: `README.md`
- Topic: Keyword-only argument binding as a contract resilient to component evolution
- Hook: "Forcing callers to name every argument seems verbose; but Svelte components are edited constantly, and positional binding silently remaps when exports are reordered"
- Key case: `src/Hello.svelte` exports `name` then `color`. A caller writes `pysvelte.Hello("World", "blue")`. A colleague adds `font_size` before `name`. The positional call now silently passes `"World"` to `font_size`. A keyword caller writing `pysvelte.Hello(name="World", color="blue")` survives the identical edit unchanged.
- The Question: "Positional args are simpler to type; this library banned them; what property of Svelte components makes positional binding unstable over time?"
- Core idea: Svelte exports are edited freely and independently of their Python callers; any insertion or reorder shifts positional binding without error; keyword binding resolves by name, decoupling call sites from export order
- Visual object: A Svelte export list being reordered, with positional arrows snapping to wrong targets while keyword arrows stay fixed
- Manim move: compare
- Example seed: `pysvelte.Counter(5, True)` breaks when `show_label` is inserted before `count`; `pysvelte.Counter(count=5, show_label=True)` is unaffected by the same edit.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: Python positional vs keyword arguments, concept of Svelte component props
- Exclusions: Python `**kwargs` mechanics, full Svelte props/reactivity system, TypeScript typing of props
- Score: 7/10
