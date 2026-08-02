# Claude Search and Retrieval Demo [Experimental] Video Ideas

## Candidate 1 — Why one question spawns multiple searches, not one

- Source: `README.md`
- Topic: Iterative query refinement through Claude's reasoning
- Hook: A user asks one question; Claude issues multiple search queries in sequence, stopping when it decides it has enough context—no human says when to stop.
- Key case: "I want gifts for my daughter interested in science" → Claude searches "science gifts" → examines results → searches "educational STEM toys" → decides adequate information gathered → stops.
- The Question: Why should multi-turn retrieval with an LLM's reasoning between turns beat single-shot keyword search?
- Core idea: Claude reads previous search results, identifies gaps in knowledge coverage, formulates a refined query, and applies a termination condition to its own search loop.
- Visual object: A decision-tree or flow diagram where one query branches into multiple searches, each returning results, with a stop/continue decision node.
- Manim move: accumulate
- Example seed: Query: "How do plants photosynthesize?" → Search 1: "photosynthesis" (3 results) → Search 2: "photosystem light reactions" (2 results) → Search 3: "electron transport chain" (2 results) → outputs stop signal.
- Length band: 2–3 min
- Still lanes: c2v (Claude in loop), raster (query→result flow)
- Prerequisites: retrieval-augmented generation basics
- Exclusions: search backend internals, vector embeddings, differences between web and local search
- Score: 9/10

## Candidate 2 — Why search results must be formatted before Claude reads them

- Source: `README.md`
- Topic: Structure and formatting as a retrieval constraint
- Hook: The same product description produces a mediocre summary if passed as plain text, but sharp synthesis if wrapped in XML tags; Claude's training created this preference.
- Key case: Raw text "Product Name: LeapFrog... Letters and words woven..." vs. same content in `<search_result><title>LeapFrog</title><content>Letters and words...</content></search_result>` yields noticeably different synthesis quality.
- The Question: Why does fine-tuning create an expectation for a specific input structure that models won't relax even if content is identical?
- Core idea: Large models trained on consistently formatted data develop strong statistical patterns for those formats. Inputs matching the training distribution are processed more coherently; outliers are compressed less effectively.
- Visual object: A before-and-after comparison pane showing unstructured text on left, formatted XML on right, with arrows pointing to output differences.
- Manim move: morph
- Example seed: Unformatted: "Product Name: Robot Building Kit. Includes 200 pieces for assembling robots." Formatted: `<item><title>Robot Building Kit</title><content>Includes 200 pieces for assembling robots.</content><category>STEM Learning</category></item>`.
- Length band: ~1 min
- Still lanes: raster (text transformation)
- Prerequisites: basic LLM training and fine-tuning concepts
- Exclusions: XML schema specifics, other markup formats, tokenization, attention mechanisms
- Score: 9/10

## Candidate 3 — How one retrieval loop works with many knowledge bases

- Source: `README.md`
- Topic: Abstraction and interface design for retrieval backends
- Hook: Your retrieval code works identically whether you query Wikipedia, Elasticsearch, a vector database, or the web; swapping backends requires changing one line, not rewriting the loop.
- Key case: A retrieval loop calls `search_tool.search(query)` without knowing whether the backend is Pinecone, Elasticsearch, or Brave; each returns results in the same structure.
- The Question: What abstraction lets you write a single retrieval mechanism that is agnostic to where data lives?
- Core idea: A common interface (SearchTool) standardizes the contract: input is a natural-language query, output is a list of documents. Implementations hide backend differences; Claude's retrieve() never needs to know which search engine is active.
- Visual object: A central retrieve() function with branching lines to multiple SearchTool implementations (Wikipedia, Elasticsearch, Pinecone, Brave), each returning formatted results through a unified input.
- Manim move: collapse
- Example seed: Three calls to `completion_with_retrieval()`: one passes WikipediaSearchTool, one passes ElasticsearchSearchTool, one passes PineconeSearchTool. Same query, same code path, different backends.
- Length band: 2–3 min
- Still lanes: c2v (Claude talking to abstraction), raster (multiple backends funneling through interface)
- Prerequisites: object-oriented design, interfaces and abstract classes
- Exclusions: implementing specific backends, vector embeddings, Elasticsearch syntax, database schema design
- Score: 8/10

The corpus is supplied directly in the prompt. Evaluating from the provided text:

---

# Claude Search and Retrieval Demo [Experimental] Video Ideas

## Candidate 04 — Why splitting search from synthesis creates an intervention point

- Source: `README.md`
- Topic: Pipeline decomposition in retrieval-augmented generation
- Hook: `completion_with_retrieval()` is simpler to call, but it is also a black box; splitting it into `retrieve()` and `answer_with_results()` opens a gap between the two stages where custom logic can be injected without modifying the library.
- Key case: After `retrieve()` returns 7 product results, the caller filters to only the 3 with a customer rating above 4.0, then passes those to `answer_with_results()`—a post-processing step that the end-to-end method can never support.
- The Question: If `completion_with_retrieval()` already does everything, why would you ever call `retrieve()` and `answer_with_results()` separately?
- Core idea: Decomposing a pipeline into two explicit stages creates an owned gap between them. The caller controls what happens in that gap—re-ranking, deduplication, logging, human review—without the library needing to anticipate those needs.
- Visual object: A pipeline diagram with a visible gap between two labeled stages, the gap containing a user-owned processing block
- Manim move: split
- Example seed: `retrieve()` returns [A, B, C, D, E, F, G]; user filters to rating > 4.0, keeping [B, D, F]; `answer_with_results()` synthesizes from only those three. Same query, same library, different answer.
- Length band: 2–3 min
- Still lanes: raster (pipeline split diagram), c2v (Claude as one named stage)
- Prerequisites: function composition, retrieval-augmented generation basics
- Exclusions: specific filtering or re-ranking algorithms, internals of either method, async pipeline patterns
- Score: 7/10

## Candidate 05 — Why the same document appearing twice inflates its weight in Claude's answer

- Source: `README.md`
- Topic: Deduplication as a correctness guard in multi-search retrieval
- Hook: Claude searches three times and the same product appears in two of those searches; without deduplication, it occupies twice the token space in Claude's context, statistically pulling the synthesis toward it—not because it is the best answer but because it is repeated.
- Key case: Searches for "science gifts," "STEM toys," and "educational kits" all return the Robot Building Kit; deduplicated context lists it once among five unique results; non-deduplicated context lists it twice among seven entries, doubling its textual mass.
- The Question: If an LLM can "see" that two entries are identical, why does the repeated entry still bias the output?
- Core idea: LLMs synthesize by attending over token sequences, not by maintaining an explicit document registry. A document appearing N times contributes N times the token evidence to attention patterns during generation, shifting outputs toward it even when the content is semantically redundant.
- Visual object: A context window with two identical document blocks side-by-side, contrasted with a deduplicated window showing one block—output arrows diverging
- Manim move: accumulate
- Example seed: Three searches return [A, B, C], [B, D], [C, E]. Non-deduplicated: A B C B D C E (7 tokens of mass, B and C doubled). Deduplicated: A B C D E (5 unique). Claude's synthesis shifts toward B and C in the first case.
- Length band: ~1 min
- Still lanes: raster (context window visualization)
- Prerequisites: LLM context window basics, retrieval-augmented generation basics
- Exclusions: exact deduplication algorithm (hash vs. fuzzy match), embedding-based similarity deduplication, attention mechanism internals
- Score: 6/10
