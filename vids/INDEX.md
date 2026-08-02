# Anthropics Scout — Video Candidate Index

> **Format note:** Cards follow `skills/make/scout/SKILL.md` as the primary reference for rubric
> structure and score fields. The claude-scout card format (§"Card format") governs ask-beat
> layout for RESEARCH/PAPERS candidates. The cli-scout card schema governs BUILD/RESEARCH
> lane fields. Sim-scout card schema governs INTERPRETABILITY/VISUAL-MATH lane fields.
> All cards are in this `vids/` folder at `<kebab-slug>.md`.

---

## CLI-Scout Pass — 2026-07-24

Full-coverage CLI-scout pass over all `books/anthropics/` subdirectories not previously carded.
25 new cards (119 total). Slot into ranked list by score as noted.

| Score | Slug | Bucket | Builder | Slots at |
|---|---|---|---|---|
| 20/20 | cookbooks-roadtrip-planner-multiagent | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 1–4 |
| 19/20 | fable-5-fallback-billing | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 19/20 | cookbooks-agentic-search-benchmark | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 19/20 | cookbooks-sentry-scheduled-deployment | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 19/20 | cookbooks-context-engineering-three-apis | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 19/20 | cookbooks-programmatic-tool-calling | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 19/20 | cookbooks-skills-api-excel-pdf | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 18/20 | cookbooks-hosting-the-agent | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-data-analyst-managed-agent | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-slack-cma-bridge | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-knowledge-graph-construction | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-contextual-retrieval-rag | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-async-multi-agent-patterns | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-sre-cma-incident-responder | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 18/20 | cookbooks-self-hosted-sandboxes | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 17/20 | cookbooks-linear-cma-bridge | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 17/20 | cookbooks-cma-mcp-server | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 17/20 | cookbooks-threat-intel-agent | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 17/20 | cookbooks-tool-search-embeddings | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 17/20 | cookbooks-evaluator-optimizer-loop | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 17/20 | cookbooks-slack-data-bot | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 17/20 | anthropic-sdk-managed-agents-observe | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 34–49 |
| 16/20 | cookbooks-text-to-sql-progressive | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 50–61 |
| 16/20 | cookbooks-automatic-context-compaction | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 50–61 |
| 16/20 | cookbooks-usage-cost-admin-api | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 50–61 |
| 16/20 | agent-sdk-python-hooks-budget | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 50–61 |
| 16/20 | cookbooks-agents-mcp-tools-quickstart | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 50–61 |
| 15/20 | agent-sdk-demos-simple-chatapp | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 62–71 |

New skip entries (extend the skip table below):

| Folder | Reason |
|---|---|
| evals/advanced-ai-risk | Raw JSONL eval data — no build mechanics |
| evals/sycophancy | Raw JSONL eval data — no build mechanics |
| evals/persona | Raw JSONL eval data — no build mechanics |
| evals/winogenerated | Raw JSONL eval data — no build mechanics |
| claude-agent-sdk-demos/hello-world | TS hello-world quickstart — subsumed by agent-sdk-workshop-four-switches |
| claude-agent-sdk-demos/hello-world-v2 | V2 Session API stub — TS-only, under 50 lines of actual content |
| claude-cookbooks/patterns/agents/basic_workflows | Prompt-chaining/parallelization/routing basics — subsumed by async-multi-agent-patterns |
| claude-cookbooks/capabilities/classification | 70%→95% classifier guide — solid but subsumed by contextual-retrieval-rag and text-to-sql in terms of teachability tier |
| claude-cookbooks/capabilities/retrieval_augmented_generation | Basic RAG — superseded by contextual-retrieval-rag |
| claude-cookbooks/capabilities/summarization | Document summarization — below threshold for standalone video |
| claude-cookbooks/misc/read_web_pages_with_haiku | Web page summarizer — below threshold; no novel mechanics |
| claude-cookbooks/misc/how_to_enable_json_mode | JSON mode — subsumed by cookbooks-structured-json-tool-use |
| claude-cookbooks/misc/sampling_past_max_tokens | Prefill continuation hack — narrow use case, superseded by extended thinking |
| claude-cookbooks/misc/how_to_make_sql_queries | Basic SQL queries — superseded by cookbooks-text-to-sql-progressive |
| claude-cookbooks/misc/generate_test_cases | Synthetic test data generation — below threshold, no novel mechanics |
| claude-cookbooks/tool_evaluation | Multi-agent evaluation harness — narrow; subsumed by cookbooks-building-evals |
| claude-cookbooks/finetuning | Bedrock finetuning — Bedrock-specific, narrow audience |
| claude-cookbooks/coding/prompting_for_frontend_aesthetics | Prompting for better UI — below threshold; no build artifact |
| claude-cookbooks/skills/notebooks/02_skills_financial_applications | Extension of skills intro — dedupe; cookbooks-skills-api-excel-pdf covers the pattern |
| claude-cookbooks/skills/notebooks/03_skills_custom_development | Advanced skills — dedupe; cookbooks-skills-api-excel-pdf covers custom skill upload |
| claude-cookbooks/tool_use/tool_search_alternate_approaches | Describe-tool alternative — dedupe companion to cookbooks-tool-search-embeddings |
| claude-cookbooks/tool_use/vision_with_tools | Vision + tools — subsumed by courses-api-fundamentals-vision |
| anthropic-sdk-python/examples/managed-agents-self-hosted-sandbox-worker | TS self-hosted worker example — subsumed by cookbooks-self-hosted-sandboxes |
| anthropic-sdk-python/examples/managed-agents-streaming-deltas-manual | Streaming delta accumulation — subsumed by cookbooks-roadtrip-planner-multiagent |
| anthropic-sdk-python/examples/agents_comprehensive | Environments + vaults + MCP comprehensive example — strong but subsumed by cookbooks-roadtrip-planner-multiagent |
| agent-sdk-workshop/02-breakouts/account-intelligence | Workshop breakout — dedupe; agent-sdk-workshop-four-switches covers the workshop |
| agent-sdk-workshop/02-breakouts/sre-agent | Workshop breakout — dedupe; cookbooks-sre-incident-agent covers SRE |
| agent-sdk-workshop/02-breakouts/customer-support | Workshop breakout — dedupe; quickstarts-customer-support-agent covers the pattern |
| claude-cookbooks/managed_agents/sre_incident_responder.ipynb | Superseded by cookbooks-sre-cma-incident-responder which makes the CMA distinction |
| claude-agent-sdk-demos/excel-demo | Electron desktop app — narrow audience (desktop app builders); below threshold |

---

## Delta Pass — 2026-07-17

A follow-up scout of folders the comprehensive pass left uncarded and unskipped.
Four new cards (93 total); slot them into the ranked list by score as noted.

| Score | Slug | Bucket | Builder | Slots at |
|---|---|---|---|---|
| 19/20 | agent-sdk-workshop-four-switches | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 5–18 |
| 18/20 | skills-folder-of-instructions | BUILD-WITH-CLAUDE | claude-explainer | with ranks 19–33 |
| 18/20 | launch-your-agent-interview-to-agent | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 19–33 |
| 16/20 | skills-skill-creator-meta | BUILD-WITH-CLAUDE | terminal-screencast | with ranks 50–61 |

New skip entry (extends the skip table below):

| Folder | Reason |
|---|---|
| claude-agent-sdk-typescript | TS twin of the fully-carded python SDK; examples/ contains only session-stores — dedupe |

Notes: `skills/` and `evals/` also carry older per-repo `youtube/video-ideas.md`
files from a previous scout generation — superseded by these vids/ cards. The
algorithmic-art skill inside `skills/` already has a dedicated build prompt at
`brutalist-art/CLAUDE-CODE-ALGORITHMIC-ART-EXPLAINER.md` ("Claude, Seeded");
`skills-folder-of-instructions` is the umbrella video, kept distinct.

---

## Ranked Candidate List

| Rank | Score | Slug | Bucket | Builder |
|---|---|---|---|---|
| 1 | 20/20 | cookbooks-one-liner-research-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 2 | 20/20 | cwc-workshop-ship-first-managed-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 3 | 20/20 | cwc-workshop-research-desk-sec-agents | BUILD-WITH-CLAUDE | terminal-screencast |
| 4 | 20/20 | cwc-workshop-rightmodel-eval-sweep | BUILD-WITH-CLAUDE | terminal-screencast |
| 5 | 19/20 | sleeper-agents-safety-training-fails | RESEARCH/PAPERS | claude-explainer |
| 6 | 19/20 | sycophancy-to-subterfuge-reward-tampering | RESEARCH/PAPERS | claude-explainer |
| 7 | 19/20 | toy-models-superposition-features | INTERPRETABILITY/VISUAL-MATH | math-explainer (Manim) |
| 8 | 19/20 | cookbooks-memory-context-editing | BUILD-WITH-CLAUDE | terminal-screencast |
| 9 | 19/20 | cookbooks-mcp-observability-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 10 | 19/20 | cookbooks-sre-incident-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 11 | 19/20 | cookbooks-cma-human-in-the-loop | BUILD-WITH-CLAUDE | terminal-screencast |
| 12 | 19/20 | cookbooks-cma-outcomes-self-grader | BUILD-WITH-CLAUDE | terminal-screencast |
| 13 | 19/20 | cookbooks-cma-plan-big-execute-small | BUILD-WITH-CLAUDE | terminal-screencast |
| 14 | 19/20 | cookbooks-cma-agent-memory-store | BUILD-WITH-CLAUDE | terminal-screencast |
| 15 | 19/20 | cookbooks-cma-orchestrate-issue-to-pr | BUILD-WITH-CLAUDE | terminal-screencast |
| 16 | 19/20 | quickstarts-autonomous-coding-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 17 | 19/20 | cwc-workshop-agents-that-remember | BUILD-WITH-CLAUDE | terminal-screencast |
| 18 | 19/20 | cwc-workshop-how-we-claude-code | BUILD-WITH-CLAUDE | claude-explainer |
| 19 | 18/20 | claude-constitution-three-principals | RESEARCH/PAPERS | claude-explainer |
| 20 | 18/20 | attribution-graphs-circuit-tracing | INTERPRETABILITY/VISUAL-MATH | math-explainer + D3/DATAVIZ |
| 21 | 18/20 | cookbooks-prompt-caching | BUILD-WITH-CLAUDE | terminal-screencast |
| 22 | 18/20 | cookbooks-extended-thinking | BUILD-WITH-CLAUDE | terminal-screencast |
| 23 | 18/20 | cookbooks-citations-api | BUILD-WITH-CLAUDE | terminal-screencast |
| 24 | 18/20 | cookbooks-chief-of-staff-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 25 | 18/20 | cookbooks-migrate-openai-to-claude-sdk | BUILD-WITH-CLAUDE | terminal-screencast |
| 26 | 18/20 | cookbooks-cma-coordinate-specialist-team | BUILD-WITH-CLAUDE | terminal-screencast |
| 27 | 18/20 | cookbooks-cma-iterate-fix-tests | BUILD-WITH-CLAUDE | terminal-screencast |
| 28 | 18/20 | cookbooks-cma-production-vaults-mcp | BUILD-WITH-CLAUDE | terminal-screencast |
| 29 | 18/20 | quickstarts-computer-use-best-practices | BUILD-WITH-CLAUDE | claude-explainer |
| 30 | 18/20 | cwc-workshop-eval-driven-agent-dev | BUILD-WITH-CLAUDE | terminal-screencast |
| 31 | 18/20 | cwc-workshop-production-ready-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 32 | 18/20 | cwc-workshop-agent-decomposition | BUILD-WITH-CLAUDE | terminal-screencast |
| 33 | 18/20 | sdk-python-examples-managed-agents-dispatch | BUILD-WITH-CLAUDE | terminal-screencast |
| 34 | 17/20 | constitutional-ai-self-critique | RESEARCH/PAPERS | claude-explainer |
| 35 | 17/20 | rogue-deploy-eval-deception | RESEARCH/PAPERS | claude-explainer |
| 36 | 17/20 | claudes-c-compiler-ai-coding-limit | BUILD-WITH-CLAUDE | claude-explainer |
| 37 | 17/20 | long-running-agent-harness-pattern | BUILD-WITH-CLAUDE | terminal-screencast |
| 38 | 17/20 | prompt-engineering-precognition | BUILD-WITH-CLAUDE | claude-explainer |
| 39 | 17/20 | cookbooks-structured-json-tool-use | BUILD-WITH-CLAUDE | terminal-screencast |
| 40 | 17/20 | cookbooks-building-evals | BUILD-WITH-CLAUDE | terminal-screencast |
| 41 | 17/20 | cookbooks-vulnerability-detection-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 42 | 17/20 | cookbooks-speculative-prompt-caching | BUILD-WITH-CLAUDE | terminal-screencast |
| 43 | 17/20 | prompt-tutorial-lesson-04-separating-data | PROMPT-ENGINEERING | claude-explainer |
| 44 | 17/20 | prompt-tutorial-lesson-08-avoiding-hallucinations | PROMPT-ENGINEERING | claude-explainer |
| 45 | 17/20 | prompt-tutorial-appendix-tool-use | PROMPT-ENGINEERING | terminal-screencast |
| 46 | 17/20 | quickstarts-browser-use-demo | BUILD-WITH-CLAUDE | terminal-screencast |
| 47 | 17/20 | quickstarts-managed-agents-chat-sdk | BUILD-WITH-CLAUDE | terminal-screencast |
| 48 | 17/20 | agent-sdk-demos-ask-user-question-previews | BUILD-WITH-CLAUDE | terminal-screencast |
| 49 | 17/20 | cwc-workshop-agent-battle-minecraft | BUILD-WITH-CLAUDE | claude-explainer |
| 50 | 16/20 | claude-agent-sdk-multi-agent-pattern | BUILD-WITH-CLAUDE | terminal-screencast |
| 51 | 16/20 | claude-code-github-action | BUILD-WITH-CLAUDE | terminal-screencast |
| 52 | 16/20 | cookbooks-session-memory-compaction | BUILD-WITH-CLAUDE | terminal-screencast |
| 53 | 16/20 | cookbooks-parallel-tools-batch-wrapper | BUILD-WITH-CLAUDE | terminal-screencast |
| 54 | 16/20 | cookbooks-cma-prompt-versioning | BUILD-WITH-CLAUDE | terminal-screencast |
| 55 | 16/20 | cookbooks-cma-explore-unfamiliar-codebase | BUILD-WITH-CLAUDE | terminal-screencast |
| 56 | 16/20 | prompt-tutorial-lesson-06-precognition | PROMPT-ENGINEERING | claude-explainer |
| 57 | 16/20 | quickstarts-financial-data-analyst | BUILD-WITH-CLAUDE | terminal-screencast |
| 58 | 16/20 | courses-api-fundamentals-streaming | COURSES | terminal-screencast |
| 59 | 16/20 | courses-tool-use-complete-workflow | COURSES | terminal-screencast |
| 60 | 16/20 | courses-real-world-prompting-medical | COURSES | claude-explainer |
| 61 | 16/20 | courses-prompt-evals-model-graded | COURSES | terminal-screencast |
| 62 | 15/20 | html-as-claude-output-format | BUILD-WITH-CLAUDE | terminal-screencast |
| 63 | 15/20 | headvis-attention-head-explorer | BUILD-WITH-CLAUDE | terminal-screencast |
| 64 | 15/20 | political-neutrality-eval-paired-prompts | RESEARCH/PAPERS | claude-explainer |
| 65 | 15/20 | computer-use-tool-architecture | BUILD-WITH-CLAUDE | terminal-screencast |
| 66 | 15/20 | cookbooks-session-browser | BUILD-WITH-CLAUDE | terminal-screencast |
| 67 | 15/20 | cookbooks-metaprompt | BUILD-WITH-CLAUDE | claude-explainer |
| 68 | 15/20 | sdk-python-examples-agents-files | BUILD-WITH-CLAUDE | terminal-screencast |
| 69 | 15/20 | sdk-python-examples-thinking | BUILD-WITH-CLAUDE | terminal-screencast |
| 70 | 15/20 | sdk-python-examples-structured-outputs | BUILD-WITH-CLAUDE | terminal-screencast |
| 71 | 15/20 | cookbooks-pdf-upload | BUILD-WITH-CLAUDE | terminal-screencast |
| 72 | 14/20 | model-written-evals-sycophancy | RESEARCH/PAPERS | claude-explainer |
| 73 | 14/20 | hh-rlhf-preference-data-structure | RESEARCH/PAPERS | claude-explainer |
| 74 | 14/20 | cookbooks-batch-processing | BUILD-WITH-CLAUDE | terminal-screencast |
| 75 | 14/20 | prompt-tutorial-appendix-search-retrieval | PROMPT-ENGINEERING | terminal-screencast |
| 76 | 14/20 | agent-sdk-demos-research-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 77 | 14/20 | agent-sdk-demos-resume-generator | BUILD-WITH-CLAUDE | terminal-screencast |
| 78 | 14/20 | courses-api-fundamentals-vision | COURSES | terminal-screencast |
| 79 | 13/20 | cookbooks-moderation-filter | BUILD-WITH-CLAUDE | terminal-screencast |
| 80 | 13/20 | prompt-tutorial-lesson-01-basic-structure | PROMPT-ENGINEERING | terminal-screencast |
| 81 | 13/20 | prompt-tutorial-lesson-02-clear-and-direct | PROMPT-ENGINEERING | claude-explainer |
| 82 | 13/20 | prompt-tutorial-lesson-03-role-prompting | PROMPT-ENGINEERING | claude-explainer |
| 83 | 13/20 | prompt-tutorial-lesson-05-formatting-output | PROMPT-ENGINEERING | claude-explainer |
| 84 | 13/20 | prompt-tutorial-lesson-07-few-shot-prompting | PROMPT-ENGINEERING | claude-explainer |
| 85 | 13/20 | prompt-tutorial-appendix-prompt-chaining | PROMPT-ENGINEERING | terminal-screencast |
| 86 | 13/20 | quickstarts-customer-support-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 87 | 16/20 | sdk-python-examples-web-search | BUILD-WITH-CLAUDE | terminal-screencast |
| 88 | 12/20 | agent-sdk-demos-email-agent | BUILD-WITH-CLAUDE | terminal-screencast |
| 89 | 12/20 | jacobian-lens-residual-stream | INTERPRETABILITY/VISUAL-MATH | math-explainer (Manim) |

---

## Top 10 Quick List

1. **cookbooks-one-liner-research-agent** — Three lines of Claude Agent SDK code produce a working web-searching research agent. Score 20/20. Builder: terminal-screencast.
2. **cwc-workshop-ship-first-managed-agent** — Seven functions to a working SRE agent that names the commit behind a latency spike. Score 20/20. Builder: terminal-screencast.
3. **cwc-workshop-research-desk-sec-agents** — Fan-out/fan-in SEC research desk: one coordinator, parallel analyst agents per ticker, shared memory store, laptop-lid-closed scheduling. Score 20/20. Builder: terminal-screencast.
4. **cwc-workshop-rightmodel-eval-sweep** — Grid your task across models × thinking × effort; get three tradeoff plots and a quality-per-dollar recommendation. Score 20/20. Builder: terminal-screencast.
5. **cookbooks-memory-context-editing** — Claude 4's memory tool and context editing system: cross-session notes at `/memories/`, automatic tool-result pruning before overflow. Score 19/20. Builder: terminal-screencast.
6. **cookbooks-sre-incident-agent** — Agent greps 70k-line log, correlates timestamps with deploys, names the N+1 query commit — the 40-minute 3am hunt automated. Score 19/20. Builder: terminal-screencast.
7. **cookbooks-cma-human-in-the-loop** — Custom tools pause the Managed Agents session and emit an event your app handles — the seam where human approval takes over from the AI. Score 19/20. Builder: terminal-screencast.
8. **cookbooks-cma-outcomes-self-grader** — A second agent independently grades the writer's work against a rubric; the grader caught a press-release citation where a 10-K was required. Score 19/20. Builder: terminal-screencast.
9. **cwc-workshop-agents-that-remember** — Memory store + Dreaming Service transforms an amnesiac agent into a colleague that improves from its own experience. Score 19/20. Builder: terminal-screencast.
10. **cwc-workshop-how-we-claude-code** — Anthropic's own three-phase AI-assisted product workflow: brainstorm prompts → design mockups → verifiable component architecture. Score 19/20. Builder: claude-explainer.

---

## Bucket Routing Summary

### NEW: CLAUDE AGENT SDK / MANAGED AGENTS → terminal-screencast

This is the largest new bucket — Managed Agents and the Claude Agent SDK are the primary new API surface area and deserve a dedicated series.

**Cookbooks — claude_agent_sdk series (7 notebooks):**
- `cookbooks-one-liner-research-agent` — research agent in 3 lines
- `cookbooks-chief-of-staff-agent` — SDK feature parity with Claude Code; CLAUDE.md memory
- `cookbooks-mcp-observability-agent` — MCP as zero-code external system integration
- `cookbooks-sre-incident-agent` — SRE incident response agent
- `cookbooks-migrate-openai-to-claude-sdk` — OpenAI → Claude SDK migration map
- `cookbooks-session-browser` — session sidebar pattern (same code as Claude Code Desktop)
- `cookbooks-vulnerability-detection-agent` — security research agent

**Cookbooks — managed_agents series (10 notebooks):**
- `cookbooks-cma-iterate-fix-tests` — the entry-point: agent + environment + session
- `cookbooks-cma-human-in-the-loop` — custom tools as pause-and-hand-to-human
- `cookbooks-cma-explore-unfamiliar-codebase` — grounding over documentation
- `cookbooks-cma-orchestrate-issue-to-pr` — end-to-end bug fix with CI recovery
- `cookbooks-cma-operate-in-production` — Vaults, MCP toolsets, webhooks
- `cookbooks-cma-coordinate-specialist-team` — tool-scoping as correctness guarantee
- `cookbooks-cma-plan-big-execute-small` — coordinator + workers, 2.5x cheaper
- `cookbooks-cma-prompt-versioning` — server-side prompt versions, rollback by ID
- `cookbooks-cma-outcomes-self-grader` — second agent verifies first agent's work
- `cookbooks-cma-agent-memory-store` — per-user persistent memory stores

**CWC Workshops (7 workshops):**
- `cwc-workshop-ship-first-managed-agent` — 7 functions to a working SRE agent
- `cwc-workshop-eval-driven-agent-dev` — write the eval first, then the agent
- `cwc-workshop-agents-that-remember` — memory store + Dreaming Service
- `cwc-workshop-production-ready-agent` — complete multi-agent M&A research system
- `cwc-workshop-agent-decomposition` — decompose a 402-line prompt into Skills + subagents
- `cwc-workshop-how-we-claude-code` — Anthropic's own product workflow
- `cwc-workshop-research-desk-sec-agents` — fan-out SEC filing analyst fleet
- `cwc-workshop-rightmodel-eval-sweep` — model × thinking × effort grid
- `cwc-workshop-agent-battle-minecraft` — agent competition as prompt engineering sport

**Agent SDK Demos (4 demos):**
- `agent-sdk-demos-research-agent` — parallel subagent research with activity tracking
- `agent-sdk-demos-resume-generator` — research-then-format pattern in miniature
- `agent-sdk-demos-ask-user-question-previews` — HTML preview cards for AskUserQuestion
- `agent-sdk-demos-email-agent` — IMAP email assistant reference implementation

**Quickstarts (6 projects):**
- `quickstarts-autonomous-coding-agent` — git-as-checkpoint for multi-session coding
- `quickstarts-managed-agents-chat-sdk` — streaming chat + Managed Agents + multi-channel adapter
- `quickstarts-computer-use-best-practices` — demo → production gap for computer use
- `quickstarts-browser-use-demo` — Playwright-backed browser tool reference
- `quickstarts-financial-data-analyst` — natural language → chart generation
- `quickstarts-customer-support-agent` — knowledge base chatbot reference

**SDK Examples (5 examples):**
- `sdk-python-examples-managed-agents-dispatch` — worker fan-out dispatch pattern
- `sdk-python-examples-web-search` — built-in web search, zero infrastructure
- `sdk-python-examples-thinking` — budget_tokens as cost-accuracy knob
- `sdk-python-examples-structured-outputs` — `.parse()` → typed Pydantic model
- `sdk-python-examples-agents-files` — Files API + agent document processing

### NEW: COOKBOOKS — CORE API PATTERNS → terminal-screencast

- `cookbooks-prompt-caching` — 90% cost reduction with one `cache_control` field
- `cookbooks-extended-thinking` — visible chain of thought; thinking block anatomy
- `cookbooks-speculative-prompt-caching` — cache-warm during typing for zero TTFT
- `cookbooks-session-memory-compaction` — proactive compaction with background thread
- `cookbooks-structured-json-tool-use` — tool use as structured output guarantee
- `cookbooks-citations-api` — native citations with exact location pointers
- `cookbooks-parallel-tools-batch-wrapper` — batch meta-tool for forced parallel calls
- `cookbooks-building-evals` — code/model/human grading; use Claude to grade Claude
- `cookbooks-batch-processing` — Message Batches API, 50% cost reduction
- `cookbooks-metaprompt` — Claude generates your prompt template from a task description
- `cookbooks-pdf-upload` — native PDF document block, no parsing required
- `cookbooks-moderation-filter` — content moderation as a prompt, updatable in natural language
- `cookbooks-memory-context-editing` — memory tool + context editing (Claude 4 feature)

### NEW: PROMPT ENGINEERING TUTORIAL → claude-explainer

All 9 lessons + 3 appendices from `prompt-eng-interactive-tutorial/`:
- `prompt-tutorial-lesson-01-basic-structure` — messages array and role alternation
- `prompt-tutorial-lesson-02-clear-and-direct` — literal instruction following
- `prompt-tutorial-lesson-03-role-prompting` — vocabulary and caution calibration
- `prompt-tutorial-lesson-04-separating-data` — XML injection prevention (**highest priority**)
- `prompt-tutorial-lesson-05-formatting-output` — prefill and stop sequences
- `prompt-tutorial-lesson-06-precognition` — chain-of-thought via XML scratchpad
- `prompt-tutorial-lesson-07-few-shot-prompting` — implicit style encoding
- `prompt-tutorial-lesson-08-avoiding-hallucinations` — grounding as the fix (**second highest**)
- `prompt-tutorial-appendix-prompt-chaining` — auditability through decomposition
- `prompt-tutorial-appendix-tool-use` — four-message tool-use loop
- `prompt-tutorial-appendix-search-retrieval` — retrieval quality as the bottleneck

### NEW: COURSES → terminal-screencast / claude-explainer

- `courses-api-fundamentals-streaming` — non-streaming UX vs. streaming UX
- `courses-api-fundamentals-vision` — base64 image content block
- `courses-tool-use-complete-workflow` — the while-loop for multi-tool agent
- `courses-real-world-prompting-medical` — safety language calibration
- `courses-prompt-evals-model-graded` — Claude grades Claude; calibration against humans

### EXISTING: RESEARCH / PAPERS → claude-explainer

*(unchanged from original 19 cards)*
- `sleeper-agents-safety-training-fails`
- `sycophancy-to-subterfuge-reward-tampering`
- `toy-models-superposition-features`
- `claude-constitution-three-principals`
- `attribution-graphs-circuit-tracing`
- `constitutional-ai-self-critique`
- `rogue-deploy-eval-deception`
- `jacobian-lens-residual-stream`
- `political-neutrality-eval-paired-prompts`
- `model-written-evals-sycophancy`
- `hh-rlhf-preference-data-structure`
- `headvis-attention-head-explorer`
- `html-as-claude-output-format`
- `computer-use-tool-architecture`
- `claude-code-github-action`
- `long-running-agent-harness-pattern`
- `claude-agent-sdk-multi-agent-pattern`
- `claudes-c-compiler-ai-coding-limit`
- `prompt-engineering-precognition`

### SKIP — Pure infra / vendored deps / third-party (unchanged)

| Folder | Reason |
|---|---|
| httpcore | Anthropic fork of httpcore HTTP library — pure infra |
| hypercorn | ASGI server — vendored dep |
| orjson | Fast JSON library for Python — vendored dep |
| tokio | Rust async runtime — vendored dep |
| triton | OpenAI's GPU programming language — third-party |
| rclone | S3/GCS sync tool — infra |
| s5cmd | S3/GCS tool — infra |
| redis-py | Redis Python client — vendored dep |
| blobfile | Blob storage library — vendored dep |
| terragrunt | Terraform wrapper — third-party infra |
| argo-cd | GitOps CD tool — third-party infra |
| nix-eval-jobs | Nix evaluator — third-party infra |
| cargo-nix-plugin | Cargo workspace Nix plugin — third-party infra |
| swift-markdown | Apple's Swift Markdown parser — third-party |
| swift-markdown-ui | SwiftUI Markdown renderer — third-party |
| leptos-chartistry | Rust charting library — third-party |
| sse-starlette | SSE for Starlette/FastAPI — vendored dep |
| python-tblib | Python traceback serialization — vendored dep |
| riegeli-rs | Riegeli file format Rust library — vendored dep |
| beam | Apache Beam — third-party data processing |
| torchtyping | Deprecated; superceded by jaxtyping — third-party |
| cfaulthandler | C backtrace faulthandler — utility |
| buffa | Rust Protocol Buffers library — no teachable video idea |
| homebrew-claude | Homebrew tap stub — no content |
| homebrew-tap | Homebrew tap for Claude Code — install tooling |
| tailscale-hint-extension | Tailscale Chrome extension — internal tooling |
| scone-bench | DeFi smart contract exploit benchmark — crypto-specific |
| original_performance_takehome | CPU optimization benchmark — not a teachable video |
| maestro | Netflix workflow orchestrator (third-party) |
| repositories.json | JSON index of repos — not content |
| youtube-playlists.json | YouTube playlist JSON — not content |
| model-cards | Claude model cards — documentation only |
| PySvelte | Python-Svelte bridge — unsupported, no config.py |
| github-mcp-server | GitHub's own repo mirrored — no Anthropic teachable idea |
| claude-ai-mcp | Announcement/issue tracker — not content |
| claude-desktop-buddy | Maker project — very narrow audience |
| knowledge-work-plugins | Reference collection — index only |
| claude-plugins-community | Community plugin marketplace mirror — index only |
| claude-plugins-official | Anthropic's official plugin directory — index only |
| claude-tag-plugins | SaaS connector plugins — integrations index |
| healthcare | Claude for Healthcare plugin — vertical reference bundle |
| financial-services | Claude for Financial Services — vertical reference bundle |
| life-sciences | Life sciences MCP marketplace — marketplace index |
| claude-for-legal | Claude for Legal agents — vertical reference bundle |
| k12-teacher-skills | K-12 lesson planning — narrow educator audience |
| ClaudeForFoundationModels | Apple Foundation Models adapter — OS 27 beta only |
| devcontainer-features | Dev container — install tooling |
| claude-code-base-action | Mirror of claude-code-action — dedupe |
| claude-code-monitoring-guide | Reference guide — no mechanism to visualize |
| claude-code-security-review | Related to claude-code-action — dedupe |
| anthropic-sdk-go / java / ruby / php / csharp | Language SDKs — API surface docs |
| anthropic-tokenizer-typescript | Tokenizer utility library |
| anthropic-tools | Deprecated tools SDK |
| apitools | YouTube API tools — third-party utility |
| anthropic-cli | `ant` CLI — API surface docs |
| anthropic-retrieval-demo | Experimental/old — superseded |
| anthropic-bedrock-python | Deprecated (moved to SDK) |
| anthropic-bedrock-typescript | Deprecated |
| riv2025-long-horizon-coding-agent-demo | Archived, not maintained |
| defending-code-reference-harness | Security/enterprise vertical — narrow audience |
| DecompositionFaithfulnessPaper | Below threshold for teachable video |
| claude-code | The product itself — not a teachable mechanism |

---

## Counts

| Bucket | Count |
|---|---|
| RESEARCH / PAPERS candidates | 9 cards (unchanged) |
| INTERPRETABILITY / VISUAL-MATH candidates | 4 cards (unchanged) |
| BUILD-WITH-CLAUDE / SDK / TOOLS candidates (original) | 6 cards (unchanged) |
| **NEW: Claude Agent SDK / Managed Agents** | **31 cards** |
| **NEW: Cookbooks — Core API Patterns** | **13 cards** |
| **NEW: Prompt Engineering Tutorial** | **11 cards** |
| **NEW: Courses** | **5 cards** |
| **NEW: Quickstarts** | **6 cards** |
| **NEW: SDK Examples** | **5 cards** |
| SKIP (listed with reason) | ~57 folders |
| **Total candidate cards written** | **93** (89 + 4 delta 2026-07-17) |
| **New cards added this pass** | **70** |
| **Delta pass 2026-07-17** | **4 cards, 1 skip** |
| Folders drilled into comprehensively | **11 source folders** |
| **CLI-Scout pass 2026-07-24** | **28 new cards; total 122** |

---

## Source Folders Drilled Into for Comprehensive Coverage

1. `claude-cookbooks/claude_agent_sdk/` — 7 notebooks, 7 cards
2. `claude-cookbooks/managed_agents/` — 10 notebooks, 10 cards
3. `claude-cookbooks/misc/` — 12 notebooks, 8 cards
4. `claude-cookbooks/tool_use/` — 9 notebooks, 4 cards
5. `claude-cookbooks/extended_thinking/` — 2 notebooks, 1 card
6. `claude-cookbooks/multimodal/` — 7 notebooks, 0 new cards (subsumed by vision + sub-agents already covered)
7. `prompt-eng-interactive-tutorial/Anthropic 1P/` — 11 lessons + 3 appendices, 11 cards
8. `claude-quickstarts/` — 7 projects, 6 cards
9. `cwc-workshops/` — 8 workshops, 8 cards
10. `claude-agent-sdk-demos/` — 7 demos, 4 cards
11. `anthropic-sdk-python/examples/` and `anthropic-sdk-typescript/examples/` — 30+ examples, 5 cards
12. `courses/` — 4 sub-courses (16+ notebooks), 5 cards

---

## Channel routing summary

All cards default to **claude-liam** (Kokoro am_onyx, free pipeline, @NikBearBrown Teardown register).

The Managed Agents / Agent SDK cards form a natural series: build them in order from the entry-point cookbook outward. Suggest building the 20/20 cards first as hero episodes, then filling in supporting cards.

The prompt engineering tutorial lessons (scores 12–17) form a playlist for beginner-to-intermediate viewers; they should be built as a coherent numbered series under one playlist title.
