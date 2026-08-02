# MBA Finance — Vox Explainer Video Candidates

Scouted from 20 chapters. Cards ordered highest score first.
All scores ≥ 8 included. Source book: `mba-finance/`.

---

## Candidate 01 — Why Bond Prices Fall When Interest Rates Rise

- Source: `mba-finance/chapters/10-bonds-and-bond-valuation.md`
- Topic: FINANCE
- Hook: A bond you paid $1,051 for will never pay you more than $1,000 — yet you still got a good deal.
- Key case: 3M corporate bond (2.25% coupon, March 2021): market rates fall to 1.24%, price rises to $1,051 even though the bond only ever repays $1,000 at maturity.
- The Question: If the bond never pays more than face value, why does its price rise above face value when rates fall — and by exactly how much?
- Core idea: A bond's coupon is fixed forever; the only thing the market can move is the price. When new bonds yield less than your old one, buyers bid up the old bond until its effective yield (accounting for the price premium) equals the new market rate. Price and yield must always move in opposite directions because the cash flows are contractual and the discount rate is set by the market.
- Visual object: A single bond timeline — fixed coupon arrows + par repayment arrow — with a sliding discount rate bar that morphs the present-value calculation into a new price in real time.
- Manim move: morph (discount rate slider causes the PV sum to morph into a new price above/below par) + trace (cash flow arrows traced individually then summed)
- Example seed: 3M bond. $1,000 par. 2.25% coupon. 5.5 years left. Rates were 2.25% at issue; by March 2021 market rates dropped to 1.24%. Show the old $1,000 price, then watch it rise to $1,051 as the discount rate slider moves down from 2.25% to 1.24%. Flip the slider up to show the reverse for rising rates (2022 scenario: rates jump to 5%, price collapses to ~$880).
- Length band: 3–5 min
- Still lanes: geo (bond timeline diagram), c2v (yield-vs-price curve), raster (3M bond screenshot optional)
- Prerequisites: Basic idea of present value; that interest rates exist.
- Exclusions: Duration math, callable bonds, credit risk, yield curve shape — all out.
- Score: 10/10

---

## Candidate 02 — Why NPV Beats IRR When Projects Differ in Size

- Source: `mba-finance/chapters/16-how-companies-think-about-investing.md`
- Topic: FINANCE
- Hook: A 14% return sounds better than 13% — until you realize the 13% project creates $1,135 more actual wealth.
- Key case: Two embroidery machines: regular ($16K, IRR 14.1%, NPV $2,836) vs. heavy-duty ($40K, IRR 13.2%, NPV $3,971). IRR says take the small machine. NPV says take the big one. The NPV answer is right.
- The Question: How can the project with the lower percentage return create more shareholder wealth — and which number should the CFO trust?
- Core idea: IRR is a rate — it is blind to how much capital is actually deployed. NPV is a dollar amount — it measures what genuinely lands in shareholders' pockets. When two mutually exclusive projects differ in scale, maximizing the rate instead of the dollar value is equivalent to preferring 20% on $100 over 15% on $10,000. The rate looks better; the wealth does not.
- Visual object: Two side-by-side "wealth meters" filling up in dollar terms — the small machine fills fast to a modest level, the large machine fills slower but to a higher level. Percentage labels hover above, dollar labels accumulate below.
- Manim move: accumulate (dollar wealth grows per year for each project) + compare (split-screen side-by-side with IRR% and NPV$ labeled)
- Example seed: Regular machine: $16K cost, cash flows $2K/$4K/$5K/$5K/$5K/$5K over 6 years, 9% cost of capital → NPV $2,836, IRR 14.1%. Heavy-duty: $40K cost, cash flows $8K/$14K/$13K/$12K/$11K/$10K → NPV $3,971, IRR 13.2%. Show that IRR ranks wrong. Then the "20% on $100 vs. 15% on $10,000" analogy closes the argument.
- Length band: 3–5 min
- Still lanes: geo (dual bar chart, wealth accumulation), c2v (NPV profile curves crossing zero)
- Prerequisites: What NPV and IRR mean at a basic level; that the firm discounts cash flows.
- Exclusions: MIRR, PI, capital rationing, multiple IRRs — all out.
- Score: 9/10

---

## Candidate 03 — The Growth Trap: How a Profitable Business Runs Out of Cash

- Source: `mba-finance/chapters/18-financial-forecasting.md`
- Topic: FINANCE
- Hook: A business grows sales 30%, posts record profit — then bounces a payroll check three months later.
- Key case: A fast-growing sporting goods retailer (Clear Lake). Income statement shows $47K net income. But to support growth, the firm must pay for inventory, payroll, and supplies months before customers pay. Midyear cash drops to $8,800 — below the $35K minimum. The business is profitable and broke simultaneously.
- The Question: If profit is real, where did the cash go — and why does faster growth make the problem worse, not better?
- Core idea: Accrual accounting records revenue when the sale happens; cash arrives only when the customer pays (30–90 days later). Meanwhile, suppliers must be paid, inventory must be bought, and payroll runs weekly. Growth amplifies the gap: every additional dollar of sales requires working capital investment before it generates cash inflow. The income statement and the bank account are measuring different things, and a fast-growing business can be perfectly profitable while draining its cash reserves.
- Visual object: A single timeline split into two tracks — "income statement track" (revenue recorded on sale date) and "cash track" (cash received 60 days later) — with a growing gap shaded red as growth rate increases.
- Manim move: split (one timeline splits into two tracks) + spread (the gap between accrual record and cash receipt widens as sales volume grows) + decay (cash balance depletes despite positive earnings)
- Example seed: Clear Lake Sporting Goods. January sales $10,408 on net-60 terms. Inventory purchased in December paid now. Payroll due Friday. Income statement: profitable. Bank account: $8,800, needs $35,000 minimum. Show the gap widen as a second year projects 30% growth. Then show how a 12-month pro forma cash budget spots the crunch in February and allows a revolving credit line to be arranged in January.
- Length band: 3–5 min
- Still lanes: geo (dual-track timeline, cash gap diagram), c2v (cash balance chart through the year)
- Prerequisites: What profit vs. cash flow means; that businesses sell on credit.
- Exclusions: Detailed pro forma mechanics, percentage-of-sales method, scenario analysis — all out.
- Score: 9/10

---

## Candidate 04 — The Diversification Paradox: How Adding a Risky Stock Lowers Your Total Risk

- Source: `mba-finance/chapters/13-statistical-analysis-in-finance.md`
- Topic: FINANCE
- Hook: You own one stock with 18% annual volatility. You add another stock — also 18% volatility. Your portfolio volatility drops to 15%. You just took on more holdings and less risk.
- Key case: Two stocks, each with 18% standard deviation, but correlation 0.4. Equal-weight portfolio: standard deviation drops to 15.1%. No change in expected return. Show the math. Then show that if correlation were 1.0, the portfolio would still be 18% — the entire benefit comes from imperfect correlation.
- The Question: How can adding a second risky asset make a portfolio safer — and what is the one number that determines how much safer?
- Core idea: Portfolio variance is not the weighted average of individual variances — it includes a covariance term that shrinks the total when assets don't move in perfect lockstep. The lower the correlation between assets, the more the covariance term reduces portfolio variance. With correlation of −1, you can theoretically build a zero-variance portfolio from two volatile assets. The "free lunch" in diversification is real, but it depends entirely on imperfect correlation — and correlations rise in crises, shrinking the benefit exactly when you need it most.
- Visual object: A two-asset scatter plot where the correlation slider moves from +1 to −1 and the portfolio standard deviation curve falls in real time. At +1: no benefit. At 0: meaningful reduction. At −1: zero risk possible.
- Manim move: transform (scatter plot of returns morphs as correlation slider moves) + collapse (portfolio std dev bar shrinks as correlation decreases) + split (variance decomposition splits into systematic and idiosyncratic components)
- Example seed: $10K split equally between Delta Airlines (σ = 52%) and Exxon (σ = 35%, correlation with Delta = 0.35). Portfolio σ = 30.4%. Now replace Exxon with Southwest Airlines (σ = 42%, correlation with Delta = 0.87). Portfolio σ = 49.1%. Same number of stocks, dramatically different diversification — because industry correlation, not count, is what matters.
- Length band: 2–3 min
- Still lanes: geo (correlation scatter plots, portfolio variance formula decomposition), c2v (sigma-vs-correlation curve)
- Prerequisites: What standard deviation means as a risk measure.
- Exclusions: Efficient frontier, CAPM, beta derivation, full Markowitz optimization — all out.
- Score: 9/10

---

## Candidate 05 — The Apple Debt Puzzle: Why Cash-Rich Companies Borrow Billions

- Source: `mba-finance/chapters/17-how-firms-raise-capital.md`
- Topic: FINANCE
- Hook: Apple had $191 billion in cash — and still borrowed $113 billion. That is not a contradiction. It is a tax strategy.
- Key case: Apple fiscal 2020. $191B in cash. $113B in long-term debt. The company borrows at 4% nominal; after the 21% corporate tax deduction, the real cost is 3.16%. Equity costs 8–10% with no tax offset. Every dollar borrowed at 3.16% that replaces equity funding at 9% reduces the weighted average cost of capital — making every future cash flow worth more in present value.
- The Question: Why would a company with more cash than most countries' GDP borrow money — and what does the tax code have to do with it?
- Core idea: Interest is tax-deductible; equity dividends are not. The after-tax cost of debt is always lower than the pre-tax rate by the factor (1 − tax rate). This creates a structural incentive to include debt in the capital structure: the interest tax shield raises firm value by T × D (the Modigliani-Miller formula with taxes). But distress costs pull in the opposite direction — too much debt risks bankruptcy. The optimal capital structure balances these two forces, and Apple's use of debt at low rates in a low-distress environment is textbook trade-off theory.
- Visual object: A WACC "blending dial" — two streams (debt at 3.16% and equity at 9%) flowing into a single blended rate. As the debt fraction increases, the blended cost falls. A distress-cost curve rises from the right and eventually bends the firm-value line back down.
- Manim move: accumulate (tax shield dollar savings stack up as debt increases) + transform (WACC blending dial shifts with capital structure mix) + split (firm value = unlevered value + tax shield − distress costs, each component labeled)
- Example seed: Apple 2020. 4% bond rate × (1 − 0.21) = 3.16% after-tax cost of debt. Equity cost ~9% via CAPM. With 25% debt weight: WACC = 0.25 × 3.16% + 0.75 × 9% = 7.54%. Without debt: WACC = 9%. The 1.46-point difference on a firm with $2.5T in assets is enormous. Show this as the reason Apple deliberately maintains the debt book even though it doesn't need the cash.
- Length band: 3–5 min
- Still lanes: geo (WACC blending diagram, trade-off theory hump chart), c2v (WACC vs. debt-fraction curve)
- Prerequisites: What interest rates and tax deductions mean. Basic idea of shareholders vs. creditors.
- Exclusions: Pecking order theory, full MM derivation, flotation costs, convertible bonds — all out.
- Score: 8/10

---

## Candidate 06 — The Early Saver Always Wins: Compounding and the Cost of Waiting

- Source: `mba-finance/chapters/07-time-value-of-money-i-single-payment-value.md`
- Topic: FINANCE
- Hook: Friend A saves for 9 years then stops. Friend B saves for 35 years and never stops. At retirement, Friend A has more money.
- Key case: Both start at age 22, both invest $5,000/year at 8%. Friend A invests years 22–30 (9 years, $45K total) and stops. Friend B invests years 30–65 (35 years, $175K total) and never stops. At 65, Friend A's balance equals or exceeds Friend B's — despite contributing less than one-quarter as much money.
- The Question: How can someone who invested for 9 years and then stopped for 35 years end up with as much as someone who invested every single one of those 35 years?
- Core idea: Compound interest is exponential, not linear. The early dollars get the most years of compounding — Friend A's year-22 deposit compounds for 43 years while Friend B's first deposit only compounds for 35. Each year of delay multiplies the required future savings by (1+r). The Rule of 72 makes this concrete: at 8%, money doubles every 9 years — so Friend A's money doubles 4–5 times while Friend B's early contributions miss the first doubling entirely.
- Visual object: Two stacked bar charts growing year by year from age 22 to 65 — one bar for contributions (gray), one for growth (green). Friend A's green section towers over their small gray section. Friend B's gray section is enormous but their green section is proportionally smaller.
- Manim move: accumulate (year-by-year balance growth for each friend) + compare (split-screen side-by-side at age 65 showing contribution vs. growth breakdown) + duplicate (each dollar "clones itself" each period to show compounding)
- Example seed: Friend A: $5,000/year × 9 years = $45,000 invested. All 9 deposits compound at 8% to age 65. Total: ~$2.3M. Friend B: $5,000/year × 35 years = $175,000 invested. All deposits compound to 65. Total: ~$2.2M. Then apply the Rule of 72: at 8%, money doubles every 9 years. Friend A gets ~5 doublings on early money; Friend B's late money gets only 2–3 doublings.
- Length band: 2–3 min
- Still lanes: geo (contribution vs. growth stacked bars, Rule of 72 table), c2v (balance trajectory curves for both friends)
- Prerequisites: What interest rates and compound growth mean at an intuitive level.
- Exclusions: Annuity formulas, retirement planning mechanics, inflation adjustments — all out.
- Score: 8/10

---

## Candidate 07 — The Hidden Interest Rate in Your Trade Discount

- Source: `mba-finance/chapters/19-the-importance-of-trade-credit-and-working-capital-in-planning.md`
- Topic: FINANCE
- Hook: Your supplier offers you a "free" 30-day extension on your invoice. The actual annual interest rate is 36.73%.
- Key case: Standard trade terms: 2/10 net 30. Pay within 10 days, get 2% off. Wait until day 30, pay full price. The 2% fee for 20 extra days annualizes to 36.73% APR — far higher than any bank line of credit. Yet most small businesses routinely forgo this discount without realizing the cost.
- The Question: If no one calls it a loan, and there's no interest line on the invoice, how can a routine payment-term choice carry an annualized rate of 36.73%?
- Core idea: When you forgo an early-payment discount, you are implicitly borrowing money from your supplier for the gap between the discount window and the net due date. The formula (360 / (net days − discount days)) × (discount% / (100% − discount%)) converts any trade terms into an annualized rate. At 2/10 net 30: (360/20) × (2/98) = 36.73%. Any firm with access to bank credit at 8–10% is leaving 27+ percentage points of free money on the table by not taking the discount.
- Visual object: A single invoice with two payment paths forking off it. Path A (pay day 10, save $210 on $10,500) and Path B (pay day 30, pay full $10,500). The $210 gap is labeled as an implicit loan, then the annualization formula animates to 36.73%.
- Manim move: split (invoice splits into two payment timelines) + transform (the $210 discount gap morphs into an annualized interest calculation) + morph (the 36.73% number appears next to a credit card rate and a bank line rate for comparison)
- Example seed: Supplier invoice: $10,500 on 2/10 net 30 terms. Pay day 10: $10,290 (save $210). Pay day 30: $10,500. You borrowed $10,290 for 20 days at a cost of $210. That's 2.04% for 20 days. Multiply by 360/20 = 18. Result: 36.73% APR. Compare: bank credit line at 8%, credit card at 22%, payday loan at 400%+. The trade discount sits between the credit card and the bank — almost invisible, almost universally ignored.
- Length band: 2–3 min
- Still lanes: geo (invoice-to-payment-fork diagram, APR comparison bar chart), c2v (timeline of payment options)
- Prerequisites: What an annual percentage rate means. Basic idea of borrowing money.
- Exclusions: Cash conversion cycle, factoring, supply chain finance, full working capital management — all out.
- Score: 8/10

---

## Candidate 08 — Real vs. Nominal: Why 15% Interest in 1981 Was Cheaper Than 6% Today

- Source: `mba-finance/chapters/03-economic-foundations-money-and-rates.md`
- Topic: FINANCE
- Hook: A small business in 1981 paid 15% interest on its bank loan. That sounds ruinous. In real terms, it was cheaper than a 6% loan today.
- Key case: 1981 US economy. Nominal rate: 15%. Inflation: 12%. Real rate: ~3%. Today: nominal rate 6%. Inflation: 2–3%. Real rate: ~3–4%. The 1981 loan was cheaper in purchasing-power terms despite the headline rate being 2.5 times higher. The nominal rate is the number you see; the real rate is the number that actually determines whether borrowing is expensive.
- The Question: How can a loan at 15% be less expensive than a loan at 6% — and which number should you actually care about?
- Core idea: Inflation erodes the real value of money. When you borrow $1M at 15% in a 12% inflation environment, you repay in dollars that are 12% cheaper — so the inflation does part of the work for you. The Fisher equation makes this precise: real rate ≈ nominal rate − inflation rate. The nominal rate without the inflation context is meaningless noise. The real rate is what actually transfers purchasing power between lender and borrower.
- Visual object: A two-panel display. Left panel: 1981 loan — large nominal number (15%) with a large inflation block (12%) underneath it, leaving only a small real rate sliver (3%) visible. Right panel: today's loan — smaller nominal number (6%) with a small inflation block (2–3%), leaving a similar real rate sliver (3–4%). The nominal numbers look very different; the real rates are nearly identical.
- Manim move: split (nominal rate bar splits into inflation component and real rate component) + compare (1981 vs. today side-by-side with both decompositions) + transform (the nominal number shrinks visually as the inflation layer is peeled off)
- Example seed: 1981: nominal 15%, inflation 12%, real rate 3%. Today: nominal 6%, inflation 3%, real rate 3%. Then an extreme case: Weimar Germany 1923 — nominal rates in the millions of percent but real rates near zero because hyperinflation eroded debt faster than interest accrued. Bring back to the practical: when evaluating any borrowing decision, always compute the real rate first.
- Length band: 2–3 min
- Still lanes: geo (stacked bar chart decomposing nominal rate into real + inflation), c2v (historical scatter of nominal vs. real rates 1970–2024)
- Prerequisites: What interest rates and inflation mean at a basic level.
- Exclusions: Fisher equation derivation, TIPS bonds, monetary policy, Fed mechanics — all out.
- Score: 8/10

---

*Scouted: 2026-07-09. All 20 chapters read. Eight candidates scored ≥ 8/10.*
