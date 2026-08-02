# Chapter 2 — Corporate Structure and Governance

*What the legal fiction buys you, and what it costs.*

---

Here is a puzzle. In 2001, the seventh-largest company in the United States — a firm with reported revenues over $100 billion, 20,000 employees, a board of independent directors, an outside auditor that had been in business for ninety years, and millions of shareholders who were, in some legal sense, its *owners* — went bankrupt. The stock fell from $90 to under $1. The pension accounts of the people who worked there, concentrated in company stock, were obliterated. The CEO went to prison.

The company was Enron.

Now here is the question that matters for this book: **how does that happen?** Not the accounting details — those come later. The structural question. The company had owners. The owners had hired managers to run their property. The managers destroyed the property. How is that even possible?

The answer is: because of what a corporation *is*. The same legal invention that let millions of strangers pool capital to build a 20,000-person company also let a small group of insiders do enormous damage before any of those strangers noticed. The corporate form is a remarkable tool. Like most remarkable tools, it cuts in more than one direction.

This chapter is about the tool — what it does, what it costs, and how the law tries to manage the cost.

---

## The legal fiction and what it buys

When you and a friend open a coffee shop, the first question your lawyer asks is what *legal form* the business takes. There are four general answers.

**Sole proprietorship.** You are the business. No legal separation. To start one, you basically just start doing business — file a tax form at year-end and you're running. The advantages are real: no separate entity to maintain, no corporate income tax, no board of directors, no governance overhead. You make every decision. Total control.

The disadvantage is also total. You have **unlimited personal liability.** Your business debts are your personal debts. If a customer wins a $500,000 judgment against your coffee shop and your insurance doesn't cover it, your house is in the pile. And if you die or quit, the business ends with you — it has no life separate from yours.

**Partnership.** Two or more people, same basic structure. Now you also have each other's liability. If your partner defrauds a client, you are on the hook for the judgment your partner can't pay. Law firms used to be general partnerships, and occasionally one partner's misconduct propagated through the firm like a fire through dry timber.

<!-- → [IMAGE: simple diagram showing liability flowing from business debts to personal assets in a sole proprietorship vs. stopping at the corporate entity in a corporation — visual of the "liability shield"] -->

**Corporation.** A legal entity *separate from its owners.* Created by filing articles of incorporation with a state (usually Delaware, which has spent 150 years building a legal infrastructure specifically for this purpose). Once incorporated, the corporation can sign contracts, sue and be sued, own property, hire employees, and raise capital — all in its own name, legally distinct from any individual who owns shares in it.

Three things follow from this separation, and they are worth taking seriously because they are not obvious.

**Limited liability.** Shareholders can lose what they invested. They cannot lose more. If the company goes bankrupt with $1 billion in unpaid debts, the creditors cannot come after the shareholders' houses. This sounds simple. Its consequences are enormous. Without limited liability, no rational person would buy a small fraction of a company run by strangers. The moment you buy a share of Apple, you are partnering with millions of people you have never met, trusting managers you did not hire, in a business you cannot supervise. You would never do that if you could be held personally liable for the company's mistakes. Limited liability is what makes public ownership *possible* — it caps the downside to exactly the amount you paid for the shares.

**Unlimited life.** The corporation persists when owners come and go. Founders die. Shareholders sell. Executives retire. The entity continues. Apple was incorporated in 1977 and has now outlived two of its three co-founders.

**Transferable ownership.** Shares can be sold, given, or inherited without disrupting the firm. In a partnership, when a partner leaves, the partnership has to be legally reformed. In a corporation, when a shareholder sells, nothing inside the firm changes. The new shareholder simply appears where the old one was on the ownership records.

These three features, together, are what lets a corporation raise capital at scale from strangers who are not equipped to run the business. That is the whole point of the corporate form.

**The cost: double taxation.** The corporation pays income tax on its profits. When it distributes those after-tax profits to shareholders as dividends, the shareholders pay income tax again. Two bites from the same apple. This is the price of legal separation.

<!-- → [TABLE: four-column comparison of sole proprietorship, partnership, corporation, LLC/LLP across: liability protection, taxation, capital access, administrative complexity] -->

**Hybrids.** The 1990s produced legal forms that try to capture the corporation's limited liability while keeping the partnership's pass-through taxation. A **limited liability company (LLC)** has owners called members who enjoy limited liability; the LLC itself pays no entity-level tax. The LLC has become the default form for new small businesses. Amazon's retail operation is structured as an LLC (Amazon.com Services LLC), even though Amazon.com Inc. is a publicly traded C corporation — large firms run hybrid structures inside themselves.

**C corporation vs. S corporation.** The standard corporation, called a **C corporation**, faces the double-tax. The tax code offers an alternative — the **S corporation** — for closely held firms, where income passes through to shareholders' personal returns. The catch is eligibility: an S corp cannot have more than 100 shareholders, cannot issue more than one class of stock, and cannot accept investment from institutional funds that are themselves required by their own governing documents to hold only C-corp shares. The standard arc for a growing technology firm is: LLC while small, S corp briefly if at all, C corp once venture capital enters, public C corp at the IPO. The conversion from LLC to C corp — the "Delaware flip" — is so routine that lawyers run it on a script.

<!-- → [INFOGRAPHIC: timeline of a typical tech startup's legal-form arc from sole proprietorship through LLC, C-corp, and IPO, with the trigger for each conversion labeled] -->

The structural choice is not a tax optimization puzzle. It is a question of what the firm needs to do next and what legal form permits it. Each conversion is forced by the next round of capital — not by preference.

---

## The gap that runs through everything

A sole proprietor has no principal-agent problem. The decision-maker and the person who profits from those decisions are the same human being. Every choice is, by construction, in the interest of the only party that matters.

A corporation breaks this unity on purpose. The owners are usually different people from the managers. The managers have day-to-day control and detailed knowledge of the business. The owners have residual claims on the profits but limited information and limited day-to-day influence. This separation is the entire design — it lets the firm raise capital from people who are not equipped to run the company. But the same separation creates the central problem of corporate governance: **agents pursuing their own interests at the expense of principals.**

A **principal** delegates a decision to an **agent.** The agent has private information the principal lacks. The agent's interests diverge from the principal's. Without something to check this, the agent takes actions that benefit themselves at the principal's expense. The gap between what the agent does and what the principal would want is **agency cost.**

In the corporate context, this shows up in three forms.

<!-- → [INFOGRAPHIC: triangle diagram showing the three principal-agent conflicts — stockholders vs. management at the top, stockholders vs. creditors at lower left, stockholders vs. other stakeholders at lower right — with a one-line description of the core tension at each vertex] -->

**Stockholders versus management.** Managers want high salaries, large empires, prestige, security, and minimal discomfort. Shareholders want returns on investment. These are correlated but not the same thing. A CEO who builds a sprawling conglomerate increases their own compensation and power even when the conglomerate destroys shareholder value. A CEO who refuses to retire takes value from shareholders who would prefer fresh leadership. Bernard Ebbers, CEO of WorldCom before its 2002 bankruptcy, arranged $400 million in personal loans from the firm — using shareholder capital to fund his personal margin calls on WorldCom stock, while the company's financials were being fabricated to sustain the stock price that was collateral on those loans.

**Stockholders versus creditors.** Once a firm has issued debt, shareholders prefer riskier strategies than creditors do. The logic is asymmetric: shareholders capture all the upside if a risky bet pays off, but creditors absorb the downside if it fails — because shareholders' downside is bounded by limited liability. After the debt is issued, shareholders have an incentive to increase the firm's risk in ways the creditors did not price when they lent the money. This is the **asset-substitution problem.** Bond covenants — restrictions on what the firm can do with borrowed money — exist largely to prevent it.

**Stockholders versus other stakeholders.** Employees, customers, suppliers, communities. Decisions that maximize shareholder value can impose costs on all of them. Layoffs, plant closures, supplier squeezes, environmental externalities. The 2011 leveraged buyout of Harry & David is a textbook case: private-equity owners loaded the firm with debt, paid themselves dividends from the debt proceeds, hired a CEO who took outsized compensation, and the firm collapsed into bankruptcy. Shareholders who arrived early profited; everyone else absorbed the cost.

---

## The partial fixes

The field has converged on a small set of mechanisms that reduce agency cost without eliminating it. None of them work perfectly. All of them matter.

**Compensation alignment.** Pay executives in stock and stock options so their wealth tracks the share price. The logic is right; the implementation is fragile. Options reward upside without symmetric downside — which can encourage *more* risk-taking, not less. The 2008 financial crisis was, among other things, evidence that compensation alignment in financial firms had created incentives to take on risk that benefited managers in the short run and destroyed shareholder value in the long run. Restricted stock that vests over time aligns better. Multi-year performance shares align better still.

**Independent boards.** A **board of directors** is the governing body that sits between shareholders and management — hired to represent the owners, empowered to fire the CEO. The theory requires board members who have no financial relationship with the firm beyond their directorship and who are therefore willing to discipline management without conflict of interest. The practice is more complicated. Many "independent" directors are CEOs of other firms with overlapping relationships, social connections that create deference, or simply too many other board memberships to pay close attention to any one of them.

The **audit committee** is the sub-committee of the board that matters most to an analyst. Required by the Sarbanes-Oxley Act of 2002 to be composed entirely of independent directors, it supervises the firm's financial reporting and the relationship with the external auditor. When you read a 10-K, you should know who chairs the audit committee, how long they have served, and whether the committee has had unusual turnover. An audit committee that has lost three members in two years is a warning. An audit committee with no member who has previously served on a public-company audit committee is a different warning.

<!-- → [TABLE: audit committee red flags vs. green flags — two-column, specific to what an analyst should look for in a proxy statement] -->

**The threat of hostile takeover.** If management is destroying value, a corporate raider can buy a controlling stake at the depressed price, fire the management, and capture the difference. The *threat* of this — even when a takeover doesn't happen — disciplines management's behavior. The 1980s saw a wave of hostile takeovers. The 1990s saw firms install anti-takeover defenses: poison pills, staggered boards, dual-class share structures. The current equilibrium is somewhere between the extremes.

**Disclosure.** Public companies are required to file extensive financial information with the SEC, audited by independent accountants. Shareholders can sue for misrepresentation. Activist investors can publish critiques. The SEC can investigate. None of this is foolproof — Enron's 10-Ks were filed and audited — but the cumulative effect is real. Disclosure is the mechanism that makes external discipline possible in the first place.

The important thing to understand about all of these mechanisms is that they cost something. Rigorous oversight is expensive, slow, and risk-averse. Generous equity compensation transfers real wealth from shareholders to managers. Takeover threats distort decisions toward short-term share-price maximization. The correct level of governance is not zero and not maximum — it is a function of how large the agency gap is, how reversible bad decisions are, and how much oversight cost the firm can afford.

---

## How public companies talk to their owners

A public corporation is owned by people who are not in the room. The infrastructure that makes this work is mandatory disclosure — a regime of required filings, audited statements, and timed announcements that gives shareholders enough information to evaluate the firm without being inside it.

Two statutes from the 1930s built the modern US regime. The **Securities Act of 1933** governs the issuance of new securities — when a company sells stock or bonds to the public for the first time. It requires a prospectus disclosing material information. The **Securities Exchange Act of 1934** governs ongoing trading and ongoing disclosure, and created the **Securities and Exchange Commission** to enforce both.

**Sarbanes-Oxley (2002)** tightened the screws after Enron and WorldCom. SOX requires the CEO and CFO to personally certify the accuracy of the firm's financial statements — false certification is a criminal offense. It requires the firm to maintain effective internal controls over financial reporting, with the auditor attesting. It created the **Public Company Accounting Oversight Board (PCAOB)** to supervise the audit profession, replacing the self-regulatory regime that had failed in the Enron era.

<!-- → [CHART: timeline from 1933 to 2010 marking the Securities Act, Exchange Act, SOX, and Dodd-Frank, with a one-line annotation of what each added to the disclosure regime — student should see that each law followed a major market failure] -->

The filings that result from this regime are the analyst's primary data source.

**Form 10-K.** The annual report. Filed within 60–90 days after fiscal year-end. Contains audited financial statements (income statement, balance sheet, cash flow statement, footnotes), Management's Discussion and Analysis (MD&A) narrating the year's results, a risk factors section that can run dozens of pages, properties, legal proceedings, executive officers. If you read one document for a company, read its most recent 10-K.

**Form 10-Q.** The quarterly update. Filed within 40–45 days after each of the first three fiscal quarters. Less comprehensive than the 10-K; statements are reviewed by the auditor rather than audited.

**Form 8-K.** The current report. Filed within four business days of any material event — a major acquisition, the departure of a CEO, a change in auditor, a bankruptcy filing. The 8-K is how you find out what just happened between quarterly filings.

**Form DEF 14A.** The proxy statement. Filed before the annual meeting. Contains the board roster, director biographies, committee assignments, executive compensation, related-party transactions, and the proposals being voted on.

All of these are filed through the SEC's **EDGAR** system — free, public, complete. Every US-listed public company's filing history back to the early 1990s is on EDGAR. This is where analyst work begins.

<!-- → [INFOGRAPHIC: visual map of EDGAR filing types with their deadlines, what each contains, and when an analyst would reach for each one] -->

**GAAP and IFRS.** US-listed companies report under **Generally Accepted Accounting Principles (GAAP)**, set by the Financial Accounting Standards Board. Most other major markets use **International Financial Reporting Standards (IFRS)**, set by the International Accounting Standards Board. The two systems share most of their structure; the significant differences are in inventory accounting (GAAP allows LIFO; IFRS does not), treatment of certain development costs, reversal of inventory write-downs, and some intangibles and lease treatments. For cross-border comparisons, the differences matter — comparing a US firm under GAAP with a European peer under IFRS without adjustment is a category error.

---

## The whole system, seen together

The corporation is a legal invention that lets large numbers of strangers pool capital to fund enterprises larger than any individual could fund. The invention required solving three problems simultaneously: how to limit the strangers' personal liability, how to govern the enterprise so that managers don't steal from the strangers, and how to tell the strangers what is happening inside the firm.

Limited liability solves the first problem.

The governance machinery — boards, audit committees, fiduciary duties, executive compensation design, the threat of hostile takeover — partially solves the second, with substantial residual agency cost.

Mandatory disclosure under the SEC's regime partially solves the third, with substantial residual information asymmetry.

The residual in both cases is what gives public-company investing its texture. If governance and disclosure were perfect, every public company would trade exactly at fair value at all times, and there would be nothing for an equity analyst to do. Because they are imperfect, there is a profession.

The questions this chapter sets up — Is the board actually independent? Does compensation align management with shareholders? Are the disclosures telling you what's really going on? — are the questions your equity research report will spend 20 chapters learning to answer.

---

## What would change my mind

This chapter argues that the principal-agent gap is the central problem of corporate governance, and that limited liability plus disclosure plus governance mechanisms constitute a partial, permanently imperfect solution. The reading would have to revise if either (a) governance scholarship demonstrated that the residual agency cost is small enough to be economically trivial — some managerialist scholars argue this — or (b) a regulatory regime emerged that closed the gap more cleanly than the current US system. Neither finding has materialized. The current framework remains the working consensus, with its costs plainly visible every time a major governance failure reaches the front page.

## Still puzzling

The cleanest unresolved issue is *who the firm is for.* Shareholder-primacy is the orthodox American legal answer. The 2019 Business Roundtable statement of corporate purpose nominally moved toward stakeholder-balancing; the empirical evidence on whether stakeholder-oriented firms actually deliver different outcomes is contested. I find myself genuinely uncertain about whether shareholder-primacy is descriptively correct (it is what corporate law mostly enforces) or normatively right (the 2008 crisis and various ESG controversies are partial evidence against). The chapter holds the question open rather than resolve it.

---

## Exercises

### Warm-up

**2.1** Name the four general legal forms of business organization. For each, state in one sentence the single most important advantage and the single most important disadvantage.
*(Tests: legal forms and their trade-offs)*

**2.2** Explain in your own words why limited liability was necessary for large-scale public ownership to exist. What would happen if shareholders of Apple were personally liable for the company's debts?
*(Tests: the logic of limited liability as a precondition for capital markets)*

**2.3** Define agency cost. Give one concrete example from the chapter where agency cost was visible — name the firm, the agent, and the cost imposed on the principal.
*(Tests: principal-agent problem and its three flavors)*

### Application

**2.4** A software startup has three founders and has been operating as an LLC for two years. It is about to close a $15 million Series A round led by a venture capital fund. The fund's lawyer says the investment requires the company to convert to a C corporation first.

(a) Explain why the VC fund cannot invest in an LLC.
(b) Describe what the LLC-to-C-corp conversion involves and what the founders give up.
(c) The founders ask whether they should convert to an S corp instead to avoid double taxation. Advise them.
*(Tests: C-corp vs. S-corp eligibility and the capital-access driver of structural conversion)*

**2.5** You are reading the proxy statement of a mid-sized consumer goods company. You find the following:

- The board has 9 members; 5 are classified as independent.
- The CEO's compensation is 80% annual cash bonus tied to one-year revenue growth.
- The audit committee has 3 members; one joined 6 months ago after two others resigned.
- The company leases its headquarters from a real-estate LLC controlled by the CEO's spouse.

Identify two agency-cost flags in this description and explain the specific risk each flag represents to shareholders.
*(Tests: reading governance signals in a proxy and connecting them to agency-cost theory)*

**2.6** Go to EDGAR (sec.gov) and locate the most recent 10-K and DEF 14A for a public company of your choice. From the 10-K, write one paragraph describing the company's primary business. From the proxy, name the members of the audit committee and identify which, if any, are designated as audit committee financial experts.
*(Tests: EDGAR navigation and ability to locate specific information in required filings)*

### Synthesis

**2.7** Enron had a board with independent, credentialed outside directors. Its audit committee was chaired by a finance professor. It had Arthur Andersen as auditor. It filed 10-Ks with the SEC every year. Every governance mechanism that should have caught the fraud was present. Yet it failed.

Using the framework of this chapter, explain why each mechanism failed in Enron's specific case. Then identify what, if anything, could have worked — and why it didn't exist or wasn't triggered.
*(Tests: critical evaluation of governance mechanisms against a real failure case)*

**2.8** The asset-substitution problem says that once a firm has issued debt, shareholders prefer riskier strategies than creditors do. Explain the logic of this in your own words. Then explain why bond covenants are a partial — not complete — solution to the problem.
*(Tests: stockholders-vs.-creditors agency conflict and the mechanics of debt covenants)*

### Challenge

**2.9** Pick a public company that has dual-class share structures (Meta, Alphabet, Snap, or any other). Read the relevant section of its most recent proxy statement — typically the section on voting rights and share classes. Answer: Who holds the super-voting shares? What voting power do ordinary public shareholders have? Has this structure been beneficial or detrimental to public shareholders over the past five years, measured by stock-price performance and any documented governance controversies? Defend your assessment.
*(Tests: ability to evaluate a real governance structure using primary sources and form a defensible analytical view)*

**2.10** The 2019 Business Roundtable statement declared that corporations should serve all stakeholders, not just shareholders. Locate the statement online. Then find two pieces of empirical research — one published before 2022 and one after — on whether firms that publicly adopt stakeholder commitments deliver materially different financial or social outcomes. Do the firms' behaviors actually change, or just their language? What does the evidence say, and what does the gap between stated purpose and observed behavior tell you about agency cost?
*(Tests: ability to evaluate the shareholder-primacy vs. stakeholder debate using external evidence, not just the chapter's framing)*

---

## Connections forward

- **Chapter 4 and 5** build the accounting and financial-statement architecture that the disclosure regime produces — what's *in* a 10-K.
- **Chapter 6** computes ratios from those statements — what an analyst *does* with what's in a 10-K.
- **Chapter 17** revisits capital structure choice — the C-corp's debt-or-equity decision.
- **Chapter 20** revisits agency cost in the form of risk management — how firms decide which risks to take and which to hedge, and how shareholders monitor that.

---

## LLM Exercise — Chapter 2: Governance and Agency Assessment

**Project:** Equity Research Report on a Chosen Public Company
**What you're building this chapter:** A governance assessment of your chosen company — board independence, executive compensation alignment, and agency-cost flags.
**Tool:** Claude Project (with the most recent DEF 14A proxy statement uploaded alongside the 10-K).

### Setup

Before running the prompt: download your company's most recent **DEF 14A proxy statement** from EDGAR and upload it to your Claude Project. The proxy is a separate filing from the 10-K and contains the governance details this exercise needs.

### The Prompt

```
Based on the most recent DEF 14A proxy statement I have uploaded for [your company], produce a governance assessment with the following structure:

1. **Board composition** — Total board size, number of independent directors, number of women and minority directors, and any directors with potential conflicts (related-party relationships, multiple board memberships, age/tenure outliers).

2. **CEO compensation** — Total compensation in the most recent year, broken down by component (base, bonus, stock awards, options, other). Identify the metrics that drive the variable portion. Comment on whether the structure aligns CEO incentives with shareholders.

3. **Audit committee** — Names of members. Number of meetings in the past year. Identify any financial-expertise designees and any unusual recent turnover.

4. **Related-party transactions** — Any transactions disclosed in the proxy. Brief description, dollar amount, and your assessment of whether each is a flag.

5. **Shareholder proposals** — Any proposals voted on at the last annual meeting. Brief summary of each, the recommendation, and the vote outcome.

Cite specific page numbers from the proxy where possible. Don't invent details — if the proxy doesn't disclose something, say so.
```

### What this produces

A two-page governance assessment for the report. Identifies whether the firm's governance structure is investor-friendly, manager-friendly, or somewhere in between.

### How to adapt this prompt

- *For your own company:* Replace [your company] with your choice.
- *For ChatGPT / Gemini:* Upload the proxy to your Custom GPT or Gemini Gem.
- *For a Claude Project:* Add the proxy alongside the 10-K already in the project.

### Connection to previous chapters

Builds on the Chapter 1 three-decisions analysis. The governance lens helps assess whether those decisions were made in shareholders' interest.

### Preview of next chapter

Chapter 3 examines macro context — interest rates, inflation, the business cycle, currency exposure. The Chapter 3 LLM Exercise will produce a macro section for your report.

---

## AI Wayback Machine

**Adolf Berle** co-authored *The Modern Corporation and Private Property* (1932) — the founding work of corporate governance scholarship.

**Run this:**

```
Who is Adolf Berle, and how does their work connect to corporate governance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Adolf Berle"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Adolf Berle's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Adolf Berle's framework."

What changes? What gets better? What gets worse?
