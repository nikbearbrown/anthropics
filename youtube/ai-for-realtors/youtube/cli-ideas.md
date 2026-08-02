# AI for Realtors — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Audit Your Listing Copy for Fair Housing Violations with Claude"
- Source: ai-for-realtors/chapters/06-fair-housing-and-ai-the-72-gap.md
- Lane: RESEARCH (Claude assistant)
- Hook: 72% of agents using AI for listing copy have never had Fair Housing training — and the phrases Claude flags as natural ("family-friendly," "young professionals," "close to worship centers") are the ones NAR says create liability.
- The artifact: a side-by-side before/after listing description with every at-risk phrase highlighted in a color-coded table — familial status (red), age-coded (orange), religious (yellow), neighborhood-coded (purple) — plus a rewritten clean version with replacement language for each phrase.
- Prompt seed: `claude "Review this listing description for potential Fair Housing violations under the seven high-risk pattern types from NAR guidance. For each flagged phrase, name the protected class implicated, explain why AI generates it, and suggest a property-feature replacement. Then rewrite the full description with all violations removed."`
- Read / check: Verify that flagged phrases match the chapter's seven categories (not just generic "bias"). Check that the replacement language describes property features, not people. Confirm the rewritten version contains zero people-descriptive phrases.
- Human supplies (Claude can't): A real (or realistic synthetic) listing description containing 3–5 of the seven risk patterns — synthesize from the chapter's examples if no real listing is available. Nothing — a synthetic listing seeded from the chapter's examples is fully acceptable for the video.
- Output medium: Manim (animated table where risk phrases light up one by one by category color, then the rewrite plays as text substitution)
- The change: Ask Claude to now audit for omission patterns — does the listing consistently omit school quality, transit, or amenity mentions only when the property is in a specific neighborhood type? Demonstrate the invisible bias of what is NOT said.
- Teardown angle: The AI generated the violations because it trained on decades of steering-adjacent copy — the model's fluency is the problem, not the fix. Only human review with a checklist closes the gap.
- Exclusions: Don't drill into Freddie Mac AVM-bias research; don't audit photos or virtual staging; don't go into SafeRent case law details.
- Score: 9/10

---

## Candidate 02 — "Measure AVM Error Range with Claude: What Zestimate Can't See"
- Source: ai-for-realtors/chapters/05-the-avm-trap-what-zestimate-can-and-cannot-do.md
- Lane: BUILD (Claude Code)
- Hook: A $600,000 Zestimate within Zillow's own stated 20% error band could be any price from $480K to $720K — that's a $240,000 spread wearing a single confident number.
- The artifact: An animated error-band visualization — a horizontal bar centered on a synthetic Zestimate with the 5%/10%/20% confidence rings drawn on either side, labeled with dollar values. A second panel shows how the band widens for off-market vs on-market properties (1.74% vs 7.20% median error). A third panel plots the five AVM failure conditions as icons that shrink/grow the band dynamically.
- Prompt seed: `claude "Write a Python script using matplotlib that animates a Zestimate error band visualization. Input: a home value and Zillow's published accuracy stats (5%/10%/20% bands for on-market and off-market). Output: an animated MP4 showing the confidence rings expanding from the center price, with dollar labels. Add a toggle between on-market (1.74% median error) and off-market (7.20%) that visually widens the band."`
- Read / check: Verify the dollar arithmetic (20% of $600K = $120K each side = $480K–$720K range). Confirm the on-market vs off-market figures match Zillow's published methodology page. Check the animation transitions are readable at video resolution.
- Human supplies (Claude can't): The Zillow methodology page URL to verify current accuracy statistics before recording — figures may shift. Zillow's published numbers are public and directly citable; synthetic home value is fine.
- Output medium: Manim (animated error band with expanding rings and dollar labels)
- The change: Add a "condition blindness" slider — drag it to show how a kitchen renovation or deferred roof adds/subtracts value the AVM can't see, shifting the true price outside the model's confidence band.
- Teardown angle: The AVM's confidence is a function of data density, not truth. The five failure conditions (unique property, sparse data, condition blindness, micro-neighborhood context, data errors) are precisely where the CMA earns its fee.
- Exclusions: Don't go into the federal AVM quality-control rule for lenders (different audience); don't compare AVMs across platforms; don't discuss appraisal licensing.
- Score: 9/10

---

## Candidate 03 — "Build a Fair Housing Audit Checklist Tool with Claude"
- Source: ai-for-realtors/chapters/10-lead-scoring-crm-ai-and-the-fair-housing-audit-youre-not-running.md + chapters/06-fair-housing-and-ai-the-72-gap.md
- Lane: BUILD (Claude Code)
- Hook: A CRM that learned from your call-back patterns can silently amplify zip-code bias — and most agents have never run the 5-step audit that would catch it.
- The artifact: A Python script that takes a CSV of CRM leads (synthetic: lead ID, zip code, price range, source, score) and outputs: (1) a geographic cluster analysis showing if high-scored leads concentrate in specific zip codes, (2) a price-band distribution chart comparing high-scored vs all leads, (3) a source/campaign breakdown. Output is an animated bar chart sweeping from full-pipeline to high-scored-only, with a "clustering detected" flag.
- Prompt seed: `claude "Write a Python script that takes a CSV of real-estate CRM leads with columns (lead_id, zip_code, price_range, source, crm_score) and produces three charts: (1) animated bar chart of zip code distribution for all leads vs top-quartile leads, (2) price band distribution comparison, (3) source breakdown. Flag any zip code that is >2x over-represented in top-quartile vs overall. Generate synthetic data if no CSV is provided."`
- Read / check: Confirm the 2x over-representation threshold is reasonable and defensible. Check that the synthetic data generator creates a detectable clustering pattern (not uniformly random). Verify charts have clear labels at video resolution.
- Human supplies (Claude can't): Nothing — fully synthetic. The script generates its own demo data with deliberate geographic clustering baked in so the flag fires visibly on screen.
- Output medium: screen-recording mp4 (live terminal run generating the charts, then the charts animate)
- The change: Add a reset — the script regenerates data with geographic weighting removed (uniform distribution) and re-runs, showing the flag disappears. Demonstrates what "fixed" looks like.
- Teardown angle: The model didn't need discriminatory intent — it learned from the agent's behavior. The audit doesn't require a data scientist; it requires a spreadsheet export and five checks.
- Exclusions: Don't attempt a real legal disparate-impact analysis; don't integrate with actual CRM APIs; don't cover the broker-level policy question.
- Score: 8/10

---

## Candidate 04 — "Build the 6-Element Defensible File Workflow with Claude"
- Source: ai-for-realtors/chapters/13-building-your-ai-workflow-fast-and-defensible.md
- Lane: BUILD (Claude Code)
- Hook: Two agents publish identical AI-generated listing copy. One has a documented file. One doesn't. A complaint arrives. They are not in the same position.
- The artifact: A Python script that takes a property description as input and generates a complete "defensible file" folder structure: source_facts.md (verified inputs), ai_draft.md (raw Claude output), audit_checklist.md (Fair Housing + factual accuracy + pricing framing checks), and review_notes.md (what was changed and why). Each file is populated with template content; the audit checklist auto-generates line items from the property description.
- Prompt seed: `claude "You are helping build a defensible AI workflow for a real estate agent. Given this property description, generate: (1) a source_facts template the agent fills in before prompting AI, (2) the AI listing draft, (3) a Fair Housing audit checklist with specific line items drawn from NAR's seven high-risk patterns, (4) a review_notes template with fields for what was changed and why. Output as four separate markdown files."`
- Read / check: Verify all seven Fair Housing pattern categories appear in the checklist. Check that the source_facts template asks for square footage, condition, pricing basis. Confirm review_notes has a field for each change type.
- Human supplies (Claude can't): Nothing — fully synthetic. The script uses a sample property description. Acceptable for demo; real agents substitute their own inputs.
- Output medium: screen-recording mp4 (terminal run showing files being created, then a quick pan through each file's contents)
- The change: Run the same script on a second property that contains a Fair Housing red flag in the input — show the checklist catching it and the review_notes documenting the edit.
- Teardown angle: Documentation isn't bureaucracy — it's the evidence that you did your job. The file answers the complaint before the agent has to.
- Exclusions: Don't build a full CRM integration; don't cover team/broker supervision policy; don't go into California AB 723 virtual staging specifically.
- Score: 8/10

---

## Candidate 05 — "Research AVM Racial Bias: What the Freddie Mac Study Found with Claude"
- Source: ai-for-realtors/chapters/05-the-avm-trap-what-zestimate-can-and-cannot-do.md + chapters/06-fair-housing-and-ai-the-72-gap.md
- Lane: RESEARCH (Claude assistant)
- Hook: Automated valuation models systematically undervalue Black-owned homes by 3.4 percentage points on average — not because of intent, but because they trained on data that reflects a century of discriminatory appraisal practices.
- The artifact: A sourced research brief (Manim-animated timeline) covering: the Freddie Mac 2021 finding, the Urban Institute 2024 peer-reviewed confirmation, the 2024/2025 federal AVM quality-control rule, and the mechanism (historical training data encoding historical discrimination). Displayed as a 4-event annotated timeline with source labels.
- Prompt seed: `claude "Research the peer-reviewed evidence on racial valuation gaps in automated valuation models. Synthesize: (1) the Freddie Mac 2021 study on racial and ethnic valuation gaps, (2) Urban Institute 2024 research on AVM bias, (3) the federal interagency AVM quality-control final rule (2024/2025) and its stated justification. For each source, cite specifically, summarize the key finding in one sentence, and explain the structural mechanism producing the bias."`
- Read / check: Verify that cited studies are real and that the 3.4 percentage point figure is correctly attributed to Urban Institute (verify exact source before publishing). Confirm the federal rule citation (effective date, issuing agencies). Check that the mechanism explanation (historical data encoding historical discrimination) matches the source text.
- Human supplies (Claude can't): Verification of the specific statistic (3.4pp) against the actual Urban Institute report before publishing — Claude may mis-attribute the figure. Citable real sources are required; the human must click through to confirm.
- Output medium: Manim (4-event animated timeline with source labels and key numbers appearing in sequence)
- The change: Add a fifth event — the agent's professional obligation. Show how the interagency rule (for lenders) signals regulatory direction that agents should anticipate, even though they are not directly subject to it.
- Teardown angle: The AVM isn't malicious — it learned from data that encoded the outcomes of redlining and discriminatory appraisal. Fixing the tool requires fixing the training data, which means the bias persists in deployed systems regardless of intent.
- Exclusions: Don't go into the full history of redlining; don't cover appraisal licensing reform; don't compare AVMs across vendors.
- Score: 8/10

---

## Candidate 06 — "Simulate the Contract Stack: What an AI Summary Misses with Claude"
- Source: ai-for-realtors/chapters/08-contract-and-document-ai-what-the-summary-misses.md
- Lane: RESEARCH (Claude assistant)
- Hook: The AI summary said the buyer had a standard inspection contingency. The addendum waived it. The summary wasn't lying — it just never read the addendum.
- The artifact: A side-by-side comparison document: base contract summary (what AI sees) vs full stack reality (what changes in each addendum layer). Displayed as a Manim-animated "stack reveal" — start with one document, layer in four more, watch provisions change or disappear as each layer adds.
- Prompt seed: `claude "I am going to give you a simulated residential transaction document stack: a base purchase agreement + three addenda. Summarize the base contract alone. Then summarize the full stack. List every provision that changed between the two summaries, and classify each change as: (1) contingency waiver, (2) deadline modification, (3) price term change, or (4) custom/handwritten addition."`
- Read / check: Verify the summary-alone vs full-stack comparison catches the simulated inspection waiver in the addendum. Confirm all six checklist categories (addenda, contingencies, deadlines, custom terms, cross-document conflicts, jurisdiction-specific) are surfaced. Check that the "what changed" list is complete.
- Human supplies (Claude can't): The synthetic document stack (base CAR purchase agreement structure + 3 addenda with deliberate modifications, including one inspection waiver). This can be a realistic synthetic, not a real transaction — create it from the chapter's examples.
- Output medium: Manim (animated document stack reveal where layers add and provisions change color as they're modified)
- The change: Run the 6-item checklist against the same stack — show how the checklist catches the waiver that the summary missed. The change beat is the checklist doing its job.
- Teardown angle: The AI summary is useful for orientation. It is not a contract review. The six-item checklist is the work that converts a starting point into a professional judgment.
- Exclusions: Don't go into legal advice territory; don't attempt to simulate actual California CAR forms; don't cover HOA-specific addenda in depth.
- Score: 7/10

---

## Candidate 07 — "Generate a CMA Comparison: AVM vs Agent Judgment with Claude"
- Source: ai-for-realtors/chapters/05-the-avm-trap-what-zestimate-can-and-cannot-do.md + chapters/13-building-your-ai-workflow-fast-and-defensible.md
- Lane: BUILD (Claude Code)
- Hook: The listing appointment moment: Zillow says $640K. The CMA says $590K. Which conversation wins — the one where the agent dismisses Zillow, or the one where they explain exactly what Zillow can't see?
- The artifact: A Python script that takes a property's synthetic data (sqft, beds/baths, neighborhood, condition notes) and outputs a two-column comparison table: AVM estimate vs CMA adjusted, with each CMA adjustment labeled (condition, micro-neighborhood, renovation, data error correction) and the dollar impact shown. Displayed as an animated bar chart where CMA adjustments "subtract" from or "add to" the AVM number one by one.
- Prompt seed: `claude "Given this property's data, generate: (1) a simulated AVM estimate using the property's attributes and recent synthetic comparable sales, (2) a CMA with explicit adjustments for condition, micro-neighborhood, renovation value, and active buyer demand. Display as a two-column comparison table where each CMA adjustment shows its dollar impact on the final value."`
- Read / check: Verify that the AVM and CMA produce different numbers (the script should be set up so condition adjustment moves value by a visible amount). Confirm adjustment labels match the chapter's five CMA-vs-AVM dimensions. Check that dollar arithmetic is correct.
- Human supplies (Claude can't): Nothing — fully synthetic. A sample property profile (generated from chapter examples) is sufficient. The lesson is the adjustment methodology, not a specific property's true value.
- Output medium: Manim (animated bar chart where CMA adjustments appear one at a time, moving the value from AVM estimate to CMA recommendation)
- The change: Add a "confidence range" display — wrap both numbers in their respective uncertainty bands (AVM error band from Zillow stats, CMA professional judgment range) and show they overlap more than the point estimates suggest.
- Teardown angle: The agent's value isn't in having a different number — it's in being able to explain each adjustment specifically. That explanation is what the seller can't get from Zillow.
- Exclusions: Don't build a real AVM model; don't use actual Zillow API calls; don't attempt to replicate specific market data.
- Score: 7/10

---

## Candidate 08 — "Research the AI Tools Hidden in Your Workflow with Claude"
- Source: ai-for-realtors/chapters/03-the-ai-tools-in-your-workflow.md
- Lane: RESEARCH (Claude assistant)
- Hook: An agent who thinks they're "not really using AI yet" opens Zillow, uses virtual staging, checks CRM lead scores, and asks a chatbot to summarize the inspection report — five AI-powered decisions before lunch.
- The artifact: A sourced research brief mapping the five AI tool categories (valuation, media alteration, lead prioritization, document summary, scheduling automation) against their primary failure modes, platform disclaimers, and the agent's minimum review requirement. Displayed as an animated five-row table that builds row by row with failure mode icons.
- Prompt seed: `claude "Research the AI capabilities embedded in the following real estate platforms: Zillow (Zestimate), ShowingTime, Follow Up Boss lead scoring, virtual staging tools, and AI document summary tools. For each: (1) what the AI is actually doing (the mechanism), (2) the platform's own stated limitations or disclaimers, (3) the primary failure mode, (4) the minimum professional review required before using the output with a client. Cite platform documentation where available."`
- Read / check: Verify that Zillow's "not an appraisal" disclaimer is correctly cited (check their current methodology page). Confirm the ShowingTime acquisition figure ($500M by Zillow) if cited. Check that each failure mode matches the chapter's taxonomy (valuation accuracy, misrepresentation risk, Fair Housing proxy variables, addendum blindness, exception handling).
- Human supplies (Claude can't): Verification that platform documentation URLs are current — Claude's training data may cite outdated methodology pages. The human must click through to confirm disclaimer language is still live.
- Output medium: Manim (animated 5-row table building row by row, each with a failure-mode icon and review-required rating)
- The change: Add the three-question audit as a reusable card: "What data did this come from? What kind of thing is this output? What decision will this influence?" Show the questions applied to one of the five tools.
- Teardown angle: The platforms are genuinely useful. The compliance posture is not "stop using AI" — it is "know which category each tool belongs to and apply the right review." The agent who can't answer the three questions is the one with the liability gap.
- Exclusions: Don't go into California AB 723 specifically; don't cover brokerage-level policy; don't build anything — this is a research/synthesis card.
- Score: 7/10

---

## Candidate 09 — "Write Your Delegate/Guard Workflow with Claude"
- Source: ai-for-realtors/chapters/13-building-your-ai-workflow-fast-and-defensible.md
- Lane: RESEARCH (Claude assistant)
- Hook: Two agents, same tools, same deadline pressure. One has a Delegate/Guard list that runs automatically. The other improvises every time — and gambling on their own attention.
- The artifact: A filled-in Delegate/Guard table for a representative agent workflow — 12 common tasks classified, audit steps written for each Delegate task, Guard tasks with a one-sentence rule. Displayed as a Manim-animated two-column table (Delegate / Guard) filling in row by row.
- Prompt seed: `claude "You are helping a residential real estate agent build their AI workflow. Classify these 12 tasks as Delegate (AI handles with review) or Guard (human judgment required, AI may assist only): listing copy drafting, CMA pricing recommendation, Fair Housing compliance review, CRM lead prioritization, contract clause summary, negotiation timing judgment, market summary for client, disclosure adequacy determination, email follow-up drafting, virtual staging approval, inspection summary for buyer, MLS photo selection. For each Delegate task, write the specific audit checklist steps. For each Guard task, write a one-sentence rule."`
- Read / check: Verify the classification matches the chapter's framework (pricing recommendation = Guard; listing copy first draft = Delegate). Check that audit checklist steps are specific (not "review the output") and traceable to the chapter's specific risk types.
- Human supplies (Claude can't): Nothing — fully synthetic. The 12-task list is drawn from the chapter. Agents substitute their own task lists in practice.
- Output medium: Manim (animated two-column table building row by row, Delegate items in blue, Guard items in amber)
- The change: Ask Claude to add a "misclassification consequence" column — what happens if each Guard task is mistakenly treated as Delegate? Show one concrete failure scenario per Guard task.
- Teardown angle: Workflow is the operating system. The checklist takes more time than publishing the first draft and less time than responding to a complaint. Repeatability is the point.
- Exclusions: Don't build a digital tool; don't go into team/broker supervision; don't cover brokerage-level E&O considerations.
- Score: 7/10

---

## Candidate 10 — "Simulate Lead Score Bias: Building the Pattern Audit with Claude"
- Source: ai-for-realtors/chapters/10-lead-scoring-crm-ai-and-the-fair-housing-audit-youre-not-running.md
- Lane: BUILD (Claude Code)
- Hook: The CRM didn't need to discriminate — it learned from the agent's call-back timing. A model trained on human behavior amplifies human patterns at scale.
- The artifact: A Python script that simulates a CRM lead dataset with deliberate geographic clustering (high-scored leads skew toward specific zip codes that correlate with a synthetic demographic). The script runs the 5-step pattern audit and outputs: a geographic cluster chart, a price-band distribution, a source breakdown — all animated to reveal the skew building from full pipeline to top-quartile view.
- Prompt seed: `claude "Build a Python simulation of a CRM lead scoring audit. Generate 200 synthetic leads with columns: lead_id, zip_code, price_range_bucket, source, crm_score. Deliberately weight the scoring so leads from zip codes 10001-10005 score 20% higher than leads from 10006-10010, holding engagement constant. Then run a 5-step audit: geographic cluster check, price-band distribution, source pattern, language/preference breakdown, score-variance analysis. Flag any check where the skew exceeds 2x. Animate as a matplotlib bar chart."`
- Read / check: Verify the synthetic dataset has a detectable 2x skew that the flag catches. Confirm the five audit steps match the chapter's procedure exactly. Check that the visualization makes the bias visible at video resolution.
- Human supplies (Claude can't): Nothing — fully synthetic. The script generates its own data with deliberate bias baked in so the audit flag fires visibly on screen.
- Output medium: screen-recording mp4 (live terminal run showing the bias building in the chart, then the audit flag appearing)
- The change: Rerun the script after "reconfiguring" (removing zip-code weighting from scoring), show the flag disappearing. Demonstrates what a clean audit looks like.
- Teardown angle: The model didn't intend to discriminate. It learned from the agent's behavior. The audit doesn't require a data scientist — it requires a spreadsheet export, five checks, and the willingness to look.
- Exclusions: Don't attempt to integrate with real CRM APIs; don't run a formal statistical disparate-impact analysis; don't go into the SafeRent legal case details.
- Score: 7/10
