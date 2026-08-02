# Chapter 14 — Your AI Use Discipline: Writing the Document That Governs Your Tools

**One-line:** The AI Use Discipline document specifies what AI may do, what it may not do, and what you will check before accepting its output — and writing it is the most valuable hour you will spend this month.

## Chapter overview

This supplemental chapter turns the framework into a concrete artifact. It is meant to be read after Chapter 5 or after any single case study chapter. By the end of this chapter, you will have written — or be ready to write — a one-page document that governs your AI use with the same precision you would apply to any other professional specification. The chapter explains what the document contains, why writing it matters even if no one else ever reads it, and what it looks like in practice across six professional contexts.

## Learning objectives

- Write delegation scope, protection scope, and handoff conditions for your specific role.
- Translate AI governance logic into a personal workflow document that fits on one page.
- Understand when and how to update the document as tools and role demands change.
- Use the act of writing the document as a cognitive audit — the process of articulating the boundary is itself the value.

---

## Opening case

A brand strategist named Elena had been using AI tools for about a year when her agency was asked to present a post-mortem on a campaign that had gone wrong. The campaign had been drafted with AI assistance, reviewed at speed, and approved under deadline pressure. When the post-mortem committee asked who had verified the cultural appropriateness of the imagery for the target market, no one had a clear answer. The AI had generated the imagery options. Elena had selected one. But the decision — which concept worked for this audience in this moment — had happened without a named human owning it.

Elena had not been negligent. She had been working the way most professionals work with AI: case by case, prompt by prompt, deciding how far to let the tool go based on how good the output looked. That feels like flexibility. In retrospect, she understood it as ungoverned. The boundary between what the AI decided and what she decided had become invisible, and when the campaign failed, so had the accountability.

Six months later, Elena had a different practice. She kept a one-page document — she called it her AI Use Discipline — that specified what AI handled in her workflow, what she handled, what data she shared with AI tools, and what she verified before accepting AI output. The document was not for her agency. It was for herself. It took her ninety minutes to write and about twenty minutes a month to update. The most important thing it did, she said, was not prevent bad outcomes. It was make her think clearly about her work before the deadline pressure arrived.

---

## Core content

### 1. Why most AI governance fails the individual professional

Organizational AI governance frameworks are real and important. The NIST AI Risk Management Framework (2023) gives organizations a structured approach: govern, map, measure, manage. ISO/IEC 42001 (2023) defines an AI management system standard. The OECD AI Principles articulate accountability, transparency, and human-centered design. These frameworks exist because ungovemed AI deployment creates real risks — biased outputs, accountability gaps, privacy violations, and compounding errors.

But they are written for organizations. They assume legal teams, procurement processes, governance committees, and IT infrastructure. A mid-career professional working in a hybrid environment with a laptop and a handful of AI subscriptions cannot implement an enterprise governance framework. And most employers have not yet handed individual professionals a clear AI use policy that governs their specific role.

The result is that most individual professionals govern AI by intuition. They open a tool, try a prompt, evaluate the output, and decide in the moment how far to let the AI's contribution extend. That is not negligence — it is a rational response to the absence of explicit guidance. But it has a predictable failure mode: the boundary drifts outward without anyone noticing. The AI handles a little more, the professional verifies a little less, and the habits that built the domain expertise begin to atrophy.

Raji et al.'s 2020 work on closing the AI accountability gap makes the organizational case for documentation: without written specifications of what a system may do and what must be verified, accountability cannot be located when things go wrong. The same logic applies at the individual level. If you cannot point to a written decision about what AI may do in your work, you have not made that decision. You have let the tool make it by default.

### 2. What the document contains

The AI Use Discipline is a one-page document. It does not require technical knowledge of AI systems. It does not need to use the vocabulary of machine learning or governance frameworks. It needs to answer five questions clearly:

**What may AI do?** This is the delegation scope. Name the specific task categories where AI handles the work. Be specific enough that a new colleague reading the document would know exactly which tasks to route through AI tools and which to bring to you. "AI may draft initial client status updates from my approved notes" is specific. "AI may help with writing" is not a specification — it is a category.

**What may AI not do?** This is the protection scope. Name the task categories where human judgment is non-delegable. These are your Tier 4–7 tasks from the taxonomy: the decisions that require domain expertise to audit, the recommendations that carry professional accountability, the communications that reference specific client context that AI does not have access to. Be specific here too. "AI may not determine final pricing recommendations or client-specific risk assessments" is specific. "AI should not make important decisions" is not useful — every decision feels important in the moment.

**What data may be shared?** This is the data boundary. Name what categories of information may go into AI tools. Client names, financial data, confidential strategy documents, personally identifiable information — these categories often have legal, professional, or contractual implications that override your individual preference. If your employer has a policy, your document defers to it. If they do not, you need a default. The safest default: no confidential client data goes into any AI tool that is not specifically approved by your organization for that purpose.

**What must be checked before acceptance?** This is the handoff condition. For each major task category in your delegation scope, name the specific check you perform before accepting AI output into your workflow. Not "I review it" — that is not a condition, it is a gesture. A handoff condition is: "Before sending any AI-drafted client communication, I verify that it references this client's specific situation accurately, that no confidential data about other clients has contaminated the output, and that the recommendation language has been replaced by my own assessment." That is verifiable. You either did it or you did not.

**Who owns the final decision?** This is the accountability statement. Name yourself as the accountable party for every output that leaves your workflow. "All recommendations, assessments, and advice that reach clients carry my name and my professional accountability, regardless of how they were drafted." This single sentence is more important than it appears. It prevents the gradual drift toward treating AI output as the decision rather than the input to a decision.

### 3. Why writing the document is itself the cognitive audit

The chapters on the cognitive audit (Chapter 5) and the phase gate (Chapter 4) describe the boundary between AI and human work as something to specify, enforce, and maintain. The AI Use Discipline document is where that specification becomes concrete.

Here is what most professionals discover when they sit down to write the document: they do not know where the boundary is. They have been operating on intuition — letting the AI do what seems reasonable, pulling back when something feels off. When forced to name the boundary explicitly, they find that what "seems reasonable" has been expanding without deliberate review.

This is the cognitive audit built into the writing process. You cannot write "what AI may not do" without thinking carefully about where your professional judgment actually matters. You cannot write a meaningful handoff condition without thinking through what could go wrong if the AI's output is wrong. You cannot write the accountability statement without confronting the question of what, specifically, you are signing your name to.

Irene Solaiman's research on AI policy and responsible release [verify: confirm Solaiman's relevant work on AI documentation and governance] supports a broader point: documentation changes deployment behavior. When organizations write down what AI systems may do, the teams operating those systems make different choices. The same mechanism applies individually. When you write down your AI Use Discipline, you make different choices — before the tool is open, before the deadline pressure arrives, before the output looks good enough that reviewing it feels like unnecessary friction.

### 4. The technical version and the plain-English version

For technically oriented professionals — programmers especially — there is a direct analogue to the AI Use Discipline in technical practice. CLAUDE.md and AGENTS.md are persistent instruction files that set rules for AI coding assistants: what patterns to follow, what patterns to avoid, what the codebase conventions are, what the AI should not touch. Chapter 6 describes how a programmer's phase gate centers on writing the specification before opening the AI tool — the spec is the gate.

The CLAUDE.md format is powerful for technical workflows. It is tool-specific, precise, and machine-readable — the AI assistant actually reads the file and follows the instructions. For a professional whose primary AI interactions are with a coding assistant or a structured tool that accepts persistent instructions, writing a CLAUDE.md or equivalent is the best implementation of the AI Use Discipline concept.

For professionals whose AI use is less structured — a real estate agent using AI for property analysis, a designer using generative tools for variations, a brand marketer using AI for campaign drafts — a plain-English document is more appropriate. It does not need to be machine-readable. It needs to be human-readable and visible. Print it. Put it near your monitor. Read it when you open an AI tool and are about to do something that feels like it might be outside your specified delegation scope.

The format is not the point. The specification is.

### 5. Updating the document as the tools change

AI tools are changing faster than any governance framework can track. A capability that was outside the AI's frontier six months ago may be inside it today. A tool you used last year may have been replaced by something with different privacy defaults. A task you were protecting because AI was unreliable at it may now be ready for delegation.

The AI Use Discipline document should be reviewed monthly. The review should answer three questions:

Has the AI's capability in my delegation scope improved enough that my handoff conditions need to be stricter? As tools improve, the failure modes become more subtle. The errors are less obvious. Handoff conditions that caught obvious problems may not catch sophisticated errors. If the tool has improved, your verification needs to keep pace.

Has a task I have been protecting become reliably AI-assisted in my field? If so, does protecting it still build judgment, or has it become a form of inefficiency? Some tasks should stay protected forever — the Tier 7 decisions, the accountability-bearing recommendations, the client-specific advice. Other tasks were protected because the AI was unreliable, and as reliability improves, the protection is no longer serving its purpose.

Has my employer issued new guidance on AI tool use, data sharing, or client communication? Employer policy governs. If your employer has issued clearer guidance since you wrote the document, update your data boundary and delegation scope accordingly.

---

## Worked example: six versions of the same document

The following templates show what an AI Use Discipline looks like for professionals from the six industries covered in this book. Each follows the same structure: delegation scope, protection scope, data boundary, handoff conditions, accountability statement. Every version is specific — deliberately avoiding the generic language that makes governance documents useless.

---

**The Programmer**

*Delegation scope:* AI may generate boilerplate code, scaffolding, test stubs, and documentation from existing code. AI may suggest refactoring approaches and identify syntax errors. AI may draft commit messages and PR descriptions.

*Protection scope:* I write all architectural decisions and requirements specifications. I personally review all AI-generated code that handles user data, authentication, or external API integration. I own all debugging decisions in production systems. I write the specification before opening any AI code generation tool.

*Data boundary:* No production data, no client credentials, no unreleased product specifications in any AI tool not approved by the organization's security policy.

*Handoff condition:* AI-generated code is accepted into my workflow only when I can trace every function to a requirement in the spec I wrote. If I cannot trace it, I do not accept it until I understand it.

*Accountability statement:* All code that ships carries my professional review. I own what I merge.

---

**The Real Estate Professional**

*Delegation scope:* AI may generate comparable sales reports, listing descriptions, market trend summaries, and disclosure document first drafts. AI may draft standard client communications from my approved notes.

*Protection scope:* I personally own all client-specific advice, negotiation strategy, and final transaction recommendations. I conduct all client conversations about pricing, offer strategy, and whether to buy or sell. I evaluate all unusual market conditions using my direct knowledge of this market.

*Data boundary:* Client financial information, offer details, and transaction terms stay in approved internal systems only. Generic market data may go into AI tools.

*Handoff condition:* Before sharing any AI-generated analysis with a client, I must be able to explain in one sentence why the analysis is or is not applicable to this client's specific situation. If I cannot write that sentence, the analysis is not ready to share.

*Accountability statement:* All advice that reaches a client carries my name and my fiduciary responsibility.

---

**The Designer**

*Delegation scope:* AI may generate initial concept variations, mood board components, and format adaptations from my written brief. AI may handle asset resizing, presentation formatting, and stock image sourcing.

*Protection scope:* I write all briefs. I evaluate all generated options against the brief before showing anything to a client. I own all decisions about which direction to pursue and all explanations of why.

*Data boundary:* No client brand guidelines, unreleased campaign concepts, or confidential strategic direction in AI generation tools without client consent.

*Handoff condition:* Before presenting any AI-generated concept to a client, I must be able to explain in one sentence why this concept serves the brief — specifically, not generally. "It looks right" is not a handoff condition.

*Accountability statement:* Every concept I present to a client reflects my professional judgment about what serves their brief. The generation method is not the client's concern.

---

**The Small Business Owner**

*Delegation scope:* AI may draft routine client communications from my approved notes, prepare first-draft proposals based on prior approved work, generate social media content within established brand guidelines, and produce financial reporting summaries from approved data.

*Protection scope:* I personally handle all pricing conversations, all client relationship issues, all hiring decisions, and all strategic decisions about the business's direction. I review every AI-drafted communication before it is sent.

*Data boundary:* No client-specific financial data, contract terms, or personally identifiable information in any AI tool outside approved internal systems.

*Handoff condition:* Every AI-drafted client communication must include at least one sentence that references this client's specific situation — something AI could not have written without my input. If no such sentence exists, the communication is not ready to send.

*Accountability statement:* Every communication that leaves this business reflects my judgment. AI drafts. I send.

---

**The Brand Marketer**

*Delegation scope:* AI may generate copy variations within a completed brief, produce A/B test assets, draft campaign performance reports, and handle scheduling and distribution logistics.

*Protection scope:* I write all briefs. I own all brand strategy decisions, all decisions about what the brand will not do or say, and all decisions about cultural timing. I personally approve every campaign asset against a specific brief criterion.

*Data boundary:* No unreleased campaign strategy, no audience segmentation data beyond what is approved for the tool, no competitive intelligence in AI tools.

*Handoff condition:* Every AI-generated campaign asset is evaluated against one specific brief criterion before approval. "It looks good" is not a handoff condition. The criterion must be named in the brief.

*Accountability statement:* The brand outcomes of campaigns I manage are mine. The AI generates options. I make decisions.

---

**The Entrepreneur**

*Delegation scope:* AI may prototype features, generate pitch deck slides from my notes, produce financial model scaffolding, draft legal document first versions for attorney review, and summarize market research.

*Protection scope:* I own the problem formulation and the insight behind the company — the observation about the world that makes this product necessary. I personally conduct all early customer conversations. I make all strategic pivots.

*Data boundary:* No proprietary customer data, unreleased product roadmap, or investor-sensitive financial projections in AI tools outside approved internal systems.

*Handoff condition:* Before investing significant resources in any AI-assisted build direction, I must be able to state in one sentence why this specific company, at this specific moment, is better positioned than anyone else to solve this problem. If that statement is not compelling, the build is premature.

*Accountability statement:* This company exists because I am willing to be wrong in public and learn from it. AI is a tool. The accountability is mine.

---

## The blank template

Use this template to write your own AI Use Discipline. Keep it to one page. Be specific enough that someone else could follow it.

---

**My AI Use Discipline**
*Name / Role / Date*

**What AI may do (delegation scope):**
[List specific task categories. Be concrete — name the task, not the category.]

**What AI may not do (protection scope):**
[List the specific decisions, recommendations, and judgments that remain yours. Name them explicitly.]

**What data may be shared (data boundary):**
[Name the categories of information that may and may not go into AI tools. If your employer has a policy, reference it here.]

**What I check before accepting AI output (handoff conditions):**
[For each major task in your delegation scope, name the specific verification step. Not "I review it" — name what you check.]

**Who owns the final decision (accountability statement):**
[One sentence. Your name is on the output. Say so explicitly.]

*Review date: [one month from today]*

---

## What to do this week

Write your one-page AI Use Discipline using the template above. Do not aim for perfection — aim for specificity. A document with three specific handoff conditions is more valuable than a comprehensive document with ten vague ones.

After writing it, use it once before the end of the week. Open an AI tool, look at your discipline document first, and notice whether what you are about to do is inside your specified delegation scope. If it is not, either adjust your delegation scope deliberately or do the task without AI. Either is fine. The point is that the decision was yours.

Revise the document after that first use. One use will surface at least one place where your specification was too vague to be useful. Fix it. That revision is the practice.

---

## Bridge

The final chapter turns the document and the audit into a specific weekly sequence — the Monday-morning implementation plan for a professional who has read the book and needs to know what happens next.

---

## Key terms

- **Delegation scope:** The specific task categories where AI handles the work in your workflow. Must be specific enough that a new colleague reading the document would know which tasks to route through AI and which to bring to you.

- **Protection scope:** The specific decisions, recommendations, and judgments that remain non-delegable to AI. These are your Tier 4–7 tasks: the work that requires domain expertise to audit, that carries professional accountability, that is specific to this client or situation in a way that AI cannot replicate.

- **Handoff condition:** The specific, verifiable criterion that AI output must meet before you accept it into your workflow. Not a gesture toward review — a named check. If you cannot determine whether you did it, it is not a handoff condition.

- **Data boundary:** The explicit specification of what categories of information may and may not be shared with AI tools. Particularly important for confidential client data, personally identifiable information, and any information covered by professional privilege or contract.

- **Accountability statement:** The explicit declaration that you own the outputs that leave your workflow, regardless of how they were produced. The single most important sentence in the document because it prevents the drift toward treating AI output as the decision rather than the input to a decision.

---

## What would change my mind

I would revise this chapter if substantial evidence emerged that informal AI governance — no written boundaries, case-by-case judgment about what to delegate — produced comparable accountability, comparable error rates, and comparable protection against deskilling as explicit written governance. The human-factors research on automation bias, combined with the governance research on accountability gaps, suggests that informal governance fails systematically in ways written governance does not. If that evidence reversed, the case for the document would need to be rebuilt.

---

## Still puzzling

- Should the document use technical syntax (CLAUDE.md format) or plain English? The right answer probably depends on the reader's role, but there is an argument that technical professionals benefit from both — the plain-English version as a thinking tool, the technical version as the operationally active one.
- In a team setting, who reviews individual AI Use Discipline documents? There is a coordination problem: if every member of a team has a slightly different protection scope, the team's collective accountability boundary becomes unclear. This probably needs a team-level phase gate layer above the individual document.
- How often should the document change as AI capabilities improve? Monthly review is suggested, but the right interval may vary by field. In rapidly evolving fields like software and marketing, quarterly review may not be frequent enough.

---

## Sources used

- NIST, *AI Risk Management Framework 1.0* (2023). National Institute of Standards and Technology. Available at nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf
- ISO/IEC 42001:2023, *Information technology — Artificial intelligence — Management system.* International Organization for Standardization, 2023.
- OECD, *Recommendation of the Council on Artificial Intelligence* (OECD/LEGAL/0449). Organisation for Economic Co-operation and Development, 2019 (updated guidance ongoing).
- Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., ... & Barnes, P. (2020). "Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing." *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAccT)*. ACM.
- Solaiman, I. [verify: confirm specific Solaiman work on AI documentation and governance; relevant publications include work on release frameworks and responsible AI deployment]
