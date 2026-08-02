# orjson Video Ideas

## Candidate 1 — Why does your `default` handler silently lose data instead of failing?
- Source: `README.md`
- Topic: The implicit-None bug in custom JSON serialization
- Hook: Your custom serializer handles Decimal but not Set; Set types become null instead of raising an error.
- Key case: A default function that explicitly handles Decimal("99.99") but encounters set({1, 2}); returns None implicitly.
- The Question: Explicit raise-on-unknown should fail loudly; this case did not; why does Python's implicit None return turn unknown types into null instead?
- Core idea: Python functions that don't explicitly return anything implicitly return None, and None becomes JSON null; the library can't distinguish "I decided to serialize this as None" from "I don't know how to handle this type" so data silently corrupts.
- Visual object: A split-screen default handler: one branch explicitly raises, the other implicitly returns None; trace which data gets lost.
- Manim move: split
- Example seed: `def default(obj): return str(obj) if isinstance(obj, Decimal) else ???` — calling it with set({1, 2}) returns None because there's no else clause, serializing as `{"value": null}` instead of erroring.
- Length band: ~2–3 min
- Still lanes: c2v
- Prerequisites: Python implicit-return semantics, JSON null
- Exclusions: general default-parameter patterns in Python, stdlib json module differences
- Score: 9/10

## Candidate 2 — How do you embed pre-serialized JSON without double-escaping?
- Source: `CHANGELOG.md`
- Topic: The Fragment wrapper for composing JSON documents
- Hook: You have JSON from another source but serializing it as a string wraps and escapes it, breaking the structure.
- Key case: Building `{"data": <another dumps() result>}` — if you pass the bytes as a string field, the quotes inside get escaped.
- The Question: String embedding should preserve JSON structure; the case did not; why does orjson.Fragment solve this?
- Core idea: Mark pre-serialized JSON bytes with Fragment so the serializer treats them as raw JSON rather than a string to escape; this lets you compose documents without string concatenation or round-tripping through the parser.
- Visual object: A JSON document with two sub-objects; one embedded as a Fragment (intact structure), one as a string (escaped quotes, broken structure).
- Manim move: compare
- Example seed: `orjson.dumps({"user": user_obj, "metadata": orjson.Fragment(metadata_json)})` embeds metadata correctly instead of escaping it as a string value.
- Length band: ~2–3 min
- Still lanes: geo, c2v
- Prerequisites: JSON escaping, string serialization
- Exclusions: composability patterns in general, JSON streaming libraries
- Score: 9/10

## Candidate 3 — Why does deeply nested JSON crash the Python interpreter instead of raising an exception?
- Source: `CHANGELOG.md`
- Topic: Recursion depth limits and parser stack safety
- Hook: A JSON file with thousands of nested objects parses fine in one implementation, crashes the interpreter in another.
- Key case: orjson added a 1024-level recursion limit in 3.9.15; before that, unbounded nesting could overflow the C stack.
- The Question: Recursion should fail gracefully with an exception; deep nesting did not; why does depth matter so much that you need a hard limit?
- Core idea: Recursive descent parsing consumes one call-stack frame per nesting level; when frames run out, the stack overflows and the entire interpreter crashes (not a catchable Python exception) — a limit prevents this by raising JSONDecodeError first.
- Visual object: A call stack diagram growing frame-by-frame with each nested `{`, then hitting a limit and halting before overflow.
- Manim move: accumulate
- Example seed: Parsing `{"a":{"b":{"c": ... }}}` nested 1025 times now raises JSONDecodeError saying "max depth exceeded" instead of segfaulting.
- Length band: ~2–3 min
- Still lanes: geo
- Prerequisites: call stacks, recursion, stack overflow
- Exclusions: general Python recursion limits, alternative parsing strategies
- Score: 8/10

## Candidate 4 — Why is string escaping 3× faster with SIMD than scalar code doing the same algorithm?
- Source: `CHANGELOG.md`
- Topic: SIMD parallelism in character-by-character scanning
- Hook: Serializing a long UTF-8 string with SIMD takes ~5µs; the same code compiled for scalar execution takes ~15µs; the algorithm is identical.
- Key case: orjson detects CPU capabilities at runtime and uses AVX-512 on amd64 machines; 3.10.16 improved AVX-512 performance further.
- The Question: Identical algorithm should have similar speed; scalar vs SIMD did not; why is parallelism so much faster here?
- Core idea: SIMD processes multiple bytes in parallel per instruction (16–64 bytes at once), while scalar code processes one byte per op; more throughput = dramatically lower latency for the same work.
- Visual object: Two execution timelines: one processor core scanning bytes one-at-a-time, another scanning 16+ bytes in a single instruction lane, both looking for quote marks and backslashes.
- Manim move: compare
- Example seed: Escaping a 512-byte string with emojis, newlines, and quotes; SIMD scans the whole thing in 2–3 ops, scalar takes 500+ ops.
- Length band: ~2–3 min
- Still lanes: c2v, geo
- Prerequisites: CPU instruction sets, parallelism, vectorization
- Exclusions: general performance optimization, CPU microarchitecture, benchmarking methodology
- Score: 8/10

## Candidate 5 — How does switching from shared to per-request buffers prevent data corruption in concurrent code?
- Source: `CHANGELOG.md`
- Topic: Buffer allocation strategy and concurrent safety
- Hook: orjson's parser used a single global deserialization buffer; concurrent calls could corrupt it; 3.11.0 switched to per-request buffers.
- Key case: Thread A deserializes a large document; Thread B starts and overwrites the buffer; Thread A reads garbage.
- The Question: Shared buffers should work across threads if serialization is fast enough; concurrent case did not; why does per-request allocation prevent corruption?
- Core idea: Shared mutable state requires synchronization to stay safe; per-request allocation eliminates the shared state entirely, so threads can't interfere; the tradeoff is memory (each call gets its own buffer) vs. simplicity and safety.
- Visual object: Two concurrent call timelines showing buffer lifecycle: first shows overlapping writes and corruption, second shows isolated buffers with no contention.
- Manim move: split
- Example seed: Two Python threads calling `orjson.loads()` simultaneously on large documents; shared buffer = data corruption, per-request = both succeed safely.
- Length band: ~2–3 min
- Still lanes: geo
- Prerequisites: threads, shared state, memory allocation, mutexes
- Exclusions: general thread-safety patterns, memory management in Python, GIL
- Score: 7/10

## Candidate 06 — Why does serializing NaN silently produce null instead of failing?
- Source: `CHANGELOG.md`
- Topic: IEEE 754 special values and JSON's representational gap
- Hook: A NaN float in your data silently becomes JSON null; your API consumer sees a missing metric where a failed computation should be visible.
- Key case: `orjson.dumps({"latency": float("nan")})` → `b'{"latency":null}'` — the NaN is consumed with no warning.
- The Question: NaN is a valid float; serialization should preserve the value or fail loudly; this case did neither; why does the library produce null?
- Core idea: JSON forbids NaN and Infinity literals by spec; the serializer must choose one of three incompatible policies — map to null (preserve shape, lose meaning), raise an error (OPT_DISALLOW_NAN), or emit a non-standard literal (post-3.11.7 flag); the default policy silently drops information, exactly like Candidate 1 but caused by a spec gap rather than Python's implicit return.
- Visual object: A three-way branch diagram: a NaN float entering one node, three labeled output paths — `null` (default), `JSONEncodeError` (OPT_DISALLOW_NAN), and `NaN` literal (non-standard flag).
- Manim move: split
- Example seed: `{"latency": float("nan"), "p99": float("inf")}` — default dumps gives `{"latency":null,"p99":null}`; OPT_DISALLOW_NAN raises on the first NaN; the post flag gives `{"latency":NaN,"p99":Infinity}` (non-standard).
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: IEEE 754 special values, JSON spec section 6
- Exclusions: JavaScript NaN propagation behavior, general float-to-string formatting, other libraries' NaN handling strategies
- Score: 8/10

## Candidate 07 — Why does orjson serialize list subclasses but refuse all tuple subclasses?
- Source: `README.md`
- Topic: The namedtuple semantic trap and deliberate asymmetry in subclass serialization
- Hook: orjson serializes subclasses of str, int, dict, and list — but explicitly blocks all tuple subclasses, including namedtuple.
- Key case: `class Point(NamedTuple): x: int; y: int` — following the subclass pattern, `Point(3, 4)` should serialize; it raises JSONEncodeError instead.
- The Question: Subclassing a serializable type should inherit serialization; tuple subclasses did not; why does one branch of the type hierarchy break the pattern?
- Core idea: namedtuple overloads tuple subclassing to create a struct with named fields; serializing it as a positional array (`[3, 4]`) silently erases all field semantics; rather than guess wrong for this common case, orjson disables all tuple subclass serialization and forces the caller to decide the representation explicitly via OPT_PASSTHROUGH_SUBCLASS and a default handler.
- Visual object: A type hierarchy tree: tuple at root, plain subclass and namedtuple branching off; one serialization arrow hits a red stop for all branches, with a label explaining the namedtuple reason.
- Manim move: split
- Example seed: `Point = namedtuple("Point", ["x","y"]); Point(3, 4)` — stdlib json gives `[3, 4]` silently; orjson raises JSONEncodeError, forcing you to write `default=lambda o: o._asdict()` and get `{"x":3,"y":4}` instead.
- Length band: ~2–3 min
- Still lanes: c2v, geo
- Prerequisites: Python type hierarchy, namedtuple vs tuple, isinstance semantics
- Exclusions: dataclass as a namedtuple replacement, OPT_PASSTHROUGH_SUBCLASS detailed usage, performance differences between subclass types
- Score: 7/10
