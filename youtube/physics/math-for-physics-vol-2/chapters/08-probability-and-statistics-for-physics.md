# Probability and Statistics for Physics

*Random variables, distributions, moments, and the propagation of uncertainty — the probabilistic machinery every advanced physics book quietly assumes.*

---

## 1. Cold open: the clicks of a counter

Put a weak radioactive source — a speck of a long-lived isotope — in front of a Geiger counter and listen. *Click. Click-click. … Click.* The counter registers a decay every time a nucleus in the sample throws off a particle. Run it for one second and you might count 18. Run it for the next second and you count 23, then 15, then 21. The source has not changed. The number of nuclei is, to any precision you care about, constant. Yet the count is different every second.

The modern-physics book states the law behind this plainly: a given nucleus has a fixed probability per unit time of decaying, and *which* nucleus decays *when* is utterly unpredictable. What you can predict is not the individual click but the *statistics* of the clicks — the average rate, and crucially the size of the second-to-second wobble around that average. The book also asserts, without much fanfare, a rule that experimentalists live by: if you count $N$ events, the uncertainty in that count is about $\sqrt{N}$. Count 100 and you know the number to roughly $\pm 10$; count 10,000 and you know it to $\pm 100$, which is only $1\%$. To beat down the noise, count longer.

Where does $\sqrt{N}$ come from? Why that function and not, say, $N$ or $\log N$? And why is the histogram of counts shaped the way it is? Answering those questions is the business of this chapter. The same machinery turns out to govern $|\psi|^2$ in quantum mechanics, the energy of a system in a heat bath, and the error bar on every measurement you will ever report. They are all the *same mathematical object* — a probability distribution with a mean and a variance — wearing different physical clothes.

---

## 2. The tool, named

Volume 1 gave you descriptive statistics: how to average a column of numbers and how to draw an error bar as a recipe. It may have shown you the bell curve as a shape. What it did not do is treat a measurement as a *sample drawn from a distribution* — and that reframing is the whole game at the upper-division level.

A **random variable** $X$ is a quantity whose value is not fixed but is governed by a probability rule. We need three new objects:

- A **probability mass function** $P(x)$ for a discrete $X$ (a die, a photon count), giving the probability that $X = x$, with $\sum_x P(x) = 1$.
- A **probability density function** $f(x)$ for a continuous $X$ (a position, a velocity), where $f(x)\,dx$ is the probability that $X$ lands in the sliver $[x, x+dx]$, with $\int_{-\infty}^{\infty} f(x)\,dx = 1$.
- The **mean** (expectation) and **variance**, which compress the whole distribution into a center and a spread.

The single most common first mistake in physics is to read a density as a probability. The quantum-mechanics book flags this as *the* beginner's error with $|\psi(x)|^2$: it is not "the probability of being at $x$" — a continuous variable has zero probability of hitting any exact point. It is a *density*, and $f(x)$ can exceed 1; only $\int f\,dx$ over an interval is a probability and is bounded by 1. Keep that distinction in your bones for the rest of this book.

---

## 3. Development and derivation

### 3.1 Mean and variance from a distribution

The **mean** is the probability-weighted average of the outcomes:
$$
\mu \equiv \mathrm{E}[X] = \sum_x x\,P(x) \qquad \text{(discrete)}, \qquad \mu = \int_{-\infty}^{\infty} x\,f(x)\,dx \qquad \text{(continuous)}.
$$
For any function $g(X)$ the same weighting gives $\mathrm{E}[g(X)] = \sum_x g(x)P(x)$. Expectation is **linear**: $\mathrm{E}[aX+b] = a\,\mathrm{E}[X]+b$, which follows immediately from the sum.

The **variance** measures spread as the mean squared deviation from $\mu$:
$$
\sigma^2 \equiv \mathrm{Var}(X) = \mathrm{E}\!\left[(X-\mu)^2\right].
$$
Expanding the square and using linearity gives the workhorse identity:
$$
\sigma^2 = \mathrm{E}[X^2 - 2\mu X + \mu^2] = \mathrm{E}[X^2] - 2\mu\,\mathrm{E}[X] + \mu^2 = \mathrm{E}[X^2] - \mu^2.
$$
"The mean of the square minus the square of the mean." The **standard deviation** $\sigma = \sqrt{\sigma^2}$ has the same units as $X$ and is the natural measure of "the spread" — the typical size of a fluctuation. This $\sigma$ is exactly the $\Delta x$ of the uncertainty principle and exactly the error bar of the lab; they are not analogies, they are the same definition.

A useful fact for sums of *independent* random variables: variances add. If $Z = X + Y$ with $X, Y$ independent, then
$$
\mathrm{Var}(Z) = \mathrm{Var}(X) + \mathrm{Var}(Y).
$$
(Means always add; variances add only when the variables don't conspire.) This is the seed of the $\sqrt{N}$ rule and of error propagation below.

### 3.2 The binomial, and its two limits

Consider $n$ independent yes/no trials, each succeeding with probability $p$. The number of successes $k$ follows the **binomial distribution**
$$
P(k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad \binom{n}{k} = \frac{n!}{k!\,(n-k)!}.
$$
(The combinatorial factor $\binom{n}{k}$ is the count of *which* trials succeeded; we derive it carefully in **Chapter 9**.) A short calculation — differentiate the binomial theorem, or sum directly — gives its moments:
$$
\mu = np, \qquad \sigma^2 = np(1-p).
$$
Almost every distribution a physicist meets is a limit of this one. Two limits matter, and they go in *opposite directions*.

### 3.3 The Gaussian as the large-$N$ limit (de Moivre–Laplace)

Hold $p$ fixed (say a fair coin, $p=\tfrac12$) and let $n$ grow. The binomial bars get so dense and so smooth that they trace out a continuous curve. Abraham de Moivre found that curve in 1733 while studying coin tosses; here is the heart of his argument.

Write $\mu = np$ and $\sigma^2 = np(1-p)$, and ask for the shape of $P(k)$ near the peak. Take the logarithm and use **Stirling's approximation** $\ln m! \approx m\ln m - m + \tfrac12\ln(2\pi m)$ (derived in Chapter 9) on each factorial. Let $k = \mu + x$ measure the displacement from the peak. Expanding $\ln P(\mu + x)$ in a Taylor series in $x$, the constant term sets the height, the *linear* term vanishes (we expanded about the maximum), and the quadratic term gives
$$
\ln P(\mu + x) \approx \ln P(\mu) - \frac{x^2}{2\sigma^2}.
$$
The cubic and higher terms are suppressed by powers of $1/\sigma \sim 1/\sqrt{n}$ and vanish as $n\to\infty$. Exponentiating, and fixing the prefactor by demanding $\int f\,dx = 1$, yields the **Gaussian (normal) distribution**:
$$
\boxed{\,f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,\exp\!\left[-\frac{(x-\mu)^2}{2\sigma^2}\right].\,}
$$
This is the **de Moivre–Laplace theorem**: the binomial $B(n,p)$ is approximated by the normal $N(np,\,np(1-p))$ for large $n$. The bell curve is not a postulate. It is what a sum of many independent yes/no contributions *becomes*.

![A Gaussian bell curve centered at mu, with the inner band from mu minus sigma to mu plus sigma shaded and labeled 68.3 percent and the wider band out to plus or minus two sigma labeled 95.4 percent](images/08-probability-and-statistics-for-physics-fig-01.png)
*Figure 8.1 — The normal distribution as a center μ and a spread σ: ±1σ holds ~68% of the probability, ±2σ holds ~95%.*

![Two panels of fair-coin binomial probability bars, n equals 10 and n equals 40, each with the matching normal curve drawn in red on top; the denser n equals 40 bars trace the red curve closely](images/08-probability-and-statistics-for-physics-fig-02.png)
*Figure 8.2 — The binomial B(n, ½) converging on the Gaussian as n grows (de Moivre–Laplace): the discrete bars fill in the continuous bell curve.*

The general statement is the **Central Limit Theorem**: the normalized sum of many independent random variables, each with finite variance, converges to a Gaussian *regardless* of the shape of the underlying distribution. Laplace gave the first broad version in 1812; the rigorous modern conditions are due to Lyapunov (1901) and Lindeberg (1922). <!-- FACT-CHECK FLAG: [UNVERIFIED] — dates are standard and correct, but exact bibliographic citation not separately confirmed; see factchecks/08-probability-and-statistics-for-physics-assertions.md --> We *assert* the general theorem rather than prove it here — the measure-theoretic proof is beyond this book — but the de Moivre–Laplace case above shows you concretely why it works: every distribution, expanded about its peak in $\ln P$, looks parabolic, and a parabola in the exponent *is* a Gaussian.

> **A calibration note.** The Gaussian is overused. The CLT needs *finite variance*; physical distributions with heavy tails (Lévy flights, power-law fluctuations) violate that assumption, and for them the bell curve is simply wrong. When in doubt, ask whether the underlying variance is finite before reaching for $N(\mu,\sigma^2)$.

### 3.4 The Poisson distribution — the binomial's other limit

Now go the *other* way. Keep the expected number of events $\lambda = np$ fixed while letting $n\to\infty$ and $p\to 0$ — many trials, each almost certain to fail. This is exactly radioactive decay: each of the $\sim 10^{20}$ nuclei has a vanishing probability of decaying in a given second, but the product (the mean count) is some modest $\lambda$.

Start from the binomial and take the limit. Write
$$
P(k) = \frac{n!}{k!\,(n-k)!}\left(\frac{\lambda}{n}\right)^k\left(1-\frac{\lambda}{n}\right)^{n-k}.
$$
As $n\to\infty$: the factorial ratio $\frac{n!}{(n-k)!\,n^k} \to 1$, the factor $(1-\lambda/n)^{n}\to e^{-\lambda}$, and $(1-\lambda/n)^{-k}\to 1$. What survives is the **Poisson distribution**:
$$
\boxed{\,P(k) = \frac{\lambda^k\,e^{-\lambda}}{k!}, \qquad k = 0,1,2,\dots\,}
$$
Its moments are remarkable. The mean is
$$
\mu = \sum_{k=0}^{\infty} k\,\frac{\lambda^k e^{-\lambda}}{k!} = \lambda e^{-\lambda}\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k-1)!} = \lambda e^{-\lambda}e^{\lambda} = \lambda.
$$
A similar manipulation of $\mathrm{E}[k(k-1)]$ gives $\mathrm{E}[k^2]=\lambda^2+\lambda$, so
$$
\sigma^2 = \mathrm{E}[k^2]-\mu^2 = (\lambda^2+\lambda) - \lambda^2 = \lambda.
$$
**For a Poisson process the variance equals the mean.**

![Stem plots of the Poisson probability mass for lambda equals 1, 4, and 10; small lambda is skewed and large lambda is near-symmetric, with the focal lambda equals 4 case in red and its spread of plus or minus the square root of lambda marked](images/08-probability-and-statistics-for-physics-fig-03.png)
*Figure 8.3 — The Poisson family for λ = 1, 4, 10: variance equals the mean, so σ = √λ — the origin of the √N counting rule.*

Therefore the standard deviation is $\sigma = \sqrt{\lambda}$ — and there is your $\sqrt{N}$ rule. If the expected count is $N$, the fluctuation is $\sqrt{N}$, and the *relative* fluctuation is $\sqrt{N}/N = 1/\sqrt{N}$. Count more to know more. This equality $\sigma^2=\mu$ is the diagnostic of counting statistics: when you see it, you are looking at a Poisson process.

### 3.5 The Boltzmann distribution — the physicist's third law

The third distribution a physicist meets constantly is not a limit of the binomial but a statement about systems in thermal equilibrium. A system in contact with a heat reservoir at temperature $T$ occupies a state of energy $E$ with probability
$$
P(E) = \frac{1}{Z}\,e^{-E/k_BT}, \qquad Z = \sum_i e^{-E_i/k_BT},
$$
where $k_B$ is Boltzmann's constant and $Z$ (the **partition function**) is the normalizing sum. We introduce it here as the third canonical distribution alongside the Gaussian and the Poisson; its *derivation by counting reservoir microstates* is the deep payoff of **Chapter 9**, which closes this loop. For now, note that it is a probability distribution like any other: it has a mean energy $\langle E\rangle$ and an energy variance, and — beautifully — the thermodynamics book shows that the heat capacity is literally that variance, $C_V = (\langle E^2\rangle - \langle E\rangle^2)/k_BT^2$. Response equals fluctuation.

### 3.6 Propagation of uncertainty

The capstone derivation. You measure several quantities $x_1,\dots,x_n$, each with its own uncertainty $\sigma_{x_i}$, and combine them into a result $y = f(x_1,\dots,x_n)$. How uncertain is $y$?

Expand $f$ to first order about the central values $\bar x_i$:
$$
y - \bar y \approx \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}\,(x_i - \bar x_i).
$$
Treat each $(x_i - \bar x_i)$ as an independent, zero-mean random fluctuation. Then $y - \bar y$ is a *sum of independent contributions*, so its variance is the sum of the variances (§3.1), with each term scaled by the squared partial derivative:
$$
\boxed{\;\sigma_y^2 \approx \sum_{i=1}^{n}\left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2.\;}
$$
This is the **law of propagation of uncertainty** — Gauss's formula (1823), standardized today as the core of the international *Guide to the Expression of Uncertainty in Measurement* (GUM). Two everyday corollaries fall out by computing the partials:

- **Sums and differences add in quadrature:** if $y = x_1 \pm x_2$, then $\sigma_y = \sqrt{\sigma_{x_1}^2 + \sigma_{x_2}^2}$. (Note: even for a *difference*, the uncertainties add.)
- **Products and ratios add *relative* uncertainties in quadrature:** if $y = x_1 x_2$ or $x_1/x_2$, then $\sigma_y/|y| = \sqrt{(\sigma_{x_1}/x_1)^2 + (\sigma_{x_2}/x_2)^2}$.

The formula is *first order*: it assumes $f$ is nearly linear over the range of the fluctuations and that the inputs are independent. When $f$ is strongly nonlinear or the inputs are non-Gaussian, modern practice (GUM Supplement 1, JCGM 101:2008) replaces this with **Monte-Carlo propagation** — sampling the input distributions and pushing each sample through $f$. The first-order formula remains the pedagogical and practical core; sampling is its industrial-strength successor.

---

## 4. Worked examples

### Example 1 — The variance *is* the heat capacity (thermodynamics)

In the canonical ensemble the mean energy is $\langle E\rangle = \sum_i E_i P_i$ with $P_i = e^{-\beta E_i}/Z$ and $\beta = 1/k_BT$. A clean trick: since $Z = \sum_i e^{-\beta E_i}$,
$$
\langle E\rangle = -\frac{1}{Z}\frac{\partial Z}{\partial \beta} = -\frac{\partial \ln Z}{\partial \beta}.
$$
Differentiate once more:
$$
\frac{\partial \langle E\rangle}{\partial \beta} = -\frac{\partial^2 \ln Z}{\partial \beta^2} = -\left(\langle E^2\rangle - \langle E\rangle^2\right) = -\sigma_E^2.
$$
Now convert from $\beta$ to $T$ using $d\beta/dT = -1/k_BT^2$:
$$
C_V = \frac{\partial \langle E\rangle}{\partial T} = \frac{\partial \langle E\rangle}{\partial \beta}\frac{d\beta}{dT} = \frac{\sigma_E^2}{k_BT^2}.
$$
The heat capacity — how much energy the system absorbs per degree — is exactly the variance of its energy fluctuations. A statistical quantity (a variance) equals a thermodynamic one (a response). This is the fluctuation–dissipation idea in its simplest dress.

### Example 2 — Expectation values are means (quantum mechanics)

The Born rule says $|\psi(x)|^2$ is a probability *density* for position. Then the quantum expectation value is nothing but the statistical mean of that distribution:
$$
\langle x\rangle = \int_{-\infty}^{\infty} x\,|\psi(x)|^2\,dx,
$$
and the uncertainty is the standard deviation,
$$
(\Delta x)^2 = \langle x^2\rangle - \langle x\rangle^2 = \int x^2|\psi|^2\,dx - \left(\int x|\psi|^2\,dx\right)^2.
$$
These are §3.1 verbatim, with $f \to |\psi|^2$. When a quantum text writes $\langle \hat A\rangle = \langle\psi|\hat A|\psi\rangle$, it is computing the mean of the distribution of measured values of $A$, and $\Delta A$ in the uncertainty principle is its standard deviation. The "spread of the wavefunction" and the "spread of a dataset" are one concept.

### Example 3 — Counting statistics of decay (modern physics)

A source gives a mean of $\bar N = 400$ counts in a fixed interval. Because decay is Poisson, $\sigma = \sqrt{400} = 20$, so a single measurement is $400 \pm 20$ — a $5\%$ relative uncertainty. To halve that to $2.5\%$ you need $\sqrt{N}/N = 0.025$, i.e. $N = 1600$ counts: four times as many, hence (at fixed rate) four times as long. This quadratic cost — to gain a factor of 2 in precision you pay a factor of 4 in time — is the iron law of all counting experiments, from Geiger tubes to CCD astronomy, where the same $\sqrt{N}$ "shot noise" sets the signal-to-noise limit.

---

## 5. Return to the cold open

Now the clicking counter makes sense. Each nucleus is one trial in a binomial with astronomically large $n$ (the number of nuclei) and astronomically small $p$ (the chance any one decays this second), with their product — the mean count $\lambda$ — a modest number. That is precisely the Poisson limit of §3.4. So the second-to-second counts are Poisson-distributed, the variance equals the mean, and the typical wobble around the average count $N$ is $\sqrt{N}$. Rutherford and Geiger confirmed exactly this in 1910 by tallying alpha particles and finding the spread matched $\sqrt{\text{mean}}$ to high accuracy.

The $\pm\sqrt{N}$ in the modern-physics book was never a recipe pulled from the air. It is the standard deviation of the Poisson distribution, which is itself the rare-event limit of the binomial, which is itself just $n$ independent trials. And the reason counting longer helps — relative error $1/\sqrt{N}$ — is the same reason averaging many measurements sharpens a result: independent contributions add in *variance*, so spreads grow like $\sqrt{N}$ while totals grow like $N$.

---

## 6. Where it generalizes

The lesson worth carrying away is not three formulas but one recognition: **$|\psi|^2$, the Boltzmann factor, and a measured-value-with-error-bar are the same object — a probability distribution with a mean and a variance.** Once you see that, the machinery transfers everywhere:

- **The distance ladder and the Hubble tension.** Every rung of the cosmic distance scale carries an uncertainty that propagates through §3.6 and compounds up the ladder. The current disagreement between two ways of measuring the expansion rate is reported at the $5\sigma$ level — that "$5\sigma$" is a propagated-and-compounded uncertainty, the bell curve's tail made into a headline.
- **Spectral line shapes.** Doppler-broadened spectral lines are Gaussian; the line width is a $\sigma$ that encodes the gas temperature. The distribution's spread is a thermometer.
- **The whole of statistical mechanics** is the study of the Boltzmann distribution and its moments — which is where Chapter 9 takes us next, deriving the Boltzmann factor itself by *counting*.

The judgment that no symbolic engine supplies is the modeling step: **which distribution does the physics demand?** A count of rare events → Poisson. A sum of many small independent errors → Gaussian. An energy spectrum in equilibrium → Boltzmann. Get that choice right and the formulas follow; get it wrong and no amount of algebra rescues you.

---

## Exercises

1. **(Moments.)** A fair six-sided die is a random variable $X$ with $P(x)=1/6$ for $x=1,\dots,6$. Compute $\mu$ and $\sigma$ directly from the definitions. Then verify the identity $\sigma^2 = \mathrm{E}[X^2]-\mu^2$.

2. **(Derivation.)** Starting from the binomial $P(k)=\binom{n}{k}p^k(1-p)^{n-k}$, take the limit $n\to\infty$, $p\to0$ with $\lambda=np$ fixed and derive the Poisson distribution $P(k)=\lambda^k e^{-\lambda}/k!$. Show each of the three limiting factors explicitly. Then prove $\mu=\sigma^2=\lambda$.

3. **(Propagation.)** A pendulum's period is $T = 2\pi\sqrt{L/g}$, so $g = 4\pi^2 L/T^2$. You measure $L = 1.000 \pm 0.005$ m and $T = 2.006 \pm 0.004$ s. Use the propagation formula to find $g$ and its uncertainty $\sigma_g$. Which input dominates the error, and why does $T$ count "twice"?

4. **(Poisson vs. Gaussian.)** For $\lambda = 25$, the Poisson distribution is well approximated by a Gaussian. Compute $P(k=25)$ from Poisson and compare to the Gaussian $f(25)$ with $\mu=25$, $\sigma=5$. By roughly what value of $\lambda$ does the approximation become good, and why (think about the de Moivre–Laplace argument)?

5. **(Conceptual.)** Explain in two sentences why, for a continuous random variable, $f(x)$ can be larger than 1 while no probability ever exceeds 1. Give a numerical example using a uniform distribution on $[0, 0.1]$.

---

## Sources

- A. de Moivre, *Approximatio ad Summam Terminorum Binomii $(a+b)^n$ in Seriem expansi* (1733), and *The Doctrine of Chances*, 2nd ed. (1738) — the normal curve as the large-$n$ limit of the binomial (de Moivre–Laplace).
- P.-S. Laplace, *Théorie analytique des probabilités* (1812) — the first broad statement of the central limit theorem.
- C. F. Gauss, *Theoria motus corporum coelestium* (1809) — the normal distribution as the law of error and the method of least squares. [Note: "Gaussian error propagation" honors Gauss the man, not the distribution.]
- S. D. Poisson, *Recherches sur la probabilité des jugements…* (1837) — the rare-event limit of the binomial.
- L. von Bortkiewicz, *Das Gesetz der kleinen Zahlen* (1898) — the canonical empirical Poisson fit (Prussian cavalry horse-kick deaths).
- E. Rutherford and H. Geiger, with H. Bateman, on alpha-particle counting statistics (1910) — empirical confirmation of Poisson decay counts and the $\sqrt{N}$ fluctuation.
- L. Boltzmann (1868, 1877) and J. W. Gibbs, *Elementary Principles in Statistical Mechanics* (1902) — the Boltzmann distribution and ensemble/partition-function language.
- BIPM/JCGM, *Guide to the Expression of Uncertainty in Measurement* (GUM, JCGM 100:2008; Monte-Carlo propagation in Supplement 1 = JCGM 101:2008; the separate introductory document JCGM GUM-1:2023 replaced JCGM 104:2009); B. N. Taylor and C. E. Kuyatt, NIST Technical Note 1297 (1994) — the law of propagation of uncertainty and Monte-Carlo propagation. <!-- FACT-CHECK: corrected 2026-05-30 — Monte-Carlo is Supplement 1 (JCGM 101:2008, 2008), not 2023. -->
- A. M. Lyapunov (1901) and J. W. Lindeberg (1922) — rigorous conditions for the central limit theorem. [verify exact citation details]
- In-series: *Physics — Quantum Mechanics* ch. 01 (Born rule, density-vs-probability); *Physics — Thermodynamics* ch. 08 (Boltzmann distribution, heat capacity as energy-variance); *Physics — Modern Physics* ch. 13 (decay as a random process, $\sqrt{N}$); *Physics — Astronomy* ch. 06–07 (Gaussian line profiles, distance-ladder error compounding and the $5\sigma$ Hubble tension).
