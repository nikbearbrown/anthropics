# Video Ideas — MBA Corporate Finance
*Scouted 2026-07-09 from 15 narrative chapters*

---

## Candidate 01 — Why Capital Structure Doesn't Matter (Until It Does)
- Source: `mba-corporate-finance/chapters/07-capital-structure-theory-the-modigliani-miller-world.md`
- Topic: CORPORATE FINANCE
- Hook: Two firms with identical assets but opposite financing — one all-equity, one loaded with debt — are worth exactly the same. This is simultaneously the most important theorem in corporate finance and obviously wrong.
- Key case: Halverson Industries: the 1958 Modigliani-Miller proof shows the pie doesn't change size when you slice it differently, so the total value of a firm is independent of its debt-equity mix in a frictionless world.
- The Question: If debt is cheaper than equity, why doesn't adding debt increase firm value — and if adding it back does create value through the tax shield, why don't firms borrow as much as possible?
- Core idea: In a world without taxes, bankruptcy costs, or information asymmetry, investors can personally replicate any corporate leverage through "homemade leverage," so corporate capital structure is redundant. The moment you add taxes back, interest deductibility creates a real tax shield worth T×D — but firms that hit 100% debt would face catastrophic distress costs that wipe out the gain.
- Visual object: Same-size pie split two ways (debt vs. equity slices) vs. a value curve that rises with the tax shield, peaks, then falls as distress costs mount — the trade-off hill.
- Manim move: morph (pie stays constant size as slices rearrange → then transform into the value curve showing the optimal peak)
- Example seed: Halverson has $400M of debt at 24% tax rate → tax shield worth $96M. If Halverson borrowed its entire enterprise value, the distress costs would swallow the shield. The optimal sits somewhere in between, and that "somewhere" is the whole subject of modern capital structure theory.
- Length band: 3–5 min
- Still lanes: c2v (equation derivation of V_L = V_U + T×D), geo (pie chart morph → trade-off curve)
- Prerequisites: Basic concept of debt vs. equity; notion of taxes
- Exclusions: Agency cost details, pecking order theory, personal taxes — those are Chapter 8
- Score: 10/10

---

## Candidate 02 — Why Most M&A Destroys Value (And CFOs Keep Doing It)
- Source: `mba-corporate-finance/chapters/11-m-and-a-the-largest-decisions-a-cfo-makes.md`
- Topic: CORPORATE FINANCE
- Hook: Acquirers underperform by 5–15% over 3–5 years on average. Targets capture most synergy value through the deal premium. The buyer is the residual claimant — and consistently gets the short end.
- Key case: Halverson's $700M acquisition of Cardinal Flow Systems: the standalone DCF floor is $550M, the synergy case adds up to $250M haircutted, but targets typically claim 50% of synergy value, leaving Halverson with a razor-thin margin — and most revenue synergies historically don't arrive.
- The Question: If sophisticated CFOs know the empirical record is negative for acquirers, why do they keep acquiring — and what would a disciplined acquirer do differently?
- Core idea: The deal premium plus integration costs typically exceeds realized synergies because revenue synergies require customer behavior changes the acquirer cannot control (30–50% realization rate) while cost synergies are under direct management control (70–80% realization rate). Overconfidence, escalation of commitment, and CEO hubris compound the error in ways the valuation model cannot capture.
- Visual object: A synergy waterfall: gross synergy → cost-synergy haircut → revenue-synergy haircut → deal premium paid → value left for acquirer (often zero or negative).
- Manim move: collapse (synergy buckets collapsing one by one as haircuts are applied, leaving a residual bar that may be negative)
- Example seed: Cardinal has $80M EBITDA. Comparable deals close at 8–12× EBITDA, implying $640M–$960M range. At $700M offer: Halverson is claiming $150M of $250M in synergy value — with revenue synergies at 30–50% realization. That margin evaporates if integration takes 36 months instead of 18.
- Length band: 3–5 min
- Still lanes: geo (waterfall diagram), c2v (synergy haircut table)
- Prerequisites: Basic M&A concept; notion of synergies
- Exclusions: Deal financing structure, LBO mechanics, hostile takeovers
- Score: 10/10

---

## Candidate 03 — The WACC Looks Precise. It Isn't.
- Source: `mba-corporate-finance/chapters/05-the-cost-of-capital-and-the-wacc.md`
- Topic: CORPORATE FINANCE
- Hook: Every major capital investment decision at a public company is made by discounting cash flows at a number called the WACC. That number is computed to one decimal place. It rests on inputs that could move it by 150 basis points in either direction without anyone being wrong.
- Key case: Halverson's FP&A team computes WACC = 8.0% using beta = 1.1 and ERP = 5.0%. With beta = 1.3 and ERP = 6.0% — both equally defensible — the WACC becomes 9.6%. Plant 4's NPV, positive at 8%, may go negative at 9.6%.
- The Question: The WACC formula is mechanical — six inputs, one output. Why is a number that can be computed in a spreadsheet still the most contested input in corporate finance?
- Core idea: Three of the six inputs require pure judgment: the equity risk premium (historical estimates range 4–7%, forward-looking estimates 4–5%), beta (a regression with a standard error of 0.15–0.25), and whether to use current or target capital structure weights. The formula looks precise; the inputs are soft. A CFO who treats the WACC as a settled number has handed capital allocation authority to whoever last touched the spreadsheet.
- Visual object: A 3×3 sensitivity grid — rows are beta (0.9, 1.1, 1.3), columns are ERP (4.5%, 5.0%, 6.0%) — with each cell showing a WACC value. The base case sits in the middle; the grid shows the full defensible range.
- Manim move: spread (sensitivity grid filling in cell by cell, revealing the range around the ostensibly precise base case)
- Example seed: Priya's WACC = 8.0%. Change beta 1.1→1.3 and ERP 5.0%→6.0%: WACC becomes 9.6%. Plant 4 NPV at 8% is $42M positive. At 9.6% it may flip negative. The investment decision changes on inputs nobody questioned since last quarter.
- Length band: 2–3 min
- Still lanes: c2v (sensitivity grid), geo (spectrum bar showing defensible range)
- Prerequisites: Basic idea of discounted cash flows; what a discount rate does
- Exclusions: CAPM derivation, multifactor models, APV — keep to the judgment inputs
- Score: 10/10

---

## Candidate 04 — Dividends and Buybacks Are Mathematically Equivalent (But Treated Completely Differently)
- Source: `mba-corporate-finance/chapters/09-returning-capital-dividends-buybacks-and-the-choice-between-them.md`
- Topic: CORPORATE FINANCE
- Hook: In a frictionless world, returning $100M through dividends and returning $100M through stock buybacks leaves shareholders with identical wealth. In the real world, the same CFO who cuts a dividend by $5M will watch the stock drop 10%, while canceling a buyback program barely registers.
- Key case: Halverson has $180M of excess cash. A special dividend, a buyback, and a dividend increase all return the same amount — but a dividend increase commits the firm to paying forever (cutting it costs dearly), while a buyback can be paused when Cardinal integration needs cash.
- The Question: If the math is the same, why does the form of payout create such different market reactions — and how should a CFO decide?
- Core idea: Three real-world frictions break the MM payout irrelevance result: taxes (buybacks are more efficient for taxable investors because of deferral and basis offset), information (a dividend increase is a costly, credible commitment to future earnings — Lintner's smoothing; a cut is severely punished), and clientele effects (income investors hold stocks partly for the dividend; changing it forces involuntary selling). The form of payout is communication, not just cash transfer.
- Visual object: A stylized event-study bar chart: dividend cut announcement → large negative stock return; buyback cancellation → near-flat reaction. Then a side-by-side commitment ladder: dividend (high commitment, hard to reverse) vs. buyback (low commitment, pausable).
- Manim move: split (one cash flow splitting into two paths — dividend path with high commitment bar and buyback path with flexible bar — then each path showing its tax, signaling, and clientele implications)
- Example seed: Halverson's quarterly dividend of $0.40/share has an implicit contract with income investors who hold the stock for the yield. Raising it to $0.42 signals confident earnings; cutting it back to $0.38 in a bad year could cause a 15% stock drop. The same $0.02 cut, but the mechanism is psychological and reputational, not financial.
- Length band: 3–5 min
- Still lanes: geo (event study chart, commitment ladder), c2v (payout arithmetic showing equivalence before frictions)
- Prerequisites: Basic notion of dividends and stock buybacks
- Exclusions: Payout taxation specifics by jurisdiction, special dividends, convertible preferred — keep to the core two-way comparison
- Score: 9/10

---

## Candidate 05 — The Cash Conversion Cycle: The Biggest Pool of Capital Nobody Talks About
- Source: `mba-corporate-finance/chapters/03-working-capital-is-where-the-cash-lives.md`
- Topic: CORPORATE FINANCE
- Hook: Halverson Manufacturing has $323M of capital trapped in its operating cycle at any given moment. That is larger than its total long-term debt. It is six times the size of the plant expansion everyone is arguing about. Nobody asked the bank for it. Nobody diluted shareholders to get it. It's just sitting there, in transit.
- Key case: Halverson: DSO = 60 days, DIO = 60 days, DPO = 35 days → CCC = 85 days. At $3.8M of COGS per day, the cycle traps $323M. Cutting the CCC by 10 days frees $38M permanently — no debt, no equity issuance required.
- The Question: If shortening the cash conversion cycle is worth tens of millions of dollars in permanent capital liberation, why do most capital allocation debates focus only on debt vs. equity?
- Core idea: Working capital is internal financing: every day shaved from the CCC permanently reduces the capital the operating cycle consumes. The arithmetic is CCC = DSO + DIO − DPO, and each component is owned by a different organizational function (sales, operations, procurement) — which is why improving it is a coordination problem, not just an analytical one. Improving DPO by stretching supplier terms shifts a cash burden onto smaller suppliers, raising an ethical question the formula doesn't show.
- Visual object: A horizontal timeline showing the 85-day cycle: cash out (pay suppliers) → inventory phase (60 days) → sales → receivables phase (60 days) → cash in; DPO shown as a leftward offset that shortens the net exposure.
- Manim move: trace (a dollar coin tracing the full 85-day arc through supplier payment → inventory → revenue recognition → collection, then a second trace at 75 days showing the freed $38M)
- Example seed: Halverson's collections team reduces DSO by 5 days by improving invoicing speed — releasing $19M permanently. The operations team reduces DIO by 5 days through better demand forecasting — releasing another $19M. Total: $38M freed without touching the balance sheet, earning no interest expense, causing no dilution.
- Length band: 2–3 min
- Still lanes: geo (timeline diagram), c2v (CCC formula derivation)
- Prerequisites: Basic understanding of accounts receivable, inventory, payables
- Exclusions: Detailed hedging of DPO ethics, factoring, supply chain finance products
- Score: 9/10

---

## Candidate 06 — NPV Is Not a Machine for Producing Correct Answers
- Source: `mba-corporate-finance/chapters/04-capital-budgeting-at-the-firm-level.md`
- Topic: CORPORATE FINANCE
- Hook: 60% of the NPV that justifies a major capital project typically comes from a single parameter — the long-run growth rate in the terminal value formula — applied to cash flows that don't start for 11 years. Changing that one number by 1 percentage point can swing the recommendation by more than the NPV itself.
- Key case: Plant 4 ($50M investment): operations team's NPV = $87M with g = 2.5%. With g = 1.5%, NPV drops to ~$30M. With g = 3.5%, NPV reaches ~$65M. The range exceeds the low-end NPV. The decision is robust (sign stays positive), but the specific number is fiction.
- The Question: If the terminal value formula is so sensitive to g that the NPV range is wider than the NPV itself, what is NPV actually good for — and what would make the investment case defensible rather than just arithmetically complete?
- Core idea: NPV is not a machine for correct answers — it is a structure for having the right argument. The formula forces every assumption (revenue, costs, working capital, discount rate, growth) into explicit, falsifiable form. Once explicit, they can be questioned, stress-tested, and revised before the board meeting. The catastrophic memo is one where the analyst can't explain the inputs. The defensible memo names exactly what would flip the sign.
- Visual object: A sensitivity waterfall: operations team's NPV of $87M → conservative ramp adjustment → risk-adjusted discount rate → g = 1.5% floor → result $28M–$87M range with the decision rule (sign is stable = proceed) shown separately from the magnitude uncertainty.
- Manim move: collapse (tall $87M NPV bar collapsing through a series of assumption challenges — each one narrowing the bar — leaving the sign still positive, revealing robustness as the output, not precision)
- Example seed: Terminal value accounts for 60% of Plant 4's NPV. With g = 2.5%, terminal value contributes ~$52M of the $87M. With g = 1.5%, it contributes ~$30M. The $22M gap between those is larger than many standalone projects. The question isn't "what is g?" — it's "can you defend your g on the record in front of the board?"
- Length band: 3–5 min
- Still lanes: c2v (perpetuity growth formula sensitivity), geo (waterfall / tornado chart)
- Prerequisites: Basic understanding of present value and NPV sign
- Exclusions: IRR vs. NPV debate, capital rationing, real options (those are Ch 6)
- Score: 9/10

---

## Candidate 07 — Why Firms with Strong Cash Flows and Low Debt Should Have High Debt (But Don't)
- Source: `mba-corporate-finance/chapters/08-capital-structure-in-the-real-world.md`
- Topic: CORPORATE FINANCE
- Hook: The MM-with-taxes theorem says optimal capital structure is 100% debt. No firm does this. Not one. Either every CFO in America is making the same elementary mistake, or the formula is missing something large.
- Key case: A regulated utility carries 50–60% debt; a high-growth software firm carries 5–15% debt; Halverson (stable industrial) carries 25–40% debt. Same four-force framework, radically different optimal capital structures — because distress costs, agency costs, and information costs all vary dramatically by firm type.
- The Question: If debt creates value via the tax shield, what exactly limits that value — and how does the answer differ for Apple vs. a utility vs. a biotech?
- Core idea: Four forces push back against the tax shield: (1) distress costs — direct (3–7% of pre-distress value in legal fees) and indirect (10–25% in customer flight, employee attrition, supplier tightening) that grow nonlinearly with leverage; (2) agency costs — the shareholder-bondholder conflict creates perverse incentives (risk-shifting, underinvestment); (3) information costs — equity issuance signals overvaluation, triggering the pecking order; (4) personal taxes — the effective marginal value of debt is only 10–15%, not the full 21–24% corporate rate. The optimal structure is firm-specific, not universal.
- Visual object: A single two-curve diagram for three different firm types side by side: the tax-shield benefit line vs. the distress-cost curve, showing how the peak shifts dramatically from left (software) to right (utility) as firm type changes.
- Manim move: scan (camera panning across three versions of the trade-off diagram, each with a different peak — software far left, manufacturer center, utility far right — with firm characteristics labeled)
- Example seed: At 80% leverage, Halverson's expected annual distress cost (probability × cost) likely exceeds $50M — more than the incremental tax shield from the additional debt. For Apple, with minimal physical assets and brand-dependent customers, distress at 50% leverage would cost far more because customers and employees flee at the first sign of trouble.
- Length band: 3–5 min
- Still lanes: c2v (the full V_L equation with all four adjustments), geo (three-firm trade-off diagram)
- Prerequisites: MM result from Chapter 7 (tax shield creates value); basic notion of financial distress
- Exclusions: Personal tax calculations in detail, debt covenants mechanics, Miller 1977 formal derivation
- Score: 9/10

---

## Candidate 08 — The Real Cost of an IPO Is Invisible
- Source: `mba-corporate-finance/chapters/10-raising-capital-ipos-secondaries-and-the-cost-of-going-to-market.md`
- Topic: CORPORATE FINANCE
- Hook: The cost of taking a company public that appears in the fee schedule is 7%. The actual cost is closer to 25–30%, and the biggest piece doesn't appear anywhere in the accounting.
- Key case: A $400M IPO: gross spread 7% = $28M (visible). Underpricing averages 15–20% = $60–80M transferred to allocatees (invisible in the financial statements). Plus a 2–3% announcement effect on existing market cap. Total real cost: $90–120M on a $400M raise.
- The Question: Why does systematic underpricing persist — and why has the 7% gross spread not compressed in 30 years of electronic trading, while every other capital markets fee has fallen to near zero?
- Core idea: Underpricing exists because of the winner's curse: informed institutional investors only bid enthusiastically on good deals, leaving uninformed investors with adverse selection (they win allocations disproportionately in bad deals). To attract uninformed participation, underwriters must price every deal low enough that buying without information is profitable in expectation. The gross spread stickiness remains genuinely unexplained — cartel pricing fails as an explanation because regulators would have broken it; pure competition fails because the fee hasn't moved in 30 years.
- Visual object: Three bars side by side — gross spread ($28M), underpricing ($70M), announcement effect ($125M market cap) — showing how the invisible costs dwarf the visible fee. Then a mechanism arrow: informed investors pass → uninformed left with adverse selection → underpricing required to compensate.
- Manim move: accumulate (three cost bars appearing one by one, the last two unlabeled at first — "what the fee schedule shows" vs. "what the actual cost is")
- Example seed: Halverson's proposed $400M SEO: visible gross spread = $16M (4%). Underpricing at 2% = $8M not in the fee schedule. Announcement effect at 2.5% on a $5B market cap = $125M market cap decline — recoverable if the strategic rationale is clear, sticky if it isn't. The real question Diane should ask is not "what's the spread?" but "why are we issuing equity now?"
- Length band: 3–5 min
- Still lanes: geo (three-bar cost stack), c2v (winner's curse mechanism flow)
- Prerequisites: Basic notion of IPO/stock offering; what a stock price is
- Exclusions: Book-building process details, lockup mechanics, convertible notes
- Score: 9/10

---

## Candidate 09 — Hedging Cannot Create Value in a Perfect World (Which Is Why It Does in This One)
- Source: `mba-corporate-finance/chapters/12-operational-risk-management.md`
- Topic: CORPORATE FINANCE
- Hook: In a perfect market, corporate hedging is completely irrelevant — shareholders can hedge any risk themselves in their own portfolios. So why does hedging interest rates, commodity prices, and foreign exchange actually make some firms more valuable?
- Key case: Halverson post-Cardinal: $700M of floating-rate debt, Plant 4 construction underway, integration consuming management capacity. A 2% rate spike adds $14M of annual interest expense — enough to force capex cuts during the most critical investment phase. An interest rate swap costs $1.75M per year to eliminate that risk.
- The Question: If investors can always hedge themselves, what exactly is the firm doing that creates value when it hedges — and how do you know when the hedge is worth the cost?
- Core idea: Three real-world frictions make corporate hedging valuable even when personal hedging is available: (1) distress cost reduction — smoothing cash flows reduces the probability of crossing the distress threshold, where costs are nonlinear; (2) tax convexity — a firm that earns $200M then $0 pays more total tax than one that earns $100M twice, so income smoothing through hedging reduces aggregate tax burden; (3) investment pipeline preservation — for a firm funding capex from internal cash, a bad year for commodity prices or rates can force cancellation of positive-NPV projects, destroying real value that external financing (expensive from Ch. 10) can't cheaply replace.
- Visual object: A two-panel diagram: left panel shows Halverson's cash flow with rate spike → capex cut → foregone Plant 4 returns (the downside without the hedge); right panel shows the smooth cash flow with the swap → capex funded → no interruption. The $1.75M annual cost sits tiny against the foregone value.
- Manim move: compare (split screen: volatile cash flows forcing capex abandonment vs. smooth hedged cash flows maintaining the investment program, with the hedge cost shown as a thin line)
- Example seed: Tom's calculation: unhedged $700M floating exposure + 2% rate rise = $14M/year extra interest = the Plant 4 capex budget. The swap costs $1.75M/year. The math says hedge — not because rates are probably rising, but because Halverson can't afford the cash flow surprise during an integration year.
- Length band: 2–3 min
- Still lanes: geo (two-panel comparison), c2v (three-friction framework list)
- Prerequisites: Basic notion of interest rate risk; what a swap does
- Exclusions: Hedge accounting under ASC 815, delta hedging, options vs. forwards details
- Score: 9/10

---

## Candidate 10 — Real Options: Why the Standard NPV Is Wrong (In Two Opposite Directions at Once)
- Source: `mba-corporate-finance/chapters/06-risk-adjusted-rates-and-real-options.md`
- Topic: CORPORATE FINANCE
- Hook: Maya's NPV for Plant 4 is $42M. It is wrong — not in the arithmetic, but in the question it answers. Using the firm's WACC understates risk (making NPV too high). Ignoring the option to defer overstates the cost of waiting (making NPV too low). The corrections point in opposite directions and don't cancel out.
- Key case: Plant 4 in Mexico (hypothetical): firm WACC = 8%, but pure-play comparables for Mexican industrial operations give an asset beta of 1.4 → project WACC = 9%. NPV drops from $42M to $25M. But if the firm waits 6 months to observe demand data — 50/50 strong ($80M NPV) vs. weak (−$10M NPV) — the deferral option is worth $5M extra. Net: $30M, not $42M. A different number and a different recommendation structure.
- The Question: Why does the standard NPV calculation fail in two opposite directions simultaneously — and how does the real-options correction change not just the number but what the board is being asked to approve?
- Core idea: The risk-adjustment corrects a valuation error (the wrong discount rate makes the NPV too high). The real-options correction corrects a strategy error (treating the commitment as irrevocable ignores the option to selectively invest only in good scenarios, breaking the NPV's symmetrical averaging across all outcomes). The deferral option adds value because selective exercise captures full upside ($80M) while avoiding full downside (choosing $0 instead of −$10M).
- Visual object: A two-panel visual: left panel is the NPV profile curve showing value falling as discount rate rises from 8% to 9.6%; right panel is a decision tree with "commit now" branch (expected NPV $35M) vs. "wait 6 months" branch (expected NPV $40M), with option value = $5M highlighted.
- Manim move: transform (NPV profile curve morphing into the decision tree, showing the two corrections as separate geometric operations on the value)
- Example seed: Board outcome without real options: "Approve $50M commitment today, NPV = $42M." Board outcome with real options: "Approve up to $50M with a 6-month deferral right pending Q2 demand indicators — preserving $5M of option value by not throwing away information available cheaply." The recommendation's structure changes, not just the number.
- Length band: 3–5 min
- Still lanes: geo (decision tree diagram), c2v (unlever-relever beta formula, selective exercise arithmetic)
- Prerequisites: Basic NPV concept; notion of discount rates
- Exclusions: Black-Scholes option pricing for real assets, binomial tree full derivation
- Score: 8/10

---

## Candidate 11 — The Four Behavioral Traps That Destroy Acquisition Value
- Source: `mba-corporate-finance/chapters/14-behavioral-corporate-finance.md`
- Topic: CORPORATE FINANCE
- Hook: The empirical record on acquisitions is negative for acquirers on average. The people making those acquisitions are smart, well-advised, and have access to the same data you do. The problem isn't information — it's the cognitive machinery running underneath the analysis.
- Key case: Maya's Cardinal integration memo 6 months post-close: everything is tracking to plan. Revenue synergies are running at 85% of projection. The reflex is to feel good. The behavioral checklist says: this is exactly when overconfidence, anchoring, escalation of commitment, and confirmation bias are most dangerous — because they feel like good judgment.
- The Question: If you know about the four behavioral biases, can you design a process that actually neutralizes them — or does knowing about them just give you new vocabulary for the same old errors?
- Core idea: (1) Overconfidence → reference class forecasting: ignore the inside view of this specific project and ask how comparable integrations actually performed (year-two revenue synergies realize at 30–50% of projection on average). (2) Anchoring → re-derive from scratch: the 8% WACC has drifted unchallenged for three quarters while Halverson's leverage, beta, and market conditions changed. (3) Escalation → reset: sunk costs are irrelevant; the question is whether you'd initiate the project today at the current implied price. (4) Confirmation bias → pre-mortem: assume the deal fails in 18 months and work backward to specific failure mechanisms — forcing the mind to generate the arguments it would otherwise suppress.
- Visual object: A 2×2 grid: bias name in each quadrant → specific failure mode → named counter-move. The pre-mortem is shown as a "reverse telescope" — looking backward from stipulated failure to causes, instead of forward from causes to probability.
- Manim move: duplicate (the same analysis appearing four times — once as overconfident, anchored, escalated, confirmation-biased → then each duplicate transformed by its counter-move until all four converge on a debiased version)
- Example seed: Pre-mortem for Cardinal: "It is month 18 and the integration has clearly failed. Cardinal's largest customer announced dual-sourcing in month 8, eroding 20% of projected revenue. The integration team was diverted by an IT migration, costing market share to a competitor in Q4. The founder left at month 12 because of conflict over operational autonomy." These specific failure mechanisms are what the pre-mortem forces out. A standard risk section would have said "execution risk — manageable."
- Length band: 3–5 min
- Still lanes: c2v (2×2 bias/counter-move grid), geo (pre-mortem reverse arrow)
- Prerequisites: Basic M&A concept; willingness to accept that smart people make systematic errors
- Exclusions: Market behavioral finance (momentum, post-earnings drift) — this is corporate, not market, behavioral finance
- Score: 8/10

---

## Candidate 12 — The Inside/Outside Gap: Why the Same Numbers Mean Different Things
- Source: `mba-corporate-finance/chapters/02-reading-the-firm-from-inside.md`
- Topic: CORPORATE FINANCE
- Hook: Three firms report identical income statements and identical cash flow statements. One is growing healthily, one is accumulating bad debt, and one is managing its earnings through quarter-end manipulation. From the outside, you cannot tell which is which from the numbers alone.
- Key case: Firms A, B, and C — all showing $95M net income and $120M operating cash flow. Firm A's AR growth comes from new customers (0–30 day aging). Firm B's AR growth comes from slow payers (60–90 day aging). Firm C's AR spike is concentrated in the last 48 hours of the quarter (revenue recognized before earned). The inside view — Aaron's AR aging schedule — distinguishes them immediately.
- The Question: What diagnostic can an outside analyst use to approximate what the inside view reveals — and how does the cash conversion ratio give early warning before the problem appears in reported earnings?
- Core idea: The cash conversion ratio (OCF / Net Income) is the most reliable early warning signal in financial statement analysis. A ratio consistently above 1.0 signals high earnings quality; a declining ratio signals working capital deterioration or earnings management; a ratio persistently below 1.0 in a non-growth firm is the earliest warning sign I know. Sloan (1996) showed that the accrual component of earnings is less persistent than the cash component — high-accrual firms systematically see earnings revisions downward.
- Visual object: Three firms side by side with identical summary financials, then three AR aging schedules showing radically different bucket distributions — current, 60-day, 90-day — making the three scenarios distinguishable.
- Manim move: scan (camera scanning across three identical-looking income statements, then zooming into three different AR aging schedules that reveal the hidden divergence)
- Example seed: Halverson's trailing cash conversion ratio has declined from 1.2 two years ago to 0.8 now. That's a real question: the ratio says each dollar of reported earnings is backing up against more working capital. Is it growth (new customers taking 60-day terms)? Slow payers? Quarter-end contract pulls? The ratio flags the question; the aging schedule answers it.
- Length band: 2–3 min
- Still lanes: c2v (cash conversion ratio formula and trend), geo (three-firm aging schedule comparison)
- Prerequisites: Basic notion of income statement vs. cash flow statement; net income vs. cash
- Exclusions: Accrual accounting mechanics in full detail, hedge accounting, inventory cost methods
- Score: 8/10

---

*Candidates below 8/10 were detected but not written: Chapter 1 (inside/outside orientation gap — strong pedagogy but weak motion test), Chapter 13 (international finance — three FX exposure types interesting but not a single visual object), Chapter 15 (capstone integration — the interdependence is the point but there is no single counterintuitive claim).*
