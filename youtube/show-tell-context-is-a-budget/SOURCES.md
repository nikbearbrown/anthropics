# SOURCES — show-tell-context-is-a-budget

**What this is.** The source behind every claim, and how it was read.

1. **Anthropic Engineering, "Effective context engineering for AI agents"** (published Sep 29, 2025; Anthropic's Applied AI team). Saved page: `anthropics/youtube/Effective context engineering for AI agents _ Anthropic.html` (+ `_files/`). Read 2026-09-26 by extracting the article text from the saved HTML with Python's `html.parser`. Sections used:
   - Introduction: context = "the set of tokens included when sampling from a large-language model"; the context state (system instructions, tools, MCP, external data, message history); an agent in a loop "generates more and more data"; curation "happens each time we decide what to pass to the model".
   - "Why context engineering is important": context rot (from needle-in-a-haystack studies), "a finite resource with diminishing marginal returns", the "attention budget", every token attends to every other token, "n² pairwise relationships for n tokens", attention "stretched thin".
   - "The anatomy of effective context": "the smallest possible set of high-signal tokens"; clear system prompts; tools with "minimal overlap in functionality"; "diverse, canonical examples" instead of "a laundry list of edge cases".
   - "Context retrieval and agentic search": "just in time" context, lightweight identifiers ("file paths, stored queries, web links"), Claude Code using "Bash commands like head and tail … without ever loading the full data objects into context".
   - "Context engineering for long-horizon tasks": the three techniques — compaction (Claude Code keeps "architectural decisions, unresolved bugs, and implementation details" and discards "redundant tool outputs or messages"), structured note-taking (notes "persisted to memory outside of the context window", a to-do list or NOTES.md, read back after context resets), sub-agent architectures ("clean context windows", "tens of thousands of tokens or more", a summary "often 1,000-2,000 tokens").
   - Conclusion: "treating context as a precious, finite resource".

Used only as context, not spoken: the Pokémon tallies, the memory tool beta, tool-result clearing, the "five most recently accessed files" detail, and the note that compaction "typically serves as the first lever". No secondary sources, no social posts.
