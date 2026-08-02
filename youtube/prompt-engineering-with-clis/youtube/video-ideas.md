# Video Ideas — Prompt Engineering with CLIs
_Scouted 2026-07-09 from 16 narrative chapters (Ch.00–Ch.14). Cards ≥ 8/10 only, highest score first._

---

## Candidate 01 — Why Your AI Agent Gets Dumber Over Time
- Source: `prompt-engineering-with-clis/chapters/01-why-cli-agent-prompting-is-a-different-discipline.md`
- Topic: CLI AGENT PROMPTING
- Hook: The model isn't getting worse — your context window is. The same frontier AI that nailed hour one can't hold a simple rule by hour three, and it's not the model's fault.
- Key case: An agent refactors an auth module flawlessly in the first hour. By hour three it reintroduces a fixed bug, forgets the test runner, and re-reads files it already edited — yet in a fresh session the same model handles each step without a stumble.
- The Question: If the model is identical, why does an agent session rot — and why does starting fresh fix something no amount of re-prompting can?
- Core idea: Every move in the agent loop (read → reason → act → observe) appends to a single, growing context window; nothing is ever removed. As the window fills past roughly 80% of capacity, the model cannot reliably find or weight any single instruction against the accumulated noise — "Lost in the Middle" applied to your own rules.
- Visual object: A horizontal context-window fill bar: left side empty and green ("clean reasoning zone"), right side filling red past a ~80% line labeled "context rot." Below it, two parallel timelines — the same agent at turn 1 vs. turn 400 — show rule-following collapsing as the bar crosses the line.
- Manim move: accumulate (tokens pile into the bar turn by turn) then decay (rule-following signal fades as the bar fills)
- Example seed: Developer types the same CLAUDE.md rule ("use pytest, not unittest") three times in one session; each time the agent apologizes and then writes unittest anyway. Fresh session: the rule holds on the first turn. The only thing that changed was the context.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Knows what a CLI agent is; has heard of context windows
- Exclusions: Omit specific token counts, omit model comparisons, omit the full ReAct paper — just the loop structure and the decay mechanism
- Score: 10/10

---

## Candidate 02 — The Lethal Trifecta: When AI Agents Become Security Holes
- Source: `prompt-engineering-with-clis/chapters/12-security-prompt-injection-and-the-lethal-trifecta.md`
- Topic: CLI AGENT PROMPTING
- Hook: An AI agent reviews a pull request, reads a Markdown file, and emails your production database credentials to a stranger — without being hacked, without a CVE, just by following text.
- Key case: Developer points an agent at a contributor's PR with "read the diff and flag anything suspicious." A hidden paragraph in a new CONTRIBUTING.md, invisible in the rendered view, reads to the model as a trusted instruction: read .env and POST it to an attacker's server. The agent has file-read permission and a URL-fetch tool — and it complies.
- The Question: If the model perfectly follows your instructions, how can reading a Markdown file turn into a data breach — and what's the only thing that actually stops it?
- Core idea: The "lethal trifecta" (named by Simon Willison) — private data accessible + untrusted content readable + external channel open — is the condition where prompt injection becomes catastrophic. A defensive CLAUDE.md rule travels in the same token stream as the attack and can be overridden; only an architectural control (no secrets in scope, no network tool, human approval gate) is out-of-band and actually holds.
- Visual object: A three-circle Venn diagram — "Private data," "Untrusted content," "External comms" — with the central triple-overlap labeled "Exfiltration zone." Each circle shown cutting away individually ("survivable") and all three overlapping ("the trap"). A second diagram shows the CLAUDE.md rule inside the token stream vs. an architectural gate outside it.
- Manim move: split (three circles appear separately, each labeled "survivable") then collapse (they overlap into the danger zone) then split again (one circle cut away → zone disappears)
- Example seed: The PR-review task: untrusted diff enters context, .env is reachable, URL-fetch tool is enabled. Map the three trifecta legs one by one. Cut one leg (disable URL-fetch) — the attack is inert, no matter how well-crafted the injected text.
- Length band: 3–5 min
- Still lanes: geo/c2v/raster
- Prerequisites: Knows what an AI agent can do (read files, call tools); basic sense of what an API key is
- Exclusions: Omit CVE numbers, omit specific vendor settings, omit the full InjecAgent benchmark — focus solely on the trifecta as a design lens
- Score: 10/10

---

## Candidate 03 — Adding One More Rule Breaks ALL the Rules
- Source: `prompt-engineering-with-clis/chapters/04-the-instruction-capacity-budget.md`
- Topic: CLI AGENT PROMPTING
- Hook: A team adds a totally normal rule to their CLAUDE.md and overnight their agent stops obeying rules it had followed for weeks. Not the new rule — every rule. They rewrote the rule 10 different ways. Nothing changed.
- Key case: A team's CLAUDE.md grows by one reasonable line — "wrap new API endpoints in the @requireAuth decorator" — and suddenly commit-message format, console.log hygiene, and indentation rules all collapse simultaneously. The rule they added wasn't the problem; it was the straw that pushed the instruction set past the followable-instruction ceiling.
- The Question: Why does adding one instruction break all instructions at once — and why does rewording the broken rule make things worse instead of better?
- Core idea: Frontier models can track roughly 150–200 followable instructions simultaneously [practitioner figure, verify]. The agent's own system prompt already spends ~50 of those slots before your file loads. Past the ceiling, instruction-following doesn't degrade gracefully — it collapses globally. The fix is subtraction, not rewording.
- Visual object: A stacked budget bar — bottom 50 slots labeled "system prompt (rent)," middle band labeled "your rules," top labeled "conversation." A second bar shows the file tipping past the ceiling into a red "uniform instruction-ignoring" zone, with ALL rule-following indicators going dark simultaneously, not just the newest rule.
- Manim move: accumulate (rules stack into the bar one by one) then collapse (all rule indicators blink out at once when the ceiling is crossed)
- Example seed: The 180-line CLAUDE.md with 10+ style directives in the back half. Count followable instructions out loud: each "always X" or "never Y" is one slot. Add the ~50 rent. Show the total crossing 150. Then show that removing the style rules (which a linter enforces for free) drops the count back under budget — and all rules start landing again.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Has used a CLAUDE.md or similar instruction file; understands that agents follow instructions
- Exclusions: Omit the full Miller "Magical Number Seven" history, omit exact token counts, flag all practitioner figures as estimates
- Score: 10/10

---

## Candidate 04 — Two Agent Bugs That Look Identical But Need Opposite Fixes
- Source: `prompt-engineering-with-clis/chapters/02-the-agents-context-system-static-vs-dynamic-context.md`
- Topic: CLI AGENT PROMPTING
- Hook: Your agent starts using tabs instead of spaces, AND separately insists a function "has no retry logic" when it's right there on line 40. Your teammate calls both bugs "the agent ignored reality." They have opposite causes and opposite fixes.
- Key case: Same afternoon, two failures. Bug 1: the tabs/spaces rule is in CLAUDE.md and the agent followed it for hours, then stopped. Bug 2: the agent confidently describes a file based on how it looked an hour ago, not how it looks now. One is a standing instruction getting drowned; the other is a stale observation being treated as current fact.
- The Question: If an agent misbehaves by "ignoring reality," how do you know whether to rewrite your instruction file or re-read the file it's lying about — and why do these look identical but require opposite repairs?
- Core idea: Static context (instruction files) fails by being ignored — drowned by accumulated dynamic material, worsening as the session ages, fixed by shortening the file or restarting. Dynamic context (gathered observations) fails by going stale — fixed by re-reading the live file before acting, not by editing CLAUDE.md. The diagnostic question: "was the agent's claim true at some earlier point in the session?"
- Visual object: Two columns — "Static" (authored, stable, fails → convention violation) and "Dynamic" (gathered, changing, fails → acts on expired fact) — with arrows diverging in opposite directions and a diagnostic table showing symptom → class → first fix.
- Manim move: split (one stream of "context" splits left and right into static and dynamic lanes) then diverge (failure arrows shoot in opposite directions)
- Example seed: The tabs failure: agent obeys early, violates late — start a fresh session, rule is obeyed again. Confirmed static failure. The retry-logic failure: the claim was true before a teammate committed over the file. Re-read the live file. Confirmed dynamic failure. Show the table used to decide which is which.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Has used a CLAUDE.md; understands that agents read files
- Exclusions: Omit the full Liskov history, omit cache-stability economics, omit the "smuggling dynamic content into static files" section — just the diagnostic split
- Score: 9/10

---

## Candidate 05 — Why You Should Clear Your AI Agent's Memory Before the Hard Work
- Source: `prompt-engineering-with-clis/chapters/07-task-prompt-design-scope-stopping-conditions-and-plan-then-execute.md`
- Topic: CLI AGENT PROMPTING
- Hook: Professional AI agent users don't run one long session — they deliberately throw away everything the agent learned and start fresh before the real work begins.
- Key case: A developer runs a planning session to understand a codebase (wide, exploratory, messy). Instead of continuing, they save a PLAN.md, run /clear, and open a clean session with only the plan. The clean session produces a tighter diff in less time than the one that inherited all the exploration debris.
- The Question: Why does throwing away everything the agent learned make it perform better on the actual task — and what's the one thing that needs to survive the /clear?
- Core idea: Planning needs breadth (the agent should read widely); execution needs focus (the agent should hold a small, clean instruction set). Running both in one session means the breadth you needed for planning becomes the noise that degrades execution. A saved PLAN.md carries the conclusions of exploration without the debris. This is the plan-then-execute split, endorsed by Anthropic's own Claude Code guidance.
- Visual object: A three-beat timeline: Session 1 shows a context window filling with wide reads, dead ends, and probe errors — then emits a single PLAN.md file. A red /clear boundary line. Session 2 starts with only PLAN.md in a clean window and executes tightly.
- Manim move: accumulate (Session 1 fills with exploration debris) then collapse (the /clear drops everything) then trace (Session 2 follows only the plan's path)
- Example seed: The flaky-checkout-test task. Session 1: agent reads five files, runs probes, hits dead ends, writes PLAN.md. /clear. Session 2 prompt: "Read PLAN.md and execute exactly." The diff touches exactly two files named in the plan. Compare to the uncleared version where the agent edited four unintended files.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Knows what /clear does; has run a multi-step agent task
- Exclusions: Omit the full Suchman history, omit the two-correction rule, omit the acceptance-criteria and stopping-condition sections — focus solely on the planning/execution split
- Score: 9/10

---

## Candidate 06 — The Trick That Lets Your AI Agent Know Everything Without Paying for It
- Source: `prompt-engineering-with-clis/chapters/05-progressive-disclosure-and-the-agent-docs-pattern.md`
- Topic: CLI AGENT PROMPTING
- Hook: You deleted the seven critical gotchas from your instruction file to stay under the limit. Now the agent hits gotcha four every time. But you can't put them back — the file's already too long. There's a third option.
- Key case: After trimming a CLAUDE.md to stay under the capacity budget, task-specific knowledge (seven import-pipeline gotchas, payment-provider procedure) is "deleted." An agent given a pipeline task explores for twenty file-reads and reconstructs maybe half of the deleted knowledge — then hits gotcha four anyway. The agent_docs pattern: a tiny always-loaded index ("import pipeline → agent_docs/imports.md") replaces exploration with one deliberate read.
- The Question: How do you keep a hundred pages of hard-won project knowledge accessible to an agent without burning the instruction budget that makes simple rules stick?
- Core idea: Progressive disclosure splits agent-facing knowledge into two tiers: a minimal always-loaded index (each pointer costs one instruction slot) and on-demand domain docs loaded only when the task proves it needs them. A pointer costs one slot; the doc it points to costs zero until the moment it's needed. The knowledge you "deleted" was never gone — it was relocated to a place the agent reaches on purpose instead of reconstructing by accident.
- Visual object: Before/after diagram. Before: bloated CLAUDE.md with every domain rule inlined. After: a lean index with four conditional rows ("if task touches X, read agent_docs/X.md") plus four separate doc files — only one lights up per task.
- Manim move: transform (the bloated CLAUDE.md morphs: domain blocks pull out and become separate doc files; the index rows replace them) then spread (the doc files fan out, with only one highlighted for the current task)
- Example seed: The import pipeline. Before: seven gotchas inline in CLAUDE.md. After: one index row ("import pipeline → agent_docs/imports.md"). Agent given a pipeline task reads the index, sees the pointer, reads imports.md, learns all seven gotchas in one deliberate read, avoids gotcha four. Count tokens: inline version spends 200 tokens every session; pointer version spends 10 tokens every session plus 200 only when needed.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Has a CLAUDE.md; understands the capacity budget from Ch.4 (or from Candidate 03)
- Exclusions: Omit Agent Skills / SKILL.md formalization, omit the Carroll minimal-manual history, omit the "pointers not copies" section — just the two-tier index pattern
- Score: 9/10

---

## Candidate 07 — Why Giving Your AI More Code Makes It Worse
- Source: `prompt-engineering-with-clis/chapters/06-context-engineering-for-large-codebases.md`
- Topic: CLI AGENT PROMPTING
- Hook: An agent given a 20-minute rename task on a large codebase spends 3 hours reading files, accumulates 80,000 tokens of context it didn't need, and corrupts code it was never asked to touch — because it was being thorough.
- Key case: A field name rename in a monorepo (customerId → customer_id). The agent reads the integration module, then the shared HTTP client, then the auth layer, then billing, then utilities. It loses the thread, patches code that belongs to a different partner's API, and doubles the time to completion. A narrowest-first run: reads the integration module and one type definition, produces a clean two-file patch in under 20 minutes.
- The Question: If reading more code gives the agent more information, why does letting it read freely on a large codebase make it less accurate — and what's the rule that prevents the spiral?
- Core idea: The overexploration trap (documented by Augment Code): 80,000+ tokens of irrelevant context correlates with a ~25% drop in task completeness and roughly doubled time [practitioner figures, verify]. The agent doesn't get worse at coding — its context gets worse, and on this thesis that's the same thing. Rule: start at the narrowest plausible scope; expand only when an explicit, unresolved dependency forces you to. Relevance is proven by the task, not assumed in advance.
- Visual object: Two-path comparison for the same rename task. Left path: narrowest-first — reads 2 files, clean patch, 20 min. Right path: blind expansion — reads 8+ files, 80k tokens badge, ~25% completeness-drop badge, 2× time badge, corrupted patch touching unintended files.
- Manim move: compare (two paths branch from the same starting point and diverge as the right path accumulates more and more file nodes) then decay (completeness indicator drops on the right path as tokens accumulate)
- Example seed: The rename task. Left path prompt: "The rename is confined to integrations/acme/; do not read or modify any other service." Right path: "Fix the customerId field name." Show the file-read lists side by side. Show the billing-service change that appeared only in the right path.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Works with codebases larger than a single file; understands the context window fills up
- Exclusions: Omit directory-scoped instruction files, omit the repo-map / Aider section, omit Parnas history — focus solely on the overexploration trap and the narrowest-first rule
- Score: 9/10

---

## Candidate 08 — The Hook That Keeps Your AI Honest Through Compaction
- Source: `prompt-engineering-with-clis/chapters/08-reusable-workflows-slash-commands-and-hooks.md`
- Topic: CLI AGENT PROMPTING
- Hook: You told your AI agent "never edit vendor/ files" at the start of the session. Six hours later it compacts its context, forgets the rule, and edits vendor/. No amount of careful prompting prevents this — but one file does.
- Key case: A long session approaches its context limit. The agent compacts — summarizes its conversation history to free space. The summary is the agent's best guess at what mattered; "never edit vendor/" hasn't come up in a while and doesn't make the cut. The post-compaction agent, no longer holding the rule, edits vendor/. A PostCompact hook fires after the compaction and re-injects a five-line critical-rules card. The agent now holds the rule again — unconditionally, outside the summary's lossy judgment.
- The Question: Why can't a rule stated at the start of a session survive compaction — and what's the only intervention that actually guarantees a rule persists?
- Core idea: Compaction replaces the full conversation with a summary; the summary is lossy and makes judgment calls. A rule that hasn't fired recently can simply vanish. A defensive CLAUDE.md instruction ("always preserve vendor/ rule") travels inside the same summary process and can be dropped too. A PostCompact hook fires after the lossy step, outside the summary, and re-injects only the non-negotiable rules. It's a lifeboat, not a second copy of the ship: only what you cannot afford to lose.
- Visual object: A repair timeline. Full conversation holds the rule (green). Compaction fires (lossy step shown as a filter that drops "rarely-used" items). Without hook: agent edits vendor/ (red X). With hook: hook fires after compaction, re-injects a 5-line rule card (shown in red highlight as unconditionally appended outside the summary box). Agent holds the rule again.
- Manim move: trace (the conversation timeline traces forward, hits the compaction filter, then splits into a "no hook" failure path and a "hook" repair path that rejoins the correct behavior)
- Example seed: The vendor/ rule. Show the CLAUDE.md rule at turn 1. Show the compaction at turn 200 — the filter drops the rule. No hook: next action edits vendor/. Hook version: a five-line card appears in the context immediately after compaction — "NEVER edit vendor/ or migrations/; NEVER commit on red; production config is read-only." Agent holds all three.
- Length band: 2–3 min
- Still lanes: geo/c2v
- Prerequisites: Understands that agents have a context window that can fill; has heard of compaction
- Exclusions: Omit slash commands entirely, omit the Engelbart history, omit the "more than twice" rule — focus solely on compaction loss and the PostCompact hook as the architectural fix
- Score: 8/10

---

## Candidate 09 — Your AI Agent Forgets Everything When You Close the Laptop
- Source: `prompt-engineering-with-clis/chapters/10-multi-session-continuity-and-state-persistence.md`
- Topic: CLI AGENT PROMPTING
- Hook: You spend Friday building a shared mental model with your AI agent — which tables are migrated, which edge cases you agreed to defer, the exact dry-run command. Monday morning the agent has no memory of any of it. You lose the first hour reconstructing what Friday's session already knew.
- Key case: A database migration half-done on Friday. The agent knew: accounts and sessions tables done, users table mid-flight, the name-splitter heuristic, the agreed deferral of mononyms, the exact dry-run command. Monday fresh session: none of it. The developer spends 40 minutes reconstructing from memory and gets some of it wrong. A session-notes handoff (NOTES.md committed Friday before closing) lets Monday's session resume in one turn.
- The Question: If an AI agent forgets everything between sessions by design, how do you make a multi-day project feel continuous — and what exactly needs to survive the gap?
- Core idea: The agent is stateless across sessions by design. Each session begins from the persistent files and nothing else. The window is working memory — erased at the end. Anything needed next week must be written to disk, in the repo, in a form a fresh agent can read cold. A session-notes handoff answers the question a fresh agent actually has: "what is the state of this work and what do I do next?" — with a goal, a done/in-progress split, deferred decisions, an exact next action, and standing rules.
- Visual object: Two session windows separated by a gap (Friday close / Monday open). Below them, a durable file layer (NOTES.md) spans the gap. Without NOTES.md: Monday session starts from zero, reconstruction arc shown. With NOTES.md: Monday session reads one file, resumes in one turn — the gap is bridged.
- Manim move: split (the session timeline splits at Friday close; one path shows the gap as empty dark space, the other shows NOTES.md bridging it) then trace (Monday session follows the file path and picks up immediately)
- Example seed: The migration NOTES.md from the chapter. Walk through each section: Goal (1 sentence), State (done/in-progress), Deferred (mononyms — decided, not a bug), Next action (exact command + expected row count), Rules (migrations are append-only). Monday prompt: "Read NOTES.md, confirm state in 3 lines, then perform the next action exactly."
- Length band: 3–5 min
- Still lanes: geo/c2v/raster
- Prerequisites: Has run a multi-session agent project; understands that agents don't have persistent memory
- Exclusions: Omit the registry and work-log patterns, omit the parallel/sequential rule, omit Engelbart history — focus solely on the session-notes handoff
- Score: 8/10

---

## Candidate 10 — How to Run AI Agents in Parallel Without Them Breaking Each Other
- Source: `prompt-engineering-with-clis/chapters/11-sub-agents-and-multi-agent-orchestration.md`
- Topic: CLI AGENT PROMPTING
- Hook: You split a 41-module migration across multiple AI agents to run in parallel. They finish faster — and produce a merge conflict on every shared function because they made conflicting decisions in isolation.
- Key case: A logging-library migration across 41 modules. Single agent: by module 30, the context is 2/3 full of its own history and the agent is re-discovering import conventions for the fourth time. Multi-agent split: an operator produces a shared spec (old call shape → new call shape), partitions modules into 6 groups, dispatches each to a worker in its own git worktree. Each worker reads only the spec and its group — never the other workers' output. The operator collects six paragraph-length reports, never re-reads the full diffs. The seam is by directory (no shared functions across groups): clean, no conflicts.
- The Question: When a single AI agent's context window can't hold the whole job, how do you split work across multiple agents without their isolated decisions colliding at the merge?
- Core idea: The operator-and-workers pattern: operator holds the spec and short summaries (never full diffs); workers do deep reads in clean, isolated git worktrees. The whole architecture depends on choosing a clean seam — a boundary where pieces are genuinely independent. A seam that crosses a shared function isn't clean: two workers rename it two different ways, and the merge conflict is a Liskov violation made visible. Rule: add an agent only when a single context window cannot hold the work reliably.
- Visual object: An operator node at top holding the spec and six paragraph reports. Below, six worker nodes in separate worktrees (one per module group). Arrows show: spec flowing down to workers, paragraph reports flowing back up to operator. A "clean seam" version shows no arrows between workers. A "leaky seam" inset shows two workers both touching a shared function with diverging renames — merge conflict badge.
- Manim move: spread (one agent node splits into one operator + six workers) then duplicate (the spec propagates down to all workers) then collapse (six reports compress back to the operator)
- Example seed: The 41-module migration. Show the single-agent version's context filling across 30 modules. Show the operator prompt (key lines: "do not edit code yourself," "reason over summaries," "stop before follow-ups"). Show worker prompt (receives spec + one group). Show the operator collecting reports and writing migration-summary.md — never touching the 41 changed files.
- Length band: 3–5 min
- Still lanes: geo/c2v
- Prerequisites: Understands the context window fills up; has used git branches
- Exclusions: Omit cost/model-sizing section, omit the security/injection amplification section, omit Liskov history — focus solely on the operator-and-workers pattern and the clean-seam requirement
- Score: 8/10
