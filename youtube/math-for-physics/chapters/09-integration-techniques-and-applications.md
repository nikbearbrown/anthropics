# Integration Techniques and Applications

*Slice the object, write what each piece contributes, integrate — and the techniques are the derivative rules read backwards.*

---

## The cold open: why a hollow tube is harder to spin up than a solid rod

Take two objects of the same mass: a solid cylinder and a hollow tube of the same length and outer radius. Lay each on a ramp and let them roll. The solid one wins, every time. Grab a long wrench by its end and swing it; grab it by the middle and swing it; the end-grip is unmistakably harder to start and stop. Something about *where the mass sits* — not how much there is — governs how stubbornly an object resists being spun.

That something is the **moment of inertia**, the rotational analog of mass, and the source chapter on rotation gives its definition as an integral:

$$I = \int r^2\,dm.$$

But this is a strange-looking integral. The variable of integration is $dm$ — a little piece of *mass* — not a tidy $dx$. You cannot integrate "over mass" directly; you must first answer a modeling question the integral sign does not ask: *how is a little piece of mass related to a little piece of position?* For a rod, for a disk, for a planet, the answer differs, and getting it right is the whole game. The integration arithmetic that follows is mechanical. The setup is the physics.

This chapter does two things. It builds the two great techniques for *evaluating* integrals — substitution and integration by parts — and reveals them as the derivative rules of Chapter 6 run backwards. Then it builds the more important skill: **setting up** the integral for a physical accumulation, by slicing an object into infinitesimal pieces and writing what each piece contributes. We will compute a rod's and a disk's moment of inertia, a planet's gravitational binding energy, and the force a fluid exerts on a wall — all with the same move.

---

## The tool, named: two techniques and one setup skill

The Fundamental Theorem of the last chapter says integration undoes differentiation. So the two hardest differentiation rules, read backwards, become the two most useful integration techniques.

**Substitution** is the chain rule reversed. The chain rule says $\frac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$. Reading right to left:

$$\int f'(g(x))\,g'(x)\,dx = f(g(x)) + C, \quad\text{or, setting } u = g(x),\ du = g'(x)\,dx:\quad \int f'(u)\,du = f(u) + C.$$

In practice: spot an inside function $u = g(x)$ whose derivative also appears (up to a constant), rename, integrate in $u$, rename back.

**Integration by parts** is the product rule reversed. The product rule says $\frac{d}{dx}(uv) = u'v + uv'$. Integrate both sides and rearrange:

$$\int u\,dv = uv - \int v\,du.$$

The point is to *trade* an integral you cannot do, $\int u\,dv$, for one you can, $\int v\,du$. The trade only helps if the new integral is simpler, which is why the choice of which factor to call $u$ matters. A common rule of thumb (LIATE — prefer $u$ to be Logarithmic, then Inverse-trig, Algebraic, Trig, Exponential) helps, but it is a hint, not a law; the real test is whether your choice makes the remaining integral easier or worse.

**The setup skill** is the one the research says students actually fail at, so we make it explicit. To accumulate a physical quantity over a continuous body:

1. **Slice** the body into infinitesimal pieces of a shape that matches the symmetry.
2. **Write the contribution** of one slice in terms of a single integration variable — this is where $dm = \lambda\,dx$, $dm = \sigma\,dA$, $dF = p\,dA$ live.
3. **Integrate** over the variable, with limits that sweep the whole body.

The arithmetic is steps after the setup. The setup is where the thinking is.

---

## Development: substitution and parts, demonstrated

### Substitution on a clean case

Evaluate $\int 2x\,(x^2 + 1)^3\,dx$. The inside function is $u = x^2 + 1$, whose derivative $du = 2x\,dx$ is sitting right there. Substitute:

$$\int (x^2+1)^3\,(2x\,dx) = \int u^3\,du = \tfrac{1}{4}u^4 + C = \tfrac{1}{4}(x^2+1)^4 + C.$$

Check by differentiating: the chain rule gives $\tfrac{1}{4}\cdot 4(x^2+1)^3\cdot 2x = 2x(x^2+1)^3$. The technique is the chain rule walked backwards, exactly as advertised.

A bookkeeping warning for *definite* integrals: if you change the variable to $u$, you must also change the limits to $u$-values, or else back-substitute to $x$ before plugging in the original limits. Forgetting to convert the limits is the single most common substitution error.

### Integration by parts on a clean case

Evaluate $\int x\,e^{x}\,dx$. Neither factor's antiderivative simplifies the other on its own, but parts lets us trade. Choose $u = x$ (so $du = dx$) and $dv = e^x\,dx$ (so $v = e^x$). Then

$$\int x\,e^x\,dx = uv - \int v\,du = x e^x - \int e^x\,dx = x e^x - e^x + C.$$

The trade worked: the new integral $\int e^x\,dx$ is trivial, where the original was not. Had we chosen the other way ($u = e^x$, $dv = x\,dx$), the remaining integral $\int \tfrac{1}{2}x^2 e^x\,dx$ would have been *worse* — a higher power of $x$. Recognizing a bad trade and restarting is part of the skill.

---

## Development: the distribution integral — slicing a body

Now the setup skill, on the moment of inertia $I = \int r^2\,dm$. The problem is that $dm$ is not an integration variable; we must express it through one.

### A uniform rod about its center

A rod of mass $M$, length $L$, lies along the $x$-axis from $-L/2$ to $+L/2$, rotating about its center. **Slice** it into segments of width $dx$ at position $x$. Each segment is at distance $r = |x|$ from the axis, so $r^2 = x^2$. **Write the contribution:** the rod's mass is spread uniformly, so the *linear mass density* is $\lambda = M/L$ (mass per length), and a slice of width $dx$ has mass

$$dm = \lambda\,dx = \frac{M}{L}\,dx.$$

That is the crucial step — the bridge from $dm$ to $dx$. Now the integral has a single variable. **Integrate** over the whole rod:

$$I = \int r^2\,dm = \int_{-L/2}^{L/2} x^2\,\frac{M}{L}\,dx = \frac{M}{L}\int_{-L/2}^{L/2} x^2\,dx = \frac{M}{L}\left[\frac{x^3}{3}\right]_{-L/2}^{L/2}.$$

Evaluate: $\left(\tfrac{(L/2)^3}{3}\right) - \left(\tfrac{(-L/2)^3}{3}\right) = \tfrac{2}{3}\cdot\tfrac{L^3}{8} = \tfrac{L^3}{12}$. So

$$I_{\text{rod, center}} = \frac{M}{L}\cdot\frac{L^3}{12} = \frac{1}{12}ML^2.$$

### A uniform disk about its axis

A disk of mass $M$, radius $R$, spins about its central axis. Here the wrong slice — vertical strips — would be a nightmare. The right slice respects the circular symmetry: **slice into thin rings.** A ring at radius $r$ with thickness $dr$ has circumference $2\pi r$, so its area is $dA = 2\pi r\,dr$. The disk's *area mass density* is $\sigma = M/(\pi R^2)$, so the ring's mass is

$$dm = \sigma\,dA = \frac{M}{\pi R^2}\cdot 2\pi r\,dr = \frac{2M}{R^2}\,r\,dr.$$

Every point on the ring is at the same distance $r$ from the axis, so $r^2$ is just $r^2$. **Integrate** from the center out to the rim:

$$I = \int_0^R r^2\,dm = \int_0^R r^2\cdot\frac{2M}{R^2}\,r\,dr = \frac{2M}{R^2}\int_0^R r^3\,dr = \frac{2M}{R^2}\left[\frac{r^4}{4}\right]_0^R = \frac{2M}{R^2}\cdot\frac{R^4}{4}.$$

$$I_{\text{disk}} = \frac{1}{2}MR^2.$$

Notice the disk's $\tfrac{1}{2}MR^2$ is larger than the same-radius solid would give if more mass sat near the axis, and smaller than a hoop's $MR^2$, where *all* the mass sits at the rim. That is the cold open quantified: the moment of inertia depends on *where the mass is*, and the integral, weighting each sliver by $r^2$, is precisely the bookkeeping of that. Choosing the ring (not the strip) as the slice was the modeling judgment; the rest was the power rule.

![A disk of radius R sliced into thin concentric rings; one highlighted ring at radius r of thickness dr has circumference 2πr, so dm = σ·2πr dr, and integrating r²dm from center to rim gives I = ½MR².](images/09-integration-techniques-and-applications-fig-01.png)
*Figure 9.1 — The setup step: choosing a ring slice and writing dm = σ·2πr dr is the load-bearing decision; the integral is then a one-line power rule.*

---

## Development: the line integral and gravitational potential energy

A force that varies along a path accumulates work as a **line integral**, $W = \int \vec{F}\cdot d\vec{r}$ (built in the work chapter). Potential energy is defined as the negative of that accumulated work,

$$\Delta U = -\int_{r_1}^{r_2}\vec{F}\cdot d\vec{r}.$$

Apply it to Newton's gravity, $\vec{F} = -\dfrac{GMm}{r^2}\hat{r}$ — attractive, pointing inward, hence the minus sign, falling off as a power law with exponent $-2$. Moving radially, $\vec{F}\cdot d\vec{r} = -\dfrac{GMm}{r^2}\,dr$, so

$$\Delta U = -\int_{r_1}^{r_2}\left(-\frac{GMm}{r^2}\right)dr = GMm\int_{r_1}^{r_2}\frac{dr}{r^2}.$$

The integrand $r^{-2}$ has antiderivative $-r^{-1}$ (power rule backwards, exponent $-2 \to -1$):

$$\Delta U = GMm\left[-\frac{1}{r}\right]_{r_1}^{r_2} = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right).$$

Choose the reference $U = 0$ at infinity ($r_1 \to \infty$, where $1/r_1 \to 0$), and write the potential energy at any distance $r$:

$$\boxed{\,U(r) = -\frac{GMm}{r}\,.}$$

The sign carries the physics: $U$ is *negative* everywhere finite, rising toward zero as $r\to\infty$. A bound pair sits in an energy well; you must do positive work to pull them apart. The whole result lives in the limits of integration (from infinity) and the sign convention — exactly the places the source chapter warns students stumble. From here, setting kinetic plus potential energy to zero at the surface, $\tfrac{1}{2}mv_{\text{esc}}^2 - \tfrac{GMm}{R} = 0$, gives the **escape velocity** $v_{\text{esc}} = \sqrt{2GM/R}$ — independent of the escaping object's mass, since $m$ cancels.

---

## Worked examples

### Example 1 — Hydrostatic force on a dam

A rectangular dam of width $w$ holds water to depth $h$. Pressure at depth $y$ is $p = \rho g y$ (the hydrostatic law from the fluids source chapter, here taking $y$ downward from the surface with the surface at atmospheric pressure subtracted out). Pressure *varies with depth*, so the total force is an accumulation — set it up by slicing. **Slice** the wetted face into horizontal strips at depth $y$, height $dy$, width $w$: area $dA = w\,dy$. **Write the contribution** of one strip: force is pressure times area,

$$dF = p\,dA = \rho g y \cdot w\,dy.$$

**Integrate** from the surface $y = 0$ to the bottom $y = h$:

$$F = \int_0^h \rho g w\,y\,dy = \rho g w\left[\frac{y^2}{2}\right]_0^h = \frac{1}{2}\rho g w\,h^2.$$

The force grows as the *square* of the depth — double the water depth and the wall feels four times the force — because both the pressure and the wetted area grow with depth. The setup (a horizontal strip whose contribution is $\rho g y\,w\,dy$) was the whole problem; the integral was a power-rule line.

![A dam holding water to depth h, with a triangular pressure profile p = ρgy growing linearly with depth; a horizontal strip of height dy contributes dF = ρgy·w dy, and integrating from surface to bottom gives F = ½ρgwh².](images/09-integration-techniques-and-applications-fig-02.png)
*Figure 9.2 — Pressure varies with depth, so the wall force is an accumulation of horizontal strips; the total grows as the square of the depth.*

### Example 2 — Center of mass of a non-uniform rod (substitution in disguise)

A rod from $x = 0$ to $x = L$ has density that increases along its length, $\lambda(x) = \lambda_0(1 + x/L)$. Its center of mass is the mass-weighted average position, $\bar{x} = \frac{1}{M}\int x\,dm$ with $dm = \lambda(x)\,dx$. First the total mass:

$$M = \int_0^L \lambda_0\left(1 + \frac{x}{L}\right)dx = \lambda_0\left[x + \frac{x^2}{2L}\right]_0^L = \lambda_0\left(L + \frac{L}{2}\right) = \frac{3}{2}\lambda_0 L.$$

Then the weighted position:

$$\int_0^L x\,\lambda_0\left(1 + \frac{x}{L}\right)dx = \lambda_0\left[\frac{x^2}{2} + \frac{x^3}{3L}\right]_0^L = \lambda_0\left(\frac{L^2}{2} + \frac{L^2}{3}\right) = \frac{5}{6}\lambda_0 L^2.$$

So $\bar{x} = \dfrac{\tfrac{5}{6}\lambda_0 L^2}{\tfrac{3}{2}\lambda_0 L} = \dfrac{5}{9}L \approx 0.56\,L$. The center of mass sits past the midpoint, pulled toward the denser end — exactly what the integral, weighting each sliver by both its position and its mass, should report.

### Example 3 — Integration by parts in a physical accumulation

Suppose a time-varying force does work and you must integrate $\int_0^{T} t\,\cos(t)\,dt$ (such forms appear in oscillation problems). Use parts with $u = t$, $dv = \cos t\,dt$, so $du = dt$, $v = \sin t$:

$$\int_0^T t\cos t\,dt = \big[t\sin t\big]_0^T - \int_0^T \sin t\,dt = T\sin T - \big[-\cos t\big]_0^T = T\sin T + \cos T - 1.$$

The trade replaced an unintegrable-by-inspection product with $\int\sin t\,dt$, which is immediate. Choosing $u = t$ (algebraic, demoted to a constant by one differentiation) over $dv = \cos t\,dt$ is exactly the judgment LIATE encodes — and you can see *why* it works: differentiating $t$ simplifies it, where differentiating $\cos t$ would not.

---

## Return to the cold open

The hollow tube is harder to spin up than the solid rod because moment of inertia is $I = \int r^2\,dm$ — every sliver of mass weighted by the *square* of its distance from the axis — and the tube keeps all its mass out at large $r$, where the $r^2$ weighting bites hardest. We made that precise by *slicing*: a rod into segments with $dm = \lambda\,dx$, giving $I = \tfrac{1}{12}ML^2$; a disk into rings with $dm = \sigma\,2\pi r\,dr$, giving $\tfrac{1}{2}MR^2$. In each case the integration arithmetic was a one-line power rule; the work was writing $dm$ in terms of the integration variable — the setup step the integral sign never asks for but always demands. The same move computed a planet's binding energy from $\int \vec{F}\cdot d\vec{r}$ and a dam's load from $\int p\,dA$. And the two techniques that evaluate such integrals — substitution and parts — are nothing more exotic than the chain rule and the product rule from Chapter 6, read backwards, which is the Fundamental Theorem keeping its promise that integration undoes differentiation.

---

## Where it generalizes

"Slice the thing into infinitesimal pieces, write what each piece contributes, integrate" is the single most reusable modeling move in all of applied mathematics, and it does not care whether the thing is a rotating wheel, a gravitating planet, or a wall of water. In statistics, the expected value of a quantity is $\int x\,f(x)\,dx$ — a center of mass of probability, the same integral as the non-uniform rod with density replaced by probability density. In electromagnetism, the field of a charge distribution is the accumulation of contributions from each $dq$, with $dq = \rho\,dV$ playing the exact role of $dm = \lambda\,dx$. In economics, a continuous stream of payments accumulates to a present value by integration. The techniques — substitution, parts — are the universal evaluators, and the setup skill is the universal modeler. What the math will not do is choose the slice. A symbolic engine evaluates $\int r^2\sigma\,2\pi r\,dr$ flawlessly, but it cannot decide to slice the disk into *rings* rather than strips, write $dm = \sigma\,2\pi r\,dr$, recognize that gravitational potential energy integrates from infinity with a minus sign, or supply a dam's width as a function of depth when the wall is not rectangular. Even the technique choice — substitution here, parts there — is a pattern-recognition judgment a solver can imitate but you must own to set the problem up at all. Integration is mechanical; deciding *what the integral is* is the physics, and that is yours.

---

## Exercises

1. **(Substitution.)** Evaluate (a) $\int 3x^2(x^3 + 5)^4\,dx$; (b) $\int_0^1 x\,e^{x^2}\,dx$. For the definite integral, convert the limits to the new variable and state both new limits.

2. **(Integration by parts.)** Evaluate $\int x\,\sin x\,dx$. State your choice of $u$ and $dv$, and explain in one sentence why the opposite choice would make the remaining integral worse.

3. **(Setting up $dm$.)** A thin rod of length $L$ has linear density $\lambda(x) = \lambda_0\,x/L$ (zero at one end, $\lambda_0$ at the other). Write $dm$ in terms of $dx$, then compute the rod's total mass $M$ by integration. (You are practicing only the setup-and-integrate step.)

4. **(Pressure force.)** A vertical rectangular window in the side of an aquarium is $2\ \text{m}$ wide and spans depths from $1\ \text{m}$ to $3\ \text{m}$ below the surface. Using $dF = \rho g y\,w\,dy$ with $\rho = 1000\ \text{kg/m}^3$, set up and evaluate the total force on the window. (Note the limits run from $y = 1$ to $y = 3$, not from $0$.)

5. **(Derivation.)** Derive the moment of inertia of a uniform disk of mass $M$ and radius $R$ about its central axis, $I = \tfrac{1}{2}MR^2$. Explain why the correct infinitesimal slice is a thin ring, write $dm$ in terms of $dr$ using the area density $\sigma = M/(\pi R^2)$, and carry out the integral $\int_0^R r^2\,dm$. State at which step the choice of slice (ring vs. strip) was the load-bearing modeling decision.

---

## Sources

- Gottfried Wilhelm Leibniz, "De Geometria Recondita," *Acta Eruditorum* (1686) and the product rule (1684) — integration by parts as the integrated product rule; substitution as the integrated chain rule. [verified — see factchecks/09-integration-techniques-and-applications-assertions.md] (original primary sources)
- Isaac Newton, *Principia* (1687), Book I — integrating contributions from infinitesimal mass elements for the gravitation of extended bodies; the gravitational potential energy integral. [verified — see factchecks/09-integration-techniques-and-applications-assertions.md] (original primary source)
- Christiaan Huygens, *Horologium Oscillatorium* (1673) — the first systematic moment-of-inertia (center-of-oscillation) computation; Leonhard Euler, *Theoria motus corporum solidorum* (1765) — the moment of inertia for rigid bodies and the term itself. [verified — Euler/Huygens priority drawn from secondary summaries, see factchecks/09-integration-techniques-and-applications-assertions.md and pantry] (original primary sources)
- Archimedes, *On the Equilibrium of Planes* (3rd c. BCE) — the law of the lever and the centroid, ancestor of the center-of-mass integral. [verified — see factchecks/09-integration-techniques-and-applications-assertions.md] (original primary source)
- Source chapters (this book's archive): "Fixed-Axis Rotation" — $I = \int r^2\,dm$ with the rod ($\tfrac{1}{12}ML^2$ about center, $\tfrac{1}{3}ML^2$ about end) and disk ($\tfrac{1}{2}MR^2$) derivations and the parallel-axis theorem; "Gravitation" — $U(r) = -GMm/r$ from $-\int\vec{F}\cdot d\vec{r}$ and escape velocity; "Potential Energy and Conservation of Energy" — spring PE $\tfrac{1}{2}kx^2$ and conservative-force definition $\Delta U = -W$; "Fluid Mechanics" — hydrostatic pressure $p = p_0 + \rho g h$.
- S. R. Jones, work on the integrand-construction (product) conception (2013, 2015); Thompson & Carlson accumulation research — the finding that students execute techniques but fail to construct the integrand $dm$/$dA$/$dV$. [verified — see factchecks/09-integration-techniques-and-applications-assertions.md]
