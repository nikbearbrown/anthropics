# MarkdownUI Video Ideas

## Candidate 1 — Block styles wrap rendered content with additional views
- Source: `Sources/MarkdownUI/Documentation.docc/Articles/GettingStarted.md`
- Topic: Composable block style wrapping
- Hook: A block style configuration receives rendered markdown content and can layer it with padding, overlays, backgrounds, and custom modifiers
- Key case: The blockquote styled with a teal left-border rectangle overlay, padding, and background color—showing the composition layers
- The Question: How do you apply structural layout changes (borders, padding, overlays) to markdown blocks without reimplementing their rendering?
- Core idea: `configuration.label` is the final rendered block content; you receive it as a value and compose SwiftUI views and modifiers around it
- Visual object: A blockquote deconstructed into layers—the content frame, padding spacing, teal border rectangle, and background color stacked together
- Manim move: split
- Example seed: A code block with rounded corners, a gray background, and a "Copy" button in the top-right corner using overlay
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: SwiftUI view composition, overlay and padding modifiers
- Exclusions: Theme architecture, specific color or spacing values
- Score: 9/10

## Candidate 2 — Theme modifier cascades styling through the view tree
- Source: `Sources/MarkdownUI/Documentation.docc/Articles/GettingStarted.md`
- Topic: Environment-based style inheritance
- Hook: A single `.markdownTheme()` modifier at a parent view completely transforms the appearance of all nested markdown elements
- Key case: The identical blockquote markdown rendered twice—once with the basic theme and once with the GitHub theme, showing dramatic visual divergence
- The Question: How does a theme applied at one level control typography, colors, and spacing deep in a nested markdown tree?
- Core idea: Theme is an environment value that cascades down; each markdown element reads the current theme and applies its stored text and block styles
- Visual object: Side-by-side blockquote renderings showing color, border style, and typography changing completely while structure stays identical
- Manim move: morph
- Example seed: A short paragraph with inline code displayed under three themes (minimal, dark, bold) producing three visually distinct results
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: SwiftUI environment values, view modifiers
- Exclusions: Theme definition syntax, internal storage, color specifications
- Score: 8/10

## Candidate 3 — Text styles can be surgically overridden within a theme
- Source: `Sources/MarkdownUI/Documentation.docc/Articles/GettingStarted.md`
- Topic: Keypath-targeted style merging
- Hook: You want to keep a theme but change only one text style—like making inline code purple with a light background
- Key case: Using `markdownTextStyle(\.code) { ... }` to override just the code styling while every other text style from the theme remains untouched
- The Question: How do you override a single inline or block style without redefining the entire theme?
- Core idea: Keypath selector targets the exact style; the override merges with the base theme at the property level, not the theme level
- Visual object: A code snippet where only the inline `code` elements shift to purple text on a light purple background while surrounding paragraph text stays unchanged
- Manim move: morph
- Example seed: A heading containing bold text, italic text, and inline code where only the code color and background change
- Length band: 1–2 min
- Still lanes: c2v
- Prerequisites: SwiftUI keypath syntax
- Exclusions: Complete style property catalog, theme composition internals
- Score: 7/10

## Candidate 4 — Pre-parsing moves markdown processing from view render to model
- Source: `Sources/MarkdownUI/Documentation.docc/Articles/GettingStarted.md`
- Topic: Parsing memoization and timing
- Hook: Markdown gets re-parsed on every view update unless you parse it once upfront and cache the result
- Key case: Creating `MarkdownContent` once in the model layer (reusable, pre-parsed) versus passing a raw string to `Markdown()` (re-parsed each redraw)
- The Question: What happens to frame time if markdown parsing runs on every view cycle instead of once?
- Core idea: `MarkdownContent` is a pre-computed syntax tree; creating it outside the view layer decouples the expensive parsing from the frequent render cycle
- Visual object: A timeline showing two paths—string input to view (parse on redraw) versus pre-parsed MarkdownContent to view (parse once)
- Manim move: trace
- Example seed: A scrolling list of 20 items, each with markdown; measure frame time with and without pre-parsing
- Length band: 3–5 min
- Still lanes: raster with timing annotations
- Prerequisites: SwiftUI lifecycle, frame budgets
- Exclusions: Parser implementation, CommonMark specification details
- Score: 6/10

## Candidate 05 — Em units scale from the inherited context, not a fixed base
- Source: `Sources/MarkdownUI/Documentation.docc/Articles/GettingStarted.md`
- Topic: Relative font sizing via em cascade
- Hook: Declaring inline code at `FontSize(.em(0.85))` produces a visually larger code span inside a heading than inside body text—the same rule, two different outcomes
- Key case: A theme sets all `\.code` text to `FontSize(.em(0.85))`; code inside a level-2 heading inherits ~24 pt and renders at ~20 pt, while code in a body paragraph inherits ~17 pt and renders at ~14 pt
- The Question: If the em multiplier is fixed at 0.85, why doesn't all inline code render at the same absolute size?
- Core idea: `.em(N)` is resolved against the font size already inherited from surrounding context; the heading's larger base size multiplies with the same factor to produce a proportionally larger code span, just like CSS em units cascade through the DOM
- Visual object: A vertical stack of three text lines—heading, body, caption—each containing an inline code token, with arrows labeling the inherited base size and the computed code size for each row
- Manim move: accumulate
- Example seed: Heading inherits 24 pt → `.em(0.85)` → code at 20.4 pt; body inherits 17 pt → `.em(0.85)` → code at 14.5 pt; caption inherits 12 pt → `.em(0.85)` → code at 10.2 pt. All labeled illustrative.
- Length band: 2–3 min
- Still lanes: raster with size annotations
- Prerequisites: CSS-style em units, SwiftUI font inheritance
- Exclusions: Full font property catalog, device-specific point-to-pixel conversion, spacing margins (`.em` used there too but a separate concept)
- Score: 9/10

## Candidate 06 — String parser and result builder converge at one intermediate tree
- Source: `Sources/MarkdownUI/Documentation.docc/Articles/GettingStarted.md`
- Topic: MarkdownContent as the shared intermediate representation
- Hook: A raw Markdown string and a typed Swift result builder are syntactically opposite, yet they produce an identical rendering—because both compile into the same intermediate content tree before the view layer ever runs
- Key case: `Markdown("**bold** text")` and `Markdown { Strong("bold"); " text" }` display identically; both ultimately hand a `MarkdownContent` value to the renderer, which only ever sees the tree
- The Question: If raw strings already work, why expose a Swift DSL—and how can two such different input forms be equivalent?
- Core idea: Every input path terminates in a `MarkdownContent` value (a parsed content tree); the view only consumes that tree; the DSL bypasses the string-parsing step entirely and lets you use Swift control flow—loops, conditionals, computed values—to assemble content programmatically
- Visual object: A Y-shaped pipeline diagram: the string branch (raw markdown → parser) and the DSL branch (typed nodes → result builder) both converge at a `MarkdownContent` node, which feeds a single renderer arrow
- Manim move: transform
- Example seed: A list of book titles fetched from a model, assembled with `BulletedList { for book in shelf { ListItem { book.title } } }`—structure impossible to express as a static string literal. Labeled illustrative.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Swift result builders, abstract syntax tree concept
- Exclusions: Parser implementation, result builder `@resultBuilder` attribute syntax, performance comparison with Candidate 4 (pre-parsing)
- Score: 7/10
