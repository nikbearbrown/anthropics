# Chapter 6 — Lease Drafting: The First Draft Is Not the Final Draft

*A lease that looks finished is not the same as a lease that reflects the deal.*

---

## The Thing About Legal Language

Here is the problem with fluent prose.

When a lease draft comes back from an AI tool in thirty seconds — clean headings, defined terms, proper recitals, the right kind of legal cadence — the natural response is relief. It looks like a lease. It reads like a lease. The formatting is correct, the section numbering follows convention, and the language sounds exactly like the language in every other lease you've seen. Nothing in the output signals that anything is wrong.

Then the attorney calls. Why does the renewal option use a fair market rent formula that nobody agreed to? Why were the CAM exclusions changed from what the parties negotiated? Where is the co-tenancy trigger?

The draft looked finished because the language was fluent. The deal was not finished.

This is a specific failure mode — different from the extraction failures in Chapter 2 and the forecasting failures in Chapter 3. Those involved AI getting things wrong while reading existing documents. This one involves AI getting things right, technically, while producing a document that doesn't reflect the actual business agreement. The grammar is correct. The syntax is correct. The clauses are recognizable forms from thousands of real leases. And the economics may be completely wrong for this transaction.

Understanding why this happens requires understanding what a large language model is actually doing when it generates legal text. It is not retrieving a clause from a database of negotiated agreements. It is not checking the generated language against the deal terms in the letter of intent. It is producing statistically plausible legal language — text that resembles what appears in leases, given the surrounding context. That is a fundamentally different operation than drafting a clause that encodes a specific business agreement. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

The two can produce identical-looking output. That is the problem.

![Of two renewal option clauses ](images/06-lease-drafting-the-first-draft-is-not-the-final-draft-fig-01.png)
*Figure 6.1 — Of two renewal option clauses *

---

## What a Lease Actually Is

Before working through the five structural decisions that matter most, it's worth being precise about what a commercial lease is at a conceptual level. Because the fluent-draft trap is easiest to fall into when this is unclear.

A lease is an allocation of economic risk between a landlord and a tenant over a defined period. Every clause is a decision about which party bears which risk, under what conditions, with what remedies available. The language is the vessel. The business agreement is the content. The two are not the same thing, and a vessel can be perfectly well-formed while carrying the wrong content entirely.

A rent escalation formula allocates the risk of inflation between landlord and tenant. A CPI-linked escalation with a 3% floor and a 5% cap means something categorically different than a fixed 3% annual bump — different financial projections, different comparative advantage depending on the inflation environment, different valuation implications for the landlord's asset. A formula that looks like a rent escalation clause but uses different parameters than the parties negotiated is not a drafting error in the grammatical sense. It is a business error with financial consequences that survive the lease term. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

CAM exclusions determine what costs the landlord can recover from tenants through common area maintenance charges. Controllable versus uncontrollable expenses, gross-up provisions, audit rights, year-over-year caps — each of these represents a negotiated position with measurable economic value. A draft that omits an agreed-upon exclusion isn't obviously broken. It reads fine. It is structurally wrong.

The co-tenancy clause in a retail lease may be the most financially consequential single clause in the document. If the anchor tenant leaves, does the tenant have the right to pay reduced rent, terminate early, or stay at full rent? The answer determines the tenant's exposure to a scenario that retail history says is not hypothetical. A draft that omits this clause is not technically defective prose — it is a document that silently removes a protection the tenant believed they had. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

This is why the looks-right problem is worse for drafting than for extraction. When AI misreads a clause during abstraction, there is at least a source document to check against. When AI generates a clause that doesn't reflect the negotiated deal, the error has no visible referent. The only way to catch it is to know what the deal was and to systematically check whether the draft reflects it.

---

## The Five Structural Decisions

There are five categories of lease provisions where the gap between fluent language and correct economics is most likely to appear, and where the financial consequences of the gap are most significant. Every AI-drafted lease should be reviewed against these five before it leaves the broker's hands.

**Rent escalation.** The formula governing how base rent increases over the lease term is the most straightforwardly financial clause in the document, and it is the one where AI generation is most likely to produce a plausible-looking wrong answer. Fixed percentage increases, CPI-linked escalations, hybrid structures with floors and caps — these are all recognizable forms that AI will generate fluently. The question is whether the specific parameters match the negotiated deal. A 3% annual fixed increase and a CPI-linked escalation with a 3% cap are not the same economic agreement. They look similar in the abstract, and they have very different implications over a ten-year term in a high-inflation environment.

The compounding question matters here in a way that is easy to miss. A cumulative compounding escalation and a non-cumulative escalation produce dramatically different landlord recovery rights over time, as established in Chapter 2's discussion of CAM caps. The same structural ambiguity that causes problems in lease abstraction also appears in lease generation: AI may produce a formula that is internally consistent but uses a different compounding logic than the parties intended. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

**CAM exclusions.** What the landlord can charge back through common area maintenance is typically heavily negotiated, and the exclusions — what can't be included in the CAM pool — are often the economically significant part. Standard exclusions include capital expenditures, management fees above a defined percentage, expenses for vacant space, costs covered by insurance proceeds, and expenses attributable to the landlord's negligence. A draft that omits exclusions the tenant negotiated, or that includes a gross-up provision structured differently than agreed, silently reallocates significant operating cost exposure. In a mixed-use West Hollywood building where the CAM pool includes a parking structure, a lobby renovation, and shared HVAC infrastructure, the difference between what the parties agreed to exclude and what the draft actually excludes can have substantial annual dollar impact.

**Renewal options.** A renewal option clause has more moving parts than it appears to, and AI generation tends to produce the simplest recognizable form: "Tenant may renew for one additional term of X years at fair market rent." That clause leaves unanswered: How is fair market rent determined — appraisal, negotiation, arbitration? What is the notice period and what happens if the tenant is late? Are the renewal economics based on comparable leases in the building, the submarket, or the market generally? Are tenant improvement allowances included in the fair market determination? Does the option survive assignment? Does it survive a default that was subsequently cured? Each of these is a business decision that the parties likely discussed. None of them is answered by the simplest form of the clause, and a draft that produces the simple form and nothing more has deferred all of these questions to the attorney — or worse, left them unaddressed in the final document.

**ROFO and ROFR provisions.** Rights of first offer and rights of first refusal are structurally complex because they are contingent rights that interact with future events — the landlord's decision to lease adjacent space or to sell the property. The economic value of these provisions depends entirely on the trigger conditions, the response timeline, the pricing mechanism, and the carve-outs. A ROFR that gives the tenant the right to match any offer the landlord receives is categorically different from a ROFO that gives the tenant the right to make the first offer before the landlord markets the space. AI generation will produce a recognizable form of each — the trigger phrase "right of first offer" produces a certain kind of clause, "right of first refusal" produces another. Whether the generated clause reflects the specific mechanics the parties agreed to requires direct comparison against the letter of intent or deal terms.

The stakes here are high enough that the Chapter 2 discussion bears repeating: a missed ROFO in a $50 million acquisition was the example that grounded the financial exposure discussion. The same stakes apply in the drafting direction. A ROFR clause that contains the right trigger but the wrong response timeline, or that excludes the right asset class from its coverage, may be unenforceable at the moment when enforcement is most valuable. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

**Co-tenancy triggers.** In retail leases, co-tenancy provisions protect tenants against the departure of anchor or companion tenants whose presence drives traffic to the space. The typical structure gives the tenant a remedy — reduced rent, termination right, or both — if the anchor tenant vacates for more than a defined period. The economic value of this provision depends on which tenants are defined as co-tenancy anchors, what the occupancy threshold is, how long the remedy-triggering vacancy can persist before the provision activates, and what the remedy schedule looks like over time.

AI generation will produce co-tenancy language that uses the right terminology and the right general structure. It will not know which specific tenants the parties identified as the anchors, what percentage of the building triggers the provision, or what the negotiated remedy schedule was. In a Beverly Hills retail corridor or a West Hollywood mixed-use project where specific anchor tenants are a material part of the tenant's business case, a co-tenancy clause that omits or misdefines the anchor specification is not a minor drafting issue. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

| What AI generates by default | What the business agreement typically adds | Financial consequence if gap is missed | Review question to ask |
| --- | --- | --- | --- |
| Rent escalation | CAM exclusions | Renewal options | ROFO |

---

## Why the Attorney Won't Necessarily Catch It

There is a common assumption that structures the wrong workflow: the broker uses AI to generate a first draft, sends it to the attorney, and relies on the attorney to catch everything that's wrong. The assumption has a hidden premise that makes it fail.

The attorney can review a lease for legal sufficiency. They can identify provisions that are unenforceable under California law, missing definitions that create ambiguity, cross-references that don't resolve, and boilerplate that needs to be updated for the jurisdiction. What the attorney cannot do, without additional information, is verify that the economic terms in the document reflect the deal the parties actually negotiated. That is not a legal question. It is a factual one about the content of a business conversation that the attorney probably wasn't in.

When the attorney sees a renewal option clause that says "fair market rent as determined by appraisal," they have no way to know whether the parties agreed to that mechanism or whether the AI generated it as a default. When they see a CAM provision that includes management fees at up to 5% of operating expenses, they have no way to know whether the parties negotiated a different cap or whether that's what the tool produced in the absence of specific input. The attorney is reviewing legal form against legal standards. The broker is the only person who can review economic substance against the negotiated deal. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

This is why the annotated draft workflow exists and why it changes the character of attorney review. The broker who sends an AI draft with a cover note that says "tool-generated, business terms attached, please align with LOI" has given the attorney something to work with. The broker who sends an AI draft as if it were a marked-up version of an agreed term sheet has pushed hidden work downstream and introduced a gap that may not surface until the tenant asks why their co-tenancy protection isn't in the document.

California DRE's licensee advisory on AI is explicit on this point: AI use does not remove the licensee's supervision, accuracy, disclosure, or fiduciary duties. That principle applies with particular force in lease drafting, where the licensee's professional obligation includes ensuring that client-facing documents reflect the actual transaction. The fluency of the AI output does not satisfy that obligation. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

![Workflow diagram ](images/06-lease-drafting-the-first-draft-is-not-the-final-draft-fig-02.png)
*Figure 6.2 — Workflow diagram *

---

## The LA/Westside Layer

The five structural decisions are universal. There is also a local layer that applies specifically to West Hollywood, Culver City, Beverly Hills, and Marina del Rey — and it is worth naming directly because generic AI drafting tools have no knowledge of it.

Local operating cost expectations are not standard. A Beverly Hills retail tenant and a Culver City creative office tenant have different expectations about what's customary in CAM structures, what's negotiable in renewal option mechanics, and what the market standard is for tenant improvement allowances. An AI tool trained on national lease data will produce national-standard language. Whether national-standard language reflects the local market norms that a sophisticated local tenant expects requires local knowledge that isn't in the model's training data. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

Parking economics in dense urban markets affect lease structure in ways that generic drafting doesn't capture. A West Hollywood restaurant tenant whose business model depends on a specific number of validated parking spaces in an adjacent structure needs lease language that addresses what happens if the parking arrangement changes — covenant of quiet enjoyment for parking access, termination rights if parking falls below a defined threshold, relocation rights if the structure is redeveloped. An AI tool will generate a parking exhibit if prompted to include one. It will not generate the specific protections that reflect the particular parking situation of this tenant in this building on this block.

Mixed-use complications alter the co-tenancy analysis in ways that a retail-focused template doesn't address. A ground-floor retail tenant in a West Hollywood mixed-use building with residential above and creative office in the upper floors has a co-tenancy situation that doesn't map cleanly onto a standard retail co-tenancy template, which is designed for shopping-center anchor configurations. The tenant's business case may depend not on a retail anchor but on foot traffic from specific complementary businesses — a fitness studio, a coffee shop, a salon — that aren't the kind of anchor a standard co-tenancy clause is designed to protect. Drafting that protection requires knowing what the tenant's actual business assumptions are, not just what the clause template looks like. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

Entitlement and use restrictions in West Hollywood and Culver City reflect specific local zoning overlays and adaptive reuse contexts that generic lease language won't address correctly. A tenant moving into a space in a converted industrial building in Culver City's arts district has a different use-clause analysis than a tenant in a ground-up office development. What uses are permitted, what approvals are required, what happens if the city changes its zoning interpretation — these are jurisdiction-specific questions that require local counsel and local knowledge.

The point is not that AI drafting tools are useless for these markets. It is that the local layer is the layer where the tool is most likely to produce standard language that doesn't reflect local reality — and where the broker who knows the market adds the most value by identifying what's missing. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

| Typical CAM structure deviation from national standard | Parking economics complication | Co-tenancy analysis complication | Entitlement | use-clause risk |
| --- | --- | --- | --- | --- |
| West Hollywood | Culver City | Beverly Hills | Marina del Rey. Columns: Typical CAM structure deviation from national standard, Parking economics complication, Co-tenancy analysis complication, Entitlement | use-clause risk |
| cells describe the specific local factor the AI draft will not capture and the question the broker must add | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## The Benchmark Problem

It is worth being direct about something that appears in the sources for this chapter and that brokers sometimes cite in conversations about AI drafting capability.

Legal benchmark performance for large language models has improved substantially. GPT-4's performance on the bar exam, cited in the 2023 Katz et al. research, was a real result — performance at or above the 90th percentile of human test-takers. That result has been widely interpreted as evidence that AI is approaching attorney-level legal capability.

The benchmark measures something specific: the ability to answer multiple-choice and essay questions about legal doctrine on a standardized test. It does not measure the ability to produce a lease clause that correctly encodes a specific business agreement. Those are different tasks.

A bar exam question asks: given these facts, what is the legally correct answer? A lease drafting task asks: given this business agreement between these two parties in this market, produce language that correctly allocates the agreed-upon economic risks with no ambiguity, no default assumptions, and no gaps. The first task has a right answer derivable from legal doctrine. The second task requires knowledge of the specific deal that is not in any training dataset. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

Benchmark performance on legal reasoning tests tells you that AI can reason about law. It does not tell you that AI can draft the specific lease you need. The distinction matters because brokers who are aware of the benchmark results may calibrate their confidence in AI-drafted output upward based on evidence that doesn't actually speak to the specific failure mode this chapter is about.

![Scatterplot or matrix ](images/06-lease-drafting-the-first-draft-is-not-the-final-draft-fig-03.png)
*Figure 6.3 — Scatterplot or matrix *

---

## The Right Workflow

None of this argues against using AI for lease drafting. First drafts and clause comparisons are genuinely useful. The question is how to use them in a way that the output can be trusted.

The workflow that solves the fluent-draft problem has three components.

The first is annotated input. Before generating a draft, supply the tool with the specific business terms: exact rent escalation formula, specific CAM exclusions agreed to, renewal option economics including the mechanism for determining fair market rent, ROFO/ROFR trigger conditions and response timelines, co-tenancy anchor definition and remedy schedule. The AI's output quality is directly proportional to the specificity of the input. A tool prompted with "draft a West Hollywood creative office lease with a 5-year term, 3% annual escalation, and a renewal option at fair market rent per CBRE submarket comps with 30-day arbitration if the parties can't agree" will produce a more accurate first draft than a tool prompted with "draft a commercial lease." [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

The second is structured review. After generating the draft, review it against the five structural decisions systematically, not impressionistically. Not "does this look right?" but "does this rent escalation formula match the LOI? Does the CAM exclusion list include everything we negotiated? Is the co-tenancy anchor definition correct?" The review is a comparison exercise with a specific reference document — the letter of intent, the deal memo, the client's instruction — not a general read for legal soundness.

The third is annotated handoff. When the draft goes to the attorney, it goes with a cover that says: this was AI-generated, these are the specific business terms it was prompted with, here are the provisions I believe need alignment with the negotiated deal, and here is the LOI for comparison. The attorney can then do targeted review of the business-term questions rather than a full re-draft from scratch. The broker has done the substantive work of identifying where the tool's output may diverge from the agreement. The attorney confirms the legal sufficiency of the resulting clauses.

That workflow uses AI for what it is actually good at — generating a plausible structural first draft at speed — and preserves human judgment for the task AI cannot do: verifying that the generated language reflects the specific business agreement between these two parties.

![Two prompt examples side by side ](images/06-lease-drafting-the-first-draft-is-not-the-final-draft-fig-04.png)
*Figure 6.4 — Two prompt examples side by side *

---

## The Fiduciary Line

One final point that the California DRE guidance makes explicit and that is worth stating directly in the context of lease drafting.

The broker's fiduciary obligation to a client includes the obligation to ensure that documents the broker transmits reflect the client's actual interest. That obligation doesn't shift to the AI tool when the broker uses one, and it doesn't shift to the attorney when the broker routes the draft for review. It stays with the broker. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

What this means in practice: a broker who transmits an AI-drafted lease to a client without reviewing it against the negotiated business terms, because "the attorney will catch it," has not satisfied their fiduciary obligation. The attorney's job is legal sufficiency. The broker's job is ensuring the document reflects the client's deal. These are different responsibilities, and one doesn't substitute for the other.

The way to think about it is simple. If a client later asks why their co-tenancy protection isn't in the lease, "the AI didn't include it and I didn't check" is not a defensible answer. "I reviewed the AI draft against our LOI, marked the co-tenancy terms for the attorney, and confirmed it was included before the document was executed" is.

That is the standard. The tool generates the first draft. The professional responsibility for whether the final draft reflects the deal belongs to the broker.

---

## LLM Exercises

The following exercises are designed to be completed with access to a large language model. They are structured experiments that reveal how AI drafting actually behaves — not just what vendors claim it does. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-lease-drafting-the-first-draft-is-not-the-final-draft-assertions.md -->

**Exercise 1 — The default clause test.** Ask an LLM to draft a renewal option clause for a commercial office lease. Accept the first output without any additional prompting. Then ask the following questions about what it produced: How is fair market rent determined? What is the notice period? Does the option survive assignment? What happens if the tenant is in default at the time of exercise? Count how many of these the clause answers and how many it leaves open. Then prompt the LLM again with specific answers to each of those questions and compare the two drafts.

**Exercise 2 — The CAM exclusion inventory.** Take a set of CAM exclusions you know to be market-standard in LA Westside office leases — from experience or from a negotiated lease you have access to. Ask an LLM to draft a CAM provision for a West Hollywood office lease. Compare the exclusions in the generated draft against your reference list. What is included, what is missing, and what appears that wasn't in your reference? What does this tell you about what the model treats as "standard"?

**Exercise 3 — The benchmark vs. the draft.** Ask an LLM a bar exam–style question about the enforceability of a co-tenancy clause under California law. Then ask it to draft a co-tenancy clause for a West Hollywood mixed-use building where the tenant's anchor is a specific fitness studio and a coffee brand, not a traditional retail anchor. Compare the quality and precision of the two outputs. Where does the LLM perform well and where does it produce generic language that wouldn't serve this specific deal?

**Exercise 4 — The annotated handoff.** Take an AI-generated lease draft — one you've produced using Exercise 1 or 2, or one from a tool you use. Write the cover note you would send to an attorney with it: identify the business terms it was prompted with, flag the provisions you believe need alignment with the negotiated deal, and note the specific questions you want the attorney to address. Then ask an LLM to review your cover note and identify anything you missed. Compare what the LLM flags against your own review.

## References

1. California Department of Real Estate. Advisory: AI in California Real Estate. 2026. https://www.dre.ca.gov/Licensees/Advisories/Advisory_2026_03_17_AI_in_California_Real_Estate.html
2. Katz, Daniel Martin, et al. GPT-4 Passes the Bar Exam. Illinois Institute of Technology, 2023. https://www.iit.edu/news/gpt-4-passes-bar-exam

## AI and Errata Disclosure

Agentic AI was used to help gather data, check assertions, and prepare supporting references for this chapter. The material goes through multiple review steps, but mistakes can still occur. Errata, corrections, and suspected mistakes may be submitted through the publisher's website at https://www.humanitarians.ai.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the figures in this chapter. Each produces a standalone HTML file you can open in a browser and modify freely.

### Figure 6.1 — Of two renewal option clauses

```
Create a standalone D3 v7 HTML figure for "Of two renewal option clauses". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 6.2 — Workflow

```
Create a standalone D3 v7 HTML figure for "Workflow". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes, arrow connectors, and direct labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 6.3 — Scatterplot or matrix

```
Create a standalone D3 v7 HTML figure for "Scatterplot or matrix". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 6.4 — Two prompt examples side by side

```
Create a standalone D3 v7 HTML figure for "Two prompt examples side by side". Use a two-panel comparison diagram with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```
