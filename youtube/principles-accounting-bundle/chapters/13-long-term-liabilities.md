# Chapter 13 — Long-Term Liabilities

## 13.1 Opening: Borrowing for the long haul

A company building a new manufacturing facility needs $50 million in capital. Its short-term credit lines are inappropriate — the project will take three years to build and another decade to pay off through generated cash flow. The company needs *long-term* financing: a multi-year loan, a commercial mortgage, a bond issuance to public investors. Each instrument creates a long-term liability — an obligation due more than a year out — with structural features that distinguish it from the current liabilities of Chapter 12.

This chapter is about long-term liabilities — bonds payable, long-term notes payable, mortgages, lease liabilities. The accounting mechanics get more involved than the current-liability cases, because long-term obligations require *present-value* mathematics: the time value of money cannot be ignored when payments are spread over decades. The core concepts — issuance, periodic interest, premium and discount amortization, retirement — all flow from one principle: long-term debt is recorded at its *present value at issuance*, and the difference between present value and face value is recognized as interest expense over the life of the debt.

By the end of this chapter, you should be able to:

- Distinguish bonds, long-term notes, mortgages, and lease liabilities as financing instruments.
- Compute the *issue price* of a bond using the present value of its cash flows.
- Journalize bond issuance at par, at a discount, or at a premium.
- Apply the *effective-interest method* to amortize bond discount or premium across the bond's life.
- Journalize bond retirement at maturity and early extinguishment.
- Distinguish *operating leases* from *finance leases* under current GAAP, and identify the balance-sheet impact of each.
- Recognize how *deferred tax liabilities* arise from timing differences between book income and taxable income.

## 13.2 Bonds, notes, mortgages, and leases

*Bonds payable* are debt instruments issued to investors, typically in $1,000 face-value increments, with stated interest rates and maturity dates that can range from 5 years to 30 years or more. Bonds are usually publicly traded after issuance, so their market price moves continuously with interest rates. A company issuing bonds typically does so through an investment bank that underwrites the offering and distributes the bonds to institutional investors.

*Long-term notes payable* are private debt instruments — a company borrows from a bank or a small group of lenders, signing a note with stated principal, interest rate, and maturity. Less liquid than bonds; often used by mid-sized companies that don't access public bond markets.

*Mortgages payable* are notes secured by real estate. Common for real-estate-heavy companies or for any business buying property with debt financing. Typical amortization schedule combines interest and principal in fixed monthly payments over a 15-30 year term.

*Lease liabilities* — current GAAP (ASC 842, effective 2019) requires most leases to be recognized as both a *right-of-use asset* and a *lease liability* on the balance sheet, even for what used to be called operating leases. The balance-sheet impact is now substantial: companies that lease their stores, vehicles, or equipment now show those obligations as long-term liabilities.

The structural common feature: each of these instruments commits the company to a stream of future cash payments — interest and/or principal — over multiple years. Each is recorded on the balance sheet as a long-term liability and amortized over time. The mechanics differ; the structural concept is the same.

## 13.3 Bond pricing: present value of cash flows

A bond's *issue price* is the present value of the cash flows the bond will pay to the investor — coupon interest payments plus the principal at maturity — discounted at the *market interest rate* applicable when the bond is issued.

Suppose a company issues a $100,000 face-value bond, 10-year maturity, 5% stated (coupon) annual interest paid annually, when the market interest rate is also 5%. The cash flows the bond will pay an investor: $5,000 in interest each year for 10 years, plus $100,000 of principal at maturity.

Present value of the interest stream (annuity of $5,000 for 10 years at 5%): approximately $5,000 × 7.722 (PV annuity factor) = $38,609.

Present value of the principal ($100,000 in 10 years at 5%): $100,000 × 0.6139 = $61,391.

Total issue price: $38,609 + $61,391 = $100,000. The bond issues *at par* — face value equals issue price — because the stated rate equals the market rate.

Now suppose market interest rates have risen to 6% by the time the company issues. Same bond, $100,000 face, 5% stated, 10 years. The investor demands a 6% return; she'll pay only what discounts the cash flows at 6%:

Interest annuity: $5,000 × 7.360 = $36,800
Principal PV: $100,000 × 0.5584 = $55,840
Total issue price: $36,800 + $55,840 = $92,640

The bond issues at a *discount* — issue price ($92,640) is less than face value ($100,000). The company receives less cash up front, but its obligation at maturity is still the full $100,000.

Conversely, if market rates have dropped to 4% when the bond is issued:

Interest annuity: $5,000 × 8.111 = $40,555
Principal PV: $100,000 × 0.6756 = $67,560
Total issue price: $108,115 (approximately)

The bond issues at a *premium*. The investor pays more than face for a bond paying above-market interest.

The structural rule: **stated rate < market rate → discount; stated rate > market rate → premium; stated rate = market rate → par.**

## 13.4 Journalizing bond issuance

**At par:** the simple case.

| Account | Debit | Credit |
|---|---|---|
| Cash | $100,000 | |
| Bonds Payable | | $100,000 |

**At a discount** ($92,640 received on $100,000 face):

| Account | Debit | Credit |
|---|---|---|
| Cash | $92,640 | |
| Discount on Bonds Payable | $7,360 | |
| Bonds Payable | | $100,000 |

The Discount on Bonds Payable is a *contra-liability* account. On the balance sheet it appears as a deduction from Bonds Payable, producing a net carrying value of $92,640 — the actual cash received. The discount will be *amortized* over the life of the bond, increasing interest expense each period.

**At a premium** ($108,115 received):

| Account | Debit | Credit |
|---|---|---|
| Cash | $108,115 | |
| Premium on Bonds Payable | | $8,115 |
| Bonds Payable | | $100,000 |

The Premium on Bonds Payable is added to Bonds Payable on the balance sheet, producing a net carrying value of $108,115. The premium is amortized over the bond's life, *reducing* interest expense each period (since the company received more cash than the face it owes, and the difference is essentially a bonus that offsets future interest cost).

## 13.5 Effective-interest method of amortization

The discount or premium gets amortized over the bond's life so that, by maturity, the bond's carrying value equals face value. Two methods exist; under U.S. GAAP, the *effective-interest method* is required for any material discount or premium.

The mechanics: each period, interest expense is computed as carrying value × market rate. Cash interest paid is fixed at face × stated rate. The difference is the amortization of discount or premium.

For our discount bond ($92,640 issue price, $100,000 face, 5% stated, 6% market, 10 years annual interest):

**Year 1:**
- Cash interest paid: $100,000 × 5% = $5,000
- Interest expense: $92,640 × 6% = $5,558
- Discount amortization: $5,558 − $5,000 = $558

| Account | Debit | Credit |
|---|---|---|
| Interest Expense | $5,558 | |
| Discount on Bonds Payable | | $558 |
| Cash | | $5,000 |

After Year 1, carrying value = $92,640 + $558 = $93,198.

**Year 2:**
- Interest expense: $93,198 × 6% = $5,592
- Cash interest: $5,000
- Discount amortization: $592

After Year 2, carrying value = $93,198 + $592 = $93,790.

The pattern continues. Each year, interest expense is slightly larger (because carrying value is rising). By Year 10, carrying value reaches $100,000 and the final amortization brings the discount to zero. The principal is paid at maturity and the bond is retired.

For premium bonds, the mechanics are mirror-image — interest expense is *less* than cash interest each period, and the premium amortizes downward.

The trade-off in the effective-interest method: it reflects the *true economic* interest expense each period (the rate that actually equates the bond's cash flows to its carrying value), at the cost of slightly more complex bookkeeping than straight-line amortization. Straight-line is permitted under GAAP only if results are not materially different from effective-interest.

## 13.6 Bond retirement

**At maturity:** straightforward. The carrying value equals face value (after full amortization). The company pays principal:

| Account | Debit | Credit |
|---|---|---|
| Bonds Payable | $100,000 | |
| Cash | | $100,000 |

**Early extinguishment:** if the company buys back its bonds in the open market before maturity, the gain or loss equals the difference between the carrying value (face less unamortized discount, or face plus unamortized premium) and the cash paid to retire.

Suppose at the end of Year 6 the company retires the discount bond above by paying $96,000 (perhaps because interest rates have risen further and the bond can be bought back below par). The carrying value at end of Year 6 (after six years of amortization) might be $96,800. Cash paid is $96,000. Gain: $800.

| Account | Debit | Credit |
|---|---|---|
| Bonds Payable | $100,000 | |
| Cash | | $96,000 |
| Discount on Bonds Payable | | $3,200 |
| Gain on Bond Retirement | | $800 |

(The $3,200 is unamortized discount that gets written off at retirement.)

Early extinguishment gains and losses appear on the income statement, often as an "Other Gain/Loss" line, sometimes broken out separately if material.

## 13.7 Lease accounting under ASC 842

Leases were historically split into two categories: *operating leases* (kept off the balance sheet — only the periodic rent expense was recognized) and *capital leases* (recognized on balance sheet as both an asset and liability). Off-balance-sheet operating leases were a significant analytical concern — companies could effectively finance assets through long-term operating-lease commitments without showing the obligation on the books.

ASC 842, effective 2019 for public companies and 2022 for private companies, brought most leases onto the balance sheet. Two categories remain:

*Finance leases* — economically equivalent to a financed purchase. The lessee recognizes a *right-of-use asset* and a *lease liability* at the present value of lease payments. Interest expense and amortization expense are recognized separately on the income statement.

*Operating leases* — the lessee recognizes a right-of-use asset and a lease liability (same as finance lease at inception), but expense is recognized on a straight-line basis as a single lease expense, rather than separately as interest and amortization.

The balance-sheet impact for many companies was substantial — retailers like Walgreens, Target, and Starbucks added billions of dollars of right-of-use assets and lease liabilities when ASC 842 took effect, even though their underlying business hadn't changed. The transparency improvement is real: balance-sheet readers can now see the long-term commitment magnitude that was previously buried in lease-disclosure footnotes.

The mechanics of right-of-use asset and lease liability accounting parallel those of bonds — present value of future payments at lease inception, periodic amortization of the asset and reduction of the liability, interest accrual on the liability balance. We won't develop the full mechanics here; intermediate accounting courses cover them in detail.

## 13.8 Deferred tax liabilities

A subtle long-term liability category arising from differences between *book income* (per GAAP) and *taxable income* (per the IRS code). Book and tax accounting often differ on timing — depreciation methods, bad-debt allowances, prepaid expenses, warranty accruals. When book income exceeds taxable income because of timing differences (e.g., faster depreciation for tax purposes than for books), the company will eventually owe more tax in future periods when the timing reverses. That future obligation is recorded as a *deferred tax liability*.

Conversely, a *deferred tax asset* arises when taxable income exceeds book income because of timing differences — the company has prepaid tax that will reduce future tax obligations.

The mechanics involve scheduling out timing differences, applying expected future tax rates, and computing the resulting deferred tax accounts. Deferred-tax accounting is one of the more complex areas of financial reporting — intermediate accounting courses devote a full chapter to it, and tax-accountants spend careers on it. For this introductory chapter, the conceptual point is enough: deferred tax liabilities are real obligations arising from timing differences in how book and tax accounting treat the same economic events.

## 13.9 Exercises

### Warm-up

1. **Distinguish bonds, long-term notes, and mortgages** in one sentence each.

2. **Why does a bond issue at a discount when the market rate exceeds the stated rate?**

3. **Distinguish a finance lease from an operating lease under ASC 842.**

### Application

4. **A company issues $200,000 of 5-year, 6% bonds when market rates are 7%.** Without computing the exact PV (assume issue price is $191,800), journalize the issuance.

5. **In Year 1 the same bond's discount amortization is $1,300.** Journalize the annual interest entry under the effective-interest method.

6. **A company retires $300,000 face of bonds with $4,800 of unamortized discount remaining for a cash payment of $295,000.** Journalize the retirement.

### Synthesis

7. **A company is choosing between issuing 10-year bonds and taking a 10-year mortgage from a bank for a real-estate purchase.** Discuss what considerations should drive the choice. What are the trade-offs in terms of cost, flexibility, and balance-sheet presentation?

8. **The 2019 transition to ASC 842 added billions to many companies' balance sheets without changing their underlying operations.** Explain what the standard fixed and what kind of analyst behavior had to change after the transition.

### Challenge

9. **A bond issued at par carries a 6% stated rate. Five years later, market rates have dropped to 4%.** What happens to the bond's market price (not carrying value)? Why might the issuer want to retire it early? What gain or loss would the issuer recognize on early retirement, and from whose perspective is it a gain or loss?

10. **Deferred tax liabilities are real obligations but arise from timing differences, not from cash transactions.** Discuss how a deferred tax liability differs structurally from a current income tax payable, and why both belong on the balance sheet.

## 13.10 Chapter summary

You walked into this chapter with current liabilities. You walk out with the long-term obligations that finance major business operations.

Long-term liabilities include bonds payable, long-term notes payable, mortgages payable, lease liabilities (right-of-use), and deferred tax liabilities. The accounting mechanics depend on present-value mathematics: the long-term obligation is recorded at the present value of its future cash flows, discounted at the market interest rate at issuance. The difference between present value (carrying value) and face value is the discount or premium, amortized over the instrument's life under the effective-interest method.

Bonds are public debt instruments; long-term notes and mortgages are typically private. ASC 842 brought most leases onto the balance sheet starting in 2019, materially expanding many companies' reported liabilities. Deferred tax liabilities arise from timing differences between book and taxable income.

The single most important idea: long-term liabilities are recorded at their *economic* value (present value), not at their *legal face value*. The difference flows through interest expense over the life of the obligation, ensuring that the income statement reflects the true cost of borrowing each period rather than the artificial coupon rate.

The common mistake to watch for: treating bond discount or premium as a one-time gain or loss at issuance. It's neither — it's a deferred adjustment to interest expense that gets recognized over the life of the bond.

## 13.11 Why companies issue bonds rather than borrowing from a bank

A practical question: when a company needs $100 million of long-term financing, why might it issue bonds to public investors rather than just taking a $100 million loan from a bank?

Three common reasons.

*Cost*. Public bond markets often offer lower interest rates than bank loans, especially for large issuances and creditworthy issuers. The bond market aggregates many small investors, each providing a slice of the financing; banks have to set rates high enough to compensate for concentration risk. For a Fortune 500 company, public bonds are usually cheaper.

*Size*. A $5 billion financing need exceeds the lending capacity of most banks (or requires a syndicate of banks, which is expensive to coordinate). Public bond markets can absorb $5 billion in a single offering.

*Term*. Banks typically prefer 5-to-10-year terms; bond markets routinely offer 30-year and even 100-year maturities. Long-term capital projects need long-term financing.

The trade-off is regulatory and disclosure cost. Public bond issuance triggers SEC filings, public disclosure of financial statements, and ongoing reporting obligations. The fixed cost of going public with a bond offering is in the seven figures. Below a certain offering size, the regulatory cost outweighs the rate savings. Mid-sized companies often prefer bank debt for this reason; only large issuers with substantial capital needs find the public market worth the regulatory friction.

A *private placement* is a hybrid — bonds sold to a small number of institutional investors (typically insurance companies and pension funds) without the full SEC registration of a public offering. Private placements offer some of the cost benefits of public bonds with less regulatory overhead.

## 13.12 Bond covenants and the lender's perspective

A consequential structural feature of long-term debt: the *covenants* — contractual restrictions the borrower agrees to in exchange for the loan or bond issuance. Common covenants include:

- *Maximum debt-to-equity ratio* — the borrower agrees not to issue additional debt that would push the ratio above a threshold.
- *Minimum interest coverage* — the borrower agrees to maintain operating income at some multiple of interest expense.
- *Restrictions on dividends* — the borrower agrees not to pay dividends that would impair its ability to service the debt.
- *Restrictions on asset sales* — the borrower agrees not to sell major assets without lender consent.
- *Cross-default provisions* — a default on any one obligation triggers default across all.

Covenants are negotiated; sophisticated treasurers spend substantial time on covenant terms because a covenant violation can be more expensive than the underlying debt itself. A *technical default* on a covenant — even without missing a payment — can trigger acceleration (the lender demanding immediate repayment) or higher interest rates.

The accounting consequence for a violator: any debt subject to a covenant violation that the lender hasn't waived must be reclassified as *current* on the balance sheet, even if scheduled payments are years away. The mechanism is part of the substance-over-form rule from Chapter 12: an obligation the lender can call on demand is current, regardless of stated maturity.

Covenants are often more restrictive for riskier borrowers. *Investment-grade* corporate bonds (rated BBB- or above by Standard & Poor's) typically have lighter covenants than *high-yield* (junk) bonds. The covenants and the credit rating are two faces of the same underlying credit-quality assessment.

## 13.13 Pension liabilities and other post-employment benefits

A category briefly worth flagging because of its scale at large public companies: pension obligations and other post-employment benefits (OPEB).

A *defined-benefit pension plan* commits the employer to specific retirement benefits for employees, calculated by formula (e.g., 2% × years of service × final average salary). The employer bears the investment risk — if the pension plan's invested assets earn less than expected, the employer must contribute more. The accounting recognizes a *pension liability* when the projected benefit obligation exceeds the plan's assets, and recognizes pension expense each period as employees earn additional benefits.

A *defined-contribution plan* (401(k), 403(b)) commits the employer only to specified contributions, with the employee bearing the investment risk. Defined-contribution plans don't create long-term liabilities — the employer pays its contribution each period as a current expense.

Most U.S. private-sector pension plans have shifted from defined-benefit to defined-contribution over the past forty years, partly because the long-term liability accounting for defined-benefit plans is so consequential. Public-sector pensions remain predominantly defined-benefit, which is why state and local government pension liabilities are now one of the largest balance-sheet items in government accounting.

OPEB — primarily retiree health insurance — operate similarly to defined-benefit pensions and are accounted for under similar present-value mechanics.

The mechanics of pension accounting are dense — actuarial calculations, expected return on plan assets, amortization of gains and losses — and beyond the scope of an introductory chapter. The conceptual point: long-term obligations to current and former employees are real liabilities, recognized at their present-value cost, recognized as expense as employees earn the benefit through service.

A note on disclosure. Long-term debt obligations require extensive footnote disclosure under GAAP — interest rates, maturity schedules, collateral, covenants, fair-value estimates. Reading the long-term debt footnote is essential for any analyst evaluating a company's capital structure; the balance-sheet line tells you the carrying value, but the footnote tells you the rate, timing, and risk of the underlying obligations.

## 13.14 Connections forward

Chapter 14 turns to the *equity* side of the corporate balance sheet — common stock, preferred stock, treasury stock, retained earnings, dividends, stock splits. The mechanics of equity accounting are different from liability accounting: equity holders are owners, not creditors, and their accounting reflects ownership claims rather than payment obligations.
---

## LLM Exercise — Chapter 13: Long-Term Liabilities (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** the long-term-liabilities module — bond pricing via present value, effective-interest amortization, lease accounting under ASC 842, deferred-tax liabilities.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 13 of building my AI Bookkeeping Tool. This chapter
taught: bonds (debt instruments with face value, coupon rate,
maturity); bond pricing as the present value of future cash flows
(PV of face + PV of coupon stream, at the market interest rate); bond
issuance journal entries (par if market rate = coupon; discount if
market > coupon; premium if market < coupon); effective-interest
method of amortization (interest expense = book value × market
rate; difference between cash interest paid and effective interest
amortizes discount or premium); bond retirement (early payoff —
gain or loss based on book value vs. retirement price); lease
accounting under ASC 842 (right-of-use asset + lease liability on
balance sheet for both operating and finance leases; only the
income-statement treatment differs); deferred tax liabilities
(when book income > taxable income due to temporary differences).

Extend the tool. Produce four outputs.

1. **A bond-pricing function.** Given face value, coupon rate,
   coupon period (annual/semi-annual), maturity in periods, market
   rate:
   - Compute PV of face + PV of coupon stream.
   - Return the price (and identify it as par, discount, or
     premium).
   - Generate the issuance journal entry.

2. **An effective-interest amortization-schedule generator.** A
   function that produces a full amortization schedule:
   - Date | Cash interest | Effective interest | Discount/Premium
     amortized | Book value at end.
   - Each row's journal entry:
     - Discount bond: Debit Interest Expense (book value × market
       rate), Credit Cash (face × coupon rate), Credit Discount on
       Bonds Payable (difference).
     - Premium bond: Debit Interest Expense, Debit Premium on
       Bonds Payable (difference), Credit Cash.
   - Total amortization over the life of the bond = original
     discount or premium.

3. **An ASC 842 lease module.** Functions for:
   - `record_lease_inception(lease_term, payments, discount_rate,
     classification)` — computes the lease liability as PV of
     lease payments; records right-of-use asset and lease
     liability (both equal at inception).
   - For operating leases: record single straight-line lease
     expense each period (debit Lease Expense, credit Lease
     Liability + adjust ROU).
   - For finance leases: record interest expense on lease
     liability + amortization expense on ROU asset (two separate
     entries).

4. **A deferred-tax module.** Functions for:
   - `compute_deferred_tax_liability(temporary_differences,
     tax_rate)` — when book income exceeds taxable income for
     temporary reasons (e.g., depreciation differences), the
     future tax owed gets recorded as a deferred tax liability.

Tests for each — a 5-year bond at discount, a 4-year operating
lease, a deferred-tax scenario from accelerated depreciation.

Update spec.
```

---

**What this produces:** A long-term-liabilities module that handles the present-value math that intimidates most beginners. The effective-interest amortization schedule is the most mathematically dense single feature in the tool.

**How to adapt this prompt:**

- *For your own project:* If your fictional business never plans to issue bonds, the bond module is overkill. Build it anyway — the next chapter (corporations) often references bond-or-stock financing decisions.
- *For ChatGPT / Gemini:* Works as written. The PV math is well-trained in all major models.
- *For Claude Code:* The right tool. Generate the amortization schedule and verify against an Excel PV/PMT calculation.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 4's adjusting entries included interest accrual; Ch 13 generalizes for compound effective-interest situations.

**Preview of next chapter:** Chapter 14 adds the corporate-equity module — common and preferred stock issuance, treasury stock, dividends, EPS, BVPS. The tool gains corporate-equity sophistication.


---

## AI Wayback Machine

**Sidney Davidson** was Chicago accounting theorist whose work on lease accounting reshaped how analysts treat long-term liabilities.

**Run this:**

```
Who is Sidney Davidson, and how does their work connect to long-term liabilities we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Sidney Davidson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Sidney Davidson's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Sidney Davidson's framework."

What changes? What gets better? What gets worse?
