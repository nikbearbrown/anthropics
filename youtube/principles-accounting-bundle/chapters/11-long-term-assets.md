# Chapter 11 — Long-Term Assets

## 11.1 Opening: A truck that cost $40,000 in 2018

A small distribution business buys a delivery truck on January 2, 2018, for $40,000. The truck is expected to last seven years and to be worth roughly $5,000 as scrap at the end. By December 31, 2024 — seven years later — the truck has driven 280,000 miles, hauled tens of thousands of orders, broken down twice, been repaired three times, and has finally been sold to a used-vehicle wholesaler for $4,800.

What did that truck cost the business? Forty thousand dollars in 2018 cash, sure. But seven years of revenue have been earned with the truck's help. If the entire $40,000 had been expensed in 2018, the company's 2018 net income would have shown an enormous loss while the next six years showed inflated profits — none of which would reflect the actual economic relationship between the truck and the revenue it produced.

The accounting solution is *depreciation* — the systematic allocation of the truck's $35,000 net cost ($40,000 acquisition cost minus $5,000 estimated salvage value) across the seven years of its useful life. Each year, a portion of the cost flows from the balance sheet (where it sits as an asset, reduced by accumulated depreciation) to the income statement (as depreciation expense). By December 31, 2024, the entire $35,000 has been expensed, and the truck's net carrying value on the books matches its scrap value. The disposal entry then settles the small remaining gap.

This chapter is about long-term assets — the equipment, buildings, vehicles, land, and intangibles that businesses use over multiple periods rather than sell. Depreciation is the central mechanic; its variants (straight-line, units-of-production, declining-balance) are the policy choices; intangible amortization and impairment are the close cousins.

By the end of this chapter, you should be able to:

- Identify which costs are *capitalized* into the cost of a long-term asset and which are *expensed* immediately.
- Compute depreciation under three methods: straight-line, units-of-production, and double-declining-balance.
- Journalize asset acquisition, periodic depreciation, ordinary repairs, and asset disposal (sale, retirement, exchange).
- Distinguish *depreciation* (tangible assets), *amortization* (intangible assets with finite lives), and *depletion* (natural resources).
- Apply the *impairment* test to long-term assets and journalize the resulting write-down when applicable.
- Distinguish intangible assets with *finite useful lives* (amortized) from those with *indefinite useful lives* (not amortized but tested for impairment) — including goodwill.

## 11.2 What gets capitalized: the cost of an asset

The recorded cost of a long-term asset is *all reasonable and necessary costs* to acquire the asset and prepare it for its intended use. For the truck:

- Negotiated purchase price: $38,000
- Sales tax: $2,000
- Delivery from dealer: $400
- Painting with company logo: $300
- License plates and registration (recurring annual fee): expensed, not capitalized
- Insurance (recurring annual cost): expensed, not capitalized
- Initial fuel: expensed, not capitalized

Capitalized cost: $38,000 + $2,000 + $400 + $300 = $40,700. This figure goes on the books as Equipment (or Vehicles) at acquisition. The recurring operating costs hit Operating Expenses as they're incurred.

For real estate, the principle is the same. *Land* — purchase price plus closing costs (legal fees, title search, surveying), plus the cost of getting the land ready (grading, clearing, removing existing structures, less any salvage from demolition). Land is *not depreciated* — it doesn't wear out and has indefinite useful life.

*Buildings* — purchase price (or construction cost) plus closing costs, plus any necessary improvements before placing the building in service. Buildings *are* depreciated over their estimated useful life.

*Equipment* — invoice price plus sales tax, freight, installation, testing. Equipment *is* depreciated over its useful life.

The trade-off in capitalization rules: capitalizing buys *matching of cost to the periods that benefit* at the cost of *judgment and complexity at acquisition*. Some costs are unambiguously capitalized (the invoice price); some are unambiguously expensed (a routine oil change three years later); some fall in a gray zone (a major engine overhaul that extends useful life — capitalize? a $300 brake replacement — expense?). The general rule: costs that *extend useful life or increase capacity* are capitalized; costs that *maintain* the asset in its existing condition are expensed.

## 11.3 Depreciation: three methods

Depreciation allocates the *depreciable base* — cost minus estimated salvage value — across the asset's *estimated useful life*. Three methods are common.

### Straight-line depreciation

The simplest. Equal depreciation each year over the useful life:

*Annual depreciation = (Cost − Salvage Value) / Useful Life*

For the truck: ($40,700 − $5,000) / 7 = $5,100 per year. Each year's adjusting entry:

| Account | Debit | Credit |
|---|---|---|
| Depreciation Expense — Vehicles | $5,100 | |
| Accumulated Depreciation — Vehicles | | $5,100 |

After Year 1: book value (or *net carrying value*) = $40,700 − $5,100 = $35,600. After Year 7: book value = $40,700 − $35,700 = $5,000, matching the salvage estimate.

Straight-line is overwhelmingly the most-used method for financial reporting, because it's simple, easily defensible, and produces stable expense across periods.

### Units-of-production depreciation

Depreciation tied to actual usage. Best when the asset's wear is more closely tied to use (miles driven, hours operated, units produced) than to time.

*Depreciation per unit = (Cost − Salvage Value) / Total Estimated Units of Production*
*Annual depreciation = Depreciation per Unit × Units Produced This Period*

For the truck, suppose total expected lifetime miles is 350,000:

Depreciation per mile = ($40,700 − $5,000) / 350,000 = $0.102 per mile

If the truck drives 60,000 miles in Year 1, depreciation = 60,000 × $0.102 = $6,120. If the truck drives only 30,000 miles in Year 2 (a slow year), depreciation drops to 30,000 × $0.102 = $3,060. Total depreciation over the asset's life still equals the depreciable base; it's just allocated by usage rather than by time.

Units-of-production matches expense to revenue particularly well for assets where utilization fluctuates. It's used in mining, manufacturing, and trucking.

### Double-declining-balance (DDB) depreciation

An *accelerated* method that recognizes more depreciation in early years and less in later years.

*Annual depreciation = 2 × Straight-Line Rate × Beginning-of-Year Book Value*

For the truck (7-year life, straight-line rate = 1/7 ≈ 14.3%, double rate = 28.6%):

- Year 1: 28.6% × $40,700 = $11,640. Book value end of Year 1 = $29,060.
- Year 2: 28.6% × $29,060 = $8,313. Book value end of Year 2 = $20,747.
- Year 3: 28.6% × $20,747 = $5,937. Book value end of Year 3 = $14,810.
- ... and so on.

Note: salvage value is *not* subtracted in the DDB formula, but DDB stops depreciating once book value reaches the salvage value. The full $35,700 of depreciable cost still gets expensed across the asset's life; the timing is just shifted forward.

DDB is popular for tax reporting (faster expense means lower current tax) and for financial reporting in industries where assets genuinely lose more value in early years (cars, electronics). The IRS *Modified Accelerated Cost Recovery System (MACRS)*, used for U.S. income tax purposes, is essentially a tabulated declining-balance method with class lives specified by the IRS for each asset type.

### Comparing the methods

For the truck across 7 years, straight-line and DDB produce different annual expense patterns but the same total depreciation ($35,700). Units-of-production produces a third pattern based on actual usage. The choice should match the economic reality of how the asset is used and how it loses value — though in practice, many companies use straight-line for financial reporting and an accelerated method for tax, with the difference producing *deferred tax* effects we won't unpack here.

## 11.4 Asset disposal

When a long-term asset is sold, retired, or exchanged, the entry must (1) remove the asset and its accumulated depreciation from the books, (2) record any cash or trade-in received, and (3) recognize a gain or loss on disposal.

The truck story, December 31, 2024 (after 7 years of straight-line depreciation):
- Cost: $40,700
- Accumulated Depreciation: $35,700 (7 × $5,100)
- Book value: $5,000
- Sale price: $4,800
- Loss on disposal: $5,000 − $4,800 = $200

Journal entry:

| Account | Debit | Credit |
|---|---|---|
| Cash | $4,800 | |
| Accumulated Depreciation — Vehicles | $35,700 | |
| Loss on Disposal of Vehicles | $200 | |
| Vehicles | | $40,700 |

If the truck had sold for $5,500 instead, the entry would have been Cash $5,500, Accumulated Depreciation $35,700, Vehicles $40,700, Gain on Disposal $500.

If the asset is retired without sale (junked, given away), there's no Cash debit; the difference between book value and any trade-in becomes the loss on disposal.

If the disposal happens partway through a year, depreciation is computed for the partial year up to the disposal date *first*, before the disposal entry is made. The accumulated-depreciation balance at disposal must be current.

## 11.5 Repairs, improvements, and revisions

Costs incurred *after* an asset is placed in service split two ways.

*Ordinary repairs and maintenance* — costs that maintain the asset in its current operating condition (oil changes, brake pads, replacement light bulbs in a building). These are *expensed in the period incurred*. Repairs Expense or Maintenance Expense.

*Capital improvements* (also called *betterments* or *extraordinary repairs*) — costs that extend the asset's useful life or significantly increase its productive capacity (engine rebuild, building expansion, machine retrofit). These are *capitalized* — added to the asset's book value, with the adjusted book value depreciated over the remaining (potentially extended) useful life.

The line is judgment, and abuse is a known earnings-management tactic — capitalizing routine repairs to defer expense to future periods is a fraud pattern auditors look for. The general principle: if the cost merely keeps the asset running as before, expense it; if it makes the asset more capable or longer-lived, capitalize.

*Revisions of useful life or salvage value*. Estimates change. Two years into the truck's expected 7-year life, suppose the company realizes the truck will actually last 10 years total and have salvage of $3,000. The remaining book value is depreciated over the *remaining revised useful life* (8 more years) down to the *revised salvage* ($3,000). No restatement of prior years' depreciation; the revision is *prospective*.

This is the standard treatment for changes in estimate — restate the future, not the past.

## 11.6 Intangible assets and goodwill

Intangible assets — assets that have value but no physical substance — are increasingly important on modern balance sheets. The major categories:

*Patents* — exclusive rights to an invention for 20 years. Capitalize the registration and legal cost; amortize over the shorter of legal life (20 years) or estimated useful life.

*Copyrights* — exclusive rights to original creative works. Capitalize legal/registration costs; amortize over useful life (typically much shorter than the legal life of life-of-author-plus-70-years).

*Trademarks* — registered brand identifiers. If renewable indefinitely (which trademarks typically are, with periodic renewal), they are *not amortized* — they are tested for impairment annually.

*Franchise rights* — fees paid for the right to operate under a franchisor's brand. Amortized over the franchise term.

*Goodwill* — the excess of purchase price over the fair value of identifiable net assets when one company acquires another. Goodwill is *not amortized*; it's tested for impairment at least annually.

The amortization mechanic for finite-life intangibles parallels straight-line depreciation: cost / useful life = annual amortization. The journal entry: Debit Amortization Expense, Credit the intangible asset directly (or Credit Accumulated Amortization, depending on company convention).

The trade-off in not amortizing indefinite-life intangibles: the books recognize that some value (a brand name, goodwill from an acquisition) doesn't naturally erode over time the way machinery does — but they require an *impairment test* to catch cases where the value has, in fact, dropped. Without amortization, the only way the asset comes off the books is through impairment.

## 11.7 Impairment

An asset is *impaired* when its carrying value exceeds the cash flows it can reasonably be expected to generate. The U.S. GAAP impairment test (ASC 360 for tangible assets, ASC 350 for intangibles and goodwill) is a two-step process:

1. *Recoverability test*. Compare carrying value to undiscounted future cash flows expected from the asset. If carrying value exceeds undiscounted cash flows, the asset is impaired.
2. *Measurement of impairment*. The impairment loss is the carrying value minus the asset's *fair value* (typically market value or discounted cash flows).

Journal entry to record impairment:

| Account | Debit | Credit |
|---|---|---|
| Loss on Impairment | (impairment amount) | |
| Asset (or Accumulated Depreciation) | | (impairment amount) |

Once impaired, the asset's new (lower) carrying value becomes the basis for future depreciation. Impairments cannot be reversed under U.S. GAAP, even if the asset's value recovers (IFRS allows reversals in some cases).

Goodwill impairment is particularly consequential because goodwill can be a substantial percentage of a balance sheet at acquisitive companies — a $2 billion impairment of goodwill is real on the income statement and the balance sheet, even though no cash moved. Companies that overpay for acquisitions in good economic times and then write down the goodwill in worse times account for many of the largest single-line impairments in any given year.

## 11.8 Natural resources and depletion

For natural-resource extractive industries (mining, oil and gas, timber), the asset is the resource itself in the ground (or on the property). The cost — acquisition, exploration, development — is capitalized, and *depleted* as the resource is extracted, on a units-of-production basis.

Depletion per unit = (Cost − Estimated Residual Value) / Total Estimated Recoverable Units
Annual depletion = Depletion per Unit × Units Extracted This Period

A timber tract bought for $1.2 million with $200,000 residual value and 50 million board feet of recoverable timber: depletion per board foot = ($1.2M − $0.2M) / 50M = $0.02. Extract 5M board feet in Year 1: depletion = $100,000.

The mechanics parallel units-of-production depreciation. The accounting parallel is exact; only the vocabulary is industry-specific.

## 11.9 Exercises

### Warm-up

1. **Distinguish capital expenditure from revenue expenditure** in one sentence each. Give an example of each for a delivery truck.

2. **Why is land not depreciated?**

3. **State the formula for straight-line depreciation.**

### Application

4. **A company buys equipment for $80,000 with $10,000 estimated salvage and 5-year useful life.** Compute Year 1 depreciation under (a) straight-line, (b) units-of-production assuming 200,000 lifetime units and 35,000 produced in Year 1, (c) double-declining-balance.

5. **A company sells a piece of equipment with original cost $60,000 and accumulated depreciation $48,000 for $14,000 cash.** Journalize the disposal.

6. **A company acquires a competitor and recognizes $5 million of goodwill on its books.** Two years later, the impairment test indicates the goodwill is worth only $3.2 million. Journalize the impairment.

### Synthesis

7. **A trucking company is choosing between straight-line and units-of-production for its fleet.** Discuss what considerations should drive the choice. Which method better matches expense to revenue? Which is administratively simpler?

8. **A manufacturer rebuilds a major piece of equipment for $80,000.** The rebuild extends the asset's useful life by four years and increases its annual capacity by 30%. Journalize the rebuild and discuss why this expenditure is capitalized rather than expensed.

### Challenge

9. **Two years into a truck's expected 7-year useful life, the company revises the useful life upward to 10 years.** Walk through the prospective revision: what changes for the remaining years' depreciation? What does *not* change (i.e., what is not restated)?

10. **Goodwill cannot be reversed under U.S. GAAP after impairment.** Explain why this asymmetric rule exists. What would the consequences be if companies were allowed to write goodwill back up if business conditions improved?

## 11.10 Chapter summary

You walked into this chapter with the merchandiser's books. You walk out understanding the long-lived asset side of the balance sheet.

Long-term assets — equipment, buildings, vehicles, land, intangibles, natural resources — are capitalized at acquisition (cost plus all reasonable costs to prepare for use) and allocated to expense over the periods they benefit. *Depreciation* allocates tangible-asset cost (everything except land); *amortization* allocates finite-life intangible cost; *depletion* allocates natural-resource cost on a units-of-production basis. Three depreciation methods — straight-line, units-of-production, double-declining-balance — produce different annual expense patterns but the same total expense over the asset's life.

Disposal entries close out the asset and accumulated depreciation, record any cash received, and recognize gain or loss based on the difference between book value and proceeds.

Impairment writes down assets whose carrying value exceeds their recoverable value. Under U.S. GAAP, impairments are not reversed even if conditions improve. Goodwill — the excess of acquisition price over fair value of net assets — is not amortized but is tested for impairment annually and is one of the more consequential single line items on acquisitive companies' balance sheets.

The single most important idea: long-term assets cost a lot upfront but their cost has to be spread across the periods that benefit, or every income statement is misleading. Depreciation is how the spreading happens. The choice of method affects the timing but not the total.

The common mistake to watch for: confusing the *book value* of a long-term asset (cost less accumulated depreciation, on the books) with its *market value* (what you could sell it for). The two are rarely equal except by coincidence; the balance sheet reports book value, not market value, for almost every long-term asset.

## 11.11 The book-value / market-value gap and what it means

Long-term assets sit on the balance sheet at *book value* — original cost less accumulated depreciation, less any impairment write-downs. Book value is a historical-cost number. Market value — what the asset could be sold for today — is rarely equal to book value, and the gap can be substantial in either direction.

For a building bought in 1995 for $2 million and depreciated to a book value of $400,000, the market value might be $5 million if real estate has appreciated. The balance sheet shows $400,000; the building is genuinely worth twelve times that. The historical-cost convention forces this understatement. Under U.S. GAAP, the company cannot write the building up. Disclosure of the gap, if any is provided, comes through fair-value footnotes or appraisal references — the balance sheet itself stays at $400,000.

In the other direction, an asset whose market value has fallen below book value is supposed to be impairment-tested and written down. The asymmetry is structural: writes-up are prohibited; write-downs are required when triggered. The balance sheet is biased toward understating assets in appreciation cases and recognizing the loss in depreciation cases. This is conservatism encoded into the standard.

For a reader of financial statements, the consequence is that long-term assets at book value are not the company's net worth at market. A real-estate-heavy company can have substantial hidden value in long-held property. A company holding intangibles whose market has weakened can have impairment liability not yet recognized. The footnotes often provide the gap; sometimes they don't. Reading book values as market values is one of the most common errors in beginning financial analysis.

## 11.12 The interaction with the cash flow statement

A subtle structural point. Depreciation is an expense on the income statement that reduces net income, but it is *not a cash outflow*. The cash went out when the asset was purchased; the depreciation is an allocation of that already-spent cash across years. On the statement of cash flows, depreciation is added back to net income in the operating section to convert accrual-basis income into cash-basis operations.

This is why companies with large long-term asset bases (capital-intensive industries — utilities, manufacturing, real estate, transportation) often show *operating cash flow* substantially higher than *net income*. The depreciation add-back is the difference. A reader who looks only at net income for these companies underestimates their cash-generating capability.

The reverse case — net income substantially higher than operating cash flow — is a warning sign. It usually means working capital (receivables, inventory) is growing faster than sales, or revenue is being recognized in advance of cash collection. Either pattern is worth investigating.

The two figures — net income and operating cash flow — are designed to differ. The relationship between them across periods is one of the most informative things a complete set of financial statements has to offer.

## 11.13 Self-constructed assets and capitalized interest

A subtler topic. When a company builds a long-term asset for itself rather than buying one — constructing a new factory, building a custom production line — the *cost* to be capitalized includes not only the direct construction costs (materials, labor, contractor fees) but also a portion of the *interest* the company pays during the construction period on debt used to finance the construction. This is *capitalized interest*. The principle is that until the asset is placed in service, the financing cost is part of getting it ready, just as freight in is part of getting purchased equipment ready. Once construction is complete and the asset is placed in service, interest stops being capitalized and starts being expensed normally.

Capitalized interest is small in dollar terms for most businesses but can be material for capital-intensive industries with long construction cycles (utilities building power plants, real estate developers, oil companies building rigs). Disclosure in the notes is required.

## 11.14 Connections forward

Chapter 12 turns to *current liabilities* — the obligations the company has to pay within the next year. Accounts payable you've already met; this chapter develops the others (notes payable, payroll-related liabilities, sales tax payable, unearned revenue, current portion of long-term debt) and the ratios that measure short-term solvency.
---

## LLM Exercise — Chapter 11: Long-Term Assets (AI Bookkeeping Tool Project)

**Project:** AI Bookkeeping Tool.
**What you're building this chapter:** the long-term-assets module — capitalization, three depreciation methods, disposal, intangibles, impairment, depletion.
**Tool:** **Claude Code.**

---

**The Prompt:**

```
I'm in Chapter 11 of building my AI Bookkeeping Tool. This chapter
taught: capitalization (what costs go INTO the asset: purchase
price + freight + installation + costs to make ready for use);
three depreciation methods:
   - Straight-line: (cost - salvage) / useful life.
   - Units-of-production: (cost - salvage) × (units this period /
     total units expected).
   - Double-declining-balance: 2 × (1 / useful life) × beginning
     book value; switches to straight-line when DB amount falls
     below SL.
Asset disposal (sale, retirement, exchange — gain/loss = proceeds -
book value); repairs vs. improvements (expense vs. capitalize);
intangible assets (patents, copyrights, trademarks, franchises) and
goodwill (only from acquisitions, never internally generated);
impairment (when carrying amount > recoverable amount);
natural-resources depletion (similar to depreciation but units-
based by definition).

Extend the tool. Produce four outputs.

1. **An Asset class/structure.** Fields:
   - Acquisition date, cost, useful life, salvage value.
   - Depreciation method (SL, UOP, DDB).
   - Per-period units (for UOP method).
   - Accumulated depreciation.
   - Book value (cost - accumulated depreciation).
   Methods:
   - `record_acquisition(date, cost, additional_costs_to_capitalize)`
     — journalizes the asset purchase, summing capitalized costs.
   - `record_depreciation(period_end_date)` — computes the period's
     depreciation by the method and journalizes (debit Depreciation
     Expense, credit Accumulated Depreciation).
   - `record_disposal(date, proceeds)` — removes the asset, computes
     gain or loss, journalizes.
   - `record_improvement(date, cost)` — capitalizes (adds to asset
     cost basis).
   - `record_repair(date, cost)` — expenses.

2. **An intangible-asset module.** Similar to PP&E but:
   - Amortization for definite-life intangibles (typically straight-
     line).
   - No amortization for indefinite-life intangibles (annual
     impairment test required).
   - Goodwill: separate handling — never amortized; annually tested
     for impairment.

3. **An impairment-test module.** A function that:
   - For a given asset, accepts the recoverable amount (the higher
     of fair value less costs to sell, or value in use).
   - Compares to book value.
   - If book value > recoverable amount, records impairment loss
     (debit Impairment Loss, credit Accumulated Depreciation or
     directly credit asset).
   - Updates book value.

4. **Tests for each.** A scenario with:
   - A truck purchased for $50,000 with $5,000 capitalizable costs.
     Useful life 5 years, salvage $5,000. Compute depreciation
     under each of the three methods for the 5-year life.
   - The truck sold in year 3 for $25,000. Compute gain or loss
     under each method's accumulated-depreciation balance.
   - An intangible patent acquired for $100,000, 10-year life, but
     impaired to $40,000 in year 5.

Update spec.
```

---

**What this produces:** A complete PP&E and intangibles module. The depreciation tests are the most operationally consequential because depreciation is a recurring monthly adjusting entry.

**How to adapt this prompt:**

- *For your own project:* If your business has minimal PP&E (a service-only business with rented space), build the module anyway. The first time you buy a piece of equipment, you'll need it.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* The right tool. DDB-switching-to-SL is the trickiest implementation; rigorous tests with known answers help.
- *For a Claude Project:* Update spec.

**Connection to previous chapters:** Ch 4's adjusting-entry templates included depreciation as a deferral. Ch 11 generalizes that.

**Preview of next chapter:** Chapter 12 adds the current-liabilities module — payroll (with the employer's hidden liabilities), sales tax, unearned revenue, contingent liabilities, and the current/quick ratio calculations.


---

## AI Wayback Machine

**Yuji Ijiri** was CMU accounting theorist who built much of the modern framework for analyzing capital and long-term assets.

**Run this:**

```
Who is Yuji Ijiri, and how does their work connect to long-term assets we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Yuji Ijiri"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Yuji Ijiri's ideas to a specific accounting question.
- Add a constraint: "Answer including criticisms or limits of Yuji Ijiri's framework."

What changes? What gets better? What gets worse?
