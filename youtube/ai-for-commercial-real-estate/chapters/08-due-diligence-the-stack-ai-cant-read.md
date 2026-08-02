# Chapter 8 — Due Diligence: The Stack AI Can't Read

## TL;DR

- Extracting every document is not the same as understanding what they say to each other.
- The chapter moves through Why extraction is not reconciliation, The amendment-stack problem, The seller-disclosure problem, The zoning contradiction problem, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Extracting every document is not the same as understanding what they say to each other.*

![A data room folder listing ](images/08-due-diligence-the-stack-ai-cant-read-fig-01.png)
*Figure 8.1 — A data room folder listing *

Suppose you have a data room with forty documents. Leases, amendments, rent rolls, operating statements, title report, zoning summary, environmental phase one, property condition report. An AI tool reads every file. It extracts each one cleanly — tenant names, rent figures, expiration dates, clause summaries, environmental findings, code references. It produces a summary of each document that a senior analyst would recognize as accurate.

Now the buyer asks three questions. Which rent escalation actually governs — the base lease or the fourth amendment? Does the tenant's actual payment history match the contracted schedule? Why does the zoning map show a different classification than the written municipal code?

The tool read the files. It did not read the stack.

That distinction is what this chapter is about. Due diligence is not a document-reading problem. It is a reconciliation problem. The question is not what each document says. The question is whether the documents agree, which one controls when they conflict, what the discrepancy reveals about the asset, and what is missing from the pile entirely. Those are different problems, and the second set requires something the extraction tool was not built to do. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

---

## Why extraction is not reconciliation

The word "extract" is precise. A language model extracts: it reads a document and pulls out the information that matches a pattern — a rent figure, a clause type, a date. It does this well and fast. For a forty-document data room, extraction can compress days of initial reading into hours.

But extraction operates on each document independently. The model reads the base lease and extracts the rent schedule. It reads the fourth amendment and extracts the modified term. It reads the rent roll and extracts the current payment. Each extraction is accurate. What the model does not do, unless specifically engineered to do so, is ask: do these three things agree? If they disagree, which one reflects reality? If they conflict, which one controls legally? [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

![Three document boxes ](images/08-due-diligence-the-stack-ai-cant-read-fig-02.png)
*Figure 8.2 — Three document boxes *

Reconciliation is not pattern-matching on a single document. It is pattern-matching across documents, in sequence, with legal and practical judgment about which document supersedes which. That requires understanding document hierarchy — which amendment modifies which provision, whether a side letter overrides a lease clause, whether an informal concession in an email has any legal standing. It requires understanding time — reading the amendment stack chronologically to reconstruct the contractual history of the tenancy. It requires understanding absence — noticing that a service contract referenced in the operating statement is not in the data room, which may mean it was never provided or may mean the seller chose not to provide it. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

None of those tasks are extraction tasks. They are reasoning tasks that require a framework the extraction tool does not have.

![Extraction vs](images/08-due-diligence-the-stack-ai-cant-read-fig-03.png)
*Figure 8.3 — Extraction vs*

---

## The amendment-stack problem

A base lease and six amendments are not seven independent documents. They are a single legal and business relationship, recorded in chronological sequence, with each document modifying or superseding specific provisions of what came before.

The active economics of a tenancy may live in the original lease, in the most recent amendment, in a side letter, or in an exhibit that one of the amendments incorporates by reference. To know which provision governs, you have to read the documents in order, track which provisions each amendment modifies, and determine whether any later document explicitly or implicitly supersedes an earlier one. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

![Amendment stack as a timeline ](images/08-due-diligence-the-stack-ai-cant-read-fig-04.png)
*Figure 8.4 — Amendment stack as a timeline *

This is not a hard problem for a careful lawyer or a diligent broker who has read enough amendment stacks. It is a hard problem for an extraction tool because the tool has to hold the entire sequence in working memory, track the state of each provision across documents, and notice when a later document changes the meaning of an earlier one. General-purpose AI tools can sometimes do this. They can also fail silently — producing a confident summary of the governing economics that reflects the base lease, or the most recent amendment, or some average of both, without flagging that the answer required sequence reasoning across six documents. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

The risk is not that the tool is wrong. The risk is that the tool is confidently wrong in a way that looks exactly like being right.

The practical rule: any time the data room contains a base lease with more than two amendments, the amendment stack needs to be read chronologically by a human who is tracking the state of the material provisions. The tool can flag the amendments. The human has to sequence them.

---

## The seller-disclosure problem

There is a second problem that is more fundamental: AI cannot extract what the seller did not provide.

A data room can be complete — in the sense that every document the seller chose to include is there — and still be missing the documents that would change the buyer's assessment. Missing service contracts mean the buyer does not know the terms of ongoing vendor relationships. Incomplete environmental history means a phase one that looks clean may be missing context. Unreported tenant disputes mean a rent roll that shows full occupancy may obscure a pending vacancy. Informal concessions that never made it into an amendment mean the rent roll shows a number the tenant has not been paying. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

| What's missing | Why it might be absent | What it could mean for the transaction |
| --- | --- | --- |
| missing service contract, incomplete environmental chain, undisclosed tenant dispute, informal concession not in amendment stack, verbal understanding about renewal. Each row shows how absence of evidence is different from evidence of absence. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

The worked example in this chapter illustrates the informal concession problem precisely. The rent roll shows a tenant paying below-market rent. The lease abstract shows scheduled escalations that should have brought rent to a higher number. The amendments reveal a temporary concession granted after a buildout delay. But the property-management ledger shows the concession continued informally — not documented in any amendment, not reflected in any formal agreement — just a pattern of lower payments that the management company accepted and never corrected.

The AI tool read every document that was in the data room. It extracted the rent figures, the concession terms, the escalation schedule. What it could not do is notice that the informal continuation of the concession, visible only in the ledger, contradicts the contracted income that the broker has been representing to the buyer. That contradiction requires comparing a document (the rent schedule in the amendment) against a pattern in data (the actual payment history in the ledger) against the absence of any documentation memorializing the continued concession — and then asking what that combination means for the income underwriting. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

That is not extraction. That is investigation.

![Ledger and lease amendment ](images/08-due-diligence-the-stack-ai-cant-read-fig-05.png)
*Figure 8.5 — Ledger and lease amendment *

---

## The zoning contradiction problem

Zoning data is harder than it looks. The National Zoning Atlas project — an effort to standardize and digitize zoning codes across American jurisdictions — exists precisely because zoning information is inconsistently maintained, incompletely digitized, and surprisingly difficult to reconcile even for experts. Research by Xu, Markley, Bronin, and Drogaris on zoning complexity shows that zoning codes frequently contain provisions that interact in non-obvious ways, with outcomes that require local expertise to interpret correctly.

For a broker using an AI tool to screen a potential acquisition, a zoning summary that says "commercially zoned, retail permitted" may be accurate as far as it goes. It may also be missing an overlay district that restricts signage, a conditional use requirement that applies to the tenant type, a parking minimum that affects the asset's usability, or a historic preservation designation that limits renovation options.

| What the automated summary says | What local verification might reveal |
| --- | --- |
| should function as a verification checklist, not just an illustration. | A concrete checkpoint for applying the chapter concept. |

In the LA/Westside market, this problem is particularly acute. A property in Culver City may be subject to CEQA requirements that affect the timeline for renovation or change of use. A Beverly Hills retail asset may be subject to parking constraints specific to the municipality. A West Hollywood property may carry a historic preservation overlay. A Marina del Rey asset may be in the coastal zone with California Coastal Commission jurisdiction. A Brentwood mixed-use building may be subject to a specific plan that modifies the base zoning in ways that are not visible in a standard zoning summary. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

None of these are exotic edge cases. They are normal features of the local regulatory environment. A document summary cannot replace a call to someone who knows what the local planning department actually does with applications of that type — not what the code says, but how it is applied.

---

## What due diligence is actually for

It helps to be precise about what due diligence is trying to accomplish, because that clarity tells you where AI is genuinely useful and where it is not.

Due diligence is an attempt to discover, before closing, the facts that would change the buyer's decision or the buyer's price. Some of those facts are in documents. Some are in patterns across documents. Some are in the absence of documents that should be there. Some are in the behavior of the property — what tenants are actually paying, how the building is actually operating — rather than in what documents say the property should be doing. And some are in information the seller has and has not disclosed.

AI is well-suited to the first category. For a forty-document data room, automated extraction can identify the relevant provisions in each document, flag provisions that warrant attention, compare stated figures against each other within a single document, and produce a structured summary that gives the buyer's team a starting point. That is genuine, substantial value. A task that used to take days of initial review can take hours.

It is less suited to the second and third categories — patterns across documents and significant absences — without specific engineering to handle those tasks. It is not suited to the fourth and fifth categories at all. Tenant behavior is in operational data, not in the lease. Seller knowledge is not in the data room.

![Due diligence information taxonomy ](images/08-due-diligence-the-stack-ai-cant-read-fig-06.png)
*Figure 8.6 — Due diligence information taxonomy *

The broker's job in due diligence is to move through all five tiers, using AI for acceleration on the first and partial assistance on the second, and applying professional judgment — including the judgment to involve counsel, environmental consultants, and local regulatory experts — on the rest.

---

## The reconciliation workflow

The practical answer to the due diligence problem is a workflow that makes the division of labor explicit.

Use AI to index and extract. Every document in the data room should be read and extracted, with the AI producing a structured summary of each: parties, key terms, dates, economic provisions, obligations, and flags for anything that looks unusual by pattern. This step the machine does well. It compresses days into hours and ensures that no document is missed in the initial pass.

Use AI to compare stated figures. Rent roll against lease abstracts. Operating statements against rent roll. Stated income against actual receipts in the property management ledger. These comparisons can be partially automated, and the flags they produce — discrepancies between the rent roll and the lease schedule, for instance — are valuable starting points for investigation. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

Then stop and do the human work. Read the amendment stack chronologically. Reconstruct the contractual history of each tenancy. Identify the provisions that have been modified and confirm which version governs. Check the data room index against the categories of documents that should be there — what is missing and why. Call the local planning department, or someone who has dealt with them recently on comparable applications. Ask for any documents not in the data room that bear on the transaction.

| Task | Tool | Human check required |
| --- | --- | --- |
| index all documents (AI | verify completeness | A concrete checkpoint for applying the chapter concept. |
| extract provisions from each document (AI | spot-check | A concrete checkpoint for applying the chapter concept. |
| compare rent roll to leases (AI | investigate discrepancies | A concrete checkpoint for applying the chapter concept. |
| read amendment stack in sequence (human | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| identify missing documents (human | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| verify zoning locally (human | local expert | A concrete checkpoint for applying the chapter concept. |
| assess informal concessions (human | ledger review | A concrete checkpoint for applying the chapter concept. |
| final risk assessment (human | counsel). Should function as a working protocol. | A concrete checkpoint for applying the chapter concept. |

The protocol is not about using AI less. It is about using AI on the tasks AI is built for, and doing the human work on the tasks that require it.

---

## The misconceptions, honestly examined

The first misconception is that a complete data room means complete diligence. A data room can contain every document the seller chose to provide and still omit the documents that matter most. Completeness of the data room is not the same as completeness of disclosure. The broker's job includes asking what is missing. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

The second misconception is that accurate extraction from each document means the package is understood. Understanding the package requires understanding the relationships among the documents — chronology, hierarchy, conflict, and silence. A set of accurate summaries is not a reconciled picture of the asset. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-due-diligence-the-stack-ai-cant-read-assertions.md -->

The third misconception is that zoning summaries are sufficient for early decisions. They are useful for screening — for quickly eliminating assets where the use type is clearly incompatible. But before any representation to a client about what the property can do, the zoning needs local verification. The automated summary is a starting point, not a conclusion.

---

## What you should be able to do now

By the end of this chapter, you should be able to look at any data room and ask: have the documents been extracted, and have they been reconciled? Is the amendment stack sequenced, and does the sequenced stack agree with the rent roll? What is missing from the data room, and does the absence mean anything? Has the zoning been locally verified, or is the summary based only on the digital record?

The buyer in the opening case did not need a better extraction tool. The buyer needed a broker who understood that reading every document is not the same as reading the stack — and who had a workflow that made cross-document reconciliation, missing-evidence investigation, and local regulatory verification explicit steps, not afterthoughts.

That workflow is what this chapter was built to produce.

---

## Bridge

Due diligence is mostly documents, and the decisive problems are about what the documents say to each other and what is not there. Negotiation is partly documents too — term sheets, letters of intent, redlines — but the decisive information is often not written down at all. It is in the room.

---

## LLM Exercises

**Apply:** Choose one active or recent transaction that involved a multi-document data room. Identify one place where two documents stated or implied different things. Write out the reconciliation process: which document controlled, how you determined that, and what the discrepancy told you about the asset.

**Analyze:** Return to the informal-concession case from this chapter. Identify the exact point where automated extraction stops being enough and human investigation has to begin. Write a paragraph explaining the gap between what the tool found and what the broker needed to know.

**Create:** Design a due diligence protocol for your own practice that specifies which tasks go to AI extraction, which tasks require human cross-document reconciliation, and which tasks always require a local expert or counsel. The protocol should be specific enough that a junior colleague could follow it without supervision on a standard Westside transaction.

---

## Sources Used

- Partner Engineering and Science, "Commercial Real Estate Due Diligence Checklist," 2024.
- National Zoning Atlas project materials.
- Xu, Markley, Bronin, and Drogaris, "Zoning by a Thousand Cuts," 2023, Cityscape/HUD User.
- California Office of Planning and Research, CEQA guidance materials.

## References

No references added by fact-check pass.
## AI and Errata Disclosure

Agentic AI was used to help gather data, check assertions, and prepare supporting references for this chapter. The material goes through multiple review steps, but mistakes can still occur. Errata, corrections, and suspected mistakes may be submitted through the publisher's website at https://www.humanitarians.ai.
