# Swift Markdown Video Ideas

## Candidate 1 — Copy-on-write selective copying resolves the immutability paradox
- Source: `Sources/Markdown/Markdown.docc/Parsing-Building-and-Modifying Markup-Trees.md`
- Topic: Persistent tree mutations with structural sharing
- Hook: Modifying a deeply nested Text node should either break immutability or copy the entire tree—instead, only the path back to root is copied
- Key case: User navigates to node at path [0, 1, 0] in the tree, mutates `text.string = "really emphasized!"`, and gets back a new Document root where only the Text node, Emphasis parent, and Document root are new; siblings remain shared with the original
- The Question: When I mutate a leaf in an immutable tree, which ancestors must be copied to preserve immutability, and which subtrees can stay shared?
- Core idea: Copy-on-write backed by persistent trees—modifying a node creates new copies only of nodes on the path from leaf to root; all sibling subtrees and unmodified ancestor branches remain structurally shared between the old and new document
- Visual object: A tree diagram showing before mutation with all nodes in one color, then after mutation with the modified path shaded differently and unmodified subtrees left outlined
- Manim move: morph
- Example seed: A minimal document tree like `Document(Paragraph(Text("before "), Emphasis(Text("bold"))))`, modify the inner Text to "after", show the Paragraph's plain Text sibling node is identical in both old and new roots
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: immutable data structures, tree traversal via index paths
- Exclusions: copy-on-write vs full copy implementation tradeoffs, reference counting details, performance benchmarks
- Score: 10/10

## Candidate 2 — Visitor protocol return types encode transformation intent
- Source: `Sources/Markdown/Markdown.docc/Visitors-Walkers-and-Rewriters.md`
- Topic: Protocol-based tree traversal with polymorphic outcomes
- Hook: Three nearly identical code patterns walk the same tree but have incompatible purposes (count links, delete nodes, convert to XML)—the only syntactic difference is the return type
- Key case: LinkCounter declared with `Result = Void` and mutates a counter, StrongDeleter with `Result = Markup?` returns nil to delete or self to pass through, a hypothetical XMLConverter with `Result = XMLElement`
- The Question: Given that all three patterns visit every node in the same order, how does the choice of Result type determine which walker to write and what mutations it enables?
- Core idea: The `MarkupVisitor` protocol abstracts traversal; the associated `Result` type acts as a compile-time intent signal—`Void` signals pure traversal with side effects only, `Markup?` signals structural rewriting by return value, and custom types signal external conversion
- Visual object: Three code snippets stacked vertically, each overlaid on the same tree diagram, with outputs shown side-by-side (a count, a pruned tree, an XML document)
- Manim move: split
- Example seed: A document with three Links and three Strong nodes; LinkCounter output shows "count: 3", StrongDeleter output shows the document with Strong nodes vanished, an XML converter output shows parallel XML structure
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: visitor design pattern, Swift associated types, mutating methods
- Exclusions: traversal order (in-order vs post-order), `descendInto` implementation, visitor vs rewriter performance
- Score: 7/10

## Candidate 03 — Parsing erases formatting choices — the formatter must invent them back
- Source: `Sources/Markdown/Markdown.docc/Snippets.md`
- Topic: Information loss in parsing and canonical resynthesis by MarkupFormatter
- Hook: `*bold*` and `_bold_` produce identical `Emphasis` nodes—when you format the tree back to Markdown, the original marker is gone and the formatter must pick one
- Key case: Parse `**strong** or __strong__`; both produce `Strong(Text("strong"))`; format with `EmphasisMarkers(.asterisk)` and both render as `**strong**`; switch to `.underscore` and both render as `__strong__`—neither output matches the original mixed input
- The Question: If parsing discards which delimiter was used, how can `MarkupFormatter` always produce well-formed, consistent Markdown from any tree—even trees assembled programmatically with no original source?
- Core idea: The tree retains semantic structure but not surface form; `MarkupFormatter` walks the tree like a visitor and resolves every ambiguous rendering decision through an explicit option set—each option (`EmphasisMarkers`, `UnorderedListMarker`, `PreferredHeadingStyle`, `ThematicBreakCharacter`) covers exactly one dimension where the parse discarded information
- Visual object: A funnel diagram—two Markdown strings collapse into one tree node at the narrow neck; the funnel then widens on the right and different option settings branch into distinct Markdown strings
- Manim move: collapse
- Example seed: Inputs `*hello*` and `_hello_` both become `Emphasis(Text("hello"))`; with option `.asterisk` format produces `*hello*`; with `.underscore` produces `_hello_`; the tree itself is identical in all three cases
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: tree traversal, Markdown emphasis syntax
- Exclusions: line-wrapping algorithm behind MaximumWidth, HTMLFormatter output, CondenseAutolinks edge cases, ordered-list numeral renumbering
- Score: 8/10

## Candidate 04 — Block directive content is de-indented before cmark sees it — then source positions are repaired
- Source: `Sources/Markdown/Markdown.docc/Markdown/BlockDirectives.md`
- Hook: The cmark parser inside Swift Markdown receives block directive content with its leading indentation stripped—yet every node's reported source column must point to the original file, not the stripped copy
- Key case: `@Outer` at column 0 contains `@Inner` at column 8, whose content `- A` sits at column 10; cmark receives `- A` starting at column 0; without adjustment, a diagnostic would falsely report the list item at column 1
- The Question: If cmark parses a de-indented copy of the content and produces source ranges relative to that copy, how does the library report accurate line and column numbers back to the user?
- Core idea: After cmark finishes and returns a tree with coordinates in the stripped coordinate space, `RangeAdjuster` makes a second pass and adds the indentation offset back to every node's source range—translating cmark's internal coordinate system to the original file's coordinate system before the tree is exposed to callers
- Visual object: Two parallel rulers side by side—left labeled "cmark sees: col 1…" and right labeled "original file: col 11…"—with a labeled shift arrow between them showing the constant offset being added
- Manim move: transform
- Example seed: A 4-space-indented directive containing `- A`; cmark reports list item at `(row=1, col=1)`; after the +4 adjustment the library reports `(row=1, col=5)`; a user-facing error message correctly underlines column 5 in the original source
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: source maps concept, basic parser pipeline
- Exclusions: argument text multi-line grammar, Doxygen command parsing, block directive nesting depth limits, diagnostic collection API
- Score: 7/10
