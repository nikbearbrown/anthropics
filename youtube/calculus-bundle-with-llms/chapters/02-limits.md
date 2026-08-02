# Chapter 2 — Limits
*Approaching Without Arriving.*

There is a speed you cannot reach.

Einstein showed this in 1905, and the proof is not philosophical — it is arithmetic. Take any object with mass $m_0$ at rest. Accelerate it. A stationary observer watching this object move at speed $v$ measures its mass as

$$m = \frac{m_0}{\sqrt{1 - \dfrac{v^2}{c^2}}}$$

where $c$ is the speed of light. Run the numbers. At ordinary speeds — even the 17,500 mph of the International Space Station — the ratio $v/c$ is so small that the denominator is essentially 1, and the moving mass is essentially the rest mass. Push harder. At half the speed of light, $v = 0.5c$, the denominator drops to $\sqrt{0.75} \approx 0.866$, and the moving mass is about 15 percent larger than at rest. At $v = 0.9c$, the mass is roughly 2.3 times the rest mass. At $0.99c$, about 7 times. At $0.999c$, about 22 times. At $0.9999c$, about 71 times.

The mass is growing. To accelerate the object further requires force proportional to its current mass, and the mass keeps rising as you push. More force, heavier object, more force needed — the cost of the next small increase in speed grows without bound as you approach $c$.

<!-- → [CHART: curve of relativistic mass ratio m/m₀ vs. v/c from 0 to 0.9999c — x-axis labeled as fraction of c, y-axis as mass multiple of m₀ — student should see the curve is nearly flat until ~0.7c, then bends sharply upward, with the vertical asymptote at v = c clearly visible but unreachable] -->

Now ask what the formula says at $v = c$ exactly. The denominator becomes $\sqrt{1 - 1} = \sqrt{0} = 0$. Division by zero. The formula gives no value. There is no answer at $v = c$ — not "infinity" as a number, not anything. The formula simply breaks.

And yet the behavior is perfectly clear. The mass doesn't hop discontinuously to some new value as you approach $c$. It climbs steadily, faster and faster, growing without bound. You can get arbitrarily close to the speed of light; each step closer costs more than the last. What the formula is doing near $v = c$ — approaching, without arriving — has a name.

It's called a *limit*.

---

## What a limit actually is

Here is the cleanest possible example. Consider the function

$$f(x) = \frac{x^2 - 4}{x - 2}$$

At $x = 2$: numerator is $0$, denominator is $0$, form is $0/0$, value is undefined. The function has a hole at $x = 2$.

But ask a different question. Not "what is $f(2)$?" but "what does $f(x)$ approach as $x$ approaches $2$?" Compute a few values. At $x = 1.9$: $f(1.9) = (3.61 - 4)/(-0.1) = 3.9$. At $x = 1.99$: $f(1.99) = 3.99$. At $x = 1.999$: $3.999$. From the other side: $x = 2.1$ gives $4.1$, $x = 2.01$ gives $4.01$, $x = 2.001$ gives $4.001$.

The function is heading toward 4 from both directions, clearly, consistently, unstoppably. We write

$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = 4$$

<!-- → [IMAGE: graph of f(x) = (x²−4)/(x−2) — plot the line y = x+2 with an open circle (hollow dot) at the point (2, 4), emphasizing that the function is defined everywhere on the line except exactly at x = 2; label the hole and the limit value L = 4 separately so the student sees they are different objects] -->

The algebra confirms it. Factor the numerator: $x^2 - 4 = (x - 2)(x + 2)$. So

$$\frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x-2} = x + 2 \quad \text{for } x \neq 2$$

For any $x$ near 2 but not equal to 2, the function is just $x + 2$. As $x$ approaches 2, $x + 2$ approaches 4. The limit is 4. The fact that the function has no value at the point itself is irrelevant.

This is the first thing worth really absorbing: *a limit is not about what happens at a point*. It is about what happens near a point. The question "what is the limit at $x = a$?" and the question "what is the function value at $x = a$?" are different questions. Sometimes they have the same answer. Sometimes they don't. Sometimes one exists and the other doesn't. Keeping them separate is the whole conceptual move.

---

## Why the concept had to be invented

Calculus was invented around 1670, more or less simultaneously by Newton and Leibniz. For the next century and a half, mathematicians used it brilliantly and somewhat guiltily — the results were right, but the foundations were not rigorous. Newton talked about "fluxions," quantities that were on their way to zero but hadn't gotten there. Bishop Berkeley famously mocked this as "the ghosts of departed quantities" — you can't have a thing that's gone away and also still there.

The trouble was that differentiation, the central operation of calculus, involves dividing by a quantity that eventually becomes zero. The average rate of change of $f$ over a small interval of width $h$ is $(f(x + h) - f(x))/h$. To get the instantaneous rate, you want $h$ to go to zero. But if $h = 0$, you've divided by zero and the expression is meaningless. If $h \neq 0$, you haven't actually reached the instantaneous rate.

What Newton and Leibniz were doing intuitively — and what Cauchy and Weierstrass pinned down precisely in the 1820s and 1860s — was taking a *limit*. The instantaneous rate of change is not a value the expression takes at $h = 0$. It is the value the expression approaches as $h$ approaches 0. The limit concept dissolves the paradox. "Approaching" and "equaling" are different things, and once you have a precise notion of approaching, you can do the mathematics without any ghosts.

Every definition in calculus — the derivative, the integral, the sum of an infinite series — is formulated as a limit. This chapter is not a detour before the real subject. It is the foundation the real subject is built on.

---

## When limits fail

A limit exists when the function approaches the same value from both sides. When it doesn't, things fall apart in one of several named ways.

The simplest failure: the two sides disagree. Consider the absolute-value function $f(x) = |x|/x$. For $x > 0$, this is $x/x = 1$. For $x < 0$, this is $-x/x = -1$. Approaching 0 from the right, the function heads toward $1$. Approaching from the left, it heads toward $-1$. There is no single value the function approaches at $0$. The two-sided limit does not exist. Each one-sided limit exists; they just don't match.

We write $\lim_{x \to 0^+} |x|/x = 1$ and $\lim_{x \to 0^-} |x|/x = -1$. The superscripts $+$ and $-$ mean "from the right" and "from the left." The two-sided limit $\lim_{x \to 0} |x|/x$ does not exist.

The second kind of failure: the function blows up. The rational function $1/x$ near $x = 0$: from the right, the values are $1, 10, 100, 1000, \ldots$ as $x = 1, 0.1, 0.01, 0.001, \ldots$ The function grows without bound. We write

$$\lim_{x \to 0^+} \frac{1}{x} = \infty$$

This notation is somewhat conventional. The limit does not "equal infinity" in the sense of taking a numerical value — infinity is not a number. The notation means the function grows without bound, and the $\infty$ symbol identifies *how* the limit fails.

The Einstein equation does exactly this. $\lim_{v \to c^-} m_0 / \sqrt{1 - v^2/c^2} = \infty$. The mass grows without bound as speed approaches the speed of light. The limit "doesn't exist" in the strict sense; in the practical sense, you know exactly what's happening.

The third kind of failure: oscillation. The function $\sin(1/x)$ near $x = 0$ oscillates infinitely often — as $x$ shrinks toward 0, the argument $1/x$ blows up, and the sine completes infinitely many full oscillations in any interval around 0, however small. The function doesn't settle on any value. Neither one-sided limit exists.

These three failure modes — jump, blow-up, oscillation — cover most of what you encounter. When a limit fails, the question to ask is: which kind of failure is this?

<!-- → [INFOGRAPHIC: three-panel side-by-side diagram of the three limit failure modes — panel 1: jump discontinuity (|x|/x), showing left and right arrows landing at different heights with gap labeled "sides disagree"; panel 2: blow-up (1/x), showing the curve shooting toward ±∞ with vertical asymptote labeled; panel 3: oscillation (sin(1/x)), showing increasingly rapid oscillation as x→0 with no settled value — each panel labels the failure type and the canonical example function] -->

---

## How to compute limits

The intuitive idea is fine for understanding. Computing by numerical experiment is fine for guessing. Neither is fast or reliable enough for actual mathematics. The limit laws turn computation into algebra.

The core laws say: if you know $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$, then limits pass through sums, differences, products, quotients (when $M \neq 0$), and powers exactly as you'd hope:

$$\lim_{x \to a}[f(x) + g(x)] = L + M, \quad \lim_{x \to a}[f(x) \cdot g(x)] = L \cdot M, \quad \lim_{x \to a}\frac{f(x)}{g(x)} = \frac{L}{M} \text{ (if } M \neq 0\text{)}$$

These laws, combined with the trivial cases $\lim_{x \to a} c = c$ (a constant stays constant) and $\lim_{x \to a} x = a$ (the identity function approaches its target), let you evaluate the limit of any polynomial or rational function by simply substituting the target value — as long as the denominator doesn't vanish there.

$$\lim_{x \to 3}(x^2 + 2x - 1) = 9 + 6 - 1 = 14$$

Done. The function is "nice" at $x = 3$, so the limit equals the value.

The interesting problems are where substitution gives $0/0$. That form is indeterminate — it doesn't mean the limit is 0, or 1, or doesn't exist. It means the limit laws aren't immediately applicable and you need to do something first.

**Factor and cancel.** This handles most polynomial cases. The example from the opening of this chapter: $\lim_{x \to 2}(x^2 - 4)/(x - 2)$. Substitution gives $0/0$. Factor: $(x^2 - 4) = (x-2)(x+2)$. Cancel the $(x-2)$ for $x \neq 2$. What remains: $\lim_{x \to 2}(x + 2) = 4$.

**Multiply by a conjugate.** For expressions involving square roots, the algebraic identity $(a - b)(a + b) = a^2 - b^2$ often clears the indeterminate form. Example:

$$\lim_{x \to 0}\frac{\sqrt{x + 1} - 1}{x}$$

Substitution gives $0/0$. Multiply numerator and denominator by $\sqrt{x+1}+1$:

$$\frac{\sqrt{x+1}-1}{x} \cdot \frac{\sqrt{x+1}+1}{\sqrt{x+1}+1} = \frac{(x+1) - 1}{x(\sqrt{x+1}+1)} = \frac{x}{x(\sqrt{x+1}+1)} = \frac{1}{\sqrt{x+1}+1}$$

Now substitute: $\lim_{x \to 0} 1/(\sqrt{x+1}+1) = 1/2$.

**The squeeze theorem.** When a function is trapped between two functions that converge on the same limit, it must share that limit. If $g(x) \leq f(x) \leq h(x)$ near $a$, and $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$, then $\lim_{x \to a} f(x) = L$.

The canonical application: $\lim_{x \to 0} x^2 \sin(1/x)$. The sine oscillates wildly — $\sin(1/x)$ doesn't have a limit at 0. But the whole expression is squeezed:

$$-x^2 \leq x^2 \sin(1/x) \leq x^2$$

Both bounds approach 0 as $x \to 0$. The expression in the middle, whatever it's doing, can't escape. Its limit is 0.

The squeeze theorem's elegance is that it never needs to look at the complicated function directly. You only need to bound it above and below by something tractable.

<!-- → [IMAGE: graph illustrating the squeeze theorem for x²sin(1/x) — plot the three curves y = x², y = −x², and y = x²sin(1/x) on the same axes near x = 0; shade the region between the two parabolas; label the "squeezed" function and the two bounding functions; mark the shared limit at (0, 0) with a dot — student should immediately see that the oscillating function cannot escape the narrowing envelope] -->

---

## Continuity

A function is *continuous at a point $a$* if three conditions hold simultaneously: $f(a)$ is defined; the limit $\lim_{x \to a} f(x)$ exists; and the limit equals $f(a)$. In practice: the function has no holes, jumps, or blowups at $a$.

All three conditions matter. You can have a function defined at $a$ but with a limit that doesn't exist (a jump). You can have a limit that exists but the function undefined at $a$ (a hole). You can have both defined and existent but disagreeing (a weird patch). Continuity is all three at once.

The failures have names.

A *removable discontinuity* is a hole: the limit exists, but the function value either doesn't exist or doesn't match. The function $f(x) = (x^2-4)/(x-2)$ has a removable discontinuity at $x = 2$. The limit is 4; the function is undefined. If you define $f(2) = 4$, the discontinuity vanishes — you "removed" it by patching in the right value.

A *jump discontinuity* is a genuine break: the one-sided limits exist but differ. No redefinition of the function value at the jump fixes it, because the left and right sides land in different places.

An *infinite discontinuity* is a blowup: the function grows without bound near the point. $1/x$ at $x = 0$.

<!-- → [INFOGRAPHIC: three-panel comparison of discontinuity types — panel 1: removable discontinuity showing a continuous-looking curve with a single open hole and a separate filled dot nearby (or none), labeled "limit exists, value missing or mismatched — patchable"; panel 2: jump discontinuity showing two separate curve segments ending at different heights at the same x-value, labeled "one-sided limits exist but disagree — not patchable"; panel 3: infinite discontinuity showing a vertical asymptote with curves shooting to ±∞, labeled "function unbounded — not patchable"; include a small example function under each panel] -->

Continuity is the condition that makes direct substitution valid as a limit-evaluation technique. When a function is continuous at $a$, $\lim_{x \to a} f(x) = f(a)$ by definition — that's what continuity means. So every time you substitute and compute a limit, you're implicitly invoking continuity. The first move in any limit problem — try substituting — is really asking whether the function is continuous at the target.

Polynomials are continuous everywhere. Rational functions are continuous wherever their denominator is nonzero. Trigonometric functions $\sin x$ and $\cos x$ are continuous everywhere. Exponential functions are continuous everywhere. These are the functions you work with most often, and on their natural domains they never have discontinuities.

---

## The Intermediate Value Theorem

Here is something a continuous function cannot do: jump from one height to another without passing through the heights in between.

The *Intermediate Value Theorem* makes this precise. If $f$ is continuous on the closed interval $[a, b]$, and $N$ is any number strictly between $f(a)$ and $f(b)$, then there is some $c$ in $[a, b]$ with $f(c) = N$.

The proof idea is topological — it follows from the completeness of the real line — but the content is geometric: a continuous graph can't get from height $f(a)$ to height $f(b)$ without drawing a connected curve, and a connected curve passes through every intermediate height.

<!-- → [IMAGE: IVT diagram — plot a smooth continuous curve from point (a, f(a)) to point (b, f(b)) on a closed interval; draw a horizontal dashed line at height N (strictly between the two endpoint values); mark the intersection point c on the x-axis with a vertical dotted line; label f(a), f(b), N, a, b, and c clearly — the visual argument is that the curve must cross the horizontal line at least once, and the diagram should make this feel obvious without needing words] -->

The practical consequence: if you can evaluate a function at two points and one value is negative and the other is positive, there must be a root somewhere between them. You don't know where. But it exists.

Example: show that $f(x) = x^3 - x - 1$ has a real root between $x = 1$ and $x = 2$.

$f(1) = 1 - 1 - 1 = -1$. Negative.
$f(2) = 8 - 2 - 1 = 5$. Positive.

$f$ is a polynomial, so it's continuous on $[1, 2]$. Since $f(1) < 0 < f(2)$, the IVT guarantees some $c$ in $[1, 2]$ with $f(c) = 0$. The root exists. Where exactly? You'd need numerical methods to pin it down. The IVT only guarantees existence — it says nothing about uniqueness or location.

This is the IVT's defining trade-off: it gives existence proofs for free, in exchange for telling you nothing about the solution itself. It's a blunt instrument that answers the question "is there a solution?" before you know how to find one.

---

## The precise definition

The intuitive definition of a limit — "the function approaches $L$ as $x$ approaches $a$" — is useful for reasoning and computing. It is not rigorous enough for proofs. The word "approaches" is doing a lot of work and carrying a lot of ambiguity.

Weierstrass gave the precise version. We say $\lim_{x \to a} f(x) = L$ if: for every $\epsilon > 0$, there exists $\delta > 0$ such that whenever $0 < |x - a| < \delta$, it follows that $|f(x) - L| < \epsilon$.

Parse the structure. $\epsilon$ is a tolerance on the output — how close to $L$ you want $f(x)$ to be. $\delta$ is a tolerance on the input — how close to $a$ you'll keep $x$. The statement says: whatever output tolerance your opponent demands, you can always find an input tolerance that delivers it. The limit equals $L$ if you can always win this game, no matter how tight the output tolerance.

The condition $0 < |x - a|$ is the "$x$ but not equal to $a$" clause — limits are about behavior near $a$, not at $a$.

<!-- → [IMAGE: ε-δ diagram — plot a generic smooth function f(x) near x = a; draw a horizontal band of width 2ε centered on L (the target output value) and a vertical band of width 2δ centered on a (the target input value); shade the region where both bands overlap; mark the point (a, L) with an open circle (since f(a) need not equal L); draw arrows showing that any x within distance δ of a (but not equal to a) maps to an f(x) within distance ε of L — the student should see the "tolerance game" visually: tighten ε, narrow δ to match] -->

A worked proof. Show $\lim_{x \to 3}(2x + 1) = 7$.

We need: for every $\epsilon > 0$, find $\delta > 0$ such that $0 < |x - 3| < \delta$ implies $|(2x+1) - 7| < \epsilon$.

Simplify the conclusion: $|(2x+1) - 7| = |2x - 6| = 2|x - 3|$.

So we need $2|x - 3| < \epsilon$, which means $|x - 3| < \epsilon/2$.

Choose $\delta = \epsilon/2$. Then if $0 < |x - 3| < \delta$, we have $|(2x+1) - 7| = 2|x-3| < 2 \cdot \epsilon/2 = \epsilon$. ✓

The recipe: manipulate the desired output inequality until it becomes a constraint on $|x - a|$, then read off the $\delta$. For linear functions this is one line of algebra. For more complicated functions it can require careful bounding — but the structure is always the same.

The $\epsilon$-$\delta$ definition is rarely used in introductory calculus practice. It becomes essential in real analysis, where you need to prove theorems about limits rather than compute them. Most of the working of this course happens at the intuitive level; the formal definition sits beneath it as the thing that justifies everything.

---

## Closing the loop

The Einstein equation is the full chapter in a single expression.

$$m(v) = \frac{m_0}{\sqrt{1 - v^2/c^2}}$$

The domain is the open interval $(-c, c)$ — for $|v| \geq c$, either the denominator vanishes or the radicand becomes negative, and neither has a physical or mathematical interpretation. On the open domain, the function is continuous: denominator is everywhere positive, and the composition of continuous operations preserves continuity.

At the right endpoint: $\lim_{v \to c^-} m(v) = \infty$. An infinite one-sided limit — the blowup kind of failure. The limit doesn't exist; the notation captures how it fails.

The IVT applies on any closed sub-interval. Between $v = 0$ (mass $= m_0$) and $v = 0.99c$ (mass $\approx 7.1 m_0$), the function is continuous and passes through every intermediate value. There is some $v$ at which the moving mass equals exactly $2m_0$, some other $v$ at which it equals $3m_0$, some other at $5m_0$. Each exists. Algebra finds them; IVT just guarantees they're there.

This is what limits actually are — not a detour, not an abstraction for its own sake. They're the language for describing behavior near a point without making a claim about the point itself. The derivative, the integral, infinite series — every central object in calculus is a limit. The machinery in this chapter is the machinery of all the chapters that follow.

The one idea to carry forward: you can approach a point without reaching it, and that approach can have a perfectly definite, computable value even if the function at the point is undefined, or wrong, or blowing up. The limit exists in the behavior near $a$, not in the behavior at $a$. Almost everything that makes calculus work depends on this distinction staying clear.

---

## LLM Exercises

The following exercises are designed for working interactively with an AI assistant. For each, the productive move is not to ask for the answer directly — it's to reason aloud, explain your thinking, and ask the AI to identify errors or push back on your reasoning.

1. **Reconstruct the Einstein limit from scratch.** Without looking at the chapter, walk the AI through why $\lim_{v \to c^-} m_0/\sqrt{1-v^2/c^2} = \infty$. Ask it to challenge every step. If it agrees too quickly, prompt it: "Is there anything imprecise or missing in what I said?"

2. **Construct your own $0/0$ example.** Build a rational function with a removable discontinuity at $x = 5$. Tell the AI what you built and why you expect the limit to exist. Ask it to verify your factoring and suggest a harder variant.

3. **The squeeze theorem, explained.** Explain the squeeze theorem to the AI as if it has never heard of it — motivate it from scratch, give the formal statement, and walk through the $x^2\sin(1/x)$ example. Ask the AI where your explanation would confuse a student seeing this for the first time.

4. **IVT as detective work.** Give the AI a function and an interval and ask it to confirm whether the IVT applies. Then ask it: what could go wrong if the continuity condition were dropped? Push until you can construct a discontinuous function that crosses zero on an interval but has no root — and explain why it doesn't contradict the IVT.

5. **Write an $\epsilon$-$\delta$ proof, narrated.** Attempt the proof that $\lim_{x \to 2}(5x - 3) = 7$. Write out every step with a sentence explaining what you're doing and why. Submit it to the AI and ask: "Where is the logic weakest? What would a grader mark down?"

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Augustin-Louis Cauchy** wrote *Cours d'Analyse* in 1821 — the textbook that put limits on rigorous footing for the first time, replacing Newton's and Leibniz's infinitesimals with an epsilon-delta framework. Modern calculus rigor begins with him.

**Run this:**

```
Who was Augustin-Louis Cauchy, and how does his rigorous treatment of limits connect to the limit concepts we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Augustin-Louis Cauchy"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one Cauchy epsilon-delta argument step by step on a specific limit.
- Ask it about Cauchy's prolific output — over 800 papers — and the political exile that pushed him to Turin and Prague.

What changes? What gets better? What gets worse?
