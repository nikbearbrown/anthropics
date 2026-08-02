# AI for Designers: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Fluency Trap Detector: Catch Polish That Conceals Bad Thinking with Claude

- Source: ai-for-designers/chapters/03-the-fluency-trap.md
- Lane: BUILD (Claude Code)
- Hook: The concept deck looked perfect. Clean hierarchy, confident language, tight layout. It was also wrong. Processing fluency had suppressed the scrutiny that would have caught it. The tool produced the polish before the thinking was done.
- The artifact: A screen-recording of Claude receiving two design concept descriptions — one genuinely strong, one fluent but hollow — and running a seven-pattern fluency trap audit: (1) confident language without evidence, (2) solution before problem definition, (3) aesthetic coherence substituting for logical coherence, (4) specificity theater (false precision), (5) completeness illusion (no gaps visible), (6) borrowed authority (best practices cited without fit), (7) polish-before-pedagogy (artifact finished, assumption untested). Claude outputs a markdown table: Pattern | Present / Absent | Evidence from the brief. A Manim animation renders the seven-pattern radar chart — one polygon per concept, showing where each is strong and where it fails.
- Prompt seed: `claude "Audit these two design concept briefs for fluency trap patterns. For each brief, check for: (1) confident language without supporting evidence; (2) solution framing before problem definition; (3) aesthetic coherence substituting for logical coherence; (4) specificity theater — false precision; (5) completeness illusion — no gaps visible; (6) borrowed authority — 'best practice' cited without fit evidence; (7) polish-before-pedagogy — artifact appears finished but pedagogical assumptions are untested. Output a table: Pattern | Brief A (Present/Absent) | Brief B (Present/Absent) | Evidence. Then flag which brief is more dangerous: the one that looks worse or the one that looks better? [paste two briefs]"`
- Read / check: Verify all seven patterns appear as rows in the output table. Confirm the "more dangerous" judgment targets the fluent-but-hollow brief (the chapter's central argument). Check that the Manim radar chart polygons are labeled and the axis names are legible at video resolution.
- Human supplies: Two synthetic design concept briefs — one genuinely strong (problem-first, evidence-cited, assumptions named), one fluent but hollow (confident language, no evidence, solution-first). A designer can supply a real brief from their practice with identifying details changed.
- Output medium: screen-recording mp4 (terminal session) + Manim (seven-pattern radar chart animation)
- The change: Add a third prompt: "Rewrite the hollow brief to eliminate all seven trap patterns without changing the core design direction." Show the before/after comparison — same concept, different epistemic quality. Label the difference: "same direction, different confidence level."
- Teardown angle: The trap is that fluent output suppresses evaluative scrutiny. The audit does not make design better — it makes the assumptions visible before the polish makes them invisible. Surface coherence is not evidence that the thinking worked.
- Exclusions: Cut neuroscience processing-fluency literature detail; cut all seven traps as a standalone list; cut advertising/branding examples that diverge from the design workflow context.
- Score: 9/10

---

## Candidate 02 — Build the IP Clearance Checklist: Run Your AI-Generated Assets Through the Risk Screen with Claude

- Source: ai-for-designers/chapters/04-ip-and-copyright.md
- Lane: BUILD (Claude Code)
- Hook: The image generator produced a logo that looked original. It was trained on copyrighted work. Your client signed off. The liability question is not about the tool — it is about whose name is on the deliverable.
- The artifact: A screen-recording of Claude receiving a list of AI-generated design assets (description of images, fonts, patterns, UI components) and running them through a five-criteria IP risk screen: (1) training data provenance — is the generator's training corpus documented and licensed?; (2) style specificity — does the output closely imitate an identifiable artist or work?; (3) commercial use rights — does the platform license cover commercial client delivery?; (4) jurisdiction gap — does the use cross jurisdictions with different AI-copyright treatment?; (5) client disclosure obligation — does the contract or client expectation require disclosure of AI generation? Claude outputs a risk table: Asset | Criterion | Risk Level (High/Medium/Low) | Recommended Action. A D3 v7 standalone HTML renders the risk matrix as a heat map — assets on one axis, criteria on the other, color-coded cells.
- Prompt seed: `claude "I've used AI image generation tools to produce these design assets for a client project: [list assets with brief description and tool used]. Run each asset through a five-criteria IP risk screen: (1) training data provenance — is the tool's training corpus documented and rights-cleared for commercial use?; (2) style specificity — does this output closely imitate an identifiable artist, brand, or copyrighted work?; (3) commercial license scope — does the platform's terms explicitly cover commercial client delivery?; (4) jurisdiction gap — are there AI-copyright differences between my jurisdiction and the client's?; (5) client disclosure — does my contract or client expectation require AI use disclosure? Output: Asset | Criterion | Risk Level | Recommended Action."`
- Read / check: Verify the five criteria cover all four dimensions from the chapter (training, style, commercial rights, disclosure). Confirm High-risk items generate a specific "Recommended Action" (not "consult a lawyer" alone but the specific action — disclose, replace, obtain license, verify terms). Check that the D3 heat map cell colors map correctly to the risk levels.
- Human supplies: A list of 5–8 synthetic asset descriptions (logo concept, icon set, background illustration, UI pattern, font pairing) with tool names (Midjourney, DALL-E, Adobe Firefly, Stable Diffusion). Real-data upgrade: a designer runs their own recent project's asset list.
- Output medium: screen-recording mp4 (terminal) + D3 heat map (screen-recorded browser interaction)
- The change: Add a "safe harbor" column to the table — for each High-risk asset, name one specific platform or alternative that would clear the same risk category. Show how the asset list changes when the high-risk tools are replaced.
- Teardown angle: The platform's terms of service do not transfer liability to the platform. The client relationship, the contract, and the professional deliverable create the designer's exposure. The risk screen is not about which tools to avoid — it is about what the designer is accountable for when the asset ships.
- Exclusions: Cut the EU AI Act compliance pathway beyond one sentence; cut the Stability AI litigation history; cut the academic copyright theory beyond what's needed for the checklist logic.
- Score: 9/10

---

## Candidate 03 — Build the AI+1 Audit: Score Your Own Workflow Against the Four-Skill Framework with Claude

- Source: ai-for-designers/chapters/01-the-ai-plus-one-designer.md
- Lane: BUILD (Claude Code)
- Hook: Design expertise. Client knowledge. AI fluency. Accountability. The AI+1 designer has all four. The designer who has only AI fluency has a dangerous gap — and the gap is invisible until the client's institutional context makes the output wrong.
- The artifact: A D3 v7 standalone HTML file rendering an interactive self-assessment radar chart with four axes: Design Expertise (craft, judgment, systems thinking), Client Knowledge (institutional context, relationship depth, tacit domain knowledge), AI Fluency (prompt engineering, tool selection, output evaluation), Accountability (signature, professional standing, liability acceptance). The user inputs a score 1–5 on each axis via sliders. The radar polygon redraws live. A "gap alert" triggers when any axis scores below 3: "This gap changes what you can safely delegate." Screen-recorded with a designer filling in the scores and following the gap-alert logic.
- Prompt seed: `claude "Build a self-contained D3 v7 HTML file that renders an interactive four-axis radar chart for the AI+1 designer self-assessment. Axes: Design Expertise, Client Knowledge, AI Fluency, Accountability. Each axis has a slider (1–5). The radar polygon redraws on slider change. Below the chart: a gap alert panel that fires when any axis drops below 3, naming the specific delegation risk for that axis — e.g., 'Client Knowledge below 3: AI output will miss institutional context your client expects you to supply.' Color: polygon fills yellow for any axis below 3, red below 2. Inline CSS and D3 7.9.0 from cdnjs."`
- Read / check: Verify all four axes appear with correct names. Confirm the gap-alert panel fires at the correct threshold and names the correct delegation risk for each axis. Check that the radar redraws correctly as sliders move — no rendering artifacts.
- Human supplies: Nothing — fully synthetic interaction. Real-data upgrade: a designer scores their own workflow and the gap alert generates a personal delegation policy.
- Output medium: screen-recording mp4 (browser interaction of D3 radar with live slider updates and gap alerts)
- The change: Add a fifth axis — "Practice Investment" (hours per week of unassisted design work). Show how the gap alert changes when Practice Investment is low even if the other four are high: "This is the axis that sustains the others over time."
- Teardown angle: AI fluency without design expertise produces confident output with no judgment. The "+1" is not a modifier — it is the condition that makes the AI useful rather than dangerous. The radar shows which skill is the constraint.
- Exclusions: Cut the salary/market comparison table; cut the "future of design work" projection; cut vendor tool recommendations.
- Score: 9/10

---

## Candidate 04 — Build the Client Disclosure Generator: Draft a Transparent AI Use Statement for Your Next Project with Claude

- Source: ai-for-designers/chapters/05-client-disclosure.md
- Lane: BUILD (Claude Code)
- Hook: Most designers either say nothing about AI use or say everything — and both are wrong. The disclosure that protects the relationship names what was generated, what was human-authored, and what the client owns.
- The artifact: A screen-recording of Claude receiving a project description (type, scope, deliverables, AI tools used) and generating a three-tier disclosure statement: Tier 1 (contract language — what the designer represents about AI use); Tier 2 (project memo language — what the client sees in the kick-off document); Tier 3 (asset-level annotation — how individual deliverables label their AI-assisted components). Claude outputs all three tiers as formatted text. A second prompt asks Claude to stress-test the disclosure: "What does this statement not cover — what could a client reasonably claim they were not told?"
- Prompt seed: `claude "I'm a designer preparing client disclosure for a brand identity project. Scope: logo, color system, typography pairing, icon set. AI tools used: Midjourney for concept exploration (not final output), Claude for naming ideation, Adobe Firefly for texture generation (used in final deliverables). Generate a three-tier AI use disclosure: Tier 1 — contract clause (formal, legal-adjacent language representing what I warrant about AI use); Tier 2 — project memo paragraph (plain language for the client kick-off document); Tier 3 — asset annotation format (brief label for each AI-assisted deliverable in the final handoff). Then: what does this disclosure not cover — what reasonable client claim would this language fail to address?"`
- Read / check: Verify Tier 1 uses warranting language, not aspirational language. Confirm Tier 3 asset annotations are deliverable-specific, not generic. Check that the stress-test identifies at least one real gap the designer should address before finalizing.
- Human supplies: A project description with tool names (the synthetic brand identity case is the stand-in). Real-data upgrade: a designer runs their own active project through the disclosure generator.
- Output medium: screen-recording mp4 (terminal session showing the three-tier build and stress-test)
- The change: Show a third prompt: "Revise the disclosure to close the gap you identified." Display the before/after Tier 1 clause side by side. Label the change with one sentence: "This is the sentence your contract was missing."
- Teardown angle: The disclosure is not about protecting the designer from the client. It is about creating the shared understanding that makes the work defensible. Undisclosed AI use is not just an ethics question — it is a contract question.
- Exclusions: Cut the academic integrity parallel to student work; cut jurisdiction-by-jurisdiction disclosure law survey; cut advertising standards specific to print/broadcast.
- Score: 8/10

---

## Candidate 05 — Build the Design Brief Expander: Turn a One-Sentence Client Ask into a Full Four-Component Prompt with Claude

- Source: ai-for-designers/chapters/02-production-tasks.md
- Lane: BUILD (Claude Code)
- Hook: The client said "make it feel premium." That is not a brief. The model will produce a confident, generic output from a vague input — and the designer will spend three rounds correcting it back toward what "premium" means for this client, this audience, and this brand history.
- The artifact: A screen-recording of two Claude API calls running in sequence. Call 1: the vague client ask passed directly to the generation prompt. Call 2: the same ask expanded through a four-component brief builder (role: designer with stated expertise; context: client category, audience, brand history, constraints; task: specific design output with format and scope; constraints: what to avoid, what to preserve). Both outputs display side by side. A D3 v7 comparison table animates below — row by row: Specificity, Brand fit, Revision likelihood, Actionability.
- Prompt seed: `claude "A client brief says: 'We need a landing page hero section that feels premium for our fintech app.' That is the entire brief. Step 1: Call the generation model with just that sentence and show the output. Step 2: Expand the brief using four components — Role (UX designer specializing in fintech, 8 years), Context (B2B payments app, enterprise clients 35–55, dark/navy brand palette, competitor Stripe's minimalism as reference), Task (hero section layout: headline, subheadline, CTA, one supporting visual — describe in detail), Constraints (no stock photo people, no green, respect existing brand system, accessibility AA minimum). Now call the generation model with the expanded brief. Compare the two outputs in a table: Specificity | Brand fit | Revision likelihood | Actionability."`
- Read / check: Verify the two outputs are genuinely different — the expanded brief should produce a more specific, brand-aligned result. Confirm the comparison table dimensions map to real design review criteria, not generic "quality" labels. Check that the side-by-side format is legible in screen recording.
- Human supplies: Claude API key (or Claude.ai session). The fintech brief is synthetic; a real designer can substitute their own current client brief.
- Output medium: screen-recording mp4 (terminal showing both API calls + D3 comparison table)
- The change: Add a third round — the designer spots one weakness in the expanded-brief output (e.g., the CTA language is too generic) and adds a single constraint to the prompt. Show the output improve in one round. Label: "The third round is where the client knowledge enters."
- Teardown angle: The model is a probability distribution conditioned on the prompt. A vague brief requests the average output. The average is never right for a specific client. The brief expansion is the mechanism by which the designer's knowledge enters the generation.
- Exclusions: Cut tool-comparison table (Claude vs. ChatGPT vs. Gemini); cut prompt library advice; cut the research on prompt engineering techniques.
- Score: 8/10

---

## Candidate 06 — Build the Taste Calibration Exercise: Train Your Evaluative Eye Before You Trust the Output with Claude

- Source: ai-for-designers/chapters/07-taste-and-accountability.md
- Lane: BUILD (Claude Code)
- Hook: The output looked good. It looked good because you were tired, you were under deadline, and the model produces fluent artifacts faster than your evaluative eye can catch up. Taste is not instinct — it is a practiced capacity. And it atrophies when you stop using it.
- The artifact: A screen-recording of Claude generating 5 design concept descriptions from the same brief — intentionally at varying quality levels (one strong, two mediocre, two hollow-but-fluent). The designer ranks them 1–5 without seeing Claude's internal quality markers. Claude then reveals the quality rationale for each concept and compares it to the designer's ranking. A Manim animation shows a ranked bar chart — designer order vs. Claude's quality-marker order — highlighting where the designer's ranking was captured by fluency rather than quality.
- Prompt seed: `claude "Generate five distinct hero section concept descriptions for a fintech brand landing page. Vary quality deliberately: one genuinely strong concept (original, client-specific, visually precise), two mediocre concepts (generic, safe, no clear visual hierarchy), two hollow-but-fluent concepts (confident language, vague specifics, impressive-sounding but non-actionable). Do not label them by quality. Present them numbered 1–5. After I rank them, reveal your internal quality assessment for each and identify where fluency may have misled the ranking. [After designer ranks]: Here is my ranking: [designer input]. Now reveal the quality breakdown."`
- Read / check: Verify the five concepts are genuinely different in quality — not just different in subject. Confirm the post-ranking reveal names specific quality signals (not "this was better" but "this concept named the specific visual hierarchy decision; that one deferred it"). Check that the Manim bar chart renders both orderings clearly with contrast.
- Human supplies: The designer's own ranking response (interactive). The brief is synthetic; a real designer can use their own current project brief.
- Output medium: screen-recording mp4 (two-part terminal: generation round + ranking + reveal) + Manim (bar chart comparison)
- The change: Add a second calibration round using a brief from a different category (wayfinding, editorial, service design). Show whether the ranking accuracy improves — labeling the improvement as evidence that the evaluative capacity is a practice skill, not a fixed trait.
- Teardown angle: Fluency suppresses scrutiny. The calibration exercise is the diagnostic — not to improve the tool's output, but to maintain the designer's capacity to evaluate it correctly. The capacity that atrophies is the one that makes the tool usable.
- Exclusions: Cut the neuroscience processing-fluency literature; cut art-education theory of taste formation; cut the historical design criticism examples.
- Score: 8/10

---

## Candidate 07 — Build the One-Client Relationship Audit: Where AI Reaches the Limit of What It Knows with Claude

- Source: ai-for-designers/chapters/06-the-one-client-relationship.md
- Lane: BUILD (Claude Code)
- Hook: The AI can generate 200 logo variants in the time it used to take to sketch 5. The client rejected all 200. The model doesn't know the stakeholder who vetoed the last three rebrands. It doesn't know the brand history that made the previous direction sacred. It can't feel the political constraints in the room.
- The artifact: A screen-recording of Claude receiving a client project brief and generating: (1) a design direction recommendation with AI rationale; (2) a "what this brief doesn't tell me" section — listing 8–10 specific client-knowledge gaps that would change the recommendation (stakeholder dynamics, brand mythology, internal political constraints, past failed directions, client's undisclosed aesthetic aversions). Claude outputs both sections side by side. A D3 v7 standalone HTML renders the gaps as an expandable checklist — the designer checks off each item as they gather it from the client relationship.
- Prompt seed: `claude "I have this client design brief: [paste brief]. Generate two outputs. Output 1 — Design direction: your best recommendation given only this brief, with specific visual direction rationale. Output 2 — What this brief doesn't tell me: list 10 specific client-knowledge gaps that would change the direction if known — stakeholder with veto power, past rejected directions, brand mythology the client treats as sacred, undisclosed budget constraints, political constraints from recent organizational changes, client's relationship with the previous designer, the audience segment the brief understates. For each gap, name the specific question to ask in the first client meeting."`
- Read / check: Verify Output 2 generates genuinely client-specific gaps — not generic "understand the brand" advice but named, specific knowledge categories. Confirm each gap has a specific question attached. Check that the D3 checklist renders all 10 items and the expand/collapse works before recording.
- Human supplies: A synthetic project brief (one paragraph, naming client type, deliverable, timeline, stated objectives). Real-data upgrade: a designer inputs their own current client brief.
- Output medium: screen-recording mp4 (terminal session showing both outputs) + D3 checklist (screen-recorded browser interaction)
- The change: After the designer checks off the 10 gaps (simulated), show a second prompt: "Now regenerate the design direction with these client knowledge inputs: [filled gap list]." Show how the direction changes — label the delta as "the return on the client relationship."
- Teardown angle: The brief is a compressed signal. The client relationship is what decompresses it. AI optimizes for what's in the brief. The designer optimizes for what the client didn't know to include — and that is the professional value that doesn't transfer to the tool.
- Exclusions: Cut the agency vs. freelance structural comparison; cut the client-type taxonomy (startup vs. enterprise vs. nonprofit); cut the negotiation advice on revision rounds.
- Score: 7/10

---

## Candidate 08 — Research the Training Data Question: What Does Generative AI Actually Learn From, and Does It Matter for Your Practice with Claude

- Source: ai-for-designers/chapters/04-ip-and-copyright.md + chapters/01-the-ai-plus-one-designer.md
- Lane: RESEARCH (Claude assistant)
- Hook: The model was trained on the internet. The internet contains every designer's work ever published. Your stylistic signatures, your clients' brand assets, your work — potentially all of it, unlicensed, in the training corpus. What does the current legal and ethical landscape actually say about this?
- The artifact: A sourced 4-section research brief synthesized by Claude: (1) what is known about the major generative AI image tools' training data composition and licensing status — cite specific tools and available documentation; (2) the current state of copyright law as it applies to AI training data and AI-generated outputs in the US and EU; (3) three documented cases or regulatory decisions that establish precedent for designers and their clients; (4) the practical implications for a design studio — what to disclose, what to document, what to avoid. Screen-recorded as the synthesis builds, flagged claims highlighted.
- Prompt seed: `claude "Research the training data and copyright landscape for generative AI tools as it applies to design practice. I need a sourced brief covering: (1) what is publicly known about training data composition and licensing for Midjourney, DALL-E, Adobe Firefly, and Stable Diffusion — what is documented vs. assumed; (2) current US and EU copyright law on AI training data and AI-generated work ownership — cite the leading cases and regulatory positions; (3) three documented cases or regulatory decisions that have established precedent relevant to designers using AI commercially; (4) what a design studio should actually do — disclosure practices, documentation standards, client contract provisions. Cite sources. Flag any claim you cannot verify."`
- Read / check: Verify the tool-specific training data claims against publicly available documentation — do not accept vendor marketing as legal fact. Check that the legal framework citations are real cases or regulatory text, not summaries of summaries. Confirm the practical implications section names specific actions, not principles. Flag all unverified claims.
- Human supplies: Nothing — Claude researches and synthesizes from public sources. Human (ideally with legal counsel) must verify flagged claims before applying them professionally. This is a starting-point brief, not legal advice.
- Output medium: screen-recording mp4 (Claude chat session building the brief) + slate (the final formatted brief as a document image)
- The change: Ask Claude to identify the three most contested claims in its own brief — places where the evidence is thin, contradicted, or rapidly changing. Show Claude's self-critique. Label: "This is what you take to a copyright attorney before the contract is signed."
- Teardown angle: The tool's terms of service are not the law. The legal landscape is unsettled, jurisdiction-dependent, and moving faster than most design contracts. The research brief is what replaces "I assumed it was fine" with "here is what I knew and when I knew it."
- Exclusions: Cut EU AI Act compliance pathway detail; cut patent law discussion; cut the art-theft framing beyond the factual legal state.
- Score: 7/10
