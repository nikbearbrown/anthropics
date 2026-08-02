# AI-Proofing Your Job — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Run Your Cognitive Audit: Map 10 Tasks to the 7 Tiers with Claude"
- Source: ai-proofing-your-job/chapters/05-your-cognitive-audit-mapping-your-own-work-to-the-tiers.md + chapters/03-what-ai-actually-can-and-cannot-do-the-seven-tiers.md
- Lane: BUILD (Claude Code)
- Hook: The cognitive audit is the ongoing practice of asking, for every task you do, whether doing it yourself is building your judgment or whether delegating it is eroding it.
- The artifact: A Python script that takes a list of 10 professional tasks as input and outputs a filled audit table: tier (1–7), frequency, currently delegated (Y/N), should be delegated (Y/N), judgment built by doing it yourself, deskilling risk if delegated. Displayed as an animated Manim table filling row by row, color-coded by tier.
- Prompt seed: `claude "Run a cognitive audit on these 10 professional tasks using the 7-tier AI taxonomy. For each task: (1) assign a tier (1=pattern/generation, 2=embodied, 3=social/relational, 4=metacognitive/supervisory, 5=causal/strategic, 6=institutional/political, 7=wisdom/accountability), (2) state if AI should handle it (YES/NO/PARTIAL), (3) name what judgment is built by doing it yourself, (4) name the deskilling risk if fully delegated. Output as a structured table."`
- Read / check: Verify the tier assignments match the chapter's taxonomy definitions. Check that the "judgment built" column names something specific (not generic "expertise"). Confirm at least two tasks are assigned PARTIAL — the interesting cases are in the middle.
- Human supplies (Claude can't): The list of 10 actual professional tasks — these must be real work tasks from the viewer's own workflow, not generic examples. The video uses a worked example (mid-career UX designer from the chapter) with the viewer's own list as the call to action.
- Output medium: Manim (animated audit table filling row by row, tier-colored)
- The change: Add a seventh column: "what happens if I delegate this for 12 months?" — animate the compounding deskilling risk for each task classified as "should not delegate but currently is."
- Teardown angle: The audit isn't about being anti-AI — it's about knowing which tasks build the judgment your career depends on. The professional who can't name their compounding tasks can't protect them.
- Exclusions: Don't go into organizational AI governance; don't cover specific software tools; don't build a complete career planning tool.
- Score: 9/10

---

## Candidate 02 — "Build a Task Bundle Exposure Analyzer with Claude"
- Source: ai-proofing-your-job/chapters/02-the-stratification-who-loses-who-wins-and-why.md
- Lane: BUILD (Claude Code)
- Hook: Two analysts, same title, same tools. One is on a contracting career trajectory. One is on an expanding one. The difference isn't how much AI they use — it's which tasks they're using it on.
- The artifact: A Python script that takes a list of professional tasks and classifies each as INSIDE the AI frontier (routine cognitive, pattern-following, verifiable output) or OUTSIDE (contextual judgment, institutional knowledge, genuine accountability). Outputs: (1) an inside/outside bar showing the task bundle's exposure, (2) a "James vs Sarah" comparison using the chapter's case, (3) a career trajectory projection if current balance doesn't shift.
- Prompt seed: `claude "Classify these professional tasks as INSIDE or OUTSIDE the AI capability frontier using the Autor-Levy-Murnane task-level framework. INSIDE: routine cognitive work that follows explicit rules and has verifiable outputs. OUTSIDE: work requiring contextual interpretation, causal reasoning, institutional knowledge, or genuine accountability. For each task: classification, one-sentence justification, current AI tool capability level (superhuman/good/poor/fails). Output as a table with an inside/outside ratio summary."`
- Read / check: Verify the classification framework matches the chapter's definitions. Check that the inside/outside ratio is calculated correctly. Confirm the "career trajectory projection" is directional (not numerically precise — the chapter doesn't claim exactness).
- Human supplies (Claude can't): The list of professional tasks (from the viewer's actual role). The worked example uses the chapter's HR director case (10 tasks, 5 inside, 5 outside).
- Output medium: Manim (animated bar chart building inside/outside ratio, then a trajectory arrow appearing based on current balance)
- The change: Slide 30% of inside-frontier tasks to AI delegation — show how the bar shifts and what the freed time could buy if redirected to outside-frontier work.
- Teardown angle: Stratification operates at the task level, not the occupation level. An exposure score for your job title tells you almost nothing. The task bundle is what matters.
- Exclusions: Don't attempt to replicate BLS projection methodology; don't go into macroeconomic displacement; don't cover specific occupations beyond the worked example.
- Score: 9/10

---

## Candidate 03 — "Write Your AI Use Discipline Document with Claude"
- Source: ai-proofing-your-job/chapters/14-your-ai-use-discipline-writing-the-document-that-governs-your-tools.md + chapters/05-your-cognitive-audit-mapping-your-own-work-to-the-tiers.md
- Lane: BUILD (Claude Code)
- Hook: Elena didn't need better AI tools. She needed to have made the delegation decision before the deadline pressure arrived.
- The artifact: A Python script that prompts the user through five questions and generates a one-page AI Use Discipline document: delegation scope, protection scope, data boundary, handoff condition, accountability statement. The document is output as a formatted markdown file. Displayed as a Manim animation where each section fills in as the user responds.
- Prompt seed: `claude "You are helping a professional write their AI Use Discipline document. Ask five questions in sequence and draft each section based on their answers: (1) What tasks may AI handle in your workflow — be specific enough that a colleague would know exactly which tasks to route through AI. (2) What tasks may AI not handle — name the professional judgment calls that require your expertise. (3) What data may be shared with AI tools. (4) What must be checked before accepting AI output for each major task type. (5) Who owns the final decision on every output. Produce a one-page formatted document from their answers."`
- Read / check: Verify the document is genuinely specific (not generic — "AI may help with writing" is not a delegation scope). Confirm the handoff condition for at least one task is verifiable (not "I review it"). Check that the accountability statement is a first-person claim.
- Human supplies (Claude can't): The five answers — these come from the viewer's own professional practice. The video demo uses a synthetic mid-career professional's answers; the real value is when the viewer fills in their own.
- Output medium: screen-recording mp4 (live terminal interaction building the document section by section, then displaying the final formatted output)
- The change: Run the same document-generation for a second professional profile with very different task composition — show how the protection scope changes dramatically between, say, a marketer and a physician.
- Teardown angle: The act of writing the document is itself the cognitive audit. You can't write "what AI may not do" without thinking carefully about where your professional judgment actually matters.
- Exclusions: Don't go into organizational policy; don't cover NIST AI RMF in detail; don't build a compliance tracking tool.
- Score: 9/10

---

## Candidate 04 — "Measure the 56% AI Wage Premium: What the Data Actually Says with Claude"
- Source: ai-proofing-your-job/chapters/13-the-56-percent-premium-what-the-market-is-actually-paying-for.md
- Lane: RESEARCH (Claude assistant)
- Hook: Marcus quit eleven years of manufacturing expertise to get an AI certification. His next job search took eight months. He misread the arrow.
- The artifact: A sourced research brief on the PwC AI Jobs Barometer finding — what the 56% premium actually measures, what the caveats are (selection effects, scarcity rent, sector variation), and what "AI fluency" means to the labor market vs what it means to certification vendors. Displayed as a Manim visualization: the wrong arrow vs the right arrow (domain expertise + AI fluency vs domain expertise → switch to AI engineering).
- Prompt seed: `claude "Research the PwC Global AI Jobs Barometer wage premium finding. Synthesize: (1) what the 56% premium actually measures (what jobs are in the 'AI skills required' category), (2) the three main caveats the press release omits (selection effects, scarcity rent, sector variation), (3) the Lightcast/Burning Glass evidence on which sectors show the fastest AI skill demand growth, (4) the Autor and Deming research on complementarity between technology and human skill. Cite sources and be explicit about what is well-evidenced vs what is observational."`
- Read / check: Verify the PwC report exists and the premium figure is correctly cited (confirm exact year, methodology, geography). Check the Autor 2015 and Deming 2017 citations are accurate. Confirm the Lightcast evidence is distinguished from the PwC evidence.
- Human supplies (Claude can't): Verification of the PwC report citation — Claude may cite an outdated or incorrect version. Human must confirm the current report's specific claims before publishing.
- Output medium: Manim (animated "wrong arrow vs right arrow" diagram, then a sourced citation timeline building)
- The change: Ask Claude to build the "evidence portfolio" concept — what three sentences from the past six months would demonstrate AI-fluent domain expertise to an employer? Show what that looks like for the manufacturing analyst from the opening case.
- Teardown angle: The premium belongs to domain experts who added AI fluency — not to people who switched to AI. The right arrow is domain expertise + AI fluency → do more of what only you can do.
- Exclusions: Don't make specific salary predictions; don't cover specific occupations beyond the worked example; don't go into the full Eloundou et al. methodology.
- Score: 8/10

---

## Candidate 05 — "Simulate the Deskilling Trap: What 12 Months of Over-Delegation Costs with Claude"
- Source: ai-proofing-your-job/chapters/12-the-deskilling-trap-how-to-use-ai-without-losing-what-you-built.md + chapters/05-your-cognitive-audit-mapping-your-own-work-to-the-tiers.md
- Lane: BUILD (Claude Code)
- Hook: James's output volume is up. His manager notices the efficiency. In 18 months, his role is reclassified. The AI tools did not create this divergence — they revealed it.
- The artifact: A Python simulation that models two career trajectories over 12 months: a professional who delegates inside-frontier tasks and protects outside-frontier tasks (Sarah path) vs one who delegates everything that feels like effort (James path). Output: two animated curves showing "outside-frontier task time as % of workweek" over 12 months. The James path curves down as skills atrophy; the Sarah path curves up as expertise compounds.
- Prompt seed: `claude "Build a Python simulation of two career trajectories over 52 weeks. Professional A (Sarah): delegates all Tier 1-2 tasks to AI, protects Tier 4-7 tasks. Professional B (James): delegates everything that AI can handle, including judgment-adjacent tasks. Simulate: (1) outside-frontier task time as % of workweek for each, (2) skill atrophy rate for James (10% per quarter for any judgment skill not practiced), (3) skill compound rate for Sarah (5% per quarter for any judgment skill consistently practiced). Plot as two time-series curves over 52 weeks."`
- Read / check: Verify the simulation parameters are reasonable (10% atrophy, 5% compound are illustrative, not empirically precise — the chapter doesn't claim exact rates). Confirm the curves diverge visibly. Check that the simulation has a "reclassification event" trigger at week ~65 for James's trajectory.
- Human supplies (Claude can't): Nothing — fully synthetic simulation. The numbers are illustrative; the shape of the curves is the lesson.
- Output medium: Manim (animated two-curve time series with labels and a "reclassification event" marker)
- The change: Add a third trajectory: a professional who started on the James path but switched at week 26. Show whether the recovery curve reaches the Sarah level, or whether the 6-month gap leaves a permanent deficit.
- Teardown angle: The deskilling trap isn't dramatic — it feels like productivity improvement. The efficiency metrics go up while the judgment that matters compounds in the wrong direction.
- Exclusions: Don't claim the simulation parameters are empirically validated; don't cover specific software tools; don't go into organizational restructuring economics.
- Score: 8/10

---

## Candidate 06 — "Map the Jagged Frontier for Your Field with Claude"
- Source: ai-proofing-your-job/chapters/02-the-stratification-who-loses-who-wins-and-why.md + chapters/03-what-ai-actually-can-and-cannot-do-the-seven-tiers.md
- Lane: RESEARCH (Claude assistant)
- Hook: The frontier isn't smooth. AI is superhuman at some tasks and below-human at others — often within the same professional domain, sometimes within the same document.
- The artifact: A field-specific jagged frontier map — for a chosen profession (finance, law, medicine, engineering, marketing), a sourced table showing: tasks where AI is superhuman, tasks where AI is good but requires supervision, tasks where AI fails silently, tasks where AI structurally cannot help. Displayed as a Manim-animated jagged-line visualization where task types are plotted against AI capability.
- Prompt seed: `claude "Map the jagged AI capability frontier for [FINANCIAL ANALYSIS]. Using the Dell'Acqua et al. 2023 BCG field experiment framing and the Autor-Levy-Murnane task taxonomy, identify: (1) 3 tasks where AI is superhuman (list specific tasks), (2) 3 tasks where AI is good but requires human supervision (list specific failure modes), (3) 3 tasks where AI fails silently — produces confident wrong output, (4) 3 tasks where AI structurally cannot help. Cite evidence for each category where available."`
- Read / check: Verify the Dell'Acqua et al. 2023 citation is accurate (the BCG field experiment on inside/outside frontier performance). Confirm the "fails silently" category includes at least one case where the output looks correct but isn't. Check that the structural-cannot-help category names something genuinely outside pattern completion.
- Human supplies (Claude can't): Selection of the specific profession — the video uses financial analysis as a worked example; viewers substitute their own field. Verification that the field-specific examples are accurate requires domain expertise.
- Output medium: Manim (animated jagged-line visualization with task labels appearing at different capability heights)
- The change: Move one task from the "AI is good" category to "AI fails silently" by adding a specificity constraint (instead of "summarize market data" → "summarize market data for a specific supply-chain disruption in a named company last week"). Show how the frontier is jagged along specificity as well as task type.
- Teardown angle: Occupation-level exposure scores are useless without task decomposition. The jagged frontier means you have to go task by task — and the tasks where AI fails are often the ones where its output looks most credible.
- Exclusions: Don't replicate the full Dell'Acqua study methodology; don't make specific predictions about which occupations will disappear; don't cover macroeconomic displacement.
- Score: 8/10

---

## Candidate 07 — "Build the Phase Gate: Where Your Work Ends and AI Begins with Claude"
- Source: ai-proofing-your-job/chapters/04-the-phase-gate-where-your-work-ends-and-ai-begins.md
- Lane: BUILD (Claude Code)
- Hook: The phase gate is not a checkpoint you visit once. It's the recurring discipline of specifying exactly what you're handing off before you hand it off.
- The artifact: A Python script that generates a phase gate specification document for any professional task: what the human completes before AI runs (the input spec), what AI may decide vs what is pre-decided, what the human verifies before accepting output, what the human owns regardless of AI contribution. Displayed as a Manim-animated four-field specification card.
- Prompt seed: `claude "Generate a phase gate specification for this professional task: [TASK]. For this task, specify: (1) BEFORE AI RUNS — what must the human complete, decide, or specify (the minimum human pre-work that makes the AI input meaningful), (2) WHAT AI MAY DECIDE — the implementation choices AI can make within the spec, (3) WHAT AI MAY NOT DECIDE — the identification choices that remain human (what specifically the prototype/output is designed to identify), (4) HUMAN VERIFICATION — what the human checks before accepting the output. Format as a four-field specification card."`
- Read / check: Verify that the "what AI may not decide" field is specific (not "ethical questions" — name the actual decision). Confirm "before AI runs" includes a meaningful minimum of human pre-work. Check that "human verification" names a concrete check, not "I review it."
- Human supplies (Claude can't): The professional task to specify. The video uses a worked example from the chapter (financial analysis, contract review, or design brief); viewers substitute their own task.
- Output medium: Manim (animated four-field card filling in section by section)
- The change: Apply the same phase gate to a task the viewer has been running without one — show how writing the specification reveals a decision that was previously being made by AI by default.
- Teardown angle: The phase gate isn't bureaucracy — it's the moment where your professional judgment becomes a spec, not a hope. If you can't write the four fields, the boundary between your work and AI's work is invisible.
- Exclusions: Don't go into software engineering specification methodology in depth; don't build a full workflow management tool; don't cover organizational governance.
- Score: 8/10

---

## Candidate 08 — "Research the Apprenticeship Ladder Problem with Claude"
- Source: ai-proofing-your-job/chapters/02-the-stratification-who-loses-who-wins-and-why.md
- Lane: RESEARCH (Claude assistant)
- Hook: If the tasks that trained the last generation of analysts, developers, and designers are now handled by AI — what trains the next generation?
- The artifact: A sourced research brief on the apprenticeship ladder problem — evidence that junior/entry-level task contraction affects expert pipeline formation, documented cases or theoretical frameworks from three fields (law, medicine, software), and the current state of evidence (is this confirmed, emerging, or speculative?). Displayed as a Manim three-field comparison: field / evidence for pipeline effect / current evidence quality.
- Prompt seed: `claude "Research the apprenticeship ladder problem — the hypothesis that AI handling of junior/entry-level tasks reduces the pipeline that produces senior experts. Find: (1) any documented evidence that junior task automation has already affected expert pipeline formation in at least one field, (2) the theoretical framework from expertise research (Ericsson et al. on deliberate practice) that explains why doing the work matters for building the judgment, (3) the counterargument that AI-augmented junior practice could substitute for traditional apprenticeship. Be honest about what is confirmed vs emerging vs speculative."`
- Read / check: Verify the Ericsson deliberate practice citation (1993 Psychological Review). Check whether any field actually has documented junior-pipeline contraction data (the chapter flags this as speculative — confirm whether Claude finds primary evidence or only commentary). Confirm the counterargument is fairly represented.
- Human supplies (Claude can't): Verification of whether primary evidence exists — the chapter explicitly says "it appears in commentaries but may not be in peer-reviewed literature yet." Claude may find this evidence or confirm its absence. Human must check at least two sources.
- Output medium: Manim (animated three-field comparison table: field / evidence / evidence quality)
- The change: Ask Claude to design a study that would confirm or disconfirm the apprenticeship ladder hypothesis — what data would you need, where would you find it, what would count as evidence?
- Teardown angle: The experience base built through years of production work is genuinely valuable precisely because the pathway that builds it is becoming less common. That makes current mid-career judgment a scarcer input than it was a decade ago.
- Exclusions: Don't go into education policy; don't cover specific professional licensing systems; don't claim the effect is proven (the chapter doesn't).
- Score: 7/10

---

## Candidate 09 — "Build the Evidence Portfolio: Document What Only You Could Catch with Claude"
- Source: ai-proofing-your-job/chapters/13-the-56-percent-premium-what-the-market-is-actually-paying-for.md
- Lane: BUILD (Claude Code)
- Hook: The professional who can't produce examples of decisions where their domain judgment changed the AI's output has a different problem than they think.
- The artifact: A Python script that prompts the user through a structured evidence-portfolio session: for each of five recent AI-assisted work outputs, record one sentence about what domain knowledge caught, corrected, or contributed that AI could not have provided. Outputs a formatted evidence portfolio document with five entries. Displayed as a Manim animation of the portfolio building entry by entry.
- Prompt seed: `claude "You are helping a professional build their evidence portfolio — a running record of decisions where domain expertise changed the AI's output. For each of five AI-assisted work outputs the professional describes, generate a formatted portfolio entry: (1) what the AI produced, (2) what the domain knowledge caught or corrected, (3) why the AI could not have known this, (4) the outcome difference. Format as five portfolio entries with a summary statement about the pattern across entries."`
- Read / check: Verify the portfolio entries name something specific (not "the AI got it wrong" — name what specifically the AI got wrong and what knowledge was needed to catch it). Confirm the "why AI could not have known this" is structural (not just "it didn't have the data" — name what kind of knowledge is structurally inaccessible).
- Human supplies (Claude can't): The five work scenarios — these must be real (or realistic synthetic) AI-assisted outputs from the viewer's own practice. The video uses a worked example from the chapter (the manufacturing analyst who caught three valuation errors).
- Output medium: screen-recording mp4 (live terminal interaction building the portfolio, then displaying the formatted output)
- The change: Ask Claude to draft a three-sentence professional positioning statement from the portfolio entries — "domain expertise first, AI fluency second, protected judgment third." Show how the evidence becomes the positioning.
- Teardown angle: The evidence portfolio is proof to yourself that the premium is real and that you hold it. Professionals who cannot produce examples have a different problem than they think — they may not need better positioning. They may need a more deliberate phase gate.
- Exclusions: Don't build a full career documentation tool; don't cover LinkedIn optimization; don't go into resume writing.
- Score: 7/10

---

## Candidate 10 — "Simulate the Lying Calculator: Tier 4 Metacognitive Auditing with Claude"
- Source: ai-proofing-your-job/chapters/03-what-ai-actually-can-and-cannot-do-the-seven-tiers.md
- Lane: BUILD (Claude Code)
- Hook: Imagine a calculator correct 85% of the time and confidently wrong the other 15%. The display looks identical either way. Who catches the errors?
- The artifact: A Python script that generates a set of 20 AI-produced outputs — a mix of correct and plausibly-wrong answers on a professional topic — and asks the viewer to classify each as CORRECT/SUSPICIOUS/WRONG before showing the verified answers. Tracks: (1) detection rate (what % of wrong answers did you catch?), (2) false-positive rate (what % of correct answers did you flag?), (3) calibration (are you more confident when you're right?). Displays as a score dashboard animated in Manim.
- Prompt seed: `claude "Generate 20 short AI-produced outputs on [FINANCIAL ANALYSIS]. Include: 14 that are correct, 4 that contain a plausible but subtle error that requires domain knowledge to catch, and 2 that are confidently wrong in a way that a non-expert would miss. Do NOT mark which is which. Format as numbered items. Then, separately, provide the answer key with which category each item belongs to and what the error is."`
- Read / check: Verify the plausible errors are actually plausible (not obviously wrong). Confirm the confident wrong answers require domain knowledge to catch (not just factual lookup). Check that the answer key correctly identifies all 20 items.
- Human supplies (Claude can't): Domain knowledge to verify the answer key — the human running the demo needs to check that the "plausible errors" are actually subtle. Real domain expertise is required to validate this card.
- Output medium: Manim (animated score dashboard: detection rate, false-positive rate, calibration score appearing after each response)
- The change: Run the same 20 items after giving the viewer the chapter's "mental arithmetic" frame — tell them what category of error to look for. Show if the detection rate improves when the search frame is explicit.
- Teardown angle: The people who catch errors are the ones with enough domain knowledge to feel that something is wrong before they can prove it. Tier 4 metacognition is built by having done the work directly — not by reviewing AI output.
- Exclusions: Don't claim the 85%/15% figure is an actual LLM accuracy rate; don't cover specific AI benchmarks; don't go into AI safety or alignment.
- Score: 7/10
