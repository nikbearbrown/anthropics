# Sources and editorial corrections

Original, preserved: `../../cwc-workshops/youtube/agent-decomposition-skills-vs-tools/`.
User transcript: `/Users/bear/.codex/attachments/a0120b46-8c59-4dd7-9397-0da0e5906907/Pasted text.txt`.

1. [Anthropic StockPilot workshop](https://github.com/anthropics/cwc-workshops/blob/main/agent-decomposition/README.md), local source `../../cwc-workshops/agent-decomposition/README.md`. Reports 402→15 system-prompt lines, ~400 lines moved into skills; daily sweep 488s/102 tool calls→~100s/3 scripts. Multiple interventions; not a controlled ablation of skills. No benchmark rerun for this film.
2. [Claude Code skills](https://code.claude.com/docs/en/skills): on-demand instructions; `context: fork` explicitly invokes a separate context. A skill is not inherently a subagent.
3. [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): separate context, configured tools and permissions; delegation overhead.
4. [Equipping agents with skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): progressive disclosure of instructions and resources.

Read 2026-09-30. Inventory/approval illustrations are constructed teaching examples, not an actual purchasing system or captured benchmark. No claim that tool calls are stateless, costless, or necessarily deterministic. No correctness-equivalence, first-week-payback, or guaranteed-speedup claims retained. The ASR's “42-line” is corrected to the workshop's 402.
