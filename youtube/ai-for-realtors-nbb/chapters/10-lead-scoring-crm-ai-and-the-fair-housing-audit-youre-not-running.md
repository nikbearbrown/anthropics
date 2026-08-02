# Chapter 10 — Lead Scoring, CRM AI, and the Fair Housing Audit You're Not Running
*The model learned from the agent's behavior. It didn't need discriminatory intent to amplify a discriminatory pattern.*

---

The CRM learned from the agent. Not from instructions — the agent never typed in a set of rules about who to call first. It learned from behavior: who got fast callbacks, which zip codes converted, which price points the agent actually worked, which searches got attention and which ones quietly expired. Over time, the model built a lead-scoring algorithm tuned to the agent's historical patterns of response. Then it started applying that algorithm to new leads — prioritizing some, deprioritizing others, automating the attention allocation that used to be a conscious choice.

The agent did not intend to discriminate. The model did not need intent to amplify a pattern.

That is the central problem this chapter is about. It is not a problem about malicious design. It is a problem about what happens when a machine learning system is trained on human behavior, that behavior contains implicit patterns, and the system replicates those patterns at scale without anyone noticing — because the output looks like productivity improvement, not Fair Housing risk.

---

## Why CRM Scoring Is Genuinely Useful

Before the compliance analysis, the value case deserves a fair statement — because the tools are useful, and dismissing them is not the answer.

An active agent with several hundred leads in a database faces a genuine attention allocation problem. Not every lead is at the same stage. Not every inquiry represents the same level of readiness. A first-time buyer browsing casually in a market they can't yet afford is a different conversation than a buyer who has been pre-approved, has toured four properties, and whose saved searches have converged on a specific neighborhood and price band. Treating those two contacts identically is not professional practice — it is noise. The agent who can identify the second contact and respond appropriately, at the moment they're ready, provides better service and closes more business.

CRM behavioral scoring automates part of that identification. It watches the behavioral signals — email opens, listing views, saved search activity, response patterns — and surfaces leads whose behavior suggests readiness. The 2025 NAR Technology Survey documents wide adoption of these tools, and the product materials from Follow Up Boss, Lofty, and Ylopo are explicit about the mechanism: behavioral signals feed a scoring model, scored leads get prioritized in the agent's queue, and follow-up timing is automated around those scores.

This is real value. The compliance question is not whether to use it. It is whether the scoring model is amplifying behavioral patterns that correlate with protected class characteristics — and whether the agent has ever checked.

| function | how it works | genuine value | Fair Housing risk |
| --- | --- | --- | --- |
| lead prioritization by behavioral signal, automated follow-up timing, contact segmentation by engagement level, source and campaign attribution, geographic filtering | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| reader should see that the same functions that create productivity value are the ones that can create Fair Housing risk | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## The Proxy Variable Problem

Fair Housing law prohibits discrimination on the basis of race, color, national origin, religion, sex, familial status, and disability. It also, under the disparate impact standard established in 24 CFR Part 100 and repeatedly affirmed by HUD, prohibits practices that have a discriminatory effect even when there is no discriminatory intent. The standard asks not whether the agent meant to discriminate, but whether the practice produces outcomes that differ significantly across protected classes without a legitimate, non-discriminatory justification.

The proxy variable problem is how that standard applies to CRM scoring. A proxy variable is a variable that is not itself a protected class characteristic but correlates with one. Geographic data — zip codes, neighborhoods, school district searches — correlates with race and national origin in ways that are well-documented in the academic literature and explicitly acknowledged in HUD's 2024 digital advertising guidance. Price point can correlate with familial status and disability. Language preference correlates with national origin. Response timing — which contacts tend to respond quickly, which ones take longer — can correlate with employment patterns that differ across protected classes.

None of these variables is inherently discriminatory. A buyer searching in a specific zip code is expressing a genuine preference. A lead who responds to emails quickly is demonstrating engagement. These are real signals that a scoring model legitimately uses. The risk is not the individual variable. It is the pattern across variables, trained on the agent's historical behavior, replicating and amplifying whatever implicit biases existed in that behavior.

| variable | what it measures legitimately | what it can correlate with (protected class) | risk level | audit question to ask |
| --- | --- | --- | --- | --- |
| zip code | geography, price point range, school district searches, response timing, communication language, listing type preferences, lead source | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

The SafeRent Solutions settlement in 2024 makes this concrete in an adjacent context. SafeRent's tenant screening algorithm used variables including payment history, credit score, and income — legitimate inputs for rental screening — in a model that produced outcomes with a statistically significant disparate impact on Black and Hispanic applicants. The settlement did not turn on whether SafeRent intended to discriminate. It turned on whether the model's outputs were discriminatory in effect. The principle transfers directly to CRM lead scoring: the relevant question is not the agent's intent. It is whether the model's prioritization outputs differ significantly across protected class proxies.

HUD's 2024 guidance on digital advertising makes the application to real estate agents explicit. The guidance addresses the distribution of housing opportunities through digital platforms, and its core principle — that automated systems that distribute attention, advertising, or access to housing opportunities must be evaluated for disparate impact regardless of intent — applies to CRM tools that automate attention allocation as clearly as it applies to targeted advertising algorithms.

---

## What the Audit Actually Looks Like

The audit is not a legal analysis. It is a pattern check that any agent can run with the data they already have. It does not require access to the model's variables or a data scientist. It requires a willingness to look at the output and ask whether it makes sense.

Here is the procedure.

**Step one: Export the last 30 to 100 prioritized leads.** Most CRM platforms have an export or reporting function. Pull the leads that received the highest scores, the fastest automated follow-up, or the first position in the agent's callback queue over the period you're reviewing.

**Step two: Compare against all new leads received in the same period.** The question is not whether the high-priority leads are engaged — they probably are, because that's what the scoring model is designed to identify. The question is whether the set of high-priority leads differs from the set of all leads in ways that map to protected class proxies.

**Step three: Look for geographic clustering.** Do the high-priority leads cluster in specific zip codes or neighborhoods? If they do, are those zip codes or neighborhoods demographically homogeneous in ways that suggest the scoring model is weighting geography as a proxy? This check does not require demographic data on the leads themselves — it requires comparing the geographic distribution of high-priority leads against the geographic distribution of all leads and asking whether the difference is explainable by engagement behavior alone.

**Step four: Look for price point clustering.** Do the high-priority leads cluster in specific price ranges? Is the lower end of the agent's price range underrepresented in the high-priority set relative to its share of all leads?

**Step five: Look for source and language patterns.** Are leads from certain campaigns, referral sources, or in certain languages consistently underrepresented in the high-priority set? Source can correlate with demographics if the agent's marketing reaches some populations more than others.

| step | what to export or review | what pattern to look for | what a problematic finding looks like | what to do if you find it |
| --- | --- | --- | --- | --- |
| geographic clustering check, price point distribution check, source and campaign pattern check, language preference check, response timing baseline check | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

**Step six: Ask whether the pattern is explainable.** If geographic clustering exists in the high-priority leads, is it fully explained by engagement behavior — the leads from those zip codes simply opened more emails and viewed more listings — or does it persist even after controlling for engagement? If you can't answer that question from the data your CRM provides, you have an unresolved risk.

The limit: some agents will need broker, vendor, or attorney assistance to access the variables and run a meaningful audit. The CRM's scoring model may not be transparent about which variables it uses or how they're weighted. If the vendor cannot explain the model's variables, that opacity is itself a risk factor. A model you cannot audit is a model whose Fair Housing compliance you cannot verify.

---

## The Attention Allocation Principle

There is a framing that makes the Fair Housing analysis more intuitive and harder to dismiss: attention allocation is housing opportunity allocation.

When a CRM system prioritizes some leads over others, it is determining which people receive prompt, engaged professional service and which people receive slower, less attentive service or none at all. That differential is not just a productivity metric. It is a difference in access to housing assistance — the same assistance the Fair Housing Act is designed to make equally available.

The legal framework for this principle is grounded in HUD's steering cases, where agents who directed some clients toward certain neighborhoods and away from others were found to have violated the Fair Housing Act regardless of the clients' stated preferences. The CRM analog is not steering in the traditional sense — the agent is not directing clients to different properties. But a scoring model that systematically deprioritizes leads from certain geographies or price ranges is producing a differential in service access that maps onto the same protected class concerns.

![Attention allocation chain ](images/10-lead-scoring-crm-ai-and-the-fair-housing-audit-youre-not-running-fig-01.png)
*Figure 10.1 — Attention allocation chain *

This framing also clarifies the response to the most common objection: "I didn't choose the variables, so I'm not responsible for them." The legal standard does not turn on whether the agent designed the algorithm. It turns on whether the agent uses a practice that produces discriminatory effects. An agent who runs a CRM scoring system that produces disparate impact outcomes and does not audit that system has used a discriminatory practice — regardless of whether they understood what the model was doing.

---

## What to Do When the Audit Finds a Problem

If the audit produces a finding — geographic clustering, price point skew, source pattern — the response has three components.

**Document the finding.** Write down what you found, when you found it, and what data you used. If this becomes relevant in an inquiry, documentation of a good-faith audit effort and a response plan is a materially better position than no audit at all.

**Configure or override.** Most CRM platforms provide configuration options that allow agents to adjust scoring weights, reset learning baselines, or impose manual overrides on specific lead segments. If geographic weighting is driving clustering, reducing or eliminating geographic variables from the scoring model is the direct fix. If the model has learned patterns from a historical period that reflected problematic behavior, resetting the learning baseline removes the contaminated training data.

**Consult the vendor.** Ask explicitly: what variables does the scoring model use, how are they weighted, and can I see how the model was trained? A vendor that cannot or will not answer those questions is providing a tool whose Fair Housing compliance you cannot verify. That is a vendor relationship worth reconsidering.

**Consult your broker.** Fair Housing compliance obligations run through the brokerage, and the broker has both the authority and the obligation to address systemic compliance issues. A finding in a CRM audit is the kind of issue brokers need to know about, both to address it and to ensure their E&O coverage and compliance protocols are aligned with the risk.

| finding type | immediate action | configuration fix | documentation required | who to consult |
| --- | --- | --- | --- | --- |
| geographic clustering in high-priority leads, price point underrepresentation at lower end, source | campaign demographic skew, language preference pattern, unexplainable score variance across lead segments | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## The Reconfiguration Question

One complication in the CRM audit process is the reconfiguration question: if the scoring model has been learning from the agent's behavior for months or years, resetting it may reduce short-term scoring accuracy. The model was calibrated to the agent's actual conversion patterns, and those patterns — problematic elements aside — contain real signal. Resetting the baseline means starting the learning process over.

This is a real cost, and acknowledging it is more useful than pretending it isn't there. The response is proportionality: the reconfiguration cost is proportionate to the risk the audit found. An audit that finds no clustering and no problematic pattern requires no reconfiguration. An audit that finds significant geographic skew in lead prioritization has identified a Fair Housing risk that outweighs the temporary scoring accuracy cost of a reset.

The practical approach: reset the variables that the audit identified as problematic, preserve the variables that the audit found unproblematic, and run a follow-up audit after three to six months of retraining to verify that the problematic patterns have not re-emerged. This is not a one-time fix. CRM scoring systems continue to learn, and the patterns they learn from continue to be the agent's behavior. The audit is a recurring discipline, not a one-time event.

| audit finding severity | reconfiguration action | variables to reset | variables to preserve | follow-up audit timing |
| --- | --- | --- | --- | --- |
| no problematic pattern found (no action needed | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| minor clustering in one variable (targeted variable adjustment | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| significant geographic or price point skew (full baseline reset for affected variables | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| unexplainable variance across multiple proxies (full reset plus vendor consultation plus broker notification | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| reader should be able to locate their audit result in a row and read across to the proportionate response | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## What Would Change This Chapter

This chapter would need revision if CRM vendors provided transparent, independently audited Fair Housing controls with agent-accessible explanations for lead scores. Currently, the opacity of scoring models is the primary obstacle to meaningful agent-level compliance. If vendors made variable weights transparent and provided built-in disparate impact reporting — the kind of capability that would let an agent run the pattern check described here inside the platform rather than by exporting to a spreadsheet — the audit procedure would be simpler and more reliable.

That transparency would not eliminate the compliance obligation. It would make the obligation more easily dischargeable. Until then, the export-and-compare audit described here is the available tool.

---

## What This Chapter Adds

The book's argument is that the agent owns every output that affects a client's experience of the transaction. CRM scoring is the chapter where that argument meets a practice that most agents have never examined — not because they don't care about Fair Housing, but because the scoring system looked like a productivity tool, not a compliance obligation.

The audit procedure in this chapter is the translation of that obligation into a practice. Thirty to a hundred leads, a geographic cluster check, a price point check, a source pattern check, a documentation record. Not a legal analysis. A habit. The same habit the book has been building since Chapter 1 — applied to the part of the practice that automates attention rather than language.

---

## LLM Exercises

**Apply:** Export the last 30 to 100 leads your CRM has flagged as high-priority or top-scored. Run the five-step audit from this chapter: geographic clustering, price point distribution, source and campaign patterns, language preference, response timing baseline. Document what you find. If any check produces a pattern you cannot explain by engagement behavior alone, identify the specific next step — configuration change, vendor consultation, or broker notification.

**Analyze:** The chapter introduces the proxy variable problem — variables that are not protected class characteristics but correlate with them. Take the specific CRM platform you use or are most familiar with and identify which variables its scoring model is documented or likely to use. For each variable, classify it as low proxy risk, moderate proxy risk, or high proxy risk based on the framework in this chapter. What does your analysis suggest about the audit priority for your specific tool?

**Create:** Draft a one-paragraph CRM Fair Housing audit policy for your practice. It should specify how often the audit runs, what data gets reviewed, what a problematic finding triggers, and who gets notified. Write it as an operational document, not a compliance disclaimer — something that would change what your team does quarterly, not just something that would be cited if a complaint arrived.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 10.1 — Attention allocation chain

Create a standalone D3 v7 HTML file for a left-to-right process diagram titled "Attention allocation chain". Use 4-5 labeled items drawn from a real-estate AI workflow: source/input, AI draft, human audit, risk review, and client-ready action. Encode the primary AI-assisted step with one red series or mark, and use neutral ink/gray for all other marks. Include direct labels, a zero baseline if numeric values are shown, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-lead-scoring-crm-ai-and-the-fair-housing-audit-youre-not-running-fig-01.html`
