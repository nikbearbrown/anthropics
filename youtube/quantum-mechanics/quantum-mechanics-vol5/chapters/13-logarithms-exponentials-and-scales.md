# Module M-13 — Logarithms, Exponentials, and Scales

**When you need this:** QM Series Vol. I, Chapter 6 (Barrier Penetration); Vol. III, Chapter 4 (WKB Approximation)

**Condensed from:** *Mathematics for Physics, Vol. 2*, Ch. 1

---

## The Fundamental Property and the Laws

The logarithm answers: to what power must we raise the base to get this number? If $y = b^x$, then $x = \log_b y$. The entire usefulness of the logarithm follows from one consequence of the exponent laws:

$$\boxed{\log_b(ac) = \log_b a + \log_b c.}$$

**The logarithm turns multiplication into addition.** The companion laws follow immediately:

$$\log_b\!\left(\frac{a}{c}\right) = \log_b a - \log_b c, \qquad \log_b(a^n) = n\log_b a.$$

**Change of base:** $\log_b a = \log_c a / \log_c b$, so in particular $\log_{10} a = \ln a / \ln 10 \approx \ln a / 2.303$.

> **Warning — the single most common error.** There is *no* law for $\log(a + b)$. The identity $\log(ac) = \log a + \log c$ applies to *products only*. Writing $\log(E_1 + E_2) = \log E_1 + \log E_2$ is always false. If you see a sum inside a logarithm, it cannot be split.

---

## Why $e$ Is Not Optional

The base that physics keeps producing on its own is $e \approx 2.71828$, singled out by the property $d(e^x)/dx = e^x$ — the exponential that is its own derivative. Physics generates $e$ because processes constantly obey the rule that the rate of change of a quantity is proportional to the quantity itself:

$$\frac{dN}{dt} = kN.$$

Separating variables and solving gives $N(t) = N_0\,e^{kt}$. If $k > 0$, exponential growth; if $k = -\lambda < 0$, exponential decay. The half-life — the time for $N$ to halve — follows from setting $N(t_{1/2}) = N_0/2$:

$$\boxed{t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}.}$$

The mean lifetime is $\tau = 1/\lambda$, so $t_{1/2} = \tau\ln 2$.

---

## Linearizing Data: The Two Key Diagnostics

Two functional forms, two types of axes, two straight-line tests:

| Law | Take $\log_{10}$ of both sides | Straight line on |
|-----|-------------------------------|-----------------|
| $y = A\,x^k$ (power law) | $\log y = k\log x + \log A$ | **log–log axes** (slope $= k$) |
| $y = A\,e^{kx}$ (exponential) | $\log y = (k/\ln 10)\,x + \log A$ | **semi-log axes** (slope $= k/\ln 10$) |

Power law gives a line on log–log axes. Exponential gives a line on semi-log axes. Which transformation straightens the data identifies which kind of law is present.

![Log-log vs semi-log linearization diagnostic](../images/13-logarithms-exponentials-and-scales-fig-01.png)
*Figure 13.1 — Linearization diagnostic: a power law $y = Ax^k$ appears as a straight line on log–log axes (slope $k$), while an exponential $y = Ae^{kx}$ appears as a straight line on semi-log axes.*

---

## Worked Example — Half-Life from a Semi-Log Plot

A radioactive sample gives the following count rates:

| $t$ (h) | Rate (counts/min) |
|---|---|
| 0 | 1200 |
| 2 | 670 |
| 4 | 375 |
| 6 | 210 |

**Step 1 — check linearity.** Take $\ln$ of each rate:

$$\ln 1200 \approx 7.09, \quad \ln 670 \approx 6.51, \quad \ln 375 \approx 5.93, \quad \ln 210 \approx 5.35.$$

Differences per 2 hours: approximately $-0.58$ each interval, consistent — a straight line on semi-log axes confirms the exponential law.

**Step 2 — read the slope.** Slope $= -\lambda$, so $\lambda = (7.09 - 5.35)/6 \approx 0.29\ \text{h}^{-1}$.

**Step 3 — compute the half-life.** $t_{1/2} = \ln 2 / \lambda = 0.693 / 0.29 \approx 2.4\ \text{h}$.

Check: at $t = 2.4\ \text{h}$, the rate should be $1200/2 = 600$ counts/min; interpolating the table gives roughly 600. Consistent.

---

## In the Quantum Series

### The Exponential in the Classically Forbidden Region

In barrier-penetration problems (Vol. I, Ch. 6), the Schrödinger equation in a region where $E < V$ becomes

$$\frac{d^2\psi}{dx^2} = \kappa^2\psi, \qquad \kappa \equiv \frac{\sqrt{2m(V-E)}}{\hbar}.$$

The general solution is $\psi(x) = Ae^{+\kappa x} + Be^{-\kappa x}$ — real exponentials, not complex waves. Because $\kappa > 0$, the growing solution $e^{+\kappa x}$ diverges and is rejected on normalizability grounds. The physical solution in the forbidden region is the **decaying exponential** $\psi(x) \propto e^{-\kappa x}$.

The transmission probability through a rectangular barrier of width $L$ is

$$\boxed{T \approx e^{-2\kappa L}, \qquad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}.}$$

This has the same $e^{-\lambda t}$ structure as radioactive decay, but in the *spatial* variable $x$. The "decay constant" is $\kappa$ (units: $\text{m}^{-1}$) and the "lifetime" is $1/\kappa$ — the spatial scale over which the wavefunction falls to $1/e$.

**Evaluate the exponent before computing** $T$. If $2\kappa L = 10$, then $T \approx e^{-10} \approx 4.5\times10^{-5}$ — five orders of magnitude suppression — without touching a calculator. If $2\kappa L = 0.1$, then $T \approx 1 - 0.1 \approx 0.9$ — essentially no suppression. Identifying the regime before doing algebra is a useful first step.

**Useful numbers for electrons with** $V_0 - E = 1\ \text{eV}$: $\kappa \approx 5.1\ \text{nm}^{-1}$. Barriers narrower than $\sim 0.2\ \text{nm}$ give significant tunneling ($\kappa L \lesssim 1$); barriers wider than $\sim 2\ \text{nm}$ are effectively opaque ($\kappa L \gtrsim 10$, $T \lesssim 10^{-9}$).

| $2\kappa L$ | $T = e^{-2\kappa L}$ | Qualitative |
|---|---|---|
| 0.5 | $\approx 0.61$ | substantial |
| 2 | $\approx 0.14$ | partial |
| 10 | $\approx 4.5\times10^{-5}$ | very small |
| 20 | $\approx 2\times10^{-9}$ | negligible |
| 50 | $\approx 2\times10^{-22}$ | essentially zero |

Rule of thumb: each 2.3 units of $2\kappa L$ reduces $T$ by one order of magnitude ($e^{-2.303} = 10^{-1}$).

![Tunneling transmission T vs barrier width on semi-log axes](../images/13-logarithms-exponentials-and-scales-fig-02.png)
*Figure 13.2 — Transmission probability $T = e^{-2\kappa L}$ versus barrier width $L$ on semi-log axes: each curve for a different $\kappa$ is a straight line, and equal increments of $L$ produce equal multiplicative drops in $T$.*

### The WKB Generalization — The Exponent Becomes an Integral

For a non-rectangular barrier where $V(x)$ varies (Vol. III, Ch. 4), the WKB approximation gives

$$T \approx \exp\!\left(-\frac{2}{\hbar}\int_{x_1}^{x_2}\sqrt{2m(V(x)-E)}\,dx\right),$$

where $x_1, x_2$ are the classical turning points. The form is identical to the rectangular case — exponential in a negative exponent — but the exponent is now an integral of $\sqrt{V - E}$ rather than the constant $\kappa L$. Taking the logarithm directly extracts this integral:

$$\ln T = -\frac{2}{\hbar}\int_{x_1}^{x_2}\sqrt{2m(V(x)-E)}\,dx.$$

The **Gamow factor** for alpha decay is exactly this integral applied to the Coulomb barrier. The decay rate $\lambda \propto e^{-G}$ where $G = (2/\hbar)\int_R^{R_c}\sqrt{2m(V_\text{Coulomb}(r)-E)}\,dr$. Small changes in nuclear charge $Z$ or decay energy $E$ produce large changes in $\lambda$ — because they enter the *exponent*. This exponential sensitivity is why nuclear half-lives span nanoseconds to $10^{10}$ years: a range of $10^{26}$, compressed to manageable numbers on a log scale.

![WKB tunneling geometry: classically allowed and forbidden regions](../images/13-logarithms-exponentials-and-scales-fig-03.png)
*Figure 13.3 — WKB tunneling geometry: the particle's wavefunction oscillates in the classically allowed regions ($E > V$), decays exponentially through the classically forbidden region ($E < V$) between turning points $x_1$ and $x_2$, and emerges as a lower-amplitude wave on the far side.*

### Order-of-Magnitude Estimation

A plot of $\ln T$ versus barrier width $L$ is a straight line of slope $-2\kappa$. From the slope we extract $\kappa$, and from $\kappa = \sqrt{2m(V_0-E)}/\hbar$ we extract the barrier height above the particle energy.

**Example.** An STM measures that the tunneling current drops by a factor of $e$ for each $0.1\ \text{nm}$ increase in tip-sample distance. What is the effective $\kappa$?

The current is proportional to $T = e^{-2\kappa L}$. A change $\Delta L = 0.1\ \text{nm}$ changes $\ln(\text{current})$ by $-2\kappa\,\Delta L = -1$, so

$$\kappa = \frac{1}{2\times0.1\ \text{nm}} = 5\ \text{nm}^{-1}.$$

This corresponds to a 1 eV effective barrier for an electron. The exponential sensitivity to tip height is why the STM achieves atomic resolution: current changes by $e$ per ångstrom of distance. The logarithm turns a one-order-of-magnitude sensitivity into a linear, readable signal.

---

## Conventions and Pitfalls

**Exponents must be dimensionless.** $e^{-2\kappa L}$ requires $\kappa L$ to be a pure number. $\kappa$ has units $\text{m}^{-1}$; $L$ has units m; the product is dimensionless. A common error is to work with $\kappa$ in $\text{nm}^{-1}$ and $L$ in m — unit mismatch by $10^9$. Check units before computing the exponent.

**Sign of the exponent.** In the classically forbidden region ($E < V$), the wavefunction is a real decaying exponential with *negative* exponent. If a calculation gives $e^{+|\kappa|x}$ as the physical solution inside the barrier, the growing exponential is not normalizable and must be rejected.

$T \leq 1$ **is a hard constraint.** If a calculation gives $T > 1$, the exponent has the wrong sign. Quick check: is $2\kappa L > 0$? If yes, $e^{-2\kappa L} < 1$.

$\ln$ **versus** $\log_{10}$. The WKB formula uses the natural exponential $e$ throughout. "Take the log to linearize" means take $\ln$, which gives the rate constant directly as the slope. Using $\log_{10}$ gives slope $= -2\kappa/\ln10 \approx -2\kappa/2.303$ — correct but requires a conversion step.

$e^{a+b} = e^a\cdot e^b$, **not** $e^a + e^b$. For a barrier in two segments, the total transmission is $T = e^{-2\kappa_1 L_1}\cdot e^{-2\kappa_2 L_2} = e^{-2(\kappa_1 L_1 + \kappa_2 L_2)}$ — exponents add, transmissions multiply. This is the log law $\log(ac) = \log a + \log c$ running in reverse.

---

## Quick Practice

1. **Tunneling estimate.** An electron ($m = 9.11\times10^{-31}\ \text{kg}$) encounters a rectangular barrier with $V_0 - E = 2\ \text{eV}$ and $L = 0.5\ \text{nm}$. (a) Compute $\kappa$. (b) Compute $2\kappa L$. (c) Estimate $T$ without a calculator, to within a factor of 3, using the table above or the rule $e^{-2.3} \approx 10^{-1}$.

2. **Semi-log reasoning.** A tunneling current measurement gives $I = 4.2\ \mu\text{A}$ at $L = 0.3\ \text{nm}$ and $I = 0.07\ \mu\text{A}$ at $L = 0.9\ \text{nm}$. (a) Find the slope of $\ln I$ versus $L$. (b) Extract $\kappa$. (c) Estimate $V_0 - E$ in eV.

3. **Units check.** The WKB exponent is $(2/\hbar)\int_{x_1}^{x_2}\sqrt{2m(V(x)-E)}\,dx$. Verify that this is dimensionless by checking the units of each factor, using SI units throughout.

---

## Go Deeper

For the full derivation of log and exponential laws, the decay ODE, power-law vs. exponential linearization, and worked examples in decibels and radiocarbon dating: *Mathematics for Physics, Vol. 2*, Ch. 1. For the WKB derivation and connection formulas: QM Series Vol. III, Ch. 4.

---

## References

- Gamow, G. "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik* 51 (1928), 204–212. [verify]
- Fowler, R.H. and Nordheim, L. "Electron Emission in Intense Electric Fields." *Proceedings of the Royal Society A* 119 (1928), 173–181. [verify]
- Binnig, G., Rohrer, H., Gerber, Ch. and Weibel, E. "Surface Studies by Scanning Tunneling Microscopy." *Physical Review Letters* 49 (1982), 57–61. [verify]
- Napier, J. *Mirifici Logarithmorum Canonis Descriptio*. Edinburgh, 1614.
