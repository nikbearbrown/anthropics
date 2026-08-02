# Chapter 27 — Money and Banking

*What money actually is, how banks create it, and the institutional plumbing that makes the modern monetary system work.*

In some Pacific islands of the 19th century, money was made of cowrie shells. In Yap, it was carved limestone disks weighing thousands of pounds. In medieval Europe, it was coins struck from gold and silver. In post-WWII America, it was paper notes redeemable in gold (until 1971), then paper notes redeemable in nothing. In the 21st century, increasingly, it is electronic entries in bank databases — most U.S. dollars never exist in physical form at all. And in some recent corners of the digital world, money is cryptographic tokens on distributed ledgers.

The thing all these have in common: they're accepted in exchange for goods and services because *other people accept them*. This is the deep observation about money — its value is collective and conventional. Cowries, gold, paper, and bytes are all, ultimately, money because we agree they are. When that agreement breaks down (as in hyperinflation, currency reform, or political collapse), the money loses value almost overnight.

This chapter is about the institutional plumbing of money. By the end you should know the four functions money serves, the difference between commodity and fiat money, how the U.S. measures money supply (M1 vs M2), what banks do, how fractional-reserve banking creates money beyond what the central bank prints, and why bank balance sheets matter for macroeconomic stability.

**Learning objectives.** By the end you should be able to: (1) state the four functions of money; (2) distinguish commodity money from fiat money; (3) define M1 and M2 money supply; (4) explain how banks act as intermediaries and what fractional-reserve banking is; (5) calculate the simple money multiplier and use it to explain how banks create money; (6) read a basic bank balance sheet and identify reserves, loans, deposits.

**Prerequisites.** Chapter 4 (financial capital, interest rates). Chapter 17 (bonds and equity). Chapter 22 (inflation).

## What money does

Money serves four functions:

**Medium of exchange.** Money is what you use to buy things. Without money, every transaction would be barter — direct exchange of goods. Barter requires a *double coincidence of wants* — I have wheat and want wool; I need to find someone with wool who wants wheat. Money eliminates this. I sell wheat for money; someone else sells wool for money; we both buy what we want.

**Unit of account.** Money is the unit in which prices are stated and accounts are kept. A pizza is $15. A car is $30,000. A salary is $80,000. We can compare values across goods because they're all denominated in the same unit.

**Store of value.** Money holds value over time (more or less, depending on inflation). Cash held today still buys things tomorrow. (Hyperinflation breaks this, which is why people in Zimbabwe in 2008 carried groceries home in wheelbarrows of cash and switched to U.S. dollars.)

**Standard of deferred payment.** Loans, mortgages, and other future-payment contracts are stated in money. The dollar promised today is what's owed.

These functions are why money is valuable. A bank note has no intrinsic worth; its value comes entirely from these functions, plus the fact that other people accept it.

## Commodity vs. fiat

**Commodity money** has intrinsic value — it's worth something even apart from its monetary use. Gold and silver coins have value as metal that could be melted down. Cowrie shells had value as decorative items. Cigarettes were money in WWII prison camps and have value as smokes.

**Fiat money** has no intrinsic value. Paper bills, electronic balances, modern currencies. Their value comes entirely from collective acceptance and government backing.

The U.S. dollar was on a gold standard until 1971 — each dollar was redeemable in a specific amount of gold. Since then, U.S. currency has been pure fiat. The dollar has value because the U.S. government accepts it for taxes, requires it for U.S. transactions, and has institutional credibility. The fact that it's not backed by gold doesn't reduce its functional value — fiat currencies have, on average, served their functions better than gold-backed ones because monetary policy can respond to economic conditions in ways gold standards cannot.

The deep paradox of fiat money is that its value is essentially circular. People accept dollars because they expect others to accept them. Others accept them because they expect a third group to accept them. The system holds together as long as everyone keeps believing everyone else will keep believing. When that breaks (hyperinflation, currency reform), the dollar's value can collapse very quickly.

## Measuring the money supply

The U.S. tracks two main measures of money supply:

**M1** includes the most liquid forms of money:
- Currency in circulation (paper bills and coins held by the public).
- Checking-account deposits (any deposit you can write a check against).
- Other very liquid deposits (savings accounts since the early 2020s methodology change).

M1 is what most people think of as "money in immediate use."

**M2** includes M1 plus less-liquid but still money-like assets:
- Savings accounts and money-market deposit accounts.
- Small certificates of deposit (under $100,000).
- Retail money-market mutual funds.

M2 is broader; it includes everything in M1 plus things that take a few days to convert to spending money.

As of mid-2020s, U.S. M1 is about $18 trillion; M2 is about $21 trillion. The ratio between them changes over time as financial-product structures evolve.

The Federal Reserve uses these measures to track and influence the amount of money in the economy. We'll see in Chapter 28 how the Fed actually does this.

## Banks as intermediaries

A commercial bank does two things at once.

**It accepts deposits.** Households and firms deposit cash with the bank, which they can withdraw on demand or with notice. The bank pays interest on these deposits.

**It makes loans.** The bank lends out most of the deposits to borrowers (households for mortgages, firms for business loans, governments for various purposes). The bank charges interest on these loans, higher than the interest it pays on deposits. The difference is the bank's gross margin.

This is **financial intermediation**. The bank bridges between savers (depositors) and borrowers (loan customers), absorbing the credit-evaluation work, providing liquidity to depositors, and earning the spread.

The crucial insight: banks lend out *most* but not *all* of their deposits. They keep a fraction in reserve — required by regulation and by prudential business considerations. This is **fractional-reserve banking**. The reserve fraction has historically been around 10 percent in the U.S., though the Federal Reserve eliminated formal reserve requirements in 2020 and now relies on other regulatory tools to ensure bank liquidity.

## How banks create money

Here's where it gets surprising. Through fractional-reserve banking, *banks collectively create money beyond what the central bank prints*.

Walk through it. The Fed creates $1,000 in new currency and gives it to a bank. The bank deposits this with itself (it's now a deposit liability). The bank keeps 10% in reserve and lends out $900. The borrower spends the $900, which ends up deposited at another bank. That second bank keeps 10% ($90) and lends out $810. Which gets deposited at a third bank. Which keeps 10% and lends out $729.

Total deposits created: $1,000 + $900 + $810 + $729 + ... = $1,000 / 0.10 = $10,000.

Started with $1,000 of new central-bank money. Ended with $10,000 of bank-deposit money. The system multiplied the central-bank "monetary base" by 10× through repeated lending and deposit creation.

The **simple money multiplier** is 1 / reserve ratio. With a 10% reserve ratio, the multiplier is 10. With a 5% reserve ratio, the multiplier is 20.

The actual money multiplier is smaller than the simple version because:
- Banks may keep more reserves than required (excess reserves).
- People hold some of their money in cash rather than bank deposits.
- Some of the loaned money is repaid before being lent again.

In the U.S. since 2008, the actual money multiplier has been very low — sometimes near 1 — because banks have held large excess reserves rather than lending them out. This was a major reason why massive Federal Reserve expansion of the monetary base in 2008–2014 didn't produce the large M2 growth and inflation that the simple multiplier formula would have predicted.

## Reading a bank balance sheet

A bank's balance sheet has the same basic structure as any business: assets equal liabilities plus equity.

**Assets** of a bank typically include:
- **Reserves** held at the central bank (cash equivalent).
- **Loans** made to households, businesses, and governments.
- **Securities** owned (Treasury bonds, mortgage-backed securities, corporate bonds).
- **Other assets** (buildings, equipment).

**Liabilities** include:
- **Deposits** of various kinds (checking, savings, certificates of deposit).
- **Borrowings** from other banks or central bank.
- **Other obligations** (debt securities issued by the bank).

**Equity** is the difference — the bank's own capital. Required regulatory minimums (capital requirements, discussed in Chapter 28) ensure that banks have enough equity to absorb some loan losses without becoming insolvent.

A simple example. A bank with $1B in deposits, $100M in reserves, $850M in loans, $50M in securities, and $50M in other assets, must hold $50M in equity to balance. If the loans depreciate by $30M (some go bad), the equity becomes $20M. If the loans depreciate by $60M, the equity is wiped out and the bank is technically insolvent.

This is why bank capital requirements matter. Higher capital requirements mean banks can absorb more loan losses without failing. Lower capital requirements allow more lending but increase the risk of bank failure.

## Bank runs and deposit insurance

Banks face a structural vulnerability: the deposits are payable on demand (or short notice), but the loans are long-term. If many depositors decide to withdraw simultaneously (a **bank run**), the bank can't liquidate the loans fast enough and may fail.

Bank runs can be self-fulfilling. People who think a bank is at risk withdraw their money. The bank, suddenly short of liquidity, may indeed fail — confirming the original fear and triggering more withdrawals from other banks. The 1930–1933 wave of U.S. bank failures (about 9,000 banks closed, with $7B of deposits lost) was partly the result of self-reinforcing runs.

The structural response is **deposit insurance**. The Federal Deposit Insurance Corporation (FDIC), created in 1933, insures bank deposits up to a limit (currently $250,000 per depositor per bank). With insurance, depositors have no reason to run; their money is safe even if the bank fails. Bank runs in the FDIC era are rare.

The trade-off is moral hazard. Insured depositors don't care what risks their bank takes — they're going to get their money back. Banks may take more risks than they otherwise would. The regulatory response is capital requirements, supervision, and stress tests, which we'll see in Chapter 28.

## Synthesis

Pull back. Money is a social institution that exists because people accept it. It serves four functions (medium of exchange, unit of account, store of value, deferred payment standard). It can be backed by a commodity (historically gold) or by fiat (modern currencies). The U.S. tracks money supply in two main aggregates (M1 narrow, M2 broader).

Banks intermediate between savers and borrowers, accepting deposits and making loans. The fractional-reserve structure means that banks collectively create money beyond the monetary base — the simple money multiplier is 1/reserve ratio. The actual multiplier varies and has been depressed since 2008.

Bank balance sheets show the bank's assets (reserves, loans, securities), liabilities (deposits, borrowings), and equity (capital). The equity buffer determines how much loan loss the bank can absorb before failing.

Bank runs are a structural vulnerability of fractional-reserve banking. Deposit insurance is the standard response, with capital requirements and supervision as the moral-hazard checks. Together, the framework has substantially reduced the frequency of bank failures since the 1930s, with periodic exceptions (savings-and-loan crisis of the 1980s, 2008 financial crisis).

The next chapter takes up the Federal Reserve specifically — how it operates monetary policy through the banking system, the tools it uses, the constraints it faces, and how its decisions ripple through the macroeconomy.

## LLM Exercises

**Exercise 1 — Trace the money multiplier.** Tell an LLM the central bank prints $5,000 in new currency. With a 5% reserve requirement, walk through the multiplier process for at least 5 rounds. Compute the total deposits created. Verify by hand using the formula. Why might the actual deposits be smaller?

**Exercise 2 — Build a simple bank balance sheet.** Tell an LLM to construct a hypothetical bank with $500M deposits, $50M equity, and a 10% reserve ratio. Allocate the assets between reserves, loans, and securities. Then introduce a 5% loan loss and show what happens to equity. The exercise teaches the structure visually.

**Exercise 3 — Diagnose money creation.** Ask an LLM why the simple money multiplier formula (1/reserve ratio) does not match actual U.S. monetary aggregates. The answer should engage with excess reserves, cash holdings, and the post-2008 regulatory environment.

**Exercise 4 — Trace a bank run.** Walk an LLM through what happens when 30% of a bank's depositors try to withdraw their money on the same day. The bank has 10% reserves. Push: what does the bank do, and what does the FDIC do?

**Exercise 5 — Crypto vs. fiat.** Ask an LLM to evaluate Bitcoin as money using the four functions. Where does it succeed (store of value? deferred payment standard?) and where does it fail (medium of exchange?)?

## What comes next

Chapter 28 — Monetary Policy and Bank Regulation covers the Federal Reserve specifically. Chapter 29 — Exchange Rates extends the framework to international currency markets. Chapter 30 — Government Budgets and Fiscal Policy covers the fiscal side of macroeconomic policy.

**What would change my mind.** The case that the simple money multiplier captures bank money creation has weakened substantially since 2008, when the U.S. monetary base expanded enormously without producing comparable expansion of M2. The traditional textbook treatment may be outdated for the current environment. If the structural relationship between monetary base and broader money returns to its pre-2008 pattern, the framework returns to relevance; if it doesn't, the textbook needs revision.

**Still puzzling.** I do not have a clean account of why some currencies maintain credibility for long periods while others don't, despite similar institutional structures. The U.S. dollar's role as global reserve currency is a circular phenomenon — people use it because others use it — but the specific mechanisms that make a currency reach this status are not predictively understood.

*Byline: Nik Bear Brown.*
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

**Walter Bagehot** was a 19th-century British journalist whose Lombard Street (1873) defined the central bank's role as lender of last resort — the framework that still guides modern banking policy in a crisis.

**Run this:**

```
Who was Walter Bagehot, and how does his "lender of last resort" doctrine connect to money and banking we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Walter Bagehot"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Bagehot's rule ("lend freely against good collateral, at a penalty rate") to a modern financial crisis.
- Add a constraint: "Answer including modern criticisms of the Bagehot framework."

What changes? What gets better? What gets worse?
