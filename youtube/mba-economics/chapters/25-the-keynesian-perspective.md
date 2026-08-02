# Chapter 25 — The Keynesian Perspective

*The case for active stabilization — when the economy needs help, and what the help looks like.*

---

By 1933, four years into the Great Depression, the U.S. unemployment rate had reached 25 percent. One in four working-age adults had no job. Industrial production had fallen by half. Banks were failing in waves. The mainstream economic view of the 1920s — that markets self-correct, that wages and prices would adjust to restore full employment, that intervention was unnecessary and counterproductive — was being tested and was failing badly.

In 1936, John Maynard Keynes published *The General Theory of Employment, Interest, and Money*. The book argued that the self-correction story was wrong. In the short run, prices and wages don't adjust fast enough to clear markets after a demand shock. A recession caused by falling demand can persist for years without the supply side providing any fix. The cure has to come from outside — government spending and tax policy that raises aggregate demand directly.

The framework Keynes built became the basis for active macroeconomic policy in most of the developed world. Its successes — the postwar prosperity, the fiscal response to 2008–09, the COVID rescue — and its failures — the 1970s stagflation that undermined the framework's credibility — are together the macroeconomic story of the past 90 years.

This chapter develops the Keynesian framework: what makes it distinct, why it advocates for fiscal stimulus in recessions, how the multiplier works, and what the Phillips curve says about the trade-off between unemployment and inflation.

---

## Sticky prices, sluggish adjustment

The Keynesian framework starts with one observation: after a demand shock, prices and wages don't adjust fast enough to clear markets.

Here is the mechanism. Demand for a firm's product falls. The firm can respond two ways: cut the price (which keeps units sold up) or cut production (which keeps the price up). In the simple competitive model, cutting prices is the right response. In practice, firms typically cut output and employment first.

Why? The reasons compound.

**Menu costs.** Changing prices is costly — printing, notification, renegotiation, disruption to customer relationships. For many firms, especially in B2B markets, prices are set in advance for extended periods.

**Coordination problems.** If my competitors aren't cutting prices, I lose margin without gaining market share. Everyone waits for someone else to move first. The result is that prices stay up and output falls.

**Wage stickiness.** As Chapter 21 showed in detail, firms don't cut wages in recessions — they lay off workers instead. Cutting wages produces resentment, turnover, and adverse selection. The layoff/wage-cut choice has a clear empirical winner: layoffs.

**Long-term contracts.** Many prices and wages are locked in for months or years. Collective-bargaining agreements, annual price contracts, long-term service agreements — all prevent the market from clearing quickly.

**Money illusion.** Workers and firms track nominal values. A worker will resist a 5% nominal wage cut even if inflation has already reduced their real wage by 5%. The resistance to nominal cuts is real, even when a nominal cut would leave the worker's real position unchanged.

The result: when aggregate demand shifts left, the adjustment comes first through output and employment, not through prices. Quantities fall before prices do. The economy enters a recession that the market-clearing model predicted would be short or nonexistent.

This is the foundation of Keynesian policy advocacy. If the economy can't fix itself quickly — and the evidence of the 1930s was that it couldn't fix itself in anything shorter than years — then waiting imposes a massive cost in unemployment and lost output. Intervention isn't just possible; it's necessary.

---

## The expenditure multiplier

The Keynesian framework has a specific mechanism that amplifies the effects of policy: the **expenditure multiplier**.

The intuition first. Suppose the government spends an extra $100 billion on infrastructure projects. That $100 billion becomes income for the construction workers, suppliers, and contractors who do the work. Those recipients save some of the income and spend the rest — say they spend 70 percent and save 30 percent. So $70 billion flows back into the economy as new spending, which becomes income for someone else. Those people spend 70 percent of $70 billion, which is $49 billion. And so on.

The total increase in GDP is:

$$\$100B + \$70B + \$49B + \$34.3B + \ldots = \frac{\$100B}{1 - 0.70} = \frac{\$100B}{0.30} = \$333B$$

The formula: if the **marginal propensity to consume (MPC)** is 0.70, the multiplier is $1/(1 - MPC) = 1/0.30 \approx 3.33$.

This is the Keynesian multiplier in its simplest form. Every dollar of government spending generates $3.33 of total income.

Real multipliers are smaller. The simple formula assumes all spending stays in the domestic economy. In practice, money leaks out through several channels: some is spent on imports (which stimulates foreign economies, not domestic ones), some goes to taxes, some is saved at higher-than-baseline rates, some is offset by reduced spending elsewhere. Incorporating these leakages:

$$\text{Multiplier} = \frac{1}{1 - MPC(1 - t) + MPM}$$

where $t$ is the marginal tax rate and $MPM$ is the marginal propensity to import. With MPC = 0.70, $t$ = 0.25, and $MPM$ = 0.10, the multiplier is roughly:

$$\frac{1}{1 - 0.70(1-0.25) + 0.10} = \frac{1}{1 - 0.525 + 0.10} = \frac{1}{0.575} \approx 1.74$$

Estimates of the actual U.S. multiplier from empirical studies of the 2009 stimulus ranged from about 0.5 to 1.5, with most in the 1.0–1.5 range. The variation reflects different types of spending, different economic conditions, and different methodologies.

The size of the multiplier matters because it determines how much fiscal stimulus is needed to fill an output gap. If the multiplier is 1.5, $200 billion of stimulus generates $300 billion of additional GDP. If it's 0.8, the same $200 billion generates $160 billion. The policy implication scales with the estimate.

The multiplier is generally **larger** when:
- The economy has significant slack (output well below potential — money isn't competing with existing activity).
- Interest rates are at or near the zero lower bound (so the central bank isn't offsetting the stimulus with tighter money).
- Spending is directed at lower-income households who have higher MPCs — they spend a larger fraction of any additional income.
- Spending is direct government purchases rather than transfers (a transfer might be partly saved).

The multiplier is generally **smaller** when:
- The economy is near full employment (fiscal expansion mainly raises prices).
- Monetary policy offsets the stimulus.
- The stimulus is directed at higher-income households with lower MPCs.
- The economy is highly open (more leakage to imports).

---

## Fiscal stabilization tools

Keynesian fiscal policy operates through two mechanisms.

**Discretionary fiscal policy** — explicit legislative decisions to spend more, tax less, or both during recessions; and to restrain spending or raise taxes during booms. The 2009 American Recovery and Reinvestment Act (~$800 billion) was the largest U.S. discretionary stimulus since World War II at the time. The 2020 CARES Act (~$2 trillion) exceeded it substantially.

**Automatic stabilizers** — features of the tax-and-transfer system that respond automatically to the cycle without requiring new legislation. When incomes fall in a recession, income-tax revenue falls automatically (because of progressive rates). Unemployment insurance pays out more. SNAP enrollment rises. Medicaid spending rises. These stabilizers expand the government's deficit precisely when the economy needs support and contract when the economy recovers.

Estimates suggest U.S. automatic stabilizers offset roughly 8 to 10 percent of any fiscal shock — so a $1 trillion demand shock is met with roughly $80–100 billion of automatic fiscal support. Not sufficient on its own, but a meaningful first response that requires no Congressional action.

Discretionary policy has well-known problems — the lags.

**Recognition lag.** It takes months, sometimes more than a year, to confirm that a recession has started. (The NBER dates recessions retrospectively.) Policymakers are trying to respond to data that's incomplete and subject to revision.

**Decision lag.** It takes months, sometimes years, for Congress to agree on and enact legislation. The deliberation is not a failure of government; it reflects genuine disagreement about the size, composition, and timing of stimulus.

**Implementation lag.** Once enacted, spending takes more months to flow through to the economy. Infrastructure projects have long lead times. Tax cuts take time to show up in paychecks. Some of the 2009 stimulus was still flowing in 2011, two years after enactment.

**Political asymmetry.** Stimulus packages are politically easy to enact; the subsequent restraint is politically hard. The ratchet pushes toward permanently larger deficits.

The combination of lags means that discretionary fiscal policy, despite good intentions, sometimes peaks in its effect during the recovery rather than the recession, risking inflationary overheating at precisely the wrong moment. The Keynesian policy ideal — timely, targeted, temporary — is easier to state than to implement.

---

## The Phillips curve

A specific implication of the sticky-price framework is the **Phillips curve** — an empirical relationship between unemployment and inflation. When unemployment is low, the labor market is tight, wages and prices rise faster. When unemployment is high, wage and price pressure falls.

The original curve emerged from A.W. Phillips's 1958 paper examining U.K. data from 1860 to 1957 — nearly a century of apparently stable trade-off between wage inflation and unemployment. Macroeconomists in the 1960s treated it as a policy menu. The implication seemed to be that policymakers could choose a point on the curve: accept more inflation for less unemployment, or tolerate more unemployment for lower inflation.

Then the 1970s arrived. The U.S. — and most of the developed world — experienced both high inflation *and* high unemployment simultaneously. Stagflation. The simple Phillips trade-off appeared to have collapsed.

The explanation came from Milton Friedman and Edmund Phelps, working independently in the late 1960s — before the stagflation actually occurred. Their insight: there is a *short-run* Phillips curve, which exhibits the trade-off, and a *long-run* Phillips curve, which is vertical at the natural rate of unemployment.

The key mechanism is expectations. The short-run curve is drawn at a given expected inflation rate. When workers expect 2 percent inflation, they accept wage increases of 2 percent plus the going employment premium. When employment is high and wages are rising, if the central bank accommodates by expanding the money supply, inflation rises. Workers eventually update their inflation expectations upward. The short-run Phillips curve shifts up. Now the same unemployment rate corresponds to a higher inflation rate, because expected inflation is higher.

A central bank that tries to keep unemployment below the natural rate by expansionary policy triggers a sequence: temporary unemployment reduction → rising inflation → rising inflation expectations → upward shift of the short-run Phillips curve → same unemployment, but now at higher inflation. The one-time gain fades; the higher inflation persists. The long-run trade-off is vertical — there is no permanent unemployment-inflation exchange.

The 1970s stagflation matched this prediction. The Fed had allowed inflation to drift up through the 1960s and 1970s partly to sustain employment. Inflation expectations became unanchored. Getting them back down required the sharp Volcker recession of 1981–82, during which unemployment exceeded 10 percent for over a year while monetary policy forcibly broke the inflation spiral.

What this taught policymakers:
- A short-run trade-off exists — monetary and fiscal policy can reduce unemployment temporarily at the cost of higher inflation.
- The trade-off is not stable — it shifts as inflation expectations change.
- The long-run curve is approximately vertical — sustained stimulus can't permanently push unemployment below the natural rate.
- Anchoring inflation expectations is as important as managing actual inflation — credibility matters.

---

## What survives of Keynes

Keynes's original framework has been substantially revised by subsequent research and events. What remains:

**Short-run demand effects are real.** Sticky prices mean that demand-side shocks reduce output and employment, not just prices. This is accepted by essentially all modern macroeconomists.

**Fiscal policy has real effects in the short run.** The multiplier is real, if smaller than early estimates suggested. Automatic stabilizers do useful work. Discretionary policy can be effective at the zero lower bound.

**The Phillips curve trade-off operates in the short run.** Demand stimulus reduces unemployment temporarily, at the cost of higher inflation.

What has been jettisoned:

**The permanent unemployment-inflation trade-off.** Friedman and Phelps were right; the long-run curve is vertical.

**Large multipliers.** Empirical estimates are substantially below the theoretical 3-plus from simple models.

**Confidence in fine-tuning.** The lags are long enough that discretionary policy often arrives late.

**The view that monetary policy is impotent.** Subsequent decades showed it has powerful effects — it is now the primary stabilization tool.

The resulting framework — usually called "new Keynesian" — retains sticky prices, real short-run demand effects, and a role for policy, while accepting that expectations matter enormously, monetary policy is primary, and the long run is supply-side determined. Keynes's essential insight that markets don't self-correct quickly remains the operating assumption of most modern macroeconomic policymaking. The specific mechanisms and numerical claims have been substantially refined.

---

## Synthesis

Pull back. Keynesianism started from one observation: markets don't always self-correct quickly after demand shocks. Sticky prices and wages mean that when aggregate demand falls, output and employment fall before prices and wages adjust. Recessions are real and can be long.

The expenditure multiplier amplifies the effects of fiscal intervention. Every dollar of stimulus generates more than a dollar of GDP, because recipients respend their income in successive rounds. The size of the multiplier determines how much stimulus is needed, and it is smaller in practice than the simple formula suggests — perhaps 0.8 to 1.5 for U.S. fiscal policy in moderate recessions.

Fiscal policy operates through discretionary legislation and automatic stabilizers. Discretionary policy is powerful but slow — recognition, decision, and implementation lags mean it often peaks after the recession it was meant to address. Automatic stabilizers are faster but limited in scale.

The Phillips curve ties unemployment to inflation through labor-market tightness. A short-run trade-off exists. It's not stable: it shifts when inflation expectations change. The long-run curve is vertical at the natural rate. Monetary and fiscal policy can't permanently buy lower unemployment with higher inflation — the gain is temporary, the higher inflation persists.

What remains of the Keynesian framework after 90 years of revision: the reality of demand-side recessions, the usefulness of stabilization policy in the short run, the importance of automatic stabilizers, and the acknowledgment that markets don't self-correct as quickly as the classical model predicted. That's not everything Keynes claimed, but it's enough to justify the policy toolkit that most advanced economies use when recessions arrive.

---

## LLM Exercises

**Exercise 1 — Compute a multiplier.** Tell an LLM the marginal propensity to consume is 0.6. The marginal propensity to import is 0.1. The tax rate on additional income is 0.25. Ask it to compute the expenditure multiplier accounting for all these leakages. Verify by hand.

**Exercise 2 — Diagnose stickiness.** Pick a real industry or labor market you know. Ask an LLM to identify which sources of price/wage stickiness are most active there: menu costs, coordination problems, wage contracts, long-term agreements, money illusion. Push for specifics.

**Exercise 3 — Argue for vs. against fiscal stimulus.** Tell an LLM the U.S. has just entered a recession. Ask it to argue both sides on a $500B fiscal stimulus package: when would it work, when wouldn't it, what would determine the size of the multiplier? A good answer engages with both sides.

**Exercise 4 — Phillips curve diagnosis.** Ask an LLM to walk through the U.S. 1970s stagflation using the Friedman-Phelps short-run/long-run Phillips curve framework. Why did the simple trade-off break? What did it teach policymakers about inflation expectations?

**Exercise 5 — Identify automatic stabilizers.** Ask an LLM to list the major U.S. automatic stabilizers. Then ask: in the absence of any discretionary policy response, how much would the automatic stabilizers offset a 5 percentage point GDP shock? The answer should be in the 0.5–1 percentage point range, depending on assumptions.

---

## LLM Exercise — Chapter 25: The Keynesian Perspective (Policy Brief Project)

**Project:** Policy Brief.  
**What you're building this chapter:** the Keynesian framing of your policy — sticky prices, the expenditure multiplier, the Phillips curve, what the chapter said survives of Keynes.  
**Tool:** **Claude Project** "Policy Brief" — appends a section.

---

**The Prompt:**

```
Chapter 25 of my Policy Brief project. Prior sections in this Claude
Project. Chapter 25 taught: Keynes' contribution — that sticky
prices and sluggish wage adjustment mean the economy can sit at
output below potential for extended periods (involuntary
unemployment is real); the expenditure multiplier (a $1 increase
in spending generates more than $1 of GDP, because the recipient
spends some of it, the next recipient spends some of THAT, and so
on; multiplier = 1/(1 - MPC)); fiscal stabilization tools
(automatic stabilizers — UI, progressive taxation; discretionary
— stimulus, infrastructure spending); the Phillips Curve (short-
run trade-off between inflation and unemployment); what survives
of Keynes (the basic mechanism in recessions; the limits at full
employment).

Write the brief's "Keynesian Reading" section in 300–500 words.

1. **The Keynesian case for the policy (if any).** Does your
   policy have a Keynesian justification — that is, does it boost
   AD when the economy is below potential? Most direct fiscal
   policies do; many indirect policies (regulation, antitrust)
   don't. If yours does, name the multiplier estimate (cite or
   reason from MPC) and the assumed slack in the economy.

2. **The Phillips-Curve check.** If your policy reduces
   unemployment via Keynesian-stimulus channels, where on the
   Phillips Curve are you? At low unemployment, the Phillips
   Curve trade-off is steep (small drops in unemployment cost a
   lot of inflation); at high unemployment, it's flatter (lots
   of stimulus possible without inflation). Name where the
   economy is when your policy is enacted.

3. **The "survives of Keynes" reading.** The chapter named that
   the basic Keynesian mechanism is well-established in
   recessions, contested at full employment. State whether the
   policy depends on the established Keynesian mechanism (slack-
   economy stimulus) or the contested one (full-employment
   stimulus / structural reform via demand).

End with one sentence on whether the Keynesian framing helps or
hurts the policy's case. Many policies are sold as Keynesian
but their substantive defense lies elsewhere; the brief should
be honest about this.
```

---

**What this produces:** A 300–500 word section that runs the Keynesian framing as a lens, with explicit attention to where the assumptions hold and where they don't.

**How to adapt this prompt:**

- *For your own project:* UBI students: this is central — Keynesian multiplier is a primary justification (transfers to liquidity-constrained households have high MPC). Tax-cut students: Keynesian effects depend on whether the cut is to high- or low-MPC households. Antitrust students: largely outside the Keynesian frame.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you want a multiplier calculation given a stated MPC, Claude Code can produce it.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 24's AD/AS framework + Ch 25's Keynesian reading + Ch 26's neoclassical reading triangulate the macro analysis.

**Preview of next chapter:** Chapter 26 covers the neoclassical perspective — rational expectations, supply-side policy, the modern synthesis. The brief should run BOTH framings as a check on its own conclusions, not just the one that supports the policy.

---

## AI Wayback Machine

**John Maynard Keynes** was a British economist whose *The General Theory of Employment, Interest, and Money* (1936) established the theoretical foundations for modern macroeconomics — arguing that insufficient aggregate demand could produce persistent unemployment and that government fiscal policy was the appropriate corrective instrument.

![John Maynard Keynes](../images/john-maynard-keynes-cv9.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is John Maynard Keynes, and how does their work connect to the
Keynesian perspective we covered in this chapter? Keep it to three
paragraphs. End with the single most surprising thing about their
career or ideas.
```

→ Search **"John Maynard Keynes"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply John Maynard Keynes's framework to a current economic question.
- Add a constraint: "Answer including criticisms or limits of John Maynard Keynes's framework."

What changes? What gets better? What gets worse?

---

*Byline: Nik Bear Brown.*
