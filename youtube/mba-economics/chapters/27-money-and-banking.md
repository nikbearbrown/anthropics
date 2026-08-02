# Chapter 27 — Money and Banking

*What money actually is, how banks create it, and the institutional plumbing that makes the modern monetary system work.*

---

In some Pacific islands of the 19th century, money was made of cowrie shells. In Yap, it was carved limestone disks weighing thousands of pounds. In medieval Europe, coins struck from gold and silver. In post-WWII America, paper notes redeemable in gold — until 1971, when that last link to physical substance was cut. Since then, the dollar has been backed by nothing except the expectation that others will accept it. In the 21st century, most U.S. dollars don't exist in physical form at all: they're electronic entries in bank databases. And in some recent corners of the digital world, money is cryptographic tokens on distributed ledgers.

What do cowries, gold, paper, and bytes have in common? They're accepted in exchange for goods and services because *other people accept them*. That's the deep observation. Money's value is collective and conventional. When the convention holds — when everyone agrees that these objects represent value — the system functions. When it breaks down, in hyperinflation or currency collapse or political chaos, the money can lose its value almost overnight. The intrinsic material is irrelevant. The agreement is everything.

This chapter is about the institutional plumbing of money: what it does, what forms it takes, how the U.S. measures it, how banks work, and — the genuinely surprising part — how the banking system creates money well beyond what the central bank ever printed.

---

## What money does

Money serves four distinct functions, and distinguishing them helps explain why some things work as money and others don't.

**Medium of exchange.** Money is what you use to buy things. Without money, every transaction would require barter — direct exchange of goods. Barter requires a *double coincidence of wants*: I have wheat and want wool; I need to find someone with wool who wants wheat. The probability of that exact match at the exact moment is low. Money eliminates the problem: I sell wheat for money, someone else sells wool for money, we both buy what we want, and the transactions don't have to happen at the same time or between the same parties.

**Unit of account.** Money is the common unit in which prices are stated and accounts are kept. A pizza is $15. A car is $30,000. A year's labor is $80,000. These prices are comparable because they share a unit. Without a common unit, you'd need prices in terms of every other good: a car costs 2,000 pizzas, or 0.375 years of labor, or 15 tons of wheat. The bookkeeping would be impossibly complex.

**Store of value.** Money holds value over time. Cash held today still buys things next month. This function works well when inflation is low and breaks down when inflation is high. In Zimbabwe in 2008, hyperinflation running at 89 sextillion percent per year made cash worthless within days — people carried groceries home in wheelbarrows of currency and quickly switched to U.S. dollars.

**Standard of deferred payment.** Loans, mortgages, and other future-payment contracts are denominated in money. The dollar promised in a contract is the dollar that will be owed. This requires money to be reasonably predictable in value over the contract's life — again, a property that breaks down in high inflation.

Together, these four functions explain why money is valuable even when it has no intrinsic worth. A bank note is just paper. Its value comes entirely from these functions and the collective agreement to honor them.

<!-- → [TABLE: The four functions of money — columns: Function | What it does | What breaks it | Example of failure; rows: Medium of exchange / Eliminates double coincidence of wants / Hyperinflation (no one accepts it) / Zimbabwe 2008 — people switched to USD; Unit of account / Provides common price denominator / Very high inflation (prices unstable) / 1920s Germany — prices quoted in millions; Store of value / Preserves purchasing power over time / Sustained inflation / Any currency with persistent high inflation; Standard of deferred payment / Denominator for future-payment contracts / Inflation uncertainty / Long-term contracts become unenforceable in value; caption: "Each function serves a different need. A currency can succeed at some while failing at others — Zimbabwe's dollar briefly still served as a unit of account while failing as a store of value."] -->

---

## Commodity vs. fiat

**Commodity money** has intrinsic value independent of its monetary role. Gold and silver coins are worth something even melted down. Cowrie shells have ornamental value. Cigarettes functioned as money in WWII prisoner-of-war camps partly because they're worth something to smokers. The monetary value of commodity money is anchored in part to the underlying commodity market.

**Fiat money** has no intrinsic value. Modern paper currency, electronic deposits, the digital numbers in a bank account — these are worth something only because the monetary system functions and people accept them. Strip away the convention and you have paper or bytes.

The U.S. dollar was on a gold standard until 1971: each dollar was officially redeemable for a fixed quantity of gold. President Nixon ended that link — the "Nixon shock" — and since then the dollar has been pure fiat. Its value rests on: the U.S. government accepting it for taxes, U.S. law requiring it for domestic transactions, and — most importantly — the global expectation that others will continue to accept it.

The gold standard had a real virtue: it constrained the government's ability to inflate its way out of debt. The amount of money in circulation was limited by the gold stock. But it had serious costs: it prevented the monetary system from expanding in response to genuine economic growth, and it meant that recessions deepened as the money supply contracted along with the economy.

The fiat system allows monetary policy to respond flexibly. That flexibility is an enormous advantage — it's why recessions in the fiat era have been significantly shorter and shallower than in the gold-standard era — but it requires institutional credibility. The value of fiat money is, at bottom, a self-confirming equilibrium: people accept dollars because they expect others to accept them. The expectation sustains itself as long as the central bank maintains inflation roughly as promised and the government remains functional. When either breaks — as in Weimar Germany, Zimbabwe, or Venezuela — the equilibrium can collapse very fast.

---

## Measuring the money supply

The U.S. tracks money supply in two main aggregates.

**M1** includes the most liquid forms: currency in circulation (bills and coins held by the public), demand deposits (checking accounts), and other deposits that can be spent immediately. These are the forms of money you'd use to buy something today.

**M2** includes everything in M1 plus less liquid but still money-like assets: savings accounts, money-market deposit accounts, small certificates of deposit, and retail money-market mutual funds. These take a little more time to convert to spending money — days rather than years — but they're part of the money supply in a broader sense.

As of the mid-2020s, U.S. M1 is roughly $18 trillion; M2 is roughly $21 trillion. These numbers dwarf the currency in physical circulation (about $2 trillion), which reflects the central role of bank deposits in the actual money supply.

The Federal Reserve uses these measures — along with velocity, credit growth, and other indicators — to track and influence the amount of money in the economy. How it does that is Chapter 28's subject.

<!-- → [TABLE: M1 and M2 money supply measures — columns: Component | M1? | M2? | Approx. U.S. amount (mid-2020s) | Liquidity; rows: Physical currency in circulation / Yes / Yes / ~$2 trillion / Instantly liquid; Demand deposits (checking accounts) / Yes / Yes / ~$5 trillion / Instantly liquid; Other checkable deposits / Yes / Yes / ~$4 trillion / Instantly liquid; Savings and money-market deposit accounts / No / Yes / ~$10 trillion / Days to access; Small CDs under $100K / No / Yes / ~$0.5 trillion / Weeks to access; Retail money-market mutual funds / No / Yes / ~$1 trillion / Days to access; M1 total / — / — / ~$18 trillion / Immediately spendable; M2 total / — / — / ~$21 trillion / Broadly liquid; caption: "M1 is what you can spend today. M2 adds things you can spend in a few days. Both are dwarfed by the credit economy they support."] -->

---

## Banks as intermediaries

A commercial bank does two things simultaneously, and the combination is what makes banking distinctive.

**It accepts deposits.** Households and firms deposit cash, which the bank owes back on demand or with notice. The bank pays depositors interest.

**It makes loans.** The bank lends out most of those deposits to borrowers — mortgages, business loans, car loans, credit cards. The bank charges interest on loans, higher than what it pays depositors. The spread is its gross margin.

This is **financial intermediation**: the bank bridges savers and borrowers. Savers want safety and liquidity; they can withdraw whenever they need the money. Borrowers want long-term capital at reasonable rates. The bank provides both by aggregating many depositors (whose withdrawals are individually unpredictable but collectively stable), taking on the credit-evaluation work, and earning the spread.

The crucial feature: banks lend out *most* but not *all* of their deposits. They keep a fraction in reserve — cash on hand and deposits at the central bank — available to meet withdrawal requests. This is **fractional-reserve banking**. The reserve fraction has historically been around 10 percent in the U.S., though the Federal Reserve eliminated formal reserve requirements in 2020, relying instead on capital requirements and other regulatory tools to ensure adequate liquidity.

---

## How banks create money

Here is the genuinely surprising part of this chapter. Through fractional-reserve banking, *the banking system collectively creates money well beyond what the central bank has printed*.

Walk through it step by step.

The Federal Reserve creates $1,000 in new currency — the "monetary base" — and it ends up deposited at Bank A. Bank A keeps 10% ($100) in reserve and lends out $900. The borrower spends the $900, which ends up deposited at Bank B. Bank B keeps 10% ($90) and lends out $810. That $810 gets deposited at Bank C, which keeps $81 and lends out $729. And so on.

The total deposits created:

$$\$1{,}000 + \$900 + \$810 + \$729 + \cdots = \frac{\$1{,}000}{0.10} = \$10{,}000$$

Started with $1,000 of new central-bank money. Ended with $10,000 of bank-deposit money. The simple **money multiplier** is $1/r$ where $r$ is the reserve ratio. With $r = 0.10$, the multiplier is 10.

This isn't magic or fraud. It's a logical consequence of the fractional-reserve structure. Each dollar deposited gives the bank the ability to lend most of it; each loan becomes a new deposit somewhere; each new deposit gives another bank the ability to lend. The same dollar is the foundation for many simultaneous deposits, each backed by a fraction of the last.

The actual money multiplier is substantially smaller than the simple $1/r$ formula for several reasons. Banks hold excess reserves (more than required — substantially so since 2008). People hold some money in cash rather than depositing it, breaking the deposit-chain. Some loans are repaid rather than immediately re-deposited.

Since 2008, the Federal Reserve has expanded the monetary base enormously — from roughly $800 billion to several trillion dollars — partly to support the banking system. But banks have held most of this as excess reserves rather than lending it out. As a result, M2 has grown much less than the simple multiplier formula would predict, and the feared inflation didn't materialize. The money multiplier — the ratio of broad money to the monetary base — has been near 1 through much of the post-2008 period, compared to historical values around 8–10.

This is a real limitation of the textbook model: the simple multiplier formula captures the mechanics but not the behavior. Banks lend when they see creditworthy borrowers at acceptable risk, not simply because they have reserves to lend. The distinction matters for understanding monetary policy.

<!-- → [DIAGRAM: Money creation cascade — vertical flow diagram; top box: "Fed creates $1,000 monetary base"; arrow down to "Bank A: keeps $100 (10%) in reserve, lends $900"; arrow down to "Bank B: keeps $90 in reserve, lends $810"; arrow down to "Bank C: keeps $81 in reserve, lends $729"; ellipsis showing continuation; bottom box: "Total deposits = $10,000 (with 10% reserve ratio)"; sidebar annotation: "Simple multiplier = 1/r = 10"; second sidebar: "Post-2008 actual multiplier ≈ 1 (excess reserves held instead of lent)"; caption: "The mechanical cascade assumes every loan becomes a deposit that gets lent again. Post-2008, banks held the reserves instead — breaking the chain."] -->

---

## Reading a bank balance sheet

A bank's balance sheet has the same structure as any business: assets equal liabilities plus equity.

**Assets** include:
- *Reserves* — cash on hand and deposits at the Federal Reserve. Liquid, safe, low-return.
- *Loans* — the bank's primary earning asset. Mortgages, business loans, consumer credit. Higher return, higher risk.
- *Securities* — Treasury bonds, mortgage-backed securities, corporate bonds. Between reserves and loans in liquidity and risk.
- *Other assets* — bank branches, equipment, software.

**Liabilities** include:
- *Deposits* — checking accounts, savings accounts, certificates of deposit. The bank owes these back to depositors.
- *Borrowings* — from other banks in the overnight lending market (fed funds), from the Federal Reserve (discount window), from bond issuance.

**Equity** is the difference: assets minus liabilities. It's the bank's own capital, the buffer that absorbs losses before depositors are affected.

A simple example. A bank with $1 billion in deposits borrows $100 million from other banks and has $100 million of equity. Total liabilities plus equity: $1.2 billion. Total assets: $120 million in reserves, $1 billion in loans, $80 million in securities. Now suppose 6% of the loans go bad — $60 million of loan losses. The losses hit equity: $100 million of equity becomes $40 million. Depositors are still fully protected. If losses instead reach 10% ($100 million), equity is wiped out. The bank is technically insolvent.

This is why capital requirements matter. Higher capital requirements force banks to hold more equity relative to assets, meaning they can absorb larger loan losses before becoming insolvent. Lower requirements allow more lending (and higher returns on equity) at the cost of more fragility.

<!-- → [TABLE: Bank balance sheet — two-column T-account format; Assets side: Reserves (Fed deposits + vault cash) $120M; Loans (mortgages, business, consumer) $1,000M; Securities (Treasuries, MBS) $80M; Total assets $1,200M; Liabilities + Equity side: Deposits (checking + savings + CDs) $1,000M; Borrowings (fed funds, discount window) $100M; Equity (capital) $100M; Total liabilities + equity $1,200M; second version showing after 6% loan loss: Loans $940M, Total assets $1,140M; Equity falls to $40M; annotation: "Depositors still protected"; caption: "The equity is the buffer. At 10% loan loss in this example, equity = 0 and the bank is insolvent. Capital requirements set the minimum buffer."] -->

---

## Bank runs and deposit insurance

Fractional-reserve banking has a structural vulnerability: deposits are payable on demand, but loans are long-term. If many depositors try to withdraw at the same time, the bank can't liquidate its loans fast enough to meet the demand. A bank with sound long-term assets can fail because of a short-term liquidity mismatch.

Worse, bank runs can be self-fulfilling. If depositors think a bank is at risk and rush to withdraw, they create the very crisis they feared — the sudden demand for cash forces the bank to sell assets at fire-sale prices, deepening its losses. Fear spreads to other banks. Other depositors run. The system destabilizes.

This is not a hypothetical. Between 1930 and 1933, roughly 9,000 U.S. banks closed, taking $7 billion in deposits with them. Depositors who panicked first got their money; depositors who waited lost everything. The incentive to run, once enough others are running, is overwhelming.

The institutional response is **deposit insurance**. The Federal Deposit Insurance Corporation (FDIC), created in 1933, guarantees bank deposits up to $250,000 per depositor per institution. With that guarantee in place, an individual depositor has no reason to panic. Their money is safe regardless of what other depositors do. Bank runs in the FDIC era are rare precisely because deposit insurance eliminates the coordination problem that makes runs self-fulfilling.

The trade-off is moral hazard. Insured depositors don't care what risks their bank takes — they'll be made whole regardless. Banks, knowing depositors won't run even if the bank takes on more risk, may take more risk than they otherwise would. The regulatory response — capital requirements, supervision, stress tests, resolution authority — is the institutional attempt to check this moral hazard without eliminating deposit insurance. Chapter 28 covers these tools in more detail.

---

## Synthesis

Pull back. Money is a social institution — it exists and has value because people accept it. Its functions (medium of exchange, unit of account, store of value, deferred payment standard) are what make it valuable, not the material it's made of. Fiat money works as well as commodity money when the institutional credibility holds and better than commodity money when the economy needs flexible monetary policy.

Banks intermediate between savers and borrowers, accepting short-term deposits and making longer-term loans, earning the spread, bearing the credit risk. Fractional-reserve banking multiplies the money supply: the banking system collectively creates deposits many times the monetary base the central bank has created. The simple money multiplier is $1/r$; the actual multiplier is smaller and depends on banks' willingness to lend and the public's willingness to borrow and deposit.

Bank balance sheets capture the assets (reserves, loans, securities) and liabilities (deposits, borrowings) with equity as the buffer. The equity buffer determines how much loan loss the bank can absorb before failing.

Bank runs are a structural vulnerability, corrected in the FDIC era by deposit insurance — but deposit insurance creates moral hazard, which requires capital requirements and supervision as checks.

The system that results has substantially reduced the frequency of bank panics since the 1930s. It is not panic-free: the savings-and-loan crisis of the 1980s and the 2008 financial crisis both tested the institutional plumbing hard. But the collapses of 2008 were resolved in months, not the years it took to recover from the 1930s bank-failure cascade. The difference is the institutional architecture: deposit insurance, central-bank liquidity provision, capital requirements, resolution authority. The plumbing works until it doesn't, and understanding the plumbing is the prerequisite for understanding when and why it fails.

---

## Exercises

**Warm-up**

*1. The four functions as diagnostic.* For each scenario, identify which function of money is being fulfilled — and whether a second function is also in play: (a) You pay for groceries with a $20 bill; (b) A contractor quotes a kitchen renovation at $45,000; (c) You hold $3,000 in a checking account as an emergency fund; (d) You sign a 30-year fixed-rate mortgage at 6.5%; (e) Zimbabwe's government in 2008 printed trillion-dollar notes. For (e), state which function has broken down and which is still functioning. *(Tests: applying the four functions to real cases; distinguishing which function fails first under hyperinflation.)*

*2. Commodity vs. fiat.* (a) When the U.S. was on the gold standard, what limited the Fed's ability to expand the money supply in a recession? (b) After 1971, what constrains the Fed's ability to expand the money supply? (c) If the U.S. returned to the gold standard today, what would happen to the Fed's ability to respond to the 2008–2009 financial crisis? (d) What is the one genuine advantage of commodity money over fiat money, and what is its cost? *(Tests: the gold standard vs. fiat trade-off; connecting institutional structure to macroeconomic policy capacity.)*

*3. Money multiplier arithmetic.* The central bank creates $2,000 in new base money. The reserve ratio is 20%. (a) Using the simple multiplier formula, calculate the total deposits the banking system can create. (b) Trace the first three rounds of deposit creation explicitly. (c) If people hold 15% of their money in cash rather than depositing it, how does this reduce the actual multiplier? (d) After the 2008 financial crisis, U.S. banks held large excess reserves. What effect did this have on the actual money multiplier, and why didn't the Fed's massive base expansion produce proportional M2 growth? *(Tests: computing the multiplier; identifying the cash-holding and excess-reserve leakages; connecting to post-2008 experience.)*

**Application**

*4. Build and stress-test a bank balance sheet.* A community bank has the following: deposits of $800 million (90% of its liabilities); it borrowed $50 million from other banks; total equity is $50 million; it keeps 8% of deposits in reserves, holds 65% of deposits in loans, and the rest in Treasury securities. (a) Construct the full balance sheet and verify it balances. (b) 7% of loans default. What happens to equity? (c) 12% of loans default. What happens, and what does the FDIC now face? (d) What equity-to-assets ratio would have allowed the bank to survive a 12% loan loss? *(Tests: constructing a balance sheet; calculating the equity buffer under different loss scenarios; connecting capital requirements to failure threshold.)*

*5. Bank run game theory.* A bank has $500 million in deposits and $50 million in reserves (10% reserve ratio). Its loans are long-term and cannot be liquidated quickly. 300 depositors each have $1 million on deposit. (a) If each depositor believes the bank is sound, does any individual have an incentive to run? (b) If each depositor believes 50% of other depositors will run, what is each individual's best strategy? Show why the run becomes self-fulfilling. (c) How does FDIC insurance change the game? (d) Why does FDIC insurance eliminate the bank run incentive even though the bank still has a maturity mismatch? *(Tests: the game-theory structure of bank runs; why deposit insurance is a solution to a coordination problem, not just an insurance product.)*

*6. Fiat credibility.* In 2022, Turkey's central bank cut interest rates while inflation was running above 80% — opposite to standard monetary policy. (a) What happened to the Turkish lira's exchange rate relative to the dollar? (b) Which function of money was most directly impaired? (c) Why might Turkish citizens have held their savings in dollars or gold rather than lira even though lira were required for local transactions? (d) What does this tell you about the conditions under which fiat money maintains its value as a store of value vs. only as a medium of exchange? *(Tests: applying the fiat credibility framework to a real contemporary case; distinguishing the functions that fail at different inflation rates.)*

**Synthesis**

*7. The money multiplier in two eras.* In 2006, the U.S. monetary base was roughly $800 billion and M2 was roughly $6.7 trillion — implying an actual money multiplier of about 8.4. By 2014, the monetary base had grown to $4 trillion and M2 was $11.5 trillion — implying a multiplier of about 2.9. (a) What explains the collapse of the actual money multiplier from 2008 onward? Name at least two specific mechanisms. (b) The Fed was worried about inflation when it expanded the base — why didn't inflation materialize? (c) What does this imply about the relationship between monetary base expansion and M2 growth in the modern banking environment? *(Tests: connecting the post-2008 evidence to the excess-reserves mechanism; understanding the limits of the simple multiplier model.)*

*8. Deposit insurance and moral hazard.* Before the FDIC, bank depositors monitored their bank's risk-taking because they stood to lose money if the bank failed. After deposit insurance, insured depositors have less reason to monitor. (a) Why might banks take on more risk when depositors don't monitor? (b) Capital requirements are the standard regulatory response to deposit-insurance moral hazard — explain the mechanism. (c) During the 2008 financial crisis, many of the riskiest positions were taken by banks that were well-capitalized by regulatory standards. What does this suggest about the limits of capital requirements as a moral-hazard check? *(Tests: the moral-hazard chain from deposit insurance to risk-taking; the regulatory response; the limits of that response.)*

**Challenge**

*9. Crypto as money.* Bitcoin is designed with a fixed supply (21 million coins maximum) and no central authority. (a) Evaluate Bitcoin against each of the four functions of money, naming specifically where it succeeds and fails today. (b) The fixed supply is designed to prevent inflation. In terms of the gold standard analogy, what would a world where Bitcoin is the primary currency do to monetary policy during recessions? (c) Suppose a government wanted to use Bitcoin as its official currency (El Salvador tried this in 2021). What specific problems would arise for each of the four monetary functions? *(Tests: applying the four-function framework to a novel monetary instrument; connecting the fixed-supply property to macroeconomic policy constraints.)*

*10. When the plumbing fails.* The chapter closes by noting that the 2008 crisis was "resolved in months, not years" compared to the 1930s cascade. (a) What specific institutional features — built after the 1930s — prevented the 2008 collapse from becoming a 1930s-scale disaster? Name at least three. (b) The 2023 Silicon Valley Bank failure is a case where a bank with apparently good capital ratios still failed rapidly. What feature of SVB's balance sheet created the vulnerability that the standard capital requirements didn't catch? (c) Does SVB's failure suggest the institutional architecture is still incomplete, or was it a case of regulatory enforcement failure rather than design failure? *(Tests: connecting the chapter's institutional history to recent events; identifying a specific gap in the post-2008 framework.)*

---

## LLM Exercises

**Exercise 1 — Trace the money multiplier.** Tell an LLM the central bank prints $5,000 in new currency. With a 5% reserve requirement, walk through the multiplier process for at least 5 rounds. Compute the total deposits created. Verify by hand using the formula. Why might the actual deposits be smaller?

**Exercise 2 — Build a simple bank balance sheet.** Tell an LLM to construct a hypothetical bank with $500M deposits, $50M equity, and a 10% reserve ratio. Allocate the assets between reserves, loans, and securities. Then introduce a 5% loan loss and show what happens to equity. The exercise teaches the structure visually.

**Exercise 3 — Diagnose money creation.** Ask an LLM why the simple money multiplier formula (1/reserve ratio) does not match actual U.S. monetary aggregates. The answer should engage with excess reserves, cash holdings, and the post-2008 regulatory environment.

**Exercise 4 — Trace a bank run.** Walk an LLM through what happens when 30% of a bank's depositors try to withdraw their money on the same day. The bank has 10% reserves. Push: what does the bank do, and what does the FDIC do?

**Exercise 5 — Crypto vs. fiat.** Ask an LLM to evaluate Bitcoin as money using the four functions. Where does it succeed (store of value? deferred payment standard?) and where does it fail (medium of exchange?)?

---

## LLM Exercise — Chapter 27: Money and Banking (Policy Brief Project)

**Project:** Policy Brief.  
**What you're building this chapter:** the monetary-system implications — does your policy interact with money supply, banking, or financial-system stability?  
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 27 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 27 taught: what money does (medium of exchange,
unit of account, store of value, standard of deferred payment);
fiat vs. commodity money; the money-supply measures (M1 = currency
+ demand deposits; M2 adds savings deposits and money-market funds);
banks as intermediaries (matching savers and borrowers, transforming
maturity, transforming risk); how banks create money through
fractional-reserve lending (the deposit multiplier); reading a bank
balance sheet; bank runs and deposit insurance.

Write the brief's "Money and Banking Implications" section in
300–500 words.

1. **Direct monetary-system interaction.** Does your policy interact
   directly with money or banks? Most non-financial policies don't.
   But a policy funded by deficit issuance affects bond markets;
   a policy that affects bank profitability affects credit supply;
   a policy that touches deposit insurance, capital requirements,
   or payment systems is direct monetary-policy territory.

2. **Indirect interaction via credit channels.** Even non-financial
   policies often work through credit. A change in firm
   profitability shifts loan demand; a change in household income
   shifts loan supply (savings) and demand (borrowing). Trace the
   credit-channel effect of your policy.

3. **Financial-stability implications.** Some policies create or
   reduce financial-stability risk. Mortgage interventions, bank
   regulation, deposit-insurance design, repo-market structure —
   all bear on stability. If your policy is in any of these
   neighborhoods, name the stability implication.

End with one sentence on whether the policy's monetary-system
effects are first-order (the policy is fundamentally about money/
banking) or second-order (the policy affects money/banking
incidentally). Most policies are second-order; the brief should
not overclaim.
```

---

**What this produces:** A 300–500 word section on the monetary and banking-system implications. For most policies this is a small section; for financial-regulation or fiscal-funding policies, it's central.

**How to adapt this prompt:**

- *For your own project:* Most policies: this is a brief paragraph. UBI students: macro-significant effect on demand for currency and deposits if funded by money creation. Antitrust on big tech: small monetary effects but large effects on payment-system competition.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 17's financial-markets analysis fed this; Ch 27 zooms in on the banking-system layer specifically.

**Preview of next chapter:** Chapter 28 covers monetary policy — the Fed's tools, expansionary vs. contractionary policy, the zero lower bound. If your policy will produce a Fed response (any macro-significant policy will), the next chapter names it.

---

## AI Wayback Machine

**Walter Bagehot** was a 19th-century British journalist and economist whose *Lombard Street* (1873) defined the central bank's role as lender of last resort — arguing that in a crisis a central bank should lend freely to solvent institutions against good collateral at a penalty rate, a doctrine that still guides modern crisis response.

![Walter Bagehot](../images/walter-bagehot-u97.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Walter Bagehot, and how does his "lender of last resort"
doctrine connect to money and banking we covered in this chapter?
Keep it to three paragraphs. End with the single most surprising
thing about his career or ideas.
```

→ Search **"Walter Bagehot"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Bagehot's rule ("lend freely against good collateral, at a penalty rate") to a modern financial crisis.
- Add a constraint: "Answer including modern criticisms of the Bagehot framework."

What changes? What gets better? What gets worse?

---

*Byline: Nik Bear Brown.*
