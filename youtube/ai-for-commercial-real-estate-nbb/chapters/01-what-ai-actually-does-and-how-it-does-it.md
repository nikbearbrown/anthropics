# Chapter 1 — What AI Actually Does (And How It Does It)
*The machine that learned to finish your sentences — and why that matters more than you think.*

![A single offering memorandum page with one clause](images/01-what-ai-actually-does-and-how-it-does-it-fig-01.png)
*Figure 1.1 — A single offering memorandum page with one clause*

There is a magic trick that always fools people the first time. You show them the trick, they applaud, you explain exactly how it works, and they applaud again — this time for the cleverness of the mechanism. The trick hasn't changed. Their relationship to it has.

That is what I want to do in this chapter. Show you the trick AI is performing, explain the mechanism precisely, and let you decide what to applaud and what to watch carefully.

Here is the trick: a broker drops an offering memorandum into an AI tool and gets back a summary that looks like a senior analyst wrote it. Eleven material points are right. The twelfth point is missing — a co-tenancy clause that changes the risk of the deal entirely. The tool produced something that looks like professional review. It is not professional review. The question worth asking is: what exactly did the tool do, and why did it produce something that looked so much like the real thing while missing the thing that mattered? [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

To answer that, we have to go back to a simpler version of the question. What is the AI actually doing?

---

## The thing the machine learned to do

Here is the simplest honest description I can give you: a large language model is a machine that learned to predict what comes next in a sequence of text, trained on an enormous amount of human writing, until it got very good at it.

That is not a metaphor or a simplification for a lay audience. That is the actual mechanism. The system looks at a context — everything written so far — and assigns probabilities to what might come next. It does this at the level of tokens, which are roughly word-pieces. The system samples from those probabilities and generates the next token, then uses that token as part of the new context, then generates another token, and so on. What you read as a fluent, coherent paragraph is the accumulated result of that process, thousands of tokens deep.

![Token-by-token generation visualized as a sequence ](images/01-what-ai-actually-does-and-how-it-does-it-fig-02.png)
*Figure 1.2 — Token-by-token generation visualized as a sequence *

![Attention lets the model look everywhere at once — weighted by relevance, not position.](images/01-what-ai-actually-does-and-how-it-does-it-fig-03.png)
*Figure 1.3 — Attention as a weighted web *

The architecture that made this work at scale is called the transformer, described by Vaswani and colleagues in 2017. Before the transformer, sequence models had trouble keeping track of relationships between words that were far apart in a sentence. The transformer introduced a mechanism called attention, which lets the model look at every position in the sequence and decide how much each position should influence every other position. The result is that a model can notice that a pronoun three sentences back refers to a specific noun much earlier, or that a contract clause at the bottom of page eight modifies a term defined at the top of page two. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

Attention is the thing worth understanding here, because it is what makes the summaries look so good. When the model reads your offering memorandum, it is not reading linearly the way a tired junior associate does at midnight. It is computing, for every word or phrase, a weighted relationship to every other word or phrase in the document. It finds patterns that match patterns it saw during training — the shape of a lease term, the structure of a renewal option, the signature of a parking provision — and it generates text that fits those patterns.

This is genuinely powerful. Do not undersell it. The pattern-matching is real, the retrieval is real, the generation is fluent and useful. When someone says AI cannot understand leases, they are making the opposite error from the broker in our opening case. The tool can save hours on summary, classification, and first-pass extraction. The question is not whether the tool works. The question is what kind of work it is doing.

---

## What the machine did not learn to do

Here is the part that people get wrong. Pattern-matching on a corpus of human text is not the same thing as materiality judgment. Those are different things. One is a learned statistical relationship between tokens. The other is a professional judgment about what changes the economics of a specific deal for a specific client in a specific market at a specific moment in time.

The co-tenancy clause in the opening case is not missing from the AI's summary because the model could not find it. It may well have found it — the clause is in the document. The clause is missing from the summary because materiality is not written into the text. Materiality is a judgment about consequences. It requires knowing that anchor-tenant occupancy can trigger rent relief, that rent relief changes the pro forma, that the changed pro forma changes whether your client closes the deal, and that your client is a specific person with a specific risk tolerance in a specific market where anchor tenants have been struggling. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

None of that is in the offering memorandum. None of it was in the training data in a form the model could apply to this document on this day for this client. The model produced a fluent, professional-looking summary of the patterns it found. It could not produce a judgment about which pattern, in this context, changes everything.

| Item | Meaning |
| --- | --- |
| Pattern-shaped work vs. judgment-shaped work | two columns. Left: extract, summarize, classify, draft, compare, format. Right: recommend, price, negotiate, disclose, sign, defend. Each row shows a CRE-specific example of each type. The visual should make the line feel crisp and meaningful, not arbitrary. |

This is the line. And the line is not about capability improving. The broker in the opening case is not waiting for a better model. She is waiting for a model that understands fiduciary responsibility, client-specific context, and professional accountability — none of which transfer to a statistical predictor, however sophisticated. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

---

## Why it looks so right when something is missing

There is a specific failure mode here that is worth naming precisely, because it is the one that bites professionals.

The AI output in the opening case does not look wrong. It looks competent. Eleven points are correct. The prose is fluent. The structure follows professional convention. The junior broker who says "it's 90 percent right" is observing something accurate. The question is what the missing ten percent is worth. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

What the model has done is produce output that is consistent with the pattern of a good summary. A good summary is fluent, organized, and covers the main points. The model has learned what good summaries look like. It generates output that looks like a good summary. But "looking like a good summary" and "being a correct professional assessment of this document" are not the same thing. The model is optimizing for the former. Your client is depending on the latter.

![Two side-by-side document excerpts ](images/01-what-ai-actually-does-and-how-it-does-it-fig-04.png)
*Figure 1.4 — Two side-by-side document excerpts *

This is not a flaw that will be fixed by a larger model or a better retrieval system. Retrieval-augmented generation — attaching the tool's outputs to source documents and checking citations — can reduce unsupported statements. It can tell you that a claim in the summary comes from page four of the document. What it cannot tell you is whether the clause on page seven changes the meaning of the clause on page four, because that judgment requires understanding consequences that are not written anywhere in the document. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

The mechanism is pattern completion. Pattern completion is excellent at finding what is there. It is not designed to find what is missing, or to assign professional significance to what it finds.

---

## The two-question test

Here is a practical way to think about any CRE task you are considering handing to an AI tool.

Question one: could a careful, well-trained assistant do the first pass by following examples and checking source documents? Not a lazy assistant — a careful one with good training. If the answer is yes, the task is probably pattern-shaped. Extraction, summarization, classification, drafting from precedent, comparison against a checklist — these are pattern-shaped. They benefit from the machine's speed and consistency.

Question two: would the correct answer change because of this client, this counterparty, this asset, this market moment, or your professional responsibility? If the answer is yes, the task is judgment-shaped. Recommendation, pricing, negotiation, disclosure, signing, defense — these are judgment-shaped. They belong to you. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

Many CRE tasks are mixed. A rent roll analysis is largely pattern-shaped — extract, calculate, compare — but the interpretation of what the numbers mean for this asset at this stage of its lifecycle is judgment-shaped. A lease abstract is largely pattern-shaped, but the assessment of which clauses are material to this transaction is judgment-shaped. The right category for most client-facing CRE work is what I would call delegate with review: use the machine for the pattern-shaped layer, then apply professional judgment to the judgment-shaped layer before anything reaches the client. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

![The two-question decision tree ](images/01-what-ai-actually-does-and-how-it-does-it-fig-05.png)
*Figure 1.5 — The two-question decision tree *

The opening case failed because the broker allowed the output to cross from first pass to client-facing recommendation without the review step. The tool did not fail. The workflow failed.

---

## The stack, from bottom to top

![The CRE data stack as a vertical diagram](images/01-what-ai-actually-does-and-how-it-does-it-fig-06.png)
*Figure 1.6 — The CRE data stack as a vertical diagram*

It helps to think about CRE work as a stack.

At the bottom is source data: leases, offering memoranda, rent rolls, trailing twelve-month financials, comparable sales, maps, notes, correspondence. This is the raw material of the practice.

Above that is extraction: pulling structured information out of unstructured documents. Which tenant, which rent, which term, which options, which clauses with economic consequences. This layer is where AI has made the biggest practical difference in the past several years. What used to take hours of careful document review can now take minutes. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

Above extraction is drafting and analysis: summaries for clients, emails for counterparties, market notes for investors, screening memos for acquisitions. This layer benefits substantially from AI assistance, with the caveat from the opening case: fluency is not accuracy, and pattern-matching is not materiality judgment.

At the top is professional judgment: what you recommend, what you sign, what you tell the client, and what you can defend if the deal goes wrong. This layer is yours. Not because the machine is incapable of producing text that sounds like a recommendation, but because the professional accountability for that recommendation cannot be delegated to a statistical system.

The stack matters because it makes the division of labor visible. The machine can climb the bottom two tiers quickly and well. It can help significantly on the third tier with appropriate review. The top tier is where your license, your judgment, and your relationship with the client live.

---

## The Westside problem

In the Los Angeles Westside market, the failure mode I described in the opening case takes a specific shape.

The AI summary looks excellent because the offering memorandum is well-formatted and the clauses follow standard patterns. The model has seen thousands of documents like it. The extraction is fast and largely accurate. The summary is fluent and professional. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

What the model has never seen is a Beverly Hills retail negotiation where the co-tenancy clause has practical meaning because of who is sitting across the table. It has not lived through a Culver City mixed-use repositioning where anchor occupancy patterns shifted faster than market assumptions could track. It has not absorbed what a West Hollywood tenant conversation actually sounds like when one clause is being contested by someone who knows exactly what it is worth. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

This is not a complaint about the technology. It is a description of where professional knowledge actually lives. Some of it is in documents. A lot of it is not. The model can only work with what is in documents, or what was in the training data, which is also documents. The tacit knowledge — the judgment about who is across the table, what the market will bear, what the client actually needs versus what they are asking for — is not in any document.

That is why the line between pattern-shaped and judgment-shaped work is not going to disappear as models improve. The models are getting better at documents. The judgment that matters most is not in documents.

---

## What this means for how you use the tool

Return to the opening case one more time. The broker gets a summary. Eleven points are right. The twelfth point is missing. Here is the process that should have happened:

First, identify the use of the document. Is this a first-pass screen, or is it going to a client? The answer changes what the review obligation is. For a first-pass screen, the machine's summary might be enough to decide whether to pursue. For anything client-facing, the review step is not optional.

Second, scan for clauses that change economics. Co-tenancy, kick-out, termination rights, rent escalations tied to conditions, CAM caps, assignment restrictions — these are the clauses that change what a deal is actually worth. The machine may have found them. It may not have. You need to check.

Third, compare the abstract to the source language. Do not trust a summary of a clause. Read the clause. The machine's paraphrase may miss a qualifier that changes everything.

Fourth, ask whether any omission changes the client recommendation. Not whether the omission changes the summary's accuracy score. Whether it changes what you would tell your client.

The machine does step one faster than you can. It does step two reasonably well on visible patterns. Steps three and four are yours.

| Step | What you're checking | Who does it | Why it matters |
| --- | --- | --- | --- |
| 1) Identify document use, (2) Scan for economic clauses, (3) Compare abstract to source, (4) Assess materiality for client. Should function as a practical checklist, not just a diagram. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | It makes the underlying reasoning visible instead of implied. |

---

## The common misconceptions, honestly examined

The first misconception is that professional tone means professional review. It does not. The opening case would fail this test at the client meeting, not at the summary stage — because the output looked competent while omitting the clause that changed the economics. Fluency is a signal the machine has learned well. It is not a signal that the output is correct.

The second misconception is that because AI does not truly "understand" leases, it is useless. This is the opposite error. The machine does not understand in the way a lawyer understands. But it can extract clauses, organize documents, and produce summaries faster and more consistently than a human doing the same mechanical work. Dismissing the tool because it lacks human understanding throws out genuine, substantial value.

The third misconception is the most seductive: that as models improve, the line between pattern-shaped and judgment-shaped work will disappear. Capability will improve. Models will handle more complex extraction, better cross-document reasoning, more nuanced drafting. The line will move. But fiduciary accountability does not transfer to the tool. When a deal goes wrong and your client wants to know what happened, the answer cannot be "the AI missed the co-tenancy clause." The accountability is yours. That is what the license is for. [unverified — needs source confirmation before publication]
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-what-ai-actually-does-and-how-it-does-it-assertions.md -->

---

## What you should be able to do now

By the end of this chapter, you should be able to look at any task in your practice and ask: is this pattern-shaped or judgment-shaped? If it is pattern-shaped, the machine can help — probably substantially. If it is judgment-shaped, the machine can produce text that looks helpful, and you need to evaluate it with that in mind.

The broker in the opening case did not need a better AI tool. She needed a clearer mental model of what the tool was doing — and a workflow that put professional judgment at the point in the process where it actually belonged.

That mental model is what this chapter was for.

---

## Bridge

Now that you understand the mechanism — prediction, pattern-matching, fluent generation without materiality judgment — the practical question becomes immediate: which tasks in your current practice should you delegate, which should you delegate with review, and which should you guard? That is the subject of the next chapter.

---

## LLM Exercises

**Apply:** Choose one active or recently completed transaction from your own practice. Classify each major task in that transaction as Delegate, Delegate with Review, or Guard. For any task you classify as Delegate with Review, write the specific review step — not a generic "check the AI output" but the exact thing you would check and why.

**Analyze:** Return to the opening case. The broker received a summary with eleven correct points and one missing point. Identify the exact step in the workflow where the failure occurred. Was it in the tool's output? The broker's review process? The workflow design? Write a paragraph explaining your reasoning.

**Create:** Design a one-page workflow rule for your own practice — or your team's practice — that would prevent the failure mode described in this chapter. The rule should specify: who runs the AI tool, what they check before passing output forward, what language is never allowed in client-facing materials without a source citation, and who signs off.

---

## Sources Used

- Vaswani et al., "Attention Is All You Need," 2017, NeurIPS.
- Brown et al., "Language Models are Few-Shot Learners," 2020, NeurIPS.
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," 2020, NeurIPS.
- Bender et al., "On the Dangers of Stochastic Parrots," 2021, FAccT.

## References

1. Vaswani, Ashish, et al. Attention Is All You Need. NeurIPS, 2017. https://arxiv.org/abs/1706.03762

## AI and Errata Disclosure

Agentic AI was used to help gather data, check assertions, and prepare supporting references for this chapter. The material goes through multiple review steps, but mistakes can still occur. Errata, corrections, and suspected mistakes may be submitted through the publisher's website at https://www.humanitarians.ai.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the figures in this chapter. Each produces a standalone HTML file you can open in a browser and modify freely.

### Figure 1.1 — A single offering memorandum page with one clause

```
Create a standalone D3 v7 HTML figure for "A single offering memorandum page with one clause". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 1.2 — Token-by-token generation visualized as a sequence

```
Create a standalone D3 v7 HTML figure for "Token-by-token generation visualized as a sequence". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes, arrow connectors, and direct labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 1.3 — Attention as a weighted web

```
Create a standalone D3 v7 HTML figure for "Attention as a weighted web". Use a horizontal bar chart with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 1.4 — Two side-by-side document excerpts

```
Create a standalone D3 v7 HTML figure for "Two side-by-side document excerpts". Use a two-panel comparison diagram with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 1.5 — The two-question decision tree

```
Create a standalone D3 v7 HTML figure for "The two-question decision tree". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes, arrow connectors, and direct labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```

### Figure 1.6 — The CRE data stack as a vertical

```
Create a standalone D3 v7 HTML figure for "The CRE data stack as a vertical". Use a stacked taxonomy diagram with 5 labeled categories with approximate values from 0 to 100. Marks: bars or rectangular panels, direct labels, and concise value labels. Channels: position for category or sequence, length for quantitative emphasis when bars are used, color for the primary highlighted item only. Use a zero baseline for quantitative bars. Preserve the chapter figure order and labels. Include role="img", aria-labelledby, title, desc, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Use the D3 7.9.0 CDN, inline CSS, and no external build step.
```
