# Apache Beam Video Ideas

## Candidate 1 — How do models batch streaming elements without losing real-time semantics?
- Source: `examples/notebooks/beam-ml/README.md`
- Topic: Streaming ML inference with windowed batching
- Hook: Machine learning models require batch inputs, but streaming data arrives one element at a time—buffering defeats streaming goals, yet ignoring it wastes model throughput.
- Key case: RunInference transform receiving individual events (sensor readings, user clicks) from Kafka, collecting them via windowing, batching for a TensorFlow model, then ungrouping predictions back to individual results.
- The Question: How can you accumulate streaming elements into batches for model input without introducing latency that undermines the streaming pipeline's real-time guarantees?
- Core idea: Windowing creates micro-batches triggered by time or element count; the RunInference transform buffers elements within each window, sends them as a batch to the model, then explodes predictions back to per-element results—the window boundary is the only buffering.
- Visual object: A timeline showing individual events arriving, being collected into a window container, fed together into a model box, then results spreading back out as individual predictions paired with their inputs.
- Manim move: accumulate, transform, spread
- Example seed: 15 user-behavior events arrive in 1-second intervals; every 3 seconds, batch up to 20 events, score sentiment with BERT, emit individual predictions with latency ≤ 4 seconds.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic Beam PCollection, windowing concept
- Exclusions: model deployment infrastructure, tuning batch size vs. latency tradeoff, handling late arrivals
- Score: 9/10

## Candidate 2 — Why does the same code run on streaming data and batch files?
- Source: `examples/java/README.md` (WindowedWordCount)
- Topic: Runner-agnostic windowing for bounded and unbounded data
- Hook: A bounded input (file) has a defined end; an unbounded input (Kafka stream) has none—yet the same WindowedWordCount pipeline works for both without code changes.
- Key case: WindowedWordCount.java invoked with `--runner=DirectRunner --input=local_file.txt` (batch) then rerun against `--input=kafka_topic` (streaming) using identical window and transform logic.
- The Question: If file-based data terminates but streams never do, how does the same windowing logic emit results in both cases?
- Core idea: Windowing triggers decouple result emission from collection type. In batch, the default trigger fires when the window closes AND the input ends. In streaming, the trigger fires repeatedly (e.g., every second) regardless of whether data still arrives.
- Visual object: Two parallel timelines—top shows a file divided into fixed 1-minute windows with a clear termination point; bottom shows a continuous stream divided into identical 1-minute windows, each firing its trigger independently.
- Manim move: split, scan
- Example seed: Word counts per minute from a 30-minute CSV file (8 windows, results at end) vs. a live Twitter stream (windows fire every minute indefinitely).
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Beam transforms, awareness of streaming vs. batch distinction
- Exclusions: watermarks, late-data handling, custom trigger logic, session windows
- Score: 7/10

## Candidate 3 — How do pandas operations execute as a distributed lazy pipeline?
- Source: `sdks/python/apache_beam/examples/dataframe/README.md`
- Topic: Pandas-compatible syntax on lazy, distributed collections
- Hook: Pandas is eagerly evaluated in-memory; Beam is lazy and distributed across machines—yet the DataFrame API lets you write as if it's pandas, then executes as a DAG.
- Key case: DataFrame wordcount where `df.groupby('word').count()` is written exactly as it would be in a pandas notebook, but is executed as a distributed Beam pipeline with GroupByKey and Combine transforms.
- The Question: How does a method like `.sum()` produce correct results on data that is unknown until runtime and scattered across workers—how does pandas syntax map to distributed semantics?
- Core idea: The DataFrame API records operations into an expression tree at definition time. At execution, the tree is lowered into Beam primitives—`groupby().count()` becomes ParDo + GroupByKey + Combine—preserving semantics.
- Visual object: A two-column diagram: left column shows pandas code (df['age'].mean()), right column shows the lowered Beam DAG (PCollection → ParDo → CombineGlobally); arrows show the transformation.
- Manim move: morph, transform
- Example seed: Compute mean income per state from 10 million person records—write `df.groupby('state')['income'].mean()` in a notebook, execute on 100 workers, get per-state results.
- Length band: 2–3 min
- Still lanes: c2v, code transformation
- Prerequisites: basic pandas syntax, concept of lazy evaluation
- Exclusions: detailed schema inference, stateful operations, complex pandas functions without Beam equivalents
- Score: 8/10

## Candidate 4 — How do you call a Java transform from a Python pipeline?
- Source: `examples/multi-language/README.md`
- Topic: Cross-language transform invocation via expansion services
- Hook: Python and Java are separate runtimes; yet Beam lets you write Python code that calls a Java transform and continues in Python—what sits in between?
- Key case: Python pipeline imports `beam.External('org.apache.beam.transforms.Count')`, calls it on a PCollection, and receives results—no JVM embedding, no serialization boilerplate visible.
- The Question: If the Python interpreter cannot natively invoke Java bytecode, how does the framework bridge the gap without rebuilding the transform?
- Core idea: The expansion service is a separate gRPC process (often Java-based) that listens for transform requests serialized as protocol buffers. It expands (translates) the requested Java transform into Beam's portable IR (a graph that any runner understands), then returns it for the Python runner to execute.
- Visual object: Three boxes arranged left-to-right: Python client (with External call), expansion service in the middle (gRPC endpoint), Java implementation on the right. Arrows show proto request → parsing → Java execution → proto response.
- Manim move: duplicate, scan
- Example seed: Python pipeline reads user events and calls Java's `Count.perElement()` via `localhost:8099` expansion service—service unmarshals request, invokes Java Count class, serializes result back to Python, execution continues.
- Length band: 3–5 min
- Still lanes: c2v, architecture diagram
- Prerequisites: Beam transform composition, gRPC awareness helpful but not required
- Exclusions: protocol buffer schema details, schema evolution, performance tuning, security of expansion service
- Score: 6/10

## Candidate 05 — Why does SQL's GROUP BY work when rows arrive one at a time?
- Source: `examples/java/sql/README.md`
- Topic: SQL query compilation to distributed Beam transforms
- Hook: SQL assumes all rows are present at query time, but Beam processes elements as they arrive one at a time — yet SqlTransform lets you write `SELECT key, MIN(val), MAX(val), SUM(val) … GROUP BY key` directly on a PCollection.
- Key case: `SqlTransformExample.java` executing a GROUP BY aggregation on a PCollection<Row> — no database, no in-memory table, just elements flowing through a Beam pipeline.
- The Question: SQL's GROUP BY must collect all rows matching a key before it can aggregate — how does this work when the "table" is a PCollection with no defined end?
- Core idea: Beam SQL (via Apache Calcite) compiles the SQL string into a relational algebra tree, then lowers each node to Beam primitives: GROUP BY becomes GroupByKey, MIN/MAX/SUM become CombinePerKey accumulators that update incrementally as each element arrives — no rows are held waiting.
- Visual object: A SQL string splitting into a parse tree of relational nodes (Scan → Filter → Aggregate), each node morphing into its Beam equivalent (Read → ParDo → CombinePerKey), with accumulator state bars updating as elements flow through.
- Manim move: morph, accumulate
- Example seed: Six sales rows (keys "west"/"east", values 10/20/30) arrive one at a time; west_min stays 10 across three arrivals, east_max ratchets 20→30; final results emit when the window closes — no full collection ever held.
- Length band: 2–3 min
- Still lanes: c2v, code transformation
- Prerequisites: SQL GROUP BY semantics, Beam PCollection concept
- Exclusions: Apache Calcite internals, streaming continuous-query semantics, JOIN implementation, schema inference
- Score: 9/10

## Candidate 06 — How does one pipeline serve a different ML model to every data key?
- Source: `examples/notebooks/beam-ml/README.md`
- Topic: Per-key ML model routing inside a single RunInference transform
- Hook: Specialized models outperform general ones, but branching a pipeline into N separate paths — one per model — is operationally unmanageable; yet a single RunInference step can dispatch each element to its correct model.
- Key case: An image classification pipeline where elements tagged "cat" are scored by a cat-breed model and elements tagged "dog" by a dog-breed model — one `RunInference` call, two models, no pipeline fork.
- The Question: If each element's model depends on its key, how can a single transform select the right model without the pipeline graph branching into N paths at authoring time?
- Core idea: `KeyedModelHandler` maintains a dictionary mapping each key to its model handler; on each element it looks up the key, retrieves (or caches) the appropriate model instance, and dispatches inference — the routing lives inside the transform, invisible to the pipeline graph.
- Visual object: A stream of (key, data) pairs entering a single RunInference box; inside the box, a small lookup table maps keys to labeled model icons; labeled predictions exit the other side — the box stays one box throughout.
- Manim move: split, collapse
- Example seed: 100 product reviews arrive; 60 tagged "electronics" route to a tech-BERT model, 40 tagged "food" route to a food-sentiment model — one transform handles both, total latency matches a single-model baseline.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Beam RunInference concept, key-value pairs in PCollections
- Exclusions: model loading latency, memory management for large model dictionaries, dynamic key registration at runtime
- Score: 7/10
