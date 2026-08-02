# Chapter 1 — Functions and Graphs

## TL;DR

- How a scale that hides a factor of 350 inside two digits forces you to understand what a function actually does.
- The chapter moves through What a function actually is, The families, The trigonometric family, unit-circle style, Inverses, exponentials, and logarithms, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*How a scale that hides a factor of 350 inside two digits forces you to understand what a function actually does.*

![Horizontal number line showing 7](images/01-functions-and-graphs-fig-01.png)
*Figure 1.1 — Horizontal number line showing 7*

Three numbers: 7.3, 8.2, 9.

They appeared in the news within a few years of each other. The first was Haiti, 2010. The third was Japan, 2011. The second was Chile, 2014. When you see them written like that — 7.3, 8.2, 9 — they look almost the same. A range of less than two. You might say Japan was "about twenty-five percent worse" than Haiti the way you'd say one temperature is warmer than another.

That comparison is off by a factor of roughly 350.

The Japan earthquake did not release twenty-five percent more energy than the Haiti earthquake. It released somewhere around 350 times more. The same string of digits, the same compact little scale, hiding a difference that's larger than the entire Gulf War's explosive yield. And if you didn't know what the Richter scale actually *is* — not what it's called, but what it *does* — you couldn't see that. The numbers would just sit there looking nearly equal.

What the Richter scale *does* is take a quantity that spans an enormous range — ground-motion amplitude, varying across many orders of magnitude between a tiny tremor and a catastrophic rupture — and compress it into something a human can read. The way it compresses is the interesting part. Every time you add 1 to the magnitude, you don't add a fixed amount to the amplitude. You *multiply* by 10. So going from magnitude 7.3 to magnitude 9 means multiplying the amplitude by $10^{9-7.3} = 10^{1.7} \approx 50$. Then, because seismic energy scales not linearly with amplitude but as amplitude raised to the 1.5 power, the energy ratio is $50^{1.5} \approx 350$. 

The tool that hides multiplication inside addition — that turns "add 1.7 to the exponent" into a tenfold jump in the underlying thing — is called a *logarithm*. To undo it and get the real physical quantity back, you apply the *inverse function*, the exponential. This chapter is about exactly that machinery: what functions are, what their inverses are, and why the logarithm and exponential are inverses of each other in a way that lets you compress and recover enormous quantities.

This is the algebraic foundation that calculus assumes you have. Every concept we'll meet in Chapter 2 and beyond — limits, derivatives, integrals — is a statement about *functions*. If "function" stays a vague idea, the rest of the course is built on sand. So we're going to be precise about it now, while it's still the main event and not background noise.

---

## What a function actually is

A *function* is a rule. It takes an input and assigns to it exactly one output. That's it. The whole definition is in that phrase: exactly one output per input.

The set of allowed inputs is the *domain*. The set where outputs land is the *range*. The notation $f \colon D \to R$ says: $f$ is a rule that takes things from the domain $D$ and sends them to the range $R$. When you write $f(x)$, you mean the specific output the rule produces when you feed it the input $x$.

The "exactly one" is not decoration — it's the whole thing. A rule that might give you two different outputs for the same input is not a function. This sounds abstract. Here's why it matters concretely: every equation in physics, every formula in economics, every algorithm in a computer program is claiming to be a function. They're claiming that given the inputs, there is one determined output. The "exactly one" is the promise that the world is, at least locally, deterministic.

Functions wear four different outfits, and fluency means being comfortable with all of them.

A *formula* like $f(x) = x^2 + 3$ is compact and exact and calculable — but it hides the shape. A *graph* in the $(x,y)$-plane shows you the shape immediately — but it loses precision and can't represent functions on infinite domains fully. A *table* of input-output pairs is concrete and grounded — but a function on the real numbers has infinitely many inputs, so a table is always incomplete. A verbal description — "the height of a thrown ball $t$ seconds after release" — is how functions actually appear in the physical world, before anyone writes a formula.

Real problems require shuttling between these four representations constantly. You read a verbal description, translate it to a formula, compute an output, then interpret the output back in words. Miss any step in that translation and you get a wrong answer that looks right because the arithmetic was fine.

![Four-panel grid showing the same function f(x) =](images/01-functions-and-graphs-fig-02.png)
*Figure 1.2 — Four-panel grid showing the same function f(x) =*

The *vertical line test* is the graph version of "exactly one output per input." Any vertical line should cross the graph of a function at most once. If it crosses twice, you have two outputs for one input, and whatever you're drawing isn't a function.

![Two side-by-side graphs ](images/01-functions-and-graphs-fig-03.png)
*Figure 1.3 — Two side-by-side graphs *

*Composition* is the operation that genuinely distinguishes functions from ordinary numbers. $(f \circ g)(x) = f(g(x))$ means: first apply $g$ to $x$, then apply $f$ to whatever came out. The key fact is that order matters. $f \circ g$ and $g \circ f$ are generally different:

$$
f(x) = x^2, \quad g(x) = x + 1
$$
$$
(f \circ g)(x) = (x+1)^2 = x^2 + 2x + 1
$$
$$
(g \circ f)(x) = x^2 + 1
$$

Different functions. The first squares first, then adds. The second adds first, then squares. The order changed the output. This non-commutativity — the fact that you can't always swap the order of operations — is something calculus inherits and that the chain rule (Chapter 3) is specifically built to handle.

![Two horizontal pipeline diagrams ](images/01-functions-and-graphs-fig-04.png)
*Figure 1.4 — Two horizontal pipeline diagrams *

One more vocabulary item worth having now: a function is *increasing* on an interval if larger inputs give larger outputs there, and *decreasing* if larger inputs give smaller outputs. A function is *even* if $f(-x) = f(x)$ — symmetric across the $y$-axis, like $x^2$ or $\cos x$. It's *odd* if $f(-x) = -f(x)$ — rotationally symmetric about the origin, like $x^3$ or $\sin x$.

---

## The families

Calculus works mostly with functions from a short list of families. Knowing the family means knowing the shape, the growth rate, the smoothness, and the domain restrictions in advance. Let me walk through them.

**Polynomials.** A polynomial of degree $n$ looks like $a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$. Polynomials are defined for every real number and are smooth everywhere — no breaks, no corners. The leading term controls what happens as $x$ gets very large or very negative: positive even degree means both ends go up; positive odd degree means the right end goes up and the left end goes down.

Lines ($mx + b$) and parabolas ($ax^2 + bx + c$) are special cases you already know. Lines have constant slope; the slope is the rate of change, and it's the same everywhere. Parabolas open up when $a > 0$ and down when $a < 0$, with vertex at $x = -b/(2a)$.

**Rational functions.** Quotients of polynomials, like $f(x) = (x^2 + 1)/(x - 3)$. The interesting behavior in rational functions lives at the zeros of the denominator — values of $x$ where division by zero would occur, which are excluded from the domain. Near those points, the function might blow up to infinity, or it might be removable (a hole in the graph). Which one it is depends on whether the same zero appears in the numerator.

**Algebraic functions.** Everything you can build from polynomials using addition, subtraction, multiplication, division, and roots. $\sqrt{x}$ is algebraic; so is $\sqrt[3]{x^2 - 1}$. Roots introduce domain restrictions: you can't take an even root of a negative number (in the reals), so $\sqrt{x}$ lives only for $x \geq 0$.

**Transcendental functions.** Functions that *cannot* be built algebraically from polynomials, no matter how many operations you use. The trigonometric functions are transcendental. So are the exponential and logarithmic functions. Transcendental functions are named for the Latin "transcendere" — to climb beyond — meaning they transcend the reach of algebra alone.

| Family | Representative example | Domain | Smooth everywhere? | Grows faster than all polynomials? |
| --- | --- | --- | --- | --- |
| polynomial, rational, algebraic | root, exponential, logarithmic, trigonometric | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

The common confusion worth flagging: $b^x$ and $x^b$ are completely different functions that happen to use the same notation structure. In $b^x$, the variable is the exponent and the base is fixed — that's exponential, and it grows (or decays) at a rate proportional to its current value. In $x^b$, the variable is the base and the power is fixed — that's a power function, polynomial-style. An exponential eventually outgrows any polynomial, no matter how large the polynomial's degree. They are not even in the same family.

![Eventually always wins — no matter the polynomial's degree, the exponential catches up and passes it](images/01-functions-and-graphs-fig-05.png)
*Figure 1.5 — Four curves on the same axes *

---

## The trigonometric family, unit-circle style

Trigonometry in calculus is done on the *unit circle* — the circle of radius 1 centered at the origin. Here's the key picture: an angle $\theta$, measured in radians as an arc length along the circle starting from $(1,0)$ going counterclockwise, points to a specific location on the circle. That location is $(\cos\theta, \sin\theta)$. That's not a definition to memorize — it's the whole picture. Cosine is the $x$-coordinate, sine is the $y$-coordinate, and the Pythagorean theorem applied to that picture immediately gives you

$$\sin^2\theta + \cos^2\theta = 1$$

because the point is on a circle of radius 1, and radius squared is $x^2 + y^2$.

![Cosine is the x-coordinate. Sine is the y-coordinate. The Pythagorean identity is just x² + y² = 1 applied to the radius.](images/01-functions-and-graphs-fig-06.png)
*Figure 1.6 — Unit circle with a point P at a*

Everything else in trig follows from this one picture:

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}, \quad \cot\theta = \frac{\cos\theta}{\sin\theta}, \quad \sec\theta = \frac{1}{\cos\theta}, \quad \csc\theta = \frac{1}{\sin\theta}
$$

Why radians? Because one radian is the angle subtended by an arc of length 1 on the unit circle — which means when the angle is measured in radians, arc length and angle measure are the same number. That identification is what makes the derivative of $\sin\theta$ come out to exactly $\cos\theta$, with no extra constant cluttering the formula. In degrees, the derivative of $\sin\theta$ would be $(\pi/180)\cos\theta$, and every formula in calculus would carry that conversion factor around forever. Radians are not an arbitrary choice; they're what makes the calculus clean.

The conversion: $360° = 2\pi$ radians. So $180° = \pi$, $90° = \pi/2$, $60° = \pi/3$, $45° = \pi/4$, $30° = \pi/6$. The reference angles $\pi/6$, $\pi/4$, $\pi/3$ are the ones worth knowing exactly, because they give exact values for sine and cosine — and because every angle in common use can be reduced to one of them plus a quadrant sign.

| angle in radians | degrees | sin | cos | tan — all values exact (fractions |
| --- | --- | --- | --- | --- |
| π | 6 (30° | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| π | 4 (45° | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| π | 3 (60° | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| π | 2 (90° | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| columns: angle in radians, degrees, sin, cos, tan | all values exact (fractions and radicals, not decimals | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| designed as a memorization target and lookup tool | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

Here's how that reduction works in practice. Find $\sin(7\pi/6)$ exactly.

$7\pi/6 = \pi + \pi/6$: that's the standard $\pi/6$ angle pushed past the negative $x$-axis into the third quadrant. The *reference angle* is $\pi/6$, for which $\sin(\pi/6) = 1/2$. In the third quadrant, both sine and cosine are negative. So $\sin(7\pi/6) = -1/2$.

The pattern is general: find the reference angle, look up the positive value, apply the sign from the quadrant. Every trig evaluation at a "non-standard" angle reduces to this three-step procedure.

![Three steps: find the reference angle, look up the positive value, apply the quadrant sign](images/01-functions-and-graphs-fig-07.png)
*Figure 1.7 — Unit circle with all four quadrants labeled with*

Periodicity: $\sin$ and $\cos$ have period $2\pi$ — go all the way around the circle and you're back where you started. $\tan$ has period $\pi$ — halfway around, and the ratio $\sin/\cos$ repeats, because both numerator and denominator change sign together, canceling.

The two angle-sum identities are the productive ones — every other trig identity descends from them:

$$
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$
$$
\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$

Set $\alpha = \beta = \theta$ to get the double-angle formulas. Set $\beta = -\alpha$ to get the Pythagorean identity again. The whole library of trig identities is a small set of pictures and two formulas.

---

## Inverses, exponentials, and logarithms

Back to the earthquake. The magnitude $M$ was a *logarithm* of the amplitude $A$: $M = \log_{10}(A/A_0)$. To recover $A$ from $M$, you apply the inverse — the exponential — and write $A = A_0 \cdot 10^M$. The logarithm and the exponential are inverses. Each undoes what the other did.

This is the general concept. A function $f$ has an *inverse* $f^{-1}$ precisely when $f$ is *one-to-one* — each output corresponds to at most one input. The visual test is the *horizontal line test*: any horizontal line should cross the graph of $f$ at most once. If a horizontal line crosses twice, two inputs gave the same output, and you can't tell which one to return when asked for the inverse.

The function $f(x) = x^2$ on all real numbers is not one-to-one: $f(2) = f(-2) = 4$. Restrict to $x \geq 0$, and each output $y \geq 0$ corresponds to exactly one input: $\sqrt{y}$. That's the inverse. Restriction of domain is how non-one-to-one functions get inverses anyway — you agree to work on a piece of the domain where the function behaves.

![Figure ](images/01-functions-and-graphs-fig-08.png)
*Figure 1.8 — Figure *

To find an inverse algebraically: write $y = f(x)$, swap $x$ and $y$, solve for $y$. What you get is $y = f^{-1}(x)$. Let's check this on a concrete example.

$f(x) = x^3 + 4$.

Set $y = x^3 + 4$. Swap: $x = y^3 + 4$. Solve: $y^3 = x - 4$, so $y = \sqrt[3]{x - 4}$. Therefore $f^{-1}(x) = \sqrt[3]{x - 4}$.

Verify: $f^{-1}(f(x)) = \sqrt[3]{(x^3 + 4) - 4} = \sqrt[3]{x^3} = x$. ✓

The graphs of $f$ and $f^{-1}$ are mirror images of each other across the line $y = x$. Swapping $x$ and $y$ in the algebra is exactly what reflection across $y = x$ does geometrically. The algebra and the geometry are saying the same thing.

### Exponential functions

$f(x) = b^x$ for fixed $b > 0$, $b \neq 1$. The base $b$ determines whether the function grows or decays: $b > 1$ gives growth, $0 < b < 1$ gives decay. The domain is all of $\mathbb{R}$; the range is $(0, \infty)$ — exponentials never reach zero or go negative, no matter what $x$ does.

The exponent rules are the algebraic backbone:

$$
b^x \cdot b^y = b^{x+y}, \quad \frac{b^x}{b^y} = b^{x-y}, \quad (b^x)^y = b^{xy}
$$

These hold for all real exponents.

The *natural exponential* $f(x) = e^x$ uses the base $e \approx 2.71828$. Euler's number $e$ is the unique base for which the derivative of $b^x$ equals $b^x$ itself — meaning the natural exponential is its own rate of change. We'll see exactly why that's true in Chapter 3. For now, know that $e$ is not an arbitrary choice; it's the base that makes calculus simplest.

![Three exponential curves on the same axes ](images/01-functions-and-graphs-fig-09.png)
*Figure 1.9 — Three exponential curves on the same axes *

### Logarithmic functions

The logarithm base $b$ is the inverse of $b^x$. By definition: $\log_b x = y$ if and only if $b^y = x$. The domain is $(0, \infty)$ — you can only take logarithms of positive numbers — and the range is all of $\mathbb{R}$.

The three rules of logarithms follow directly from the three exponent rules, because the logarithm is the inverse of the exponential:

$$
\log_b(xy) = \log_b x + \log_b y
$$
$$
\log_b\!\left(\frac{x}{y}\right) = \log_b x - \log_b y
$$
$$
\log_b(x^p) = p\log_b x
$$

| Item | Meaning |
| --- | --- |
| b^x · b^y = b^(x+y)) / (log_b(xy) = log_b x + log_b y | A concrete checkpoint for applying the chapter concept. |
| b^x | b^y = b^(x−y)) / (log_b(x |
| b^x)^p = b^(xp)) / (log_b(x^p) = p log_b x) | student should see that the log rules are not three new facts but the same three rules written in inverse notation |

Read these rules carefully. The first one says the logarithm turns multiplication into addition. That's not a coincidence or a trick — it's the entire structural reason logarithms exist. Before electronic computation, all multiplication of large numbers was done by converting to logarithms (look up in a table), adding, then converting back. The exponent rules and the log rules are the same rules, expressed in different notation.

The *natural logarithm* $\ln x = \log_e x$ is the inverse of $e^x$. It's the one you'll see most in calculus.

The *change-of-base formula* connects all logarithms:

$$
\log_b x = \frac{\ln x}{\ln b}
$$

Any logarithm in any base can be computed from natural logs.

### Closing the loop

The Japan quake had $M = 9$; the Haiti quake had $M = 7.3$. The magnitude is $M = \log_{10}(A/A_0)$, so the amplitude ratio is:

$$
\frac{A_\text{Japan}}{A_\text{Haiti}} = 10^{9 - 7.3} = 10^{1.7} \approx 50
$$

Seismic energy scales as amplitude to the 1.5 power:

$$
\frac{E_\text{Japan}}{E_\text{Haiti}} = 50^{1.5} \approx 350
$$

Two numbers, 7.3 and 9, that looked almost the same. One inverse function — the exponential undoing the logarithm — and the real comparison emerges. The entire chapter's machinery in one calculation.

---

## The synthesis

Here is what you now have. Functions are precise rules. They live in families: polynomial, algebraic, transcendental. They can be combined by arithmetic and by composition. They can be transformed — shifted, stretched, reflected — in predictable ways that produce predictable changes in the graph. They have inverses when they're one-to-one, and the inverse's graph is the original's mirror image across $y = x$. The exponential and logarithmic functions are inverses of each other, and that relationship turns multiplication into addition, which is why every scale that spans many orders of magnitude — earthquakes, sound levels, acidity, stellar brightness — is logarithmic.

And every single one of these concepts is a statement *about functions*. That's not a coincidence. Calculus is the study of functions: their behavior near a point (limits), their rates of change (derivatives), and their accumulated totals (integrals). The function vocabulary in this chapter is the language that Chapter 2 is written in. Without it, the definitions don't parse. With it, they fall into place.

!["Logarithmic scales in the wild" ](images/01-functions-and-graphs-fig-10.png)
*Figure 1.10 — "Logarithmic scales in the wild" *

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a collaborative thinking partner — asking it to check your reasoning, generate similar problems, or explain a step you're stuck on. The goal is to think alongside the tool, not to have the tool think for you.

**Exercise 1.** Tell an LLM: "I want to understand why the horizontal line test determines whether a function has an inverse. Explain the connection between the test and the definition of one-to-one, and then give me two examples — one function that passes and one that fails — along with their graphs described in words." Evaluate the explanation it gives. Does it connect the geometry to the algebra, or does it just state the rule?

**Exercise 2.** Give an LLM the function $f(x) = \ln(x^2 + 1)$ and ask it to identify: the domain, the range, whether the function is even or odd, and what family it belongs to. Then ask it to find the composition $f \circ g$ where $g(x) = e^x - 1$. Check whether it simplifies the composition correctly all the way to a clean form.

**Exercise 3.** Ask an LLM to explain why the derivative of $\sin x$ is $\cos x$ *only* when $x$ is measured in radians, not degrees. Ask it to show what happens to the formula if you use degrees. Evaluate whether the explanation gets at the underlying reason — the arc-length definition of radians — or just states the result.

**Exercise 4.** Give an LLM the equation $\log_2(x+1) + \log_2(x-1) = 3$ and ask it to solve for $x$. Before seeing its work, solve it yourself by combining the logarithms first. Compare approaches. Did the LLM check the solution against the original domain constraints?

**Exercise 5.** The Richter magnitude was described in this chapter as $M = \log_{10}(A/A_0)$. Ask an LLM to explain the pH scale (chemistry), the decibel scale (acoustics), and the apparent magnitude scale (astronomy) in the same terms — identifying what physical quantity is being logarithmically compressed, what the base is, and what the reference value represents. Then ask it to compute: how many times more intense is a sound at 90 dB than a sound at 60 dB?

**Exercise 6.** Ask an LLM to help you find the inverse of $f(x) = (2x+3)/(x-1)$. Walk through the algebra yourself first — swap $x$ and $y$, isolate $y$ — then compare your steps to the LLM's. Verify the inverse by computing $f(f^{-1}(x))$ and checking that it simplifies to $x$. Ask the LLM to explain geometrically what it means that $f$ and $f^{-1}$ are reflections across $y = x$.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Sophie Germain** taught herself calculus during the French Revolution by reading Lagrange and Euler — sometimes corresponding with Gauss under the male pseudonym M. Le Blanc. Her work on Fermat's Last Theorem and on elasticity theory earned her a Paris Academy prize that she could not receive in person because she was a woman.

![Sophie Germain](../images/sophie-germain-66o.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Sophie Germain, and how does her mathematical work connect to the functions and graphs we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Sophie Germain"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Germain's results on elasticity — using the language of functions and graphs you just learned.
- Ask it about Gauss's letter to Germain after he discovered she was a woman.

What changes? What gets better? What gets worse?
