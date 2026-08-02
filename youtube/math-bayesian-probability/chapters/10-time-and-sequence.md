# Chapter 10 — Time and Sequence

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **(Apply)** Fit a frequentist ARIMA model and produce a point forecast with a prediction interval.
2. **(Apply)** Build a Bayesian structural time series model with sequential updating and produce a posterior predictive distribution.
3. **(Analyze)** Explain sequential updating — "today's posterior is tomorrow's prior" — as a natural consequence of Bayesian inference made visible by the time structure of data.
4. **(Evaluate)** Assess the practical value of a full predictive distribution versus a point forecast for an inventory reorder decision.

---

## The Problem

A regional distribution company tracks weekly demand for one of its best-selling products. At the start of the year, demand was around 8,000 units per week; by week 52, it has climbed to roughly 11,000. The trend is real but noisy — demand spikes and dips week to week, and there is some seasonal pattern the manager suspects is genuine.

The manager needs to place orders for the next quarter. Her supplier requires 10-week lead time, which means she must commit to order quantities now. The critical threshold is 10,000 units per week: below that, current inventory carries her; above that, she risks stocking out, which costs roughly 3× what excess inventory costs.

She needs to know: is demand likely to exceed 10,000 units over the next quarter? Not "roughly what will demand be" — she needs the probability.

An ARIMA model will give her a point forecast and a prediction interval. The interval will be honest about its uncertainty. But it will not, by itself, tell her P(demand > 10,000). A Bayesian structural time series model will.

Before we build either model, notice what makes this problem structurally different from everything we have done so far. In previous chapters, we had a fixed dataset — all observations available at once, inference performed once. Here, observations arrive in sequence over time. The manager will receive a new demand reading every week. Each new reading should update her forecast. This is not a special feature of time series problems — it is Bayesian inference in its most natural form. Every Bayesian analysis is implicitly sequential: you could always have stopped earlier, used the posterior as a prior, and updated when more data arrived. Time series just makes the sequential structure unavoidable and explicit.

---

## Frequentist Solution: ARIMA

### The Setup

**ARIMA** (AutoRegressive Integrated Moving Average) is the frequentist workhorse for time series forecasting. Developed systematically by Box & Jenkins (1970), with a current standard treatment in the 5th edition (Box, Jenkins, Reinsel, & Ljung 2015), it remains the most widely implemented time-series method in economics, epidemiology, and operations research.

Three components, each addressing a different data structure:

- **AR (autoregressive):** This week's demand is partially predicted by last week's demand (and possibly weeks before that). Formally: $y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \ldots + \varepsilon_t$.
- **I (integrated):** Differencing to remove a trend. Demand that trends upward is non-stationary — its mean changes over time. Taking the first difference $\Delta y_t = y_t - y_{t-1}$ often removes the trend, leaving a stationary series.
- **MA (moving average):** Past forecast errors enter the model. Formally: $y_t = \varepsilon_t + \theta_1 \varepsilon_{t-1} + \ldots$. This captures short-term correlations in the error structure.

The notation ARIMA(p, d, q) specifies the orders: p autoregressive terms, d differences, q moving-average terms. For our upward-trending demand series, `auto.arima` (R) or `pmdarima` (Python) will typically select ARIMA(1,1,1): one AR term, one difference, one MA term.

### Model Selection

ARIMA model selection uses the autocorrelation function (ACF) and partial autocorrelation function (PACF) of the differenced series to identify the AR and MA orders, verified by information criteria (AIC, BIC). In practice, automated selection tools handle this reliably for standard series. For our 52-week demand series, ARIMA(1,1,1) fits well.

### Estimation and Forecast

Fitted to 52 weeks of demand data, ARIMA(1,1,1) produces:

```
Method:     ARIMA(1,1,1) — selected by auto.arima
Fitted on:  weeks 1–52

Week 53 forecast:
  Point forecast:         10,840 units
  95% prediction interval: [8,200, 14,600]
  Interval width:         6,400 units
```

*(Illustrative example; structure based on the BSTS comparison in Scott & Varian 2014.)*

The prediction interval grows as the forecast horizon extends — week 60's interval will be substantially wider than week 53's. This is correct: genuine uncertainty about a non-stationary process accumulates.

### What the Manager Can Conclude

- Expected demand in week 53 is approximately 10,840 units.
- The 95% prediction interval [8,200, 14,600] means: intervals constructed this way will contain the true future demand approximately 95% of the time. This is a guarantee about the procedure, not a probability statement about this particular interval.
- P(demand > 10,000 in week 53)? Not directly available from the prediction interval without additional assumptions.

### Where the Frequentist Model Strains

The manager's decision requires a probability. She needs to know whether P(demand > 10,000) is 0.55 or 0.85 — these lead to different order quantities. The prediction interval tells her the range but not the probability she needs.

One workaround: if the forecast is approximately normally distributed, she can compute P(demand > 10,000) from the normal distribution using the point forecast and interval width. For ARIMA(1,1,1) with normally distributed errors, this is valid. The point forecast is 10,840 and the interval [8,200, 14,600] implies an SD of about (14,600 − 8,200) / (2 × 1.96) ≈ 1,633 units. Then P(demand > 10,000) ≈ P(Z > (10,000 − 10,840) / 1,633) ≈ P(Z > −0.51) ≈ 0.70.

This is not wrong — but it requires an additional assumption (normality of the forecast distribution) that the ARIMA framework does not guarantee for all specifications, and it is not a native output of the model. The manager has to do extra work to extract what she actually needs.

More fundamentally, when a new week's demand arrives, there is no natural way to update the ARIMA model without refitting it from scratch on all available data. Sequential updating is not built into the ARIMA framework. The manager refits every week; she does not update.

---

## Bayesian Solution: Structural Time Series

### Sequential Updating: The Core Idea

Before writing down the model, step back to a simpler problem you have already solved.

In Chapter 3, you started with a Beta(1,1) prior on a defect rate and updated it each time a circuit board was tested. After 10 boards (2 defective), you had Beta(3, 9). After 20 boards (4 total defective), you had Beta(5, 17). The posterior after 10 boards was the prior for boards 11–20.

Now ask: what if the true defect rate was changing over time? This is the time series problem. The hidden state — the true demand level, or the true defect rate, or the true disease incidence — is not fixed; it evolves. The Bayesian structural time series model handles this by specifying a prior distribution over the hidden state at each time step and updating it as each new observation arrives.

This is the Kalman filter (Kalman 1960). Rudolf Kálmán showed that for linear models with Gaussian noise, Bayesian sequential updating has an exact closed-form solution: after each observation, the posterior is Gaussian, and that Gaussian becomes the prior for the next step. The Kalman filter is Bayesian updating in action, applied to a sequence of states rather than a fixed parameter.

### The Structural Time Series Model

Harvey (1989) formalized the framework the manager needs. A **Bayesian structural time series (BSTS)** model decomposes demand $y_t$ into components:

$$y_t = \mu_t + \varepsilon_t, \qquad \varepsilon_t \sim \text{Normal}(0, \sigma_\varepsilon^2)$$

$$\mu_t = \mu_{t-1} + \delta_{t-1} + \eta_t, \qquad \eta_t \sim \text{Normal}(0, \sigma_\eta^2) \qquad \text{[local level]}$$

$$\delta_t = \delta_{t-1} + \zeta_t, \qquad \zeta_t \sim \text{Normal}(0, \sigma_\zeta^2) \qquad \text{[local trend]}$$

**Term by term:**

- $y_t$ is observed demand at week $t$. It equals the true level $\mu_t$ plus observation noise $\varepsilon_t$.
- $\mu_t$ is the unobserved true demand level — the hidden state. It evolves according to a random walk on the trend $\delta_{t-1}$, with additional noise $\eta_t$.
- $\delta_t$ is the trend — the rate at which demand is growing. It also evolves, allowing the trend to change over time.
- $\sigma_\varepsilon^2$ is observation variance (how noisy are individual demand readings?).
- $\sigma_\eta^2$ is level variance (how much does the true level jump week to week?).
- $\sigma_\zeta^2$ is slope variance (how much does the growth rate change week to week?).

The three variance parameters are estimated from the data. Their ratio (signal-to-noise ratios) determines how much the model learns from each new observation versus how much it smooths past data.

### Priors

$$\mu_0 \sim \text{Normal}(8000, 1000^2) \qquad \text{[initial level at week 0]}$$

$$\delta_0 \sim \text{Normal}(50, 100^2) \qquad \text{[initial weekly growth rate]}$$

$$\sigma_\varepsilon, \sigma_\eta, \sigma_\zeta \sim \text{Half-Normal}(0, \text{scale}^2) \qquad \text{[noise parameters]}$$

The initial level prior says: "demand at the start of the year was around 8,000 units, give or take 1,000." The growth rate prior says: "weekly growth was around 50 units, which matches the observed trend from roughly 8,000 to 11,000 over 52 weeks." These are weakly informative — reasonable anchors that the data will update.

Note that prior specification for structural time series is genuinely hard. Scott & Varian (2014) note that there is no consensus on weakly informative defaults for the signal-to-noise ratios. The priors above are defensible for this dataset but should be checked via prior predictive simulation (ask the LLM to simulate time series from the prior before fitting to data, and verify they look plausible).

### Sequential Updating in Action

The fitting procedure runs the Kalman filter recursively:

- **Week 1:** Start with prior $(\mu_0, \delta_0)$. Observe demand $y_1 = 8,150$. Update: compute posterior on $(\mu_1, \delta_1)$ using Bayes' theorem. Posterior concentrates slightly above 8,000.
- **Week 2:** Prior for $(\mu_2, \delta_2)$ is derived from the week-1 posterior. Observe $y_2 = 8,220$. Update again.
- ...
- **Week 52:** Prior is derived from the week-51 posterior. Observe $y_{52} = 10,950$. Posterior on $(\mu_{52}, \delta_{52})$ is well-concentrated near the observed trend.

After week 52, the posterior on the current state is the input to forecasting. Extrapolating the state forward gives the posterior predictive distribution for week 53, 54, and beyond.

The key property: at each step, yesterday's posterior is today's prior. The manager does not refit the model each week from scratch — she updates it. Each new observation makes the forecast sharper.

### Results

```
Model:   Local level + linear trend (BSTS)
Priors:  N(8000, 1000) on initial level; N(50, 100) on initial slope
         Half-N(0, 500) on observation SD; Half-N(0, 50) on level SD; Half-N(0, 5) on slope SD

Posterior predictive (week 53):
  Mean:                   10,780 units
  SD:                     1,560 units
  95% CrI:                [7,720, 13,840]
  P(demand > 10,000 | data) = 0.69
  P(demand > 12,000 | data) = 0.23
```

*(Illustrative example; BSTS structure from Scott & Varian 2014.)*

The manager can now answer her question directly: there is about a 69% probability that demand next week exceeds her reorder threshold of 10,000 units. Given that stocking out costs 3× excess inventory, she should almost certainly order to cover 10,000+ units. The decision is now quantified, not qualitative.

She can also update this probability as each week passes. If week 53 comes in at 11,400, the posterior updates: P(demand > 10,000 in week 54) rises. If week 53 comes in at 9,200, P falls. The forecast learns.

---

## Side-by-Side Comparison

| | ARIMA(1,1,1) | Bayesian structural time series |
|---|---|---|
| Point forecast (week 53) | 10,840 units | 10,780 units (posterior mean) |
| Interval type | 95% prediction interval | 95% posterior predictive CrI |
| Interval | [8,200, 14,600] | [7,720, 13,840] |
| P(demand > 10,000) | Requires additional assumption | 0.69 — directly from posterior |
| Sequential updating | Refit model on all data | Update posterior with new observation |
| Seasonal component | Integrated via differencing | Explicit component, can be inspected |
| Computation | Fast, closed form | MCMC required; slower |
| Prior required | No (implicit flat prior on trend) | Yes — on initial level, trend, variances |
| Forecasting accuracy | Strong for stationary series | Comparable; advantage in decision support |

### Why Anyone Uses ARIMA

The forecasting competition literature (M4, M5 competitions, Makridakis and collaborators) consistently finds that simple methods — including ARIMA and exponential smoothing — perform as well or better than complex Bayesian models on raw forecast accuracy. BSTS does not systematically beat ARIMA on RMSE.

The Bayesian advantage is not raw forecasting accuracy. It is the output format: a full posterior predictive distribution rather than a point forecast plus an interval. For decisions that require probability statements about future thresholds (stocking out, recession, clinical event rates), the full distribution is essential. For decisions that require only a rough planning estimate, ARIMA is faster, simpler, and widely enough understood that its outputs need no explanation.

ARIMA is also the industry-standard tool in econometrics, epidemiology (Box-Jenkins methods are taught in every time series econometrics course), and operations research. Its outputs are expected by journals, regulators, and forecasting committees. The Bayesian approach earns its complexity cost when the decision format requires it; otherwise ARIMA is a perfectly reasonable choice.

Scott & Varian (2014) demonstrate BSTS forecasting initial unemployment insurance claims using Google search queries as regressors — a real, public dataset (available via FRED and the `bsts` R package) where the Bayesian approach enables variable selection and nowcasting. Their paper is the closest thing to a verified empirical anchor for this chapter's claims. For weekly employment data — which ties directly to the book's BLS companion datasets — BSTS with Google Trends regressors outperforms ARIMA on short-horizon nowcasting in that specific context. Do not generalize beyond what they demonstrated.

---

## Worked Example: Updating a Demand Forecast

**Situation:** The manager has 40 weeks of demand history. She runs a BSTS model and produces a week-41 through week-52 forecast. Then week 41 arrives: actual demand is 11,800 units, substantially above the model's week-41 forecast of 10,600.

**Question:** How does this update the forecast for weeks 42–52? Should she revise her order quantities?

**Process:**

Step 1: With 40 weeks of data, the posterior on the state at week 40 has mean $\mu_{40} = 10,500$, trend $\delta_{40} = 48$ units/week. P(demand > 10,000 in week 52) = 0.74.

Step 2: Observe week 41 = 11,800. This is 1,200 units above the model's prediction. Update the posterior:

$$\text{posterior mean} \approx 10,500 + 48 + K \times (11,800 - (10,500 + 48))$$

where $K$ (the Kalman gain) depends on the ratio of observation variance to total prediction variance. With typical parameters (high observation noise relative to level noise), $K \approx 0.4$. The update shifts the level estimate up by about $0.4 \times 1{,}252 = 501$ units.

Updated state: $\mu_{41} \approx 11,049$, trend $\delta_{41} \approx 52$ (trend adjusted upward slightly by the above-average observation).

Step 3: With week 41 incorporated, the posterior predictive for week 52 shifts up. P(demand > 10,000 in week 52) rises from 0.74 to approximately 0.86.

**Dead end encountered:** The manager asks: "should I also revise my supplier contract, which assumes a flat demand profile?" The BSTS model gives her the posterior predictive distribution — it does not tell her the optimal contract revision. That requires a decision model layered on top of the forecast. The BSTS model is decision-relevant input, not a decision.

**Resolution:** Use the posterior predictive to compute expected cost of three contract scenarios (current, 10% increase, 20% increase) weighted by P(demand in each range). The optimal contract minimizes expected cost. The BSTS model quantifies the probabilities; the manager specifies the cost structure.

**Lesson:** Sequential updating narrows forecast uncertainty as observations arrive. A model that cannot update is discarding information. The lesson is not "always use Bayesian methods for time series" — it is "match the output format to the decision format."

**Limit:** The worked example uses a linear Gaussian model, where Kalman filtering gives exact updates. For nonlinear or non-Gaussian series (demand with hard lower bound at zero, for example), exact sequential updating is not available and requires approximations (particle filters, variational inference). The chapter's results do not generalize automatically to those settings.

---

## Prompting for Implementation

### Fitting ARIMA

A reliable prompt for ARIMA:

> I have 52 weekly demand observations stored in a vector called `demand`. Please fit an ARIMA model using `auto.arima` from the `forecast` package in R (or `auto_arima` from `pmdarima` in Python). Report: the selected (p,d,q) orders, the point forecast for weeks 53–65, the 95% prediction intervals, and the residual diagnostics (Ljung-Box test for autocorrelation in residuals). Interpret the results in plain language.

Verify the output: if the Ljung-Box p-value is below 0.05, residuals are autocorrelated and the model is misspecified. Ask the LLM to try a higher-order model.

### Fitting BSTS

Specifying a BSTS model requires more precision:

> I have 52 weekly demand observations stored in `demand`. Please fit a Bayesian structural time series model using the `bsts` package in R. Use a local linear trend component. Specify these priors:
> - Initial level: Normal(8000, 1000)
> - Initial slope: Normal(50, 100)
> - Observation SD: Half-Normal(0, 500)
> - Level SD: Half-Normal(0, 50)
> - Slope SD: Half-Normal(0, 5)
>
> Run 4,000 MCMC iterations (2,000 warmup). Report: (a) the posterior predictive distribution for weeks 53–65, (b) P(demand > 10,000) for each forecast week, (c) the posterior means and 95% CrIs for the level and slope at week 52, and (d) a trace plot to verify MCMC convergence.

**Verification steps:**
1. Check trace plots: if the chains look like random noise with no drift or spikes, the MCMC has converged.
2. Check the week-52 posterior mean for the level: it should be close to the observed demand at week 52.
3. Check P(demand > 10,000 at week 53): it should be plausible given that the week-52 observation was near 11,000.
4. Ask the LLM to plot the fitted values against observed data for weeks 1–52. If the model tracks the data reasonably well (not perfectly — some smoothing is expected), specification is plausible.

**Aging note (2026):** LLM-generated `auto.arima` code is reliable and well-tested. LLM-generated `bsts` code is variable — the package is less commonly in training data. If `bsts` code fails, ask for the PyMC or Stan equivalent, or for the `prophet` package as a simpler BSTS-adjacent alternative. The statistical content of this section is stable; the specific package recommendations may evolve.

---

## Common Misconceptions

### 1. "The prediction interval tells me the probability demand will be above the threshold."

No — not without an additional assumption. The ARIMA prediction interval is a frequentist interval: 95% of such intervals, constructed from this procedure, will contain the true future value. This is a guarantee about the procedure, not a probability statement about this particular forecast. To get P(demand > threshold), you need either to assume the forecast error is normally distributed and compute from the normal CDF, or to use a model — like BSTS — that produces a posterior predictive distribution directly.

The distinction matters less for large symmetric intervals and more when the threshold is near the edge of the interval or when the forecast error distribution is non-normal (which ARIMA does not guarantee for all data).

### 2. "The Bayesian model is more accurate than ARIMA."

Not necessarily. Forecast competition evidence (M4 Competition: Makridakis, Spiliotis, & Assimakopoulos 2020 [verify]; M5 Competition 2020) consistently finds that simple methods are competitive with complex Bayesian models on raw accuracy metrics (RMSE, MASE). The Bayesian advantage is in the decision-support format: a full posterior predictive distribution rather than a point estimate plus interval. If the decision requires only a point forecast, there is no reliable accuracy advantage to the Bayesian approach, and you should use the simpler tool.

### 3. "Sequential updating means I get a new posterior every week without refitting the model."

Exactly right conceptually — and more nuanced in practice. True sequential updating (the Kalman filter for Gaussian models) updates the state estimate each week without refitting from scratch: you propagate the previous posterior through the transition model and update with the new observation. This is what the BSTS framework does in principle.

In practice, most practitioners refit the entire model periodically (monthly or quarterly) rather than running a true online update, because hyperparameters ($\sigma_\varepsilon$, $\sigma_\eta$, $\sigma_\zeta$) may also need updating as patterns change. The conceptual purity of sequential updating is real; the production implementation is often more pragmatic. Do not overclaim.

---

## AI Wayback Machine

**Rudolf Emil Kálmán (1930–2016)**

In 1960, Rudolf Kálmán published a paper in the *Journal of Basic Engineering* (Kalman 1960) that solved a problem the US space program urgently needed solved: how to estimate a rocket's position in real time from noisy radar measurements, updating the estimate with each new reading.

The Kalman filter, as it came to be known, is a recursive Bayesian algorithm for linear Gaussian systems: given the current state estimate (a Gaussian distribution) and a new noisy observation, it computes the updated state estimate (another Gaussian). The posterior from step $t$ becomes the prior for step $t+1$. Every GPS receiver, every smartphone navigation app, and the Apollo guidance computer that landed humans on the Moon all run variants of this algorithm.

Kálmán was born in Budapest in 1930, trained as an electrical engineer (PhD Columbia, 1957), and worked at the Research Institute for Advanced Study in Baltimore when he wrote the 1960 paper. He emigrated from Hungary to the US in 1943; his career spanned control theory, systems engineering, and applied mathematics rather than statistics per se — which is part of why his contribution to Bayesian inference is less widely recognized in statistics education than it deserves to be. President Obama awarded him the National Medal of Science in 2009.

The connection to this chapter is direct: the Kalman filter is Bayesian sequential updating, made algorithmic. Every BSTS model runs the Kalman filter (or an approximation to it) at its core. Kálmán was doing Bayesian inference before "Bayesian" was a common term in statistics.

Anchor prompt: *"Explain Rudolf Kálmán's 1960 filter in plain language: what does it mean to say that a Kalman filter is doing Bayesian updating at each time step, and how does this connect to the BSTS models we use for demand forecasting?"*

---

## Exercises

**1. (Apply)** Using BLS employment data for an occupation category of your choice (available at the companion website or via the BLS API), fit both an ARIMA model and a Bayesian structural time series model. Compare the 12-week forecasts: point estimates, interval widths, and — for the BSTS model — P(employment > a threshold you choose). Report which model you would use for a planning decision and why.

**2. (Analyze)** The ARIMA prediction interval for week 53 is [8,200, 14,600] units. A colleague says: "There's a 95% chance demand will be between 8,200 and 14,600." Explain precisely what is wrong with this statement. Then explain what the interval does mean, and how you would compute P(demand > 10,000) from it if you had to — along with what additional assumption you would need.

**3. (Evaluate)** The manager's reorder threshold is 10,000 units, and stocking out costs 3× excess inventory. Using the BSTS posterior predictive P(demand > 10,000) = 0.69 from the chapter, compute the expected cost of: (a) ordering for 10,000 units, and (b) ordering for 11,000 units. (Assume: excess inventory of 1,000 units costs $c$; a stockout of 1,000 units costs $3c$.) Which order quantity minimizes expected cost? What would change your recommendation?

**4. (Production)** Prompt an LLM to fit a BSTS model to the weekly demand data from the chapter (use the 52-observation illustrative series, or the BLS data from Exercise 1). Verify: (a) MCMC convergence via trace plots, (b) that the week-52 level estimate is close to observed week-52 demand, and (c) that P(demand > 10,000) is consistent with where the forecast distribution falls. Report what you had to correct or iterate.

---

## What Would Change My Mind

**ARIMA is the right tool when:**
- The decision requires only a rough point forecast or a confidence bound.
- The data is stationary or can be made stationary by differencing.
- Computation time is constrained and MCMC is not feasible.
- The forecasting audience expects standard time series output and cannot be walked through posterior predictive distributions.

**BSTS earns its cost when:**
- The decision requires P(future value > threshold) — directly.
- The manager will update the forecast week by week and wants a principled update rule.
- External variables (search queries, leading indicators) are available for inclusion via the BSTS regression component.
- The trend is expected to change over time (which the local linear trend model handles naturally).

If forecasting competition evidence consistently showed that BSTS outperformed ARIMA on raw accuracy across diverse settings, I would weight the Bayesian approach more heavily even when decisions only require point estimates. The current evidence (M4, M5) does not support this claim, and I will not make it.

---

## Still Puzzling

1. **How much does prior specification affect BSTS forecasts?** For the signal-to-noise ratio parameters, there is no consensus on weakly informative defaults. Different practitioners use different scales, and the implied smoothing varies substantially. A prior sensitivity analysis (Chapter 7's method applied here) is the right response, but the chapter cannot specify a single correct default.

2. **True sequential updating versus periodic refitting:** The conceptual case for sequential updating is clean. The production case is messier: hyperparameters may drift, structural breaks may occur, and refitting on all data periodically is often more reliable than strict online updating. How to teach the gap between the clean theory and the messier practice without undermining the theory is an unsolved pedagogical problem.

3. **Deep learning and foundation models for time series:** Transformer-based models (Amazon Chronos [verify publication status], Nixtla TimeGPT [verify]) and similar architectures now produce competitive short-horizon forecasts. They are not Bayesian and do not produce calibrated uncertainty estimates. Whether they eventually displace ARIMA and BSTS for production forecasting is genuinely unclear as of 2026. [AGING — verify model and publication status before print.]

4. **Seasonal adjustment and BLS data:** BLS employment series are already seasonally adjusted using X-13ARIMA-SEATS — a frequentist seasonal decomposition procedure. Students using BLS data from the companion website may not realize they are working with pre-processed data. Flag this in the companion dataset documentation.

---

## Bridge to Chapter 11

Chapter 10 used sequential structure to make the Bayesian updating story vivid. Every new observation is a chance to update; every posterior is the prior for the next step.

Chapter 11 turns to a different kind of output: not a forecast of a continuous quantity, but a classification decision — loan approved or declined, occupation at-risk or not, email spam or legitimate. The model still produces a probability. But converting that probability to a decision requires something the model cannot supply: a loss function. What does it cost to get it wrong, and which kind of wrong costs more? That is the question Chapter 11 builds a framework to answer.

---

*Sources: Box & Jenkins (1970); Kalman (1960); Harvey (1989); Scott & Varian (2014); Brodersen et al. (2015). Inventory demand series is illustrative — labeled as such. BSTS numerical results are illustrative based on the structure in Scott & Varian (2014). Forecasting competition accuracy claims refer to M4/M5 competitions [verify full Makridakis et al. 2020 citation before print].*
