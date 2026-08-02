# AI Sherpa — CLI Video Ideas ("X with Claude")

> Note: ai-sherpa's chapter content (Chapter 1) is a placeholder — "[CHAPTER 1 CONTENT PLACEHOLDER]".
> The frontmatter establishes the book as "AI Sherpa" by Nik Bear Brown, Bear Brown LLC.
> Cards are derived from the book's title concept: AI as a guide/navigation tool, the metaphor of
> having an experienced guide who knows the terrain. All cards are BUILD lane (the title implies
> tooling/navigation — a technical guidance assistant).

## Candidate 01 — "Build a Claude-Powered Project Navigator with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (title/concept)
- Lane: BUILD (Claude Code)
- Hook: A sherpa doesn't carry you — they know the terrain so you can make the decisions that matter. That's the exact role Claude should play in a project workflow.
- The artifact: A Python script that takes a project description and generates a structured navigation plan: (1) the terrain map (what is known, what is uncertain, what is unknown-unknown), (2) the first three decision points where human judgment is required, (3) the AI-handleable scouting tasks that can run in parallel, (4) the first checkpoint where the human must review before proceeding. Displayed as an animated Manim flowchart.
- Prompt seed: `claude "You are an AI sherpa for a project. Given this project description, generate a navigation plan: (1) TERRAIN MAP — what is well-understood (safe to delegate), what is uncertain (needs human judgment at handoff), what is unknown (requires discovery first). (2) FIRST THREE DECISION POINTS — where human judgment is irreplaceable. (3) SCOUTING TASKS — AI-handleable reconnaissance that runs in parallel to decision-making. (4) FIRST CHECKPOINT — what the human reviews before proceeding. Format as a structured navigation document."`
- Read / check: Verify the terrain map produces a meaningful split (not everything in "uncertain"). Confirm the decision points name judgment calls (not tasks). Check the scouting tasks are genuinely parallelizable with the decision-making.
- Human supplies (Claude can't): The project description — must be specific enough that the terrain map is non-trivial. The video uses a synthetic project (building a research report, launching a product feature, or planning an event). Synthetic is fully acceptable.
- Output medium: Manim (animated flowchart building: terrain map → decision points → scouting tasks → checkpoint)
- The change: Run the navigation plan for a second, more ambiguous project — show how the terrain map changes when unknowns dominate, and how the sherpa role shifts toward reconnaissance over direction.
- Teardown angle: The sherpa metaphor names the right relationship — the guide knows the terrain and carries the load; the climber makes the decisions that matter. Confusing these roles is how projects get lost.
- Exclusions: Don't go into project management methodology in depth; don't build a full PM tool; don't cover team coordination.
- Score: 8/10

---

## Candidate 02 — "Map Your AI Blind Spots with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (title/concept — navigation implies knowing where the map ends)
- Lane: BUILD (Claude Code)
- Hook: Every map has edges. The sherpa who doesn't know where their map ends is the most dangerous guide on the mountain.
- The artifact: A Python script that takes any domain (e.g., real estate, medicine, education, finance) and generates a structured blind-spot map for AI in that domain: (1) where AI has excellent coverage (trained on abundant data), (2) where AI has thin coverage (sparse in training corpus), (3) where AI has confident-wrong coverage (abundant but systematically biased data), (4) where AI has structural absence (things that cannot be in any corpus). Displayed as a Manim four-zone map.
- Prompt seed: `claude "Generate an AI blind-spot map for the domain of [EDUCATION]. Identify: (1) EXCELLENT COVERAGE — where AI has trained on abundant, high-quality data (what Claude does well here), (2) THIN COVERAGE — where training data is sparse or low-quality (where Claude hedges), (3) CONFIDENT-WRONG — where abundant data is systematically biased (where Claude sounds authoritative but reflects historical errors), (4) STRUCTURAL ABSENCE — what cannot be in any corpus (lived experience, real-time local knowledge, tacit expertise). Cite the mechanism for each zone."`
- Read / check: Verify the "confident-wrong" zone names a specific mechanism (not just "bias" — name what kind of bias and why). Confirm the "structural absence" zone includes things that are genuinely impossible to corpus-capture (not just hard to find). Check that the domain-specific examples are plausible.
- Human supplies (Claude can't): Nothing — fully synthetic. The domain choice drives the specificity; any plausible domain works. Domain expertise to validate the blind-spot examples is required for a real use case but not for the demo video.
- Output medium: Manim (animated four-zone map, zones appearing in sequence)
- The change: Ask Claude to generate a "navigation rule" for each zone — how should you adjust your use of AI when you're operating in each zone? Show the rules as a decision tree.
- Teardown angle: The sherpa metaphor is about knowing where the trail is marked and where it isn't. The blind-spot map makes the unmapped terrain visible before you walk into it.
- Exclusions: Don't go into AI technical architecture; don't cover specific model benchmarks; don't build a comprehensive AI audit tool.
- Score: 8/10

---

## Candidate 03 — "Build a Prompt Specification Protocol with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (concept: guidance before execution)
- Lane: BUILD (Claude Code)
- Hook: A sherpa briefs you before you leave base camp — not after you're lost. The prompt spec is the briefing.
- The artifact: A Python script that takes a vague request and transforms it into a structured prompt specification: (1) the goal (what success looks like in one sentence), (2) the constraints (what the output may and may not do), (3) the context (what Claude needs to know that isn't obvious), (4) the verification step (how the human will check the output), (5) the scope exclusions (what to cut if uncertain). Then runs the specification through Claude and compares the output against the spec.
- Prompt seed: `claude "I want to transform a vague request into a structured prompt specification. For this request: [REQUEST], generate: (1) GOAL — what success looks like in one sentence, (2) CONSTRAINTS — three specific things the output must do and two it must not do, (3) CONTEXT — what Claude needs to know that isn't in the request, (4) VERIFICATION — how the human will check the output, (5) SCOPE EXCLUSIONS — what to cut if uncertain. Then generate the output using the specification, and score it against the spec."`
- Read / check: Verify the five-field specification is specific enough to be falsifiable (not "produce a good document"). Confirm the verification step is a concrete check. Check that the scope exclusions prevent common scope creep for the vague request type.
- Human supplies (Claude can't): A genuinely vague request to specify — use a common one from professional practice (e.g., "summarize this report," "write a proposal," "analyze this data"). Synthetic is fully acceptable.
- Output medium: screen-recording mp4 (terminal showing the spec being built, then the output running, then the verification check)
- The change: Run the same vague request without the specification — show how the unspecified output diverges from what the spec would have produced, and mark the gap.
- Teardown angle: The sherpa briefs you before you leave. The prompt spec is the briefing — it converts a vague intention into a navigable route before Claude starts generating.
- Exclusions: Don't go into prompt engineering theory in depth; don't cover system prompts or multi-turn conversations; don't build a full prompt library.
- Score: 8/10

---

## Candidate 04 — "Generate a Decision Tree for When to Use AI with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (concept: navigation guidance for AI use)
- Lane: BUILD (Claude Code)
- Hook: The sherpa's most important skill isn't knowing the path — it's knowing when the path is wrong and turning back before it's too late.
- The artifact: A Python script that generates a decision tree for any professional domain: given a task, should you use AI? The tree branches on: (1) is the output verifiable without domain expertise? (2) does the task require specific local knowledge? (3) will the output be used to make a consequential decision? (4) is the error mode silent or visible? Displayed as an animated Manim decision tree.
- Prompt seed: `claude "Build a decision tree for when to use AI assistance in [PROFESSIONAL DOMAIN]. The tree should branch on four questions: (1) Is the output verifiable without deep domain expertise (YES → AI safe, NO → proceed with caution), (2) Does the task require specific local or contextual knowledge (YES → AI will miss it, NO → AI may handle it), (3) Will this output drive a consequential decision (YES → human must own, NO → AI first draft acceptable), (4) Is the error mode silent (looks correct when wrong) or visible (clearly wrong when wrong) (SILENT → mandatory human review, VISIBLE → review recommended). Output as a formatted decision tree."`
- Read / check: Verify the four branching questions are independent (not just variations of the same question). Confirm the tree produces distinct outcomes for common task types (some tasks should clearly reach "AI safe," some clearly "human required"). Check that the "silent error" branch correctly identifies the highest-risk category.
- Human supplies (Claude can't): The professional domain — the video uses a worked example (financial analysis, medical documentation, or legal research). Synthetic domain is fully acceptable.
- Output medium: Manim (animated decision tree building branch by branch, with task examples appearing at each terminal node)
- The change: Apply the decision tree to five real tasks from the chosen domain — show the tree routing each one and highlight any surprising classifications.
- Teardown angle: The sherpa's judgment is knowing when not to proceed. The decision tree makes that judgment explicit — so the agent can run it automatically instead of improvising under deadline pressure.
- Exclusions: Don't attempt to be comprehensive across all professional domains; don't go into AI safety in depth; don't cover organizational governance.
- Score: 7/10

---

## Candidate 05 — "Build a Context-Loading Protocol for Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (concept: preparing the guide before the expedition)
- Lane: BUILD (Claude Code)
- Hook: A sherpa who doesn't know the client's fitness level, equipment, or target summit gives generic advice that could get someone killed. Context loading is how you turn Claude from a generic advisor into a specific guide.
- The artifact: A Python script that generates a context-loading document for any professional task: (1) the task statement (precise), (2) the professional context (role, industry, constraints), (3) the project history (what's already been decided), (4) the audience context (who reads the output and what they know), (5) the verification criteria (how success is measured). Outputs a formatted system-prompt template the user pastes before their first Claude message.
- Prompt seed: `claude "Generate a context-loading document for this professional task: [TASK]. The document will be pasted as context before I ask Claude for help. Include: (1) TASK STATEMENT — the precise goal in one sentence, (2) PROFESSIONAL CONTEXT — my role, industry, and key constraints, (3) PROJECT HISTORY — what has already been decided that Claude should not re-open, (4) AUDIENCE CONTEXT — who reads this output and what they already know, (5) VERIFICATION CRITERIA — how I will check the output. Format as a pasteable context block."`
- Read / check: Verify the context-loading document is specific enough to change Claude's output (not just generic role-play). Confirm the "project history" field prevents Claude from re-recommending already-rejected options. Check the verification criteria are concrete.
- Human supplies (Claude can't): The professional task and context — these must be specific to produce a useful demo. The video uses a worked example (a strategic memo, a research brief, or a design specification). Synthetic is fully acceptable.
- Output medium: screen-recording mp4 (terminal showing the context-loading document being generated, then pasted into a Claude conversation, then the improved output compared to a no-context version)
- The change: Run the same task with and without the context-loading document — display both outputs side by side and mark where the context-loaded version avoids the common failure modes.
- Teardown angle: The sherpa knows your fitness level, your gear, and your goal before you start. Context loading is how you give Claude that briefing — and it's the single most effective way to improve output quality without changing the model.
- Exclusions: Don't go into system prompt engineering for API access; don't cover multi-turn conversation management; don't build a full context library.
- Score: 7/10

---

## Candidate 06 — "Research What Makes a Good AI Guide: The Sherpa Literature with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (concept: the guidance metaphor grounded in evidence)
- Lane: RESEARCH (Claude assistant)
- Hook: The sherpa metaphor isn't just poetic — it names a specific relationship between human expertise and navigational assistance that has been studied in instructional design, clinical decision support, and expert systems research.
- The artifact: A sourced research brief on the conditions that make AI guidance effective: (1) the guide-as-instrument vs guide-as-oracle distinction (from decision support research), (2) the conditions under which guidance increases calibration vs overconfidence (from cognitive psychology), (3) one documented failure of AI guidance where users deferred to the AI past the point of their own expertise. Displayed as a three-panel Manim comparison.
- Prompt seed: `claude "Research the conditions that make AI guidance effective vs counterproductive. Find: (1) the guide-as-instrument vs guide-as-oracle distinction in clinical decision support or expert systems research — what makes the difference, (2) research on when AI assistance increases human calibration vs when it induces automation bias/overconfidence, (3) one documented case where AI guidance led professionals to defer past their own expertise. Cite sources and distinguish well-evidenced from speculative claims."`
- Read / check: Verify that at least one cited source is peer-reviewed. Confirm the automation bias citation is accurate (there is substantial research on this — check that Claude doesn't confabulate a specific study). Check that the "documented failure" case is real and accurately described.
- Human supplies (Claude can't): Verification of specific citations — Claude may cite automation bias studies inaccurately. Human must confirm at least two sources exist and describe what the abstracts claim.
- Output medium: Manim (animated three-panel comparison: guide-as-instrument / calibration conditions / documented failure)
- The change: Ask Claude to derive three design principles for AI guidance tools from the research — what would a well-designed AI sherpa do differently than a standard chatbot?
- Teardown angle: The sherpa metaphor is grounded — there's research on what effective guidance looks like. The design principles aren't aesthetic choices; they're evidence-based distinctions that separate useful guides from dangerous oracles.
- Exclusions: Don't go into AI safety research in depth; don't cover specific products; don't review the full automation bias literature.
- Score: 7/10

---

## Candidate 07 — "Build a Terrain-Scanning Protocol for Unknown AI Territory with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (concept: scouting before committing)
- Lane: BUILD (Claude Code)
- Hook: Before committing to a route, the sherpa scouts. Before committing to an AI output in unfamiliar territory, the professional scans.
- The artifact: A Python script that implements a terrain-scanning protocol for any new AI task: (1) run three short test prompts on the same task to probe Claude's consistency, (2) check for confidence language ("certainly," "clearly," "always") that may signal overreach, (3) identify any specific claims that would require domain expertise to verify, (4) produce a "terrain report" summarizing: safe zones, uncertain zones, verify-before-proceeding zones. Displayed as a terminal screen-recording showing the protocol running.
- Prompt seed: `claude "I am going to run a terrain-scanning protocol on this AI task: [TASK]. Step 1: Generate three responses to the same core question using slightly different framings. Step 2: Identify any claims that use high-confidence language ('certainly,' 'always,' 'clearly,' 'definitively') — flag these for verification. Step 3: List every specific claim that requires domain expertise to verify (not just factual lookup). Step 4: Produce a terrain report: SAFE ZONES (output is reliable), UNCERTAIN ZONES (needs human review), VERIFY-BEFORE-PROCEEDING (requires expert confirmation)."`
- Read / check: Verify the three response variants are actually different (not just paraphrases). Confirm the confidence-language scanner catches at least one instance. Check the terrain report has a meaningful three-zone split.
- Human supplies (Claude can't): The task to scan — the video uses a professional domain where AI is known to have uneven coverage (medical information, legal advice, financial projections). Synthetic is fully acceptable.
- Output medium: screen-recording mp4 (live terminal showing the three-probe run, then the terrain report appearing)
- The change: Run the same protocol on a task where Claude has excellent, consistent coverage — show that the terrain report comes back mostly SAFE, demonstrating that the protocol is calibrating, not paranoid.
- Teardown angle: The sherpa scans before committing. The terrain-scanning protocol takes five minutes and tells you whether you're on a well-marked trail or heading into improvised territory.
- Exclusions: Don't go into AI red-teaming in depth; don't build a comprehensive prompt testing framework; don't cover adversarial prompting.
- Score: 7/10

---

## Candidate 08 — "Generate a Learning Expedition Plan with Claude"
- Source: ai-sherpa/chapters/00-frontmatter.md (concept: guided learning as navigation)
- Lane: BUILD (Claude Code)
- Hook: The sherpa doesn't just lead — they teach. Every expedition is also a learning expedition for the climber. Claude can serve the same role if the plan is built right.
- The artifact: A Python script that generates a learning expedition plan for any topic: (1) base camp (what the learner must know before starting), (2) waypoints (three milestone concepts that mark progress), (3) summit conditions (what the learner can do at the end that they couldn't at the start), (4) altitude sickness markers (common misconceptions that signal the learner is off-route), (5) the sherpa's role at each stage (what Claude handles, what the learner must work through alone). Displayed as a Manim-animated expedition map.
- Prompt seed: `claude "Generate a learning expedition plan for mastering [TOPIC]. Include: (1) BASE CAMP — three prerequisite concepts the learner must have before starting, (2) WAYPOINTS — three milestone concepts that mark meaningful progress (with one verifiable checkpoint per waypoint), (3) SUMMIT CONDITIONS — what the learner can do at the end that they couldn't do at the start (stated as a performance, not a fact), (4) ALTITUDE SICKNESS MARKERS — three common misconceptions that signal the learner is off-route, (5) SHERPA'S ROLE — for each stage, what Claude handles vs what the learner must work through alone."`
- Read / check: Verify the summit conditions are stated as a performance (not "understands X" — "can do X in context Y"). Confirm the altitude sickness markers are specific misconceptions, not just "misunderstanding the concept." Check that the sherpa's role at each stage includes at least one "learner must work through alone" item.
- Human supplies (Claude can't): The learning topic — must be specific enough that the waypoints are non-trivial. The video uses a worked example (probability, machine learning, contract law, or a programming language). Synthetic is fully acceptable.
- Output medium: Manim (animated expedition map building: base camp → waypoints → summit → sickness markers → role assignments)
- The change: Apply the expedition plan to a learner who has already reached the first waypoint — show how the sherpa's role shifts as the learner's capability increases.
- Teardown angle: The learning expedition metaphor names the right relationship: the guide knows the terrain, the learner does the climbing. The plan is the route; the verification checkpoints are where you know you're on course.
- Exclusions: Don't build a full tutoring system; don't cover specific EdTech tools; don't go into curriculum design methodology.
- Score: 7/10
