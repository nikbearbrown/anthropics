# Module M-10 — Multivariable Calculus and Separation of Variables

**When you need this:** QM chapters II·5 (The 3D Schrödinger Equation), II·9 (The Hydrogen Atom)

**Condensed from:** *Mathematics for Physics* Vol 2, Ch 7 (primary); Vol 2, Ch 2 (partial-derivative foundations)

---

## When You Need This

When we move from one-dimensional quantum mechanics to three-dimensional problems, the Schrödinger equation becomes a partial differential equation in three variables. Chapter II·5 presents this equation; working with it requires the technique of **separation of variables**, which breaks a PDE in three coordinates into three independent ODEs.

Chapter II·9 (hydrogen) shows the payoff most clearly: three coordinate separations produce three quantum numbers $(n, \ell, m)$, each arising from a boundary or regularity condition on the separated equation for that coordinate. This module develops the tools needed to follow that logic — including why $m$ must be an integer and where the centrifugal barrier comes from.

---

## Partial Derivatives: The Essential Notation

A function $f(x,y,z)$ has a separate rate of change in each direction. The **partial derivative** with respect to $x$ holds all other variables fixed:

$$\left(\frac{\partial f}{\partial x}\right)_{y,z} = \lim_{h\to 0}\frac{f(x+h,y,z)-f(x,y,z)}{h}.$$

The subscript names what is held fixed. When variables are genuinely independent (as $x,y,z$ in Cartesian coordinates), the subscript is often dropped; when variables are linked by a constraint, dropping it is an error. In spherical coordinates $r,\theta,\phi$ are independent, so $\partial/\partial r$ at fixed $\theta,\phi$ is unambiguous.

The **total differential** accounts for all directions:

$$df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz.$$

**Equality of mixed partials (Clairaut–Schwarz).** For any smooth function, $\partial^2 f/\partial y\,\partial x = \partial^2 f/\partial x\,\partial y$. The order of differentiation does not matter. The self-adjointness of the separated operators ultimately traces back to this property.

---

## The Gradient and the Laplacian

The **gradient** points in the direction of steepest increase:

$$\nabla f = \frac{\partial f}{\partial x}\,\hat x + \frac{\partial f}{\partial y}\,\hat y + \frac{\partial f}{\partial z}\,\hat z.$$

The **Laplacian** $\nabla^2 f = \nabla\cdot\nabla f$ in Cartesian coordinates:

$$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}.$$

The 3D time-independent Schrödinger equation is:

$$\boxed{-\frac{\hbar^2}{2m}\nabla^2\psi + V(\mathbf{r})\,\psi = E\psi.}$$

Solving it requires expressing $\nabla^2$ in a coordinate system matched to the geometry of $V$, then separating variables. For a central potential $V = V(r)$, spherical coordinates are the appropriate choice.

---

## The Spherical Laplacian

In spherical coordinates $(r,\theta,\phi)$ — where $\theta\in[0,\pi]$ is the polar angle from the $z$-axis and $\phi\in[0,2\pi)$ is the azimuthal angle — the Laplacian is:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\,\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2}.$$

The three terms correspond to radial, polar, and azimuthal variation. Their different $r$-prefactors are what allow the radial and angular parts to separate cleanly.

---

## Separation of Variables: The Method in Four Steps

The approach is to assume the solution is a **product of single-variable functions**, substitute, and show the equation splits into independent parts. Working through this once carefully makes the pattern clear.

**Illustration: the 3D infinite square well** (Cartesian coordinates, $V = 0$ inside $[0,L]^3$, $\psi = 0$ on the walls).

**Step 1 — product ansatz.** We assume $\psi(x,y,z) = X(x)\,Y(y)\,Z(z)$. Substituting into $-(\hbar^2/2m)\nabla^2\psi = E\psi$:

$$-\frac{\hbar^2}{2m}(X''YZ + XY''Z + XYZ'') = EXYZ.$$

**Step 2 — divide by the product.** Dividing through by $XYZ$:

$$-\frac{\hbar^2}{2m}\left(\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z}\right) = E.$$

**Step 3 — the separation argument.** Each term $X''/X$ depends only on $x$; the others depend only on $y$ and $z$. A function of $x$ alone that equals a function of $y$ and $z$ alone must be a constant. Therefore each ratio is separately constant:

$$\frac{X''}{X} = -k_x^2, \qquad \frac{Y''}{Y} = -k_y^2, \qquad \frac{Z''}{Z} = -k_z^2,$$

with the constraint $\hbar^2(k_x^2+k_y^2+k_z^2)/(2m) = E$.

The sign $-k^2$ (negative) is chosen deliberately: it gives oscillatory solutions $\sin(k_x x)$ and $\cos(k_x x)$, which can satisfy zero-at-walls boundary conditions. A positive constant would give growing and decaying exponentials, which cannot vanish at both walls simultaneously. Choosing the wrong sign is the single most common error in separation of variables.

**Step 4 — boundary conditions quantize.** The condition $X(0) = X(L) = 0$ forces $X_{n_x}(x) = \sin(n_x\pi x/L)$ with $k_x = n_x\pi/L$, $n_x = 1,2,3,\ldots$ The separation constant is not arbitrary — it is quantized by the boundary condition. The PDE has produced discrete eigenvalues:

$$E_{n_x n_y n_z} = \frac{\hbar^2\pi^2}{2mL^2}(n_x^2+n_y^2+n_z^2), \qquad n_x,n_y,n_z = 1,2,3,\ldots$$

A sum of product solutions is also a solution, by linearity of the Schrödinger equation. The general solution is a superposition over all allowed $(n_x,n_y,n_z)$.

![Four-step Cartesian separation-of-variables cascade](../images/10-multivariable-calculus-and-separation-of-variables-fig-01.png)
*Figure 10.1 — The four-step separation-of-variables cascade: product ansatz, division by the product, three independent ODEs, and boundary conditions that quantize each separation constant.*

---

## Separation in Spherical Coordinates: The Central-Force Split

For a central potential $V = V(r)$, we substitute $\psi(r,\theta,\phi) = R(r)\,\Theta(\theta)\,\Phi(\phi)$ into the Schrödinger equation with the spherical Laplacian. Multiplying through by $r^2/(R\Theta\Phi)$, the $\phi$ dependence appears only in the last term of the Laplacian; setting it equal to a constant $-m^2$ gives the **azimuthal equation**:

$$\frac{d^2\Phi}{d\phi^2} = -m^2\Phi \;\Longrightarrow\; \Phi(\phi) = e^{im\phi}.$$

**Regularity quantizes** $m$: the wavefunction must be single-valued — $\Phi(\phi+2\pi) = \Phi(\phi)$ — which forces $e^{2\pi im} = 1$, hence $m\in\mathbb{Z}$. This is not a postulate. The integer character of the orbital magnetic quantum number $m$ is a consequence of single-valuedness of a function defined on the sphere. (Spin escapes this argument because spinors transform under SU(2), which admits half-integer representations — they are not ordinary functions on the sphere.)

The remaining radial-plus-polar equation separates again. The polar part, with $u = \cos\theta$, becomes the **associated Legendre equation** with separation constant $\ell(\ell+1)$:

$$\frac{d}{du}\!\left[(1-u^2)\frac{dP}{du}\right] + \left[\ell(\ell+1) - \frac{m^2}{1-u^2}\right]P = 0.$$

**Regularity quantizes** $\ell$: finiteness at the poles $u = \pm 1$ forces $\ell$ to be a non-negative integer with $|m|\leq\ell$. The solutions are the associated Legendre functions $P_\ell^m(\cos\theta)$. The full angular factor is the **spherical harmonic**:

$$Y_{\ell m}(\theta,\phi) = N_{\ell m}\,P_\ell^m(\cos\theta)\,e^{im\phi}.$$

The **radial equation**, with the angular part separated and contributing the constant $\ell(\ell+1)$:

$$-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right) + \left[\frac{\hbar^2\ell(\ell+1)}{2mr^2} + V(r)\right]R = ER.$$

The term $\hbar^2\ell(\ell+1)/(2mr^2)$ is the **centrifugal barrier** — it comes not from any classical assumption but directly from the angular separation constant. The angular equation never involved $V(r)$. The spherical harmonics $Y_{\ell m}$ are therefore the angular eigenfunctions for **every** central potential — hydrogen, the 3D harmonic oscillator, and the free particle alike. What differs between problems is the radial equation and its solutions.

![Spherical separation cascade producing three quantum numbers](../images/10-multivariable-calculus-and-separation-of-variables-fig-02.png)
*Figure 10.2 — Spherical separation cascade: one central-potential equation branches into three independent ODEs, each generating one quantum number through its own regularity or single-valuedness constraint.*

---

## Worked Example: The 3D Infinite Square Well and Its Degeneracy

Energy levels: $E_{n_x n_y n_z} = \frac{\hbar^2\pi^2}{2mL^2}(n_x^2+n_y^2+n_z^2)$, with $n_x,n_y,n_z \geq 1$.

The ground state $(1,1,1)$ has energy $E_{111} = 3\hbar^2\pi^2/(2mL^2)$ — non-degenerate.

The first excited energy level has $n_x^2+n_y^2+n_z^2 = 6$, achieved by $(2,1,1)$, $(1,2,1)$, $(1,1,2)$ — a **3-fold degeneracy** arising from the cubic symmetry of the box. Each state has the same energy but a different spatial wavefunction. For $(2,1,1)$: $\psi \propto \sin(2\pi x/L)\sin(\pi y/L)\sin(\pi z/L)$ — a product of three factors, each determined by a separate ODE.

This is the first appearance in the series of degeneracy from spatial symmetry: because the box has the same length in all three directions, permuting $(n_x,n_y,n_z)$ gives states with the same energy but genuinely different spatial structure.

---

## In the Quantum Series

**QM II·5 — The 3D Schrödinger Equation.** The chapter opens with the full spherical Laplacian and the product ansatz $\psi = R(r)\Theta(\theta)\Phi(\phi)$. The material above provides the mechanics: substitution, division-by-product, why each resulting ratio must be constant, and where quantum numbers come from. Working through the Cartesian (box) separation completely before tackling the spherical case is recommended.

**QM II·9 — The Hydrogen Atom.** The central-force problem with $V(r) = -e^2/(4\pi\varepsilon_0 r)$. The angular separation is identical to the general case — $Y_{\ell m}$ regardless of the potential. The new content is the radial equation for the Coulomb potential, whose solutions are the associated Laguerre polynomials (Module M-11). The principal quantum number $n$ arises from a termination condition on the radial power series, exactly as the energy eigenvalues of the 1D harmonic oscillator arise from terminating the Hermite series.

The three quantum numbers $(n,\ell,m)$ arise from three different places:
- $m$ from the azimuthal equation, via single-valuedness
- $\ell$ from the polar equation, via finiteness at the poles
- $n$ from the radial equation, via normalizability (series termination)

No number is postulated. Every one is a boundary or regularity condition in disguise.

---

## Conventions and Pitfalls

**Sign of the separation constant.** A negative separation constant $-k^2$ gives oscillatory solutions; a positive one gives exponentials. The choice is dictated by which boundary condition must be met: zero-at-walls requires oscillation, so the constant must be negative. Choose the sign before writing the ODE.

![Decision fork for the sign of the separation constant](../images/10-multivariable-calculus-and-separation-of-variables-fig-03.png)
*Figure 10.3 — Sign-of-separation-constant decision fork: a negative constant yields an oscillatory solution that can satisfy zero-at-walls, while a positive constant yields exponentials that cannot.*

**Spherical coordinate conventions.** The QM series uses the physics convention: $\theta\in[0,\pi]$ is the polar angle (colatitude, from the $z$-axis) and $\phi\in[0,2\pi)$ is the azimuthal angle. Mathematics texts and some engineering references reverse $\theta$ and $\phi$. Verify the convention before consulting any external source. Mixing them makes $Y_{10}\propto\sin\theta$ instead of $\cos\theta$.

**The angular equation does not see the potential.** The $Y_{\ell m}$ functions are universal for central potentials because $V(r)$ factors out when dividing by $\psi = R\Theta\Phi$. The hydrogen wavefunctions are not hydrogen's angular functions — they are the angular functions of every spherically symmetric problem.

**Termination vs. regularity quantization.** Two distinct mechanisms produce discrete eigenvalues: (1) a power series that must *terminate* to remain normalizable (Hermite, Laguerre polynomials), and (2) finiteness at a *singular endpoint* of the ODE (Legendre at $u = \pm 1$). Both are regularity conditions, but they arise at different stages and should not be conflated.

---

## Quick Practice

1. **Sign choice.** Separate $\partial^2\psi/\partial x^2 + \partial^2\psi/\partial y^2 = 0$ on the strip $0\leq x\leq L$, $y\geq 0$, with $\psi = 0$ at $x = 0,L$ and $\psi\to 0$ as $y\to\infty$. Explain why the separation constant must be negative for $X(x)$ and positive for $Y(y)$, and write down the allowed modes.

2. **Degeneracy count.** For the 3D infinite square well of side $L$, list all $(n_x,n_y,n_z)$ triples at the second excited energy level (the third distinct energy value). What is the degeneracy, and what symmetry of the box causes it?

3. **Where** $m$ **comes from.** Starting from $\Phi'' = -m^2\Phi$ with solution $\Phi = e^{im\phi}$, state the regularity condition that forces $m\in\mathbb{Z}$, and explain in one sentence why this argument fails for $\text{spin-}\tfrac{1}{2}$.

---

## Go Deeper

The separation mechanics and spherical-coordinate Laplacian are developed fully in *Mathematics for Physics* Vol 2, Ch 7 ("Special Functions and Separation of Variables"), Sections 3–6.

---

## References

- Griffiths, D.J. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018. §4.1–4.2. [verify]
- Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994. Ch. 13. [verify]
- Boas, M.L. *Mathematical Methods in the Physical Sciences*, 3rd ed. Wiley, 2006. Ch. 13. [verify]
- Legendre, A.-M. "Recherches sur l'attraction des sphéroïdes homogènes." *Mémoires de Mathématiques et de Physique*, Vol. 10 (read 1782, published 1785). [verify]
