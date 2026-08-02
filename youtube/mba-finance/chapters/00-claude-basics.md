# Chapter 00 — Claude Basics

**Suggested titles**
1. The Tool You're About to Use
2. Why This Book Has an AI Layer
3. Onboarding for the Modern Analyst

**TL;DR.** This book is about finance. It is also about a working way to do finance — using a large language model as a thinking partner, a sanity-checker, and a junior research assistant. This chapter explains the LLM layer: why it's there, what kinds of prompts you'll meet, how to use them well, where Claude fails on finance topics, and what the running equity research project will produce.

---

## The puzzle of the better-trained junior analyst

In 2026, a junior analyst at a sell-side investment bank doesn't write a research report alone.

They start by asking Claude to summarize the latest 10-K. They have Claude draft three competing scenarios for next year's revenue. They paste the firm's earnings transcript into a project and ask Claude to identify what management *stopped* talking about quarter-over-quarter. They build a DCF in a spreadsheet, then have Claude re-derive it from the assumptions to check for arithmetic errors. They draft the report, then have Claude critique it as a hostile-but-fair reader would.

None of this replaces the analytical thinking. The analyst still has to understand the firm, build the model, defend the price target, and stake their reputation on the conclusion. But the LLM layer changes how much of the routine work the analyst has to do alone, and changes the speed at which they can iterate.

A finance student in 2026 who learns finance without learning to use LLMs alongside it is half-trained. So is a student who uses LLMs as a substitute for understanding rather than as an amplifier.

This chapter is the onboarding for the LLM layer that runs through the rest of this book. By the end, you should know:

- Why finance students should learn to use LLMs.
- The two kinds of LLM prompts the book uses (Dig Deeper and LLM Exercises) and how each fits.
- The mechanics of using Claude (and adapting to other LLMs).
- Where Claude is reliable on finance topics and where it isn't.
- What you'll be building, week by week, as the equity research project.

For students using a different LLM (ChatGPT, Gemini, others), the prompts in this book mostly transfer. We'll note adaptations where they matter. The framework is universal; the specific tool used to apply it is your choice.

---

## Learning objectives

After working through this chapter, you should be able to:

- Articulate three things LLMs are reliably useful for in finance work.
- Distinguish a Dig Deeper prompt from an LLM Exercise.
- Use Claude across its main interfaces (chat, Project, Code, Cowork) and choose the right one for the task.
- Identify three failure modes of LLMs on financial questions.
- Set up your running project: pick a public company, build a Claude Project, draft a one-page company snapshot.

**Prerequisites.** None. This is the book's onboarding chapter.

---

## Concept 1 — Why this book uses LLMs

Three honest reasons.

### Reason 1 — LLMs are genuinely useful for some kinds of finance work

There are specific tasks where Claude (and competitor LLMs) reliably help:

- **Summarizing long documents.** A 10-K runs 100-300 pages. An LLM can produce a structured summary in seconds. The summary won't replace your reading the original, but it tells you where to focus.
- **Translating jargon into plain English.** "Asset-liability mismatch" or "duration gap" can be re-explained in everyday terms. Useful for first-pass understanding and for sanity-checking your own explanations.
- **Drafting structured analyses.** "Compare these three companies on the following dimensions" produces a usable table in seconds. You verify, you refine, you publish.
- **Sanity-checking calculations.** Build a DCF in a spreadsheet. Paste it into Claude. Ask it to find arithmetic errors. It often does.
- **Brainstorming alternative scenarios.** "What could go wrong with my revenue forecast?" produces a list of plausible risks. You filter for relevance.
- **Drafting first versions of emails, memos, reports.** The first draft is the hardest part. LLMs make first drafts trivially fast. Your editing is what matters.

These are real gains in productivity for the kinds of writing-heavy tasks that occupy most of a junior analyst's day. None of them replace the analytical work that actually creates value; all of them speed up the surrounding work that doesn't.

### Reason 2 — LLMs fail badly on certain finance tasks

There are also tasks where Claude is unreliable or actively wrong:

- **Numerical precision.** LLMs produce wrong arithmetic regularly, especially for multi-step calculations. Always re-derive numbers in a spreadsheet and check.
- **Recent data.** Claude's training data has a cutoff date. Asking for "the current Treasury yield" or "Apple's latest earnings" may produce stale or wrong answers. Always verify against primary sources (FRED, EDGAR, the firm's IR site).
- **Specific citations.** LLMs sometimes invent plausible-looking sources. "According to the Journal of Finance, 1987..." may or may not refer to a real paper. Always check citations before quoting them.
- **Confident wrongness on technical edge cases.** Multi-stage DDM with non-standard cash flow patterns, intermediate-bond mathematics, derivatives pricing edge cases — LLMs often produce plausible-sounding answers that are subtly wrong. Verify the math.
- **Future predictions.** LLMs cannot predict markets, interest rates, or specific firm performance. Treat any "forecast" the LLM produces as a hypothesis to test, not as analysis to rely on.

The right posture: **curious, skeptical, iterative.** Ask the LLM. Read the answer with attention. Verify the parts that matter. Iterate when something is off.

### Reason 3 — Learning to work with LLMs is the actual job market

The work life of a 2025+ junior analyst includes daily LLM use. Firms expect new hires to bring this skill. A graduate who can't use LLMs to amplify their analytical work is at a competitive disadvantage that grows over time.

This isn't a bet on a specific company or specific tool. Claude, ChatGPT, and Gemini all do roughly equivalent work for finance students; the underlying skill is in knowing how to *use* an LLM well, regardless of which one is in front of you. The book uses Claude as the primary tool because the prompts and workflows we've designed work cleanly with it; small adaptations make them work elsewhere.

↳ **Dig Deeper — Prompt engineering for finance work**

*The same finance question can produce dramatically different LLM outputs depending on how you phrase the prompt. Effective prompts for finance work follow patterns that aren't immediately obvious — role specification, structured output requests, explicit reasoning steps, and verification framing all matter.*

**Prompt:**
> Compare the quality of LLM responses to these three versions of the same question, and explain why the third typically produces better output:
>
> Version 1: "Tell me about Apple's financial health."
> Version 2: "You are an experienced equity analyst. Based on Apple's most recent 10-K, analyze its financial health."
> Version 3: "You are an experienced equity analyst. Based on Apple's most recent 10-K (uploaded), analyze its financial health by computing: (1) current ratio, (2) debt-to-equity, (3) free cash flow conversion, (4) ROIC. Cite the specific 10-K page or footnote for each input. Where data is unclear, say so rather than estimating. Format as a structured report."
>
> What general principles for prompt-writing in finance work do you extract?

**What to do with the output:** Save it. Apply the principles to every LLM Exercise in subsequent chapters; better prompts produce dramatically better outputs.

### The trade-off (concept 1)

Using LLMs in finance trades **speed-of-iteration against verification overhead**. The first draft is faster. The verification adds time. For routine tasks, the trade is favorable. For high-stakes calculations, the verification is the work, and the LLM just made the first version available faster.

### Common misconceptions

- *"LLMs are calculators."* They aren't. They produce text. Sometimes the text contains correct arithmetic; sometimes not.
- *"LLMs replace junior analysts."* They make junior analysts more productive. The hiring shift is toward analysts who can *use* the tools, not toward replacing them.

---

## Concept 2 — The two prompt types in this book

Throughout the chapters, you'll encounter two distinct kinds of LLM prompts. They serve different purposes.

### Type 1: Dig Deeper prompts (inline, optional)

These are scattered through the chapters. Format:

```
↳ Dig Deeper — [Concept name]

[One-line motivation: what this explores and why it rewards a detour.]

Prompt:
> [The actual copy-paste-ready prompt, 2-5 sentences.]

What to do with the output: [What to read it for.]
```

**Purpose:** Optional rabbit holes for curious learners. When a concept catches your attention and you want to go further than the chapter goes, the Dig Deeper prompt gives you a head start.

**They produce no deliverables for the running project.** Skipping them costs nothing. Some chapters have 4 of them; some have 2. They're invitations, not assignments.

A typical Dig Deeper prompt might say: *"Here's the chapter's discussion of WACC. Write me a follow-up explanation of why investment-grade bond yields are a good starting point for cost-of-debt estimation, and three real-world cases where they aren't."*

You read the output, learn something, move on. Or you don't read it at all, and you still understand the chapter.

### Type 2: LLM Exercises (chapter-end, project-driven)

These are at the end of every chapter, with this format:

```
LLM Exercise — Chapter [N]: [Title]

Project: Equity Research Report on a Chosen Public Company
What you're building this chapter: [One sentence.]
Tool: [Recommended tool.]

The Prompt:
[Full copy-paste-ready prompt, designed to advance the running project.]

What this produces: [Concrete description.]
How to adapt this prompt: [Domain-specific variations.]
Connection to previous chapters: [How this builds on prior work.]
Preview of next chapter: [What's coming.]
```

**Purpose:** These advance the **running project** — the equity research report you'll build over the course of the book. By the time you finish Chapter 20, the LLM Exercises will have produced (with your editing and judgment) a complete equity research report on the company you choose.

**They are designed to be done in sequence.** Each exercise builds on the prior chapter's output. By Chapter 11, your DCF model has the cash flows from Chapter 5's 10-K reading and the discount rate from Chapter 14's beta computation. The compound effect across 20 exercises is substantial.

**Adaptation matters.** The prompts are written generically. You replace the placeholders with your company name, your data, your context. The book's author wrote the prompts; you make them yours.

### When to do which

Both types are recommended. The breakdown:

- **Dig Deeper**: pursue when curious. Skip when not.
- **LLM Exercises**: do every one if you're following the project. Each one delivers a chunk of the final report.

If you're using the book without doing the running project, the LLM Exercises are still useful as standalone analytical exercises — they just won't accumulate into the report.

### The trade-off (concept 2)

Two prompt types trade **breadth (Dig Deeper covers more ground) against depth (LLM Exercises produce a complete deliverable)**. A reader who skips Dig Deepers but does every LLM Exercise gets the complete project; a reader who does every Dig Deeper but skips Exercises gets broad understanding but no artifact at the end. Most learners benefit from both, but the project arc requires the Exercises.

### Common misconceptions

- *"Dig Deeper prompts are required."* They aren't. They're entirely optional.
- *"The LLM Exercise produces the final report by itself."* No — it produces *one piece* of it. The synthesis at the end is your work.

---

## Concept 3 — How to use Claude well

Three operational topics: which Claude interface to use, how to recover from bad outputs, and where Claude's limitations show up most often.

### Choosing the right interface

Claude offers several entry points. Pick by task.

**Claude Chat** (claude.ai) — the standard interface. Best for one-off questions, single-document analysis, conversational thinking. Use when each task is independent.

**Claude Projects** — the interface for ongoing work. Upload reference documents (10-Ks, prior analyses, your DCF spreadsheet) once, then reference them across multiple conversations. Best for the running equity research project: upload your company's recent 10-Ks and proxy statements, then ask questions across chapters that all draw on the same context.

**Claude Code** — for software engineering tasks. Less directly relevant to most finance work, but useful for the regression analyses in Chapter 14 (writing actual Python code to compute beta) and the more complex spreadsheet logic in Chapters 18-19.

**Cowork** (within Claude Code) — for multi-step automation involving file manipulation, web fetches, and shell commands. Useful if you're building reproducible workflows; less commonly needed for a one-time research project.

For the running project, **Claude Projects is the recommended primary interface.** Upload your company's 10-K and 10-Q. Drop in your prior chapter outputs as you go. Each LLM Exercise in subsequent chapters can reference what you've built so far.

### Adapting prompts to other LLMs

The prompts in this book work in Claude. Most also work in ChatGPT, Gemini, and similar models with minor adjustments:

- **Replace "Claude Project"** with "ChatGPT Custom GPT" or "Gemini Gem" if using alternatives.
- **The phrasing of prompts** is universal — "Summarize the risk factors section in 200 words" works equivalently in all major LLMs.
- **Quality of output varies** by model. ChatGPT is comparable for most finance tasks. Gemini is comparable for many. For specific tasks (long-context analysis, code review), one may outperform another.

For the project, you can swap any LLM for Claude with very minor adjustments. The structure of the prompts and the workflow are what matter.

### When Claude's output is wrong or thin

Common failure modes and the fixes:

**Failure 1: arithmetic error.** Claude says "the present value is $48,372" but the correct answer is $42,189.
- *Fix*: don't take any number from Claude as authoritative. Re-derive in a spreadsheet. Use Claude's number only as a starting point.

**Failure 2: invented citation.** Claude says "according to Smith (2019)..." and the paper doesn't exist.
- *Fix*: never quote a citation Claude provides without verifying it. If the citation is to a real journal article, search Google Scholar to confirm.

**Failure 3: stale data.** Claude says "the 10-year Treasury yields 1.5%" when the current rate is 4.5%.
- *Fix*: don't ask Claude for current data. Get current data from FRED, EDGAR, or the firm's IR site, then ask Claude to analyze it.

**Failure 4: confident bullshit.** Claude produces a plausible-sounding but subtly wrong analysis. Most common with multi-step technical questions.
- *Fix*: cross-check the analysis against a textbook or another source. Test the prediction against a worked example.

**Failure 5: thin output.** Claude gives you three obvious points when you wanted six insightful ones.
- *Fix*: iterate. Try a more specific prompt: "give me three more, each focused on a different aspect of the firm's competitive position." Or change the framing: "as an experienced equity analyst skeptical of management's optimistic guidance, what would you challenge in this MD&A?"

The general principle: **iterate.** Claude's first response is often a draft, not an answer. The second prompt — refining, challenging, or extending the first — is where the value is.

### Carrying outputs forward

For the running project, the LLM Exercises accumulate. Best practice for managing the accumulation:

1. **One Claude Project per company.** Upload reference documents once.
2. **Save each exercise's output** in a Word doc or Markdown file. Review and edit it before moving on.
3. **Reference prior outputs in subsequent prompts.** Example for Chapter 6: "Using the company's 10-K I uploaded earlier, and my preliminary financial-statement summary I'm including below, compute the following ratios..."
4. **Refine as you go.** Your understanding deepens. Earlier outputs may need updating in light of later analysis.

By Chapter 20, you should have 20 chapter outputs (plus this Chapter 00 setup) that synthesize into the equity research report.

### Worked example — the Chapter 1 LLM Exercise, walked through

To make the prompt-iteration process concrete, here's how you might do the Chapter 1 LLM Exercise (which we'll formally introduce in Chapter 1).

The prompt asks: *"For your chosen public company, identify and explain the three business-finance decisions (working capital, capital budgeting, capital structure). Where on the balance sheet does each live?"*

**First-iteration prompt (paste into Claude Project after uploading the 10-K):**

> Based on Apple's most recent 10-K (uploaded), identify Apple's three business-finance decisions:
> 1. A working capital decision (relating to short-term assets/liabilities)
> 2. A capital budgeting decision (relating to long-term investment)
> 3. A capital structure decision (relating to long-term debt and equity)
>
> For each, name the specific balance sheet line item it affects, the dollar magnitude (from the most recent fiscal year), and one paragraph explaining what the decision implies for Apple's strategy.

**Strong response would include:**
- Working capital: changes in inventory or accounts payable management, with current asset/liability line items and dollar amounts.
- Capital budgeting: a recent capex disclosure (e.g., the 2024 chip-design investments), magnitude, and strategic context.
- Capital structure: the firm's debt issuance and stock-buyback program, with specific recent transactions and amounts.

**Weak response:** Generic statements about "Apple invests in research and development" without specifics. If you get this, follow up: "Be more specific. Reference exact line items from the 10-K and exact dollar amounts. Cite the relevant page or footnote where possible."

The iteration is what produces useful output. The first prompt produces a starting point; the second prompt refines.

### Claude's limitations in the finance context

Beyond the general failure modes above, three specific finance-relevant limitations:

**1. Beta and statistical estimates.** Claude can describe how to compute beta but cannot reliably compute it from raw return data without you running the regression in Excel/Python and pasting the result. Treat Claude's "this stock has beta 1.2" claims as invented unless you verified the regression.

**2. Specific firm details.** Claude's information about specific companies may be stale or partially wrong. Always verify firm-specific facts against the firm's most recent filings.

**3. Confident financial advice.** Claude isn't a financial advisor and shouldn't be treated as one. For personal investment decisions, the project framework is analytical training; actual advice for actual money requires actual professionals.

### Quick-reference card

A compact summary you can return to:

| Prompt type | When to use it | What it produces | Recommended tool |
|---|---|---|---|
| Dig Deeper | When a concept catches your attention | Optional deeper exploration | Claude chat |
| LLM Exercise | At the end of each chapter | One section of the running project | Claude Project |
| Sanity-check calculation | After building a spreadsheet | Verification of arithmetic | Claude chat |
| Document summary | Before reading a long document | Where to focus | Claude Project |
| Memo first draft | When you've done the analysis | Editable starting text | Claude chat |
| Brainstorm risks/scenarios | During analytical thinking | Hypotheses to test | Claude chat |

For verifying numbers and recent data, **don't use Claude.** Use FRED for macro data, EDGAR for company filings, the firm's IR website for current disclosures.

↳ **Dig Deeper — When NOT to use an LLM**

*The book argues for using LLMs as analytical amplifiers. But there are specific finance tasks where LLMs are actively dangerous — situations where their failure modes are most likely to mislead you. Knowing these is part of using the tool well.*

**Prompt:**
> Identify five specific finance tasks where you should NOT rely on LLM output, even with verification:
> (1) computing precise present values for high-stakes decisions,
> (2) generating specific firm-level statistics or recent data,
> (3) generating citations to academic literature,
> (4) producing legal or regulatory advice,
> (5) any task where speed-to-rough-answer is worth less than care-and-precision.
>
> For each, explain the specific failure mode and what alternative approach is appropriate.

**What to do with the output:** Save it. The discipline of knowing when to NOT use the LLM is at least as valuable as knowing when to use it.

### The trade-off (concept 3)

Working with Claude trades **speed of first-draft against verification overhead**. The faster you can iterate, the more analytical depth you can produce per hour. The more you trust unverified Claude output, the more wrong analyses you ship. The right balance: iterate fast on Claude, verify on every important number.

### Common misconceptions

- *"If Claude said it, it must be right."* No. Claude is sometimes confidently wrong. Verify.
- *"I should use Claude for everything."* No. Some tasks (current data, precise math, financial advice) are better served by other tools or human professionals.

---

## Synthesis — what this book is asking of you

This book is not "how to use Claude" — it's "principles of finance, with Claude as a working tool." The finance is what you're learning. Claude is the tool you're learning to use *while* learning the finance.

By the end of the book, you should be able to:

1. Read a 10-K and tell what the firm is doing financially.
2. Build a DCF model and compute a defensible price target.
3. Use Claude as a research assistant: summarize, sanity-check, draft, iterate.
4. Distinguish what Claude can reliably do from what it can't.
5. Produce a complete equity research report on a public company of your choice.

For the running project, the deliverable from this chapter is concrete:

1. **Pick a public company.** It should be a firm whose business you find interesting — you'll work on it for the rest of the book.
2. **Set up a Claude Project.** Name it for your company.
3. **Upload the most recent 10-K and most recent two 10-Qs** from EDGAR (sec.gov/edgar).
4. **Draft a one-page company snapshot.** Use the prompt below.

The snapshot becomes the executive summary of your final equity research report. You'll revise it many times.

---

## LLM Exercise — Chapter 00: Pick Your Company

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** Your project's foundation — company selection, Claude Project setup, one-page snapshot.
**Tool:** Claude Project (for ongoing context across chapters).

### The Prompt

```
I am beginning an equity research project on [your chosen company, ticker]. I have uploaded their most recent 10-K to this Claude Project.

Please produce a one-page company snapshot covering:

1. **Business overview** — What the company does, its main products/services, and how it makes money (2-3 sentences).
2. **Industry context** — The industry/sector, the firm's main competitors, and the firm's approximate market position (2-3 sentences).
3. **Financial scale** — Most recent fiscal year revenue, operating income, net income, total assets, market capitalization (a small table with one column of values).
4. **Major strategic themes** — Three things from the 10-K's MD&A that suggest where the company is going (3 short bullet points).
5. **Key risks** — Three risks from the 10-K's risk-factor section that I should track throughout my analysis (3 short bullet points).

Cite specific pages or sections of the 10-K where possible. Don't invent figures or claims; if something is unclear from the 10-K, say so explicitly.
```

### What this produces

A one-page document that becomes the first page of your equity research report. You'll revise it as you do more work in subsequent chapters, but the core elements (business, industry, scale, strategy, risks) stay roughly stable.

### How to adapt this prompt

- *For your own company:* Replace [your chosen company, ticker] with the actual name and ticker (e.g., "Apple, AAPL").
- *For ChatGPT or Gemini:* Works identically. Replace "Claude Project" with "Custom GPT" or "Gemini Gem" in the setup, but the prompt itself transfers.
- *For Claude Code:* Less appropriate for this exercise; Claude chat or Project is better suited.

### Connection to previous chapters

This is Chapter 00. There are no previous chapters.

### Preview of next chapter

Chapter 1 introduces the field of finance — the three areas, the central trade-off, the three business-finance decisions. The Chapter 1 LLM Exercise will ask you to identify the three business-finance decisions for your chosen company.

---

## Exercises

### Warm-up

**0.1** Name three things LLMs are reliably useful for in finance work, and three failure modes.

**0.2** Distinguish a Dig Deeper prompt from an LLM Exercise.

**0.3** When should you use Claude Projects rather than Claude chat?

### Application

**0.4** Pick a public company. Justify your choice in two sentences (why this company, why this industry).

**0.5** Set up a Claude Project for your chosen company. Upload the most recent 10-K and 10-Q from EDGAR.

**0.6** Run the Chapter 00 LLM Exercise above. Save the output as your project's first deliverable.

### Synthesis

**0.7** A friend says: "Using LLMs to write reports is just cheating. The student doesn't really learn the material." Construct a counter-argument that addresses (a) what LLMs do that doesn't replace learning, (b) where they amplify learning, and (c) where the friend's concern is genuinely valid.

---

## Chapter summary

- LLMs (Claude, ChatGPT, Gemini, others) are useful for summarizing, drafting, sanity-checking, and brainstorming. They are unreliable for precise math, current data, and specific citations.
- The book has two prompt types: **Dig Deeper** (inline, optional, exploratory) and **LLM Exercise** (chapter-end, project-driven).
- The running project is an **equity research report** on a public company you choose. By Chapter 20, the LLM Exercises produce the report's content; your editing and judgment shape the result.
- **Claude Projects** is the recommended primary interface for the project (one project per company, with reference documents uploaded once).
- Verify numbers and current data outside Claude (FRED, EDGAR, IR sites). Iterate when output is thin.
- The book's question is not "how to use AI" — it's "how to do finance well, with AI as a tool."

---

## What would change my mind

The chapter argues that learning finance with LLMs is more useful than learning it without. The reading would have to revise if (a) LLMs proved consistently misleading on finance topics across all major tasks (they don't — they're reliable on some, unreliable on others, and the reliability is roughly predictable), or (b) firms moved away from LLM-augmented analyst workflows (they've moved toward them; the trend is durable).

## Still puzzling

The cleanest unresolved question is *whether students who use LLMs heavily understand the underlying finance as deeply as students who don't*. The empirical research is early. My current view: students who use LLMs *as amplifiers* (do the analysis themselves, then iterate with the LLM) deepen their understanding faster. Students who use LLMs *as substitutes* (have the LLM do the analysis and read the output) understand less. The book's framing is for the first kind. The second kind doesn't get the value the chapters are designed to deliver.

---

## Connections forward

- **Chapter 1** introduces the field of finance and the three business-finance decisions.
- All subsequent chapters include LLM Exercises that build on this chapter's setup.
- By **Chapter 20**, the LLM Exercises will have produced a complete equity research report on your chosen company.

---

**Tags:** Claude, LLM-fundamentals, equity-research-project, prompt-engineering, AI-in-finance


---

##  AI Wayback Machine

![Fischer Black](../images/fischer-black-4o2.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Fischer Black, and how does their work connect to finance with tools we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Fischer Black"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Fischer Black's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Fischer Black's framework."

What changes? What gets better? What gets worse?
