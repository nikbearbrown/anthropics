# AI for Realtors (NBB) — CLI Video Ideas ("X with Claude")

> Note: ai-for-realtors-nbb shares identical chapter content with ai-for-realtors. Cards below
> are identical in concept but numbered independently and may be built as separate reels with
> a different audience register if desired (e.g., a Nik Bear Brown / NBB voice variant).

## Candidate 01 — "Audit Your Listing Copy for Fair Housing Violations with Claude"
- Source: ai-for-realtors-nbb/chapters/06-fair-housing-and-ai-the-72-gap.md
- Lane: RESEARCH (Claude assistant)
- Hook: 72% of agents using AI for listing copy have never had Fair Housing training — and the phrases Claude flags as natural ("family-friendly," "young professionals," "close to worship centers") are the ones NAR says create liability.
- The artifact: A side-by-side before/after listing description with every at-risk phrase highlighted in a color-coded table — familial status (red), age-coded (orange), religious (yellow), neighborhood-coded (purple) — plus a rewritten clean version with replacement language for each phrase.
- Prompt seed: `claude "Review this listing description for potential Fair Housing violations under the seven high-risk pattern types from NAR guidance. For each flagged phrase, name the protected class implicated, explain why AI generates it, and suggest a property-feature replacement. Then rewrite the full description with all violations removed."`
- Read / check: Verify that flagged phrases match the chapter's seven categories (not just generic "bias"). Check that the replacement language describes property features, not people. Confirm the rewritten version contains zero people-descriptive phrases.
- Human supplies (Claude can't): Nothing — a synthetic listing seeded from the chapter's examples is fully acceptable for the video.
- Output medium: Manim (animated table where risk phrases light up one by one by category color, then the rewrite plays as text substitution)
- The change: Ask Claude to audit for omission patterns — does the listing consistently omit school quality, transit, or amenity mentions in certain neighborhoods? Show the invisible bias of what is NOT said.
- Teardown angle: The AI generated the violations because it trained on decades of steering-adjacent copy — the model's fluency is the problem, not the fix. Only human review with a checklist closes the gap.
- Exclusions: Don't drill into Freddie Mac AVM-bias research; don't audit photos; don't go into SafeRent case law details.
- Score: 9/10

---

## Candidate 02 — "Measure AVM Error Range with Claude: What Zestimate Can't See"
- Source: ai-for-realtors-nbb/chapters/05-the-avm-trap-what-zestimate-can-and-cannot-do.md
- Lane: BUILD (Claude Code)
- Hook: A $600,000 Zestimate within Zillow's own stated 20% error band could be any price from $480K to $720K — that's a $240,000 spread wearing a single confident number.
- The artifact: An animated error-band visualization — a horizontal bar centered on a synthetic Zestimate with the 5%/10%/20% confidence rings drawn on either side, labeled with dollar values. A second panel shows how the band widens for off-market vs on-market (1.74% vs 7.20% median error).
- Prompt seed: `claude "Write a Python script using matplotlib that animates a Zestimate error band visualization. Input: a home value and Zillow's published accuracy stats (5%/10%/20% bands for on-market and off-market). Output: an animated MP4 showing the confidence rings expanding from the center price, with dollar labels. Add a toggle between on-market (1.74% median error) and off-market (7.20%) that visually widens the band."`
- Read / check: Verify the dollar arithmetic (20% of $600K = $120K each side = $480K–$720K). Confirm the on-market vs off-market figures match Zillow's published methodology page. Check the animation is readable at video resolution.
- Human supplies (Claude can't): Verify current Zillow accuracy statistics before recording — figures may shift. Zillow's published numbers are public; synthetic home value is fine.
- Output medium: Manim (animated error band with expanding rings and dollar labels)
- The change: Add a "condition blindness" slider — drag to show how a kitchen renovation or deferred roof shifts the true price outside the model's confidence band.
- Teardown angle: The AVM's confidence is a function of data density, not truth. The five failure conditions are precisely where the CMA earns its fee.
- Exclusions: Don't go into the federal AVM quality-control rule for lenders; don't compare AVMs across platforms; don't discuss appraisal licensing.
- Score: 9/10

---

## Candidate 03 — "Build a CRM Lead Scoring Audit with Claude"
- Source: ai-for-realtors-nbb/chapters/10-lead-scoring-crm-ai-and-the-fair-housing-audit-youre-not-running.md
- Lane: BUILD (Claude Code)
- Hook: A CRM that learned from your call-back patterns can silently amplify zip-code bias — and most agents have never run the 5-step audit that would catch it.
- The artifact: A Python script that takes a CSV of CRM leads (synthetic) and outputs three charts: geographic cluster analysis, price-band distribution (high-scored vs all leads), source/campaign breakdown — animated to reveal skew when it exists.
- Prompt seed: `claude "Write a Python script that takes a CSV of real-estate CRM leads with columns (lead_id, zip_code, price_range, source, crm_score) and produces three animated charts: zip code distribution for all vs top-quartile leads, price band comparison, source breakdown. Flag any zip code >2x over-represented in top-quartile vs overall. Generate synthetic data if no CSV is provided."`
- Read / check: Confirm the synthetic data generator creates a detectable clustering pattern. Verify charts are labeled clearly at video resolution. Check the 2x threshold fires correctly.
- Human supplies (Claude can't): Nothing — fully synthetic.
- Output medium: screen-recording mp4
- The change: Regenerate data with geographic weighting removed — show the flag disappears.
- Teardown angle: The model learned from agent behavior. The audit requires a spreadsheet export and five checks.
- Exclusions: Don't attempt real CRM API integration; don't run formal statistical analysis; don't go into SafeRent case law.
- Score: 8/10

---

## Candidate 04 — "Build the Defensible AI Workflow File with Claude"
- Source: ai-for-realtors-nbb/chapters/13-building-your-ai-workflow-fast-and-defensible.md
- Lane: BUILD (Claude Code)
- Hook: Two agents publish identical AI-generated listing copy. One has a documented file. One doesn't. A complaint arrives. They are not in the same position.
- The artifact: A Python script that takes a property description as input and generates a complete defensible-file folder: source_facts.md, ai_draft.md, audit_checklist.md (Fair Housing + factual accuracy + pricing framing), review_notes.md.
- Prompt seed: `claude "Given this property description, generate: (1) a source_facts template, (2) the AI listing draft, (3) a Fair Housing audit checklist with NAR's seven high-risk patterns, (4) a review_notes template. Output as four markdown files."`
- Read / check: Verify all seven Fair Housing pattern categories appear in the checklist. Check the source_facts template asks for condition, pricing basis, square footage.
- Human supplies (Claude can't): Nothing — fully synthetic.
- Output medium: screen-recording mp4
- The change: Run on a second property with a Fair Housing red flag in the input — show the checklist catching it.
- Teardown angle: Documentation isn't bureaucracy — it's the evidence that you did your job.
- Exclusions: Don't build a full CRM integration; don't go into California AB 723 specifically; don't cover team supervision.
- Score: 8/10

---

## Candidate 05 — "Research AVM Racial Bias: What the Studies Found with Claude"
- Source: ai-for-realtors-nbb/chapters/05-the-avm-trap-what-zestimate-can-and-cannot-do.md + chapters/06-fair-housing-and-ai-the-72-gap.md
- Lane: RESEARCH (Claude assistant)
- Hook: AVMs systematically undervalue Black-owned homes — not because of intent, but because they trained on data that encodes a century of discriminatory appraisal practices.
- The artifact: A sourced 4-event animated timeline: Freddie Mac 2021 finding → Urban Institute 2024 confirmation → federal AVM quality-control rule (2024/2025) → mechanism (historical data encoding historical discrimination).
- Prompt seed: `claude "Research the peer-reviewed evidence on racial valuation gaps in automated valuation models. Synthesize the Freddie Mac 2021 study, Urban Institute 2024 research, and the federal interagency AVM quality-control final rule. For each source, cite specifically, summarize the key finding in one sentence, and explain the structural mechanism."`
- Read / check: Verify cited studies are real. Confirm federal rule citation (effective date, issuing agencies). Check the mechanism explanation matches source text.
- Human supplies (Claude can't): Verification of specific statistics against the actual reports — Claude may mis-attribute figures. Human must click through to confirm.
- Output medium: Manim (animated 4-event timeline with source labels)
- The change: Add a fifth event — the agent's professional obligation even without being subject to the lender rule.
- Teardown angle: The AVM isn't malicious — it learned from redlining outcomes. The bias persists regardless of intent.
- Exclusions: Don't cover the full redlining history; don't compare AVMs across vendors; don't cover appraisal licensing reform.
- Score: 8/10

---

## Candidate 06 — "Simulate the Contract Stack: What AI Summary Misses with Claude"
- Source: ai-for-realtors-nbb/chapters/08-contract-and-document-ai-what-the-summary-misses.md
- Lane: RESEARCH (Claude assistant)
- Hook: The AI summary said the buyer had a standard inspection contingency. The addendum waived it. The summary wasn't lying — it just never read the addendum.
- The artifact: A Manim-animated "stack reveal" showing base contract summary vs full stack reality — provisions changing or disappearing as each addendum layer adds.
- Prompt seed: `claude "I am going to give you a simulated residential transaction document stack: a base purchase agreement + three addenda. Summarize the base contract alone. Then summarize the full stack. List every provision that changed between the two summaries, classified as: contingency waiver, deadline modification, price term change, or custom/handwritten addition."`
- Read / check: Verify the summary-alone vs full-stack comparison catches the simulated inspection waiver. Confirm all six checklist categories are surfaced.
- Human supplies (Claude can't): The synthetic document stack (base CAR purchase agreement structure + 3 addenda with deliberate modifications). Create from chapter examples.
- Output medium: Manim (animated document stack reveal)
- The change: Run the 6-item checklist against the same stack — show how it catches the waiver the summary missed.
- Teardown angle: The AI summary is useful for orientation. The six-item checklist is the work.
- Exclusions: Don't attempt to simulate actual California CAR forms; don't give legal advice; don't cover HOA addenda in depth.
- Score: 7/10

---

## Candidate 07 — "Build a CMA vs AVM Comparison Tool with Claude"
- Source: ai-for-realtors-nbb/chapters/05-the-avm-trap-what-zestimate-can-and-cannot-do.md
- Lane: BUILD (Claude Code)
- Hook: Zillow says $640K. The CMA says $590K. The agent who can explain each adjustment wins the listing appointment.
- The artifact: A Python script that outputs a two-column comparison table: AVM estimate vs CMA adjusted, with each CMA adjustment labeled and its dollar impact shown as an animated bar.
- Prompt seed: `claude "Given this property's data, generate: (1) a simulated AVM estimate, (2) a CMA with explicit adjustments for condition, micro-neighborhood, renovation value, and active buyer demand. Display as a two-column comparison table where each CMA adjustment shows its dollar impact."`
- Read / check: Verify the AVM and CMA produce different numbers. Confirm adjustment labels match the chapter's five CMA-vs-AVM dimensions.
- Human supplies (Claude can't): Nothing — fully synthetic from chapter examples.
- Output medium: Manim (animated bar chart where CMA adjustments appear one at a time)
- The change: Add confidence range bands around both numbers, showing they overlap more than point estimates suggest.
- Teardown angle: The agent's value is in explaining each adjustment specifically — not in having a different number.
- Exclusions: Don't build a real AVM model; don't use actual Zillow API; don't attempt real market data.
- Score: 7/10

---

## Candidate 08 — "Write Your Delegate/Guard AI Workflow with Claude"
- Source: ai-for-realtors-nbb/chapters/13-building-your-ai-workflow-fast-and-defensible.md
- Lane: RESEARCH (Claude assistant)
- Hook: Two agents, same tools, same deadline pressure. One has a Delegate/Guard list. The other improvises — gambling on their own attention every time.
- The artifact: A filled-in Delegate/Guard table for 12 common agent tasks — classified, audit steps written for each Delegate task, Guard tasks with a one-sentence rule. Animated as a two-column table filling in row by row.
- Prompt seed: `claude "Classify these 12 real estate tasks as Delegate or Guard: listing copy drafting, CMA pricing recommendation, Fair Housing compliance review, CRM lead prioritization, contract clause summary, negotiation timing judgment, market summary for client, disclosure adequacy determination, email follow-up drafting, virtual staging approval, inspection summary for buyer, MLS photo selection. For each Delegate task, write the specific audit checklist steps. For each Guard task, write a one-sentence rule."`
- Read / check: Verify the classification matches the chapter's framework. Check audit checklist steps are specific and traceable to chapter risk types.
- Human supplies (Claude can't): Nothing — fully synthetic.
- Output medium: Manim (animated two-column table, Delegate in blue, Guard in amber)
- The change: Add a "misclassification consequence" column — what happens if each Guard task is mistakenly treated as Delegate?
- Teardown angle: Workflow is the operating system. The checklist takes more time than publishing the first draft and less time than responding to a complaint.
- Exclusions: Don't build a digital tool; don't go into team supervision; don't cover brokerage E&O.
- Score: 7/10

---

## Candidate 09 — "Research the AI Tools Hidden in Your Workflow with Claude"
- Source: ai-for-realtors-nbb/chapters/03-the-ai-tools-in-your-workflow.md
- Lane: RESEARCH (Claude assistant)
- Hook: An agent who thinks they're "not really using AI yet" checks Zillow, uses virtual staging, reads CRM scores, and asks a chatbot to summarize the inspection report — five AI-powered decisions before lunch.
- The artifact: A sourced five-row table mapping AI tool categories (valuation, media alteration, lead prioritization, document summary, scheduling automation) to their failure modes, platform disclaimers, and minimum review requirements. Animated row by row.
- Prompt seed: `claude "Research the AI capabilities embedded in Zillow Zestimate, ShowingTime, Follow Up Boss lead scoring, virtual staging tools, and AI document summary tools. For each: (1) the mechanism, (2) the platform's own stated limitations, (3) the primary failure mode, (4) the minimum professional review required. Cite platform documentation where available."`
- Read / check: Verify Zillow's "not an appraisal" disclaimer is correctly cited. Check each failure mode matches the chapter's taxonomy.
- Human supplies (Claude can't): Verification that platform documentation URLs are current — human must click through to confirm disclaimer language is live.
- Output medium: Manim (animated 5-row table building row by row)
- The change: Apply the three-question audit card to one tool: what data? what kind of output? what decision?
- Teardown angle: The platforms are useful. The compliance posture is "know which category each tool belongs to and apply the right review."
- Exclusions: Don't go into California AB 723; don't cover brokerage-level policy; don't build anything.
- Score: 7/10

---

## Candidate 10 — "Generate the Self-Review Failure: Why AI Can't Audit Its Own Fair Housing Output"
- Source: ai-for-realtors-nbb/chapters/06-fair-housing-and-ai-the-72-gap.md
- Lane: RESEARCH (Claude assistant)
- Hook: The agent asks the AI tool to review its own listing copy for Fair Housing violations. The tool flags three phrases. The agent makes the changes and publishes. The complaint arrives anyway — for the phrase the tool missed.
- The artifact: A research brief demonstrating the self-review failure: (1) AI-generated listing with five violations, (2) AI self-review output (showing what it flags and what it misses), (3) human audit output (showing the complete catch). Displayed as a three-column Manim comparison.
- Prompt seed: `claude "Generate a listing description that contains five Fair Housing violations from NAR's seven high-risk patterns. Then audit your own output for Fair Housing issues. Finally, I will audit the output independently. We will compare what the self-review caught vs. what remains. Do NOT reveal the violations you planted — generate the listing first, then audit it separately."`
- Read / check: Verify the self-review misses at least one violation (set up the prompt so a locally-coded neighborhood descriptor is included that the model is unlikely to flag). Confirm the human audit catches the full set.
- Human supplies (Claude can't): Local market knowledge to include a neighborhood descriptor that is coded in a specific metro but would appear innocuous to a nationally-trained model. This is the one place real local knowledge is irreplaceable.
- Output medium: Manim (three-column table: violations planted / AI self-review flagged / human audit flagged)
- The change: Repeat with a second listing that uses only locally-coded language (no generic Fair Housing terms) — show that the self-review catches zero violations while the human audit catches all of them.
- Teardown angle: The model reviewing its own output has the same structural limitation as the model generating it. Review must be performed by someone who knows what to look for — not by the same model.
- Exclusions: Don't turn this into a legal advice video; don't attempt to identify real cities by name; don't go into the SafeRent settlement details.
- Score: 7/10
