# Chapter 12 — Liability: What Happens When AI Is Wrong and Your Name Is on It


## TL;DR

- This chapter gives a working overview of Liability: What Happens When AI Is Wrong and Your Name Is on It, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through The Name on the File, What Fiduciary Duty Actually Means in This Context, Three Regulatory Signals, The File as Defense, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The model has no license to lose. You do.*

---

## The Name on the File

Here is the structural fact that every other point in this chapter follows from.

A broker uses an AI tool to generate a market analysis. The tool draws on a dataset with a coverage gap in the relevant submarket. The analysis understates recent vacancy. The broker transmits it to a client who makes a leasing decision based on it. The decision goes wrong.

The client does not sue the model. There is no model to sue — not as a licensed professional, not as a fiduciary, not as the party that represented their interest in the transaction. The client's attorney looks for the name on the deliverable. That name belongs to a human being who holds a California real estate license, who owed a duty of care and a fiduciary obligation to the client, and who made a representation — whether or not they wrote it themselves — by putting their name on a document and transmitting it. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

This is not a theoretical concern. It is the governing legal and regulatory reality of professional practice in 2026, and it has been true throughout the development of every professional tool that came before AI. When a CPA uses tax software that contains a computational error, the CPA bears responsibility for the return. When a doctor uses a diagnostic imaging tool that produces a false negative, the doctor bears responsibility for the diagnosis. The tool is a tool. The professional is the professional. Accountability does not route through the software.

What is new about AI is not the structure of professional liability. What is new is the specific failure modes that AI tools introduce — the confident-sounding wrong output, the hallucinated clause, the coverage gap that looks like data, the generative summary that reflects the model's default rather than the negotiated deal — and the speed at which AI output can move from internal first pass to client-facing deliverable without a review step that would catch those failures. The liability structure is old. The failure modes are new. The combination is the problem. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

![A document with a broker's signature at the](images/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-fig-01.png)
*Figure 12.1 — A document with a broker's signature at the*

---

## What Fiduciary Duty Actually Means in This Context

The term "fiduciary duty" appears often in discussions of professional liability and is sometimes treated as a general obligation to be careful. It is more specific than that, and the specificity matters when AI is involved. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

A licensed California real estate broker owes their client a duty of care, a duty of loyalty, a duty of disclosure, a duty of confidentiality, and a duty of accounting. Each of these has a precise legal meaning, and each of them applies to AI-assisted work in ways that are worth understanding concretely. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The duty of care means the broker must exercise the skill and care that a reasonably competent broker would exercise under similar circumstances. In the context of AI tools, this means a broker who relies on an AI output without a review step proportional to the consequence of getting it wrong has failed the duty of care — not because they used AI, but because a reasonably competent broker would have verified the output before transmitting it. The standard is not "did you use AI?" It is "was your reliance on this output reasonable given what was at stake?"

The duty of disclosure means the broker must disclose to the client all material information relevant to the transaction. In the AI context, this creates a question that has not been fully answered by California regulators but that the direction of travel suggests will be answered: is the use of AI to generate a client-facing deliverable material information? The California DRE's 2026 licensee advisory on AI doesn't resolve this definitively, but it makes clear that licensees remain responsible for accuracy and that AI use does not remove existing disclosure obligations. A prudent broker operates as though the use of AI in generating a material deliverable may need to be disclosed — and structures their workflow accordingly. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The duty of loyalty means the broker must act in the client's interest, not their own or any third party's. In the AI context, this surfaces most acutely in the algorithmic pricing situation: a broker or property manager who uses a revenue management tool that was optimizing for outcomes that don't align with the client's interest has a loyalty problem that is distinct from the accuracy problem. The RealPage situation is partly a loyalty problem — the algorithm was optimizing for landlord revenue in a way that may have been adverse to the broader market interests that antitrust law exists to protect.

The California DRE's guidance is explicit: AI use does not remove supervision, accuracy, advertising, disclosure, or fiduciary duties. That is not a qualification. It is the operating principle. The tool assists the licensee. The licensee owns the obligation.

| What the duty requires generally | How AI tool use implicates it specifically | The workflow question it generates | What failure looks like |
| --- | --- | --- | --- |
| Duty of care | Duty of disclosure | Duty of loyalty | Duty of confidentiality. Columns: What the duty requires generally, How AI tool use implicates it specifically, The workflow question it generates, What failure looks like |

---

## Three Regulatory Signals

The regulatory landscape for AI in CRE is not settled. But there are three signals — each arising from a distinct source — that together point in a clear direction, and a broker who understands them is better positioned than one who is waiting for final rules.

**The RealPage signal.** The DOJ's proposed settlement with RealPage in November 2025 established the first regulatory blueprint for what algorithmic pricing tools can and cannot do. The core prohibition: revenue management tools cannot use current, non-public, competitively sensitive data from competing landlords. The bright line is twelve-month-old data from non-active leases. Tools that cross this line create antitrust exposure, and the exposure is not limited to the vendor. The private plaintiff MDL proceeding against RealPage and co-defendant landlords is ongoing. Property managers who were users of a non-compliant tool are potential co-defendants — not because they built the algorithm, but because they used it in a way that, the plaintiffs argue, facilitated price-fixing.

The lesson for brokers is not limited to revenue management. The lesson is structural: tool use can create compliance questions even when the broker didn't build the tool, didn't design its data inputs, and may not have understood what it was doing internally. "I just used the software my firm subscribed to" has not historically been a complete defense to professional liability, and the RealPage proceedings suggest it will not be sufficient for AI tool use either. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

**The AVM signal.** The CFPB and five other federal agencies finalized quality-control standards for automated valuation models in 2024/2025. The rule applies specifically to AVMs used in mortgage-related credit decisions secured by a consumer's principal dwelling — it is primarily a residential-lending rule, not a general CRE mandate. But it signals the direction of regulatory expectation for any automated valuation output: high confidence standards, data manipulation protections, conflict-of-interest controls, random sample testing, and nondiscrimination compliance. A broker who presents an AI-generated valuation output to a client without understanding what quality controls produced it, and without labeling it appropriately, is operating against the direction the regulatory environment is traveling — even when the specific rule doesn't yet reach their transaction.

The practical standard for a CRE broker presenting an AI-generated value estimate is: label it as an automated screening output, state the source and date, explain the limitations, compare it to broker-selected comps, and separate it from the broker's professional recommendation. That is not required by a specific rule. It is required by a reasonable reading of where the duty of care sits when presenting automated valuation outputs to clients. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

**The AO-41 signal.** The Appraisal Foundation's Advisory Opinion 41, adopted April 23, 2026, establishes USPAP guidance on appraiser responsibility for AI tool use — including generative AI. It applies to appraisers, not brokers. But it is the clearest statement any professional standard-setting body has produced about how AI reliance should be structured in a licensed profession, and the framework it establishes is instructive for every licensed professional who uses AI in client-facing work.

AO-41's core requirements: document the tool used and why it was appropriate for the assignment; document how the output was evaluated for reasonableness; document why reliance was warranted; disclose AI tool use when necessary to avoid misleading the client; maintain prompts and AI outputs in the work file. Technology outputs are not assignment results. The professional's judgment is the assignment result.

A broker reading AO-41 should not conclude "this applies to appraisers, not me." They should conclude: this is what a professional standard looks like when it catches up to AI use, and the California DRE's guidance is likely to converge on a similar framework. Operating now as if that framework already applies is conservative. It is also defensible.

| What it directly governs | What it signals for CRE brokers | Specific workflow implication | Risk if ignored |
| --- | --- | --- | --- |
| RealPage DOJ settlement | AVM quality-control rule | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## The File as Defense

There is a practical discipline that emerges from the liability analysis, and it is worth stating clearly because it is more specific than "keep good records." [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

If AI was used in producing a client deliverable, the file should contain four things: the source of the AI tool or output, the prompt or input used where practical, the broker's human review notes documenting what was checked and what was verified, and the final deliverable showing any edits the broker made to the AI output before transmission. The goal is not documentation as ritual. The goal is being able to reconstruct, after the fact, that a reasonable professional exercised reasonable judgment at the appropriate point in the workflow.

The test is simple: if a client complaint or a licensing board inquiry arrives asking why a specific output was included in a deliverable, can the broker explain what they verified, what they found, and why they concluded that reliance was appropriate? If the answer is "I used the tool and transmitted what it produced," that is not a defense. If the answer is "I used the tool, checked the output against the comps I know, identified that the submarket estimate was based on thin data and noted that in the document, and presented it as a screening estimate rather than a valuation conclusion," that is a defense.

The documentation standard is not onerous. A note in the file — "AI-generated market analysis, reviewed against CoStar Q1 2026 data, coverage thin in WeHo creative office, presented as screening only" — is more than nothing and less than a legal brief. It is a professional record that reflects a professional's judgment. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

What the documentation should not contain is a prompt engineered to produce a specific output, or evidence that the broker transmitted AI output without review in a context where review was clearly required. Documentation is a defense only if the underlying workflow was defensible. It is not a substitute for the workflow.

![A sample file annotation ](images/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-fig-02.png)
*Figure 12.2 — A sample file annotation *

---

## What "The Vendor Is Liable" Gets Wrong

There is a specific reasoning error that surfaces regularly when brokers discuss AI liability, and it is worth addressing directly because it produces the wrong workflow.

The reasoning goes: the vendor built the tool, the vendor trained the model, the vendor made claims about accuracy — therefore, if the tool produces a wrong output, the vendor bears the liability. The broker was just using the product. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

This reasoning is wrong in two ways.

First, it conflates vendor liability and broker liability as if they were mutually exclusive. They are not. The vendor may have liability for building a tool that performs below its stated claims, for failing to disclose material limitations, or for design choices that made failures foreseeable. The broker has separate liability for choosing to rely on that tool in a specific context, failing to review its output at the appropriate standard of care, and transmitting that output to a client in a way that created a professional representation. These are independent claims. Both can be true simultaneously. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

Second, and more fundamentally, it misunderstands the structure of professional duty. A licensed broker's duty to their client is not contingent on the tools they use being reliable. The duty is to the client, and it includes the obligation to exercise reasonable care in selecting tools, understanding their limitations, and reviewing their outputs before reliance. If a broker uses a tool that they know has thin submarket coverage, in a submarket where coverage is thin, and presents its output without that qualification, the fact that the vendor's marketing materials claimed 95% accuracy is a limited defense. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The correct framing is not "who is liable — the vendor or me?" It is "what did I verify, and was my level of verification proportional to the stakes?" That framing points toward the right workflow: use the tool for what it does well, understand what it doesn't do well, review the output before it becomes a client deliverable, and document the review.

---

## The Disclosure Question

One question the source material for this chapter flags as unsettled — and that is worth sitting with rather than resolving prematurely — is what AI use a broker should affirmatively disclose to clients.

California's regulatory posture on AI disclosure in real estate transactions is evolving. The 2026 DRE advisory makes clear that existing disclosure obligations apply to AI-assisted work, but it does not yet create a specific disclosure requirement for AI tool use in the way that, say, dual-agency representation creates a mandatory disclosure requirement. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The prudent approach, in the absence of a specific rule, is to consider materiality. If a client would likely consider it significant — in deciding whether to rely on a deliverable, in evaluating the professional's work, in making a transaction decision — then the fact that the deliverable was AI-assisted is probably material information that the duty of disclosure reaches. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The more specific question is what the disclosure should say. "This analysis was produced with the assistance of AI tools" is accurate and almost meaningless. A more useful disclosure names the tool, the nature of its output (screening estimate, document extraction, demand signal), the review the broker performed, and the limitation the broker identified. That disclosure does two things simultaneously: it satisfies the duty of disclosure and it demonstrates the professional judgment the broker exercised. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

There are uses of AI that go beyond disclosure and require counsel before proceeding. Presenting an AI-generated AVM output as a valuation conclusion, using an AI lease abstraction without source-document verification in a transaction with material clause-level consequences, and incorporating revenue management outputs in a market where algorithmic pricing is under active regulatory scrutiny — these are situations where the broker should consult with their attorney before the workflow is designed, not after the output is transmitted. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

Disclosure does not replace diligence. The correct sequence is: verify that the use is appropriate, perform proportional review, disclose what was used and what was checked. Not: use the output, transmit it to the client, and add a disclosure that AI was involved. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

---

## The Fair Housing Dimension

One liability dimension that deserves explicit mention because it is underweighted in most AI and CRE discussions is fair housing and nondiscrimination. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The Fair Housing Act and California's Unruh Civil Rights Act create protected-class obligations that apply to commercial transactions involving residential properties — multifamily acquisitions, mixed-use projects with residential components, and tenant screening tools used in housing contexts. The ECOA's nondiscrimination requirements apply to commercial credit decisions. The AI tools used in these contexts — tenant screening algorithms, AVM tools, revenue management systems, market analysis tools that influence tenant selection — all have the potential to produce disparate-impact outcomes that create fair housing exposure.

This is not theoretical. The SafeRent settlement, in which a tenant screening algorithm was found to discriminate against housing-choice voucher applicants, resulted in both operational restrictions on the algorithm's use and monetary damages. The fact that the algorithm produced the discriminatory outcome rather than a human making a deliberate discriminatory decision did not remove the liability. The AI feature became the discrimination mechanism, and the company that deployed it bore the consequence. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

For CRE brokers, the practical implication is: any AI tool used in a context that touches housing, residential tenancy, or residential credit decisions should be evaluated for disparate-impact risk before deployment — not just for accuracy, coverage, and methodology, but for whether its outputs treat protected classes differently in ways that would not survive a fair housing analysis. This is a question for counsel and, in larger organizations, for a formal risk assessment. It is not a question the broker should answer alone based on the vendor's marketing materials.

| Potential liability theory | Regulatory signal that applies | Documentation required | When to consult counsel |
| --- | --- | --- | --- |
| Market analysis | Lease abstraction | Revenue management | AVM output |

---

## Unsettled Regulation Is Not a Reason to Wait

The source material for this chapter includes a flag that some of the regulatory landscape is contested — the RealPage settlement is proposed, not final; state actions are proceeding independently; the direction of California DRE guidance on AI disclosure is not yet crystallized. It is worth addressing that uncertainty directly, because it sometimes produces the wrong conclusion.

The wrong conclusion is: regulation is too unsettled to act on, so the right posture is to wait and see. That conclusion has it backwards.

Unsettled regulation is a reason for conservative workflow, not for improvisation. When the regulatory standard isn't clear, the professional who is building a defensible record of reasonable judgment under ambiguous conditions is in a better position than the one who is waiting for a clear rule before taking the question seriously. The first broker can demonstrate, in a future proceeding, that they were exercising professional judgment about a genuinely uncertain question. The second broker has documentation that they weren't thinking about it at all. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The direction of regulatory travel in AI and professional services is clear even when the destination is not yet fixed: more documentation, more disclosure, more accountability for AI tool selection and review, and less tolerance for "the vendor said it was accurate." The NIST AI Risk Management Framework, ISO/IEC 42001 on AI management systems, the AVM quality-control rule, AO-41, and the California DRE advisory all point the same direction. The broker who builds their workflow against that direction now has less adjustment to make when the specific rules arrive — and a more defensible record in the meantime. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

The standard to aim for is simple. For any AI-assisted client deliverable, be able to answer three questions: What did the tool produce? What did I check? Why was my reliance on this output reasonable given the stakes? If those three questions have honest, documented answers, the workflow is defensible. If any of them don't, it isn't — regardless of what the specific rule says.

![Regulatory convergence diagram ](images/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-fig-03.png)
*Figure 12.3 — Regulatory convergence diagram *

---

## LLM Exercises

The following exercises are designed to be completed with access to a large language model. They are structured experiments in liability awareness — using AI to test your own understanding of where professional responsibility sits. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/12-liability-what-happens-when-ai-is-wrong-and-your-name-is-on-it-assertions.md -->

**Exercise 1 — The liability chain.** Describe to an LLM a realistic scenario in which a CRE broker used an AI tool in producing a client deliverable that turned out to contain a material error. Ask the LLM to walk through the potential liability theories: breach of fiduciary duty, negligence, misrepresentation, regulatory violation. Then identify which of the theories the LLM describes accurately and which it understates or overstates. What does the exercise reveal about the limits of AI legal analysis on fact-specific questions?

**Exercise 2 — The disclosure draft.** Take a real or hypothetical AI-assisted deliverable from your practice — a market analysis, a lease abstract, a comp set, a draft offering memo. Ask an LLM to draft a disclosure paragraph that could accompany that deliverable: naming the tool, characterizing the nature of the output, describing the review performed, and identifying the limitation flagged. Evaluate whether the resulting disclosure is accurate, specific enough to be meaningful, and positioned correctly relative to the broker's professional recommendation. What would you change?

**Exercise 3 — The documentation audit.** Describe your current workflow for AI-assisted client deliverables to an LLM. Ask it to audit the workflow against the three questions in this chapter: What did the tool produce? What did you check? Why was reliance reasonable given the stakes? Where does your current workflow produce clear answers to these questions and where does it leave gaps? What would you add or change?

**Exercise 4 — The regulatory direction read.** Ask an LLM to summarize the current regulatory signals affecting AI use in CRE brokerage — the RealPage settlement, the AVM quality-control rule, USPAP AO-41, and California DRE guidance. Then ask it to project what a California-specific broker AI-use standard might look like if the regulatory trend continues for another two years. Evaluate whether its projection is consistent with the analysis in this chapter and where it diverges. What does the divergence tell you about the limits of forward-looking regulatory analysis?

## References

1. California Department of Real Estate. Advisory: AI in California Real Estate. 2026. https://www.dre.ca.gov/Licensees/Advisories/Advisory_2026_03_17_AI_in_California_Real_Estate.html
2. U.S. Department of Justice. Justice Department Sues RealPage for Algorithmic Pricing Scheme that Harms Millions of American Renters. 2024. https://www.justice.gov/opa/pr/justice-department-sues-realpage-algorithmic-pricing-scheme-harms-millions-american-renters
## AI and Errata Disclosure

Agentic AI was used to help gather data, check assertions, and prepare supporting references for this chapter. The material goes through multiple review steps, but mistakes can still occur. Errata, corrections, and suspected mistakes may be submitted through the publisher's website at https://www.humanitarians.ai.
