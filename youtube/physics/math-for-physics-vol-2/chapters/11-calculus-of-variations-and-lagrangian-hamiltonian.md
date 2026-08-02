# Calculus of Variations and the Lagrangian/Hamiltonian Formalism

*Functionals, the calculus of variations and the Euler–Lagrange equation, generalized coordinates, the Lagrangian and Hamiltonian, and conservation laws from symmetry — the variational mathematics behind least action, Fermat's principle, and analytical mechanics.*

---

## 1. Cold open: the curve of fastest descent

In June 1696 Johann Bernoulli threw down a challenge to "the sharpest mathematicians in the world." Take two points, one higher than the other but not directly above it, and connect them with a frictionless wire. Release a bead at the top. *Along which curve does the bead slide to the bottom in the least time?* A straight line is the shortest path — but is it the fastest? A steeper initial drop builds up speed early, which might win even though the path is longer.

This is the **brachistochrone** ("shortest-time") problem, and it broke open a new branch of mathematics. Newton, the story goes, received the challenge one evening, solved it overnight, and submitted his answer anonymously; Bernoulli recognized the author at once — "I know the lion by his paw." Leibniz, l'Hôpital, and both Bernoullis also solved it. The answer is neither the straight line nor the circular arc but a **cycloid** — the curve traced by a point on a rolling wheel.

Here is what makes the problem genuinely new, and why ordinary calculus is not enough. In Volume 1 you minimized a *function*: you had a quantity $f(x)$ depending on a number $x$, and you found the best $x$ by setting $f'(x) = 0$. But here the unknown is not a number — it is an entire *curve* $y(x)$, the whole shape of the wire. The thing being minimized, the descent time, depends on the *function*, not on any single point of it. We need a calculus that can take the derivative "with respect to a whole function" and set it to zero. That calculus — the **calculus of variations** — is the subject of this chapter, and its master equation, the Euler–Lagrange equation, turns out to generate not just the brachistochrone but Newton's laws, Snell's law of optics, and the conservation of energy and momentum. One mathematical idea, extremizing a functional, sits under an astonishing amount of physics.

---

## 2. The tool, named

Volume 1 taught you to extremize a function $f(x)$ by setting $df/dx = 0$. This chapter is the exact conceptual upgrade: extremizing a **functional** $S[y]$ — a machine that eats a whole function $y(x)$ and returns a single number — by setting its **variation** $\delta S = 0$. Where ordinary calculus asks "which *point* is the minimum?", the calculus of variations asks "which *path* is the minimum?"

This is the capstone of the methods sequence, and it is the most prerequisite-heavy chapter in the book: it leans on single-variable calculus (extremizing), ODEs (the Euler–Lagrange equation *is* an ODE to solve), multivariable calculus and the Legendre transform from Chapter 2 (to pass from the Lagrangian to the Hamiltonian), and integration by parts (the engine of the central derivation). We scope it tightly — derive the Euler–Lagrange equation, recover Newton's second law and one conservation law, state Hamilton's equations and Noether's theorem with one example each, and point onward. Going further (canonical transformations, Hamilton–Jacobi theory) turns a capstone into a course; that belongs to the advanced classical-mechanics book.

One honest word before we begin. The principle physicists actually use is the principle of **stationary** action — the action is an *extremum or a saddle point*, a place where the variation vanishes, not necessarily a minimum. "Least action" is the traditional name and is often literally true, but "stationary" is the honest word, and we will use it.

---

## 3. Development and derivation

### 3.1 Functionals and the variation

A **functional** assigns a number to a function. The brachistochrone's descent time is one:
$$
T[y] = \int_{x_1}^{x_2} \sqrt{\frac{1 + y'^2}{2gy}}\;dx,
$$
which depends on the whole curve $y(x)$ between fixed endpoints. The general functional we study has the form
$$
S[y] = \int_{x_1}^{x_2} L\big(y,\,y',\,x\big)\,dx,
$$
where $L$ is some given function of the path's value $y$, its slope $y' = dy/dx$, and the independent variable $x$. In mechanics $x$ will become time $t$, $y$ a coordinate $q$, and $L$ the Lagrangian.

To extremize, mimic ordinary calculus. There, you nudge $x$ to $x + dx$ and demand the first-order change in $f$ vanish. Here, nudge the *whole path*: let $y(x)$ be the true extremal path and consider a neighboring trial path
$$
\bar y(x) = y(x) + \varepsilon\,\eta(x),
$$
where $\varepsilon$ is a small number and $\eta(x)$ is an arbitrary smooth "shape of the wiggle." Because both paths must hit the *same fixed endpoints*, the wiggle must vanish there:
$$
\eta(x_1) = \eta(x_2) = 0.
$$
This fixed-endpoint condition is load-bearing — remember it; an entire term in the derivation lives or dies by it. The **variation** $\delta S$ is the first-order change in $S$ as $\varepsilon\to 0$, i.e. $\delta S = \varepsilon\,\frac{d}{d\varepsilon}S[y + \varepsilon\eta]\big|_{\varepsilon=0}$. Stationarity means $\delta S = 0$ for *every* allowed wiggle $\eta$.

![Two fixed endpoints joined by a solid red stationary path and a brown trial path that bows away in the middle but rejoins both endpoints, with the vertical gap labeled epsilon times eta of x and a note that the wiggle vanishes at both endpoints](images/11-calculus-of-variations-and-lagrangian-hamiltonian-fig-01.png)
*Figure 11.1 — The stationary path y(x) and a varied neighbor ȳ = y + εη(x): every trial path is pinned to the same endpoints, so η(x₁) = η(x₂) = 0 and the boundary term vanishes.*

### 3.2 The Euler–Lagrange equation

Compute $\frac{d}{d\varepsilon}S[y + \varepsilon\eta]$ at $\varepsilon = 0$. Differentiating under the integral and using the chain rule (note $\frac{\partial \bar y}{\partial\varepsilon} = \eta$ and $\frac{\partial \bar y'}{\partial\varepsilon} = \eta'$):
$$
\frac{dS}{d\varepsilon}\bigg|_{0} = \int_{x_1}^{x_2}\left(\frac{\partial L}{\partial y}\,\eta + \frac{\partial L}{\partial y'}\,\eta'\right)dx = 0.
$$
The first term already has the bare $\eta$ we want; the second has $\eta'$. To extract a common factor of $\eta$, **integrate the second term by parts**:
$$
\int_{x_1}^{x_2}\frac{\partial L}{\partial y'}\,\eta'\,dx = \underbrace{\left[\frac{\partial L}{\partial y'}\,\eta\right]_{x_1}^{x_2}}_{\text{boundary term}} - \int_{x_1}^{x_2}\frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)\eta\,dx.
$$
Here is where the fixed endpoints earn their keep: the boundary term contains $\eta(x_1)$ and $\eta(x_2)$, both **zero**, so it vanishes entirely. (Forget that $\eta$ vanishes at the ends and the whole derivation collapses — this is the single most common student error in the subject.) What remains is
$$
\int_{x_1}^{x_2}\left[\frac{\partial L}{\partial y} - \frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)\right]\eta(x)\,dx = 0.
$$
This must hold for *every* shape $\eta(x)$. The only way an integral of (something)$\times\eta$ can vanish for all $\eta$ is if the something is identically zero (the **fundamental lemma of the calculus of variations**). Therefore
$$
\boxed{\;\frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right) - \frac{\partial L}{\partial y} = 0.\;}
$$
This is the **Euler–Lagrange equation**. Any path that makes $S$ stationary must satisfy it. Euler found it geometrically in 1744; the 19-year-old Lagrange recast it in the clean analytic $\delta$-notation we just used, and in his 1788 *Mécanique analytique* rebuilt all of mechanics on it — boasting, famously, that his book contained not a single diagram.

### 3.3 Mechanics: the Lagrangian and the recovery of Newton

Now make the leap to physics. Replace $x\to t$ (time), $y \to q$ (a generalized coordinate), $y' \to \dot q$ (its time-derivative, the generalized velocity), and define the **action**
$$
S[q] = \int_{t_1}^{t_2} L(q, \dot q, t)\,dt,
$$
with the **Lagrangian** taken to be
$$
L = T - V \qquad(\text{kinetic minus potential energy}).
$$
**Hamilton's principle** asserts that the actual motion of a system is the one that makes $S$ stationary. The Euler–Lagrange equation becomes
$$
\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q}\right) - \frac{\partial L}{\partial q} = 0.
$$
Test it on a single particle moving in one dimension under a potential $V(x)$. Here $T = \tfrac12 m\dot x^2$, so $L = \tfrac12 m\dot x^2 - V(x)$. Compute the two pieces:
$$
\frac{\partial L}{\partial \dot x} = m\dot x \;\Rightarrow\; \frac{d}{dt}\frac{\partial L}{\partial \dot x} = m\ddot x, \qquad \frac{\partial L}{\partial x} = -\frac{dV}{dx}.
$$
The Euler–Lagrange equation then reads $m\ddot x + \frac{dV}{dx} = 0$, i.e.
$$
m\ddot x = -\frac{dV}{dx} = F.
$$
**Newton's second law**, recovered from a variational principle. The action knew $F = ma$ all along.

Why $L = T - V$, with that strange minus sign? Honestly: it cannot be derived from within classical mechanics without circularity. It is justified by *what it produces* — it reproduces Newton's laws, as we just saw — and the deeper "why" lies in quantum mechanics, where Feynman's path integral makes the classical path the one of stationary action as a stationary-phase limit. We assert the form, verify it gives Newton, and point onward. That is the intellectually clean way to handle a postulate that earns its place by its consequences.

### 3.4 Generalized coordinates: where the method beats Newton

If Lagrangian mechanics only reproduced $F = ma$, it would be a curiosity. Its power is that the Euler–Lagrange equation holds in *any* coordinates $q_i$ — angles, distances along a constraint, whatever makes the problem simplest — and constraints are handled automatically by the *choice* of coordinates, with no need to compute constraint forces.

Take a simple pendulum: a mass $m$ on a rigid rod of length $\ell$. In Cartesian coordinates you would fight the tension force that keeps the bob on its arc. In Lagrangian mechanics, choose the single coordinate that respects the constraint — the angle $\theta$ — and the tension never appears. With $T = \tfrac12 m\ell^2\dot\theta^2$ and $V = -mg\ell\cos\theta$,
$$
L = \tfrac12 m\ell^2\dot\theta^2 + mg\ell\cos\theta.
$$
Then $\frac{\partial L}{\partial\dot\theta} = m\ell^2\dot\theta$ and $\frac{\partial L}{\partial\theta} = -mg\ell\sin\theta$, and the Euler–Lagrange equation gives the equation of motion immediately:
$$
m\ell^2\ddot\theta + mg\ell\sin\theta = 0 \;\Longrightarrow\; \ddot\theta = -\frac{g}{\ell}\sin\theta.
$$
No tension, no resolving forces along the arc — just energy bookkeeping and one derivative. For the double pendulum or a bead on a rotating wire, where the Newtonian force analysis is a nightmare, this advantage becomes decisive.

### 3.5 The Hamiltonian: a Legendre transform

The Lagrangian lives on coordinates and velocities $(q, \dot q)$. Hamilton's reformulation trades velocity for **momentum** and produces a function on $(q, p)$. Define the generalized (canonical) momentum
$$
p \equiv \frac{\partial L}{\partial \dot q},
$$
and the **Hamiltonian** as the Legendre transform of $L$ — the same Legendre transform that built the thermodynamic potentials in Chapter 2:
$$
H(q, p) = p\,\dot q - L.
$$
A short computation of $dH$, using the definition of $p$ and the Euler–Lagrange equation, separates cleanly into $dq$ and $dp$ pieces and yields **Hamilton's canonical equations**:
$$
\boxed{\;\dot q = \frac{\partial H}{\partial p}, \qquad \dot p = -\frac{\partial H}{\partial q}.\;}
$$
Two first-order equations replace one second-order equation, with a beautiful symmetry between $q$ and $p$. For a conservative system with time-independent $L$, $H$ equals the total energy $T + V$. And this $H$ is the object quantum mechanics is built on: promote it to an operator $\hat H$ and you have the Schrödinger equation $\hat H\psi = i\hbar\,\partial\psi/\partial t$. The bridge from classical to quantum runs straight through the Hamiltonian.

### 3.6 Noether's theorem: symmetry is conservation

The deepest result the chapter touches, treated lightly. In 1918 Emmy Noether — working at Göttingen under formal barriers that for years kept her lecturing under Hilbert's name because the university would not appoint a woman — proved a theorem of breathtaking generality: **every continuous symmetry of the action corresponds to a conserved quantity.**

We will not prove it in full but demonstrate one case. Suppose $L$ does not depend explicitly on a coordinate $q$ (it is "ignorable" or **cyclic**) — that is, the action is unchanged if you shift $q$ by a constant. Then $\partial L/\partial q = 0$, and the Euler–Lagrange equation collapses to
$$
\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q}\right) = 0 \;\Longrightarrow\; \frac{\partial L}{\partial \dot q} = p = \text{constant}.
$$
The momentum conjugate to a symmetry direction is conserved. If $L$ is invariant under spatial translation, *linear momentum* is conserved; under rotation, *angular momentum*; and (by a slightly longer argument involving no explicit time dependence) under time translation, *energy* is conserved. Conservation laws are not separate postulates bolted onto mechanics — they are the shadows of symmetries, and Noether's theorem is the lamp.

---

## 4. Worked examples

### Example 1 — Snell's law from Fermat's principle (optics)

Fermat's principle (1662) says light travels the path of stationary travel time. Consider a ray going from a point in medium 1 (index $n_1$, light speed $c/n_1$) to a point in medium 2 (index $n_2$), crossing the flat interface at horizontal position $x$. The travel time is a functional of the crossing point — but here it reduces to a *function* of the single number $x$, so ordinary calculus suffices:
$$
T(x) = \frac{n_1}{c}\sqrt{a^2 + x^2} + \frac{n_2}{c}\sqrt{b^2 + (d - x)^2},
$$
where $a, b$ are the perpendicular distances to the interface and $d$ the horizontal separation. Set $dT/dx = 0$:
$$
\frac{n_1\,x}{c\sqrt{a^2+x^2}} - \frac{n_2(d-x)}{c\sqrt{b^2+(d-x)^2}} = 0.
$$
But $x/\sqrt{a^2+x^2} = \sin\theta_1$ and $(d-x)/\sqrt{b^2+(d-x)^2} = \sin\theta_2$ (the sines of the angles from the normal). Hence
$$
n_1\sin\theta_1 = n_2\sin\theta_2 \qquad\text{(Snell's law).}
$$
The law of refraction is a stationary-time condition.

![A light ray from source A in the faster upper medium crossing an interface at point P and bending toward the vertical normal into the slower lower medium to reach target B, with angles theta one and theta two marked and the relation n one sine theta one equals n two sine theta two](images/11-calculus-of-variations-and-lagrangian-hamiltonian-fig-03.png)
*Figure 11.3 — Fermat's principle of least time: the ray crosses at the point that minimizes travel time, bending toward the normal in the slower medium — which is exactly Snell's law.*

Notably, Johann Bernoulli solved the brachistochrone by *imagining* the bead as a light ray refracting through layers of ever-increasing speed — the same variational idea bridging optics and mechanics, a connection Hamilton later made exact.

### Example 2 — Conservation of energy for a falling body, via Noether

A particle in free fall has $L = \tfrac12 m\dot z^2 - mgz$, which contains no explicit $t$. By the time-translation case of Noether's theorem, the energy $E = T + V = \tfrac12 m\dot z^2 + mgz$ is conserved. Check directly: $\frac{dE}{dt} = m\dot z\ddot z + mg\dot z = \dot z(m\ddot z + mg) = \dot z\cdot 0 = 0$, using the equation of motion $m\ddot z = -mg$. The conservation law and the equation of motion are two faces of the same symmetry.

### Example 3 — The brachistochrone is a cycloid

Return to the cold open. The descent-time functional $T[y] = \int\sqrt{(1+y'^2)/(2gy)}\,dx$ has an integrand $L = \sqrt{(1+y'^2)/(2gy)}$ with no explicit $x$ dependence. When $L$ does not depend on the independent variable, the Euler–Lagrange equation has a **first integral** (the "Beltrami identity"):
$$
L - y'\frac{\partial L}{\partial y'} = \text{constant}.
$$
Substituting and simplifying yields $y(1 + y'^2) = \text{constant}$ — a differential equation whose solution, in parametric form, is
$$
x = R(\phi - \sin\phi), \qquad y = R(1 - \cos\phi),
$$
the parametric equations of a **cycloid**, the curve traced by a point on a wheel of radius $R$ rolling along a line. The bead descends fastest not along the straight chord nor a circular arc but along the path of a rolling wheel — a result that no amount of staring at the geometry would suggest, but that the Euler–Lagrange equation delivers almost mechanically.

![A bead descending from an upper-left start to a lower-right end, with the straight chord drawn dashed grey and the cycloid path bowing below it in red, dropping steeply at first, plus a dashed circle hinting at the generating wheel](images/11-calculus-of-variations-and-lagrangian-hamiltonian-fig-02.png)
*Figure 11.2 — The brachistochrone is a cycloid, not the straight chord: it drops steeply early to build speed and wins despite being the longer path.*

---

## 5. Return to the cold open

The brachistochrone is solved, and more importantly the *method* that solves it is now in hand. The unknown was a whole curve; ordinary calculus, which optimizes over numbers, could not touch it. The calculus of variations optimizes over functions: write the quantity to be extremized as a functional $T[y] = \int L\,dx$, demand that its variation vanish for every wiggle of the path that respects the fixed endpoints, integrate by parts, kill the boundary term, and read off the Euler–Lagrange equation. Solving that equation for the brachistochrone integrand gives the cycloid; solving it for $L = T - V$ gives Newton's second law; solving it for the optical travel time gives Snell's law.

That is the unity the chapter promised. "Set the derivative to zero" (Volume 1) and "set the variation to zero" (this chapter) are the same idea, one level up — and that single idea, applied to one functional after another, generates mechanics, optics, and, through Noether, the conservation laws themselves.

---

## 6. Where it generalizes

The variational principle is the organizing idea of essentially all of modern theoretical physics:

- **Quantum mechanics.** The Hamiltonian built here becomes the operator $\hat H$ of the Schrödinger equation. The variational *method* — minimizing $\langle\psi|\hat H|\psi\rangle$ over trial wavefunctions — is the workhorse approximation behind ground-state energies and Hartree–Fock theory. And Feynman's **path integral** makes the action $S$ the central quantum object: a quantum particle "tries every path," and the classical trajectory is simply where the action is stationary, so that nearby paths interfere constructively. This is the deepest answer to "why does nature extremize the action."
- **Field theory and general relativity.** Maxwell's equations, Einstein's general relativity (the Einstein–Hilbert action), and the entire Standard Model are each derived by extremizing an action functional. Noether's theorem, applied to gauge symmetry, yields conservation of electric charge. The variational principle is the common language of all fundamental physics.
- **Optics and beyond.** Fermat's principle generalizes from flat interfaces to curved, inhomogeneous, and anisotropic media, and ultimately to light following geodesics — paths of stationary interval — in the curved spacetime of general relativity. Hamilton's optico-mechanical analogy, that mechanics is to particles what ray optics is to light, foreshadowed quantum mechanics by a century.

The judgment no symbolic engine supplies is the **modeling step**: writing down the right $L$. A computer will solve the Euler–Lagrange ODE for you; it will not choose the generalized coordinates that make the problem trivial, identify $T$ and $V$, or spot the symmetry hiding a conserved quantity. The physics lives entirely in setting up the functional — and that is the irreducibly human part of the work.

---

## Exercises

1. **(The key derivation.)** Derive the Euler–Lagrange equation from $\delta S = 0$ for $S[y] = \int_{x_1}^{x_2} L(y, y', x)\,dx$. Make explicit where the fixed-endpoint condition $\eta(x_1) = \eta(x_2) = 0$ is used, and state the fundamental lemma you invoke at the end.

2. **(Newton from a Lagrangian.)** For a particle of mass $m$ in a central potential, working in polar coordinates $(r,\theta)$ with $T = \tfrac12 m(\dot r^2 + r^2\dot\theta^2)$ and $V = V(r)$, write $L$ and obtain both Euler–Lagrange equations. Identify the cyclic coordinate and the conserved quantity it implies, and name it physically.

3. **(Hamiltonian.)** For the simple harmonic oscillator $L = \tfrac12 m\dot x^2 - \tfrac12 kx^2$, compute the canonical momentum $p$, construct $H(x,p)$, verify $H = T + V$, and write Hamilton's equations. Show they reproduce $\ddot x = -(k/m)x$.

4. **(Fermat.)** Rederive Snell's law by treating the crossing point $x$ as the variable and setting $dT/dx = 0$, showing each algebraic step from $T(x)$ to $n_1\sin\theta_1 = n_2\sin\theta_2$. Then explain in one paragraph the sense in which this is a calculus-of-variations problem even though it reduces to ordinary calculus.

5. **(Conceptual / honesty.)** Explain why "least action" is more precisely called "stationary action," giving a situation where the true path is a saddle rather than a minimum. Separately, address the unmotivated minus sign in $L = T - V$: in what sense is it *justified* rather than *derived*?

---

## Sources

- Johann Bernoulli, the brachistochrone challenge, *Acta Eruditorum* (June 1696) — the founding problem; solutions by Newton, Leibniz, l'Hôpital, and the Bernoullis; Johann's optical-analogy solution.
- L. Euler, *Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes* (1744) and *Elementa Calculi Variationum* (1756) — the first systematic theory and the naming of the calculus of variations.
- J.-L. Lagrange, the 1755 letter to Euler (the analytic $\delta$-method) and *Mécanique analytique* (1788) — mechanics rebuilt on a single variational principle; $L = T - V$ and Lagrange's equations.
- P. de Fermat, principle of least time (1662) — the optical variational principle; Snell's law.
- W. R. Hamilton, "On a General Method in Dynamics," *Phil. Trans. R. Soc.* (1834–1835) — stationary action, the Hamiltonian, and the canonical equations.
- E. Noether, "Invariante Variationsprobleme," *Nachrichten der Göttinger Gesellschaft* (1918; presented by F. Klein) — continuous symmetry ⇒ conserved quantity.
- On the analytical-mechanics lineage: S. Kovalevskaya's integrable spinning top (the "Kovalevskaya top"), a rigid-body problem solved within exactly this Lagrangian/Hamiltonian tradition. [verify primary citation]
- Standard treatments: H. Goldstein, *Classical Mechanics*; J. R. Taylor, *Classical Mechanics*; L. D. Landau and E. M. Lifshitz, *Mechanics*. [verify editions/pages]
- In-series: *Physics — Optics* ch. 02 (Snell's law from Fermat's principle, with the generalization to geodesics); *Physics — Classical Mechanics* ch. 09 (work–energy bookkeeping, $T$ and $V$ as the accounts energy moves between — the conceptual on-ramp).
