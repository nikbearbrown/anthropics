# Chapter 7 — Lease Abstraction: The 95% That Hides the 5%
*High accuracy is not the same as low risk — because the errors are not random.*

---

Ninety-five percent accuracy sounds reassuring until you ask what the other five percent contains.

That is the question this chapter is about. Not whether AI lease abstraction works — it does, in the sense that it processes documents faster than a human reader and extracts standard clauses with high reliability on standard lease forms. The question is whether high accuracy on average tells you anything useful about the risk in a specific document. And the answer is: not as much as you'd think. Because the five percent that the tools miss is not randomly distributed across lease language. It concentrates in exactly the clause types where money hides. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

This is a specific claim, and it deserves a specific argument. So let's start with what accuracy actually means in this context, and then look at where it breaks down.

| document | what it says | what the AI abstract captured | what the abstract missed |
| --- | --- | --- | --- |
| base lease, second amendment (renewal notice window | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| CAM exhibit (operating expense exclusions | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| side letter (anchor departure rent relief | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| reader should see at a glance how a "mostly right" abstract diverges from the governing document stack | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## What Accuracy Means — and What It Doesn't

When a vendor says their lease abstraction tool achieves 95% accuracy, they are describing a ratio: the number of fields correctly extracted divided by the total number of fields, on the documents in their test set. That is a meaningful number. It is also a number you should handle carefully, because it depends on at least four things that the headline figure does not tell you. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

First, the test set. A tool trained and evaluated on standard NNNNN retail leases will perform differently on a ground-floor creative office lease in a mixed-use building with a custom operating expense schedule. The accuracy number is accurate for the documents the vendor tested. You need to know whether your documents resemble those documents. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

Second, the field definitions. A tool that counts "rent escalation clause present or absent" as one field will report higher accuracy than a tool that counts "escalation percentage," "CPI index reference," "floor rate," "cap rate," and "step-up dates" as five separate fields. Both tools might be described as having 95% accuracy. They are measuring different things. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

Third, the materiality threshold. Missing a notice address is not the same as missing a co-tenancy trigger. A summary accuracy figure treats all fields as equally important. Lease economics do not.

Fourth, absence versus presence. High accuracy on identifying clauses that exist is a different problem from correctly reporting that a clause does not exist. If a tool is trained on documents where renewal options are common, it will flag renewal options reliably. Verifying their absence — confirming that this specific lease genuinely has no renewal right — requires a different kind of check. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

Lextract and CAMAudit both document these distinctions in their current materials, and both are clear that accuracy is highest on standard clauses in standard lease forms and lower on unusual provisions, complex riders, and non-standard language. The vendors are not hiding this. The problem is that the headline accuracy figure travels faster than the qualifications. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

| what the headline figure says | what it depends on | what you need to know before relying on it |
| --- | --- | --- |
| test set composition, field definitions used, materiality weighting, absence verification | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| reader should be able to map any vendor claim against this framework | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## Where the Five Percent Lives

Now for the specific claim. The errors in AI lease abstraction are not random. They concentrate in five areas, and each one represents a category where a single missed clause can dominate the economics of a deal.

**CPI-linked escalations with floors and caps.** A rent escalation schedule is easy to identify. A CPI escalation with a 2% floor and a 4% cap, where the floor is defined in one section and the cap appears in an exhibit, and the CPI index reference was changed in the second amendment — that is harder. The tool may correctly identify that an escalation clause exists and miss the floor-and-cap structure that determines what the tenant actually pays at year five.

**Percentage rent breakpoints.** In retail leases, percentage rent provisions can represent significant additional income above base rent. The breakpoint calculation — the sales threshold above which percentage rent kicks in — may appear in the base lease, be modified in an addendum, and interact with an exclusion for certain tenant departments. The tools are good at finding percentage rent clauses. They are less reliable on the complete breakpoint mechanics.

**ROFO and ROFR rights.** Rights of first offer and rights of first refusal are transactional rights that can affect a deal's entire structure. They are also variable in their trigger conditions, notice windows, and exercise mechanics. A tool may correctly report that a ROFO exists. Whether the specific conditions in this lease allow the buyer to proceed on their intended terms requires reading the operative language.

**Co-tenancy provisions.** A co-tenancy clause gives a tenant the right to reduce rent, terminate, or seek other remedies if a defined co-tenant — often an anchor — vacates or fails to meet operating requirements. In retail and mixed-use properties, these provisions can be decisive. They are also written in highly variable language, with trigger conditions that can range from simple occupancy requirements to complex operating and retenanting obligations.

**CAM exclusions and caps.** Common area maintenance is often the largest variable in a tenant's occupancy cost, and lease documents frequently contain both inclusions and exclusions that are scattered across the base document, exhibits, and amendments. A tool may correctly capture the CAM recovery structure and miss an exhibit that excludes a category the underwriting model assumed was recoverable.

| clause type | why AI misses it | economic consequence of the miss | required verification action |
| --- | --- | --- | --- |
| CPI escalations with floors | caps, percentage rent breakpoints, ROFO | ROFR rights, co-tenancy provisions, CAM exclusions | caps |

The pattern across all five is the same: the clause is not a single field in a single location. It is a construct assembled from language in multiple places — the base document, exhibits, amendments, side letters — that has to be read together to be understood. The tool's accuracy on any individual piece may be high. The accuracy on the assembled meaning is where the risk lives.

---

## The Temporal Priority Problem

There is a deeper structural problem with AI lease abstraction that the accuracy statistics do not capture at all: a lease is rarely one document. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

A commercial lease in active use might consist of a base lease executed ten years ago, three amendments, an exhibit that defines operating expense terms by reference to a separate schedule, an assignment agreement, a landlord's consent letter that modifies assignment terms, and an estoppel certificate that the tenant signed two years ago and that may or may not reflect current conditions. Each document was executed at a different time by parties who may not have been thinking carefully about consistency with the other documents. The question that matters is not what each document says. It is which one governs now. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

This is the temporal priority problem. When two documents conflict — and in complex leases, they frequently do — the legal answer depends on the hierarchy of the documents, the governing clauses about amendment and modification, and sometimes on the specific language used in each version. An AI tool processing each document in isolation may produce an accurate extraction of each individual document and still fail to identify the conflict between them.

![Lease document stack ](images/07-lease-abstraction-the-95-that-hides-the-5-fig-01.png)
*Figure 7.1 — Lease document stack *

The opened-case scenario at the start of this chapter is this problem in a specific form. The abstract is accurate on the base lease. The second amendment changes the renewal notice window. The exhibit modifies CAM exclusions. The side letter grants rent relief on an anchor departure. Each of those documents might have been abstracted correctly in isolation. The failure is in reading them as a system, not as a collection of individual files.

The practical implication: any lease review workflow that treats the AI abstract as the final record of what the lease says is making a structural error. The abstract is a map of what the documents contain. It is not an answer to the question "what does this tenant's lease actually say?"

---

## Hallucination Is a Different Problem from Omission

Two failure modes matter in lease abstraction, and they require different responses. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

The first is omission: the tool misses a clause that exists. This is the failure mode most people think about. The tool did not find the co-tenancy trigger. The renewal option was in an exhibit and did not get extracted. These failures are serious, and the seven-item checklist at the end of this chapter is designed to catch them.

The second failure mode is more unsettling: the tool reports a clause that is not there. This is not the same as a random error. Language models trained on large numbers of commercial leases develop strong priors about what leases contain. Renewal options are common. CAM recovery is common. Percentage rent in retail is common. A tool with those priors may, on a lease that does not contain a renewal option, report a renewal option anyway — because the pattern matches documents that usually do. The technical name for this is hallucination. In lease abstraction, it means your abstract contains rights that the tenant does not have. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

The response to omission is verification of presence: find the clause the tool found and confirm it says what the tool says it says. The response to hallucination is verification of absence: confirm that the clause is genuinely not there, not just that the tool did not find it. These are different actions, and the second one is harder to build into a workflow because it requires the reviewer to go looking for something whose absence is the important fact. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

| failure type | what the tool does | risk to the deal | verification action required |
| --- | --- | --- | --- |
| omission (tool misses a clause that exists | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| hallucination (tool reports a clause that does not exist | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

The seven-item checklist addresses both. For each clause type on the list, the verification action covers both confirming that reported clauses are accurate and confirming that unreported clauses are genuinely absent. Both steps are required.

---

## The Seven-Item Checklist

There is a set of clause types where the failure-mode risk is high enough that AI abstraction output alone should never be the final record. For each of these, the verification step is a source-document check — not a check against the abstract, but a check against the underlying lease language itself.

The seven:

**Rent escalation.** Verify the full mechanics: base escalation schedule, CPI reference if applicable, any floor or cap on CPI-linked escalation, and step-up dates. Check amendments for modifications to any element.

**Renewal options.** Verify existence, number of options, option term length, notice window and notice requirements, rent determination at renewal, and any conditions precedent (no default, landlord consent). Verify absence if the abstract reports none.

**ROFO and ROFR rights.** Verify trigger conditions, notice window, exercise period, and the specific space or interest to which the right applies. Check whether the right runs to assignees. Verify absence if the abstract reports none.

**Co-tenancy provisions.** Verify trigger conditions, affected tenant and operating requirements, remedy structure (rent reduction, termination, other), cure period and retenanting obligations. This clause type varies more in language than almost any other in retail leases.

**CAM exclusions and caps.** Verify the full exclusion list, any cap on controllable expenses, the base year for expense comparison if relevant, and any exhibit-defined terms that modify the main lease CAM language.

**Exhibit-defined terms.** Identify which key economic terms — operating expenses, permitted use, building services, landlord work — are defined by reference to an exhibit rather than in the body of the lease. Verify that the exhibit is present in the data room and that the AI abstraction reflects the exhibit definition, not the body of the lease where the exhibit is referenced.

**Amendment priority.** Identify all amendments, confirm their execution dates and the order in which they govern, and verify whether any amendment contains a superseding provision that changes an earlier amendment or the base lease. This is the temporal priority problem in checklist form.

| clause type | what to verify (presence | mechanics) | where to look (base lease | amendments |
| --- | --- | --- | --- | --- |
| seven-item verification checklist — | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

![Checklist decision tree ](images/07-lease-abstraction-the-95-that-hides-the-5-fig-02.png)
*Figure 7.2 — Checklist decision tree *

This is not a comprehensive lease review. It is a targeted check on the clause types where AI abstraction is most likely to produce a confident-sounding output that is partially or materially wrong. The broker who runs this checklist on a complete document set, using source citations from the abstract to navigate, will catch most of what matters. The broker who uses the abstract as the record skips straight to the part where the missed clause surfaces in discovery.

---

## The Worked Example in Detail

A buyer is reviewing a retail center. The AI abstract for the anchor tenant's lease says CAM is recoverable, there is one renewal option at fair market rent, no ROFO, and no co-tenancy clause. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

The broker pulls up the abstract, notes the CAM section, and opens the cited source in the base lease. The base lease says CAM is recoverable, with standard exclusions. The broker then opens the third amendment — not cited in the abstract, because the amendment addresses a different primary topic — and finds a clause that caps controllable operating expenses at 3% annual increases and excludes capital expenditures for HVAC replacement from the recoverable pool. The underwriting model assumed full CAM recovery with no controllable expense cap. The amendment changes the number. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

The broker then checks the ROFO and co-tenancy fields. The abstract reports absence. The broker searches the document set — base lease, all three amendments, the assignment agreement — for "right of first" and "co-tenancy." The search returns nothing. The absence is confirmed.

The lesson is in the structure of that workflow: the abstract pointed the broker to the work. The amendment was the work. Without the abstract, the broker might have spent an hour finding the CAM section. Without the amendment check, the broker would have modeled the wrong number with confidence.

![Workflow diagram for the worked example ](images/07-lease-abstraction-the-95-that-hides-the-5-fig-03.png)
*Figure 7.3 — Workflow diagram for the worked example *

---

## What Would Change This Chapter

The chapter would need revision if independent benchmarks — not vendor test sets — demonstrated that AI abstraction tools reliably handle amendment priority, exhibit cross-references, absence verification, and materiality-weighted accuracy across messy, multi-document CRE lease stacks. That evidence does not currently exist at the level of specificity and independence required to change the core claim: that the seven-item checklist represents a necessary human step, not an optional quality control measure. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/07-lease-abstraction-the-95-that-hides-the-5-assertions.md -->

The tools are improving. The claim is that they are not yet at the point where the improvement eliminates the source-document check for material clause types.

---

## What This Chapter Adds

The book's argument is that AI belongs on the pattern-shaped work of CRE and that broker judgment belongs where accountability cannot be delegated. This chapter makes that argument precise for the specific case of lease abstraction: the pattern-shaped work is the extraction, and the accountability work is the interpretation of a document stack where temporal priority, exhibit cross-references, and hallucination risk are all in play simultaneously.

The next chapter expands the same logic from a single lease to a full data room.

---

## LLM Exercises

**Apply:** Take the seven-item checklist and apply it to one lease from your current or recent practice. For each item, document the source location you checked, what the abstract said, and whether the source confirmed or modified the abstract's output. Note specifically any item where the amendment stack changed the base lease representation.

**Analyze:** The chapter distinguishes omission from hallucination. Take a specific clause type — renewal options or co-tenancy — and describe what a verification workflow looks like for each failure mode separately. What does verifying presence look like? What does verifying absence look like? Why are they different actions?

**Create:** Draft a one-paragraph policy statement for your firm or team that specifies which of the seven clause types require source-document verification before an AI abstract can be used in a client-facing diligence memo. Frame it as a minimum standard, not a best practice.

## References

No references added by fact-check pass.

## AI and Errata Disclosure

Agentic AI was used to help gather data, check assertions, and prepare supporting references for this chapter. The material goes through multiple review steps, but mistakes can still occur. Errata, corrections, and suspected mistakes may be submitted through the publisher's website at https://www.humanitarians.ai.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the figures in this chapter. Each produces a standalone HTML file you can open in a browser and modify freely.

### Figure 7.1 — Lease document stack

```
Create a standalone D3 v7 HTML figure for "Lease document stack". Use a stacked taxonomy diagram with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 7.2 — Checklist decision tree

```
Create a standalone D3 v7 HTML figure for "Checklist decision tree". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes, arrow connectors, and direct labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 7.3 — Workflow for the worked example

```
Create a standalone D3 v7 HTML figure for "Workflow for the worked example". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes, arrow connectors, and direct labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```
