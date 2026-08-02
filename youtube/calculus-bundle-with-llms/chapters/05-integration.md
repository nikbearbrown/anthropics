# Chapter 5 — Integration
*The Geometry of Accumulation, and the Theorem That Unlocked It.*

A cyclist rides for an hour. Her speedometer works perfectly — she can read her speed at any instant. At the end of the ride, she wants to know how far she went.

If she had ridden at a constant speed, the answer would be trivial: distance equals speed times time. But her speed varied. It climbed early, settled near 18 mph for a long stretch, dropped on a hill, paused at a light, climbed again. There is no single number to multiply by the hour. The answer is not a multiplication problem. It is something else.

Here is the strategy she might use without knowing any calculus. Divide the hour into sixty one-minute intervals. In each minute, her speed didn't change much — treat it as constant within that minute. Compute the distance for each minute: speed at that minute times one-sixtieth of an hour. Add up sixty numbers. You have an approximation to the actual distance.

Now divide the hour into 600 intervals of six seconds each. Better approximation. Divide into 6000 intervals of one second each. Better still. There is a pattern here: as the intervals get smaller, the estimate gets more accurate. The *exact* distance is what this process approaches in the limit, as the interval width shrinks to zero.

That limiting process has a name and a notation. The exact distance is

$$\text{distance} = \int_0^1 v(t) \, dt$$

The symbol on the right is the *definite integral* of the velocity function $v(t)$ over the interval from $t = 0$ to $t = 1$. The sliced-and-summed process is a *Riemann sum*; the definite integral is its limit.

This is what integration is. Not a formula. Not a trick. A limit of sums — the same idea from Chapter 2, applied to accumulation rather than to instantaneous rates.

---

## The machinery of Riemann sums

Let $f$ be a function defined on an interval $[a, b]$. Slice the interval into $n$ equal pieces of width

$$\Delta x = \frac{b - a}{n}$$

In each piece, pick any representative point $x_i^*$ — the left end, the right end, the midpoint, it doesn't matter for what follows. Form the sum

$$S_n = \sum_{i=1}^n f(x_i^*) \, \Delta x$$

Each term is a rectangle: height $f(x_i^*)$, width $\Delta x$. The sum approximates the area under the curve — or, in the cyclist's case, the total distance traveled.

As $n \to \infty$ and $\Delta x \to 0$, the rectangles multiply and thin. If the limit exists and doesn't depend on which representative points were chosen, we call it the definite integral:

$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \, \Delta x$$

The notation is deliberate. The integral sign $\int$ is an elongated "S" — for sum. The $dx$ is the limit of $\Delta x$, a differential sliver of width. Reading the expression aloud: "the sum of $f(x)$-times-$dx$ contributions from $a$ to $b$, as $dx$ shrinks to zero." The symbolism carries the construction inside itself.

A quick computation to see what these sums do. Estimate $\int_0^4 x^2 \, dx$ using four rectangles with the right-endpoint rule.

$\Delta x = 1$. Right endpoints: $x = 1, 2, 3, 4$. Function values: $1, 4, 9, 16$.

$$S_4 = (1 + 4 + 9 + 16)(1) = 30$$

The exact answer — which we'll compute properly in a moment — is $64/3 \approx 21.33$. The four-rectangle estimate of 30 overestimates badly, because $x^2$ is increasing and the right endpoints are the highest points in each slice. With more rectangles, the estimate closes in on $21.33$ from above.

<!-- → [IMAGE: side-by-side panels showing Riemann sum convergence for ∫₀⁴ x² dx — left panel: n=4 right-endpoint rectangles sitting above the parabola curve, with total shaded area visibly larger than the area under the curve; right panel: n=20 right-endpoint rectangles, noticeably tighter fit; label S₄ = 30 and exact = 64/3 ≈ 21.33 on the respective panels — student should see that the rectangles shrink toward the curve as n grows] -->

Any continuous function is Riemann integrable — the limit exists for any sequence of sampling choices. Functions with finitely many jumps are also integrable. This is a theorem, not obvious, and it matters because it guarantees the integral exists before we try to compute it.

---

## Why this is hard, and why there's a shortcut

Computing a definite integral directly from the Riemann-sum definition is, for all but the simplest functions, a combinatorial nightmare. For $\int_0^4 x^2 \, dx$ you can do it — you'd need the closed-form formula for $\sum_{i=1}^n i^2$ and then take a limit — but for $\int_0^1 \sin(x^2) \, dx$ there is no algebraic route through the sum. The definition is intellectually clean and computationally impractical.

The shortcut came with the discovery that integration and differentiation are inverse operations. This is so surprising, and so consequential, that it is called the *Fundamental Theorem of Calculus*.

Here is why it's surprising. The derivative is a *local* concept. It asks how fast a function is changing at a single point — a rate, an instantaneous slope. The integral is a *global* concept. It asks how much has accumulated over an entire interval — a running total across all the slices. These don't obviously have anything to do with each other.

And yet.

Define a function $F$ by

$$F(x) = \int_a^x f(t) \, dt$$

$F(x)$ is the accumulation of $f$ from $a$ up to $x$ — a running total. Ask what happens when $x$ increases by a tiny amount $h$:

$$F(x + h) - F(x) = \int_x^{x+h} f(t) \, dt \approx f(x) \cdot h$$

The right side approximation improves as $h \to 0$, because $f$ is nearly constant over a tiny interval. Divide both sides by $h$ and take the limit:

$$F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x)}{h} = f(x)$$

The running total's instantaneous rate of change is exactly $f(x)$. Differentiating the accumulation recovers what was being accumulated.

This is the Fundamental Theorem, Part 1. Differentiation undoes integration.

<!-- → [IMAGE: diagram illustrating FTC Part 1 — plot a positive curve f(t) above the t-axis; shade the area under f from a to x in one color to represent F(x); shade the thin additional strip from x to x+h in a contrasting color to represent F(x+h) − F(x); label the strip width as h and its height as approximately f(x); show the equation F(x+h) − F(x) ≈ f(x)·h beneath — student should see that the derivative of the accumulated area is the height of the curve at the leading edge] -->

---

## The Fundamental Theorem and why it works

Part 2 is the computational engine.

*FTC Part 2*: If $f$ is continuous on $[a, b]$ and $F$ is any antiderivative of $f$ — meaning $F'(x) = f(x)$ — then

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

The proof is almost immediate from Part 1. Let $G(x) = \int_a^x f(t) \, dt$ be the specific accumulation function. By Part 1, $G'(x) = f(x)$. If $F$ is any other antiderivative of $f$, then $F'(x) = G'(x)$, so $F$ and $G$ differ by a constant: $F(x) = G(x) + C$. Then

$$F(b) - F(a) = [G(b) + C] - [G(a) + C] = G(b) - G(a) = \int_a^b f(t) \, dt$$

The constant cancels. Any antiderivative works; the choice doesn't affect $F(b) - F(a)$.

Apply it to the integral we estimated. Find an antiderivative of $x^2$: by the power rule in reverse, $F(x) = x^3/3$. Check: $F'(x) = 3x^2/3 = x^2$. Then

$$\int_0^4 x^2 \, dx = F(4) - F(0) = \frac{64}{3} - 0 = \frac{64}{3}$$

That's the $21.33$ the Riemann sums were converging toward. No sum, no limit calculation, no combinatorics. Just antidifferentiate and evaluate at the endpoints.

The FTC turns a problem in approximation and limits into a problem in finding antiderivatives. That is the trade it makes: effortless computation for anything with a known antiderivative, silence on everything without one.

<!-- → [INFOGRAPHIC: two-column diagram contrasting the two routes to ∫₀⁴ x² dx — left column labeled "Definition (Riemann sum)": shows the sum formula, requires knowing Σi² = n(n+1)(2n+1)/6, shows limit calculation, arrives at 64/3; right column labeled "FTC (antiderivative)": shows F(x) = x³/3, evaluates F(4) − F(0) = 64/3 − 0 in two steps — the visual argument is that both columns reach the same answer, but the right column is dramatically shorter] -->

---

## The indefinite integral and the basic antiderivatives

When you want the antiderivative of $f$ without specifying limits, you write the *indefinite integral*:

$$\int f(x) \, dx = F(x) + C$$

The $+ C$ is not decoration. It is the whole family of antiderivatives. Since any constant differentiates to zero, any function of the form $F(x) + C$ is a valid antiderivative. The indefinite integral is a family, not a single function.

The basic antiderivatives come from reversing the derivative formulas:

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)$$

$$\int x^{-1} \, dx = \ln|x| + C$$

$$\int e^x \, dx = e^x + C$$

$$\int \cos x \, dx = \sin x + C$$

$$\int \sin x \, dx = -\cos x + C$$

$$\int \frac{1}{1 + x^2} \, dx = \arctan x + C$$

Each formula is a derivative formula run backwards. The power rule gives $\frac{d}{dx}[x^{n+1}/(n+1)] = x^n$; flip it to get the antiderivative of $x^n$. The derivative of $\sin x$ is $\cos x$; flip it to get the antiderivative of $\cos x$.

Linearity carries over cleanly:

$$\int [c \cdot f(x) + d \cdot g(x)] \, dx = c \int f(x) \, dx + d \int g(x) \, dx$$

<!-- → [TABLE: two-column reference card of basic antiderivatives — left column: integrand f(x); right column: antiderivative F(x) + C; rows: xⁿ (n≠−1) → xⁿ⁺¹/(n+1)+C; x⁻¹ → ln|x|+C; eˣ → eˣ+C; cos x → sin x+C; sin x → −cos x+C; 1/(1+x²) → arctan x+C — pair each row with the corresponding derivative rule it reverses, shown in a light third column, so the student sees the table as a mirror image of the derivative table from Chapter 3] -->

Constants factor out; sums split. What doesn't carry over is products. There is no formula like $\int f(x) g(x) \, dx = (\int f) \cdot (\int g)$. Products are genuinely harder to integrate than to differentiate — the product rule of differentiation has an integration analog, but it's called integration by parts and it belongs in the next chapter. For now, the rule to internalize is that you cannot distribute an integral across a product.

---

## Substitution: the chain rule in reverse

Differentiation has a chain rule: $\frac{d}{dx}[F(g(x))] = F'(g(x)) \cdot g'(x)$.

Run it in reverse. If you see an integrand of the form $F'(g(x)) \cdot g'(x)$, you know the antiderivative is $F(g(x))$. The substitution method is how you see it.

The procedure. Identify an inner function $u = g(x)$. Compute $du = g'(x) \, dx$. Rewrite the integral in terms of $u$. If the substitution was right, everything simplifies.

Example: $\int 2x \cos(x^2) \, dx$.

Let $u = x^2$. Then $du = 2x \, dx$. The integral becomes

$$\int \cos u \, du = \sin u + C = \sin(x^2) + C$$

Check by differentiating: $\frac{d}{dx}[\sin(x^2)] = \cos(x^2) \cdot 2x$. Correct.

With definite integrals, substitution changes the limits too. Example: $\int_0^1 (3x^2 + 1)\sqrt{x^3 + x + 1} \, dx$.

Let $u = x^3 + x + 1$. Then $du = (3x^2 + 1) \, dx$. When $x = 0$: $u = 1$. When $x = 1$: $u = 3$.

$$\int_1^3 \sqrt{u} \, du = \frac{2}{3} u^{3/2} \bigg|_1^3 = \frac{2}{3}(3\sqrt{3} - 1) \approx 2.80$$

The limits converted from $x$-values to $u$-values. You don't substitute back at the end — when you change variables in a definite integral, you change everything, including the limits.

The substitution method's elegance is the same as the chain rule's: it handles an infinite family of compositions with a single pattern. Once you can recognize $g'(x) \, dx$ hiding in an integrand and identify the matching $u = g(x)$, an enormous range of integrals collapses to basic forms. The skill is in the recognition.

<!-- → [INFOGRAPHIC: step-by-step flowchart for u-substitution — box 1: "Identify inner function u = g(x)"; box 2: "Compute du = g′(x) dx"; box 3: "Rewrite integrand entirely in terms of u and du"; box 4a (indefinite): "Integrate in u, then back-substitute u = g(x)"; box 4b (definite): "Convert limits: x=a → u=g(a), x=b → u=g(b); integrate in u; do NOT back-substitute" — show the ∫ 2x cos(x²) dx example flowing through boxes 1–4a alongside the flowchart] -->

---

## What the integral is measuring

Before the FTC took over the calculations, it's worth being clear about what the integral measures — because the Riemann-sum definition says it geometrically, and the geometry is the source of all the applications.

When $f(x) \geq 0$ on $[a, b]$, the definite integral $\int_a^b f(x) \, dx$ is the area of the region bounded by the curve, the $x$-axis, and the vertical lines $x = a$ and $x = b$. Each rectangle in the Riemann sum is a slice of that area; the limit is the whole area. The integral is area.

When $f$ dips below zero, the rectangles in the negative region have negative heights, and the integral counts negative area there — the net signed area, with regions above the axis positive and regions below negative. If you want the total geometric area (unsigned), you integrate $|f(x)|$ instead.

<!-- → [IMAGE: signed area diagram for a function that crosses the x-axis — plot a curve that is positive on [a, c] and negative on [c, b]; shade the positive region above the axis in one color labeled "+A₁"; shade the negative region below in a contrasting color labeled "−A₂"; show the equation ∫ₐᵇ f dx = A₁ − A₂ (net signed area) vs ∫ₐᵇ |f| dx = A₁ + A₂ (total geometric area); label which quantity the definite integral computes by default] -->

When $f$ is velocity, the integral is displacement. When $f$ is a force, the integral against distance is work. When $f$ is a density (mass per unit length, charge per unit area), the integral is the total mass or charge. When $f$ is a rate of cash flow, the integral is total accumulated value. All of these are the same mathematical object seen in different physical contexts. The Riemann sum is always: break the quantity into small pieces, add them up, take the limit. The interpretation changes; the mathematics doesn't.

There is a useful sanity check built into the units. The integral $\int_a^b f(x) \, dx$ has units equal to the units of $f$ multiplied by the units of $x$. Velocity in miles per hour integrated against time in hours gives miles. Force in newtons integrated against distance in meters gives joules. If the units don't multiply correctly, the setup is wrong.

---

## The theorem Newton and Leibniz both found

Newton and Leibniz each arrived at the FTC independently in the 1670s and 1680s, and a bitter priority dispute followed — one of the nastier episodes in the history of mathematics, eventually leaving mathematics divided between British notation (Newton's fluxions, $\dot{x}$ for derivatives) and Continental notation (Leibniz's $dy/dx$ and $\int$). British mathematicians stubbornly used Newton's notation for over a century, cutting themselves off from the more flexible Leibniz formalism that the rest of Europe was developing. It was not until the early nineteenth century that British mathematicians, led by the Analytical Society at Cambridge, systematically adopted the Continental notation.

What both Newton and Leibniz saw — what earlier mathematicians like Fermat, Cavalieri, and Barrow had separately developed methods for tangent slopes and for areas without connecting them — was that the two operations were inverses. That connection was the central achievement. The Riemann-sum definition of the integral came later, in the 1850s, when Bernhard Riemann put the foundations on firmer ground. Newton and Leibniz had both been working with the intuitive notion; Riemann made it precise.

The philosophical content of the FTC is one of the great surprises in mathematics. The rate of change at a point — an infinitesimal, local concept — is the complete information needed to recover the accumulated total. Conversely, the accumulated total — a global integral over an entire interval — fully determines the rate at each instant. Local and global descriptions of a changing quantity are equivalent, interchangeable, two sides of one object.

---

## What integration cannot do

It is important to be clear about what the FTC's machinery doesn't solve.

Many functions have no elementary antiderivative. The Gaussian $e^{-x^2}$ is the most famous: it is smooth, it is positive, it has a perfectly well-defined integral over any interval, and it has absolutely no antiderivative expressible in terms of the functions taught in calculus — no combination of polynomials, exponentials, logarithms, and trigonometric functions will give $e^{-x^2}$ when differentiated. This is not a gap in anyone's knowledge; it has been proven, by Liouville in the 1830s, that no such expression exists. The definite integral $\int_{-\infty}^{\infty} e^{-x^2} \, dx$ does have an exact value — it equals $\sqrt{\pi}$, found by a clever trick in polar coordinates — but the indefinite integral defines a new function, the error function $\text{erf}(x)$, which cannot be reduced to more familiar ones.

Similarly for $(\sin x)/x$, $e^x/x$, and many others. For these, numerical integration takes over: Riemann sums with many intervals, Simpson's rule, Gaussian quadrature. Each method approximates the integral to any desired precision without needing a closed-form antiderivative.

The structural lesson is this: calculus did not give a method that always produces clean formulas. It gave a method that always produces *approximations to arbitrary precision*. For physics, for engineering, for probability, that is sufficient. For pure mathematics, the limits of elementary antidifferentiation motivated two centuries of new theory — complex analysis, special functions, real analysis — aimed at extending the catalog of integrable forms.

---

## Closing the loop: the cyclist, computed

Return to the cyclist. Suppose her velocity is

$$v(t) = 18 + 5\sin(2\pi t)$$

in mph over one hour. The integral of velocity is distance:

$$\int_0^1 (18 + 5\sin(2\pi t)) \, dt = 18 \int_0^1 dt + 5 \int_0^1 \sin(2\pi t) \, dt$$

The first integral is $18 \cdot 1 = 18$. For the second, substituting $u = 2\pi t$:

$$\int_0^1 \sin(2\pi t) \, dt = \left[-\frac{\cos(2\pi t)}{2\pi}\right]_0^1 = -\frac{1}{2\pi} + \frac{1}{2\pi} = 0$$

Total distance: 18 miles. The sinusoidal fluctuation contributed nothing — the time spent above 18 mph exactly offset the time spent below, because sine averages to zero over a full period. The fluctuation was real; its net effect on distance was not.

Now make the problem harder. Suppose the hill in the middle of the ride drops her speed:

$$v(t) = 18 - 6 e^{-100(t - 0.5)^2}$$

The exponential term models a sharp, temporary dip centered at $t = 0.5$, falling up to 6 mph at the worst. The total distance is

$$\int_0^1 v(t) \, dt = 18 - 6 \int_0^1 e^{-100(t - 0.5)^2} \, dt$$

The remaining integral has no elementary antiderivative — the Gaussian again, rescaled and shifted. Numerical integration with a modest number of subintervals gives approximately $0.177$, so the total distance is $18 - 6(0.177) \approx 16.94$ miles.

<!-- → [CHART: plot of the two cyclist velocity profiles on the same axes from t=0 to t=1 — curve 1: v(t) = 18 + 5sin(2πt), oscillating gently above and below 18 mph, labeled "sinusoidal profile — net area = 18 miles"; curve 2: v(t) = 18 − 6·exp(−100(t−0.5)²), showing a sharp Gaussian dip to ~12 mph centered at t=0.5, labeled "Gaussian hill profile — net area ≈ 16.94 miles"; shade the area under each curve to make the accumulated distance visually obvious; mark the dip's depth and location on curve 2] -->

The FTC answered the first version exactly. It reduced the second version to a number we compute numerically. Both routes go through the same concept: the integral is accumulated velocity, the calculation method adapts to what's available.

---

## The one idea to carry forward

The definite integral is a limit of sums. The FTC connects it to antiderivatives, making most integrals computable in practice. Substitution handles compositions. Linearity handles sums and constant multiples. Numerical methods handle everything without a closed-form antiderivative.

But under all the technique is one idea: *integration is accumulation*. Break a quantity into pieces. Multiply the rate by the size of the piece. Add everything up. Take the limit as the pieces shrink. That is the integral — in physics, in geometry, in probability, in economics, in every field that has to sum up infinitely many infinitesimal contributions. The FTC is the shortcut. The Riemann sum is the meaning.

In the next chapter, this meaning gets applied: areas between curves, volumes, arc lengths, work, and every other accumulation problem the derivative-based framework of Chapters 3 and 4 left open. The strategy will always be the same: slice, integrate, evaluate.

---

## LLM Exercises

The following exercises are designed for working interactively with an AI assistant. For each, the productive move is not to ask for the answer directly — it's to reason aloud, explain your thinking, and ask the AI to identify errors or push back on your reasoning.

1. **Reconstruct the Riemann sum from scratch.** Without looking at the chapter, explain to the AI what a Riemann sum is, why the choice of sample point doesn't affect the final limit, and what it means for a function to be Riemann integrable. Ask it to challenge any step that relies on intuition rather than argument.

2. **Derive FTC Part 1 in your own words.** Walk through the argument that $F'(x) = f(x)$ where $F(x) = \int_a^x f(t) \, dt$. Don't copy the chapter's version — reconstruct the reasoning. Submit it to the AI and ask: "Where am I waving my hands? What would need to be made more rigorous?"

3. **Find the flaw in a wrong antiderivative.** Tell the AI you are computing $\int_0^1 x \cdot e^{x^2} dx$ and that you claim the answer is $\frac{1}{2}(e - 1)$. Ask it to check your work step by step. (It is correct — but work through the substitution yourself first before confirming.)

4. **Design a physical integral.** Pick any physical quantity that accumulates — heat dissipated, charge stored, money earned, fuel consumed — and describe it as a definite integral. Tell the AI your setup: what $f$ represents, what $x$ represents, what the limits are, what the units work out to. Ask it to verify the unit analysis and suggest one thing that could go wrong in the physical model.

5. **Explain why $e^{-x^2}$ has no elementary antiderivative — or try.** Attempt to explain Liouville's result in your own words: not the full proof, but the intuition for why this should be true. Ask the AI where your explanation is correct, where it oversimplifies, and what a rigorous statement of the result would actually say.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Bernhard Riemann** introduced the rigorous definition of the integral that bears his name in 1854 — partitioning intervals into smaller and smaller pieces and taking the limit of the sums. The Riemann sum you computed in this chapter is the foundation of every modern integration technique.

**Run this:**

```
Who was Bernhard Riemann, and how does the Riemann integral connect to the integration concepts we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Bernhard Riemann"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to compute a Riemann sum on one specific function by hand and compare it with the exact integral.
- Ask it about Riemann's other contributions — Riemann surfaces, the Riemann zeta function, Riemannian geometry — and which one led to general relativity.

What changes? What gets better? What gets worse?
