# INFO 7375: Branding and AI — Video Ideas

## Candidate 01 — Why Your GitHub Portfolio Stopped Working (And What Replaced It)
- Source: `info-7375-branding-and-ai-spring-2026/chapters/01-the-creative-engineer.md`
- Topic: Signaling theory and the AI labor-market shift
- Hook: A peer-reviewed experiment showed AI tools cut coding time by 56% — and that number quietly made your GitHub portfolio obsolete.
- Key case: Peng et al. 2022 RCT — 95 professional developers, HTTP server task, 161 min control vs. 71 min Copilot group; a decade-old interview-filter task now takes an afternoon.
- The Question: If everyone can produce a working app, what signal does a GitHub repo still send — and what signal actually sorts candidates now?
- Core idea: Spence's 1973 signaling mechanism predicts that when a signal's cost collapses, the market shifts to costly signals that remain — and for engineers in 2026, those are Ideate, Brand, and Ship, not Build.
- Visual object: A two-column equilibrium chart — left: "Separating Equilibrium 2010" (costly signal sorts), right: "Pooling Equilibrium 2026" (signal pools, everyone looks the same).
- Manim move: split — the separating chart cleanly divides, then the right side collapses into a single undifferentiated pile.
- Example seed: Imagine 10 engineers applying for the same role. In 2015, 3 had deployed apps (costly signal separates). In 2025, all 10 have deployed apps in a day (pool). Recruiter can't tell them apart. Show the transition numerically.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Viewer knows what GitHub is; has some awareness of AI coding tools.
- Exclusions: Do not go into LLM architecture, fine-tuning, or AI capability debates. Do not discuss four verbs in detail — just name them. No deep-dive on Spence's Nobel or economics history.
- Score: 9/10

---

## Candidate 02 — The Archetype Is a Forcing Function (Not a Personality Quiz)
- Source: `info-7375-branding-and-ai-spring-2026/chapters/03-jungian-brand-archetypes-as-a-system.md`
- Topic: Brand archetypes as decision-making constraint
- Hook: Tropicana changed its packaging, lost $30M in sales in two months, and rolled back — not because the new design was ugly, but because customers couldn't find their orange juice anymore.
- Key case: Tropicana Pure Premium January 2009 redesign — orange-with-straw replaced by a glossy glass, 20% sales drop, rollback announced February 23, 2009.
- The Question: Why does changing a carton design destroy $30M in revenue in 60 days when the juice inside is identical?
- Core idea: A brand archetype is a recognition asset built by consistent touchpoints — when the archetype expression changes, the customer's mental model collapses and they stop finding you, not because they're loyal to a logo but because they've lost the cognitive handle.
- Visual object: A grocery-store shelf with one OJ carton visible — first the orange-with-straw version (recognizable), then swapped to the new version (invisible among competitors).
- Manim move: morph — orange-with-straw carton morphs into the new glossy design, then a simulated "shelf scan" eye-track misses it entirely.
- Example seed: A customer scans a shelf of 8 orange juice brands in 3 seconds. They've bought Tropicana 100 times, so their eye goes to position X. After the redesign, position X no longer matches the stored pattern — they grab a competitor. Run the numbers: 30M revenue / avg OJ purchase = ~15M lost transactions in 60 days.
- Length band: 2–3 min
- Still lanes: raster
- Prerequisites: No prior branding knowledge needed. Basic visual intuition.
- Exclusions: Do not explain all 12 archetypes — only name the Innocent archetype and its visual commitments. Do not cover the Gap or New Coke cases. No discussion of archetype shadows.
- Score: 9/10

---

## Candidate 03 — Why Architecture Is Brand (The Madison Framework Insight)
- Source: `info-7375-branding-and-ai-spring-2026/chapters/02-the-madison-framework.md`
- Topic: Multi-agent system design and brand legibility
- Hook: An AI marketing system with five named layers isn't just easier to debug — it creates product surfaces that a company can sell, price separately, and explain to a CFO. The engineering choice and the brand choice are the same choice.
- Key case: Madison's five-layer architecture (Intelligence, Content, Research, Experience, Performance) contrasted with a hypothetical single mega-agent — same capability, radically different customer-facing surfaces.
- The Question: If two AI systems do the same work, why does the one with five named layers build more customer trust than the black-box version — and why does that make it worth more money?
- Core idea: Named, specialized layers create inspectable failure points (engineering benefit) and product surfaces customers can reason about, compare, and purchase separately (brand benefit) — the decomposition is one decision with two downstream consequences.
- Visual object: Two boxes side by side: left is a single black box labeled "AI Marketing"; right is five labeled boxes stacked inside an orchestration shell. Customer talks to the right one; can't interact with the left.
- Manim move: split — single box splits into five labeled layers, then each layer gets an arrow pointing to a customer capability: "sell separately," "version independently," "debug by name."
- Example seed: A marketing director's Monday morning. Single agent breaks — "the AI is broken." Five-layer system: "the Intelligence Agent is down, Content is still running, your dashboard is fine." Recovery time: minutes vs. hours. Product trust: intact vs. destroyed.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Viewer has some sense of what an API or software module is. No LLM knowledge required.
- Exclusions: Do not explain ReAct loops or Thompson sampling. Do not go into CrewAI or LangGraph implementation. Do not discuss all five Madison layers in depth — two or three with the comparison is enough.
- Score: 9/10

---

## Candidate 04 — The $100,000 No: Why Scope Discipline Is Brand Strategy
- Source: `info-7375-branding-and-ai-spring-2026/chapters/04-product-requirements-and-scope.md`
- Topic: Product scope discipline and brand coherence
- Hook: Linear, a project management tool, turned down a six-figure enterprise contract because the customer wanted a configuration the product's philosophy didn't allow. That refusal is a brand statement, not just a product decision.
- Key case: Linear's published Method — opinionated software, no feature sprawl, decline of enterprise customization even at significant deal value — with $35M ARR reached by a lean team building fewer features than competitors.
- The Question: How does saying no to a paying customer make your product more valuable to the customers you kept — and how many nos does it take before the constraint becomes the identity?
- Core idea: Every feature you refuse preserves the coherence that made your core users love the product; incoherence accumulates the same way coherence does — one decision at a time, compounding in the direction you chose.
- Visual object: Two product timelines — left: "accepts all feature requests" with a coherence meter that declines over time; right: "Linear-style no" with coherence meter that holds, then rises as word-of-mouth compounds.
- Manim move: accumulate — decisions pile up on each timeline, coherence meter responds, original user base size tracked on both.
- Example seed: Product A and Product B both launch with the same core feature set. Over 12 months, A accepts 6 enterprise customization requests; B accepts 0. Show A's codebase complexity, user satisfaction, and brand clarity vs. B's. Invent small numbers: A's churn rises from 5% to 12%; B's falls from 5% to 3%.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Viewer has some awareness of SaaS products or software development. No deep technical knowledge needed.
- Exclusions: Do not explain PRD format in detail. Do not go into Lean Startup methodology or Build-Measure-Learn. Do not discuss Madison's scope decisions.
- Score: 9/10

---

## Candidate 05 — Every External API Is a Contract You Don't Control
- Source: `info-7375-branding-and-ai-spring-2026/chapters/05-data-pipelines-and-workflow-automation.md`
- Topic: Pipeline fragility as brand risk
- Hook: Apollo — the best-designed third-party Reddit app, loved by millions — was killed in 30 days not by a code failure but by a pricing decision it had no control over. The pipeline was excellent. The contract was lethal.
- Key case: Reddit API pricing change May–June 2023 — $0.24 per 1,000 API calls, Apollo's 7B monthly requests = ~$20M/year implied cost, 30-day shutdown announcement, third-party ecosystem collapse.
- The Question: When a tool you didn't build changes the rules, whose brand pays — and what could Apollo's developer have built differently to survive even a $20M/year contract change?
- Core idea: A data pipeline is a chain of contracts owned by someone else, each subject to change without your consent — designing for contract failure (degraded modes, stable fallbacks, monitoring) is a brand decision as much as an engineering one.
- Visual object: A 5-node pipeline diagram with one node lit red (Reddit API contract fails) — left side shows a crash propagating to the user; right side shows a graceful degradation path with an informative failure message.
- Manim move: decay — left pipeline: failure propagates downstream, tool dies; right pipeline: failure hits fallback node, partial output continues, user sees "limited mode" not crash.
- Example seed: A 3-node pipeline: RSS feed (stable, no auth) → deduplication → Google Sheets. The RSS feed goes down. Left version: blank output, users confused. Right version: last successful result served with "updated 3 hours ago" timestamp, alert sent to developer. Same pipeline, one extra node, completely different brand outcome.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Basic awareness of APIs — viewer has heard of an API or made a web request. No coding required.
- Exclusions: Do not explain n8n interface or workflow tooling in detail. Do not go into Twitter/Heroku cases — Apollo is sufficient. Do not discuss ETL vs. stream processing taxonomy.
- Score: 9/10

---

## Candidate 06 — Autonomy vs. Orchestration: The Hardest Design Decision in AI Products
- Source: `info-7375-branding-and-ai-spring-2026/chapters/06-ai-intelligence-and-multiagent-systems.md`
- Topic: AI system architecture and the autonomy/orchestration trade-off
- Hook: AutoGPT sessions in 2023 cost users $80 and delivered nothing. Cursor became the tool engineers trust for daily work. Same underlying LLMs. The difference was one architectural choice.
- Key case: AutoGPT's 2023 compounding error and cost-runaway failures vs. Cursor's augmentation model — identical model access, wildly different production reliability and user trust outcomes.
- The Question: If you give an AI agent total autonomy to pursue a goal, why does a 10% per-step error rate mean only a 1.5% chance of a correct result after 40 steps — and how do you design around that math?
- Core idea: The autonomy/orchestration spectrum is not about capability — it's about where in the workflow the AI decides and where a deterministic system decides; errors compound geometrically in autonomous chains, while orchestrated pipelines fail locally and recoverably.
- Visual object: A line chart — x-axis: number of agent steps (0–40), y-axis: probability of error-free output (0–100%). One curve at 10% per-step error rate (0.9^n) drops from 100% to 1.5% at step 40.
- Manim move: trace — the compounding error curve draws from left to right, key values annotate at 10, 20, 40 steps; a second line shows "orchestrated system with validation checkpoints" maintaining a higher floor.
- Example seed: A 5-step autonomous research agent. Step 1: finds source (correct). Step 2: misattributes a fact (10% error). Steps 3–5: build on the wrong fact. By step 5, the output is confidently wrong about the founding claim. An orchestrated system validates at step 2 and routes to human review. Show the divergence with made-up percentages: autonomous agent delivers wrong answer 40% of runs; orchestrated delivers correct answer 92% of runs.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Viewer has heard of AI tools like ChatGPT or Copilot. No LLM architecture knowledge required.
- Exclusions: Do not explain ReAct loop mechanics. Do not go into CrewAI or LangGraph implementation details. Do not discuss conversation-based vs. graph-based orchestration distinction.
- Score: 9/10

---

## Candidate 07 — The Interface Is a Contract Renewed Every Session
- Source: `info-7375-branding-and-ai-spring-2026/chapters/07-interface-design-and-deployment.md`
- Topic: Interface-brand alignment and the Bard failure mechanism
- Hook: Google Bard gave one factually wrong answer in a promotional video, and Alphabet lost $100 billion in market cap in 48 hours. The AI wasn't the problem. The interface was.
- Key case: Google Bard February 2023 launch — promotional video showed Bard claiming JWST took the first exoplanet images (wrong by nearly 20 years), Reuters caught it within hours, Alphabet stock dropped ~$100B by close.
- The Question: How does one wrong bullet point — in a product full of disclaimers about being experimental — cost a company $100 billion, while other AI products produce wrong answers every day without a market-cap event?
- Core idea: The interface makes an implicit promise with every visual element — polished Google-branded presentation promised verified, authoritative information; the system delivered research-preview-quality output; the gap between the two is what the market priced, not the error itself.
- Visual object: A two-column "alignment audit" table — left: "What the interface promised" (polished, confident, authoritative bullets); right: "What the system delivered" (unverified research preview). Each row shows a pass or fail mark.
- Manim move: compare — two columns fill in simultaneously; mismatch rows light red; the gap between promise and delivery grows visually.
- Example seed: A student's AI tool has a "Summarize any document" button. The system handles PDFs up to 20 pages but fails on Excel files. The interface promises broad capability; the system has narrow capability. Run 10 users through the tool: 3 upload Excel files, get silent failures, never return. The interface cost the tool 30% of its first-time users. Show the fix: rename to "Summarize PDFs (up to 20 pages)" — conversion holds, churn drops.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Has used at least one AI tool (ChatGPT-level familiarity). No technical background needed.
- Exclusions: Do not cover Snapchat redesign or Microsoft Tay cases — Bard is sufficient. Do not explain Streamlit vs. Gradio framework choice. Do not go into WCAG accessibility standards.
- Score: 8/10

---

## Candidate 08 — The Negative Space Is the Brand (Stripe's 15-Year Refusal List)
- Source: `info-7375-branding-and-ai-spring-2026/chapters/08-startup-brand-path-brand-strategy.md`
- Topic: Brand strategy through systematic declination
- Hook: Stripe built a $95 billion company partly by refusing to do enterprise sales, refusing to rush product launches, and refusing to write marketing-style blog posts. The brand is visible most clearly in what it never did.
- Key case: Stripe's 15-year brand consistency — no enterprise sales process for years, no rapid product proliferation (Atlas in 2016, Issuing in 2018, Climate in 2020), documentation as product rather than marketing content.
- The Question: Why is a list of what a company refuses to do a stronger brand signal than a list of what it builds — and how do you write a no-list specific enough to be useful?
- Core idea: Brand coherence is produced by the consistency of constraint — each systematic refusal preserves the archetype expression that made the brand recognizable, and over time the no-list is what distinguishes the brand from a competitor doing all the same things but without the discipline.
- Visual object: Two timelines side by side — Stripe's 15-year product launch cadence (sparse, deliberate) vs. a hypothetical competitor's (feature after feature, rapid). Below each: the brand clarity score over time. Stripe's rises; the competitor's plateaus then fragments.
- Manim move: accumulate — declinations stack up on Stripe's timeline; each "no" is a brick in the brand wall. A parallel timeline shows a competitor accepting every feature request; their brand wall has gaps.
- Example seed: A startup with $100K in ARR gets an enterprise inquiry. The customer wants custom SSO, white-label branding, and a dedicated Slack channel. That's $40K/year. But building custom SSO changes the product from developer-self-serve to enterprise-managed. Run the math: $40K now vs. the next 10 developer-self-serve customers worth $5K/year each for 5 years = $250K. The no-list tells you which bet to make.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Basic awareness of SaaS business models. No branding background needed.
- Exclusions: Do not explain all seven brand strategy components in depth. Do not go into personal brand path vs. startup brand path distinction. Do not discuss archetype shadows or naming tests.
- Score: 8/10

---

## Candidate 09 — Story Shape and Archetype Mismatch: Why the Pepsi Kendall Jenner Ad Failed in 24 Hours
- Source: `info-7375-branding-and-ai-spring-2026/chapters/10-brand-storytelling.md`
- Topic: Narrative-archetype alignment and brand storytelling failure
- Hook: Pepsi pulled an ad 24 hours after launch that had taken months to produce, starred Kendall Jenner, and cost millions — not because a single element was wrong, but because the story shape was borrowed from an archetype Pepsi has no claim to.
- Key case: Pepsi "Live for Now" Kendall Jenner ad, April 2017 — pulled within 24 hours after widespread backlash; the ad appropriated protest-movement imagery (Outlaw/Rebel archetype territory) for an Innocent/Jester brand that cannot credibly inhabit that space.
- The Question: An Innocent brand tells a Rebellion story — why does the audience immediately feel the falseness even if they can't articulate why, and what story shape was available to Pepsi that would have worked?
- Core idea: Story shapes have archetypal commitments built into them — protest/social-movement content belongs culturally to Outlaw or Caregiver archetypes; an Innocent brand borrowing that content reads as exploitation of the content's cultural weight rather than genuine participation in it.
- Visual object: A 3x3 grid mapping archetypes (rows: Innocent, Outlaw, Hero) to story shapes (columns: Rebellion story, Quest story, Hero's Journey). Green cells = native fit. Red cells = mismatch. Pepsi's attempted move lands on a red cell.
- Manim move: transform — the grid appears, cells color in, then Pepsi's specific campaign gets mapped to the red cell with an arrow showing what green cell was available.
- Example seed: An Innocent brand like Pepsi (joy, refreshment, simple pleasure) has access to Jester stories (inversion/delight) and Voyage stories (shared adventure). Run through a hypothetical Jester-aligned Pepsi ad concept vs. the failed Rebellion concept — same budget, different story shape, different outcome. Made-up metric: Jester-aligned refreshes brand favorability +12%; Rebellion attempt: brand favorability -18% in 48 hours.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Has seen brand advertising; basic cultural awareness. No marketing background needed.
- Exclusions: Do not explain all seven Booker plots. Do not go into the Bud Light or Jaguar cases from the chapter. Do not explain Joseph Campbell's 17 Hero's Journey stages — only the three-act shape.
- Score: 8/10

---

## Candidate 10 — The Portfolio That Compounds: Why One Developer's Site Was Forked 6,000 Times
- Source: `info-7375-branding-and-ai-spring-2026/chapters/11-portfolio-as-product.md`
- Topic: Portfolio as compounding brand asset
- Hook: Brittany Chiang published her portfolio website in 2017. Seven years later, developers are still forking the repo — 6,000+ times — and using it as the foundation for their own portfolios. She built the asset once; it's still working.
- Key case: Brittany Chiang's v4 portfolio GitHub repo — 6,000+ forks, 9,000+ stars as of 2024; dark-themed, mint-green accents, monospace typography; career trajectory through Upstatement, Apple, Spotify, Klaviyo.
- The Question: What makes one portfolio template get forked 6,000 times while thousands of equally functional portfolios get zero — and can you design for the indirect-reference and template-effect channels before you launch?
- Core idea: A portfolio compounds through three channels — direct hiring (visible), indirect reference (invisible, delayed, high-compounding), and template effects (autonomous, scales with craft) — and most developers only design for the first while the second and third are where the non-linear returns live.
- Visual object: Three arrows from a central portfolio artifact — Channel 1: short arrow labeled "Direct hiring" (predictable, controlled); Channel 2: long curved arrow labeled "Indirect reference" (invisible, delayed, compounding); Channel 3: branching arrow labeled "Template effects" (autonomous, scales).
- Manim move: spread — arrows emerge from the portfolio, Channel 2 and 3 extend outward beyond the frame while Channel 1 terminates early; counters on each arrow accumulate impressions over time.
- Example seed: Two developers launch portfolios the same week. Developer A: standard template, recruiter-readable, no distinctive craft. Developer B: cohesive visual identity, archetype-legible, open-source code. After 6 months: Developer A: 3 recruiter views from direct applications. Developer B: 3 recruiter views from direct + 2 mentions from referrals + 40 repo forks. Made-up numbers, real mechanism.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Has a GitHub account or has seen developer portfolios. No design background needed.
- Exclusions: Do not go into v0, Framer, or specific portfolio tools. Do not explain visual identity system components from Chapter 9. Do not discuss the resume or LinkedIn surfaces — keep it on the portfolio compound mechanism.
- Score: 8/10
