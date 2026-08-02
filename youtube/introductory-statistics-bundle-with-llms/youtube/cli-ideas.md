# Introductory Statistics Bundle with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Simulate the Literary Digest Bias with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/01-sampling-and-data.md + LLM Exercise Ch.1
- Lane: BUILD (Claude Code)
- Hook: The Literary Digest had 2 million responses and missed the 1936 election by 18 points. A biased sample of 2 million beats a good sample of 2 thousand — build the simulation and watch size fail.
- The artifact: A Python simulation comparing two sampling procedures over 1000 trials: (A) a biased sample of 2M drawn from a population that overrepresents wealthy voters (true support for candidate = 45%, biased population support = 57%), and (B) an unbiased SRS of 50K. Plot the distribution of estimated candidate support across 1000 trials for each method. The biased method's distribution is centered at 57%; the unbiased at 45%. Rendered as Manim with two overlapping sampling distributions animating in.
- Prompt seed: `claude "Write Python code to simulate 1000 elections comparing two sampling methods. Population: true_support=0.45. Method A: biased sample n=2000000, p_in_sample=0.57 (wealthy-skewed). Method B: unbiased SRS n=50000, p_in_sample=0.45. For each method: simulate 1000 poll estimates using np.random.binomial. Plot two overlapping histograms of the estimates with vertical lines at 0.45 (true) and 0.57 (biased). Return matplotlib code."`
- Read / check: Verify Method A's distribution centers at 0.57 (not 0.45); verify Method B's distribution centers at 0.45 and is tighter (larger n); verify the visual clearly shows Method B is closer to truth despite smaller n.
- Human supplies: Nothing — fully synthetic. The 1936 parameters are illustrative approximations of the actual Literary Digest disaster.
- Output medium: Manim (two distributions animate in overlapping; vertical dashed lines mark truth at 0.45 and bias at 0.57; gap between Method A peak and truth is annotated as "the bias — size cannot fix this")
- The change: Increase Method A's sample to 10 million and show the distribution tightens but stays centered at 0.57. The bias persists exactly. Size made confidence increase while accuracy stayed wrong.
- Teardown angle: Bias and variance are orthogonal. A large biased sample is highly confident in the wrong answer — the worst possible configuration. Method matters more than size.
- Exclusions: No political science history, no modern polling methodology, no nonresponse bias beyond the one concept used.
- Score: 10/10

---

## Candidate 02 — Build the CLT Convergence Demonstration with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/07-the-central-limit-theorem.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The Central Limit Theorem says that sample means are normally distributed regardless of the original population's shape. Build it live: start with a skewed population, watch the sampling distribution become a bell.
- The artifact: A 4-panel Manim animation: panel 1 = the original skewed population (exponential), panels 2–4 = sampling distributions of the mean for n=5, n=30, n=100. Each panel draws a theoretical normal overlay. The transition from "definitely not a bell" to "unmistakably a bell" is the lesson.
- Prompt seed: `claude "Write Python code to demonstrate the CLT. Population: exponential(scale=2), n_pop=10000. For n_samples=[5, 30, 100]: draw 3000 samples of size n, compute sample means, plot histogram of means. Overlay the theoretical normal N(mu=2, sigma=2/sqrt(n)) as a smooth curve. Arrange as 1 row, 3 subplots. Title each subplot 'n={n}'. Population histogram in a 4th panel on the left. Return matplotlib code."`
- Read / check: Verify the exponential population is visibly right-skewed; verify the n=5 distribution is not yet bell-shaped; verify the n=100 distribution closely matches the overlaid normal; verify the theoretical mean=2 and sigma=2/sqrt(n) are correct.
- Human supplies: Nothing — fully synthetic. The exponential distribution is chosen because it is maximally non-normal: one-sided, right-skewed, bounded below.
- Output medium: Manim (population panel appears first; then n=5, n=30, n=100 panels animate in sequentially, each with the theoretical normal curve drawing in last)
- The change: Replace the exponential population with a bimodal distribution (two bumps) and show the same convergence — proving "any population" means any population, not just well-behaved ones.
- Teardown angle: The CLT is the reason inferential statistics works. Without it, every population would require a custom inference method. With it, one framework covers nearly everything.
- Exclusions: No proof of the CLT, no characteristic functions, no moment-generating functions. Shape → shape → shape → normal. That is the whole video.
- Score: 10/10

---

## Candidate 03 — Build the Confidence Interval Factory with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/08-confidence-intervals.md + LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: "95% confidence" does not mean there is a 95% chance the true mean is in your interval. It means the procedure works 95% of the time. Build 100 intervals and count the misses.
- The artifact: A Manim animation of 100 confidence intervals for a known population mean: 100 horizontal line segments stacked vertically, each built from a different sample. 5 of them (approximately) miss the true mean and are colored red. A vertical dashed line marks the true mean. The viewer watches intervals accumulate and the red ones fail.
- Prompt seed: `claude "Write Python code to visualize confidence interval coverage. Population: N(mu=50, sigma=10). Draw 100 samples of n=30. For each: compute 95% CI using t-distribution. Plot 100 horizontal CIs stacked vertically, colored green if they contain mu=50, red if not. Add a vertical dashed line at mu=50. Count and display red intervals. Return matplotlib code."`
- Read / check: Verify the CI formula uses t.ppf(0.975, df=29) correctly; verify intervals are centered at the sample mean (not at mu); verify the vertical line at mu=50 is labeled; verify approximately 5 intervals miss (±3 is fine for 100 trials).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (intervals appear one by one animating downward; each one colors green or red as it appears; counter in corner shows running "misses: N/100")
- The change: Change confidence level to 99% and rebuild — show that intervals widen and fewer miss. Show the trade: more confidence = wider net.
- Teardown angle: The procedure is the unit. Not "this interval." The interval already exists; the probability already resolved. What the 95% measures is the quality of the factory, not the contents of the current box.
- Exclusions: No Bayesian credible intervals, no bootstrap CIs, no comparison between z and t critical values beyond a single sentence.
- Score: 9/10

---

## Candidate 04 — Measure p-Hacking's Family-Wise Error Rate with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/09-hypothesis-testing-with-one-sample.md (§p-hacking section)
- Lane: BUILD (Claude Code)
- Hook: If you run 20 independent hypothesis tests at α=0.05 on null effects, you're nearly guaranteed to find at least one "significant" result by chance. Build the math and watch the false-positive rate explode.
- The artifact: A Manim animated line chart: x-axis = number of independent tests (1 to 50), y-axis = probability of at least one false positive = 1 - 0.95^k. A horizontal dashed line at α=0.05. The curve starts at 0.05, crosses 0.5 around k=14, and approaches 1 by k=50. A vertical marker shows k=20 with the probability labeled.
- Prompt seed: `claude "Write Python code to plot the family-wise error rate for multiple hypothesis testing. x = range(1, 51). y = 1 - 0.95**x. Plot y vs x. Add: (1) horizontal dashed line at y=0.05 labeled 'single-test alpha', (2) vertical line at x=20 labeled 'k=20 tests', (3) horizontal annotation showing P(at least one false positive) at x=20. Title: 'Running 20 tests at alpha=0.05: 64% chance of at least one false positive'. Return matplotlib code."`
- Read / check: Verify y at x=20 = 1-0.95^20 ≈ 0.641; verify the curve shape is correct (concave, approaching 1); verify all three annotations appear correctly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (curve draws from left to right; horizontal alpha line appears; vertical k=20 marker drops; probability label pops in)
- The change: Add a second curve for Bonferroni-corrected alpha (α/k per test) showing the family-wise error rate held flat at 0.05. Show the cost: individual test power drops.
- Teardown angle: p-hacking isn't fraud — it's the inevitable consequence of running many tests and reporting only the winners. The fix isn't more honesty; it's pre-registration and multiple-testing correction baked into the procedure.
- Exclusions: No FDR vs FWER debate, no Benjamini-Hochberg, no replication crisis sociology. One equation, one chart, one lesson.
- Score: 9/10

---

## Candidate 05 — Build the Type I / Type II Error Trade-off Visualizer with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/09-hypothesis-testing-with-one-sample.md (§Two kinds of error)
- Lane: BUILD (Claude Code)
- Hook: Lowering α reduces false positives — but raises false negatives. The errors are in tension. Build the trade-off and find the crossing point for a specific decision.
- The artifact: A 2-panel Manim chart: left panel = two overlapping normal distributions (H0 and Ha), with a moveable rejection boundary; right panel = Type I error rate and Type II error rate as functions of the boundary position. As the boundary moves right, Type I falls and Type II rises. The two error curves cross at the "balanced" threshold.
- Prompt seed: `claude "Write Python code to visualize Type I/II error trade-off. H0: N(0,1), Ha: N(2,1). Threshold sweeps from -3 to 5. For each threshold: alpha = P(Z > threshold | H0) = 1 - norm.cdf(threshold, 0, 1); beta = P(Z <= threshold | Ha) = norm.cdf(threshold, 2, 1). Plot two panels: (1) both distributions with shaded alpha and beta regions at threshold=1.65; (2) alpha and beta as functions of threshold. Mark the crossing point where alpha=beta. Return matplotlib code."`
- Read / check: Verify alpha at threshold=1.645 ≈ 0.05; verify beta at threshold=1.645 for Ha~N(2,1) is approximately norm.cdf(1.645, 2, 1) ≈ 0.36; verify the crossing point is correctly identified; verify both panels reference the same threshold value.
- Human supplies: Nothing — fully synthetic. The N(0,1) vs N(2,1) separation is illustrative.
- Output medium: Manim (threshold bar slides left/right; both panels update simultaneously; when threshold hits 1.645, an annotation labels it "conventional alpha=0.05" with the beta labeled)
- The change: Increase the separation between H0 and Ha (move Ha mean from 2 to 3) and show that both error rates drop simultaneously — this is the "effect size" lesson: larger true effects are easier to detect.
- Teardown angle: The crossing point has no special significance — the right threshold is determined by the cost of each error in context, not by mathematical balance. The camping bag example from the chapter makes this visceral.
- Exclusions: No power analysis formula derivation, no sample size calculation, no Cohen's d. Two distributions, one threshold, one trade-off.
- Score: 9/10

---

## Candidate 06 — Visualize the Normal Distribution Empirical Rule with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/06-the-normal-distribution.md + LLM Exercise Ch.6
- Lane: BUILD (Claude Code)
- Hook: 68-95-99.7. Three numbers cover almost all of statistics. Build the visual and verify them from first principles — not a lookup table.
- The artifact: A standard normal bell curve with three nested shaded bands: ±1σ (68%), ±2σ (95%), ±3σ (99.7%). Each band fades in separately, with the percentage labeled inside. The tail areas outside ±3σ are labeled as 0.15% each. Rendered as Manim with each band appearing in sequence.
- Prompt seed: `claude "Write Python code to draw the standard normal bell curve with three nested shaded regions: (1) -1 to 1 sigma (shade in blue, label '68%'), (2) -2 to 2 sigma (shade in lighter blue, label '95%'), (3) -3 to 3 sigma (shade lightest blue, label '99.7%'). Compute probabilities analytically using scipy.stats.norm. Verify: print norm.cdf(1)-norm.cdf(-1), norm.cdf(2)-norm.cdf(-2), norm.cdf(3)-norm.cdf(-3). Label left tail beyond -3 as '0.15%' and right tail '0.15%'. Return matplotlib code."`
- Read / check: Verify the three probability computations match 68.27%, 95.45%, 99.73% respectively; verify the nested shading is visible (lighter outward); verify all label positions are inside the shaded regions and readable.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (bell curve draws first; then three bands fade in one by one from inside to outside; tail labels appear last)
- The change: Show what the empirical rule means for IQ scores (mu=100, sigma=15): label the actual IQ values at each boundary (85/115, 70/130, 55/145) and shade bands on the IQ scale.
- Teardown angle: The three numbers are memorable because they come from the math, not from convention. The bell curve's tails decay so fast that 99.7% of events land within 3 standard deviations — which is why extreme events ("more than 3 sigma") feel genuinely surprising.
- Exclusions: No z-table mechanics, no Q-Q plot, no normality testing. One distribution, three bands, three numbers.
- Score: 9/10

---

## Candidate 07 — Build the Standard Error "Square Root Law" with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/07-the-central-limit-theorem.md (§standard error section)
- Lane: BUILD (Claude Code)
- Hook: To halve the standard error you need to quadruple the sample size. That diminishing return has enormous practical consequences for every poll, clinical trial, and A/B test. Build the curve.
- The artifact: A Manim animated line chart: x-axis = sample size n (1 to 1000), y-axis = standard error = sigma/sqrt(n), for sigma=10. Three key points labeled: n=25 (SE=2), n=100 (SE=1), n=400 (SE=0.5). A "cost-to-halve" arrow appears between each labeled point, annotating the 4× cost.
- Prompt seed: `claude "Write Python code to plot standard error vs sample size. sigma=10, n_range = np.arange(1, 1001). se = sigma / np.sqrt(n_range). Plot se vs n_range. Add vertical dotted lines at n=25, 100, 400. Label each: (n=25, SE=2.0), (n=100, SE=1.0), (n=400, SE=0.5). Add horizontal brackets between n=25 and n=100 labeled '4x n to halve SE'. Add between n=100 and n=400 same label. Title: 'The Square Root Law: doubling precision costs 4x the data'. Return matplotlib code."`
- Read / check: Verify SE at n=25 = 10/5 = 2.0, at n=100 = 10/10 = 1.0, at n=400 = 10/20 = 0.5; verify the brackets correctly span n=25-to-100 and n=100-to-400; verify the curve is concave (diminishing returns visible).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (curve draws left to right; vertical markers drop at n=25, 100, 400; labels appear; then brackets animate in with "4× cost" labels)
- The change: Add a cost axis (cost = n × $1/data_point) on the right y-axis, showing the dollar cost of each standard-error reduction. The diminishing returns become spending decisions.
- Teardown angle: The square root law is why pharmaceutical companies don't just run bigger trials to get more precision — there's a point of diminishing return where the next standard-error gain costs more than the drug approval is worth.
- Exclusions: No formal proof of CLT, no bias/variance tradeoff, no power analysis.
- Score: 9/10

---

## Candidate 08 — Build the Regression-to-the-Mean Visualizer with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/13-linear-regression-and-correlation.md
- Lane: BUILD (Claude Code)
- Hook: A student scores 85 on the midterm. The regression line predicts they'll score 86.29 on the final — not 89 or 91. The 2.71-point "shortfall" is not random; it's regression to the mean, and it's encoded in the slope.
- The artifact: A scatter plot (midterm vs. final) with the regression line, the mean point (x̄, ȳ), and two annotated data points: the student at (85, actual) and the predicted point (85, 86.29). Arrows show the midterm deviation (+11 from mean) and the predicted final deviation (+10.29 from mean), with the fraction labeled as r × (sy/sx) = 0.935. Rendered as Manim with annotations appearing sequentially.
- Prompt seed: `claude "Write Python code to demonstrate regression to the mean. Generate 25 synthetic exam data points with rho=0.85, xbar=74, ybar=76, sx=10, sy=11 (use np.random.multivariate_normal). Compute b1 = r*(sy/sx), b0 = ybar - b1*xbar. Plot scatter, regression line, horizontal line at ybar, vertical line at xbar, and the mean point (xbar, ybar) as a bold dot. Annotate point at x=85: draw vertical brackets showing 11-unit deviation from xbar and 0.935*11=10.29 deviation from ybar on the prediction. Return matplotlib code."`
- Read / check: Verify b1 = 0.85*(11/10) = 0.935; verify b0 = 76 - 0.935*74 = 6.81; verify predicted y at x=85 = 6.81+0.935*85 = 86.285; verify the bracket showing regression-toward-mean shrinks from 11 to 10.29.
- Human supplies: Nothing — fully synthetic. Synthetic data generated with the correct correlation structure serves the lesson identically to real exam data.
- Output medium: Manim (scatter plots first; regression line draws; mean lines appear; brackets animate showing the midterm deviation and the smaller predicted final deviation)
- The change: Drop r from 0.85 to 0.50 and show how the predicted deviation shrinks further (from 11 to 5.5) — the weaker the correlation, the more regression toward the mean.
- Teardown angle: Galton named this "regression" because the children of tall fathers regress toward the population mean. It is not noise — it is the predictable consequence of imperfect correlation. Any time you predict from a correlated variable, regression to the mean is already baked in.
- Exclusions: No multiple regression, no causal inference debate, no R-squared decomposition beyond one sentence.
- Score: 9/10

---

## Candidate 09 — Simulate the p-value Misconception with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/09-hypothesis-testing-with-one-sample.md (§What the p-value is not)
- Lane: BUILD (Claude Code)
- Hook: A p-value of 0.04 does not mean there's a 96% chance the drug works. It's the probability of the data given H0, not the probability of H0 given the data. The difference is not subtle — it's the difference between making the right call and the wrong one.
- The artifact: A 2-panel infographic (Manim): left panel = "what the p-value measures" (arrow from H0 to data), right panel = "what we want to know" (arrow from data to H0). Between them: a large ≠ symbol. A worked Bayes' theorem example shows that P(H0|data) requires a prior and is always different from P(data|H0).
- Prompt seed: `claude "Write Python code to compute a Bayes' theorem example contrasting p-value with posterior. Setup: P(data|H0)=0.04 (p-value), P(H0)=0.90 (prior, 90% of tested drugs don't work), P(data|Ha)=0.80 (power). Compute P(data) = P(data|H0)*P(H0) + P(data|Ha)*P(Ha). Compute posterior P(H0|data) = P(data|H0)*P(H0)/P(data). Print all values clearly labeled. Plot as a 2-row table with LaTeX labels. Return code."`
- Read / check: Verify P(data) = 0.04*0.90 + 0.80*0.10 = 0.036+0.08 = 0.116; verify P(H0|data) = 0.036/0.116 ≈ 0.31; verify the result is labeled as "31% chance H0 is true given the data" — NOT 4%.
- Human supplies: Nothing — fully synthetic. The 90% prior is illustrative (matching the "most tested drugs don't work" intuition from clinical research).
- Output medium: Manim (two-arrow diagram animates; Bayes table fills in line by line; the final result "P(H0|data)=31%" appears in large type beside "p-value=0.04" to show the gap)
- The change: Change the prior P(H0) to 0.50 (equally likely) and show how the posterior changes — making the prior sensitivity visible and the point that "p-value as posterior probability" requires knowing the prior.
- Teardown angle: The p-value is not the probability you care about. It runs in the wrong direction. Getting this right is the difference between scientific reasoning and statistical theater.
- Exclusions: No full Bayesian statistics, no MCMC, no prior selection theory. One worked example, one diagram, one distinction.
- Score: 9/10

---

## Candidate 10 — Analyze a Real Dataset End-to-End: Descriptive Statistics with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/02-descriptive-statistics.md + LLM Exercise Ch.2
- Lane: BUILD (Claude Code)
- Hook: Mean vs. median: the same 43 engineers produce an average salary of $95,000 and a median of $51,500. Both are correct. Build the visualization that shows why one is honest and one is a lie.
- The artifact: A synthetic salary dataset (42 junior engineers + 1 principal engineer) with: histogram showing right skew, a mean line ($95K) vs. median line ($51.5K), and a box plot revealing the outlier. Manim animated, with the mean vs. median gap labeled as "the gap that recruiters exploit."
- Prompt seed: `claude "Write Python code to analyze a salary dataset. Create: 42 salaries sampled uniformly from (48000, 62000) plus one salary of 780000. Compute mean, median, IQR. Plot side by side: (1) histogram with vertical lines at mean (red) and median (blue), labeled; (2) horizontal box plot showing the outlier as a point. Title: 'Same 43 people. Different honest numbers.' Return matplotlib code."`
- Read / check: Verify mean ≈ $95K (the outlier should drag it significantly); verify median ≈ $51-55K (depends on the random draw but should be well below mean); verify the outlier ($780K) appears as an individual point on the box plot beyond the upper whisker.
- Human supplies: Nothing — fully synthetic. The dataset is deliberately constructed to illustrate the concept; a real salary dataset from Glassdoor/LinkedIn would be more authentic but is not required.
- Output medium: Manim (histogram draws; mean line slides in from left labeled "mean: $95K"; median line appears labeled "median: $51.5K"; then box plot appears below with the outlier point visible)
- The change: Remove the outlier and show how both statistics converge — making the point that the outlier isn't wrong, it just changes which statistic is informative.
- Teardown angle: Mean and median are both correct descriptions of the same data. The question is which one answers the question you're actually asking. For "what does a typical engineer earn?", the median wins. The recruiter who uses the mean is not lying — they are choosing the correct answer to a different question.
- Exclusions: No weighted mean, no geometric mean, no Gini coefficient. One dataset, two statistics, one honest comparison.
- Score: 8/10

---

## Candidate 11 — Research the Replication Crisis: What Statistics Got Wrong with Claude
- Source: introductory-statistics-bundle-with-llms/chapters/09-hypothesis-testing-with-one-sample.md (§p-hacking section)
- Lane: RESEARCH (Claude assistant)
- Hook: The replication crisis revealed that dozens of "statistically significant" findings in psychology and medicine couldn't be reproduced. Research the 4 structural causes and the reforms that followed.
- The artifact: A sourced 4-cause brief: (1) p-hacking, (2) publication bias, (3) underpowered studies, (4) researcher degrees of freedom — each with a specific documented example and the reform proposed to address it. Rendered as a Manim animated cause-reform table.
- Prompt seed: `claude "Research the replication crisis in psychology and medicine. For each of the 4 main structural causes — p-hacking, publication bias, underpowered studies, researcher degrees of freedom — provide: (1) a specific documented finding that failed replication, (2) the estimated scale of the problem (% of studies affected, where known), (3) the main reform proposed. Cite specific sources for each."`
- Read / check: Verify cited failed replications are real (e.g., ego depletion, power posing, social priming); verify the reform column names real initiatives (pre-registration, OSF, registered reports); verify sources are real.
- Human supplies: Nothing — fully synthetic research synthesis is acceptable.
- Output medium: Manim (4-row table builds: cause → example → scale → reform; each row slides in)
- The change: Ask Claude to identify the single reform that would have prevented the most failed replications — and justify the choice with evidence.
- Teardown angle: The crisis was not caused by fraud. It was caused by structural incentives that made p-hacking rational and publication bias inevitable. The fix is procedural, not ethical.
- Exclusions: No sociology of science, no specific lab takedowns, no political dimensions of replication.
- Score: 8/10

---

## Candidate 12 — Build the Confidence Interval Width Calculator with Claude Code
- Source: introductory-statistics-bundle-with-llms/chapters/08-confidence-intervals.md + LLM Exercise Ch.8
- Lane: BUILD (Claude Code)
- Hook: You can control the width of a confidence interval with two levers: sample size and confidence level. They pull in opposite directions. Build the interactive map.
- The artifact: A 2D heat map: x-axis = sample size (n = 10 to 1000), y-axis = confidence level (90%, 95%, 99%), color = CI width = 2 × z* × sigma/sqrt(n). Rendered as Manim with the heat map animating in, then two specific cells highlighted: "n=100, 95%, width=1.96" and "n=400, 99%, width=1.29" showing the trade-off.
- Prompt seed: `claude "Write Python code to create a 2D heatmap of confidence interval width. sigma=10. x-axis: n_values = [10, 25, 50, 100, 200, 400, 1000]. y-axis: confidence levels with z_stars = [1.645, 1.96, 2.576] for 90%, 95%, 99%. Width = 2 * z_star * sigma / sqrt(n). Plot as imshow with n on x-axis, confidence level on y-axis, color = width. Add text in each cell showing the width rounded to 1 decimal. Title: 'CI Width: two levers, opposite effects'. Return matplotlib code."`
- Read / check: Verify width at n=100, z*=1.96 = 2*1.96*10/10 = 3.92; verify width decreases left-to-right (larger n); verify width increases bottom-to-top (higher confidence); verify all cell values are printed.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (heatmap fades in; then two cells highlighted with annotations showing how to read the trade-off)
- The change: Add a "cost per unit of precision" row — how many additional respondents does each 0.1-unit narrowing of the CI cost at the current sample size?
- Teardown angle: The heatmap makes the abstract concrete: every CI design is a budget decision. More confidence costs more data. More precision costs more data. You can't have both for free.
- Exclusions: No bootstrap CIs, no Bayesian credible intervals. One formula, one heatmap, two levers.
- Score: 8/10
