# FACTCHECK — show-tell-five-ways-to-wire-an-agent

**What this is.** Every claim the film speaks or shows, checked against its one source: Anthropic Engineering, "Building effective agents" (Erik S. and Barry Zhang, published Dec 19, 2024), read from the saved page `anthropics/youtube/Building Effective AI Agents _ Anthropic.html`. **Result:** PASS. No numbers are claimed. Every drawn count (stations, workers, votes, step pips, cost stacks) is an illustration and has an EXEMPT row. Nothing needed a secondary source, so nothing is attributed beyond Anthropic itself (named aloud in BIDEA and in the Your Turn prompt).

Status: PASS · 2026-09-26 · checked by Claude (Opus 5.5) for Bear

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | Anthropic worked with dozens of teams building agents | PASS | "We've worked with dozens of teams building LLM agents across industries." | — |
| 2 | BIDEA | The most successful ones used simple patterns, not complex frameworks | PASS | "the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns." | — |
| 3 | BIDEA | Ask for the simplest one that works (writer: "the smartest agent?" → "the simplest one that works?") | PASS (paraphrase) | "we recommend finding the simplest solution possible, and only increasing complexity when needed." The "smartest agent" line is the naive question the film corrects, not a claim. | — |
| 4 | BDEFS | Augmented LLM: a language model with retrieval, tools, and memory attached | PASS | "an LLM enhanced with augmentations such as retrieval, tools, and memory." | — |
| 5 | BDEFS | Workflow: models and tools run along paths written in code ahead of time | PASS | "Workflows are systems where LLMs and tools are orchestrated through predefined code paths." | — |
| 6 | BDEFS | Agent: the model directs its own steps and its own tool use | PASS | "Agents … are systems where LLMs dynamically direct their own processes and tool usage." | — |
| 7 | B00 | Everything starts with one station, and every pattern after it is built from stations like it | PASS | "The basic building block of agentic systems is an LLM enhanced with augmentations…"; "we'll assume each LLM call has access to these augmented capabilities." | — |
| 8 | B00 | Retrieval to look things up, tools to act, memory to keep what matters | PASS (paraphrase) | "generating their own search queries, selecting appropriate tools, and determining what information to retain." | — |
| 9 | B00 | Drawing: tools shown as the dark connector block from the plugin film | EXEMPT (illustration) | The article names the Model Context Protocol as one way to implement augmentations; the block is a visual, not a claim that tools must be MCP. | — |
| 10 | B01 | Prompt chaining splits the job into fixed steps; each call works on the output of the one before | PASS | "decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one"; "cleanly decomposed into fixed subtasks." | — |
| 11 | B01 | A gate between steps checks that it's still on track | PASS | "You can add programmatic checks (see 'gate' …) on any intermediate steps to ensure that the process is still on track." | — |
| 12 | B01 | "Outline, check, then write." | PASS | Example: "Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline." | — |
| 13 | B01 | Drawing: three stations, one gate after the first | EXEMPT (illustration) | Mirrors the article's diagram (call → gate → call → call). The count is illustrative. | — |
| 14 | B02 | Routing classifies what comes in and sends it down the line built for it | PASS | "Routing classifies an input and directs it to a specialized followup task." | — |
| 15 | B02 | Refunds go one way, tech support another | PASS | Example: "customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools." | — |
| 16 | B02 | Easy questions can go to a smaller, cheaper model | PASS | "Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models." (The film names no model.) | — |
| 17 | B03 | Parallelization runs the calls at the same time and merges the results in code | PASS | "LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically." | — |
| 18 | B03 | Sectioning runs different parts of the job side by side | PASS | "Sectioning: Breaking a task into independent subtasks run in parallel." | — |
| 19 | B03 | Voting runs the same task several times and compares the answers | PASS | "Voting: Running the same task multiple times to get diverse outputs"; the voting examples compare the outputs against "vote thresholds". | — |
| 20 | B03 | Drawing: two checks and one cross; the two agreeing answers merge | EXEMPT (illustration) | The article does not fix a majority rule; the picture shows one possible aggregation. | — |
| 21 | B04 | A central model decides the subtasks on the spot, hands them to worker models, and pulls the results together | PASS | "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results." | — |
| 22 | B04 | Unlike parallelization, the pieces aren't fixed in advance | PASS | "the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input." | — |
| 23 | B04 | Drawing: four workers appear, then a fifth | EXEMPT (illustration) | The worker count is illustrative; the fifth worker shows that the count depends on the job. | — |
| 24 | B05 | One call makes the work; another judges it and sends it back with notes, round and round | PASS | "one LLM call generates a response while another provides evaluation and feedback in a loop." | — |
| 25 | B05 | "against clear criteria" | PASS | "particularly effective when we have clear evaluation criteria." | — |
| 26 | B05 | Drawing: sent back once, passes on the second round | EXEMPT (illustration) | The number of rounds is illustrative (the article's loop has no fixed count). | — |
| 27 | B06 | Take the rails away: that's an agent. It plans and picks its own route, one tool call at a time | PASS | Rails = the "predefined code paths" of workflows (row 5). "Once the task is clear, agents plan and operate independently"; "They are typically just LLMs using tools based on environmental feedback in a loop." | — |
| 28 | B06 | It checks real results, like a test run, at every step | PASS | "it's crucial for the agents to gain 'ground truth' from the environment at each step (such as tool call results or code execution)." | — |
| 29 | B06 | It gets a stop condition, such as a maximum number of steps | PASS | "it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control." | — |
| 30 | B06 | Drawing: four hops, eight step pips, a stop marker | EXEMPT (illustration) | Counts are illustrative. | — |
| 31 | B07 | Start with the simplest | PASS | "finding the simplest solution possible"; Summary: "Start with simple prompts … add multi-step agentic systems only when simpler solutions fall short." | — |
| 32 | B07 | Often one good call with retrieval and examples is enough | PASS | "For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough." | — |
| 33 | B07 | Every added step costs time and money | PASS (derivation) | "Agentic systems often trade latency and cost for better task performance"; prompt chaining trades "latency for higher accuracy"; agents mean "higher costs". Each added LLM call is another paid call; chained calls add latency. | — |
| 34 | B07 | Add one only when you can measure that it helps | PASS | "you should consider adding complexity only when it demonstrably improves outcomes"; "The key to success … is measuring performance and iterating." | — |
| 35 | B07 | Drawing: a staircase with growing cost stacks and a gauge | EXEMPT (illustration) | No data; heights are illustrative. | — |
| 36 | BHTF | Your Turn: map one weekly task to the simplest pattern; say what a simpler one gets wrong and what to measure; check on five real examples first | PASS (instruction) | An exercise built on rows 31–34. "Five real examples" is the viewer's own test size, not a claim. | — |
| 37 | Title | "Five Ways to Wire an Agent" | PASS (framing) | The article presents five workflow patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) and calls every variation an "agentic system"; the film says aloud that the sixth thing, a true agent, is what you get when the rails come off. | — |
| 38 | — | Currency of the source | NOTE | The saved page carries Anthropic's note that "much of the tooling landscape described in this post has changed since December 2024." The film uses only the patterns and the advice, not the framework or tooling list. | — |
