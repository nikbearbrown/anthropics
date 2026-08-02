# Chapter 6 — Applications of Integration


## TL;DR

- What to do once you know how to add up infinitely many infinitely thin things.
- The chapter moves through A single question, Area between curves, Volume: slicing into disks, Volume: slicing into shells, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*What to do once you know how to add up infinitely many infinitely thin things.*

---

## A single question

Here is the question this chapter answers: if you can integrate, what can you actually compute?

The answer turns out to be an embarrassingly long list. Area. Volume. The length of a curve. The work done by a force that changes as you push. The energy required to lift every drop of water out of a tank. The center of mass of an irregular object. The expected value of a continuous random variable. All of these are integrals. The chapter is about learning to see them that way.

But rather than start with the list, let's start with a single object that forces all the ideas to the surface: a wine bottle.

A wine bottle is not a cylinder. It has a flared base, a curved shoulder, a tapering neck. You cannot compute its interior volume with $\pi r^2 h$. There is no single radius. There is a *profile* — a curve $r(y)$ that gives the bottle's radius at each height $y$. To find the volume, you have to add up the contributions from every horizontal slice of the bottle, from the bottom to the top.

Each horizontal slice is approximately a disk. A thin disk at height $y$ has radius $r(y)$, thickness $dy$, and volume $\pi [r(y)]^2 \, dy$. Add them all up — that is, integrate — and you have the total interior volume:

$$V = \int_a^b \pi [r(y)]^2 \, dy$$

<!-- → INFOGRAPHIC: cutaway diagram of a wine bottle with a horizontal slice at height y highlighted — one thin disk pulled out to the side showing its radius r(y) and thickness dy labeled, with the volume element π[r(y)]²dy written next to it. The full stack of disks should be visible inside the bottle silhouette, conveying the accumulation idea before any formula is written. -->

This is not a special formula for bottles. It is the general pattern for every application in this chapter: slice the quantity into infinitesimal pieces, identify each piece's contribution, integrate. The integral is always a sum. What changes from problem to problem is what you're summing and what each piece looks like. Learning that pattern — not memorizing formulas — is what this chapter is for.

---

## Area between curves

The simplest case. Two curves, $y = f(x)$ above and $y = g(x)$ below, from $x = a$ to $x = b$. At each position $x$, the vertical gap between them is $f(x) - g(x)$. The area of a thin strip at position $x$ with width $dx$ is $[f(x) - g(x)] \, dx$. Add them up:

$$A = \int_a^b [f(x) - g(x)] \, dx$$

<!-- → IMAGE: graph of two curves f(x) and g(x) with the region between them shaded, one thin vertical strip of width dx highlighted at an arbitrary x, with the height of the strip labeled f(x)−g(x). The strip should be visually distinct (a different shade) to isolate the integrand geometry from the accumulated area. -->

Let me work one example through. Find the area enclosed by $y = x^2$ and $y = x + 2$.

First, where do they meet? Set $x^2 = x + 2$, which rearranges to $x^2 - x - 2 = 0$, or $(x-2)(x+1) = 0$. They intersect at $x = -1$ and $x = 2$.

On that interval, which is on top? At $x = 0$: $x^2 = 0$ and $x + 2 = 2$. The line is above the parabola.

$$A = \int_{-1}^{2} [(x+2) - x^2] \, dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2}$$

$$= \left(2 + 4 - \frac{8}{3}\right) - \left(\frac{1}{2} - 2 + \frac{1}{3}\right) = \frac{10}{3} + \frac{7}{6} = \frac{9}{2}$$

The enclosed area is $9/2$ square units.

One subtlety: if the curves cross within the interval you're integrating over, the formula breaks down. Where $f(x) - g(x)$ is negative, the integral subtracts area instead of adding it. The fix is to split the integral at every crossing point and always integrate the *upper* curve minus the *lower* curve on each sub-interval. That ensures you're summing positive widths.

---

## Volume: slicing into disks

Spin the curve $y = f(x)$, from $x = a$ to $x = b$, around the $x$-axis. The swept solid has circular cross-sections perpendicular to the axis. At position $x$, the cross-section is a circle of radius $f(x)$, with area $\pi [f(x)]^2$. A thin slab of thickness $dx$ has volume $\pi [f(x)]^2 \, dx$. The total volume:

$$V = \int_a^b \pi [f(x)]^2 \, dx$$

This is the *disk method*. It is the wine-bottle formula from the opening, written in $x$ instead of $y$.

A worked example. Rotate $y = \sqrt{x}$ from $x = 0$ to $x = 4$ around the $x$-axis. The cross-sectional radius at position $x$ is $\sqrt{x}$, so $[f(x)]^2 = x$.

$$V = \int_0^4 \pi x \, dx = \pi \cdot \frac{x^2}{2} \bigg|_0^4 = 8\pi$$

The resulting solid is a paraboloid. Its volume is exactly $8\pi$ cubic units.

<!-- → IMAGE: the paraboloid generated by rotating y=√x around the x-axis from x=0 to x=4, rendered as a 3D solid with a single disk cross-section at an arbitrary x drawn in — showing the circular face of radius √x, with the thickness dx labeled. The solid should be translucent enough that the disk is visible inside it. -->

When the rotation produces a solid with a hole through the middle — say, rotating the region *between* two curves around an axis — each cross-section is a washer rather than a disk: a full circle with a smaller circle removed. The area of that washer is $\pi(R^2 - r^2)$, where $R$ is the outer radius and $r$ is the inner radius. The volume integral becomes:

$$V = \int_a^b \pi[R(x)^2 - r(x)^2] \, dx$$

The reasoning is identical to the disk method; the geometry of the cross-section is slightly richer.

---

## Volume: slicing into shells

The disk method slices perpendicular to the axis. There is a second approach — *shells* — that slices parallel to the axis.

Take the region under $y = f(x)$ from $x = a$ to $x = b$ and rotate it around the $y$-axis. A thin vertical strip at position $x$ with width $dx$ sweeps out a cylindrical shell. The shell has radius $x$ (its distance from the axis), height $f(x)$, and thickness $dx$. The volume of a thin cylindrical shell is approximately its circumference times its height times its thickness:

$$dV = 2\pi x \cdot f(x) \cdot dx$$

Add them up:

$$V = \int_a^b 2\pi x \, f(x) \, dx$$

A worked example. Rotate $y = x^2$ from $x = 0$ to $x = 2$ around the $y$-axis.

$$V = \int_0^2 2\pi x \cdot x^2 \, dx = 2\pi \int_0^2 x^3 \, dx = 2\pi \cdot 4 = 8\pi$$

The shell method and the disk method are two different decompositions of the same solid. Neither is more correct; they're different ways of slicing. The useful heuristic: if the axis of rotation is *perpendicular* to the natural slicing direction, use disks. If the axis is *parallel* to it, use shells. For some problems one method produces a clean integral and the other produces an algebraic mess. With experience you develop intuition for which to reach for.

<!-- → INFOGRAPHIC: two side-by-side diagrams of the same solid of revolution — left diagram shows the disk decomposition (horizontal slices, circular faces), right shows the shell decomposition (vertical strips, cylindrical shells). Each should label the relevant dimensions: radius and thickness for disks; radius, height, and thickness for shells. Caption: "same solid, two ways of slicing — the choice of method changes the integrand, not the answer." -->

---

## Arc length

How long is a curve?

If the curve were a straight line, the answer would be easy: the distance formula. For a general curve $y = f(x)$, the idea is the same as always — slice, identify, integrate. Break the curve into tiny pieces. Each piece, when it's short enough, is approximately a straight line segment. The length of the segment connecting $(x, f(x))$ to $(x + dx, f(x + dx))$ is given by the Pythagorean theorem:

$$d\ell = \sqrt{(dx)^2 + (dy)^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx = \sqrt{1 + [f'(x)]^2} \, dx$$

<!-- → IMAGE: a smooth curve with one small segment magnified into an inset — the inset shows the right triangle with legs dx and dy, hypotenuse dℓ, and the label √(dx²+dy²) on the hypotenuse. This makes the Pythagorean origin of the arc length integrand visual rather than purely algebraic. -->

Add them up over $[a, b]$:

$$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$

One worked example where the integral simplifies nicely. Find the length of $y = \frac{2}{3} x^{3/2}$ from $x = 0$ to $x = 3$.

$f'(x) = x^{1/2}$, so $[f'(x)]^2 = x$, and the integrand is $\sqrt{1 + x}$.

$$L = \int_0^3 \sqrt{1 + x} \, dx = \frac{2}{3}(1 + x)^{3/2} \bigg|_0^3 = \frac{2}{3}(8 - 1) = \frac{14}{3}$$

This case cooperated. Most don't. The arc length integrand $\sqrt{1 + [f'(x)]^2}$ rarely simplifies to something elementary. For a circle, a parabola, an ellipse — most familiar curves — the arc length integral cannot be expressed in closed form. It has to be evaluated numerically. The formula is always the same; the integration is usually harder.

This is not a failure of the formula. It is a fact about the geometry of curves. Arc length is genuinely hard to compute, and the integral reflects that honestly.

---

## Work done by a variable force

In introductory physics, work equals force times distance: $W = F \cdot d$. This assumes the force is constant. It never is, in practice — at least not over anything interesting.

When the force $F(x)$ varies with position, the work done in moving from $x = a$ to $x = b$ is, once again, the integral of the infinitesimal contributions. Each thin displacement $dx$ requires work $F(x) \, dx$. The total:

$$W = \int_a^b F(x) \, dx$$

The canonical example is a spring. Hooke's law says that the force required to stretch a spring by displacement $x$ from its natural length is $F(x) = kx$, where $k$ is the spring constant. To stretch the spring from its natural length to a distance $d$:

$$W = \int_0^d kx \, dx = \frac{k d^2}{2}$$

For $k = 4$ N/m and $d = 0.5$ m, the work is 0.5 joules. That energy is stored as potential energy in the spring — the very energy released when you let go.

The spring is clean because the force law is simple. More interesting: pumping water.

---

## Pumping water out of a tank

Suppose a cylindrical tank of radius $r$ and height $h$ is filled with water, and you want to pump all the water out over the top rim. How much work does that require?

The difficulty is that different layers of water sit at different depths. Water near the top needs to travel almost no distance; water near the bottom has to travel the full height of the tank. The work depends on where each layer sits.

Slice the water column into horizontal layers of thickness $dy$ at height $y$ above the bottom. Each layer:

- Has volume $\pi r^2 \, dy$ (for a cylinder, the cross-section is constant).
- Has mass $\rho \pi r^2 \, dy$, where $\rho = 1000$ kg/m³ is the density of water.
- Has weight $\rho g \pi r^2 \, dy$, the downward force it exerts (with $g \approx 9.8$ m/s²).
- Must be lifted a distance $h - y$ to reach the top rim.
- Contributes work $(h - y) \cdot \rho g \pi r^2 \, dy$.

Integrate over the full depth of the tank, from $y = 0$ to $y = h$:

$$W = \int_0^h \rho g \pi r^2 (h - y) \, dy = \rho g \pi r^2 \left[hy - \frac{y^2}{2}\right]_0^h = \rho g \pi r^2 \cdot \frac{h^2}{2}$$

<!-- → INFOGRAPHIC: vertical cross-section of a cylindrical tank with water filled to height h — one horizontal layer at height y highlighted with its thickness dy labeled, and an arrow showing the lift distance (h−y) from the layer to the top rim. The four quantities annotated on the diagram: volume πr²dy, mass ρπr²dy, weight ρgπr²dy, and work contribution (h−y)·ρgπr²dy. Makes the four-step physical reasoning visual. -->

For a non-cylindrical tank — a cone, a sphere, a more exotic shape — the cross-sectional area $A(y)$ varies with height. The formula generalizes to:

$$W = \int_0^h \rho g \, A(y) \, (h - y) \, dy$$

The structure is always the same: weight of layer times distance traveled, integrated. The geometry of the tank goes into $A(y)$.

---

## The wine bottle, computed

Return to the opening. The bottle has a profile $r(y)$ that varies with height. Take a simplified model: the body (from $y = 0$ to $y = 20$ cm) has constant radius 4 cm; the shoulder (from $y = 20$ to $y = 25$ cm) tapers linearly from 4 cm to 1.5 cm; the neck (from $y = 25$ to $y = 30$ cm) has constant radius 1.5 cm.

The integral $V = \int_0^{30} \pi [r(y)]^2 \, dy$ splits into three pieces at the transitions in the profile.

The *body* contributes $\pi (4)^2 \cdot 20 = 320\pi \approx 1005$ cm³.

The *neck* contributes $\pi (1.5)^2 \cdot 5 = 11.25\pi \approx 35$ cm³.

The *shoulder* requires a little more work. The radius decreases linearly from 4 to 1.5 over 5 cm, so $r(y) = 4 - 0.5(y - 20)$ for $y \in [20, 25]$. Substituting $u = y - 20$:

$$\int_{20}^{25} \pi [4 - 0.5(y - 20)]^2 \, dy = \pi \int_0^5 (4 - 0.5u)^2 \, du$$

$$= \pi \int_0^5 (16 - 4u + 0.25u^2) \, du = \pi \left[16u - 2u^2 + \frac{u^3}{12}\right]_0^5 \approx 40.4\pi \approx 127 \text{ cm}^3$$

Total: $1005 + 127 + 35 \approx 1167$ cm³, or about 1.17 liters. A standard wine bottle holds 750 mL, so the model overestimates by about a third — not surprising, since a real bottle narrows appreciably even in the body. Refine the profile to match the actual shape and the integral produces the actual volume to whatever precision the measurement supports.

<!-- → CHART: bar chart with three segments stacked vertically — body (1005 cm³), shoulder (127 cm³), neck (35 cm³) — with the 750 mL standard bottle volume shown as a horizontal reference line. Annotates the overestimate visually and shows the relative contribution of each section to the total. A second, thinner bar showing a refined cylindrical model alongside for comparison would be effective. -->

The point isn't the specific number. It's that the same method — slice, identify, integrate — computes the volume of any shape that can be described by a profile function. The structural pattern doesn't change; only the integrand does.

---

## The pattern underneath everything

Step back. Every computation in this chapter followed the same sequence of moves.

*Identify what accumulates.* Area, volume, length, work — each is a quantity that builds up continuously as you move along an axis.

*Slice into infinitesimal pieces.* At each position, there is a thin slice — a strip, a disk, a shell, a layer of water — that contributes a small amount to the total.

*Write the contribution of one piece.* This is the integrand. Getting it right requires understanding the geometry of the slice — its dimensions, its weight, its distance from some reference.

*Integrate.* Add up all the contributions over the relevant range.

<!-- → INFOGRAPHIC: four-panel flow diagram — (1) "Identify what accumulates" with icon of a shaded region, (2) "Slice into pieces" with a single thin strip extracted, (3) "Write one piece's contribution" with the integrand expression labeled, (4) "Integrate" with the integral symbol and limits. An arrow connects each panel to the next. At the bottom, five rows showing how each application in the chapter maps to this pattern: area, disk volume, shell volume, arc length, work. -->

The Fundamental Theorem of Calculus, which we developed in Chapter 5, is what makes step four tractable: it converts the limit of a sum into an antiderivative evaluated at two points. Without it, every problem would require evaluating a Riemann sum directly. With it, the accumulated quantity reduces to finding an antiderivative — the reverse of differentiation.

This is also why integration is harder than differentiation. Differentiation has rules: given any elementary function, you can differentiate it by applying the chain rule, product rule, and a small table of basic derivatives. Integration has no such systematic procedure. Some antiderivatives exist in closed form; many don't. The arc length of a parabola, the volume under a Gaussian curve, the period of a nonlinear pendulum — these integrals don't have elementary antiderivatives. They must be evaluated numerically.

In practice, numerical integration is what engineers and scientists actually use. Software libraries handle the computation; the human's job is to set up the integral correctly — to identify what accumulates, write the integrand, specify the limits. The setup requires understanding. The computation is delegated.

---

## What's waiting beyond this chapter

The slice-identify-integrate pattern extends far past the applications here. Continuous probability lives entirely in integration: the probability that a random variable falls in an interval is the integral of its density function over that interval; the expected value is the integral of the variable weighted by the density. The integral is not an analogy — it *is* the probability.

Center of mass is another integral: the balance point of a continuous distribution of mass is the weighted average position, computed as a ratio of integrals. Hydrostatic pressure on a dam face — the force that the water column exerts as depth and hence pressure increases — is an integral of pressure times area over depth. Surface area of a solid of revolution, the area of the skin swept out when a curve spins around an axis, follows the same pattern as arc length, with an extra $2\pi f(x)$ factor for the circumference at each height.

And in more advanced settings — multivariable calculus, differential equations, physics, engineering, statistics — integration in multiple dimensions handles the volumes of shapes that can't be swept out by a single curve, the flow of fluid through a surface, the probability over a joint distribution. The operations are more elaborate; the pattern of slicing and accumulating is structurally identical.

---

## Summary

Integration is the mathematics of accumulation. Differentiation asks how fast something is changing right now; integration asks how much has accumulated.

The formulas in this chapter — area between curves, volume by disks or shells, arc length, work, pumping — are not separate things to memorize. They are all instances of one procedure: identify the infinitesimal piece, write its contribution as an integrand, integrate over the range.

*Area between curves*: integrate the vertical gap $f(x) - g(x)$ over the interval, upper curve minus lower.

*Volume by disks*: $\pi$ times the radius squared, integrated — the area of the circular cross-section times the thickness.

*Volume by shells*: $2\pi$ times the radius times the height, integrated — the circumference times the height times the thickness of the shell.

*Arc length*: $\sqrt{1 + [f'(x)]^2}$, integrated — the Pythagorean length of each infinitesimal segment.

*Work*: force times displacement, integrated — or, for pumping, weight of layer times distance traveled, integrated.

The trade-off running through all of it: the method is universal, but the integrals it produces are often hard. Closed-form antiderivatives exist only for the problems that were designed to have them. Real problems — real bottle profiles, real force fields, real probability distributions — almost always require numerical evaluation. The integral is still the right setup. The computation just needs a computer.

The single most important idea: every quantity that accumulates continuously is an integral, and every integral is a limit of sums. The Fundamental Theorem turns those sums into antiderivatives. The applications are just places where that machinery has work to do.

---

## Exercises

### Warm-Up

1. Find the area between $y = x$ and $y = x^2$ from $x = 0$ to $x = 1$. Which curve is on top? Set up the integrand before evaluating.

2. Find the volume of the solid generated by rotating $y = x$ from $x = 0$ to $x = 2$ around the $x$-axis using the disk method.

3. A spring with constant $k = 6$ N/m is stretched from its natural length to a displacement of 0.4 m. Compute the work done.

### Application

4. Find the area enclosed by $y = \sin x$ and $y = \cos x$ between their first two intersections in $[0, \pi]$. Identify where the curves cross, which is on top in each sub-interval, and split the integral accordingly.

5. The region under $y = x^2$ from $x = 0$ to $x = 1$ is rotated around the $y$-axis. Compute the volume using the shell method. Then set up — but do not evaluate — the equivalent disk method integral in $y$. Which setup is cleaner, and why?

6. Find the arc length of $y = \frac{1}{3}(x^2 + 2)^{3/2}$ from $x = 0$ to $x = 3$. Compute $f'(x)$ first, simplify $1 + [f'(x)]^2$, and check whether the result is a perfect square before integrating.

### Synthesis

7. A cylindrical tank of radius 2 m and height 4 m is filled with water ($\rho = 1000$ kg/m³, $g = 9.8$ m/s²). Compute the work to pump all the water out over the top rim. Set up the layer-by-layer integral explicitly — volume of layer, weight of layer, distance traveled — before combining.

8. A conical tank (vertex down) has height 6 m and top radius 3 m, and is filled with water. The cross-sectional radius at height $y$ above the vertex is $r(y) = y/2$. Compute the work to pump all the water out the top. Compare with a cylindrical tank of the same height and top radius — which requires more work, and why does the geometry explain the answer?

### Challenge

9. The profile of a vase is given by $r(y) = 2 + \sin(\pi y / 10)$ for $y \in [0, 10]$ cm, where $r$ is in centimeters. Write the integral for the interior volume and evaluate it. Does the sinusoidal bulge produce a noticeably different volume from a straight cylinder of the same height and average radius? Compute both and compare.

10. The arc length formula $L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$ looks like the Pythagorean theorem applied to each infinitesimal piece of the curve. Derive it from scratch: start from the length of the chord connecting $(x, f(x))$ to $(x + \Delta x, f(x + \Delta x))$, apply the Mean Value Theorem to relate $\Delta y$ to $f'$, and take the limit as $\Delta x \to 0$. What smoothness condition on $f'$ is required for the argument to go through, and what goes wrong at a corner?

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a collaborative thinking partner — asking it to check your reasoning, generate similar problems, or explain a step you're stuck on. The goal is to think alongside the tool, not to have the tool think for you.

**Exercise 1.** Ask an LLM to set up the integral for the area between $y = \sin x$ and $y = \cos x$ on $[0, \pi/2]$. Before reading its work, find the intersection point yourself ($x = \pi/4$), determine which function is on top in each sub-interval, and write the split integral. Compare. Did the LLM correctly handle the sign change at the intersection, or did it integrate $|\sin x - \cos x|$ as if it were always one expression?

**Exercise 2.** Give an LLM the region bounded by $y = x^2$ and $y = 4x$ rotated around the $x$-axis, and ask for the volume using both the disk method and the shell method. Solve it yourself first using disks (washer method, since the rotation produces a hollow solid). Then check the LLM's shell-method setup — is the radius the correct distance from the axis, or did it confuse "distance from axis" with "value of $x$"? The two methods must agree; if the LLM's two answers don't match, find the error.

**Exercise 3.** Ask an LLM to compute the arc length of $y = \cosh x$ from $x = 0$ to $x = 1$. The integrand simplifies cleanly because of the identity $1 + \sinh^2 x = \cosh^2 x$. Before seeing its work, derive this simplification yourself and integrate. Did the LLM apply the identity, or did it leave a complicated radical and try numerical integration? Both can land at the right answer; only one of them shows the structural reason it works.

**Exercise 4.** Set up — with the LLM's help — the work integral for pumping water out of a *hemispherical* tank of radius 3 m through the top. The horizontal cross-section at depth $y$ below the top is a disk of radius $\sqrt{9 - y^2}$. Walk the LLM through the layer-by-layer setup: volume of layer = $\pi(9 - y^2)\,dy$, weight = $1000g\pi(9 - y^2)\,dy$, distance lifted = $y$. Did it correctly identify the distance each layer travels, or did it confuse "depth below top" with "height above bottom"? Set up the integral and evaluate.

**Exercise 5.** Give an LLM the wine bottle from this chapter — interior radius profile $r(y)$ following the simplified three-piece model — and ask it to *recompute* the interior volume using Simpson's rule with 10 intervals. Compare to the analytical answer in the chapter. How close is the numerical approximation? Then ask: how many intervals would you need for Simpson's rule to be accurate to within 1 mL, and what does this say about the trade-off between analytical and numerical integration?

**Exercise 6.** Tell an LLM that you want to find the centroid of the region bounded by $y = x^2$, $y = 0$, and $x = 1$. The centroid coordinates require integrals weighted by $x$ and by $y$ separately. Set up both integrals yourself before showing them. Compute. Compare to the LLM's answer. Then ask the LLM: what does the centroid represent physically, and why is it not generally located on the curve $y = x^2$ itself? The geometric interpretation is the point of the calculation; the algebra is the means.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Émilie du Châtelet** translated Newton's *Principia* into French in the 1740s — adding her own commentary on the calculus of motion and area that introduced the concept of *kinetic energy* (mv²) into Continental physics. The work she did made Newton applicable to real engineering problems.

![Émilie du Châtelet](../images/emilie-du-chatelet-d8i.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Émilie du Châtelet, and how does her work translating and commenting on Newton's Principia connect to the applications of integration we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Émilie du Châtelet"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of du Châtelet's energy-from-motion arguments using the integration techniques you just learned.
- Add a constraint: "Answer as du Châtelet's introductory note to her 1746 translation of Newton."

What changes? What gets better? What gets worse?
