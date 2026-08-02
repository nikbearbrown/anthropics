# MBA Marketing: with LLMs — CLI Video Ideas ("X with Claude")

Lane: BUILD+RESEARCH (quantitative marketing models → BUILD; strategy/behavior/policy analysis → RESEARCH)
Book: mba-marketing (22 substantive chapters covering consumer behavior, segmentation, pricing, digital marketing, product development, promotion mix)

---

## Card 1 — Customer Value Ratio Analyzer

**Source:** Chapter 2 (Marketing and Customer Value) — V = B/P model, four B-layers (functional, monetary, social, psychological), Gatorade vs. Powerade 67.7% market share puzzle
**Lane:** BUILD
**Hook:** Gatorade has 67.7% of its market. Powerade is made by Coca-Cola. In a blind taste test you can't tell them apart. The difference is entirely in B — the perceived benefit numerator. Claude builds the B/P decomposition for any product comparison and shows which layer is doing the most work.
**The artifact:** A Python script that takes two competing products with user-supplied benefit scores across four layers (functional/monetary/social/psychological) and a price, computes V = B/P for each, decomposes the B gap into layers, and produces a Manim animated stacked bar showing where the value advantage lives.
**Prompt seed:** `claude "Build a customer value ratio analyzer. Inputs: two products with price and four benefit scores (functional, monetary, social, psychological) rated 1-10. Compute: B_total = weighted sum, V = B/P. Produce: (1) a stacked bar chart showing B decomposition for each product; (2) an arrow annotating the V gap; (3) a sensitivity analysis: which single benefit layer, if raised 20%, would most improve Product B's V ratio? Animate in Manim."`
**Read/check:** Verify the V = B/P framework from Chapter 2. Confirm the four layers (functional, monetary, social, psychological) match the chapter's pyramid infographic. Verify Gatorade's 67.7% share is accurately cited.
**Human supplies:** Benefit scores (1-10) for each layer for both products, and both prices. The video uses synthetic scores for Gatorade vs. Powerade calibrated to match the chapter's narrative. Synthetic scores are fine for the video.
**Output medium:** Manim animated stacked bar — two bars (Product A / Product B) build layer by layer (functional → monetary → social → psychological); the V ratio appears as a label above each bar; the gap arrow animates; sensitivity result highlights which layer to invest in.
**The change:** Cut Product B's price by 15% — watch V improve immediately, then ask Claude to compare the B-raising strategy vs. the price-cutting strategy. Claude should show: price cut is instantly copyable; brand B-raising is durable but slow. Narrate: "The fraction looks symmetric. The strategy isn't."
**Teardown angle:** Ask Claude which of the four B-layers is hardest to replicate (social and psychological — built through decades of marketing, not purchasable) and which is easiest (functional — product improvement). This surfaces why market leaders persist.
**Exclusions:** No conjoint analysis or willingness-to-pay econometrics (Chapter 2 covers the conceptual model; measurement methods are in Chapter 8).
**Score:** 9/10 — clean BUILD artifact (the stacked bar is visually instructive), the Gatorade puzzle is a compelling hook, the price-cut change has a strong narrative payoff, and the teardown produces strategic insight.

---

## Card 2 — Consumer Buying Behavior Mapper

**Source:** Chapter 5 (Consumer Markets and Purchasing Behavior) — Pepsi Challenge paradox (blind taste vs. branded experience), five categories of influence (cultural/social/personal/psychological/situational), five-stage decision process, four buying-behavior types
**Lane:** RESEARCH
**Hook:** Coca-Cola drinkers chose Pepsi in blind taste tests. Then kept buying Coke. The brand is part of the product — but which of the five influence categories explains it? Claude maps the buyer's black box for any product category.
**The artifact:** A buyer behavior analysis report: given a product category and target segment, Claude outputs (1) which of the five influence categories is dominant for this purchase; (2) where in the five-stage decision process most customers drop off or can be influenced; (3) which of the four buying-behavior types (complex, dissonance-reducing, habitual, variety-seeking) governs this category; (4) three specific marketing interventions calibrated to the dominant influence and buying type.
**Prompt seed:** `claude "Map the consumer buying behavior for the following product category: [category] targeting [segment]. Apply five frameworks: (1) identify the dominant influence category (cultural, social, personal, psychological, or situational) and give one example from this category; (2) trace the five-stage decision process — where do customers most often drop off? (3) classify the buying behavior type (complex/dissonance-reducing/habitual/variety-seeking); (4) prescribe three marketing interventions tailored to the dominant influence and behavior type."`
**Read/check:** Verify the Pepsi Challenge story from Chapter 5 — confirm the branded-vs-unbranded distinction is correctly represented. Verify the four buying-behavior types (complex, dissonance-reducing, habitual, variety-seeking) from Chapter 5. Confirm the five decision-process stages.
**Human supplies:** A product category and target segment description (2-3 sentences). The video uses two contrasting examples: (a) luxury sneakers (social factor dominant, complex buying behavior) and (b) store-brand detergent (habitual, situational). Synthetic examples are fine.
**Output medium:** Manim animated black-box diagram — inputs (stimuli) on the left; five influence categories illuminate in order of relevance for this category; five-stage decision funnel on the right with drop-off arrows; buying-behavior type label appears at the bottom; three interventions appear as annotated action cards.
**The change:** Switch the segment from Gen-Z urban to Baby Boomer suburban — watch the dominant influence category shift (social/psychological → personal/situational), buying behavior shift (complex → habitual), and all three interventions change. Narrate: "Same product, different customer — completely different marketing."
**Teardown angle:** Ask Claude to identify the one situational factor in this category that the firm can control most easily (in-store atmospherics, e.g.) and estimate what behavior change it would produce. This surfaces the underrated situational lever from Chapter 5.
**Exclusions:** No neuromarketing or eye-tracking analysis. No conjoint analysis of attribute preferences (that's in Chapter 8).
**Score:** 8/10 — the Pepsi/Coke paradox is one of the most famous illustrations in marketing, the five-category → four-behavior-type structure gives the video multiple distinct beats, and the segment-switch change produces a genuinely different prescription.

---

## Card 3 — Segmentation Scoring Model

**Source:** Chapter 7 (Market Segmentation, Targeting, and Positioning) — STP framework, four segmentation bases (geographic/demographic/psychographic/behavioral), evaluating segment attractiveness (measurable, substantial, accessible, differentiable, actionable)
**Lane:** BUILD
**Hook:** The STP framework says: segment the market, target the best segment, position to win it. But which segment is "best"? Claude builds a scoring model that rates every candidate segment on five attractiveness criteria and ranks them.
**The artifact:** A Python script that takes: a product, a list of candidate segments (each described with geographic/demographic/psychographic/behavioral tags), and scores each segment on five criteria (measurable, substantial, accessible, differentiable, actionable — each 1-5). Outputs a ranked segment table and a Manim animated scoring grid with an overall segment-attractiveness index.
**Prompt seed:** `claude "Build a segment attractiveness scoring model for a new B2C fitness app. Evaluate four candidate segments: (1) Urban Millennials 25-35 gym-goers, (2) Suburban parents 35-50 time-constrained, (3) College students 18-24 fitness-curious, (4) Boomers 55+ health-motivated. Score each on 5 criteria (1-5): measurable (can we quantify this segment?), substantial (large enough to be profitable?), accessible (can we reach them?), differentiable (will they respond differently to our offer?), actionable (can we build a program for them?). Output a ranked table and recommend the primary target."`
**Read/check:** Verify the five attractiveness criteria from Chapter 7 (measurable, substantial, accessible, differentiable, actionable). Confirm the four segmentation bases match the chapter's taxonomy.
**Human supplies:** A product/service description and 3-5 candidate segment descriptions. The video uses the fitness app scenario with synthetic segments. Real use: the marketer supplies their own candidate segments with supporting data. Synthetic is acceptable for the video.
**Output medium:** Manim animated scoring grid — each segment's five criteria bars fill sequentially (grey → color); overall attractiveness index appears as a final score badge; segments rank from top to bottom by index score with the winner highlighted.
**The change:** Add a constraint — the marketing budget is limited to digital-only channels. Re-run the scoring, reducing the "accessible" score for segments with low digital engagement (e.g., Boomers 55+). Watch the ranking shift. Narrate: "Channel constraints change who is actually your best segment, even if they look attractive on paper."
**Teardown angle:** Ask Claude to write the positioning statement for the top-ranked segment using the Chapter 7 format: "For [target segment], [brand] is the [frame of reference] that [point of difference] because [reason to believe]." This connects the scoring output directly to executional marketing.
**Exclusions:** No psychographic profiling data (VALS, Nielsen Prizm — those require licensed databases). No competitive positioning map against named competitors (that would require primary research data).
**Score:** 9/10 — the scoring grid is a directly usable tool, the budget-constraint change shows real-world prioritization trade-offs, and the positioning-statement teardown delivers a complete STP pipeline. Highly practical BUILD artifact.

---

## Card 4 — New Product Launch Scorecard (Seven-Stage Filter)

**Source:** Chapter 13 (Maintaining a Competitive Edge with New Offerings) — Dollar Shave Club case, five new-product categories, seven-stage development process, concept testing as the most underinvested stage, failure rates (50-80%)
**Lane:** RESEARCH
**Hook:** Most new products fail. Dollar Shave Club beat Gillette with a funny video and three true consumer insights. Claude runs any new product idea through all seven development stages and flags which ones it would fail — before any money is spent.
**The artifact:** A new-product launch scorecard: given a product idea description, Claude evaluates it against all seven stages (idea generation → screening → concept development → marketing strategy → business analysis → product development → commercialization). For each stage, it identifies the key question, the likely answer for this product, and a red/yellow/green risk flag. Final output: a go/proceed-with-caution/kill recommendation with the single highest-risk stage highlighted.
**Prompt seed:** `claude "Run a new product development audit for the following idea: [describe product]. Evaluate all seven development stages: (1) Idea Generation — what market insight does this idea address? (2) Idea Screening — does it fit firm strategy and address a real need? (3) Concept Development — what are the three strongest concept variants? Which is most differentiated? (4) Marketing Strategy — target segment, positioning, price range, distribution approach. (5) Business Analysis — estimate revenue, cost, profitability threshold. (6) Product Development — what is the highest-technical-risk feature? (7) Commercialization — what is the go-to-market channel sequence? Flag each stage Red/Yellow/Green and give a final recommendation."`
**Read/check:** Verify the seven stages from Chapter 13 and the claim that concept testing is the most underinvested stage. Confirm the Dollar Shave Club case details (Unilever acquisition for $1B in 2016, five years after launch). Confirm failure rate range (50-80%).
**Human supplies:** A new product idea description — 2-3 paragraphs describing what it is, who it serves, and why it would be different. The video uses the yogurt powder concept from Chapter 13 as the example. Synthetic ideas are fine.
**Output medium:** Manim animated seven-stage pipeline — stages light up one by one; each stage's risk flag (red/yellow/green) appears as a badge; the highest-risk stage pulses; the final recommendation appears as a summary panel.
**The change:** Reveal that concept testing has not been done (a realistic omission in most failed launches) — ask Claude to re-score Stage 3 red and explain what happens when an unvalidated concept reaches Stage 5 (business analysis based on assumptions rather than evidence). The whole pipeline turns more red. Narrate: "The stage you skip is the stage that kills you."
**Teardown angle:** Ask Claude to design a minimum viable concept test for this product — describe who to interview, what to show them, and what a positive signal looks like. This gives the viewer the Chapter 13 recommendation made operational.
**Exclusions:** No IP analysis (that's mba-intellectual-property). No financial modeling of NPV/IRR for the launch (that's mba-corporate-finance territory).
**Score:** 8/10 — the seven-stage structure creates natural video beats, the skip-concept-testing change is dramatically instructive, and the minimum viable concept test teardown is immediately actionable. Strong RESEARCH artifact.

---

## Card 5 — Digital Marketing Funnel Analyzer

**Source:** Chapter 19 (Direct, Online, Social Media, and Mobile Marketing) — Apple ATT and Meta's $10B hit, funnel metrics by stage, attribution problem (last-click vs. multi-touch), ROI as the governing metric, influencer FTC disclosure requirements
**Lane:** BUILD
**Hook:** A campaign produced a million clicks and fifty purchases. Another produced a hundred thousand clicks and five thousand purchases. Which one worked? Claude builds the funnel model and solves the attribution problem — then calculates true ROI.
**The artifact:** A Python digital marketing funnel calculator: inputs are campaign data by channel (spend, impressions, clicks, conversions, revenue) for multiple channels (paid search, social, email, organic). Outputs: (1) CTR, conversion rate, CPC, CPA for each channel; (2) attributed revenue by last-click and multi-touch models; (3) ROI by channel; (4) Manim animated funnel diagram with metric labels at each stage; (5) the channel with best ROI highlighted.
**Prompt seed:** `claude "Build a digital marketing funnel analyzer. Input campaign data: channels=[search, social, email, organic], each with: spend, impressions, clicks, conversions, revenue. Compute for each channel: CTR=clicks/impressions, conv_rate=conversions/clicks, CPC=spend/clicks, CPA=spend/conversions, ROI=(revenue-spend)/spend. Run two attribution models: (1) last-click (100% credit to final channel); (2) equal multi-touch (credit split evenly across all channels touched). Animate a funnel in Manim with metrics at each stage. Flag the highest-ROI channel."`
**Read/check:** Verify the CTR/CPC/CPA/ROI formulas from Chapter 19. Confirm the Apple ATT/Meta $10B revenue impact story. Verify that the FTC disclosure requirement (#ad) is accurately cited for influencer content.
**Human supplies:** Campaign performance data by channel — impressions, clicks, conversions, revenue, spend. The video uses synthetic data calibrated to realistic digital marketing benchmarks (Google Ads: CTR ~3-5%, conv rate ~2-4%; social: CTR ~0.5-1%, conv rate ~1-2%). Synthetic data is fine.
**Output medium:** Manim animated funnel — each stage (impressions → clicks → conversions → revenue) narrows with metric labels; channel bars appear side by side at the bottom showing ROI by channel; attribution comparison table shows last-click vs. multi-touch split.
**The change:** Apply the Apple ATT scenario — reduce social channel's impression tracking accuracy by 40% (simulating loss of user-level data). Watch social CPA appear to rise (less attributed revenue) while the actual conversion count doesn't change. Narrate: "The channel didn't get worse. The measurement got worse. That's the ATT effect."
**Teardown angle:** Ask Claude to recommend which channel to cut and which to increase, given the ROI ranking — and flag the attribution uncertainty as a reason to run a holdout test before making final budget cuts. This surfaces the "don't optimize on bad attribution" lesson.
**Exclusions:** No A/B test significance calculator (that requires statistical methods not covered in Chapter 19). No programmatic bidding strategy.
**Score:** 9/10 — the funnel animation is a classic marketing visual done in code; the ATT change moment is vivid and timely; the attribution-uncertainty teardown is sophisticated but expressible simply. Strong BUILD artifact.

---

## Card 6 — Pricing Strategy Selector

**Source:** Chapter 15 (Pricing Products and Services) — Amazon Prime case, five Cs of pricing (cost, customers, channels, competition, compatibility), value-based vs. cost-plus pricing, price elasticity
**Lane:** BUILD
**Hook:** Amazon sets Prime's price not based on what it costs to run Prime — but on the behavioral change that happens at $119/year (members spend 4.6× more than non-members). Claude builds the pricing decision model and shows when value-based pricing beats cost-plus.
**The artifact:** A Python pricing strategy tool: given cost structure, elasticity estimate, and competitor prices, Claude computes: (1) cost-plus price (cost × (1 + margin)); (2) value-based price (customer WTP estimate based on described value drivers); (3) competitive price (relative to market midpoint); (4) a sensitivity table showing revenue and profit at five price points. Animates the demand curve with the three pricing anchors marked.
**Prompt seed:** `claude "Build a pricing strategy model for the following product: [describe]. Inputs: unit_cost=X, target_margin=Y, elasticity=-1.5, competitor_price=Z, WTP_estimate=W (derived from described value). Compute: (1) cost_plus_price=unit_cost*(1+margin); (2) value_based_price=WTP_estimate*0.85 (capture 85% of WTP); (3) competitive_price=competitor_price*1.05. For each price point, compute: revenue=price*quantity(price), profit=revenue-unit_cost*quantity(price). Build demand curve in Manim with three anchor prices marked. Recommend optimal price."`
**Read/check:** Verify the five Cs of pricing from Chapter 15 (cost, customers, channels, competition, compatibility). Confirm Amazon Prime statistic (members spend 4.6× more — verify against Chapter 15 or published sources). Verify the elasticity-revenue rule from Chapter 15.
**Human supplies:** Cost structure (unit cost, fixed costs) and competitor price. WTP estimate derived from the product description — Claude can infer it from described value drivers. Synthetic numbers are fine for the video; real use requires customer research or conjoint analysis data.
**Output medium:** Manim animated demand curve — curve sweeps across the frame; three price anchors (cost-plus, value-based, competitive) appear as vertical lines with revenue rectangles; the optimal price (highest profit) highlights; sensitivity table populates below.
**The change:** Increase the elasticity magnitude from -1.5 to -2.5 (more price-sensitive market) — watch the optimal price shift down, value-based advantage shrink, and competitive price become the most defensible anchor. Narrate: "Elasticity determines which pricing strategy is valid. Don't pick a strategy before you know your elasticity."
**Teardown angle:** Ask Claude to recommend one value-adding feature that would shift the demand curve right (increase WTP) rather than reducing price — and estimate the revenue impact of a WTP increase of $5 vs. a price cut of $5. The value-raising strategy almost always wins on margin.
**Exclusions:** No price discrimination / yield management (Chapter 15 covers this but it requires a separate card). No auction pricing (out of scope).
**Score:** 9/10 — demand curve animation is a classic economics visualization done in code; the Amazon Prime hook is vivid; the elasticity-change demonstrates the model's practical sensitivity; the WTP-raising teardown delivers the chapter's core strategic lesson.

---

## Card 7 — Marketing Research Survey Designer

**Source:** Chapter 8 (Marketing Research and Market Intelligence) — LEGO gender study, seven-step research process, primary vs. secondary data, survey design pitfalls (leading questions, double-barreled questions), concept testing
**Lane:** RESEARCH
**Hook:** LEGO discovered that girls played with LEGO as long as boys — but didn't feel the brand was for them. That insight came from a two-year ethnographic study, not a survey. Claude designs the right research method for any marketing question — and flags the common design errors that produce misleading data.
**The artifact:** A marketing research design document: given a marketing question, Claude outputs (1) research objectives (what decision will this research inform?); (2) recommended method (survey, focus group, ethnographic observation, secondary data, A/B test) with rationale; (3) if survey — a 5-question draft with error analysis (leading questions flagged, scales validated); (4) sample design (who to recruit, n, sampling strategy); (5) analysis plan.
**Prompt seed:** `claude "Design a marketing research study to answer the following business question: [question]. Apply the seven-step process: (1) Define the problem and research objectives; (2) Develop the research plan — recommend one primary method (survey/focus group/observation/experiment) and one secondary source; (3) Draft 5 survey questions if survey is recommended — check each for leading language, double-barreled structure, or social desirability bias; (4) Specify sample: n, sampling method, recruitment channel; (5) Outline the analysis approach and what a positive/negative finding would look like."`
**Read/check:** Verify the seven-step research process from Chapter 8. Confirm LEGO's gender study methodology (two-year ethnographic observation, not survey). Verify the common survey errors the chapter discusses (leading questions, double-barreled questions, social desirability).
**Human supplies:** A marketing question — what business decision needs research support? The video uses two contrasting questions: (a) "Should we extend our brand into a new category?" (requires concept testing) and (b) "Why are customers churning?" (requires qualitative investigation). Synthetic scenarios are fine.
**Output medium:** Manim animated seven-step pipeline — each step populates with the research decision for this question; if survey, questions appear on screen with error flags highlighted in red; sample design appears as a final specs card.
**The change:** Reveal that the team chose a survey but wrote leading questions ("How much do you agree that our product's sustainability features are important to you?"). Ask Claude to rewrite the question to be neutral. Watch the question transform and the likely response distribution change. Narrate: "The question you ask determines the answer you get — not the truth."
**Teardown angle:** Ask Claude to estimate the cost and timeline of the recommended research design and compare it to the cost of launching the product without research. This makes the ROI of market research explicit — and connects back to the Chapter 13 lesson about skipping concept testing.
**Exclusions:** No advanced statistical analysis (regression on survey data — that's mba-economics territory). No biometric/neuromarketing research methods.
**Score:** 8/10 — the LEGO study is a compelling hook (counter-intuitive finding from rigorous research), the question-rewriting change is concrete and demonstrable, and the cost/timeline teardown grounds the abstract research process in real budget terms.

---

## Card 8 — IMC Message Consistency Auditor

**Source:** Chapter 16 (Integrated Marketing Communications) — Peloton controversy (TV ad + earned media = 172% sales surge during COVID), six promotion mix tools, seven-element communication process, message encoding/decoding gap
**Lane:** RESEARCH
**Hook:** Peloton's ad was called sexist. It produced a Twitter storm. Then COVID hit and Peloton's sales rose 172%. The controversy created awareness that converted when the market shifted. Claude audits a brand's IMC for message consistency — and flags where encoding and decoding diverge.
**The artifact:** An IMC consistency audit: given a brand's messaging samples across multiple channels (ad copy, social post, PR statement, email subject line, website hero), Claude (1) extracts the implied brand promise from each channel; (2) scores consistency across channels (1-5); (3) identifies decoding risks — where a target audience might read the message differently than intended; (4) recommends three specific changes to unify the message.
**Prompt seed:** `claude "Audit the integrated marketing communications for the following brand: [brand description]. Review these channel messages: Ad copy: [paste]. Social post: [paste]. PR statement: [paste]. Email: [paste]. Website: [paste]. Extract: (1) the implied brand promise from each channel; (2) a consistency score (1-5) across all channels — are they saying the same thing? (3) the two highest decoding risks — where could the target audience misread the message? (4) three specific edits to unify the message across channels."`
**Read/check:** Verify the Peloton case from Chapter 16 (2019 ad, social media eruption, COVID surge in 2020-2021, 172% sales growth). Confirm the seven-element communication process (sender → encoding → message → media → receiver → decoding → feedback) from Chapter 16.
**Human supplies:** Channel message samples — the brand's actual ad copy, social posts, PR statement, email subject lines, and website copy. For the video, use synthetic samples for a fictional sustainable apparel brand showing inconsistent messaging (aspirational on social, transactional in email, corporate in press release). Synthetic samples are fine.
**Output medium:** Manim animated message consistency matrix — rows are channels, columns are key brand dimensions (tone, promise, audience assumed); cells filled with extracted message and a consistency color (green/yellow/red); the two highest-risk cells pulse; three edit recommendations appear as overlays.
**The change:** Add a crisis scenario — the brand's manufacturer was just exposed for labor violations. Ask Claude to re-audit: which channel messages are now most damaging (aspirational sustainability claims become hypocrisy in the new context)? Which should be pulled or revised immediately? The matrix turns red in the sustainability-claim cells.
**Teardown angle:** Ask Claude to draft one unifying brand sentence that could appear verbatim across all six channels — the "single brand idea" that every piece of communication should express. This is the practical output of a real IMC planning session.
**Exclusions:** No media plan (channel selection, reach/frequency planning) — that's a separate quantitative exercise. No crisis communications planning (would require its own card).
**Score:** 8/10 — the Peloton story is one of the best recent marketing case studies; the consistency matrix animation is clean and instructive; the crisis-scenario change shows that IMC is dynamic, not a one-time audit; the single-brand-sentence teardown is a real deliverable.
