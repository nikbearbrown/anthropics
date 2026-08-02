# Claude Code ROI Measurement Guide Video Ideas

## Candidate 1 — Why longer Claude Code sessions don't generate proportionally more output

- Source: `sample-report-output.md`
- Topic: Session duration vs. PR productivity curve
- Hook: Doubling your session time doesn't double your output — there's an optimal window and a productivity cliff.
- Key case: A team averaging 40-minute sessions generates fewer PRs per sprint than one averaging 28 minutes, despite sessions 40% longer.
- The Question: If Claude Code's value scales with time invested, why does a 90-minute deep-work session sometimes produce fewer merged PRs than two separate 30-minute focused sessions?
- Core idea: Each session has a context-accumulation cost. Early in a session, Claude builds understanding of your codebase and task intent. After 25–35 minutes, additional tokens yield diminishing returns as working context fills and cognitive momentum decays; developers must restart effort, losing gains.
- Visual object: A bell curve showing PRs completed (y-axis) against session duration (x-axis), peaking at 25–35 minutes and declining steeply beyond 60 minutes.
- Manim move: scan
- Example seed: Q1 baseline: 40-min average sessions, 18 PRs per sprint. Q2 after optimizing to 28-min sessions with same tool usage: 26 PRs per sprint without scope creep.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: PR workflows, developer task batching
- Exclusions: LLM context windows and token limits (too technical); time-management frameworks (scope creep)
- Score: 9/10

## Candidate 2 — How token costs collapse in month two without changing usage

- Source: `claude_code_roi_full.md` (Prometheus queries), `sample-report-output.md` (Cost Analysis)
- Topic: Prompt caching and token cost optimization over time
- Hook: Your team spends the same budget on Claude in month two but extracts three times more value — the model is reading your codebase from cache.
- Key case: Week 1: 300K input tokens, 5K cache-read tokens, $47 cost. Week 4: 90K input tokens, 450K cache-read tokens, $31 cost. Same feature velocity, 34% cost reduction.
- The Question: If cost per session is determined by tokens spent, why does the same team's cost-per-feature drop 40% in the second month when query patterns and model pricing remain constant?
- Core idea: Prompt caching accumulates invisibly as Claude processes the same codebase repeatedly. Initial sessions are expensive (full context encoding); subsequent sessions reuse cached embeddings and parsed code structures, compressing token spend. This compounds as the team's "hot" code (frequently queried files) grows a cache footprint.
- Visual object: A pie chart of token composition (input %, output %, cache-read %) morphing from week 1 (input-dominated) to week 4 (cache-read-dominated), with dollar values embedded.
- Manim move: morph
- Example seed: 60K-line codebase on Opus. Week 1: $47, 250K input tokens, 8K cache reads. Week 4: $31, 90K input tokens, 380K cache reads. Same team velocity; cache hits absorbed 75% of reading work.
- Length band: 3–5 min
- Still lanes: c2v, raster with cost breakdowns
- Prerequisites: API pricing fundamentals, token counting concepts
- Exclusions: Cache invalidation mechanics, distributed cache architecture, token accounting edge cases
- Score: 9/10

## Candidate 3 — The cost-per-PR learning curve

- Source: `sample-report-output.md` (Cost Analysis, Cost per Issue metric)
- Topic: Cost efficiency compounding through repeated tool use
- Hook: As your team masters Claude Code, the cost to ship the same feature halves — not because pricing changed, but because the team got better at prompting and caching worked.
- Key case: Month 1 cost-per-PR: $5.80. Month 3 cost-per-PR: $2.90. Identical Opus pricing, identical feature complexity; only the team's execution changed.
- The Question: If tokenizer behavior and model costs are fixed, and feature scope stays constant, how does cost-per-PR decline by 50% in twelve weeks?
- Core idea: Cost efficiency compounds through three layered mechanisms: tool-usage fluency (fewer rejected edits = wasted tokens avoided), prompt-engineering skill (precise specifications reduce back-and-forth queries), and codebase warming (cache hits accumulate). Each is invisible per-session but stacks into predictable monthly curves.
- Visual object: A downward-sloping line chart of cost-per-PR (y-axis) over weeks, with inflection points marking onboarding phases or team-composition shifts.
- Manim move: decay
- Example seed: Week 1: 20 PRs shipped at $6.20 per PR ($124 total spend). Week 12: 24 PRs shipped at $3.15 per PR ($75.60 total spend). Same velocity, 40% cost reduction.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Pricing models, PR workflows, learning curves in teams
- Exclusions: Model version changes, subscription discounts, bulk pricing negotiation
- Score: 8/10

## Candidate 4 — The adoption-rate threshold

- Source: `sample-report-output.md` (Tool acceptance rates and merge-time improvements)
- Topic: Tool acceptance thresholds and their sharp effect on velocity
- Hook: A team at 74% edit acceptance sees zero speed gain. A team at 76% sees PR merge time fall 16%. The threshold acts like a phase transition.
- Key case: Team A (72% Edit acceptance, 6.8 hr mean merge time) vs. Team B (78% Edit acceptance, 5.6 hr mean merge time). Identical codebase, size, Claude Code training. Only variable: willingness to trust Claude's edits without rewriting.
- The Question: If developer productivity scales smoothly with tool adoption, why do merge-time improvements appear suddenly above 75% adoption instead of scaling linearly from 0% to 100%?
- Core idea: Below a critical threshold, developers rewrite most suggestions, converting saved time to wasted validation cycles. Above it, a cultural shift occurs: Claude suggestions become default-trusted, review becomes verification-only, and review bottlenecks dissolve. The transition is abrupt, not gradual.
- Visual object: A scatter plot of team adoption rates (x-axis, 50–100%) vs. PR merge time (y-axis, 4–10 hours), with a visible kink or cloud split around 75%.
- Manim move: trace
- Example seed: 12 teams in Q2. Below 75% Edit acceptance: 6.2–8.1 hr merge time (mean 7.2). Above 75%: 4.8–5.9 hr merge time (mean 5.3). Threshold visible as a sharp separation.
- Length band: 2–3 min
- Still lanes: c2v, scatter with annotation
- Prerequisites: Code review workflows, team velocity metrics
- Exclusions: Change management, organizational psychology, per-tool fine-grained acceptance differences
- Score: 7/10

## Candidate 5 — The commit-velocity paradox

- Source: `sample-report-output.md` (Productivity Comparison: Commits/Week before/after)
- Topic: Commit frequency as a proxy for developer autonomy
- Hook: Teams using Claude Code commit 17% more frequently — and it's not churn. Merge times drop and code stays smaller, simpler, better-reviewed.
- Key case: Before Claude Code: 8.2 commits/week, 7.5 hr mean merge time, 165 LOC per PR. After: 9.6 commits/week, 6.3 hr mean merge time, 145 LOC per PR. More commits, faster reviews, cleaner diffs.
- The Question: More frequent commits usually signal rushed, untested work and slower reviews. Why does this team's commit velocity increase while merge time and PR size *decrease* simultaneously?
- Core idea: Claude automates boilerplate, test scaffolding, and implementation scaffolding, so developers commit smaller, more atomic changes. These are individually simpler to review (fewer files, clearer intent), so review cycles accelerate despite higher volume. Commit frequency becomes a proxy for developer autonomy — Claude handles the tedium — rather than panic or incompleteness.
- Visual object: A before-and-after grouped bar chart showing commit frequency (bars), merge time (overlaid line), and PR size (color shade). The pattern: taller bars, shorter lines, lighter colors.
- Manim move: compare
- Example seed: Individual developer, 4 commits/week baseline. After Claude Code: 5.3 commits/week. PR size: 180 LOC → 145 LOC. Merge time: 8.2 hrs → 6.8 hrs.
- Length band: 1–2 min
- Still lanes: c2v
- Prerequisites: Git workflows, code review culture
- Exclusions: Commit message quality, test coverage metrics, the sociology of shipping deadlines
- Score: 7/10

## Candidate 06 — Why typing one word can multiply your API bill by 1,000x

- Source: `claude_code_roi_full.md`
- Topic: Reasoning budget keywords and hidden token cost spikes
- Hook: "Ultrathink" isn't a style choice — it silently allocates thousands of hidden reasoning tokens your cost dashboard won't itemize.
- Key case: A developer runs the same architectural analysis twice. With "think": $0.003. With "ultrathink": $0.34. Same codebase, same question, 100x cost difference — and the chat output looks identical in length.
- The Question: If API costs are metered by visible input and output tokens, how can a single English word multiply the session bill by 100x without changing what the developer sees in the response?
- Core idea: Claude Code maps a fixed phrase ladder ("think" < "think hard" < "think harder" < "ultrathink") to internal reasoning-budget multipliers. Each level triggers an extended thinking phase that accumulates thousands of hidden inference tokens before output generation. These tokens are billed at full model rates but never surface in the transcript — they are reasoning work, not response work. The keyword acts as a hidden API parameter embedded in natural language, bypassing any token-count estimate a developer might form from prompt length alone.
- Visual object: Two side-by-side token receipts — visible input/output bars (roughly equal between runs) next to a reasoning-tokens bar that dwarfs them under "ultrathink," with dollar amounts embedded in each bar.
- Manim move: accumulate
- Example seed: Query: "ultrathink about the best database schema for this feature." Visible tokens: 820 input, 580 output. Hidden reasoning tokens: ~21,000. Cost: $0.34. Same query with "think": 820 input, 580 output, ~180 reasoning tokens. Cost: $0.003. *(illustrative)*
- Length band: ~1 min
- Still lanes: c2v, raster with token receipt breakdown
- Prerequisites: API token pricing fundamentals, prompt engineering basics
- Exclusions: Extended thinking API configuration, model internals and benchmark deltas across thinking levels, subscription-plan behavior under thinking keywords
- Score: 8/10
