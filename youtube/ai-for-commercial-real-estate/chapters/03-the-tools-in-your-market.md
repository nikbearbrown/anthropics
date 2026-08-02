# Chapter 3 — The Tools in Your Market


## TL;DR

- This chapter gives a working overview of The Tools in Your Market, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through The Thing About a Dashboard, Five Things Tools Actually Do, The Major Platforms, Mapped, What "Embedded" Means for Professional Responsibility, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The AI is already in your software. The question is whether you know what layer it's touching.*

---

## The Thing About a Dashboard

Here is something worth sitting with for a moment.

A broker logs into CoStar on a Tuesday morning, pulls up a submarket report for West Hollywood, and sees a graph showing tenant demand trending upward. The number is there. The color is green. The arrow points the right direction. The broker sends the report to a client with a note that the submarket is looking active. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

Nothing about that sequence feels like "using AI." It feels like checking the data. But somewhere between the raw lease transactions in CoStar's database and the green arrow on that dashboard, a set of decisions was made — about which signals to weight, which transactions to include, how to handle gaps in coverage, what the forward-looking estimate is based on. Those decisions are model decisions. They are not the broker's decisions. The broker transmitted them to a client without examining them. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

This is not a dramatic failure. No one got hurt. But it is a habit that scales badly. The same reflex — "I saw it in the platform, so it's the data" — applied to a more consequential output, produces a real problem. A misread demand forecast that supports a leasing strategy. An extraction tool output that misses a critical clause and crosses directly into a client memo. A revenue management recommendation presented as market consensus when it is a pricing model's output.

The fix is not skepticism about platforms. CoStar, VTS, Dealpath, AppFolio, Yardi — these are genuinely useful tools. The fix is something more precise: knowing which layer of the stack each tool is touching, what kind of thing it is producing, and what that means for how much review the output requires before it crosses from internal first pass to client-facing fact. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

This chapter is about building that map. Not a list of platforms with bullet points about features — that would be outdated in six months. A conceptual framework that tells you what any CRE tool is actually doing when it shows you a number, a summary, an extraction, or a recommendation. Because the platforms change. The underlying question does not.

![Illustration of a broker's morning workflow ](images/03-the-tools-in-your-market-fig-01.png)
*Figure 3.1 — Illustration of a broker's morning workflow *

---

## Five Things Tools Actually Do

Before cataloguing specific platforms, it helps to build a taxonomy that survives platform updates. Every AI feature in a CRE tool is doing one of five things. Sometimes one tool does several of them. Knowing which one you're looking at tells you the failure mode.

**The first is data aggregation.** The tool is pulling together transaction records, property characteristics, lease comps, ownership records, or demographic information from multiple sources and displaying them in one place. CoStar's core property database is largely this. The AI here is mostly in the ingestion and deduplication — matching records, resolving address ambiguities, filling gaps from secondary sources. The output is structured data. The failure mode is coverage gaps and source quality: CoStar's data is strongest in dense urban markets and large transactions; thinner in smaller markets, specialty assets, and off-market activity. A strong-looking dataset in a thin market is not the same as a strong dataset in a thick one.

**The second is signal extraction.** The tool is reading unstructured documents — offering memoranda, rent rolls, lease agreements, construction bids, financial statements — and pulling structured information out of them. Dealpath AI Extract is the clearest example here: paste in an OM or a flyer, get back a structured set of fields with the deal terms populated. The failure mode is the one established in Chapter 2: extraction works well on standard phrasing and fails on bespoke language, complex amendment structures, and clauses that require temporal priority reasoning across multiple documents. The output requires source-document review before it crosses into anything consequential.

**The third is demand forecasting.** The tool is making a forward-looking estimate about market behavior — where tenant demand is heading, which submarkets are likely to see absorption, what the probability is that a given space will lease in a given timeframe. VTS 4 and VTS Data operate here. The methodology involves large leasing-signal datasets: tours scheduled, letters of intent executed, leases signed, tenant requirements entered into the platform. The output is genuinely useful for prospecting and market sensing. The failure mode is exactly what you'd expect: a forecast is a model output built on historical patterns and current signals. It is not a market fact. It degrades as submarket coverage thins, as the current cycle diverges from historical patterns, and as the question gets more specific than the model's training resolves.

**The fourth is workflow automation.** The tool is executing a sequence of actions that used to require a human to initiate each step. AppFolio's Realm-X Flows, Yardi's Virtuoso AI Agents, automated lease renewal reminders, 24/7 inquiry response systems — these are all workflow automation. The AI is doing pattern-matching and routing: if condition A is true, execute action B. The failure mode here is not accuracy on a specific task; it's coverage of edge cases and the quality of the handoff condition. An automated inquiry response that handles 90% of prospective tenant questions correctly and routes the other 10% to a human is a different thing from one that handles 90% correctly and sends the other 10% to a folder nobody checks.

**The fifth is generative output.** The tool is producing text, images, or structured content that didn't exist before the query: a property description draft, an offering memorandum section, a market analysis narrative, a lease clause summary. This is where ChatGPT, Claude, and the generative modules built into various CRE platforms operate. The failure mode is the one specific to large language models: confident-sounding output that is factually wrong. A generative tool summarizing a lease doesn't know that it missed the co-tenancy clause — it produces a clean, professional-looking summary of what it found, and nothing in the formatting signals that it didn't find everything.

Those five categories — data aggregation, signal extraction, demand forecasting, workflow automation, generative output — map cleanly onto five different review requirements and five different failure modes. If you know which category a tool is operating in, you know what to check.

| What the tool produces | Primary failure mode | Review required before client use | Example platforms |
| --- | --- | --- | --- |
| Data aggregation | Signal extraction | Demand forecasting | Workflow automation |

---

## The Major Platforms, Mapped

With that framework in place, the major CRE platforms become easier to read. Not as a list of features, but as a set of tools operating at different layers of the stack with different risk profiles.

**CoStar and LoopNet** are primarily data aggregation with some demand forecasting layered on top. The core database — property records, lease comps, transaction history, owner information — is the aggregation layer. The AI does the work of ingestion at scale: matching records across sources, estimating values where direct data is missing, filling coverage gaps. The demand forecast products are the forecasting layer: model outputs built on the transaction database, with all the failure modes that implies.

The 2024 acquisition of Matterport is worth understanding because it signals where CoStar's platform is heading. Matterport produces digital twins — three-dimensional spatial representations of properties built from scan data. Integrated into CoStar's property intelligence stack, this moves the platform toward AI-enabled spatial analysis: automated measurement extraction, virtual walkthrough, condition assessment from imagery. That is a different kind of data than a lease comp. It is property-state data with its own coverage gaps and verification requirements. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

For West Hollywood, Culver City, Beverly Hills, and Marina del Rey: CoStar's headline market statistics are generally reliable on large, brokered transactions. They are noticeably thinner on sub-1,000-square-foot retail, owner-occupied properties, value-add deals that never hit the open market, and the relationship-priced transactions that define a significant share of local deal flow in dense urban submarkets. A strong-looking CoStar query does not mean the market is well-represented in the database. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

**VTS and VTS Data** operate primarily at the demand forecasting layer. The claim that VTS 4 forecasts tenant demand six to nine months ahead is a claim about model output, not market fact. The inputs are leasing signals drawn from the platform: tour activity, letter-of-intent execution, tenant requirements entered by users. This makes VTS data subject to a structural limitation that is different from CoStar's: VTS signals are drawn from transactions on the VTS platform, which means markets and asset types with lower VTS adoption have proportionally weaker signal.

The working approach to a VTS demand indicator is not "demand is rising." It is: here is a signal worth examining. What tenant behavior produced it? What is the platform coverage in this submarket? What do the brokers who are active here say when I call them? Does the signal change my prospecting, or does it confirm what I already know? A tool that surfaces a question worth asking has done its job. A tool that produces an answer you transmit without asking the questions has been misused. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

**Dealpath** operates primarily at the signal extraction layer, with some workflow automation for deal management. Dealpath AI Extract pulling OM data into structured fields in under a minute is genuinely useful, and the product materials are appropriately framed: faster extraction with review, not replacement of the analyst. That is the right posture, and it reflects a real design choice. The platform is built to accelerate the population of a deal model, not to make the judgment calls about whether the deal is worth pursuing.

The 95% accuracy figure that Dealpath reports for AI Extract is a vendor claim, with all the caveats that Chapter 2 established. Ninety-five percent on standard fields means something different than ninety-five percent on a lease that contains a ground lease, a co-tenancy clause written in non-standard phrasing, and an amendment stack from three different decades. The review requirement does not go away because the tool is fast. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

**AppFolio Realm-X and Yardi Virtuoso AI Agents** operate primarily at the workflow automation layer. Lisa, AppFolio's AI Leasing Assistant, handles prospect inquiries around the clock. Yardi's agent marketplace deploys automated workflows triggered by data signals without human intervention. These tools matter to brokers because clients — particularly institutional landlord clients — use them. A broker advising an owner who uses Realm-X needs to know that the leasing assistant is fielding prospect inquiries, that the revenue management system is pricing new and renewal leases, and that the operational reports crossing the broker's desk may reflect AI-generated workflow outputs, not human analyst judgment.

The failure mode for workflow automation is not that the tool makes dramatic errors on individual decisions. It's that the handoff conditions are poorly defined: edge cases that fall outside the automation's routing logic get dropped or delayed, and nobody is watching the bucket they fall into. For a broker advising a client who uses these tools, the question is not whether the automation is working — it probably is, for the 90% of cases it was designed to handle. The question is what happens to the 10% it wasn't. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

**JLL Falcon, CBRE Nexus, and the enterprise platform layer** are worth understanding as a category even if most brokers don't have direct access to them. JLL GPT has been used by over 47,000 JLL professionals. CBRE's Nexus platform covers over a billion square feet of client properties. These are not external tools a broker uses; they are internal AI infrastructures that shape the analysis, market data, and deliverables that enterprise brokers produce for clients. Understanding that a competitor's analysis was produced with JLL Falcon — which integrates generative AI with JLL's proprietary market data — is different from understanding that a human analyst produced it from scratch. The output looks the same. The process behind it is different.

| Platform | Primary category (aggregation | extraction | forecasting | automation |
| --- | --- | --- | --- | --- |
| Major CRE platforms mapped to the five-category taxonomy — | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## What "Embedded" Means for Professional Responsibility

There is a temptation, once AI features are embedded in a platform subscription, to treat them as simply part of the tool — the same way a spreadsheet's formula functions are part of the spreadsheet. You don't think of VLOOKUP as "using AI." It's just the tool working.

This is a category error, and it's worth being precise about why.

A spreadsheet formula executes a deterministic operation on defined inputs. The same inputs always produce the same output. You can audit it cell by cell. You can trace every number to its source. If the formula is wrong, it's wrong in a transparent, auditable way.

An AI feature in a CRE platform is not deterministic in the same sense. A demand forecast model was trained on a particular dataset, over a particular time window, with particular methodology choices that are not visible in the output. A generative summary of a lease document reflects the model's interpretation of that document, which may diverge from a lawyer's interpretation in ways that are not flagged. A workflow automation that routes an inquiry to a queue rather than a human represents a design choice about edge-case handling that may not be documented anywhere a broker would look.

The embedded nature of the feature does not change its character. It changes how easy it is to forget that character.

This is what "embedded AI" actually means for professional responsibility: the fact that you didn't open a separate AI application doesn't mean AI judgment isn't in the output. If a platform feature uses machine learning to produce the number, the extraction, the forecast, or the recommendation, then the professional responsibility question — did I review this before transmitting it to a client? — applies regardless of whether the feature looked like an AI button or just looked like the interface.

![Comparison: left panel shows an analyst manually building](images/03-the-tools-in-your-market-fig-02.png)
*Figure 3.2 — Comparison: left panel shows an analyst manually building*

---

## The Coverage Problem, Specifically

The taxonomy and the platform mapping matter most when they intersect with local market knowledge. And in the LA Westside markets — West Hollywood, Culver City, Beverly Hills, Marina del Rey — there is a specific coverage problem worth naming directly.

National platforms are built on national transaction data. Their accuracy and reliability are functions of transaction density and platform adoption. In a market like Manhattan or Chicago's Loop, where transaction volume is high, properties are well-documented, and platform adoption among brokers is near-universal, CoStar and VTS signal data approaches something like genuine market coverage. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

In a dense urban submarket where a significant share of transactions are relationship-priced, owner-occupied, or sub-institutional-size, the coverage picture is different. Not absent — the major transactions, the headline deals, the significant vacancy events, they're all there. But the texture of the market — the tenant who's about to expand and hasn't listed a requirement anywhere, the landlord who priced a space based on a conversation at an industry event, the block where retail turnover is accelerating before any vacancy shows up in a database — that texture is not in the data.

A VTS signal that shows demand rising in a West Hollywood creative office submarket is worth examining. It tells you something about what large-platform-tracked tenants in that submarket are doing. It tells you less about the owner-user contingent, the creative-sector-adjacent tenants who find space through relationships rather than formal search processes, and the block-by-block dynamics that define micro-market value in a district where a half-mile can mean the difference between a struggling space and a waiting list. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

The coverage problem is not a reason to ignore platform data. It is a reason to know what the platform data covers and to be specific about what it doesn't. "The platform shows X" is a starting point. The professional judgment question is always: what does the platform not show, and how do I fill that gap?

![Conceptual coverage map of LA Westside submarkets ](images/03-the-tools-in-your-market-fig-03.png)
*Figure 3.3 — Conceptual coverage map of LA Westside submarkets *

---

## The Methodology Caution, Specifically

Beyond coverage, there's a methodology caution that applies specifically to forecasting tools — and it is worth stating clearly because it runs counter to a natural instinct.

When a forecasting tool produces an estimate — VTS projecting demand six to nine months ahead, an AVM marking a cap rate, a market analysis tool projecting absorption — the instinct is to treat the estimate as an answer and calibrate your confidence based on how confident the tool sounds. A confident-looking forecast with a tight range sounds more reliable than a wide-range estimate with caveats.

This instinct gets the epistemology backwards.

A forecast is not reliable because it sounds confident. A forecast is reliable to the extent that its methodology is appropriate for the question being asked, its training data covers the relevant market conditions, and the current moment is not one where historical relationships have broken down. None of those things are visible in the output. A forecast produced by a model trained on 2015–2019 office leasing patterns, applied to West Hollywood creative office in 2026 — four years after remote work permanently restructured office demand dynamics — has a methodology problem that doesn't show up in the confidence interval. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

The working posture toward any CRE forecast tool is: a forecast tells me what the model expects, given what it was trained on. My job is to decide whether what it was trained on is the right model for the question I'm actually asking. That requires knowing something about the methodology, something about the current market that may diverge from historical patterns, and something about whether the signal would change my professional judgment or simply confirm it. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

A forecast that confirms what you already know from direct market contact probably doesn't change your recommendation. A forecast that contradicts what you're hearing from active market participants is not necessarily wrong — but it demands the question of why the divergence exists before it changes anything.

![Illustrative divergence diagram ](images/03-the-tools-in-your-market-fig-04.png)
*Figure 3.4 — Illustrative divergence diagram *

---

## The Right Question for Any Tool

The framework this chapter has been building toward reduces to three questions you should be able to answer for any tool output before it influences a client-facing deliverable.

The first question is: **What data?** Where did the input come from? What is the source, the coverage, the vintage? A national dataset with strong coverage in institutional markets may have significant gaps in the local context where you're using it. A model trained on pre-2020 patterns may not be the right model for 2026. A platform with strong adoption in large transactions may be thin on the mid-market deals that define your practice.

The second question is: **What output?** What kind of thing is the tool producing — a structured extraction from a defined source document, a model estimate built on historical patterns, an automated workflow output, a generative summary, a data visualization of underlying records? Each of these has a different relationship to the underlying reality it purports to represent, and each requires a different review posture. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

The third question is: **What decision?** What action will this output influence? A demand signal that changes where you prioritize prospecting calls is a different decision than a lease extraction that feeds into a client's acquisition due diligence. The review requirement scales with the consequence of getting it wrong. A misread prospecting signal costs you a few calls. A misread lease clause in a $30 million deal costs something else entirely. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

Those three questions — What data? What output? What decision? — are not a checklist to run through every time you open a platform. They are a mental posture that becomes automatic once it's built. The broker who has internalized them doesn't stop and formally assess every tool interaction. They see a green arrow on a dashboard and automatically think: this is a model forecast, not a transaction fact, and I need to know what coverage and methodology produced it before I cite it.

That is not skepticism. That is literacy.

![Three-question decision card ](images/03-the-tools-in-your-market-fig-05.png)
*Figure 3.5 — Three-question decision card *

---

## The Policy Implication

One last point that this chapter's framework makes clear, because it comes up as a question and the answer is not obvious until you see it.

The question is: do embedded AI features in platform subscriptions require a separate AI policy?

The answer is yes, and here is why.

An AI policy — whether for an individual broker or a brokerage — exists to define which outputs require review before they influence client deliverables, who is responsible for that review, and what the review standard is. That policy is triggered by the character of the output, not by whether the tool was labeled "AI" when you opened it. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

If you use Dealpath AI Extract to populate a deal model and that model feeds into a client investment memo, the review requirement doesn't disappear because AI Extract is embedded in Dealpath's interface rather than a standalone AI tool. If your market analysis pulls a VTS demand signal and that signal shows up in a client presentation without annotation, the methodology caution doesn't disappear because VTS is part of your standard research workflow. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

Embedded AI features still affect client deliverables. They belong in the workflow policy. The absence of a separate AI button doesn't mean the absence of AI judgment in the output.

What an AI policy for embedded tools looks like in practice is simple: for each platform feature that produces a number, extraction, forecast, or summary that could influence a client deliverable, define the review step that has to happen before transmission. For extraction tools: source-document verification of material provisions. For demand forecasting tools: methodology check and direct market contact before the signal changes advice. For generative summaries: human review of the full output against the source document.

That is not a complicated policy. It is a clear one. And having it explicit — rather than assuming it exists because "of course I review things" — is the difference between a professional practice and a habit that works until the ninety-sixth time.

---

## LLM Exercises

The following exercises are designed to be completed with access to a large language model. They are structured experiments, not assessment questions — the goal is to reveal AI behavior directly, in the context of real tool categories. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-tools-in-your-market-assertions.md -->

**Exercise 1 — Taxonomy self-test.** Describe to an LLM a CRE platform feature you actually use (or one from this chapter). Ask the LLM to classify it according to the five-category taxonomy: data aggregation, signal extraction, demand forecasting, workflow automation, or generative output. Then identify whether its classification matches yours and where the disagreement, if any, comes from. What does the disagreement reveal about the feature's actual behavior?

**Exercise 2 — The coverage probe.** Take a specific submarket you know well — a neighborhood, a block, an asset type. Ask an LLM what a national CRE data platform would likely cover and not cover in that submarket, given what you know about transaction volume, off-market activity, and platform adoption patterns. Compare the LLM's answer to your own direct knowledge. Where does the LLM have accurate intuitions about coverage gaps? Where does it miss something that only local market experience would surface?

**Exercise 3 — The forecast methodology question.** Find a forecast — from VTS, CoStar, or any CRE analytics platform — that covers a market you know. Describe the forecast to an LLM and ask it to generate three questions you would need to answer about the methodology before the forecast should change your professional advice. Compare those questions to the ones you would have generated without the LLM. Are there methodology concerns the LLM surfaced that you wouldn't have asked about?

**Exercise 4 — The policy draft.** Describe to an LLM your typical workflow for producing a client-facing market analysis or investment summary. Ask the LLM to identify every step where an AI tool — embedded or explicit — could influence the output, and to draft a brief review requirement for each step. Then evaluate: does the resulting policy reflect how you actually want to work, or does it reveal gaps in your current practice?

## References

1. AppFolio. AppFolio Unleashes Realm-X AI Capabilities. AppFolio, 2024. https://www.appfolio.com/newsroom/appfolio-unleashes-realm-x-ai-capabilities
2. CoStar Group. Full Year 2025 Revenue Increased 19% Year-over-Year. SEC Form 8-K exhibit, 2026. https://www.sec.gov/Archives/edgar/data/1057352/000105735226000012/q42025earningspressrelea.htm
3. VTS. VTS Data: Accurate, Real-Time CRE Industry Insights. VTS. https://www.vts.com/vts-data
## AI and Errata Disclosure

Agentic AI was used to help gather data, check assertions, and prepare supporting references for this chapter. The material goes through multiple review steps, but mistakes can still occur. Errata, corrections, and suspected mistakes may be submitted through the publisher's website at https://www.humanitarians.ai.
