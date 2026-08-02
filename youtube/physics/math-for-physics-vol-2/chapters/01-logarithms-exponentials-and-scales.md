# Logarithms, Exponentials, and Scales

*The one function that turns multiplication into addition — and why physics measures the world with it.*

## The cold open: a star catalog written backwards

Open an astronomy book to the chapter on stellar brightness and you meet a scale that seems designed to confuse. The brightest stars in the sky — Sirius, Vega, Arcturus — are assigned *small* numbers; the faintest stars you can see with the naked eye are *sixth* magnitude, and stars fainter still run to seventh, eighth, twentieth and beyond, the number climbing as the star dims. Brighter means smaller. Worse, the scale is not evenly spaced in any quantity you can measure with an instrument: a first-magnitude star is not "six times" brighter than a sixth-magnitude one. It is *one hundred* times brighter. And a single step in magnitude — from third to fourth, say — corresponds to a brightness ratio of about $2.512$, the same ratio at every step, no matter where on the scale you are.

This is not arbitrary cruelty. The magnitude scale is the fossilized record of a deep fact about measurement: when a physical quantity ranges over an enormous span — stellar fluxes vary by a factor of billions across the visible sky — and when human perception itself responds to *ratios* rather than to *differences*, the natural way to measure it is logarithmically. The same logic produces the decibel for sound and signal power, the pH scale for acidity, and the Richter scale for earthquakes. To read any of these you need one mathematical tool, the logarithm, fluently enough to invert it: to go from "$+12$ decibels" back to "how many times louder?", or from "fifth magnitude fainter" back to "one hundred times dimmer." That fluency — reading scales and linearizing data — is what this chapter builds.

## The tool, named

Volume 1 introduced the logarithm and the exponential as functions: $b^x$ for a base $b$, its inverse $\log_b$, the number $e$, the natural logarithm $\ln$, and the algebraic laws. We assume those as known. What Volume 1 did *not* do — and what the advanced courses constantly demand — is **fluency at reading logarithmic scales and at linearizing data**: recognizing a power law as a straight line on log–log axes, an exponential as a straight line on semi-log axes, and inverting a scale definition to recover the physical ratio it encodes. That is the gap this chapter fills. The mathematics is elementary; the skill is interpretive, and it is precisely the skill a symbolic calculator cannot supply.

## Development and derivation

### The defining property

A logarithm answers the question: *to what power must I raise the base to get this number?* If $y = b^x$, then $x = \log_b y$. The two functions are inverses, and the entire usefulness of the logarithm flows from a single consequence of the exponent laws. Since $b^{x_1} \cdot b^{x_2} = b^{x_1 + x_2}$, taking logarithms of both sides gives

$$\log_b(b^{x_1} \cdot b^{x_2}) = x_1 + x_2 = \log_b(b^{x_1}) + \log_b(b^{x_2}).$$

Writing $a = b^{x_1}$ and $c = b^{x_2}$, this is the law that started it all:

$$\boxed{\;\log_b(ac) = \log_b a + \log_b c.\;}$$

**The logarithm turns multiplication into addition.** This is not a curiosity — it is the reason John Napier invented logarithms in 1614, publishing tables in the *Mirifici Logarithmorum Canonis Descriptio* expressly so that astronomers could replace the multiplication of large numbers (then done by hand, slowly and with errors) by the addition of table entries. The companion laws follow the same way:

$$\log_b\!\left(\frac{a}{c}\right) = \log_b a - \log_b c, \qquad \log_b(a^n) = n\,\log_b a.$$

The first comes from $\log_b(a/c) + \log_b c = \log_b a$; the second by repeated application of the product law. And to change base — to convert a natural logarithm into a base-10 one, which we will need constantly — write $a = b^{\log_b a}$ and take $\log_c$ of both sides:

$$\log_c a = \log_b a \cdot \log_c b \quad\Longrightarrow\quad \log_b a = \frac{\log_c a}{\log_c b}.$$

In particular $\log_{10} a = \ln a / \ln 10$, with $\ln 10 \approx 2.3026$.

**A warning the data will not give you.** The laws above are for products, quotients, and powers. They say *nothing* about sums. The single most common error is to write $\log(a+b) = \log a + \log b$ — which is false — or to confuse $\log a / \log b$ with $\log(a/b)$. There is no law for the logarithm of a sum. Keep the boxed identities pure: they apply to multiplicative structure only.

### Why $e$ and the natural log are not optional

Base 10 is convenient for human-built scales because we count in tens. But the base that physics keeps choosing on its own is $e \approx 2.71828$, defined as the limit

$$e = \lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^{n},$$

and singled out by the property that $\dfrac{d}{dx}e^{x} = e^{x}$ — the exponential that is its own derivative. The reason physics keeps producing $e$ is that physical processes constantly obey the rule *the rate of change of a quantity is proportional to the quantity itself.* That sentence is a differential equation,

$$\frac{dN}{dt} = kN,$$

and its solution (separate variables: $dN/N = k\,dt$, integrate to $\ln N = kt + C$) is

$$N(t) = N_0\, e^{kt},$$

with $N_0$ the value at $t=0$. If $k>0$ this is exponential growth; if $k<0$, decay. We will see in a moment that radioactive decay is exactly this equation, with the decay law $N(t) = N_0 e^{-\lambda t}$.

### The central derivation: power laws and exponentials become straight lines

Here is the skill that makes log scales worth the trouble. Suppose two quantities are related by a **power law**,

$$y = A\,x^{k},$$

with $A$ and $k$ constants — the kind of relation that appears whenever one quantity scales as some fixed power of another (luminosity versus radius, period versus orbital distance, intensity versus distance). Take the base-10 logarithm of both sides and use the product and power laws:

$$\log_{10} y = \log_{10} A + k\,\log_{10} x.$$

Now define new variables $Y = \log_{10} y$ and $X = \log_{10} x$. The equation becomes

$$\boxed{\;Y = kX + \log_{10}A,\;}$$

which is the equation of a **straight line** with slope $k$ and intercept $\log_{10} A$. So: *a power law is a straight line on log–log axes, and its slope is the exponent.* If you suspect your data follow a power law, plot $\log y$ against $\log x$; if the points fall on a line, you have confirmed the power law and can read off the exponent $k$ directly as the slope — no curve-fitting required.

![Log–log plot of orbital period versus orbital distance for the planets. The seven points from Mercury to Neptune fall on a straight line of slope three-halves, confirming Kepler's third law; a dashed slope triangle reads the exponent directly off the axes.](images/01-logarithms-exponentials-and-scales-fig-01.png)
*Figure 1.1 — A power law plots as a straight line on log–log axes; the slope is the exponent (Kepler's $T^2 \propto a^3$, slope $3/2$).* This is how Henrietta Leavitt, working with photographic plates at the Harvard College Observatory, discovered the Cepheid period–luminosity relation around 1908–1912: plotting brightness against the *logarithm* of the pulsation period gave a straight line, and that line became the cosmic distance ladder. <!-- FACT-CHECK FLAG: [CONFIRMED] — see factchecks/01-logarithms-exponentials-and-scales-assertions.md (Leavitt noted the pattern c.1908, established the relation in her 1912 publication) -->

An **exponential** linearizes on a different pair of axes. Take

$$y = A\,e^{kx}$$

and apply $\log_{10}$:

$$\log_{10} y = \log_{10} A + \frac{k}{\ln 10}\,x.$$

Here only $y$ is logged; $x$ stays linear. On **semi-log axes** (logarithmic $y$, linear $x$) this is a straight line of slope $k/\ln 10$. So an exponential process — anything obeying $dN/dt = kN$ — shows up as a line when you plot $\log y$ against $x$ itself. The two diagnostics are worth memorizing as a pair: *power law → line on log–log; exponential → line on semi-log.* Which one straightens your data tells you which kind of law you have.

A caution that the recent literature on "exponential-growth bias" makes vivid: a semi-log plot can *hide* the explosive acceleration of an exponential from an untrained reader, because steady multiplicative growth looks like a gentle straight line. The log plot is a tool for the analyst, not always a kindness to the audience. Use it knowing what it conceals.

## Worked examples

### Example 1 — The decibel as a log ratio (acoustics and optics)

Engineers at Bell Labs in the 1920s faced a problem with the same shape as Napier's: signal power along a telephone line drops by a *factor* at each cable section, and cascaded factors multiply, which is awkward to track. Their fix, formalized when the unit was named the *decibel* in 1929 after Alexander Graham Bell, was to take the logarithm so that the factors add. The sound intensity level (or any power level) is defined as

$$\beta = 10\,\log_{10}\!\left(\frac{P}{P_0}\right) \;\text{decibels},$$

a logarithm of a power *ratio* against a reference $P_0$. For acoustics the reference is $I_0 = 10^{-12}\ \mathrm{W/m^2}$, the threshold of hearing. Two consequences fall straight out of the log laws:

- A tenfold increase in power, $P/P_0 = 10$, gives $\beta = 10\log_{10}10 = +10\ \mathrm{dB}$.
- A *doubling* of power, $P/P_0 = 2$, gives $\beta = 10\log_{10}2 \approx +3.01\ \mathrm{dB}$ — the origin of the rule "$+3\ \mathrm{dB}$ is twice the power."

To **invert** the scale — the skill the chapter is really about — solve for the ratio. If two signals differ by $\Delta\beta$ decibels, then $\Delta\beta = 10\log_{10}(P_1/P_0)$, so

$$\frac{P_1}{P_0} = 10^{\,\Delta\beta/10}.$$

Thus $+12\ \mathrm{dB}$ means $10^{1.2} \approx 15.8$ times the power. (For *amplitude* or field quantities the convention switches to $20\log_{10}$, because power goes as amplitude squared and the power law $\log(a^2)=2\log a$ pulls out the factor of two. Knowing whether your quantity is a power or an amplitude — which the formula will not tell you — is exactly the convention-awareness this chapter insists on.)

![A vertical decibel scale with rungs at 0, 10, 20, 30 and 40 decibels, each labelled with its power ratio of 1, 10, 100, 1000 and 10000. A red brace marks that one plus-ten-decibel step equals one tenfold increase in power; a footnote gives the plus-three-decibel doubling rule.](images/01-logarithms-exponentials-and-scales-fig-03.png)
*Figure 1.3 — The decibel ladder: each additive $+10\ \mathrm{dB}$ step multiplies the power by ten, the logarithm turning a multiplicative range into an even ladder.*

A clean modern instance: single-mode silica optical fiber loses about $0.2\ \mathrm{dB/km}$ at the $1550\ \mathrm{nm}$ wavelength. <!-- FACT-CHECK FLAG: [CONFIRMED] — see factchecks/01-logarithms-exponentials-and-scales-assertions.md (1550 nm is the silica minimum-loss window; ~0.2 dB/km is the standard single-mode value) --> Because loss in *decibels* is the logarithm of the power ratio, and the underlying power falls *exponentially* with distance, the decibel loss adds linearly: over $100\ \mathrm{km}$ the loss is $0.2 \times 100 = 20\ \mathrm{dB}$, a power ratio of $10^{-2}$ — one percent of the light survives. The exponential decay of power has become a linear accumulation of decibels. That is Napier's trick, working in fiber optics three and a half centuries later.

### Example 2 — Half-life from a decay exponential (modern physics)

Rutherford and Soddy established in 1902–03 that a radioactive substance transforms a fixed *fraction* of itself per unit time, not a fixed amount. In symbols, the number $N$ of undecayed nuclei obeys

$$\frac{dN}{dt} = -\lambda N,$$

with $\lambda > 0$ the decay constant. This is our growth/decay equation with $k = -\lambda$, so

$$N(t) = N_0\, e^{-\lambda t}.$$

The **half-life** $t_{1/2}$ is the time for half the nuclei to decay: $N(t_{1/2}) = N_0/2$. Substitute and solve, using the logarithm to undo the exponential:

$$\frac{N_0}{2} = N_0\,e^{-\lambda t_{1/2}} \;\Longrightarrow\; \tfrac{1}{2} = e^{-\lambda t_{1/2}} \;\Longrightarrow\; \ln\tfrac{1}{2} = -\lambda t_{1/2} \;\Longrightarrow\; \boxed{\,t_{1/2} = \frac{\ln 2}{\lambda}.\,}$$

The half-life is independent of $N_0$ — every halving takes the same time, the signature of exponential decay. Inverting, $\lambda = \ln 2 / t_{1/2}$. For carbon-14, $t_{1/2} = 5730\ \mathrm{yr}$ gives $\lambda = \ln 2 / 5730 \approx 1.21\times 10^{-4}\ \mathrm{yr^{-1}}$, the constant behind radiocarbon dating.

This is also the canonical *semi-log* example. Taking the natural log of the decay law,

$$\ln N = \ln N_0 - \lambda t,$$

so a plot of $\ln N$ (or counts per minute, which is proportional) against time $t$ is a straight line of slope $-\lambda$. A laboratory measures count rate at intervals, plots it on semi-log axes, fits a line, and reads $\lambda$ — and hence $t_{1/2}$ — off the slope. The exponential law has been linearized exactly as the general derivation promised.

![Two panels of radioactive decay. Left, on linear axes, the count rate falls along a curved exponential with equal-time successive halvings marked at each half-life. Right, the same data on semi-log axes is a straight line whose slope is minus the decay constant.](images/01-logarithms-exponentials-and-scales-fig-02.png)
*Figure 1.2 — An exponential decay curves on linear axes but straightens on semi-log axes, where the slope is $-\lambda$ and equal time steps are equal halvings.*

### Example 3 — The Arrhenius plot (thermal and chemical physics)

A reaction rate often follows the Boltzmann/Arrhenius form $\text{rate} = A\,e^{-E_a/kT}$, where $E_a$ is an activation energy, $k$ Boltzmann's constant, and $T$ temperature. This is an exponential, but in the variable $1/T$. Take the natural log:

$$\ln(\text{rate}) = \ln A - \frac{E_a}{k}\cdot\frac{1}{T}.$$

Plotting $\ln(\text{rate})$ against $1/T$ — the Arrhenius plot — gives a straight line of slope $-E_a/k$, from which the activation energy is read directly. Same move as the decay example: log the exponential, identify the straight line, extract the physical constant from the slope. The recurrence of this one technique across radioactivity, chemical kinetics, and thermodynamics is the chapter's thesis in miniature.

## Return to the cold open: the magnitude scale, decoded

Now the backwards star catalog makes sense. The eye, like the ear, responds roughly to ratios of stimulus rather than to differences — the Weber–Fechner observation that perceived intensity scales as the logarithm of physical intensity. (Whether perception is *exactly* logarithmic is genuinely contested — S. S. Stevens argued in 1957 for a power law instead — so treat "the eye sees logarithmically" as a good motivation, not a settled law.) The ancient six-class ranking of Hipparchus, brightest as first magnitude, was therefore already a rough logarithmic scale by accident of human perception.

In 1856 Norman Pogson made it exact. <!-- FACT-CHECK FLAG: [CONFIRMED] — see factchecks/01-logarithms-exponentials-and-scales-assertions.md (Pogson 1856, MNRAS 17, Issue 1, pp. 12–15) --> He defined a difference of **five magnitudes to mean exactly a factor of $100$ in flux**, so that one magnitude is the fifth root of one hundred:

$$10^{1/5} = 100^{1/5} = 2.512\ldots$$

— the "Pogson ratio" the cold open quoted. Writing this as a relation between the magnitudes $m_1, m_2$ of two stars and their fluxes $F_1, F_2$: the flux ratio for a magnitude difference $\Delta m$ must satisfy $F_1/F_2 = 100^{-\Delta m/5}$ (the minus sign because brighter is a *smaller* magnitude). Take $\log_{10}$ of both sides:

$$\log_{10}\!\left(\frac{F_1}{F_2}\right) = -\frac{\Delta m}{5}\log_{10}100 = -\frac{2\,\Delta m}{5},$$

and solving for the magnitude difference gives the working formula:

$$\boxed{\,m_1 - m_2 = -2.5\,\log_{10}\!\left(\frac{F_1}{F_2}\right).\,}$$

There is the factor $2.5$, there is the minus sign that makes the scale backwards, and there is the logarithm of a ratio — the same structure as the decibel, built from the same algebra. To **invert** it, recover the flux ratio: $F_1/F_2 = 10^{-(m_1-m_2)/2.5}$. A difference of one magnitude is $10^{-1/2.5} = 10^{-0.4} \approx 0.398$, i.e. the fainter star has about $40\%$ the flux of the brighter — equivalently the brighter is $2.512$ times the fainter, the Pogson ratio again, now derived rather than asserted.

The scale extends to *intrinsic* brightness through the **distance modulus**. The absolute magnitude $M$ is the magnitude a star would have at a standard distance of $10\ \mathrm{pc}$; since flux falls as $1/d^2$, the same $-2.5\log_{10}$ machinery gives

$$m - M = 5\,\log_{10}\!\left(\frac{d}{10\ \mathrm{pc}}\right).$$

For a worked case from the series astronomy book: a star with apparent magnitude $m_V = 3.5$ and parallax $0.025''$ lies at $d = 1/0.025 = 40\ \mathrm{pc}$, so

$$M_V = m_V - 5\log_{10}(40/10) = 3.5 - 5\log_{10}4 = 3.5 - 5(0.602) = 0.49,$$

and comparing to the Sun's absolute magnitude via $L/L_\odot = 10^{(M_\odot - M_V)/2.5}$ gives $L \approx 55\,L_\odot$. <!-- FACT-CHECK FLAG: [UNVERIFIED] — see factchecks/01-logarithms-exponentials-and-scales-assertions.md. The arithmetic is AI-CONFIRMED internally consistent (d=40 pc, M_V=0.49, L≈55 L_⊙ with M_⊙,V≈4.83); only the specific worked example's attribution to the series astronomy book is unverifiable. --> Every step is the log laws applied to a defined scale. The catalog is not written backwards out of perversity; it is written in logarithms, because that is how brightness, spanning a billion-to-one range and perceived by a ratio-sensitive eye, is naturally measured.

## Where it generalizes

The pattern — *take the logarithm of a ratio to compress an enormous dynamic range into a manageable, additive scale* — recurs everywhere a quantity spans many orders of magnitude or where perception and signal-processing care about ratios. The pH scale is $-\log_{10}[\mathrm{H}^+]$; the Richter and moment-magnitude scales are logarithms of seismic amplitude and energy; information is measured in bits, a base-2 logarithm of the number of states (and entropy, in Chapter 9, will be a logarithm of multiplicity). The linearization technique generalizes too: whenever you suspect a law of the form $y = Ax^k$ or $y = Ae^{kx}$, the right pair of axes turns it into a line whose slope is the physical exponent — the working method of experimental physics for fitting power laws and rates. And the exponential $dN/dt = kN$ itself, the source of the natural log, is the simplest and most ubiquitous differential equation in science, reappearing in cooling, charging capacitors, population dynamics, and the Boltzmann factor that opens statistical mechanics. One function, learned once, reads them all.

## Exercises

1. **(Algebra, no traps.)** Simplify $\log_{10}(1000\,x^3) - \log_{10}(x)$ to a single logarithm plus a constant. Then state, in one sentence, why $\log(a+b)$ cannot be simplified the same way.

2. **(Decibels, inversion.)** A sound is measured at $85\ \mathrm{dB}$; a quieter source reads $61\ \mathrm{dB}$. By what factor do their *intensities* differ? Then: an optical fiber loses $0.35\ \mathrm{dB/km}$. What fraction of the input power remains after $50\ \mathrm{km}$?

3. **(Derivation — required.)** Starting from the assumption that a radioactive sample decays so that a fixed fraction transforms per unit time, $dN/dt = -\lambda N$, derive $N(t) = N_0 e^{-\lambda t}$ and then the half-life relation $t_{1/2} = \ln 2/\lambda$. Show every integration step. Finally, prove that the *mean lifetime* $\tau \equiv 1/\lambda$ satisfies $t_{1/2} = \tau \ln 2$.

4. **(Linearization.)** You measure a quantity $y$ at several values of $x$ and find that plotting $\log_{10}y$ against $\log_{10}x$ gives a straight line of slope $-2$ and $y$-intercept $1.7$. Write down the law $y(x)$ explicitly, including the numerical value of the constant. What physical relation has this slope? (Hint: think of an inverse-square law.)

5. **(Magnitudes, derivation and number.)** Starting only from Pogson's definition that five magnitudes equal a flux factor of exactly $100$, derive $m_1 - m_2 = -2.5\log_{10}(F_1/F_2)$. Then compute: two stars differ by $3.0$ magnitudes; what is the ratio of their fluxes, and which is brighter?

## Sources

- John Napier, *Mirifici Logarithmorum Canonis Descriptio* (Edinburgh, 1614); construction in *Mirifici Logarithmorum Canonis Constructio* (1619, posthumous).
- Norman R. Pogson, "Magnitudes of Thirty-six of the Minor Planets for the first day of each month of the year 1857," *Monthly Notices of the Royal Astronomical Society* 17, Issue 1 (1856), pp. 12–15. [pagination confirmed 2026-05-30 — https://academic.oup.com/mnras/article/17/1/12/956950]
- W. H. Martin, "Decibel — The Name for the Transmission Unit," *Bell System Technical Journal* 8(1) (January 1929), pp. 1–2.
- E. Rutherford and F. Soddy, "The Cause and Nature of Radioactivity," Parts I & II, *Philosophical Magazine* 4 (1902), pp. 370–396 and 569–585; and "Radioactive Change," *Philosophical Magazine* 5 (1903), pp. 576–591.
- G. T. Fechner, *Elemente der Psychophysik* (Leipzig, 1860), building on E. H. Weber (1834).
- S. S. Stevens, "On the psychophysical law," *Psychological Review* 64 (1957), pp. 153–181. [counter-cite to Fechner]
- Henrietta S. Leavitt, period–luminosity relation, Harvard College Observatory Circulars (pattern noted c. 1908; relation established in the 1912 publication, "Periods of 25 Variable Stars in the Small Magellanic Cloud," HCO Circular 173). [confirmed 2026-05-30]
