# Chapter 2 — Corporate Structure and Governance

**Suggested titles**
1. Who Is the Firm For?
2. The Strange Invention of the Corporate Person
3. Owners, Managers, and the Gap Between Them

**TL;DR.** A corporation is a legal fiction that can do things a sole proprietorship cannot — outlive its founders, sue and be sued, raise capital from strangers, separate ownership from operation — and every benefit it confers creates a corresponding governance problem the law and the field of finance spend most of their time managing. This chapter pulls apart the legal forms, the principal-agent gap, and the disclosure machinery that makes public ownership work.

---

## The puzzle of the legal person

In late 2001, Enron Corporation — at one point the seventh-largest company in the United States, with reported revenues of over $100 billion — filed for bankruptcy. The filing was the largest in US history at the time. Within months, the company's stock had fallen from $90 to under $1. Twenty thousand employees lost their jobs. Pension accounts that had been concentrated in Enron stock were obliterated. Criminal charges followed; the CEO went to prison.

The mechanics of what happened are a story for a different chapter. The puzzle that matters here is structural: **how does this happen at all?** Enron had a board of directors. It had outside auditors (Arthur Andersen, a 90-year-old accounting firm that did not survive the scandal). It filed quarterly and annual reports with the Securities and Exchange Commission. Its stock was held by thousands of mutual funds, pension funds, and individual investors who were, in some legal sense, the *owners* of the company. The company's own management — the agents the owners had hired to run their property — were the people who hid the losses, lied to the board, and ultimately bankrupted the firm.

That gap — between who *owns* a corporation and who *runs* it — is the thing this chapter is about. The legal form of the corporation made it possible for a 20,000-person company to exist, raise tens of billions of dollars from public markets, and operate across continents. The same legal form made it possible for a small group of insiders to do enormous damage before any of the company's millions of owners noticed.

If you want to read a public company's 10-K and form a defensible opinion about whether to invest in its stock — which is the project running through this book — you have to understand the machinery. The 10-K is a disclosure document. *To whom*, *why*, and *enforced how* are the questions Chapter 2 answers.

---

## Learning objectives

After working through this chapter, you should be able to:

- Compare the four main forms of business organization — sole proprietorship, partnership, corporation, hybrid (LLC/LLP) — across liability, taxation, governance, and ability to raise capital.
- Distinguish a C corporation from an S corporation, and identify why a growing firm typically converts.
- Define the principal-agent problem in a corporate context, name the three main flavors (stockholders vs. management, stockholders vs. creditors, stockholders vs. other stakeholders), and identify mechanisms used to mitigate it.
- Describe the structure and core responsibilities of a board of directors, including the audit committee.
- Read a corporate filing (10-K, 10-Q, 8-K) and tell what you would expect to find in it.
- Locate a public company's filings on EDGAR.

**Prerequisites.** Chapter 1, especially the three areas of finance and the basic balance-sheet vocabulary.

---

## Concept 1 — The four forms, and why most large firms end up as corporations

Suppose you and a friend open a coffee shop. The first decision the lawyer asks you about is *what legal form* the business takes. The choice changes who is liable for what, how you are taxed, who can own a piece of the business, and what happens to the business when one of you wants out. There are four general answers.

**Sole proprietorship.** One owner, no separate legal entity. You *are* the business. To start one, you basically just start doing business — file a Schedule C with your tax return at year-end and you're done. The advantages are real: simplicity, no separate corporate income tax, total control. The disadvantages are also real, and they are the reason most successful sole proprietors eventually convert.

The first disadvantage is **unlimited personal liability**. Your business and your personal finances are legally the same pile of money. If a customer slips on icy stairs and wins a $500,000 judgment, your house and your savings are at risk for the difference between the judgment and your liability insurance. The second disadvantage is **the firm cannot outlive you** — proprietorships generally end when the proprietor dies or quits. The third is **limited access to capital** — banks lend cautiously to sole proprietors because the assets behind the loan are personal, and outside equity investors are functionally locked out because the legal form has no shares to sell.

**Partnership.** Two or more owners, no separate legal entity. Same basic structure as a sole proprietorship, doubled. Each general partner is liable for the partnership's debts — *and* for the misconduct of every other general partner. If your partner fraudulently mismanages a client account and the client wins a judgment for $2 million, you are on the hook for whatever your partner cannot pay. This sounds like a horror story; it is, periodically, an actual horror story. Modern law firms used to be general partnerships before liability-protected forms became available, and large firms occasionally collapsed when one partner's misconduct propagated.

Partnerships have certain tax advantages — income passes through to the partners' personal returns, avoiding the corporate income tax — and they let multiple people pool capital and expertise. They retain most of the proprietorship's disadvantages: unlimited liability, mortality, and limited capital access.

**Corporation.** A legal entity *separate* from its owners. This is the move. A corporation is created by filing **articles of incorporation** with a state (often Delaware, for reasons that are mostly about Delaware's specialized corporate law and chancery courts). Once incorporated, the corporation can sign contracts, sue and be sued, own property, hire employees, raise capital — all in its own name, distinct from any of its owners.

Three things flow from the separation.

First, **limited liability**. A corporation's owners (its shareholders) can lose what they invested in the company's stock — and no more. If the company goes bankrupt with $1 billion in unpaid debts, the shareholders are not on the hook for those debts. Their downside is bounded by what they paid for the shares. This single feature is what makes large-scale public ownership *possible*. Without it, no rational person would buy a fraction of a stranger's business.

Second, **unlimited life**. Owners come and go; the corporation persists. Shares trade between investors, founders die, executives retire — the entity continues. Apple was incorporated in 1977 and is older now than two of its three co-founders.

Third, **transferable ownership**. Shares of stock can be sold, given, or inherited without disrupting the firm. In a partnership, when a partner leaves, the partnership has to be reformed. In a corporation, when a shareholder sells, nothing inside the firm changes — the new shareholder simply replaces the old on the cap table.

The corporation's main disadvantage is **double taxation**. The corporation pays income tax on its profits. When it distributes after-tax profits to shareholders as dividends, the shareholders pay income tax again on the dividends. This is the price of separation.

**Hybrids — LLC and LLP.** The 1990s gave rise to legal forms that combine the corporation's limited liability with the partnership's pass-through taxation. A **limited liability company (LLC)** has owners called "members" who enjoy limited liability; the LLC is taxed as a partnership (no entity-level tax). A **limited liability partnership (LLP)** is similar in spirit and is the standard form for professional services firms — law, accounting, architecture — where one partner's misconduct should not bankrupt the others.

The LLC has become the default form for new small businesses in the United States. It is administratively heavier than a sole proprietorship — articles of organization must be filed with the state — but the limited-liability protection is usually worth the trouble. A small note that surprises people: Amazon's retail operation is structured as an LLC (Amazon.com Services LLC), even though Amazon.com Inc. is a publicly traded C corporation. Big firms run hybrid structures.

**C corporation vs. S corporation** — a footnote that matters. A regular corporation, called a **C corporation** for tax-code reasons, faces the double-taxation problem above. The tax code carves out an alternative — the **S corporation** — for closely held firms. An S corporation is taxed like a partnership: income passes through to shareholders' personal returns, no entity-level tax. The catch is eligibility: an S corp cannot have more than 100 shareholders, the shareholders must mostly be US citizens or residents, and the firm cannot have more than one class of stock. The first time an S corporation needs to raise capital from a wide range of investors — including institutional investors who can't hold S-corp stock under the rules — it converts to a C corp. This is the standard trajectory: S corp while small, C corp once growth requires public markets.

↳ **Dig Deeper — Dual-class share structures**

*Some public companies (Meta, Google, Snap, many media firms) issue two classes of stock with different voting rights — founders keep super-voting shares while public investors hold non-voting or low-voting shares. Critics call this "permanent founder control"; defenders call it "long-term thinking insulation."*

**Prompt:**
> Explain the structure and rationale for dual-class share structures. Walk through three real examples (Meta/Facebook, Google/Alphabet, Snap). Then evaluate the empirical evidence: do dual-class firms outperform or underperform single-class firms over 5-10 year periods? What's the strongest argument for and against allowing them in major indexes?

**What to do with the output:** Save it as governance context. Many tech companies your equity research project might cover have dual-class structures; the assessment in Chapter 2's LLM Exercise should engage this directly.

### The trade-off (concept 1)

Every legal form trades **owner protection against tax efficiency, governance simplicity, and ability to raise capital**. The sole proprietorship maximizes governance simplicity (one decision-maker) at the cost of unlimited liability and capital access. The C corporation maximizes capital access and limited liability at the cost of double taxation and governance complexity. The LLC tries to split the difference. There is no dominant form — the right choice depends on size, growth ambitions, and how much governance overhead the owners can tolerate.

### Worked example — a growing firm's structural arc

Consider a fictitious software firm that goes through five stages over fifteen years.

| Stage | Form | Reason for the choice |
|---|---|---|
| Founder writes code in evenings | Sole proprietorship | No separation needed; tax simplicity. |
| Brings on co-founder | LLC, two members | Limited liability matters now; pass-through taxation preserves simplicity. |
| Hires 12 employees, raises seed round from angels | LLC, multi-member | Still pass-through; angels accept LLC interests. |
| Series A — raises $20M from a venture firm | Converts to C corporation | VC funds are required by their own structures to invest in C corps. |
| IPO at year 12 | C corporation, public | Limited liability + transferable shares + ability to issue new stock to public buyers. |

The structural arc is so common in technology that lawyers and venture investors have a script for the LLC-to-C-corp conversion (often called a "Delaware flip") and execute it routinely. The interesting thing is *why* the script exists: each stage forced a structural change because the prior structure could not handle the next round of capital. The legal form is a tool, and you change tools when the work changes.

### Common misconceptions

- *"The corporation is just a tax dodge."* No — it is fundamentally a *liability* solution. The tax structure is a side effect that varies by jurisdiction.
- *"All corporations are public."* The vast majority of C corporations in the United States are privately held. Public companies are a small fraction of the corporate population, but they hold a large fraction of corporate assets.
- *"LLCs are always better than corporations."* For small firms, often. For firms raising venture capital, never — VC funds cannot invest in LLCs without massive structural friction. The optimal form depends on the firm's destination.

---

## Concept 2 — The principal-agent problem (the gap that runs through everything)

A sole proprietor has no principal-agent problem. The decision-maker, the residual claimant on profits, and the bearer of risk are the same person. Every decision is, by construction, in the interest of the only party that matters — themselves.

A corporation breaks this unity by design. The owners (shareholders) are usually different people from the managers (executives, employees). The managers have day-to-day control. The owners have residual claims on profits but limited information and limited day-to-day influence. This separation is the entire point of the corporate form — it lets you raise capital from people who are not equipped to run the company. But the same separation creates the central problem of corporate governance: **agents pursuing their own interests at the expense of principals.**

### The principal-agent problem, formally

A **principal** delegates a decision to an **agent**. The agent has private information (about effort, ability, costs, opportunities) the principal lacks. The agent's incentives may diverge from the principal's. Without mitigation, the agent will take actions that benefit themselves at the principal's expense — *agency cost.*

In the corporate context, this shows up as three flavors.

**Stockholders versus management.** Managers want high salaries, generous benefits, prestige, large empires, and minimal discomfort. Shareholders want high returns on investment. These are correlated but not identical. A CEO who builds a sprawling conglomerate increases their own compensation and prestige even when the conglomerate destroys shareholder value. A CEO who refuses to retire takes value from shareholders who would prefer fresh leadership. A CEO who arranges sweetheart loans from the firm — as WorldCom's Bernard Ebbers did before the firm's 2002 bankruptcy — is using shareholder capital to fund personal lifestyle.

**Stockholders versus creditors.** Once a firm has issued debt, shareholders prefer riskier strategies than creditors do. The reasoning is asymmetric: shareholders capture all the upside if a risky bet pays off, but creditors absorb most of the downside if it fails (because shareholders' downside is bounded by limited liability). After the debt is issued, shareholders have an incentive to *increase* the firm's risk in ways the creditors did not bargain for — the **asset-substitution problem**. Bond covenants exist largely to prevent this.

**Stockholders versus other stakeholders.** Employees, customers, suppliers, and communities also have stakes in the firm's behavior. Decisions that maximize shareholder value can — and routinely do — impose costs on other stakeholders. Layoffs, plant closures, supplier squeezes, environmental externalities. The 2011 leveraged-buyout-then-bankruptcy of Harry & David is a case in point: the new owners loaded the firm with debt, paid themselves dividends, hired a CEO who took outsized compensation, and the firm collapsed. Shareholders who arrived early profited; shareholders who arrived late, employees, suppliers, and the firm's community absorbed the cost.

### Mechanisms to mitigate agency costs

The field has converged on a small set of partial fixes.

**Compensation alignment.** Pay executives in stock and stock options so their wealth tracks the share price. The logic is sound; the implementation is fragile. Stock options reward upside without symmetric downside, which can encourage *more* risk-taking, not less. Restricted stock that vests over time aligns better. Long-term performance shares with multi-year horizons align better still. The 2008 financial crisis was, among other things, a referendum on the limits of compensation alignment in financial firms.

**Independent boards.** Boards of directors with a majority of *independent* members — directors who have no material financial relationship with the firm beyond their directorship. The logic: independent directors can fire underperforming CEOs without conflict of interest. The implementation: many "independent" directors are CEOs of other firms with overlapping interests, golf-circle relationships, or service-on-multiple-boards conflicts. Sarbanes-Oxley (2002) tightened the rules in response to Enron; subsequent scandals (Wells Fargo's account-fraud crisis, for example) suggest the rules can still be evaded.

**Hostile takeovers.** If a firm's management is destroying value, a corporate raider can buy a controlling stake at a depressed price, fire the management, and capture the value-creation gain. The threat of this — even when a takeover doesn't happen — disciplines management. The 1980s saw a wave of hostile takeover activity. The 1990s saw firms install poison pills and other anti-takeover defenses. The current equilibrium is somewhere between the extremes.

**Disclosure and oversight.** Public companies are required to file extensive financial information with the SEC, audited by independent accountants. Shareholders can sue. Activist investors can publish detailed critiques. The SEC can investigate. None of this is foolproof — Enron's 10-Ks were filed and audited — but the cumulative effect is real.

### The audit committee — the part of the board that matters most for an analyst

Every public company's board has an audit committee — a sub-committee, required by SOX to be composed entirely of independent directors, that supervises the firm's financial reporting and the relationship with the external auditor. As an analyst reading a 10-K, you should know who is on the audit committee, how many financial-expertise designees they have, and whether the committee has had unusual turnover. An audit committee that has lost three members in two years is a warning. An audit committee with no member who has served on a public-company audit committee before is a different warning.

### ESG ratings — a contested addition

Over the past two decades, third-party firms have begun rating public companies on **environmental, social, and governance (ESG)** factors. Investors increasingly use these ratings to screen and select investments. ESG ratings are also contested — different rating providers can give the same company wildly different scores, and the empirical relationship between ESG scores and stock returns is the subject of ongoing academic debate.

For the running project — building a defensible equity research report — ESG ratings are a useful input but not a primary signal. Treat them as one of several data points, examine the rater's methodology, and form your own view of the underlying issues (environmental risk, board diversity, executive compensation alignment) rather than deferring to a composite score.

↳ **Dig Deeper — Stakeholder capitalism vs. shareholder primacy**

*The 2019 Business Roundtable statement nominally moved from shareholder-primacy to stakeholder-balancing as the corporate purpose. The empirical evidence on whether stakeholder-oriented firms actually deliver different outcomes is contested.*

**Prompt:**
> Explain the historical context and substantive content of the 2019 Business Roundtable "Statement on the Purpose of a Corporation." Then summarize the empirical evidence: do firms that publicly commit to stakeholder principles (or score high on ESG metrics) deliver materially different financial returns, employee outcomes, or community outcomes than firms that don't? Distinguish "talking about stakeholder principles" from "behaving differently."

**What to do with the output:** Read with care. The shareholder-vs-stakeholder question shapes how you assess your project company's stated purpose vs. its observable behavior.

### The trade-off (concept 2)

Mechanisms that mitigate agency cost themselves cost something. Rigorous oversight is expensive, slow, and risk-averse. Generous executive compensation aligns incentives but can transfer real wealth from shareholders to managers. The threat of hostile takeover keeps management honest but can also distort decisions toward short-term share-price maximization at the expense of long-run value. The correct level of governance is not zero and not maximum. It is a function of how large the agency gap is, how reversible bad decisions are, and how much oversight cost the firm can absorb.

### Worked example — reading a proxy statement for agency-cost signals

A public company's annual **proxy statement** (filed as Form DEF 14A on EDGAR) is the document you read to assess governance. It includes:

- The board's composition, with each director's biography, other board memberships, and committee assignments.
- Executive compensation — base salary, bonus, stock awards, stock-option grants, perquisites, deferred compensation. The compensation discussion and analysis (CD&A) section explains the rationale.
- Related-party transactions — any deals between the company and its directors, executives, or their relatives.
- Shareholder proposals and management's responses.

When reading a proxy as an analyst, the questions to ask:

1. **Is the board independent?** Count the independent directors. Read their other affiliations. A board where the CEO's golf buddies and former colleagues dominate is a different governance environment than one with seasoned outside directors.
2. **Is compensation aligned?** Read the CD&A. Is bonus tied to one-year metrics or multi-year? Are stock awards performance-vested or time-vested? What happens to compensation if the firm underperforms?
3. **Are there related-party transactions?** Lease payments to a building owned by the CEO's family trust, consulting fees to a director's firm, sweetheart loans — these are not necessarily illegal but they are flags.
4. **What do shareholder proposals say?** Frequent governance-related shareholder proposals (declassify the board, separate chair and CEO, allow proxy access) indicate that other shareholders see governance issues that management is not addressing.

This is the level of analysis your equity research report will demonstrate by Chapter 20. We are setting up the questions now so the answers can accumulate as the book proceeds.

### Common misconceptions

- *"Maximizing shareholder value is the same as being good for everyone."* It is not. The trade-offs against employees, customers, communities, and creditors are real. The shareholder-primacy model is *one* answer to "who is the firm for"; stakeholder-balancing models are alternatives. Reasonable people disagree.
- *"Independent directors prevent agency problems."* They reduce them. Enron had an independent board. WorldCom had an independent board. Wells Fargo had an independent board during its account-fraud crisis. Independence is necessary but not sufficient.
- *"ESG scores are objective."* They are not. Different providers using different methodologies give the same firm different scores. Use them as inputs, not as conclusions.

---

## Concept 3 — How public companies talk to their owners

A public corporation is owned by people who are usually not in the room. The legal infrastructure that makes this work is **mandatory disclosure** — a regime of required filings, audited statements, and timed announcements that gives shareholders enough information to evaluate the firm without being inside it. Disclosure is the price of public ownership.

For an analyst writing an equity research report, mandatory disclosure is the source material. Most of the data in your final report — every line of the financial statements, every footnote, every management commentary on segment performance, every executive's compensation, every material risk factor — comes from these filings. Knowing where to look and what to look for is a basic professional skill.

### The Securities Acts and the SEC

Two pieces of 1930s legislation built the modern US disclosure regime. The **Securities Act of 1933** governs the issuance of new securities — primary-market activity. It requires the issuing firm to register the securities with the SEC and file a prospectus disclosing material information. The **Securities Exchange Act of 1934** governs ongoing trading and ongoing disclosure — secondary-market activity — and created the **Securities and Exchange Commission (SEC)** to enforce both acts.

Subsequent legislation added pieces. The **Sarbanes-Oxley Act of 2002 (SOX)** was passed in response to Enron and WorldCom. SOX requires:

- The CEO and CFO must personally certify the accuracy of the firm's financial statements. False certification is a criminal offense.
- The firm must maintain an effective system of internal controls over financial reporting, with the auditor attesting to that effectiveness.
- The audit committee must be entirely independent and must include at least one member with financial expertise.
- The Public Company Accounting Oversight Board (PCAOB) supervises the public-company audit profession, replacing the largely self-regulatory regime that had failed in the Enron era.

The **Dodd-Frank Act of 2010** was passed in response to the 2008 financial crisis and added requirements around executive compensation, derivatives, and large-bank stress testing.

The cumulative effect: a US-listed public company is required to disclose far more than its private peers, with serious legal consequences for misrepresentation.

### The required filings — the analyst's reading list

Every public company files a small set of standard documents. The most important:

**Form 10-K — annual report.** Filed within 60–90 days after fiscal year-end (timing depends on the firm's size). The 10-K is the most comprehensive single document a public company produces. It contains:

- Audited financial statements — income statement, balance sheet, cash flow statement, statement of stockholders' equity, with footnotes.
- Management's Discussion and Analysis (MD&A) — narrative commentary on the year's results, segment performance, liquidity, capital resources, and known trends.
- Risk factors — a list, often dozens of pages long, of material risks the firm faces.
- Properties, legal proceedings, executive officers.
- Five-year selected financial data.

If you read only one document for a company, read its most recent 10-K. We will spend Chapter 5 working through the structure of these statements in detail.

**Form 10-Q — quarterly report.** Filed within 40–45 days after each of the first three fiscal quarters (the fourth quarter rolls into the 10-K). Less comprehensive than the 10-K, but contains updated financial statements (typically *unaudited* — only "reviewed" by the auditor) and a brief MD&A.

**Form 8-K — current report.** Filed within four business days of any material event. Acquisitions, departures of executives, changes in auditor, bankruptcy filings, material contracts, material accounting changes. The 8-K is how you find out what just happened between quarterly filings.

**Form DEF 14A — proxy statement.** Filed before the annual meeting. Contains the board roster, director biographies, committee assignments, executive compensation, related-party transactions, and the slate of items being voted on at the annual meeting.

**Form S-1 — registration statement for new securities.** Filed before an IPO or other public offering. Particularly important for newly public companies — it includes a more thorough business description than a 10-K and is the closest thing to a prospectus available.

All of these are filed electronically through the SEC's **EDGAR** system, which is free and public. Every public US-listed company's complete filing history is available on EDGAR. As an analyst, EDGAR is the equivalent of a cardiologist's stethoscope — basic, cheap, indispensable.

### Investor relations — the firm's side of the conversation

The flip side of mandatory disclosure is **voluntary disclosure** — the additional communication a firm chooses to provide to investors. Quarterly earnings conference calls, investor days, management presentations at brokerage conferences, press releases, the corporate IR website. The Investor Relations (IR) function inside the firm is responsible for these.

Voluntary disclosure is not optional in practice. A firm that says nothing beyond its required filings will be punished by the market through wider bid-ask spreads, lower analyst coverage, and a higher cost of equity. Most public firms hold quarterly earnings calls within 45 days of fiscal quarter-end. The transcript and audio are usually available on the firm's IR website and through services like Bloomberg or Seeking Alpha.

For the equity research project, the quarterly call is one of the richest sources of information you have. Listen to or read the most recent call for your chosen company. The CEO's prepared remarks tell you the story management wants told. The Q&A section — when sell-side analysts ask the questions they actually want answered — tells you what the professional analyst community is concerned about. Read three or four consecutive quarters of calls back-to-back; the things management *stops* talking about are often more revealing than the things they emphasize.

### GAAP, IFRS, and the international wrinkle

US-listed companies report under **Generally Accepted Accounting Principles (GAAP)**, the standard set by the Financial Accounting Standards Board (FASB). Most other major markets — the European Union, the United Kingdom, Australia, Singapore, much of Asia — use **International Financial Reporting Standards (IFRS)**, set by the International Accounting Standards Board (IASB).

GAAP and IFRS share most of their structure. The major differences are in:
- Inventory accounting — GAAP allows LIFO (last-in, first-out), IFRS does not.
- Development costs — IFRS allows capitalization of certain development costs that GAAP requires to be expensed.
- Reversal of inventory write-downs — IFRS allows reversal under some conditions, GAAP does not.
- Treatment of certain intangibles, leases, and consolidations.

For an analyst doing cross-border comparisons, the differences matter — comparing a US firm under GAAP with a European peer under IFRS without adjustment is a category error. Many large firms file *reconciliations* in their annual reports to help bridge.

### The trade-off (concept 3)

Mandatory disclosure trades **the firm's privacy and compliance cost against the public market's ability to function**. A firm with no disclosure obligation is cheaper to run but cannot raise capital from public markets at any reasonable cost — investors will not finance what they cannot see. A firm with maximum disclosure obligation is more expensive to run but enjoys lower cost of capital because investors can evaluate it. Public listing is the choice to accept high disclosure cost in exchange for cheap capital. Some firms — Mars, Cargill, Koch — have decided the trade is not worth it and stay private despite their size.

### Worked example — finding what you need on EDGAR for the project

For your chosen public company, the first hour of analyst work looks like this:

1. Go to SEC.gov, click "EDGAR" in the navigation, click "Company Search."
2. Type the company name or ticker. Open the company's filings page.
3. Find and download:
   - Most recent **10-K** (full year, audited).
   - Most recent two **10-Qs** (latest two quarters).
   - Most recent **DEF 14A** (proxy).
   - Any **8-Ks** filed in the past 12 months.
4. Skim the 10-K's Item 1 (Business) and Item 1A (Risk Factors). These give you the firm's description of itself and the risks it discloses.
5. Open the proxy. Read the director biographies and the executive compensation tables.
6. Make a note of the auditor's name (in the 10-K) and the audit committee's composition (in the proxy).

You now have, in one hour, the foundation for everything that follows. Every chapter from here adds analytical layers to this base.

### Common misconceptions

- *"Disclosure documents are propaganda."* They are managed but not propaganda. Items are required, formats are constrained, the auditor signs off, the CEO certifies, and lying carries criminal penalties. Read them critically — but read them.
- *"The 10-Q is enough; the 10-K is too long."* The 10-K contains the audited statements and the full risk factors and MD&A. It is the document. The 10-Q is the update.
- *"Press releases are reliable."* Not particularly. They are firm-authored communications without auditor sign-off. They are starting points; the underlying filings are the source of truth.

---

## Synthesis — owners, agents, and disclosure as one system

The corporation is a legal invention that lets large numbers of strangers pool capital to fund enterprises larger than any individual could fund. The invention required solving three problems at once: how to limit the strangers' personal liability, how to govern the enterprise so that managers do not steal from the strangers, and how to tell the strangers what is going on inside the firm.

Limited liability solved problem one. The corporate-law machinery — boards of directors, audit committees, fiduciary duties, the threat of hostile takeover — partially solves problem two, with substantial residual agency cost. Mandatory disclosure under the SEC's regime partially solves problem three, with substantial residual information asymmetry.

The remaining residual is what gives public-company investing its texture. If governance and disclosure were perfect, every public company would trade exactly at fair value at all times, and there would be nothing for an equity analyst to do. Because they are not, there is a profession.

For the running project, this chapter has set up the data sources (EDGAR), the documents (10-K, 10-Q, 8-K, DEF 14A), and the questions to ask of them (independence, compensation alignment, related-party transactions, audit committee competence). Subsequent chapters fill in what to *do* with the documents.

---

## Exercises

### Warm-up

**2.1** Name the four general legal forms of business organization and one major advantage and disadvantage of each.

**2.2** Distinguish a C corporation from an S corporation in three respects: shareholder limit, taxation, and typical use case.

**2.3** Write one sentence each defining: principal-agent problem, agency cost, audit committee, related-party transaction.

### Application

**2.4** Imagine you are starting a small consulting firm with one partner. Compare the legal forms LLC, LLP, and S corporation across:
(a) Liability protection
(b) Tax treatment
(c) Administrative complexity
(d) Ability to bring in outside investors later

Recommend a form and explain in two sentences why.

**2.5** Read the following description of a hypothetical CEO compensation package and identify two features that align incentives with shareholders and two that potentially misalign them:

> "The CEO receives a base salary of $1.5 million, an annual cash bonus of up to 200% of base salary tied to one-year EPS growth, $5 million per year in stock options that vest over four years, $2 million per year in restricted stock that vests immediately, a personal-use corporate aircraft allowance of $400,000, and a guaranteed severance payment of three years' base salary in the event of any termination, including for cause."

**2.6** Locate, on EDGAR, the most recent 10-K and most recent DEF 14A for a public company of your choice. Write a one-paragraph description of the company based on the 10-K's Item 1 (Business). List the names of the directors from the proxy. Identify the chair of the audit committee.

### Synthesis

**2.7** Enron's board of directors consisted of largely independent, well-credentialed outsiders, and the firm's audit committee was chaired by a finance professor at Stanford. The firm had Andersen as auditor. Yet the firm collapsed in 2001 amid a multi-billion-dollar accounting fraud. List three governance mechanisms that *should* have prevented this and explain why each one failed in the specific case.

**2.8** A friend says: "Public companies should just do what's best for shareholders. Stakeholder considerations are a distraction." Construct your strongest version of (a) a counter-argument from agency theory, (b) a counter-argument from long-run shareholder value, and (c) a counter-argument from legitimacy of the corporate form itself. You may end up persuaded or unpersuaded — show your reasoning.

### Challenge

**2.9** Read the executive compensation section of the most recent proxy statement for the company you chose for the equity research project. Identify the CEO's total compensation in the most recent year, the breakdown by component (salary, bonus, stock awards, options, other), and the performance metrics that drive the variable portion. Then, read the same section in the proxy from five years earlier. Has compensation grown faster or slower than the firm's revenue? Operating income? Stock price? Defend your reading of whether compensation has been aligned with performance.

**2.10** ESG ratings for the same company can vary dramatically across rating providers (MSCI, Sustainalytics, S&P Global, ISS). Pick a public company and look up its ESG scores from two different providers. (Some are paywalled; FREE views may suffice.) Explain why the providers might disagree and which (if either) you find more credible. What does this tell you about the usefulness of ESG ratings as inputs to investment decisions?

---

## Chapter summary

- Four main legal forms — sole proprietorship, partnership, corporation, hybrid (LLC/LLP). Each trades liability protection, tax efficiency, governance simplicity, and capital access differently.
- The corporation's defining features: limited liability, unlimited life, transferable ownership. Cost: double taxation (in the C-corp case).
- The principal-agent problem arises whenever owners and managers are different people. Three flavors: stockholders vs. management, stockholders vs. creditors, stockholders vs. other stakeholders. Mitigation tools: aligned compensation, independent boards, takeover threat, disclosure.
- A public company's required filings (10-K, 10-Q, 8-K, DEF 14A) on EDGAR are the analyst's primary data source.
- Mandatory disclosure under the 1933 and 1934 Acts, expanded by SOX (2002) and Dodd-Frank (2010), is the price of public capital — and the substrate of every analytical move in the rest of this book.

---

## What would change my mind

The chapter argues that the corporate form's separation of ownership from management is the central problem of corporate governance, partially solved by independent boards, aligned compensation, and mandatory disclosure. The reading would have to revise if either (a) governance scholarship demonstrated that the residual agency cost is small enough that it isn't actually the central problem (some managerialist scholars argue this), or (b) a regulatory regime emerged that closed the principal-agent gap more cleanly than the current US system — for example, dual-class structures with strong long-term locked-in shareholders, as in some European cooperative banking groups. Neither finding has materialized; the current US framework remains the working consensus.

## Still puzzling

The cleanest unresolved issue is *who the firm is for*. Shareholder-primacy is the orthodox American answer; the Business Roundtable's 2019 statement of corporate purpose nominally moved toward stakeholder-balancing; the empirical evidence on whether stakeholder-oriented firms outperform shareholder-oriented firms across cycles is contested. I find myself genuinely uncertain about whether shareholder-primacy is descriptively correct (it is what corporate law mostly enforces) or normatively right (it may not be — the 2008 crisis and various ESG controversies are partial evidence against). The chapter holds the question open rather than resolve it.

---

## Connections forward

- **Chapter 4 and 5** build the accounting and financial-statement architecture that the disclosure regime produces — what's *in* a 10-K.
- **Chapter 6** computes ratios from those statements — what an analyst *does* with what's in a 10-K.
- **Chapter 17** revisits capital structure choice — the C-corp's debt-or-equity decision.
- **Chapter 20** revisits agency cost in the form of risk management — how firms decide which risks to take and which to hedge, and how shareholders monitor that.

---

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

**Tags:** corporate-governance, principal-agent, business-forms, EDGAR, disclosure, audit-committee


---

## AI Wayback Machine

**Adolf Berle** was co-authored The Modern Corporation and Private Property (1932) — the founding work of corporate governance scholarship.

**Run this:**

```
Who is Adolf Berle, and how does their work connect to corporate governance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Adolf Berle"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Adolf Berle's framework to a specific finance question.
- Add a constraint: "Answer including criticisms or limits of Adolf Berle's framework."

What changes? What gets better? What gets worse?
