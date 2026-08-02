# The Integral

*The second question: how much accumulates? — and the theorem that reveals it is the first question run backwards.*

---

## The cold open: how far did you go, and how much work did you do?

In Chapter 5 we named two questions calculus would answer. Chapter 6 answered the first — *how fast is something changing right now?* — with the derivative. Here is the second, and it arrives in two disguises.

Disguise one: you have a graph of your speed over a trip — fast on the highway, slow in town, stopped at lights. *How far did you travel in total?* If your speed were constant, distance would be speed times time, trivially. But the speed keeps changing. You cannot multiply a single number by the time, because there is no single number.

Disguise two, from the source chapter on work and energy: you draw a bow. At the start the string is slack and easy; at full draw it fights back hard. The force you apply grows as you pull. *How much work did you do storing energy in the bow?* Work is force times distance — but the force changed over the distance, so again there is no single number to multiply.

Both questions have the same shape: a quantity is the product of two things (speed × time, force × distance), but one of the factors *varies* as the other runs. You cannot just multiply. What you *can* do is chop the motion into slices so thin that, within each slice, the varying factor is effectively constant — multiply within each thin slice, then add up all the slices. Push that chopping to its limit, and you have invented the **definite integral**: the mathematics of accumulation. It is the tool this chapter builds, and its punchline — the Fundamental Theorem of Calculus — is one of the most beautiful surprises in mathematics: this second question turns out to be the first question, asked backwards.

---

## The tool, named: the definite integral

Suppose a quantity accumulates as $f$ runs over an interval from $a$ to $b$ — distance accumulating as speed $v$ runs over time, work accumulating as force $F$ runs over position. Chop the interval into $n$ small pieces each of width $\Delta x$. On the $k$-th piece, pick a sample point $x_k$ and approximate the accumulation there as the **product** $f(x_k)\,\Delta x$ — the area of a thin rectangle of height $f(x_k)$ and width $\Delta x$. Add them all:

$$S_n = \sum_{k=1}^{n} f(x_k)\,\Delta x.$$

This is a **Riemann sum**. As the slices get thinner ($n \to \infty$, $\Delta x \to 0$), the staircase of rectangles hugs the curve ever more tightly, and the sum approaches a limit. That limit is the **definite integral**:

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{k=1}^{n} f(x_k)\,\Delta x.$$

The elongated S — Leibniz's symbol, from *summa* — is a frozen reminder that an integral *is* a sum. The $dx$ is the surviving ghost of the slice width $\Delta x$, telling you what you are accumulating with respect to. Geometrically, the definite integral is the **area under the curve** $f$ between $a$ and $b$. Physically, it is the **total accumulated** when $f$ is a rate or a density.

A piece of advice that the research on how students learn this is unanimous about: do not let the product $f(x_k)\,\Delta x$ become invisible. It is not decoration. It is *one thin sliver of the answer* — one sliver of distance, $v\,\Delta t$; one sliver of work, $F\,\Delta x$. The integral is the sum of those slivers, and keeping the sliver in view is what separates understanding from symbol-pushing.

---

## Development: the integral as a limit of sums, the way Archimedes saw it

The idea is older than calculus. Archimedes, in the third century BCE, found the area of curved regions by his **method of exhaustion**: trap the region between inscribed and circumscribed polygons, and let the polygons grow until the gap between them shrinks to nothing. The area was squeezed between an under-estimate and an over-estimate that converged. That is a Riemann sum in ancient dress — rectangles instead of polygons, but the same logic of approximation-then-limit.

Make it concrete with distance from speed. Take a velocity $v(t)$ over the interval $[0, T]$. Slice time into $n$ intervals of width $\Delta t = T/n$. In the $k$-th interval the object moves *almost* at constant speed $v(t_k)$, so it covers *almost* $v(t_k)\,\Delta t$ — one sliver of distance, the area of one rectangle on the velocity–time graph. The total distance is approximately

$$x \approx \sum_{k=1}^{n} v(t_k)\,\Delta t.$$

The approximation is imperfect because $v$ does drift within each slice — but the thinner the slices, the smaller the error in each, and in the limit the error vanishes:

$$x = \lim_{n\to\infty}\sum_{k=1}^n v(t_k)\,\Delta t = \int_0^T v(t)\,dt.$$

Displacement is the area under the velocity–time curve. The chopping made the varying speed manageable; the limit made it exact.

![A velocity curve shown with a coarse partition of wide rectangles (visible gaps to the curve) and a fine partition of thin rectangles (gaps nearly gone); each rectangle is a sliver v(tₖ)Δt, and the sum approaches the integral ∫v dt.](images/08-the-integral-fig-01.png)
*Figure 8.1 — The definite integral is the limit of a sum of thin slivers; as the slices thin, the staircase hugs the curve and the sum becomes exact.*

---

## Development: the antiderivative, and the surprise

Here is where accumulation meets the derivative. Define an **accumulation function** — the integral as a function of its upper limit:

$$A(x) = \int_a^x f(t)\,dt.$$

$A(x)$ is the area swept out from the fixed left edge $a$ to a moving right edge $x$. As you push $x$ rightward by a tiny amount $dx$, you add a thin strip of area — height $f(x)$, width $dx$ — so the area grows by $f(x)\,dx$. The *rate* at which the accumulated area grows, per unit of $x$, is therefore $f(x)$ itself. In symbols:

$$\frac{dA}{dx} = f(x).$$

This is the **Fundamental Theorem of Calculus, Part 1**, and it is the surprise: *the derivative of the accumulation function is the original function.* Accumulating and rate-finding are inverse operations. The two questions named back in Chapter 5 — slope and area — are not two questions at all. They are one question and its undoing.

Let us prove Part 1 cleanly. By definition,

$$\frac{dA}{dx} = \lim_{h\to 0}\frac{A(x+h) - A(x)}{h}.$$

The numerator $A(x+h) - A(x)$ is the area of the strip between $x$ and $x+h$ — a thin sliver under $f$. If $f$ is continuous, then over the tiny width $h$ its value stays close to $f(x)$, so the strip's area is approximately $f(x)\cdot h$:

$$A(x+h) - A(x) \approx f(x)\,h.$$

Divide by $h$ and let $h\to 0$ (the approximation becomes exact as the strip narrows):

$$\frac{dA}{dx} = \lim_{h\to 0}\frac{f(x)\,h}{h} = f(x). \qquad\blacksquare$$

### From the surprise to the shortcut

A function $F$ whose derivative is $f$ is called an **antiderivative** of $f$. Part 1 says $A(x) = \int_a^x f$ is one such antiderivative. Now suppose you have found *any* antiderivative $F$ (so $F' = f$). Then $A$ and $F$ differ at most by a constant (two functions with the same derivative differ by a constant), so $A(x) = F(x) + C$. At $x = a$, $A(a) = \int_a^a f = 0$, giving $C = -F(a)$. Therefore $A(x) = F(x) - F(a)$, and evaluating at $x = b$:

$$\boxed{\,\int_a^b f(x)\,dx = F(b) - F(a)\,.}$$

This is the **Fundamental Theorem of Calculus, Part 2** — the shortcut. To compute the area (the accumulation), you do *not* have to grind out the limit of a Riemann sum. Find an antiderivative $F$, evaluate it at the two endpoints, subtract. The infinite sum collapses to one subtraction.

![Paired panels: on the left, f with the swept area A(x) shaded to a moving edge x and a thin growth strip f(x)dx; on the right, the accumulation curve A(x) whose slope at x equals f(x); the boxed result ∫ₐᵇ f = F(b) − F(a).](images/08-the-integral-fig-02.png)
*Figure 8.2 — The Fundamental Theorem links slope and area: the accumulation A(x) has derivative f, so finding area and finding slope are inverse operations.* This is why the integral, defined as a forbidding limit of sums, is in practice computed by guessing a function and plugging in two numbers.

One distinction to keep clean: $\int_a^b f\,dx$ is a *number* (the definite integral, an accumulation), while $\int f\,dx$ without limits denotes the *family of antiderivatives* (the indefinite integral, a set of functions differing by a constant $C$). The constant matters when you reconstruct a function from its rate; it cancels when you take a difference $F(b) - F(a)$.

---

## Worked examples

### Example 1 — Distance from a velocity graph, recovering a kinematic equation

An object starts at rest and accelerates uniformly, $v(t) = at$. How far does it travel in time $T$? The distance is the area under the velocity line — a triangle of base $T$ and height $aT$, area $\tfrac{1}{2}(T)(aT) = \tfrac{1}{2}aT^2$. Confirm with the integral and the power-rule antiderivative ($F(t) = \tfrac{1}{2}at^2$, since $F'(t) = at$):

$$x = \int_0^T at\,dt = \left[\tfrac{1}{2}at^2\right]_0^T = \tfrac{1}{2}aT^2 - 0 = \tfrac{1}{2}aT^2.$$

This is exactly the kinematic equation $x = \tfrac{1}{2}at^2$ from the straight-line-motion chapter — and now we see *where it comes from*: it is the area under the velocity–time graph, the accumulation of speed over time. The kinematic equations are integrals.

### Example 2 — Work done stretching a spring (a variable force)

A spring resists with force $F = kx$ when stretched a distance $x$ (Hooke's law). The work to stretch it from $0$ to $X$ is the accumulation of force over distance — and because the force grows linearly with $x$, no single multiplication will do; we integrate. The antiderivative of $kx$ is $\tfrac{1}{2}kx^2$:

$$W = \int_0^X kx\,dx = \left[\tfrac{1}{2}kx^2\right]_0^X = \tfrac{1}{2}kX^2.$$

This is the area of the triangle under the force–distance line — the genuine area-under-a-curve that motivated the bow in the cold open. The bow stores $\tfrac{1}{2}kX^2$ of energy; that is the work your muscles did, accumulated sliver by sliver across the draw.

### Example 3 — Impulse as the area under a force–time curve

A force acting over time changes an object's momentum. Newton's second law is $F = m\,dv/dt$, so $F\,dt = m\,dv$. Accumulate both sides from $t_1$ to $t_2$:

$$\int_{t_1}^{t_2} F\,dt = \int m\,dv = m\,v_2 - m\,v_1 = \Delta p.$$

The left side is the **impulse** — the area under the force–time curve. The integral says the accumulated push equals the change in momentum, $J = \Delta p$. Same tool, a third physical face: where speed-times-time gave distance and force-times-distance gave work, force-times-time gives the change in momentum.

---

## Return to the cold open

Both opening questions are now answerable, and they are the same question. *How far did you go?* — accumulate speed over time, $x = \int_0^T v\,dt$, the area under the velocity–time graph, computed as one sliver $v\,\Delta t$ at a time and summed in the limit. *How much work did you do drawing the bow?* — accumulate force over distance, $W = \int_0^X F\,dx$, the area under the force–distance curve, $\tfrac{1}{2}kX^2$ for a spring-like bow. Neither could be done by a single multiplication, because in each a factor varied as the other ran; both yielded to chopping into slivers and summing.

And the Fundamental Theorem tied the whole of Part II together. The first question — the derivative, the slope, the instantaneous rate — and the second question — the integral, the area, the accumulation — are inverse operations. To find an accumulation you find an antiderivative: a function whose *rate of change* is the thing you are accumulating, then take its net change across the endpoints. The slope question and the area question, which felt like two unrelated puzzles when we named them in Chapter 5, are one idea seen from two sides.

---

## Where it generalizes

The integral is the mathematics of "how much accumulates," and that question is everywhere once you learn to hear it. Charge is the accumulation of current over time, $Q = \int I\,dt$. The total mass of a non-uniform object is the accumulation of its density over its volume. In probability, the chance of an outcome falling in a range is the area under a probability-density curve. In economics, consumer surplus is an area under a demand curve; total revenue is an accumulation of marginal revenue. Each is the same move — slice, form the product, sum to the limit — and each is evaluated by the same shortcut, the antiderivative and the Fundamental Theorem. What the math cannot supply is the recognition that a quantity *is* an accumulation, and the construction of the right sliver $f(x)\,dx$. A solver evaluates $\int_0^X kx\,dx$ instantly — but a human must first see that the work done by a varying force *is* a sum of (force)×(tiny displacement), build the product $F\,dx$, choose the limits $0$ and $X$, and read the resulting number as joules. The research on learning this is blunt: students master the antiderivative arithmetic and fail at the modeling — at seeing the sliver. The Fundamental Theorem hands you the arithmetic; deciding what to integrate, and why the answer means what it means, is yours.

---

## Exercises

1. **(Riemann sum by hand.)** Estimate $\int_0^4 (2x)\,dx$ using four rectangles of width 1, taking the height at the right end of each slice. Then compute the exact value with the Fundamental Theorem and explain the discrepancy. What happens to the discrepancy as the slices shrink?

2. **(Antiderivatives.)** Find the indefinite integral (include the constant $C$): (a) $\int 3x^2\,dx$; (b) $\int (4t + 1)\,dt$; (c) $\int v_0\,dt$ ($v_0$ constant); (d) $\int x^{-2}\,dx$.

3. **(Distance from velocity.)** A particle's velocity is $v(t) = 6 - 2t$ (m/s) for $0 \le t \le 3$ s. Find the displacement over those 3 seconds by integrating. Then find the *total distance traveled*, noting that $v$ changes sign — and explain why displacement and distance differ here.

4. **(Work from a force law.)** A variable force $F(x) = 12 - 3x$ (N) acts over $0 \le x \le 4$ m. Compute the work as $\int_0^4 F\,dx$. Sketch the force–distance graph and identify the area you computed.

5. **(Derivation.)** State and prove the Fundamental Theorem of Calculus, Part 1: for $A(x) = \int_a^x f(t)\,dt$ with $f$ continuous, show $A'(x) = f(x)$ directly from the limit definition of the derivative, explaining the step where the thin-strip area is approximated by $f(x)\,h$. Then explain in two or three sentences how Part 2, $\int_a^b f = F(b) - F(a)$, follows.

---

## Sources

- Bernhard Riemann, "Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe" (habilitation, 1854; pub. 1867) — the integral as the limit of sums over partitions (Riemann sums). [verified — 1854 habilitation and title confirmed; publication 1867/1868 per source, see factchecks/08-the-integral-assertions.md] (original primary source)
- Augustin-Louis Cauchy, *Résumé des leçons sur le calcul infinitésimal* (1823) — the first rigorous definition of the integral as a limit of sums for continuous functions, and a version of the Fundamental Theorem; Riemann generalized Cauchy's construction. [verified — Cauchy/Riemann credit split confirmed from secondary sources, see factchecks/08-the-integral-assertions.md and pantry] (original primary source)
- Archimedes, *Quadrature of the Parabola* and *The Method* (3rd c. BCE) — the method of exhaustion, area as a limit of approximating polygons. [verified — see factchecks/08-the-integral-assertions.md] (original primary sources)
- Gottfried Wilhelm Leibniz — the $\int$ symbol (1686) for *summa*; Isaac Barrow, *Lectiones Geometricae* (1670) — a geometric form of the Fundamental Theorem. [verified — see factchecks/08-the-integral-assertions.md] (original primary sources)
- Source chapter (this book's archive): "Work and Kinetic Energy" — work as $W = \int \vec{F}\cdot d\vec{r}$, the spring/bow example; "Motion Along a Straight Line" — displacement as the integral of velocity; "Linear Momentum and Collisions" — impulse as $\int F\,dt = \Delta p$.
- V. Sealey, "A framework for characterizing student understanding of Riemann sums and definite integrals," *Journal of Mathematical Behavior* 33 (2014): 230–245; S. R. Jones, work on the product/accumulation conception of integrals (2013, 2015) — the documented failure to connect the symbolic integral to the limit of sums and to construct $f(x)\,dx$. [verified — see factchecks/08-the-integral-assertions.md]
