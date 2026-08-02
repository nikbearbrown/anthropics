# Functions, Graphs, and Power Laws

*The shape of a relationship, and how to read an exponent off a straight line.*

---

## The cold open: the shape of a fall

On October 14, 2012, Felix Baumgartner stepped off a capsule 39 kilometers above the New Mexico desert. He did not fall at a steady speed. For the first half-minute he barely seemed to move; then he was supersonic. If you had a stopwatch and a way to mark his altitude, you could write down a table: at 10 seconds he had dropped 490 meters; at 20 seconds, 1,960 meters; at 30 seconds, 4,410 meters.

Look at those numbers. From 10 to 20 seconds he fell almost four times as far as in the first 10 seconds, and the third interval is larger still. The distances are not growing by a fixed amount each second. They are growing by a fixed *rule* — and the rule is the whole physics of the fall. Galileo found it four centuries ago by rolling balls down inclined planes: the distance fallen is proportional to the *square* of the elapsed time. Double the time, quadruple the distance. That single sentence — distance grows as time-squared — is more than a fact about falling rocks. It is a statement about a particular kind of relationship between two quantities, and that relationship has a name, a graph, and a fingerprint you can recognize anywhere.

Before we can do calculus — before we can ask how fast Baumgartner is moving at the instant the clock reads 30 seconds, or how far he has gone in total — we need to be fluent in the objects calculus operates on. Those objects are **functions**, and the pictures of functions are **graphs**. This chapter builds that fluency, and it ends by naming the two questions the rest of Part II will spend its time answering.

---

## The tool, named: the function

A **function** is a rule that assigns to each input exactly one output. We write $f(x)$ — read "$f$ of $x$" — for the output the rule $f$ produces from the input $x$. The input $x$ is the **independent variable**; the output is the **dependent variable**, often called $y$, because it depends on $x$.

In physics the inputs and outputs are physical quantities. Baumgartner's altitude is a function of time: feed in a time $t$, get back a height $y(t)$. We name the rule by what it produces — $y(t)$, $v(t)$, $F(x)$ — and the letter in the parentheses tells you what you are allowed to feed in.

It is tempting to read $f(x)$ as nothing more than "an instruction: plug in a number, turn the crank, read off a number." That is true, but it is not the whole truth, and treating it as the whole truth will quietly sabotage everything that follows. The deeper view — the one calculus needs — is that a function is itself a *thing*: an object with a shape, a graph you can draw, a steepness you can measure, an area you can compute underneath it. A speedometer needs the *shape* of $y(t)$ near an instant, not just one value. Keep both views in mind, and when in doubt, **draw the graph first**. The graph is the function made visible.

### The Cartesian graph

The picture comes from René Descartes, who in 1637 paired algebra with geometry: lay down two perpendicular axes, mark the input $x$ along the horizontal and the output $y$ along the vertical, and for every input place a point at height $y = f(x)$. The collection of all such points is the **graph**, and the relationship between the two quantities becomes a curve you can see.

The right way to read such a curve is not as a static shape to memorize but as a *story of two quantities changing together*: as $x$ slides to the right, what does $y$ do — rise, fall, rise faster, level off? That habit of imagining the covariation is the mental muscle the derivative will formalize.

---

## Development: a catalog of four shapes

Most relationships in introductory mechanics are built from four elementary forms. Each has a defining algebraic shape, a characteristic graph, and a physical fingerprint.

### Linear: constant rate

$$y = mx + b$$

The graph is a straight line. The number $m$ is the **slope** — the rise over the run, $\Delta y / \Delta x$ — and it is constant everywhere on the line: the same steepness at every point. The number $b$ is the **intercept**, the value of $y$ when $x = 0$. A linear relationship is the signature of a *constant rate*: equal steps in $x$ produce equal steps in $y$. An object moving at constant velocity has position $x(t) = x_0 + vt$ — linear in time, slope $v$.

### Quadratic: the parabola

$$y = ax^2 + bx + c$$

The graph is a **parabola**. Its defining feature is the $x^2$ term: the curvature is constant, and the curve is symmetric about a vertical line through its vertex. The physical fingerprint is *constant acceleration*. Baumgartner's altitude, ignoring air, is

$$y(t) = y_0 + v_0 t - \tfrac{1}{2} g t^2,$$

a parabola opening downward. The $-\tfrac{1}{2}g t^2$ term is exactly Galileo's time-squared law. Equal steps in time do *not* produce equal steps in height — that is the whole difference from the linear case, and it is why he fell farther in each successive interval.

### Power law: scaling

$$y = a x^{b}$$

Here the exponent $b$ is a fixed number — it can be a whole number, a fraction, or negative — and it controls how $y$ *scales* when $x$ changes by a factor. Stretch $x$ by a factor of $c$, and $y$ stretches by $c^{b}$:

$$a(cx)^b = a c^b x^b = c^b \cdot (a x^b).$$

This *scale-invariance* is the heart of a power law and what makes it special. The quadratic $y = ax^2$ is a power law with $b = 2$; the inverse-square gravitational force $F \propto 1/r^2 = r^{-2}$ is a power law with $b = -2$; a pendulum's period grows as the square root of its length, $T \propto L^{1/2}$, a power law with $b = \tfrac{1}{2}$.

### Exponential: constant fractional change

$$y = a\,b^{x} \qquad (b > 0)$$

Now the variable is in the *exponent*, not the base — the opposite of a power law, and a distinction students reliably confuse. An exponential's fingerprint is *constant fractional change*: each unit step in $x$ multiplies $y$ by the same factor $b$. Atmospheric pressure falls roughly exponentially with altitude, $p(h) = p_0\,e^{-h/H}$; radioactive decay and the amplitude of a damped oscillation are exponential. The most natural base is $e \approx 2.718$, for reasons that will become clear once we have the derivative.

**Power versus exponential — get this straight.** In $x^2$ the variable is the *base*; in $2^x$ the variable is the *exponent*. They could not be more different: $x^2$ grows briskly, $2^x$ eventually outruns *any* power. The tool that tells them apart cleanly is the logarithm.

![Four mini-plots: a linear function (straight line, constant rate), a quadratic parabola (constant acceleration), a power law (scaling), and an exponential (constant fractional change), each labeled with its physical fingerprint.](images/05-functions-graphs-and-power-laws-fig-01.png)
*Figure 5.1 — Four elementary shapes and their physical fingerprints: the shape of the curve is the physics.*

---

## Development: logarithms and the straightening of curves

A power law and an exponential are both curved on ordinary axes, and curves are hard to read precisely — you cannot eyeball an exponent. The logarithm fixes this by turning multiplication into addition. We need only two of its rules, which follow from the definition of a logarithm as the inverse of exponentiation:

$$\log(AB) = \log A + \log B, \qquad \log(A^p) = p \log A.$$

These two identities are the engine of everything that follows.

### A power law becomes a straight line on log–log axes

Start with $y = a x^b$ and take the logarithm of both sides:

$$\log y = \log\!\left(a x^b\right) = \log a + \log\!\left(x^b\right) = \log a + b\,\log x.$$

Now read this carefully. Let $Y = \log y$ and $X = \log x$. Then

$$Y = b\,X + \log a.$$

That is the equation of a *straight line* — slope $b$, intercept $\log a$ — in the variables $Y$ and $X$. So if you plot $\log y$ against $\log x$ (this is a **log–log plot**), a power law appears as a straight line, **and its slope is the exponent $b$.** The question "what is the scaling exponent?" has become the question "what is the slope of this line?" — and slope we know how to measure.

### An exponential becomes a straight line on semi-log axes

Do the same to $y = a\,b^x$:

$$\log y = \log a + x \log b.$$

Here $\log y$ is linear in $x$ *itself* (not in $\log x$): plotting $\log y$ against $x$ — a **semi-log plot** — straightens an exponential. The slope is $\log b$.

This gives a clean diagnostic. Plot your data both ways. **Straight on log–log → power law. Straight on semi-log → exponential.** The shape of the straightened data tells you which kind of relationship you are looking at, and the slope hands you its key number.

### Reading the slope correctly

The single most common error on log–log paper is to measure slope using the raw printed values instead of their logarithms. The slope is

$$b = \frac{\Delta(\log y)}{\Delta(\log x)} = \frac{\log y_2 - \log y_1}{\log x_2 - \log x_1}.$$

A handy shortcut: on log–log axes, one *decade* (a factor of 10) in either direction is one unit of $\log$. So if $y$ climbs two decades while $x$ climbs one decade, the slope is $2/1 = 2$. We will verify exactly this on the falling-body data in a moment.

---

## Worked examples

### Example 1 — Free fall as a power law (verify the exponent is 2)

Take Baumgartner's fall from rest, $y_{\text{fallen}}(t) = \tfrac{1}{2} g t^2$ with $g = 9.8\ \text{m/s}^2$, so the distance fallen is $d = 4.9\,t^2$. This is a power law with $a = 4.9$ and $b = 2$. Let us pretend we did not know the exponent and extract it from data the way a scientist would.

| $t$ (s) | $d = 4.9 t^2$ (m) | $\log_{10} t$ | $\log_{10} d$ |
|---|---|---|---|
| 1 | 4.9 | 0.000 | 0.690 |
| 10 | 490 | 1.000 | 2.690 |
| 100 | 49,000 | 2.000 | 4.690 |

From $t = 1$ to $t = 100$, the input climbs two decades ($\log t$ goes from $0$ to $2$) while $d$ climbs four decades ($\log d$ goes from $0.69$ to $4.69$). The slope is

$$b = \frac{4.690 - 0.690}{2.000 - 0.000} = \frac{4.00}{2.00} = 2.$$

The log–log slope is exactly 2 — Galileo's time-squared law, read off a straight line. Notice that the intercept $\log a = 0.690 = \log_{10}(4.9)$ recovers the constant $a = 4.9$, which encodes $g/2$. The slope carries the *scaling*; the intercept carries the *scale*.

![Free-fall data d = 4.9t² at t = 1, 10, 100 s plotted as log d against log t falls on a straight line; the rise of 4 decades over a run of 2 decades gives slope b = 2.](images/05-functions-graphs-and-power-laws-fig-02.png)
*Figure 5.2 — A power law straightens on log–log axes; its slope is the exponent. "What is the exponent?" becomes "what is the slope?"*

### Example 2 — Stopping distance versus speed

When a car brakes with constant deceleration $a$, the kinematic relation $v^2 = v_0^2 - 2a\,d$ (derived in the source chapter on straight-line motion) gives, at the stopping point $v = 0$,

$$d = \frac{v_0^{\,2}}{2a}.$$

Stopping distance is a power law in initial speed with exponent $b = 2$: a log–log plot of braking distance against speed is a straight line of slope 2. The road-safety consequence is blunt. Doubling your speed does not double your stopping distance — it *quadruples* it ($2^2 = 4$). Tripling it multiplies the distance by nine. The exponent, not intuition, governs the danger, and the exponent is visible as the slope of a line.

### Example 3 — Reading an exponent that is *contested*

Across the animal kingdom, an organism's metabolic rate $B$ scales with its body mass $M$ as a power law. Plot $\log B$ against $\log M$ for animals from a mouse to an elephant — many orders of magnitude — and the points fall remarkably close to a straight line. Max Kleiber, in the 1930s, measured its slope at about $0.75$, suggesting $B \propto M^{3/4}$.

Here the chapter's tool does its job perfectly and then stops. The slope is a *measurement*: the data really do lie near a line of slope $\approx 0.75$. But *why* the exponent is $3/4$ rather than, say, $2/3$ (which a naive surface-area argument would predict) is a scientific question the graph cannot answer. West, Brown, and Enquist proposed in 1997 that fractal nutrient-distribution networks force the $3/4$; critics argue the exponent is not universal at all [contested — see pantry]. The lesson is exactly the book's thesis: a straight log–log line is evidence of a power law and hands you a number, but the *meaning* of that number — and whether a fitted $0.74$ is "really" $3/4$ — is a judgment a curve-fitter cannot make for you.

---

## Return to the cold open

We can now say precisely what kind of object Baumgartner's fall is. His altitude $y(t) = y_0 + v_0 t - \tfrac{1}{2}g t^2$ is a **quadratic function** of time — a parabola — and the distance he has fallen, $d(t) = \tfrac{1}{2}g t^2$, is a **power law** in time with exponent 2. The shape of that curve *is* the physics: a parabola is precisely what constant acceleration produces, and the exponent 2 is precisely Galileo's law. The numbers in our opening table — 490, 1,960, 4,410 — are not arbitrary; they are $4.9 \times 10^2$, $4.9 \times 20^2$, $4.9 \times 30^2$, the time-squared rule made arithmetic.

But two questions remain, and the function alone cannot answer them. First: *how fast is Baumgartner moving at the instant the clock reads exactly 30 seconds?* That is a question about the **slope** of the position curve at a single point — and right now we only know how to find the slope of a straight line, not of a parabola at one instant. Second: *given his speed at every moment, how far has he fallen in total?* That is a question about the **area** underneath the speed curve.

Slope of a curve at a point, and area under a curve — these are the two questions calculus was built to answer. We have just learned to recognize the curves and read their exponents. The next chapter answers the first question (the derivative); the integral chapters answer the second. Hold those two questions; the whole engine of Part II is their machinery.

---

## Where it generalizes

The power law is one of the most transferable objects in all of quantitative science, precisely because the log–log straightening trick works regardless of what the quantities *are*. Kepler's third law of planetary motion is a power law, $T^2 \propto r^3$, exponent $3/2$, read off a log–log line three centuries before anyone knew why. Earthquake frequency versus magnitude, city size versus rank, the brightness of a star versus its mass, the bandwidth of a network versus its cost — all are power laws diagnosed by the same straight-line-on-log-axes test. The skill you have just acquired, "turn 'what is the exponent?' into 'what is the slope?'," is the same skill whether the curve describes a falling body, a metabolizing mouse, or a galaxy's rotation. And the judgment the tool cannot supply — *which* two quantities to plot, on *which* axes, and what a slope physically *means* — is yours to keep. That division of labor, the mechanical math against the human modeling, is the spine of this book.

---

## Exercises

1. **(Identify the form.)** For each relationship, state whether it is linear, quadratic, power-law, or exponential, and give the physical fingerprint (constant rate? constant acceleration? scaling? constant fractional change?): (a) $x(t) = 5 + 3t$; (b) the period of a pendulum, $T = 2\pi\sqrt{L/g}$, as a function of $L$; (c) bacterial population $N(t) = N_0\,2^{t/20}$; (d) kinetic energy $K = \tfrac{1}{2}mv^2$ as a function of $v$.

2. **(Reading a log–log slope.)** Drag force at high speed obeys $F \propto v^2$. On a log–log plot of $F$ against $v$, you read two points: $(v, F) = (10\ \text{m/s},\ 8\ \text{N})$ and $(40\ \text{m/s},\ 128\ \text{N})$. Compute the slope $\Delta(\log F)/\Delta(\log v)$ and confirm it equals the exponent 2.

3. **(Power vs. exponential.)** A dataset is straight when you plot $\log y$ against $x$, but curved when you plot $\log y$ against $\log x$. Which form is it — power law or exponential — and why? What would the *opposite* result tell you?

4. **(Scaling consequence.)** Stopping distance scales as $d \propto v^2$. A car stops in 12 m from 30 km/h. Using only the scaling (no value of $g$ or friction), find its stopping distance from 90 km/h. State the factor by which the distance grows and where it came from.

5. **(Derivation.)** Starting from the general power law $y = a x^b$, derive that a plot of $\log y$ versus $\log x$ is a straight line, and identify its slope and its intercept in terms of $a$ and $b$. Then show that for an exponential $y = a\,b^x$, it is instead $\log y$ versus $x$ that is straight, and give that line's slope. Explain in one sentence why this difference lets you tell the two forms apart from data alone.

---

## Sources

- Galileo Galilei, *Discorsi e dimostrazioni matematiche intorno a due nuove scienze* (*Two New Sciences*), 1638 — the time-squared law of free fall and the square–cube scaling argument. [verified — see factchecks/05-functions-graphs-and-power-laws-assertions.md] (original primary source)
- René Descartes, *La Géométrie*, 1637 — the coordinate graph pairing algebra with geometry. [verified — see factchecks/05-functions-graphs-and-power-laws-assertions.md] (original primary source)
- Julian S. Huxley, *Problems of Relative Growth*, 1932; J. S. Huxley & G. Teissier, "Terminology of relative growth," *Nature* 137 (1936): 780–781 — allometry and the convention that a power law $y = ax^b$ is a straight log–log line of slope $b$. [verified — see factchecks/05-functions-graphs-and-power-laws-assertions.md] (original primary sources)
- Max Kleiber, "Body size and metabolism," *Hilgardia* 6 (1932): 315–353 — the empirical metabolic-rate-versus-mass scaling. [verified — see factchecks/05-functions-graphs-and-power-laws-assertions.md] (original primary source)
- G. B. West, J. H. Brown, B. J. Enquist, "A general model for the origin of allometric scaling laws in biology," *Science* 276 (1997): 122–126 — the disputed $3/4$-exponent mechanism. [contested — see pantry]
- Source chapter (this book's archive): "Motion Along a Straight Line" — Baumgartner free-fall data and the stopping-distance relation $v^2 = v_0^2 - 2a\,d$.
- A. Sfard, "On the dual nature of mathematical conceptions," *Educational Studies in Mathematics* 22 (1991): 1–36; M. Carlson et al., "Applying covariational reasoning while modeling dynamic events," *Journal for Research in Mathematics Education* 33 (2002): 352–378 — the process-vs-object view of functions and covariational reasoning. [verified — see factchecks/05-functions-graphs-and-power-laws-assertions.md]
