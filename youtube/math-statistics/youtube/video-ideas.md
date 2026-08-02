# Introductory Statistics Video Ideas

<!-- Scouted 2026-07-09 from 13 narrative chapters -->

## Candidate 01 — Why a 98%-Accurate Test Can Be Wrong 91% of the Time
- Source: `math-statistics/chapters/03-probability-topics.md`
- Topic: STATISTICS
- Hook: A positive mammogram from a test that is 98% accurate sounds nearly certain — but the real chance of cancer can be less than 10%.
- Key case: A woman in her fifties gets a routine mammogram. The test is 98% accurate. It comes back positive. Her doctor estimates a 90% chance she has cancer. The correct answer is about 9%.
- The Question: A test that is right 98% of the time just flagged you. That should mean you're almost certainly sick. So why is the chance of actually having cancer only 9%?
- Core idea: The test's accuracy and the reliability of a positive result are two different conditional probabilities pointing in opposite directions; the base rate of the disease — here just 1% — dilutes true positives with far more common false positives from the healthy majority.
- Visual object: A 10,000-person grid, color-coded by true cancer status, with positive-test squares highlighted — showing 98 true positives drowned by 990 false positives
- Manim move: accumulate
- Example seed: A workplace drug-screening program uses a test that is 95% accurate for both sensitivity and specificity. Only 5% of employees actually use drugs. Of 10,000 employees tested, 475 true positives appear — but so do 475 false positives. A positive test is a coin flip.
- Length band: 3–5 min
- Still lanes: geo (10,000-person grid; conditional-probability arrow diagram), c2v (mammogram machine or petri dish for tone)
- Prerequisites: what a probability is, the idea of conditional probability
- Exclusions: no Bayes' theorem formula or algebraic derivation, no odds-form shortcut, no sensitivity/specificity table formalism, no history of Thomas Bayes
- Score: 10/10

## Candidate 02 — Why Two Million Wrong Answers Are Worse Than Two Thousand Right Ones
- Source: `math-statistics/chapters/01-sampling-and-data.md`
- Topic: STATISTICS
- Hook: The 1936 Literary Digest collected two million survey responses and still missed the presidential election by 18 points — while George Gallup used 50,000 and nailed it.
- Key case: The Literary Digest sends ten million postcards in 1936. Two million come back. They predict Landon beats Roosevelt 57–43. Roosevelt wins 61–39. The largest poll ever run is the most catastrophically wrong.
- The Question: Two million data points should give an almost perfect estimate. So how do you collect two million responses and still be wrong by 18 percentage points?
- Core idea: Sample size controls random error; sample method controls systematic bias — and a biased method with two million responses simply amplifies a wrong answer, because more data never corrects the distortion that was there from the start.
- Visual object: Two balance scales side by side — one overloaded with biased weights all on the same side, one small and balanced at center
- Manim move: compare
- Example seed: A university surveys satisfaction by emailing 8,000 students who use the campus gym. 3,200 respond. The mean satisfaction score is 8.7 out of 10. A stratified random sample of 200 students gets 5.9. The gym-user list is the population measured; the campus is the population that matters.
- Length band: 3–5 min
- Still lanes: geo (bias-vs-variance diagram, two balance scales), c2v (postcard or ballot box for cold open)
- Prerequisites: the idea that a sample tries to estimate a whole population
- Exclusions: no stratified/cluster sampling taxonomy, no math formulas for bias, no discussion of non-response bias as a separate mechanism, no George Gallup biography
- Score: 10/10

## Candidate 03 — Why Averaging Random Chaos Always Produces a Bell
- Source: `math-statistics/chapters/07-the-central-limit-theorem.md`
- Topic: STATISTICS
- Hook: Start with a wildly skewed population — incomes, earthquake sizes, anything non-normal — and the average of random samples still forms a perfect bell curve.
- Key case: Casino payouts follow a wildly skewed distribution: most spins lose small amounts, rare jackpots are enormous. Plot the payout from one spin: ugly, right-skewed blob. Average 30 spins: bell curve, centered exactly on the house's expected take.
- The Question: The distribution of individual casino payouts looks nothing like a bell. So why does the distribution of average payouts — across many sessions of 30 spins — look exactly like one?
- Core idea: When independent random quantities are averaged together, the extreme values in one direction on one draw get canceled by extremes in the other direction on another draw; as the number averaged grows, the cancellation becomes so consistent that the average's own distribution converges to the symmetric bell shape regardless of what the original looked like.
- Visual object: A histogram morphing — starting jagged and skewed, smoothing and narrowing into a bell as the sample size counter ticks up from n=1 to n=30 to n=100
- Manim move: morph
- Example seed: Daily website load times are right-skewed: most pages load in under 1 second, but occasional server spikes hit 20 seconds. Sample 5 load times, average them: still skewed. Sample 40 and average: the histogram of those averages is nearly normal, centered at 1.3 seconds with a tight standard error of 0.08 seconds.
- Length band: 3–5 min
- Still lanes: geo (histogram morph animation frames, standard-error shrink diagram), c2v (casino dice or slot machine for cold-open tone)
- Prerequisites: what a mean is, what a histogram is, the idea that data has a distribution
- Exclusions: no formal CLT proof, no characteristic-function argument, no discussion of when n=30 is insufficient (heavy tails), no law of large numbers distinction in depth
- Score: 10/10

## Candidate 04 — Why "p < 0.05" Does Not Mean "95% Chance the Drug Works"
- Source: `math-statistics/chapters/09-hypothesis-testing-with-one-sample.md`
- Topic: STATISTICS
- Hook: The most-reported number in science — the p-value — is almost universally misread, including by the scientists who compute it.
- Key case: A clinical trial reports p = 0.04. The lead researcher tells the press: "There is a 96% chance the drug works." This statement is wrong in a way that has shaped millions of treatment decisions.
- The Question: A p-value of 0.04 is supposed to tell us how likely the result is. So what does p = 0.04 actually mean — and why does it not mean there's a 96% chance the drug is effective?
- Core idea: The p-value measures P(data this extreme | null hypothesis is true) — not P(null hypothesis is true | this data) — and these two reversed conditionals can differ by a factor of ten, a confusion that is the same error the mammogram-misreading doctor made in Chapter 3.
- Visual object: Two arrows on a probability diagram — one pointing from hypothesis to data (what p measures), one pointing from data to hypothesis (what researchers want) — with a red cross through the wrong direction
- Manim move: compare
- Example seed: A pain medication is tested on 10,000 patients. The mean improvement is 0.3 points on a 100-point scale. The p-value is 0.0001. Statistically significant. Practically: below measurement error for the questionnaire. The p-value confirms the effect is real; it says nothing about whether it matters.
- Length band: 3–5 min
- Still lanes: geo (two-arrow conditional-probability reversal plate), geo (normal curve with rejection region and p-value shading)
- Prerequisites: what a null hypothesis is, the basic idea of random sampling, conditional probability (briefly)
- Exclusions: no Bayesian p-value alternative, no Bonferroni or family-wise correction, no power or Type II error in depth, no replication-crisis history beyond one sentence
- Score: 9/10

## Candidate 05 — What "95% Confident" Actually Means (It's Not What You Think)
- Source: `math-statistics/chapters/08-confidence-intervals.md`
- Topic: STATISTICS
- Hook: Every poll reports a margin of error, but almost every reader — and many researchers — misinterpret what "95% confidence" means.
- Key case: A county health survey reports that the average number of poor-mental-health days is between 9.3 and 11.1, with 95% confidence. The department director tells a reporter: "There's a 95% chance the true average falls in that range." This is technically wrong.
- The Question: If I build a confidence interval and it contains a range, why can't I say there is a 95% probability the true value is inside it?
- Core idea: Once an interval is built, the true parameter either is or isn't inside it — no probability remains; "95% confidence" is a statement about the procedure that built it, not about this particular interval, meaning 95 out of 100 such intervals catch the truth and you cannot tell which yours is.
- Visual object: A stack of 100 horizontal confidence intervals, 95 drawn in one color crossing a vertical true-mean line, 5 drawn in red missing it — with one interval highlighted as "yours"
- Manim move: accumulate
- Example seed: A polling firm surveys 1,000 likely voters and reports 58% approval ± 3.1 points at 95% confidence. The true approval is 55%. This interval (54.9% to 61.1%) misses the truth — but the firm cannot know that. They used a procedure right 95% of the time; this was one of the 5%.
- Length band: 3–5 min
- Still lanes: geo (100-interval stack diagram, margin-of-error parabola), c2v (poll or ballot icon for cold open)
- Prerequisites: what a sample mean is, the idea of sampling variability, z-score basics
- Exclusions: no t-distribution vs. z distinction, no sample-size formula derivation, no proportion-interval formula, no Bayesian credible-interval contrast
- Score: 9/10

## Candidate 06 — Why Cutting Your Margin of Error in Half Costs Four Times as Much
- Source: `math-statistics/chapters/08-confidence-intervals.md`
- Topic: STATISTICS
- Hook: To make a poll twice as precise, you don't need twice as many people — you need four times as many.
- Key case: A news organization runs a poll of 1,000 people and gets ± 3.1% margin of error. Their client demands ± 1%. The firm quotes four times the price — not double. The client is baffled.
- The Question: Precision costs money, but why does halving the margin of error require quadrupling the sample — not doubling it?
- Core idea: The margin of error shrinks as 1/√n, so to cut it in half you must multiply n by 4; each additional unit of precision costs quadratically more, because you are fighting the square-root relationship between sample size and the spread of sample means.
- Visual object: A curve showing required sample size (vertical) against desired margin of error (horizontal) — a hyperbola bending steeply as the margin shrinks below 2%
- Manim move: trace
- Example seed: A school district wants to estimate mean test score within ± 2 points (σ = 10). They need n = 96 students. To get within ± 1 point they need n = 384 — four times as many, for half the margin. The superintendent's budget conversation changes immediately.
- Length band: 2–3 min
- Still lanes: geo (hyperbolic cost curve, standard-error shrink diagram)
- Prerequisites: what a margin of error is, the idea of standard deviation
- Exclusions: no confidence-interval formula derivation, no proportion vs. mean distinction, no t vs. z distinction, no discussion of what happens when n is very large
- Score: 9/10

## Candidate 07 — The Drug Test That Tells You Almost Nothing
- Source: `math-statistics/chapters/03-probability-topics.md`
- Topic: STATISTICS
- Hook: A 95%-accurate drug test, applied to a population where 5% use drugs, gives you a coin-flip result on a positive reading.
- Key case: A company rolls out mandatory drug testing. The test catches 95% of users and correctly clears 95% of non-users. An employee tests positive. HR assumes near-certainty of guilt. The math says 50/50.
- The Question: A test that is 95% accurate just flagged an employee. How is it possible that there is only a 50% chance the employee actually uses drugs?
- Core idea: When the condition being tested is rare relative to the false-positive rate, the absolute number of false positives swamps the true positives — a 95%-accurate test on a 5%-prevalence population produces equal numbers of true and false positive flags.
- Visual object: A 10,000-person grid with drug users in one color (500 squares) and non-users in another; positive-test squares highlighted — showing 475 true positives next to 475 false positives
- Manim move: accumulate
- Example seed: A university screens 2,000 athletes for a banned substance used by about 4% of competitive athletes. The test has 96% sensitivity and 95% specificity. Of 115 positive tests, only 77 are true users — 38 clean athletes face sanctions. The 95%-accurate test is wrong on one-third of its positive flags.
- Length band: 2–3 min
- Still lanes: geo (grid diagram with colored squares), c2v (drug test strip or courtroom for cold open)
- Prerequisites: basic probability, the idea of a false positive
- Exclusions: no Bayes' theorem formula, no sensitivity/specificity table formalism, no policy discussion of how to set the threshold, no mammogram case (that is Candidate 01)
- Score: 9/10

## Candidate 08 — Why Running 20 Experiments Guarantees a False Discovery
- Source: `math-statistics/chapters/09-hypothesis-testing-with-one-sample.md`
- Topic: STATISTICS
- Hook: If you run 20 independent tests at the standard 5% significance level and every null hypothesis is true, you are nearly certain to find a "significant" result.
- Key case: A marketing team runs 20 A/B tests simultaneously on campaigns with no real effect. One test comes back p = 0.03. They launch that campaign. The effect was never real.
- The Question: Each test was run correctly at 5% significance. So how does running 20 correct tests guarantee a wrong answer?
- Core idea: A 5% significance level means you accept a 1-in-20 chance of a false positive per test; run 20 independent tests and the probability of at least one false positive climbs to 64%, making "statistically significant" nearly meaningless when researchers test many hypotheses and report only the winner.
- Visual object: A probability tree or accumulating bar showing the family-wise false-positive rate rising from 5% at 1 test to 64% at 20 tests, continuing upward
- Manim move: accumulate
- Example seed: A pharmaceutical company explores 15 biomarkers as potential drug targets, all in the same patient cohort at α = 0.05. Probability of at least one false significant result: 54%. Three biomarkers show p < 0.05; the one pursued in clinical trials fails to replicate. p-hacking without intent.
- Length band: 2–3 min
- Still lanes: geo (family-wise error rate curve, 20-test probability diagram)
- Prerequisites: what a p-value is, what a significance level means, the idea of independent tests
- Exclusions: no Bonferroni correction formula, no FDR vs. FWER distinction, no pre-registration advocacy, no replication-crisis history beyond the cold-open example
- Score: 9/10

## Candidate 09 — Why the Memoryless Bus Has No Memory of How Long You've Waited
- Source: `math-statistics/chapters/05-continuous-random-variables.md`
- Topic: STATISTICS
- Hook: After waiting 10 minutes for a randomly arriving bus, your intuition says it must come soon — but the math says you're no closer than you were when you arrived.
- Key case: Calls arrive at a help desk at random, averaging one every 4 minutes. The last call was 8 minutes ago. An operator thinks: "It must be coming any second now." The probability of waiting another 2 minutes is exactly the same as it was at minute zero.
- The Question: You've already waited twice the average. The next arrival must be close. Why does probability say you're no closer than when the wait began?
- Core idea: The exponential distribution — which models truly random arrivals — has the memoryless property: the distribution of remaining wait time is identical regardless of how long you have already waited, because constant-rate arrival means each instant has the same fixed probability of being the arrival instant, with no memory of the past.
- Visual object: A timeline with tick marks showing past non-arrivals and the distribution of future wait time — shown identical at minute 0 and at minute 8
- Manim move: compare
- Example seed: A server failure occurs on average once every 200 hours. A server has been running cleanly for 150 hours. The probability it fails in the next 50 hours is the same as for a brand-new server: e^(-50/200) ≈ 22%. The 150 hours of clean running bought zero extra reliability.
- Length band: 2–3 min
- Still lanes: geo (timeline diagram, exponential decay curve with conditional overlay), c2v (bus stop or server rack for cold open)
- Prerequisites: what a probability distribution is, the basic idea of expected value
- Exclusions: no exponential CDF derivation, no Poisson connection, no uniform distribution comparison, no physical wear-out distributions (Weibull), no casino gambler's fallacy (that is a different misconception)
- Score: 9/10

## Candidate 10 — Why the Mean Salary Is a Lie That Is Technically True
- Source: `math-statistics/chapters/02-descriptive-statistics.md`
- Topic: STATISTICS
- Hook: A recruiter quotes an average salary of $95,000. Every number she said is correct. The typical employee makes $51,500.
- Key case: A tech company has 43 employees: 42 junior engineers earning $48,000–$62,000 and one principal earning $780,000. The mean is $95,000. The median is $51,500. Both are accurate. One describes reality; one doesn't.
- The Question: The mean and the median describe the same 43 people with the same salaries. How can two correct averages disagree by $43,500?
- Core idea: The mean is the balance point of the distribution and is dragged toward extreme values; the median is the middle rank and is immune to them; when a distribution is skewed, the mean and median measure different things, and choosing between them is a choice about which question you're actually answering.
- Visual object: A number line with 43 salary weights, showing the fulcrum (mean) pulled far right by one heavy weight, and the median marker sitting still at the 22nd value
- Manim move: transform
- Example seed: A small town has 50 residents: 49 earn $30,000 and one earns $5,000,000. Mean income: $129,400. Median: $30,000. A housing developer citing "average income of $129,400" to justify building luxury condos is using a number that describes zero of the 50 residents.
- Length band: 2–3 min
- Still lanes: geo (number-line balance-point diagram, skewed distribution with mean/median markers), c2v (salary/pay stub icon for cold open)
- Prerequisites: what an average is, the idea of a distribution
- Exclusions: no standard deviation, no IQR, no percentile formula, no mode discussion, no histogram-shape taxonomy
- Score: 9/10

## Candidate 11 — Why Tall Fathers Have Sons Shorter Than Themselves
- Source: `math-statistics/chapters/13-linear-regression-and-correlation.md`
- Topic: STATISTICS
- Hook: The tallest fathers in a generation produce sons who are tall — but shorter than their fathers. The shortest fathers produce sons who are short — but taller than their fathers. This is not noise. It is a mathematical law.
- Key case: Galton plots 1,875 father-son height pairs. He expects perfect inheritance. Instead the regression line has a slope less than 1: a father 4 inches above average has a son only about 2 inches above average. The tallest men reliably produce less-tall sons.
- The Question: Height is heritable. So why don't the tallest fathers produce the tallest sons?
- Core idea: An extreme observed value is partly from a true underlying trait and partly from luck; luck doesn't repeat, so the next observation from the same process regresses toward the population mean by an amount exactly equal to (1 - r) times the original deviation — encoded in the slope of the least-squares line.
- Visual object: A scatter plot of father vs. son heights with the regression line drawn through the cloud — showing the line's slope less than 1, visibly flatter than the "perfect inheritance" 45-degree diagonal
- Manim move: trace
- Example seed: A statistics professor tracks midterm and final exam scores. A student scores 95 on the midterm — 21 points above the mean of 74. With r = 0.85 and equal standard deviations, the predicted final is 74 + 0.85×21 = 91.85. The student "regressed" 3 points toward the mean. The best student in the class should expect a slightly lower final — not because they got worse, but because some of the 95 was luck.
- Length band: 3–5 min
- Still lanes: geo (scatter plot with regression line, slope comparison diagram), c2v (father-and-son silhouettes or height ruler for cold open)
- Prerequisites: what a correlation is, the idea of a mean
- Exclusions: no regression-formula derivation (slope and intercept equations), no r² computation, no residual-plot analysis, no multiple regression, no causal-inference warning (that is a separate card)
- Score: 9/10

## Candidate 12 — Why Running One Test on Five Groups Is Safer Than Running Ten Tests
- Source: `math-statistics/chapters/12-f-distribution-and-one-way-anova.md`
- Topic: STATISTICS
- Hook: Comparing five fertilizers with ten pairwise t-tests gives you a 40% chance of a false positive even when no fertilizer works. One ANOVA keeps that chance at 5%.
- Key case: Fisher, standing in a wheat field in Hertfordshire in the 1920s, needs to compare five fertilizer plots. The obvious approach — test every pair — guarantees a misleading "discovery." He invents a single test instead.
- The Question: Ten separate t-tests each use a 5% significance threshold. That means each has a 95% chance of being correct. So how does running ten correct tests create a 40% false-positive rate?
- Core idea: Independence means the probability of all ten tests being correct is 0.95^10 ≈ 0.60, leaving a 40% chance that at least one of ten false nulls gets rejected by chance; ANOVA asks one joint question — is between-group variation larger than within-group noise? — under a single rejection threshold whose error rate remains exactly α regardless of the number of groups.
- Visual object: A line chart showing the family-wise false-positive rate rising from 5% at 1 comparison to 40% at 10, next to an ANOVA bar staying flat at 5% regardless of group count
- Manim move: compare
- Example seed: A nutritionist tests four protein supplements on 24 participants (6 per group). Six pairwise t-tests at α = 0.05 give a 26% family-wise false-positive rate. The ANOVA F-statistic compares between-group MS to within-group MS in one step — one p-value, 5% error rate.
- Length band: 3–5 min
- Still lanes: geo (error-rate line chart, SS-partition bar diagram), c2v (wheat field or laboratory bench for cold open)
- Prerequisites: what a t-test is, what a significance level means, the idea that variance can be partitioned
- Exclusions: no ANOVA-table computation in detail, no F-distribution derivation, no post-hoc Tukey HSD method, no two-way ANOVA, no Welch ANOVA
- Score: 8/10

## Candidate 13 — Why Mendel's Perfect Data Is Suspicious
- Source: `math-statistics/chapters/11-the-chi-square-distribution.md`
- Topic: STATISTICS
- Hook: Gregor Mendel's pea-plant counts fit his genetic theory so perfectly that Ronald Fisher suspected someone adjusted the numbers — because real data is always messier than the model predicts.
- Key case: Mendel records 882 yellow and 118 green offspring from an experiment predicting a 3:1 ratio. Chi-square = 92.93. The theory fails dramatically. But in other experiments, Mendel's data fit the expected ratios almost too well — chi-square values suspiciously close to zero.
- The Question: Data that fits the theory almost exactly sounds like good science. So why does a chi-square statistic near zero make a statistician suspicious rather than impressed?
- Core idea: A chi-square value much smaller than its degrees of freedom means observed counts are closer to expected than random sampling could plausibly produce; real data always has noise, so data that is too clean — too few deviations from prediction — signals either data selection or adjustment, not excellent experimental design.
- Visual object: A chi-square distribution curve for df=5, with a vertical line at the observed statistic of 1.05 sitting well to the left of the mean (5), and a shaded "suspicious zone" at the far left labeled "too clean"
- Manim move: scan
- Example seed: A lottery commission runs 6,000 draws and records each of six numbers. Expected count: 1,000 each. Observed: 980, 1,010, 1,020, 995, 990, 1,005. Chi-square = 1.05. The mean of a chi-square with df=5 is 5. A value of 1.05 is so far left that the machine looks rigged — perfectly, suspiciously fair.
- Length band: 2–3 min
- Still lanes: geo (chi-square distribution curve with suspicious-left-tail shading, observed vs. expected bar chart)
- Prerequisites: what a chi-square test is, the basic idea of expected vs. observed counts
- Exclusions: no goodness-of-fit formula derivation, no independence-test application, no full Mendel historical biography, no Fisher-Mendel dispute beyond the core observation
- Score: 8/10
