# Special Functions and Separation of Variables

*Separating Laplace's and Schrödinger's equations in Cartesian, cylindrical, and spherical coordinates; the special functions as the separated ODEs' solutions; and Sturm–Liouville theory as the single reason they are all orthogonal complete bases.*

---

## 1. Cold open: the shape of the hydrogen atom

The hydrogen atom is the one atom physics can solve exactly, and its solution is the template for the entire periodic table. An electron sits in the Coulomb potential of a proton; the Schrödinger equation that governs it,

$$
-\frac{\hbar^2}{2m}\nabla^2\psi - \frac{e^2}{4\pi\varepsilon_0 r}\psi = E\psi,
$$

is a partial differential equation in three dimensions. Out of it must come everything that organizes chemistry: the discrete energy levels, the quantum numbers $(n, \ell, m)$, the $s$, $p$, $d$ orbital shapes, and the $2n^2$ electron capacity of each shell. None of this is put in by hand. It all falls out of solving one PDE — provided you solve it the right way.

The right way is to *separate variables*: guess that the solution factors into a product, one factor per coordinate, and watch the single PDE shatter into independent ordinary differential equations. The angular factors turn out to be the **spherical harmonics** $Y_{\ell m}(\theta,\phi)$; the same functions describe the rigid rotor, multipole radiation, and the temperature map of the cosmic microwave background. The radial factor involves associated Laguerre polynomials. And these are not isolated curiosities: spherical harmonics, Legendre polynomials, Hermite polynomials, and Bessel functions are all the *same kind of object* — orthogonal eigenfunctions of a self-adjoint differential operator — unified by one theorem. This chapter derives the method, then catalogues the functions, then names the theorem that ties them together.

This is a reference-heavy chapter. The method is the part to *learn*; the catalogue of functions is the part to *consult*. Do not try to memorize the polynomial coefficients — learn where they come from.

---

## 2. The tool, named

Volume 1 introduced partial derivatives, the wave equation, and the idea of expanding a function in an orthogonal basis (Fourier series). Chapter 5 gave the spectral theorem for Hermitian operators in finite dimensions; Chapter 6 took the orthogonal-expansion idea to a continuum. This chapter is where those threads meet a partial differential equation.

The method is **separation of variables**: assume the solution of a linear PDE is a product of single-variable functions, substitute, and divide, so that the equation splits into ordinary differential equations linked only by **separation constants**. Those constants become *eigenvalues*, fixed by boundary and regularity conditions. The ODEs that result, in the standard coordinate systems, are the defining equations of the **special functions** — Legendre, Hermite, Bessel, and their relatives. The unifying hinge is **Sturm–Liouville theory**: each family is the set of orthogonal eigenfunctions of a self-adjoint second-order operator, which is *why* arbitrary boundary data expands in them, exactly as a periodic function expands in a Fourier series. Sturm–Liouville is the infinite-dimensional cousin of Chapter 5's spectral theorem.

---

## 3. Development & derivation

### The separation method, done once carefully

Take Laplace's equation $\nabla^2\Phi = 0$ in Cartesian coordinates as the cleanest illustration:

$$
\frac{\partial^2\Phi}{\partial x^2} + \frac{\partial^2\Phi}{\partial y^2} + \frac{\partial^2\Phi}{\partial z^2} = 0.
$$

**Step 1 — assume a product.** Guess $\Phi(x,y,z) = X(x)\,Y(y)\,Z(z)$. This is an *ansatz*, justified after the fact by completeness: it will not give every solution directly, but sums of such products will. Substituting,

$$
X''YZ + XY''Z + XYZ'' = 0.
$$

**Step 2 — divide by the product.** Divide through by $XYZ$:

$$
\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} = 0.
$$

**Step 3 — the separation argument.** Each term depends on only one variable. The first depends on $x$ alone, yet the equation says it equals $-(Y''/Y + Z''/Z)$, which contains no $x$. A function of $x$ alone that equals a function of $y$ and $z$ alone must be a *constant*. So each term is constant:

$$
\frac{X''}{X} = -k_x^2, \qquad \frac{Y''}{Y} = -k_y^2, \qquad \frac{Z''}{Z} = -k_z^2,
\qquad k_x^2 + k_y^2 + k_z^2 = 0.
$$

The PDE has become three ODEs. The $-k^2$ are the **separation constants**, and the *sign* matters: written this way, the solutions of $X'' = -k_x^2 X$ are oscillatory ($\sin, \cos$); a positive constant would give exponentials. Which you need is dictated by the boundary conditions — getting the sign wrong is the single most common error in the method, because it decides whether the solution can oscillate (to fit periodic or zero-at-walls conditions) or must grow/decay.

**Step 4 — boundary conditions quantize.** On a box with $\Phi=0$ on the walls, the requirement $X(0)=X(L)=0$ forces $k_x = n\pi/L$ for integer $n$ — the separation constant is *quantized* by the boundary condition. This is exactly how a continuous PDE produces discrete modes.

![A flow diagram. One partial differential equation, the Laplacian of phi equals zero, is given the product ansatz phi equals X times Y times Z. Dividing by the product, each term depends on a single variable and must equal a constant, so the PDE splits into three ordinary differential equations linked only by separation constants, which boundary conditions then quantize.](images/07-special-functions-and-separation-of-variables-fig-01.png)
*Figure 7.1 — Separation of variables: the product ansatz, divided through, forces each single-variable term to be constant, shattering the PDE into ODEs whose separation constants the boundary conditions quantize.*

The lesson to carry: separation is a *general* PDE method, not a quantum trick. The same four steps work for the heat equation, the wave equation, and Schrödinger's equation; what changes with the geometry is which coordinate system makes the boundaries simple, and therefore which special functions appear.

### Spherical coordinates: where the spherical harmonics live

The hydrogen atom and every spherically symmetric problem call for spherical coordinates $(r, \theta, \phi)$. The Laplacian is

$$
\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial}{\partial r}\right)
+ \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\,\frac{\partial}{\partial\theta}\right)
+ \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2}.
$$

Assume $\psi = R(r)\,\Theta(\theta)\,\Phi(\phi)$ and substitute into $\nabla^2\psi = (\text{stuff})\,\psi$. After multiplying by $r^2/(R\Theta\Phi)$, the radial part separates off, leaving an angular equation set equal to a separation constant we *name* $\ell(\ell+1)$ (with foresight). The angular equation separates again. The $\phi$-equation is

$$
\frac{d^2\Phi}{d\phi^2} = -m^2\Phi \;\Longrightarrow\; \Phi(\phi) = e^{im\phi}.
$$

Here a **regularity condition** quantizes $m$: the wavefunction must be single-valued, $\Phi(\phi + 2\pi) = \Phi(\phi)$, which forces $m$ to be an *integer*. (This is exactly why orbital angular momentum is integer-valued; spin, which is not a function on the sphere, escapes this argument and may be half-integer.) The remaining $\theta$-equation, after substituting $u = \cos\theta$, is the **associated Legendre equation**

$$
\frac{d}{du}\!\left[(1-u^2)\frac{dP}{du}\right] + \left[\ell(\ell+1) - \frac{m^2}{1-u^2}\right]P = 0,
$$

whose regular solutions exist only when $\ell$ is a non-negative integer with $|m|\leq\ell$ — a second quantization, this time from demanding finiteness at the poles $u=\pm1$. The solutions are the **associated Legendre functions** $P_\ell^m(\cos\theta)$, and the full angular factor is the **spherical harmonic**

$$
Y_{\ell m}(\theta,\phi) = N_{\ell m}\,P_\ell^m(\cos\theta)\,e^{im\phi}.
$$

![A plot of the Legendre polynomials P-zero through P-three on the interval minus one to one. P-zero is flat at one, P-one is the line u, and P-two and P-three are curves with increasing numbers of zeros. Any two are orthogonal with unit weight.](images/07-special-functions-and-separation-of-variables-fig-02.png)
*Figure 7.2 — The first Legendre polynomials $P_\ell(u)$ on $[-1,1]$: each has $\ell$ zeros and any two are orthogonal with weight $1$ — one instance of the Sturm–Liouville theorem.*

The deep point: the angular equation never saw the potential. It came entirely from the Laplacian's angular part, so $Y_{\ell m}$ is the angular solution for *every* central potential — hydrogen, the harmonic well, the free particle alike. The angular eigenvalue $\ell(\ell+1)$ "only knows about the rotation group." (Historically, Legendre introduced $P_\ell(\cos\theta)$ in 1782 as the coefficients in the multipole expansion of the gravitational potential $1/|\mathbf r - \mathbf r'|$; the name "spherical harmonics" was coined later by Kelvin and Tait, 1867. The functions arrived from a physics problem.)

### Cylindrical coordinates: where the Bessel functions live

In cylindrical coordinates $(\rho, \phi, z)$ the relevant equation — for a vibrating circular drumhead, an optical fiber, or a waveguide — separates with the $\phi$ and $z$ dependence again giving exponentials, and the radial part giving **Bessel's equation**:

$$
\rho^2\frac{d^2R}{d\rho^2} + \rho\frac{dR}{d\rho} + (k^2\rho^2 - m^2)R = 0.
$$

Its regular solution is the **Bessel function** $J_m(k\rho)$, an oscillation whose amplitude decays and whose zeros are not evenly spaced. (Bessel functions predate Bessel: Daniel Bernoulli used $J_0$ for the hanging chain in 1732, and Euler used integer-order $J_n$ for the vibrating membrane in 1764; Bessel systematized them in 1824 studying planetary perturbations.) The boundary condition that the drumhead is pinned at the rim, $R(\rho = a) = 0$, requires $k a$ to be a *zero* of $J_m$ — so the allowed frequencies are set by the Bessel zeros, the cylindrical analogue of $n\pi/L$.

### Cartesian coordinates with a quadratic potential: where the Hermite polynomials live

The quantum harmonic oscillator, $-\frac{\hbar^2}{2m}\psi'' + \frac12 m\omega^2 x^2\psi = E\psi$, separates trivially in one dimension but produces a non-trivial ODE because of the $x^2$ potential. Substituting the asymptotic Gaussian factor $\psi = H(x)\,e^{-m\omega x^2/2\hbar}$ and a dimensionless variable $\xi = \sqrt{m\omega/\hbar}\,x$, the equation for $H$ becomes **Hermite's equation**:

$$
H'' - 2\xi H' + 2n H = 0.
$$

Demanding that $H$ be a *polynomial* (so that $\psi$ stays normalizable rather than blowing up against the Gaussian) forces the energy to quantize as $E_n = \hbar\omega(n + \tfrac12)$ with $n$ a non-negative integer — the oscillator's evenly spaced ladder. The solutions are the **Hermite polynomials** $H_n(\xi)$. The termination-of-the-series condition is the quantization; this is the cleanest place to see an eigenvalue born from "the solution must not diverge."

### The Sturm–Liouville hinge

Three different geometries, three different special functions — but one structure underneath. Every one of the separated radial/angular ODEs can be written in the **Sturm–Liouville form**

$$
\frac{d}{dx}\!\left[p(x)\frac{dy}{dx}\right] + q(x)\,y + \lambda\,w(x)\,y = 0,
$$

with a real weight $w(x) > 0$, on an interval with suitable boundary conditions. The operator $\hat L y = \frac{1}{w}\big[-(p y')' - q y\big]$ is **self-adjoint** with respect to the weighted inner product $\langle f, g\rangle = \int f^*(x) g(x)\,w(x)\,dx$. And here Chapter 5 pays off: a self-adjoint operator has *real eigenvalues* and *orthogonal eigenfunctions*. The proof is the same two lines, now with functions and an integral instead of vectors and a sum.

Concretely, for two eigenfunctions $y_m, y_n$ with distinct eigenvalues $\lambda_m \neq \lambda_n$, the self-adjointness gives

$$
(\lambda_m - \lambda_n)\int_a^b y_m(x)\,y_n(x)\,w(x)\,dx = \big[p(y_m' y_n - y_m y_n')\big]_a^b = 0,
$$

the boundary term vanishing by the boundary/regularity conditions — so

$$
\boxed{\;\int_a^b y_m(x)\,y_n(x)\,w(x)\,dx = 0 \quad (m\neq n).\;}
$$

This single theorem explains *all* the orthogonalities: Legendre polynomials are orthogonal with weight $w=1$ on $[-1,1]$; Hermite polynomials with weight $e^{-\xi^2}$ on $(-\infty,\infty)$; Bessel functions $J_m(k_i\rho)$ with weight $w=\rho$ on $[0,a]$. They are not four coincidences; they are four instances of one theorem. And because each family is also *complete*, any reasonable boundary function expands in it — a **generalized Fourier series**

$$
f(x) = \sum_n c_n\, y_n(x), \qquad
c_n = \frac{\int f\,y_n\,w\,dx}{\int y_n^2\,w\,dx},
$$

with coefficients computed by orthogonality, exactly as in an ordinary Fourier series. The orthogonality *is* what makes the coefficients computable — projecting $f$ onto each basis function in turn.

---

## 4. The special-function catalogue (reference)

This table is for consulting, not memorizing. Each family is the Sturm–Liouville eigenfunction set of the indicated separated ODE.

| Family | Defining ODE | Interval, weight $w$ | Physics origin |
|---|---|---|---|
| **Legendre** $P_\ell(u)$ | $\frac{d}{du}[(1-u^2)P'] + \ell(\ell+1)P = 0$ | $[-1,1]$, $w=1$ | polar part of spherical Laplace; multipole expansion |
| **Associated Legendre** $P_\ell^m(u)$ | as above, with $-\,m^2/(1-u^2)$ term | $[-1,1]$, $w=1$ | non-axisymmetric angular solutions |
| **Spherical harmonics** $Y_{\ell m}(\theta,\phi)$ | $\hat L^2 Y = \ell(\ell+1)Y$ | sphere, $w=\sin\theta$ | angular part of *every* central potential |
| **Hermite** $H_n(\xi)$ | $H'' - 2\xi H' + 2nH = 0$ | $(-\infty,\infty)$, $w=e^{-\xi^2}$ | quantum harmonic oscillator |
| **Bessel** $J_m(x)$ | $x^2 R'' + x R' + (x^2 - m^2)R = 0$ | $[0,a]$, $w=\rho$ | circular drum, fiber modes, Airy disk |
| **Associated Laguerre** $L_n^k(r)$ | $r L'' + (k{+}1{-}r)L' + nL = 0$ | $[0,\infty)$, $w=r^k e^{-r}$ | hydrogen radial function |

The associated Laguerre polynomials supply the hydrogen *radial* factor $R_{n\ell}(r)$; we name the equation and place it in the same Sturm–Liouville scheme rather than deriving it in full — its quantization (which yields the principal quantum number $n$ and the energies $E_n \propto -1/n^2$) follows the same termination logic as Hermite.

---

## 5. Worked examples

### Example 1 — One Laplacian, two geometries

Solve $\nabla^2\Phi=0$ in a rectangular box versus a sphere, to see that separation is a general method, not a quantum trick. In the **box**, separation gives $\Phi = \sin(k_x x)\sin(k_y y)\,\sinh(k_z z)$-type products: sines where boundaries pin the function to zero, a hyperbolic sinh where one face is held at a fixed potential — the separation-constant signs chosen so the boundary conditions can be met. In the **sphere**, the *same* operator separates into the radial equation (solutions $r^\ell$ and $r^{-\ell-1}$) and the angular $Y_{\ell m}$. The electrostatic potential outside a charged sphere is a sum $\Phi = \sum_{\ell m} b_{\ell m}\, r^{-\ell-1} Y_{\ell m}$ — the multipole expansion, with the $\ell=0$ term the monopole $1/r$, $\ell=1$ the dipole, and so on. Same PDE, same method, different special functions selected by the geometry.

### Example 2 — A drumhead, and where the $1.22$ comes from

A circular membrane of radius $a$, pinned at the rim, vibrates with displacement $u(\rho,\phi,t) = J_m(k\rho)\cos(m\phi)\cos(\omega t)$ from cylindrical separation. The rim condition $u(a)=0$ requires $J_m(ka)=0$: the allowed $k$ are the Bessel zeros divided by $a$. The fundamental mode ($m=0$) uses the first zero of $J_0$, $j_{0,1}\approx 2.405$, giving $\omega = (j_{0,1}/a)\,c$ — *not* a harmonic ratio, which is why a drum sounds inharmonic where a string sounds tonal. The same Bessel structure governs a circular optical aperture: its Fraunhofer diffraction pattern (Chapter 6) is the Airy disk built from $J_1$, whose first zero at $j_{1,1}\approx 3.832$ gives the Rayleigh resolution limit $\theta_{\min} = 1.22\,\lambda/D$, since $1.22 = j_{1,1}/\pi$. The famous $1.22$ is a Bessel zero.

![Three vibration modes of a circular drumhead pinned at the rim. The fundamental mode uses the first zero of J-zero; a higher mode adds a nodal circle at the second zero; an angular mode adds a nodal diameter at the first zero of J-one. Because the Bessel zeros are unevenly spaced, the overtones are inharmonic.](images/07-special-functions-and-separation-of-variables-fig-03.png)
*Figure 7.3 — Drumhead modes sit at the zeros of Bessel functions; the uneven spacing of the zeros makes a drum inharmonic, and the first zero of $J_1$ supplies the $1.22$ of the Rayleigh limit ($1.22=j_{1,1}/\pi$).*

### Example 3 — The harmonic oscillator ground state

From Section 3, the oscillator's $n=0$ Hermite polynomial is the constant $H_0 = 1$, so the ground state is the pure Gaussian $\psi_0(x) \propto e^{-m\omega x^2/2\hbar}$ with energy $E_0 = \tfrac12\hbar\omega$ — the zero-point energy, nonzero because the termination condition's lowest allowed $n$ is $0$, not because of any classical reason. The first excited state uses $H_1(\xi) = 2\xi$, giving $\psi_1 \propto x\,e^{-m\omega x^2/2\hbar}$, which is odd and has a node at the origin. Orthogonality $\int \psi_0\psi_1\,dx = 0$ is automatic: it is the Hermite orthogonality with weight $e^{-\xi^2}$, an instance of the Sturm–Liouville theorem, and you can also see it directly because the integrand (even times odd) is odd.

---

## 6. Return to the cold open: the hydrogen atom

Now run the method on hydrogen. The potential is central, so use spherical coordinates and the product ansatz $\psi(r,\theta,\phi) = R(r)\,Y_{\ell m}(\theta,\phi)$. The angular part is *already solved*: it is the spherical-harmonic eigenvalue problem of Section 3, contributing the centrifugal term $\ell(\ell+1)$ and producing the quantum numbers $\ell$ (integer, from finiteness at the poles) and $m$ (integer, $|m|\leq\ell$, from single-valuedness in $\phi$). What remains is the radial equation,

$$
-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{dR}{dr}\right)
+ \left[\frac{\hbar^2\ell(\ell+1)}{2mr^2} - \frac{e^2}{4\pi\varepsilon_0 r}\right]R = E R,
$$

where the $\ell(\ell+1)$ separation constant has reappeared as a centrifugal barrier. Demanding that $R$ be normalizable (decaying at infinity, finite at the origin) terminates its series — associated Laguerre — and quantizes the energy:

$$
E_n = -\frac{13.6\,\text{eV}}{n^2}, \qquad n = 1, 2, 3, \dots, \qquad \ell = 0, 1, \dots, n-1.
$$

Everything the cold open asked for now falls out. The discrete levels: from the radial termination condition. The quantum numbers $(n,\ell,m)$: three separation/regularity conditions, one per coordinate. The orbital shapes: $|Y_{\ell m}|^2$ — $\ell=0$ spherical ($s$), $\ell=1$ lobed ($p$), $\ell=2$ ($d$). The $2n^2$ capacity: for each $n$ there are $n$ values of $\ell$, each with $2\ell+1$ values of $m$, summing to $n^2$ spatial states, doubled by spin. The periodic table is the bookkeeping of one separated PDE. No piece was inserted by hand; every piece is a separation constant fixed by a boundary or regularity condition.

---

## 7. Where it generalizes

- **Angular momentum, everywhere.** Because the $Y_{\ell m}$ are the angular solutions for any central potential, they reappear in the rigid rotor, selection rules, and multipole radiation. They are the eigenfunctions of the commuting observables $\hat L^2, \hat L_z$ — the Chapter 5 structure made concrete.
- **Cosmology.** Temperature fluctuations on the celestial sphere expand in spherical harmonics; the angular power spectrum $C_\ell$ is the $Y_{\ell m}$ analogue of a Fourier power spectrum, and reading it is how the geometry and contents of the universe are inferred from the cosmic microwave background.
- **Electrostatics and waveguides.** Boundary-value problems in spherical or cylindrical regions reduce to Legendre or Bessel expansions matched to the boundary — the original Legendre/Laplace gravitational-potential problem, generalized.
- **The unifying view.** Sturm–Liouville theory says all of this — Fourier series, Legendre, Hermite, Bessel, the discrete modes of a box — is one phenomenon: a self-adjoint differential operator has an orthogonal complete eigenbasis, and "solve the PDE" means "expand the data in that basis." Chapter 5's finite-dimensional spectral theorem and this chapter's infinite-dimensional one are the same idea at two sizes.

A computer algebra system returns $Y_{\ell m}$ and $J_m$ instantly. It does not choose which coordinate system makes the geometry separable, pick the sign of the separation constant, recognize that the angular equation is identical for *every* central potential, apply the regularity condition that quantizes the eigenvalue, or know that the orthogonality of the basis is what makes the expansion coefficients computable at all. The chapter builds the judgment that turns "look up the special function" into "derive why this function and not another."

---

## Exercises

1. **(Separation, with the sign decision.)** Separate the two-dimensional Laplace equation $\Phi_{xx} + \Phi_{yy} = 0$ on the strip $0 \leq x \leq L$, $y \geq 0$, with $\Phi = 0$ on the sides $x=0, L$ and $\Phi\to 0$ as $y\to\infty$. Show why the separation constant must make $X(x)$ oscillatory and $Y(y)$ decaying, and find the allowed modes.

2. **(Regularity quantizes.)** In the spherical separation, show that requiring $\Phi(\phi)$ single-valued forces $m$ to be an integer, and explain in one sentence why this argument does *not* apply to spin.

3. **(Derivation — required.)** Prove the Sturm–Liouville orthogonality theorem: for two eigenfunctions of $\frac{d}{dx}[p\,y'] + q\,y + \lambda w\,y = 0$ with distinct eigenvalues, $\int_a^b y_m y_n\, w\,dx = 0$, provided the boundary term $[p(y_m'y_n - y_m y_n')]_a^b$ vanishes. State which boundary/regularity conditions make it vanish.

4. **(Bessel zeros.)** A circular drumhead of radius $a$ has its lowest mode at the first zero of $J_0$. Look up $j_{0,1}$ and $j_{1,1}$ and compute the ratio of the first two axisymmetric mode frequencies. Explain why a drum is inharmonic while a string is harmonic.

5. **(Generalized Fourier series.)** Expand the function $f(u) = u^2$ on $[-1,1]$ in Legendre polynomials $P_0, P_1, P_2$, using orthogonality to find the coefficients. Verify by direct comparison that the expansion reproduces $u^2$ exactly with only these three terms.

---

## Sources

- Legendre, A.-M. "Recherches sur l'attraction des sphéroïdes homogènes." *Mémoires de Mathématiques et de Physique, présentés à l'Académie Royale des Sciences par divers savans* **10** (read 1782, published 1785). [Introduced $P_\ell(\cos\theta)$ as multipole coefficients of the Newtonian potential. The functions arrived from a physics problem.]
- Laplace, P.-S. *Traité de mécanique céleste* (1799–1825), and the 1782 memoir. [Laplace's equation on the sphere; the angular eigenvalue problem.]
- Thomson, W. (Lord Kelvin), and P. G. Tait. *Treatise on Natural Philosophy* (Oxford, 1867). [Coined "spherical harmonics" for Laplace's 1782 functions.]
- Bernoulli, D. Work at St. Petersburg (1732). [First appearance of a Bessel function: $J_0$ for the hanging chain.] Euler, L. (1764). [Integer-order $J_n$ and the series for the vibrating circular membrane.]
- Bessel, F. W. Systematization of the functions now bearing his name (1824), arising from planetary-perturbation calculations (Kepler's equation). [verify exact publication.]
- Hermite, C. Work on the Hermite polynomials (1864; also in his 1873 proof of the transcendence of $e$). [The polynomial factors of the quantum-oscillator eigenstates.]
- Sturm, J. C. F., and J. Liouville. Papers founding Sturm–Liouville theory, *Journal de Mathématiques Pures et Appliquées* vols. 1–2 (1836–1837; the joint memoir appears in vol. 2, 1837, pp. 220–233). [The unifying theorem: each special-function family is the orthogonal eigenfunction set of a self-adjoint second-order operator. Dates/venue confirmed (Lützen, *Arch. Hist. Exact Sci.*).]
- Wawro, M., and M. D. Caballero, et al. "Upper-division student difficulties with separation of variables." *Physical Review ST — Physics Education Research* **11**, 020131 (2015); arXiv:1507.03938. And "Students' difficulties with partial differential equations in quantum mechanics," *Physical Review PER* **16**, 020163 (2020). [Documents the separation-constant-sign and implicit-boundary-condition difficulties this chapter is designed around.] <!-- FACT-CHECK FLAG: UNVERIFIED — pedagogical citations not individually confirmed against authoritative record. See factchecks/07-special-functions-and-separation-of-variables-assertions.md -->
