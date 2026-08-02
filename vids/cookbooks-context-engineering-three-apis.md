## cookbooks-context-engineering-three-apis

- **Source path:** claude-cookbooks/tool_use/context_engineering/context_engineering_tools.ipynb
- **Teachable claim:** Three context-management APIs target three different causes of context window overflow — memory tool (cross-session persistence), compaction (conversation-length overflow), and tool clearing (tool-result bloat) — and the wrong choice for your cause makes performance worse, not better.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The problem: a biology-researcher agent runs across 53-cell notebook — token counter fills; show the three different growth curves (conversation accumulation, tool-result accumulation, long sessions losing early facts)
2. Memory tool: agent writes notes to `/memories/`; session 2 reads them; the cross-session recall test — what does the agent remember without memory vs. with?
3. Compaction: when conversation hits the threshold, SDK summarizes and reinitializes; show the before (context rot, wrong recall) vs. after (summary preserves key facts)
4. Tool clearing: after each tool call result, strip it from context with `tool_result_message_edit`; show token counter before/after on a 30-tool-call run

### Score
- Teachability: 5/5 — the "wrong API for wrong cause = worse performance" frame is the key insight
- Visual: 4/5 — token counter + recall test + before/after is concrete and checkable
- Pull: 5/5 — every developer with a long-running agent hits context problems
- Freshness: 5/5 — this three-way comparison is new and directly tied to the Effective Context Engineering blog post
- **Total: 19/20**
