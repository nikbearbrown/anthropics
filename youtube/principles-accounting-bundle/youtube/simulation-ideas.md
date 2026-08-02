# Principles of Accounting Bundle — Simulation Ideas

*Generated 2026-07-26 · MANIM lane only · Score ≥ 6 · D3 cards excluded*

---

*Honest assessment: After reading all 16 chapters, only 2 candidates passed all three gates (simulatable equation → visible motion; two exact testable predictions; surprising result). Most accounting content is procedural (journal entries, classification rules, GAAP disclosure requirements) with no equation that drives a visible animated artifact. The following 2 cards are genuine — no others were forced.*

---

## Candidate 01 — Declining-Balance vs. Straight-Line Depreciation: Two Curves Drawing

- Source: `principles-accounting-bundle/chapters/11-long-term-assets.md`
- Topic: Depreciation; double-declining-balance vs. straight-line
- Lane: MANIM (directed animation)
- Hook: Straight-line and double-declining-balance depreciation assign the same total cost over an asset's life — but their curves cross exactly once, and a firm that chooses DDB over SL is essentially borrowing from the IRS, paying lower taxes now and higher taxes later without anyone going to prison.
- The rule: SL: annual depreciation = (Cost − Salvage)/N; book value_SL(t) = Cost − t×(Cost − Salvage)/N. DDB: annual depreciation = 2/N × book_value_(t-1); stops when book value = salvage; book value_DDB(t) = Cost × (1 − 2/N)^t (until the floor).
- Concrete numbers: Cost = $40,000; Salvage = $5,000; N = 7 years; SL annual = $35,000/7 = $5,000/yr; DDB rate = 2/7 ≈ 28.57%/yr; DDB Year 1 = 0.2857 × 40,000 = $11,429; Year 2 = 0.2857 × 28,571 = $8,163; Year 3 = $5,831; Year 4 = $4,165 → DDB now BELOW SL per-year; Year 4 switches to SL for remaining balance. Total depreciation both methods = $35,000.
- The artifact / what moves: A single-axis chart (x = year 1–7, y = cumulative accumulated depreciation) draws two curves simultaneously — one linear (SL, steady slope) and one convex-then-linearizing (DDB, fast at first, then switching); at Year 1 the DDB curve is $6,429 ahead of SL; the two curves converge to the same endpoint ($35,000) at Year 7; a second sub-panel shows annual depreciation expense as two bar series — DDB bars are tall then short, SL bars are flat; the crossover year (where DDB annual < SL annual) highlights with a vertical marker.
- Output medium: Manim (mp4)
- Two testable predictions: P1: After Year 1, DDB accumulated depreciation ($11,429) is 2.29× the SL accumulated depreciation ($5,000) — the acceleration is most extreme in the first year. P2: By Year 4, the DDB book value ($16,577) is BELOW the SL book value ($19,300) — the curves have crossed and DDB is now "ahead" in cost recognition by $2,723; the DDB curve is now higher (closer to total).
- The change: Change salvage from $5,000 to $0 — the DDB formula now continues declining until year 7 without the floor interrupt; both curves still end at the same total ($40,000); the crossover point shifts right by about one year.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Choosing an accelerated depreciation method is a legal, approved interest-free loan from the Treasury: you recognize more expense now, pay less tax now, and pay more tax later. The only cost is the administrative complexity of tracking two sets of books.
- Exclusions: Units-of-production method (which varies by usage, appropriate for D3 slider), IRS MACRS tables (too procedural), goodwill impairment (no equation-driven curve).
- Sim slug: depreciation-sl-vs-ddb-curves
- Score: 6/10

---

## Candidate 02 — Bond Carrying Value: Effective-Interest Amortization Curve

- Source: `principles-accounting-bundle/chapters/13-long-term-liabilities.md`
- Topic: Long-term liabilities; bond discount amortization; effective-interest method
- Lane: MANIM (directed animation)
- Hook: A bond issued at a discount appears to have its face value as a liability, but the company actually received less — and the accounting "grows" the carrying value up to face over the bond's life, which means the liability on the balance sheet increases every year even as the company makes all its payments on time.
- The rule: Carrying value_t = PV_0 × (1 + r_market)^t − coupon × [(1 + r_market)^t − 1]/r_market; equivalently, CV_t = CV_(t-1) + (CV_(t-1) × r_market − coupon); discount amortization each period = interest expense − cash paid = CV_(t-1) × r_market − face × r_stated.
- Concrete numbers: Face = $100,000; stated rate = 5%; market rate = 6%; maturity = 10 years annual coupon; issue price = $92,640 (as computed in chapter: PV of annuity + PV of face); coupon cash = $5,000/yr; Year 1 interest expense = $92,640 × 6% = $5,558; discount amortization = $558; CV after Y1 = $93,198; Year 10 CV = $100,000 exactly.
- The artifact / what moves: A horizontal axis spans Years 0–10; the carrying value curve draws from $92,640 at t=0 and climbs in an exponential arc (convex upward, since each year's starting CV is higher) to exactly $100,000 at t=10; each year's interest expense bar draws below the axis — it grows slightly each year as CV grows; a separate cash-paid flat line at $5,000 draws for comparison; the difference (amortization amount) is labeled as the gap between the two; at t=10 the curves close and the bond is retired.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Total interest expense over 10 years = total cash paid + total discount amortized = $50,000 + $7,360 = $57,360; equivalently, $92,640 borrowed → $150,000 repaid (10×$5,000 + $100,000 face) → total cost = $57,360 ✓. P2: The amortization amount in Year 5 is larger than in Year 1 (because CV is higher in Y5 → higher effective interest → larger gap vs. fixed cash coupon); computed: CV after Y4 ≈ $95,300; Y5 amortization = $95,300 × 6% − $5,000 = $718 vs. $558 in Y1.
- The change: Switch from discount to premium — market rate drops to 4%, issue price = ~$108,115; now carrying value starts above face and declines to $100,000 over 10 years; the curve runs downward instead of upward; interest expense each year is *less* than cash paid (premium amortizes down); the animation mirror-flips.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The balance sheet shows a liability that rises every year even as you make every payment on time — not because you're getting deeper in debt, but because the accounting is catching up to the economic reality of what you actually borrowed. This confuses analysts who only look at the balance sheet line.
- Exclusions: Semi-annual coupon adjustments (mechanics same, periods doubled), lease accounting under ASC 842 (similar math, separate story), deferred tax build-up.
- Sim slug: bond-effective-interest-carrying-value
- Score: 6/10
