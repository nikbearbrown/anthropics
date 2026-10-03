# Agent Decomposition: Skills vs Tools

Claude skills, tools, and subagents do different jobs. Learn where to put instructions, actions, and separate workers.

A slow agent does not necessarily need a shorter prompt. This illustrated teardown shows how to divide a workflow: load instructions only when needed, call tools for evidence and action, and delegate only when separate context earns its cost.

Follow an inventory assistant from policy to stock evidence, draft recommendation, and human approval. Then examine Anthropic's StockPilot workshop: a 402-line system prompt became 15 lines, while its daily sweep went from 102 tool calls to 3 scripts and from 488 seconds to about 100. Those are workshop-reported results from several changes together—not a benchmark reproduced here or a guaranteed speedup.

The test is the complete workflow: correctness, elapsed time, and usage. A faster wrong answer is not an improvement.

YOUR TURN
Paste into Claude: "Split my workflow into instructions, actions, and separate workers. Justify each boundary."
Check: can every action be tested? Does every separate worker need its own context?

CHAPTERS
0:00 Divide the work, not just the prompt
0:10 Skills, tools, and subagents
0:22 What belongs in the core?
0:36 402 lines to 15: where the instructions went
0:51 Skills load into context
1:05 Tools perform actions
1:19 When a separate worker helps
1:34 An inventory workflow
1:48 Human approval before spending
2:02 Batching: 102 calls to 3 scripts
2:16 What the reported speedup actually means
2:32 Measure the whole workflow
2:46 Your turn: justify the boundaries

SOURCES
Anthropic StockPilot workshop:
https://github.com/anthropics/cwc-workshops/blob/main/agent-decomposition/README.md
Claude Code skills:
https://code.claude.com/docs/en/skills
Claude Code subagents:
https://code.claude.com/docs/en/sub-agents

CREDITS
Nik Bear Brown. Narrated by Liam, in for Bear, using a synthetic Kokoro voice. Original animated illustrations; the inventory scenario is a teaching example. Independent educational commentary, not an Anthropic endorsement.

#Claude #AgentSkills #AgenticAI #NikBearBrown

## SEO Keyword Tags

Agent Decomposition, Agent Skills, Claude, Claude Code, Skills vs Tools, AI Subagents, Context Engineering, Agent Workflows, Human Approval, AI Evaluation, StockPilot Workshop, Nik Bear Brown
