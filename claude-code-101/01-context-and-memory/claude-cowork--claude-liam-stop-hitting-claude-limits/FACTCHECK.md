# FACTCHECK — stop-hitting-claude-limits

| Claim | Source | Status | Action |
|---|---|---|---|
| "Message 30 costs 31× more than message 1" | Ruben Hassid, "How to AI" newsletter | AUTHOR'S CLAIM — The underlying mechanic (Claude re-reads full history per message) is documented, but the specific 31× multiplier is the author's own calculation | Present as author's framing; do not state as Anthropic fact |
| "98.5% of tokens spent re-reading history" | Cited in article as "one developer tracked his usage" | ONE DEVELOPER'S REPORTED FINDING — not a general statistic, not published research | Frame explicitly as "one developer's reported finding" in narration or on-screen caveat |
| "A single PDF page costs 1,500–3,000 tokens" | Ruben Hassid | AUTHOR'S CLAIM — plausible ballpark but varies widely by content density, fonts, encoding | Flag as approximate; do not present as Anthropic specification |
| "A 1000×1000 screenshot ≈ 1,300 tokens" | Ruben Hassid | AUTHOR'S CLAIM — vision token costs depend on resolution tiers, not a fixed spec Anthropic publishes this way | Flag as approximate |
| "Tight crop can drop from 1,300 to under 100 tokens" | Ruben Hassid | AUTHOR'S CLAIM — plausible directionally, but specific numbers are not verified | Flag as illustrative, not guaranteed |
| "A 20-message session burns roughly 105,000 tokens" | Ruben Hassid | AUTHOR'S CLAIM — depends heavily on message length, not a universal figure | Flag as illustrative example |
| "A 30-message session burns 232,000 tokens" | Ruben Hassid | AUTHOR'S CLAIM — same caveat as above | Flag as illustrative example |
| "$20 plan" and "$100 plan" pricing | Ruben Hassid | DATABLE — Claude pricing can change; verify against current claude.ai plans before publish | Check pricing at time of publish |
| "Projects use RAG on paid plans" | Ruben Hassid citing Anthropic documentation | PLAUSIBLE — consistent with Anthropic docs at time of writing, but implementation details can change | Acceptable; note "as of writing" |
| "Claude uses a rolling 5-hour window for usage limits" | Ruben Hassid | DATABLE — Anthropic may change window parameters | Verify before publish |
| "Claude can't generate images" | Ruben Hassid | DATABLE — Claude's image capabilities have evolved; verify current capability before publish | Check at publish time |
| "Anthropic confirmed that similar prompts get partially cached" | Ruben Hassid paraphrasing Anthropic docs | PLAUSIBLE — prompt caching is real, but the specific "similar prompts" framing is the author's interpretation | Acceptable with caveat |
