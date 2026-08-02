# INFO 7375: Branding and AI (Spring 2026) — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build an Archetype Classifier with Claude: Identify a Brand's Archetype from Its Public Signals

- Source: info-7375-branding-and-ai-spring-2026/chapters/03-jungian-brand-archetypes-as-a-system.md
- Lane: BUILD (Claude Code)
- Hook: A brand archetype is not a personality quiz — it is a consistency-enforcement device. The same brand that is an Explorer in product voice might be a Caregiver in customer service. The diagnostic reveals the drift.
- The artifact: a Python CLI tool that takes a brand name as input, prompts Claude to classify the brand's archetype across three signal domains (visual/verbal identity, product commitments, partnership choices), identifies contradictions across domains (e.g., Explorer visual but Caregiver tone), and outputs a structured archetype report with a consistency score (1–10). Rendered as an animated Manim score card.
- Prompt seed: `claude "You are a brand archetype analyst using the Mark-Pearson 12-archetype system (Hero, Outlaw, Magician, Sage, Explorer, Innocent, Ruler, Creator, Caregiver, Everyman, Lover, Jester). Analyze the brand [BRAND_NAME]. For each of three signal domains: (1) Visual/verbal identity — what archetype does the visual language, copy tone, and tagline signal? (2) Product commitments — what archetype do the product design decisions and feature priorities signal? (3) Partnership choices — what archetype do sponsorships, collaborations, and co-branding signal? For each domain: name the primary archetype, cite a specific brand signal as evidence, and state confidence level. Then: identify any archetype contradictions across domains. Output a JSON with fields: visual_archetype, product_archetype, partnership_archetype, contradictions (list), consistency_score (1-10), shadow_risk (which archetype failure mode is most likely given current drift)."`
- Read / check: Verify that the Mark-Pearson system is correctly cited (Margaret Mark and Carol Pearson, "The Hero and the Outlaw," McGraw-Hill, 2001) and that the 12 archetypes listed are from that system. Check that the "shadow" concept is correctly applied — each archetype's shadow is its specific failure mode, not a generic corruption. Watch for Claude conflating the Jungian psychological archetype with the brand archetype.
- Human supplies (Claude can't): The brand selection — the video demo uses a well-known consumer brand; the student applies to their own project brand. The signal evidence Claude cites should be verifiable; the student audits the citations before accepting.
- Output medium: Manim (a 3×3 grid: rows = signal domains, columns = archetype name / evidence / confidence; contradictions flash in orange; consistency score animates as a dial)
- The change: Run the same analysis on the student's own project brand from the course — compare their intended archetype (Chapter 2 audit) with what the classifier finds in their actual materials.
- Teardown angle: The classifier reveals the difference between the archetype you think you have and the archetype your signals actually communicate. The gap between intent and signal is the design problem.
- Exclusions: Jungian depth psychology, Myers-Briggs typology, genre/literary archetype systems.
- Score: 9/10

---

## Candidate 02 — Build a Color Palette Accessibility Checker with Claude: WCAG AA for Every Text Combination

- Source: info-7375-branding-and-ai-spring-2026/chapters/09-visual-identity-systems.md
- Lane: BUILD (Claude Code)
- Hook: A visually compelling palette that fails WCAG AA is a legal liability and an accessibility failure. Testing every text-on-background combination by hand takes hours. This does it in seconds — and animates which combinations pass and fail.
- The artifact: a Python script that takes a color palette (hex codes for primary, accent, and neutral colors), computes the WCAG 2.1 contrast ratio for every possible text-on-background combination using the relative luminance formula, and outputs a pass/fail matrix. Animated as a Manim grid where passing cells glow green and failing cells glow red, with the contrast ratio displayed in each cell.
- Prompt seed: `claude "Write a Python script that: (1) Takes a list of hex color codes as a palette (e.g., ['#1A1A2E', '#16213E', '#0F3460', '#E94560', '#FFFFFF']). (2) Computes the WCAG 2.1 relative luminance for each color using the formula: L = 0.2126*R + 0.7152*G + 0.0722*B (where R, G, B are linearized sRGB values). (3) Computes the contrast ratio between each pair: (L_lighter + 0.05) / (L_darker + 0.05). (4) Outputs a pass/fail matrix: WCAG AA requires contrast ≥ 4.5:1 for normal text, ≥ 3:1 for large text. (5) Also write a Manim scene that displays this matrix as a grid — green cells for pass (ratio shown), red for fail."`
- Read / check: Verify the relative luminance linearization: for sRGB values ≤ 0.03928, use value/12.92; otherwise use ((value+0.055)/1.055)^2.4. Verify WCAG AA thresholds: 4.5:1 for normal text, 3:1 for large text, 7:1 for AAA. Check a known pair (black on white = 21:1; white on mid-gray may be borderline) to validate the calculation.
- Human supplies (Claude can't): The specific palette hex codes — use the student's project palette or the vox palette from DESIGN.md for the demo. The calculation is fully automated; only the palette input requires a human decision.
- Output medium: Manim (n×n grid where n = number of palette colors; cells animate in with contrast ratio and pass/fail color; failing pairs flash briefly to draw attention)
- The change: Add a "fix suggestions" pass: for each failing pair, compute the minimum lightness adjustment to reach 4.5:1 and display the suggested corrected hex code.
- Teardown angle: WCAG compliance is not an accessibility checkbox — it is a signal-to-noise problem. Insufficient contrast isn't "subtle" — it is unreadable for roughly 8% of male users with color vision deficiency. The palette test is the first quality gate on any visual identity.
- Exclusions: Full WCAG 2.2 rule set (focus indicators, etc.), specific design software integration, color blindness simulation.
- Score: 9/10

---

## Candidate 03 — Build an n8n Workflow with Claude: Fetch-Transform-Store a Brand Signal Pipeline

- Source: info-7375-branding-and-ai-spring-2026/chapters/05-data-pipelines-and-workflow-automation.md
- Lane: BUILD (Claude Code)
- Hook: Every external dependency is a contract. Every contract will change. The Apollo/Reddit API collapse killed a thriving third-party app overnight — brand damage from a broken upstream contract. Build the pipeline with graceful degradation from the start.
- The artifact: a working n8n workflow (exported as JSON) that: (1) fires on a schedule (daily), (2) fetches brand mention data from a public API (Reddit search or similar, no auth required), (3) transforms the result (extracts mention count and top keywords using a Claude single-call step), (4) stores the output to a file or Google Sheet, (5) sends a Slack/email alert if the fetch fails (graceful degradation). The CLI session shows Claude generating the workflow JSON from a contracts-first specification.
- Prompt seed: `claude "Generate an n8n workflow JSON for a brand monitoring pipeline. The workflow: (1) Schedule trigger: daily at 8am. (2) HTTP Request node: GET 'https://www.reddit.com/search.json?q=[BRAND_NAME]&limit=25' (no auth required, Reddit public API). (3) Code node (JavaScript): parse the response, extract: post count, top 5 subreddits, top 3 most-upvoted post titles. Output as a JSON summary object. (4) Write to File node: append today's date and the summary to 'brand-mentions.jsonl'. (5) Error handler: if the HTTP node fails, send an email notification (stub the SMTP credentials as env vars). Document every external dependency as a contract: what it provides, failure mode, and degraded mode. Output as valid n8n workflow JSON."`
- Read / check: Verify the Reddit public search API endpoint is correct (reddit.com/search.json is a real public endpoint). Check that the Code node JavaScript correctly parses the Reddit API response structure (data.children array). Confirm the error handler is wired to the HTTP node (not just at the end of the workflow). Verify the SMTP credentials use n8n environment variable syntax.
- Human supplies (Claude can't): The brand name to monitor; n8n instance (local Docker or cloud — setup instructions in chapter prerequisites). The workflow JSON can be imported into any n8n instance; the human runs it and verifies the output file.
- Output medium: screen-recording mp4 (the Claude CLI session showing the workflow JSON being generated → the JSON imported into n8n UI → the workflow running → the brand-mentions.jsonl file appearing with today's data)
- The change: Add a second data source (e.g., Hacker News Algolia API, also public and no-auth) and show how the contracts document changes to reflect two upstream dependencies — and why having two independent sources reduces single-point-of-failure risk.
- Teardown angle: The pipeline is where products die — not from bad AI but from broken upstream contracts. Documenting every dependency as a contract and designing graceful degradation is not engineering overhead. It is brand architecture.
- Exclusions: n8n server administration, Kafka/stream processing, advanced ETL patterns.
- Score: 8/10

---

## Candidate 04 — Build a Multi-Agent Brand Research System with Claude: Orchestrator + Specialist Agents

- Source: info-7375-branding-and-ai-spring-2026/chapters/06-ai-intelligence-and-multiagent-systems.md
- Lane: BUILD (Claude Code)
- Hook: The hardest design decision in any agentic system is not which model to use — it is where the AI decides and where it does not. A multi-agent brand research system shows the four patterns of AI intelligence in one build.
- The artifact: a Python script (~60 lines) implementing a simple multi-agent brand research system using Claude: (1) Orchestrator agent receives the brand research task and breaks it into sub-tasks (competitor analysis, audience sentiment, archetype audit), (2) three specialist agents each handle one sub-task with a specific system prompt and structured output, (3) Orchestrator synthesizes the three outputs into a final research brief. The CLI shows the full agent chain running with step-ceiling enforcement (max 3 Claude calls per agent).
- Prompt seed: `claude "Write a Python script implementing a 3-agent brand research system using the Anthropic API (claude-sonnet-4-5 or equivalent). Architecture: (1) Orchestrator: receives brand name, sends one call to decompose the task into 3 sub-tasks (competitor landscape, audience sentiment signals, archetype consistency check). (2) Three specialist agents: each receives its sub-task + structured output format (JSON schema). Each agent is limited to 1 Claude call (step ceiling). (3) Synthesizer: receives the 3 JSON outputs, sends one final call to generate a 3-paragraph research brief. Total Claude calls: 1 + 3 + 1 = 5 maximum. Include anti-hallucination guard: each agent must include a 'confidence' field (High/Medium/Low) and a 'sources_cited' boolean. Print each agent's output before the final synthesis."`
- Read / check: Verify the step ceiling is enforced (each specialist gets exactly 1 call, not a loop). Check that the anti-hallucination guard (confidence + sources_cited) appears in the output schema for each agent. Confirm the synthesizer receives the full structured output, not just summaries. Watch for Claude omitting the orchestrator's decomposition step and jumping straight to the specialists.
- Human supplies (Claude can't): The Anthropic API key (set as environment variable); the brand name to research. The video demo uses a well-known consumer brand.
- Output medium: screen-recording mp4 (terminal showing the orchestrator decomposing the task → each specialist agent's JSON output appearing → the synthesizer's research brief appearing as the final output)
- The change: Stress-test the step ceiling by asking the orchestrator to handle a vague brand name — show how the system handles insufficient input without looping indefinitely (the orchestrator returns "task underspecified" after 1 call rather than retrying).
- Teardown angle: The architecture is a brand decision. A system with high autonomy (the AI decides what to research next) embeds your brand in the AI's reasoning failures. A system with deliberate orchestration (the human defines the sub-tasks, the AI executes them) keeps the creative and strategic judgment in the human layer.
- Exclusions: CrewAI/LangGraph framework deep-dives, model fine-tuning, vector database integration.
- Score: 8/10

---

## Candidate 05 — Build a Typography Pair Scorer with Claude: Rate Font Combinations Against Archetype Alignment

- Source: info-7375-branding-and-ai-spring-2026/chapters/09-visual-identity-systems.md
- Lane: BUILD (Claude Code)
- Hook: A Sage's typeface logic differs from a Hero's. The chapter specifies this but doesn't operationalize it. This tool takes a committed archetype and a candidate typeface pair, and scores the alignment — revealing the mismatch before the design is built.
- The artifact: a Python CLI tool that takes: (1) a committed brand archetype (from the 12-archetype system), (2) a display typeface name and a body typeface name. It sends a structured Claude prompt that scores each typeface against the archetype's visual personality attributes (e.g., Sage: analytical restraint, authority, legibility over flair; Hero: bold, decisive, strong contrast), returns a 1–10 alignment score for each face, identifies the combination's overall signal (coherent, contradictory, or neutral), and suggests one alternative pairing if the score is below 7.
- Prompt seed: `claude "You are a brand typography consultant using the Mark-Pearson 12-archetype system. The brand has committed to the [ARCHETYPE] archetype. Evaluate this typeface pair for archetype alignment: Display face: [DISPLAY_FONT], Body face: [BODY_FONT]. For each face: (1) describe its visual personality attributes (3 adjectives), (2) score its alignment with the [ARCHETYPE] archetype's visual commitments on a 1-10 scale, (3) cite one well-known brand that uses this face and its archetype. Then: (4) rate the combination's coherence (Coherent / Contradictory / Neutral), (5) if score below 7, suggest one alternative pairing that would score higher. Output as JSON with fields: display_score, body_score, combination_coherence, alternative_suggestion."`
- Read / check: Verify that the archetype-to-typography mapping is grounded in the chapter's principles (not invented by Claude). Check that the well-known brand citations are real (not hallucinated — the student should verify the brand-font-archetype claim). Confirm the alternative suggestion is a real available typeface (not a fictional name).
- Human supplies (Claude can't): The committed archetype and the candidate typeface names. The video demo uses a Hero archetype with contrasting type pairs (one well-aligned, one misaligned). Font knowledge must be verified by the student — Claude may hallucinate typeface attributes.
- Output medium: Manim (a 2-row table: display face and body face, each with a score bar animating to its value; a coherence verdict appearing at the bottom; the alternative suggestion fading in if the score is below 7)
- The change: Run the same scorer on three competing typeface pairs for the same archetype and produce a ranked shortlist — the tool as a design decision aid, not just an audit.
- Teardown angle: Typography alignment is not aesthetics — it is brand signal. A Sage brand with a Hero display face is communicating two contradictory things simultaneously. The customer resolves the contradiction by trusting neither.
- Exclusions: Font licensing and procurement, CSS font-stack implementation, web performance impact of typefaces.
- Score: 8/10

---

## Candidate 06 — Research the Pepsi Document: How a Visual Identity Without Strategy Produces the 27-Page Justification

- Source: info-7375-branding-and-ai-spring-2026/chapters/09-visual-identity-systems.md
- Lane: RESEARCH (Claude assistant)
- Hook: The "BreathTaking" document had to invoke the Mona Lisa and the gravitational field because there was nothing else to invoke. When visual work lacks strategic substance, the justification expands to fill the gap. Research the pattern and its prevention.
- The artifact: a sourced brief on the Pepsi 2009 redesign and the "BreathTaking" brand document: (1) what the document claimed, (2) why the design community's response was negative, (3) the structural problem — visual work done without committed brand strategy, (4) two additional historical cases of visual identity failures where the design lacked strategic grounding, (5) the prevention: what a creative brief must contain to prevent this.
- Prompt seed: `claude "Research the 2009 Pepsi logo redesign and the 'BreathTaking' brand identity document. Sections: (1) What the document claimed (design theory, Golden Ratio references, Earth's gravitational field — cite the document's actual claims). (2) Why the design community and public responded negatively — what specifically was lacking. (3) The structural problem: visual work done before or without committed brand strategy. (4) Two additional historical cases where a visual identity redesign failed due to the same structural problem (Gap 2010 logo, RadioShack rebrand, or equivalent). (5) What a creative brief must contain to prevent this: archetype alignment, tone words, useful and anti-references. Cite sources for each case."`
- Read / check: Verify the Pepsi "BreathTaking" document is a real artifact (it was widely circulated in 2009 — the document's existence is documented). Check that the Gap 2010 logo story is accurately cited (the revert happened within a week of the launch, October 2010). Confirm the structural problem framing matches the chapter's argument: design without strategy, not design without talent.
- Human supplies (Claude can't): The "BreathTaking" document itself (it circulated online in 2009 — the human should verify Claude's citations against the actual document or documented summaries). Expert design community review to validate the historical cases.
- Output medium: Manim (a timeline of redesign failures: Pepsi 2009 → Gap 2010 → each annotated with "missing ingredient" — the strategic commitment that was absent before the visual work began; the final panel shows the creative brief checklist that prevents each failure)
- The change: Apply the creative brief checklist to the student's own project brand — show what was (or wasn't) committed before the visual work began, and what the brief would have required.
- Teardown angle: The 27-page document is not the failure — it is the symptom. The failure happened weeks earlier when visual work began without a committed archetype, positioning statement, and creative brief. The document was written to justify a visual that had no brief to justify it.
- Exclusions: Pepsi product history, competitive cola market analysis, graphic design history at length.
- Score: 8/10

---

## Candidate 07 — Build a Brand Story Arc Auditor with Claude: Check Narrative Structure Against Archetype Commitments

- Source: info-7375-branding-and-ai-spring-2026/chapters/10-brand-storytelling.md
- Lane: BUILD (Claude Code)
- Hook: Every brand archetype commits to a specific story structure. The Hero archetype's story is always a challenge overcome. The Sage's story is always a truth revealed. A story arc that violates the archetype's structure undermines the brand consistency the archetype exists to enforce.
- The artifact: a Python CLI tool that takes: (1) committed archetype, (2) a brand story or About page text (pasted by the user). It sends to Claude a structured prompt that evaluates: does the story follow the archetype's canonical narrative arc? Does it reference the shadow (failure mode)? Does it establish who the Villain/Challenge/Problem is? Returns a structured audit with pass/fail per element and a one-sentence revision suggestion for each failing element.
- Prompt seed: `claude "You are a brand narrative auditor using the Mark-Pearson 12-archetype system. The brand has committed to the [ARCHETYPE] archetype. Audit this brand story for narrative structure alignment: [BRAND_STORY_TEXT]. Check for: (1) Does the story follow the [ARCHETYPE]'s canonical arc structure? (e.g., Hero: challenge → struggle → triumph; Sage: question → investigation → insight; Explorer: confinement → journey → discovery) (2) Does the story establish a clear antagonist/challenge/problem — the structural necessity for the archetype's role? (3) Does the story avoid the archetype's shadow (its specific failure mode)? (4) Is the brand's role consistent with what the archetype commits to? For each check: Pass/Fail, one specific quote from the text as evidence, and one revision suggestion if failing. Output as JSON."`
- Read / check: Verify that the canonical arc structures for each archetype are sourced from Mark-Pearson (not invented by Claude). Check that the shadow definitions are archetype-specific (not generic "corruption"). Confirm the tool's output includes a quote from the input text as evidence — this prevents Claude from hallucinating a fictional quote.
- Human supplies (Claude can't): The brand story text — this is the student's actual brand story from their course project. The video demo uses a sample About page. The student should audit Claude's failure identifications against their own read of the story.
- Output medium: screen-recording mp4 (the terminal showing the prompt → JSON audit output → the student seeing two "Fail" elements → applying the revision suggestions → re-running → both elements now "Pass")
- The change: Add a second pass where Claude rewrites one failing paragraph according to the revision suggestion — showing the before/after for one structural element.
- Teardown angle: A brand story that feels coherent but violates the archetype's canonical arc is storing up brand confusion. The customer doesn't consciously notice the structural violation — they just feel that the brand is inconsistent, and they stop trusting it.
- Exclusions: Screenplay structure beyond brand archetypes, Jungian narrative theory at length, specific copywriting formulas.
- Score: 7/10

---

## Candidate 08 — Build a Madison Brand Stack Generator with Claude: PRD → Pipeline → Agent Spec in One Session

- Source: info-7375-branding-and-ai-spring-2026/chapters/04-product-requirements-and-scope.md + 05-data-pipelines-and-workflow-automation.md + 06-ai-intelligence-and-multiagent-systems.md
- Lane: BUILD (Claude Code)
- Hook: The Madison sequence runs: archetype → PRD → pipeline → AI agent. Each step commits to constraints the next step must respect. A single session that generates all three in dependency order shows the whole design philosophy in 10 minutes.
- The artifact: a CLI session that, given a brand archetype and a one-sentence product idea, generates in sequence: (1) a Career PRD (Problem, User, Value Prop, Scope — what the tool does and explicitly does not do), (2) a pipeline contracts document (external dependencies, failure modes, degraded modes), (3) an agent specification (role, goal, tools, step ceiling, anti-hallucination guards). Each output depends on the prior step's decisions.
- Prompt seed: `claude "You are the Madison brand advisor. Given: Archetype: [ARCHETYPE], Product idea: [ONE_SENTENCE]. Generate in sequence (do not skip steps): (1) Career PRD: Problem (one sentence), User (specific, not 'everyone'), Value Proposition (what the tool uniquely provides given the archetype's commitments), Scope (three things it does; three things it explicitly does not do). (2) Pipeline Contracts: list the three most critical external dependencies the tool will require, with for each: what it provides, failure mode, degraded mode. (3) Agent Specification: role (one sentence), goal (what the agent achieves per invocation), allowed tools (list), step ceiling (max Claude calls per invocation), anti-hallucination guard (one structural rule). Format each section clearly. Each step must reference constraints from the prior step."`
- Read / check: Verify that the PRD's Scope section explicitly includes both what the tool does AND what it does not do (the "does not" list is load-bearing for the archetype's commitments). Check that the pipeline contracts document references the PRD's user and scope (not generic dependencies). Confirm the agent specification's step ceiling is a specific number (not "as needed").
- Human supplies (Claude can't): The archetype commitment (from their Chapter 3 work) and the one-sentence product idea. The student must review all three outputs before the next step — the tool generates them but the student owns the decisions.
- Output medium: screen-recording mp4 (terminal showing the three documents generating in sequence; each references the prior step; the student pauses between steps to review — the pause is visible in the recording)
- The change: Run a second session with the same archetype but a different product idea — show how the archetype constraint (what the brand commits to NOT do) changes the PRD's "does not" list even for unrelated products.
- Teardown angle: The Madison sequence is not a form to fill out. It is a dependency chain: the archetype constrains the PRD, the PRD constrains the pipeline, the pipeline constrains the agent. A student who skips to the agent without the PRD has built something that cannot be defended — because they never decided what it was for.
- Exclusions: Full course project submission, LMS grading rubric, specific platform deployment.
- Score: 9/10
