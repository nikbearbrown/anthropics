# FACTCHECK — show-tell-claude-plugin-portal

**What this is.** Every claim the film speaks or shows, checked against Anthropic's announcement post (claude.com/blog/build-plugins-for-claude, 2026-09-25) and the @ClaudeDevs launch post on X. **Result:** PASS. One figure (110x) comes only from the X post, and the film attributes it on screen and aloud.

Status: PASS · 2026-09-26 (v2: hesitant-writer opener, terms card, composer Your Turn) · checked by Claude (Opus 5.5) for Bear

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | Claude just opened a portal for plugins | PASS | Blog, 2026-09-25: the "directory submission portal" (claude.ai/directory/manage/new). @ClaudeDevs: "We built a new portal to submit your plugin, track review, and see usage." | — |
| 2 | B01 | A plugin packages MCP connectors, skills, or both | PASS | Blog: "Plugins package MCP connectors, Agent Skills, or both". | — |
| 3 | BDEFS, B01 | MCP (Model Context Protocol) plugs Claude into outside tools and data; a skill is written instructions Claude loads to do one kind of task well | PASS (definition) | Standard definitions of MCP (Model Context Protocol connects models to external tools and data) and Agent Skills (folders of instructions Claude loads). Plain-language glosses, not quoted claims. | — |
| 4 | B02 | Way one: a single MCP connector, pointing at your own remote MCP server | PASS | Blog: "Single MCP connector: point to your remote MCP server". | — |
| 5 | B03 | Way two: a plugin bundle of MCP servers and skills in a GitHub repository; you submit the repo | PASS | Blog: "Plugin bundle: combine MCP servers and skills, host them on GitHub, and submit the repo." | — |
| 6 | B04 | You submit inside Claude, from the directory's manage page | PASS | The portal lives at claude.ai/directory/manage/new, in the Claude web app. | — |
| 7 | B04 | Open to developers on paid plans | PASS | Blog: the portal "is open to developers on paid Claude plans." | — |
| 8 | B04 | Checked and safety-scanned the moment you submit, so problems show up early | PASS | Blog: "Each submission is checked and safety-scanned as soon as you submit, so you catch issues early." | — |
| 9 | B05 | Track where it is in review, the safety-scan results, and recommended changes | PASS | Blog: "See where your plugin is in the review process, results from the safety scan, and recommended changes." | — |
| 10 | B05 | Submitted → In review → Live | PASS (illustration) | Three stages drawn from the blog's flow (submit, review, published to the directory). The stage names are the film's labels, not portal UI strings. | — |
| 11 | B06 | Installs by product and version; listing views; which searches lead people to it | PASS | Blog: "installs by product surface and version", "how often your listing is viewed and which searches lead people to it." | — |
| 12 | B06 | Bar and line chart values | EXEMPT (illustration) | Illustrative shapes with no numbers or axes. Not real data. | — |
| 13 | B07 | MCP usage across Claude products is up 110 times this year | PASS (attributed) | @ClaudeDevs on X (status 2103577007938228300): "MCP usage across Claude products is up 110x this year!" Not in the blog. Attributed aloud ("Claude's developer team says") and on screen ("per Claude's developer team"). The curve's shape is illustrative. | — |
| 14 | B07 | Plugins are becoming the way to build for Claude | PASS (attributed) | @ClaudeDevs: "are becoming the way to build for Claude"; blog: "the main way to build third-party extensions for Claude." | — |
| 15 | BHTF | Your Turn prompt: plan one MCP connector plus one skill for a tool you use; check that every action traces to real use and nothing unneeded is exposed | PASS (instruction) | An exercise built on the plugin contents in rows 2 and 5. Not a factual claim. | — |
| 16 | BDEFS | MCP is an open standard | PASS | Anthropic introduced the Model Context Protocol as an open standard in November 2024 (anthropic.com/news/model-context-protocol). | — |
| 17 | BDEFS | A plugin carries MCP connectors, skills, or both | PASS | Same as row 2 (blog). | — |
