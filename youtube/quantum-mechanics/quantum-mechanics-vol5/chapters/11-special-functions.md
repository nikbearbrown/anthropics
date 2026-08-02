# Module M-11 — Special Functions: Hermite, Legendre, Laguerre, Spherical Harmonics, Bessel

When we solve the quantum harmonic oscillator, the angular momentum problem, the hydrogen atom, and the scattering problem, we encounter four different families of functions — Hermite polynomials, Legendre polynomials and spherical harmonics, associated Laguerre polynomials, and spherical Bessel functions. A student working through the series encounters all four in succession and may conclude they are four unrelated collections of exotic formulas to memorize.

They are not. Every family is the set of orthogonal eigenfunctions of a self-adjoint second-order differential operator. One theorem — the Sturm-Liouville theorem — explains why all of them are orthogonal, why arbitrary functions expand in them, and why their eigenvalues are real. The same two-line proof applies to all four families; only the weight function changes.

The explicit polynomial coefficients are available in any reference table. What we focus on here is the structure — how each family arises, why it is orthogonal, and what its orthogonality weight is.

---

## The Unifying Structure: Sturm-Liouville Theory

Every special function family satisfies an equation of the form

$$\frac{d}{dx}\!\left[p(x)\frac{dy}{dx}\right] + q(x)\,y + \lambda\,w(x)\,y = 0,$$

the **Sturm-Liouville form**, where $p(x)$ and $w(x) > 0$ are real functions on $[a,b]$ and $\lambda$ is the eigenvalue. Define the operator $\hat{L}y = \frac{1}{w}[-(py')' - qy]$; it is **self-adjoint** with respect to the weighted inner product

$$\langle f, g\rangle = \int_a^b f^*(x)\,g(x)\,w(x)\,dx.$$

Self-adjointness means $\langle f,\hat{L}g\rangle = \langle\hat{L}f,g\rangle$, provided the boundary term $[p(f^*g' - (f^*)'g)]_a^b$ vanishes — which it does whenever the boundary or regularity conditions that quantize the eigenvalue are imposed.

**The orthogonality theorem.** For eigenfunctions $y_m$, $y_n$ with distinct eigenvalues $\lambda_m \neq \lambda_n$:

$$(\lambda_m - \lambda_n)\int_a^b y_m(x)\,y_n(x)\,w(x)\,dx = \bigl[p(y_m' y_n - y_m y_n')\bigr]_a^b = 0,$$

so $\int_a^b y_m\,y_n\,w\,dx = 0$. This is the same two lines of algebra every time; the boundary term vanishes for the same reason the eigenvalue is quantized. Every orthogonality relation in what follows is an instance of this single theorem.

**Generalized Fourier series.** Because each family is also complete, any sufficiently smooth function expands as

$$f(x) = \sum_n c_n\,y_n(x), \qquad c_n = \frac{\langle y_n, f\rangle}{\langle y_n, y_n\rangle} = \frac{\int f\,y_n\,w\,dx}{\int y_n^2\,w\,dx}.$$

We project onto each basis function in turn, using the weighted inner product. The ordinary Fourier series is the special case with a trigonometric basis; every special-function expansion is the same idea, adapted to the geometry of the problem.

![Sturm-Liouville taxonomy of seven special-function families](../images/11-special-functions-fig-01.png)
*Figure 11.1 — Sturm–Liouville taxonomy: all seven special-function families descend from the same self-adjoint operator structure, differentiated by their quantization mechanism (series termination, regularity at endpoint, or asymptotic boundary condition).*

<!-- → [TABLE: special function catalogue — columns: family name, defining ODE, interval and weight w, QM role; rows for each of the seven families (Hermite, Legendre, Associated Legendre, Spherical harmonics, Associated Laguerre, Spherical Bessel, Cylindrical Bessel); this is the reference table students will consult when identifying which family a new ODE belongs to] -->

---

## Hermite Polynomials — Harmonic Oscillator

The 1D harmonic oscillator in the dimensionless variable $\xi = \sqrt{m\omega/\hbar}\,x$ reads

$$-\frac{d^2\psi}{d\xi^2} + \xi^2\psi = \frac{2E}{\hbar\omega}\psi.$$

The asymptotic behavior as $|\xi|\to\infty$ is Gaussian, so we factor it out: writing $\psi(\xi) = H(\xi)\,e^{-\xi^2/2}$ and substituting gives **Hermite's equation** for $H$:

$$H'' - 2\xi H' + 2nH = 0, \qquad n = \frac{E}{\hbar\omega} - \frac{1}{2}.$$

The power-series solution to this equation has infinitely many terms in general. For $\psi$ to be normalizable, $H$ must be a polynomial — the series must terminate. This forces $n$ to be a non-negative integer:

$$\boxed{E_n = \hbar\omega\!\left(n+\tfrac{1}{2}\right), \qquad n = 0,1,2,\ldots}$$

The evenly spaced energy ladder, including zero-point energy $E_0 = \tfrac{1}{2}\hbar\omega$, follows from the termination condition alone.

**First few polynomials** (physicist's convention, leading coefficient $2^n$):

$$H_0 = 1, \quad H_1 = 2\xi, \quad H_2 = 4\xi^2 - 2, \quad H_3 = 8\xi^3 - 12\xi.$$

**Full eigenstates:** $\psi_n(x) = N_n H_n(\xi)e^{-\xi^2/2}$ with $N_n = (m\omega/\pi\hbar)^{1/4}/\sqrt{2^n n!}$.

**Orthogonality** (weight $e^{-\xi^2}$, the Sturm-Liouville weight for this family):

$$\int_{-\infty}^\infty H_m(\xi)\,H_n(\xi)\,e^{-\xi^2}\,d\xi = \sqrt{\pi}\,2^n\,n!\,\delta_{mn}.$$

**Recurrence relation** (the practical tool for matrix elements):

$$H_{n+1}(\xi) = 2\xi\,H_n(\xi) - 2n\,H_{n-1}(\xi).$$

Combined with $\xi H_n = \tfrac{1}{2}H_{n+1} + nH_{n-1}$, this allows us to compute $\langle n|\hat{x}|n'\rangle$ and $\langle n|\hat{p}|n'\rangle$ algebraically, without evaluating a Gaussian integral.

![Hermite polynomial eigenstates for n=0 to 3 showing node count](../images/11-special-functions-fig-02.png)
*Figure 11.2 — Harmonic oscillator eigenstates for $n = 0$ to $3$: each wavefunction has exactly $n$ nodes, with positive and negative lobes enveloped by the Gaussian factor $e^{-\xi^2/2}$.*

One convention note: the physicist's $H_n$ has leading coefficient $2^n$ and weight $e^{-\xi^2}$. The probabilist's $\text{He}_n$ has leading coefficient 1 and weight $e^{-\xi^2/2}$. QM uniformly uses the physicist's convention. To verify, check $H_1$: the physicist's convention gives $2\xi$; the probabilist's gives $\xi$. Using the wrong convention changes normalization constants by powers of 2.

---

## Legendre Polynomials and Spherical Harmonics — Angular Momentum

Separating the spherical Laplacian produces the polar equation. With $u = \cos\theta$:

$$\frac{d}{du}\!\left[(1-u^2)\frac{dP}{du}\right] + \ell(\ell+1)\,P = 0.$$

This is the **Legendre equation**. Requiring finiteness at $u = \pm1$ (the poles $\theta = 0,\pi$) forces $\ell\in\{0,1,2,\ldots\}$ and gives the **Legendre polynomials**:

$$P_0(u) = 1, \quad P_1(u) = u, \quad P_2(u) = \tfrac{1}{2}(3u^2-1), \quad P_3(u) = \tfrac{1}{2}(5u^3-3u).$$

**Orthogonality** (weight $w = 1$):

$$\int_{-1}^1 P_m(u)\,P_n(u)\,du = \frac{2}{2n+1}\,\delta_{mn}.$$

**Associated Legendre functions** arise for non-axisymmetric solutions ($m\neq0$):

$$P_\ell^m(u) = (-1)^m(1-u^2)^{m/2}\frac{d^m}{du^m}P_\ell(u), \qquad |m|\leq\ell.$$

The constraint $|m|\leq\ell$ comes from combining the regularity condition at the poles with the azimuthal single-valuedness requirement.

**Spherical harmonics** combine the polar and azimuthal parts:

$$Y_{\ell m}(\theta,\phi) = \sqrt{\frac{(2\ell+1)}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}\,P_\ell^{|m|}(\cos\theta)\,e^{im\phi}.$$

**Orthonormality on the sphere** (weight $w = \sin\theta$, the spherical area element):

$$\int_0^{2\pi}\!\int_0^\pi Y_{\ell'm'}^*\,Y_{\ell m}\,\sin\theta\,d\theta\,d\phi = \delta_{\ell\ell'}\delta_{mm'}.$$

**Key** $\text{low-}\ell$ **harmonics:**

$$Y_{00} = \frac{1}{\sqrt{4\pi}}, \quad Y_{10} = \sqrt{\frac{3}{4\pi}}\cos\theta, \quad Y_{1,\pm1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}.$$

$Y_{00}$ is spherically symmetric (the $s$-orbital shape). $Y_{10}$ corresponds to the $p_z$ lobe. Linear combinations of $Y_{1,\pm1}$ give $p_x$ and $p_y$.

**Angular momentum eigenvalue equations:**

$$\hat{L}^2 Y_{\ell m} = \hbar^2\ell(\ell+1)Y_{\ell m}, \qquad \hat{L}_z Y_{\ell m} = \hbar m\,Y_{\ell m}.$$

The separation constant $\ell(\ell+1)$ from the PDE is the eigenvalue of $\hat{L}^2$. The quantum number $m$ from the azimuthal separation is the eigenvalue of $\hat{L}_z$. The PDE separation and the operator eigenvalue problem are the same thing, viewed from two angles.

The $(-1)^m$ factor in the associated Legendre functions for $m > 0$ is the **Condon-Shortley convention**, standard in physics. [verify: Condon & Shortley, The Theory of Atomic Spectra, 1935] Some mathematical tables omit it. Mixing conventions produces incorrect phases in angular momentum matrix elements and selection rules.

---

## Associated Laguerre Polynomials — Hydrogen Radial Wavefunctions

With the angular part separated, the hydrogen radial equation for $R(r)$ (reduced mass $\mu$, Bohr radius $a_0$) has, after factoring out $\rho^\ell$ (regular at origin) and $e^{-\rho/2}$ (normalizable at infinity), the remaining factor satisfying the **associated Laguerre equation**:

$$\rho\frac{d^2L}{d\rho^2} + (2\ell+2-\rho)\frac{dL}{d\rho} + (n-\ell-1)L = 0,$$

where $\rho = 2r/(na_0)$.

For the series to terminate — so $R$ is normalizable — the quantity $n-\ell-1$ must be a non-negative integer (the radial quantum number $n_r = n-\ell-1\geq0$). This forces $n = 1,2,3,\ldots$ and $\ell = 0,1,\ldots,n-1$. The hydrogen energy spectrum:

$$\boxed{E_n = -\frac{13.6\;\text{eV}}{n^2}, \qquad n = 1,2,3,\ldots}$$

**Orthogonality** (weight $w = r^2$, the radial part of the spherical volume element):

$$\int_0^\infty R_{n\ell}(r)\,R_{n'\ell}(r)\,r^2\,dr = \delta_{nn'}.$$

**Degeneracy.** For fixed $n$, $\ell$ runs from 0 to $n-1$, and $m$ runs from $-\ell$ to $+\ell$. The total spatial states at energy $E_n$: $\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$, doubled by spin: $2n^2$ states per level. Every quantum number, and the degeneracy count, follows from the three separation conditions.

**First two explicit radial functions:**

$$R_{10} = 2\left(\frac{1}{a_0}\right)^{3/2}e^{-r/a_0}, \quad R_{20} = 2\left(\frac{1}{2a_0}\right)^{3/2}\!\!\left(1-\frac{r}{2a_0}\right)e^{-r/2a_0}.$$

$R_{10}$ has no radial nodes; $R_{20}$ has one node at $r = 2a_0$. In general, $R_{n\ell}$ has $n-\ell-1$ radial nodes.

---

## Spherical Bessel Functions — Scattering

For a free particle (or a particle outside a finite-range potential, where $V = 0$), the radial Schrödinger equation in spherical coordinates, with $u = rR$, is

$$\frac{d^2u}{dr^2} + \left[k^2 - \frac{\ell(\ell+1)}{r^2}\right]u = 0.$$

The two linearly independent solutions are the **spherical Bessel function** $j_\ell(x)$ (regular at $r = 0$) and the **spherical Neumann function** $n_\ell(x)$ (singular at $r = 0$). They are Bessel functions of half-integer order:

$$j_\ell(x) = \sqrt{\frac{\pi}{2x}}\,J_{\ell+1/2}(x).$$

**First few:**

$$j_0(x) = \frac{\sin x}{x}, \qquad j_1(x) = \frac{\sin x}{x^2} - \frac{\cos x}{x}, \qquad n_0(x) = -\frac{\cos x}{x}.$$

**Asymptotic forms** ($kr\to\infty$):

$$j_\ell(kr) \overset{kr\to\infty}{\longrightarrow} \frac{\sin(kr-\ell\pi/2)}{kr}, \qquad n_\ell(kr) \overset{kr\to\infty}{\longrightarrow} -\frac{\cos(kr-\ell\pi/2)}{kr}.$$

Outside the interaction region, the general radial solution is $j_\ell\cos\delta_\ell - n_\ell\sin\delta_\ell$. The **phase shift** $\delta_\ell$ encodes how much the potential has displaced the asymptotic wave from the free-particle solution $j_\ell$. The total cross section:

$$\sigma = \frac{4\pi}{k^2}\sum_\ell(2\ell+1)\sin^2\delta_\ell.$$

For a hard sphere of radius $a$: $\tan\delta_\ell = j_\ell(ka)/n_\ell(ka)$, with the $\ell = 0$ phase shift dominating at low energy ($ka\ll1$). We use $j_\ell$ because the free particle solution must be regular at the origin; $n_\ell$ appears in scattering because the scatterer occupies the interior and both solutions are allowed outside it.

**Cylindrical Bessel functions** $J_m(x)$ arise in cylindrical-symmetry problems (waveguides, optical fibers, quantum wires). For a hard-wall cylinder of radius $a$, the condition $J_m(ka) = 0$ quantizes the allowed modes. The factor 1.22 in the Rayleigh resolution limit $\theta_\text{min} = 1.22\lambda/D$ is $j_{1,1}/\pi$ where $j_{1,1}\approx3.832$ is the first zero of $J_1$.

---

## Worked Example: Which Special Function and Why

The diagnostic logic follows five steps: (1) choose the coordinate system that makes the potential or boundary conditions separable; (2) apply the product ansatz; (3) recognize the ODE by its form; (4) apply the regularity or termination condition that quantizes the eigenvalue; (5) the special function is the name of the regular solution.

<!-- → [TABLE: worked example table — columns: QM system, coordinate system, separated ODE, quantization mechanism, special function; rows: (1) 1D harmonic oscillator, Cartesian, Hermite equation, series termination (normalizability), H_n(ξ); (2) any central potential angular, spherical (θ,φ), associated Legendre, finiteness at poles, Y_ℓm; (3) hydrogen radial, spherical (r), associated Laguerre, series termination, L^(2ℓ+1)_(n-ℓ-1)(ρ); (4) free particle or scattering radial, spherical (r), spherical Bessel, regularity at origin or asymptotic form, j_ℓ(kr) and n_ℓ(kr); (5) cylindrical geometry, cylindrical (ρ), Bessel equation, zeros at wall J_m(ka)=0, J_m(kρ)] -->

**The ground state of the harmonic oscillator.** With $n = 0$, $H_0(\xi) = 1$ — a constant — so $\psi_0\propto e^{-\xi^2/2}$: a pure Gaussian with no nodes. Energy $E_0 = \tfrac{1}{2}\hbar\omega$. The zero-point energy is nonzero because the termination condition's minimum is $n = 0$, not $n = -1$.

**Normalization of** $\psi_0$. With $\psi_0 = N_0 e^{-\xi^2/2}$ and $d\xi = \sqrt{m\omega/\hbar}\,dx$:

$$N_0^2\sqrt{\frac{\hbar}{m\omega}}\int_{-\infty}^\infty e^{-\xi^2}\,d\xi = N_0^2\sqrt{\frac{\hbar}{m\omega}}\cdot\sqrt{\pi} = 1 \implies N_0 = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}.$$

The Gaussian integral $\int e^{-\xi^2}\,d\xi = \sqrt{\pi}$ from M-02 is the only tool needed. This computation template — factor out the Gaussian, recognize the resulting integral, apply the result — repeats for every $n$ via the Hermite orthogonality relation.

---

## Quick Practice

1. **Identification.** A particle is confined to the surface of a unit sphere (rigid rotor). The Hamiltonian is $\hat{H} = \hat{L}^2/(2I)$. Write down the energy eigenvalues and eigenfunctions without solving an ODE — by recognizing which special functions apply and why.

2. **Orthogonality check.** Use the orthogonality of Legendre polynomials to compute $\int_{-1}^1 P_2(u)\cdot u\,du$. First express $u = P_1(u)$, then apply $\int_{-1}^1 P_m P_n\,du = \tfrac{2}{2n+1}\delta_{mn}$.

3. **Hydrogen degeneracy.** List all quantum states $(n,\ell,m)$ with $n = 3$. Count them (excluding spin) and verify the count equals $n^2 = 9$. Identify which subshell ($3s$, $3p$, $3d$) each set belongs to and state how many radial nodes each $R_{3\ell}$ has.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the Sturm-Liouville orthogonality argument.*
   The Legendre equation $\frac{d}{du}[(1-u^2)P'] + \ell(\ell+1)P = 0$ is in Sturm-Liouville form with $p(u) = 1-u^2$, $q = 0$, $w = 1$. (a) Identify $p(u)$ and evaluate $p(\pm1)$. (b) The orthogonality proof requires the boundary term $[p(y_m'y_n - y_m y_n')]_{-1}^{+1}$ to vanish. Show that it vanishes because $p(\pm1) = 0$, without knowing the explicit polynomials. (c) Write out the orthogonality integral for $P_2$ and $P_3$ and verify it is zero using the explicit formulas $P_2 = \tfrac{1}{2}(3u^2-1)$ and $P_3 = \tfrac{1}{2}(5u^3-3u)$.
   *Tests: reading the boundary term directly from p(±1); connecting the vanishing boundary term to orthogonality; verifying with explicit polynomials.*

2. *Difficulty: Warm-up — tests Hermite polynomial identification and normalization.*
   (a) Verify that $H_2(\xi) = 4\xi^2 - 2$ satisfies Hermite's equation $H'' - 2\xi H' + 4H = 0$ (with $n = 2$). (b) The eigenfunction is $\psi_2(\xi) \propto H_2(\xi)e^{-\xi^2/2}$; sketch its shape and count its nodes. (c) The orthogonality of $H_0 = 1$ and $H_2$ requires $\int_{-\infty}^\infty (4\xi^2 - 2)e^{-\xi^2}\,d\xi = 0$. Verify this directly using $\int x^2 e^{-x^2}dx = \sqrt{\pi}/2$ and $\int e^{-x^2}dx = \sqrt{\pi}$.
   *Tests: verifying a Hermite polynomial satisfies the ODE; node counting; verifying orthogonality by direct integral.*

3. *Difficulty: Warm-up — tests spherical harmonic identification.*
   (a) Verify that $Y_{00} = 1/\sqrt{4\pi}$ is normalized: compute $\int|Y_{00}|^2\sin\theta\,d\theta\,d\phi$ explicitly. (b) Verify that $\hat{L}_z Y_{10} = 0$: use $\hat{L}_z = -i\hbar\partial/\partial\phi$ and $Y_{10} = \sqrt{3/4\pi}\cos\theta$. (c) The eigenvalue equation $\hat{L}^2 Y_{10} = \hbar^2\ell(\ell+1)Y_{10}$ with $\ell = 1$ gives $2\hbar^2 Y_{10}$. What is the quantum number $m$ for $Y_{10}$, and what does $\hat{L}_z Y_{10} = \hbar m Y_{10}$ give?
   *Tests: normalization of a spherical harmonic; direct application of angular momentum operators; identifying quantum numbers.*

**Application**

4. *Difficulty: Application — harmonic oscillator matrix elements via recurrence.*
   Using the recurrence relation $\xi H_n = \tfrac{1}{2}H_{n+1} + nH_{n-1}$ and the orthogonality $\int H_m H_n e^{-\xi^2}d\xi = \sqrt{\pi}2^n n!\delta_{mn}$: (a) compute the matrix element $\langle n|\hat\xi|n'\rangle = N_n N_{n'}\int\xi H_n H_{n'}e^{-\xi^2}d\xi$ and show the only nonzero cases are $n' = n\pm1$; (b) find the explicit values $\langle n|\hat\xi|n+1\rangle$ and $\langle n|\hat\xi|n-1\rangle$; (c) identify the selection rule $\Delta n = \pm1$ for electric dipole transitions and explain its physical meaning.
   *Tests: using the recurrence to evaluate matrix elements without direct integration; selection rules from orthogonality.*

5. *Difficulty: Application — hydrogen quantum numbers and degeneracy.*
   (a) List all quantum states $(n,\ell,m)$ with $n = 4$ (excluding spin). Count them and verify the count is $n^2 = 16$. (b) For each subshell ($4s$, $4p$, $4d$, $4f$), state the number of radial nodes in $R_{4\ell}$ and the number of angular nodes (nodal planes or cones) in $|Y_{\ell m}|^2$. (c) What is the total number of quantum states (including spin) at the $n = 4$ level? What would change if the Hamiltonian broke the $\ell$-degeneracy (as fine structure does)?
   *Tests: systematic enumeration of hydrogen quantum numbers; node counting for radial and angular parts; understanding the source of degeneracy.*

6. *Difficulty: Application — scattering phase shift for a hard sphere.*
   For a hard sphere of radius $a$ (potential infinite for $r < a$, zero for $r > a$), the radial wavefunction for $r > a$ is $R_\ell(r) \propto j_\ell(kr)\cos\delta_\ell - n_\ell(kr)\sin\delta_\ell$. (a) The boundary condition is $R_\ell(a) = 0$; use this to show $\tan\delta_\ell = j_\ell(ka)/n_\ell(ka)$. (b) For $\ell = 0$ and $ka\ll1$: use $j_0(x) = \sin x/x \approx 1 - x^2/6$ and $n_0(x) = -\cos x/x \approx -1/x$ to show $\tan\delta_0 \approx -ka$ and $\delta_0 \approx -ka$. (c) Compute the $\ell = 0$ partial cross-section $\sigma_0 = (4\pi/k^2)\sin^2\delta_0$ in the low-energy limit and compare to the geometric cross-section $\pi a^2$.
   *Tests: applying the hard-sphere boundary condition; low-energy expansion of spherical Bessel functions; the low-energy cross-section exceeding the geometric value.*

**Synthesis**

7. *Difficulty: Synthesis — Sturm-Liouville unification across two families.*
   (a) Write the Hermite equation $H'' - 2\xi H' + 2nH = 0$ in Sturm-Liouville form by identifying $p(\xi)$, $q(\xi)$, $w(\xi)$, and $\lambda$. (Hint: multiply through by $e^{-\xi^2}$ and rewrite the first two terms as $(e^{-\xi^2}H')'$.) (b) Verify the boundary term $[p(f^*g' - (f^*)'g)]_{-\infty}^{+\infty}$ vanishes for Hermite polynomial eigenfunctions using the weight $e^{-\xi^2}$. (c) Write the Legendre equation in Sturm-Liouville form (already standard: $p = 1-u^2$, $w = 1$) and identify $\lambda$. (d) Both families have $\lambda$ equal to a non-negative integer — for Hermite it is $2n$ and for Legendre it is $\ell(\ell+1)$. Identify the quantization mechanism in each case (termination vs. regularity at the boundary) and explain why they are physically different even though both produce discrete spectra.
   *Tests: converting a non-standard ODE to Sturm-Liouville form; comparing quantization mechanisms across families.*

8. *Difficulty: Synthesis — hydrogen wavefunction structure.*
   The hydrogen ground state is $\psi_{100}(r,\theta,\phi) = R_{10}(r)Y_{00}(\theta,\phi)$. (a) Write out the full explicit wavefunction and verify it is normalized: $\int|\psi_{100}|^2 r^2\sin\theta\,dr\,d\theta\,d\phi = 1$ (the angular integral gives 1 by normalization of $Y_{00}$; the radial integral uses $\int_0^\infty r^2 e^{-2r/a_0}dr = a_0^3/4$). (b) Compute the expectation value $\langle r\rangle = \int r|\psi_{100}|^2 r^2\sin\theta\,dr\,d\theta\,d\phi$ and show the result is $3a_0/2$. (c) Show that the most probable radius (where $r^2|R_{10}|^2$ peaks) is $a_0$, and explain why this differs from $\langle r\rangle$.
   *Tests: full normalization integral split into radial and angular parts; expectation value of r; distinction between most probable radius and mean radius.*

**Challenge**

9. *Difficulty: Challenge — completeness and the Sturm-Liouville expansion.*
   The associated Laguerre polynomials $L_n^k(\rho)$ satisfy the orthogonality relation $\int_0^\infty L_m^k(\rho)L_n^k(\rho)\rho^k e^{-\rho}\,d\rho = \frac{(n+k)!}{n!}\delta_{mn}$. The full set $\{L_n^k\}_{n=0}^\infty$ for fixed $k$ is complete on $[0,\infty)$ with weight $\rho^k e^{-\rho}$. (a) Write out the first three associated Laguerre polynomials $L_0^1$, $L_1^1$, $L_2^1$ using the formula $L_n^k(\rho) = \sum_{j=0}^n (-1)^j\binom{n+k}{n-j}\rho^j/j!$. (b) Expand the function $f(\rho) = \rho^2$ on $[0,\infty)$ in terms of $\{L_n^1\}$ by computing the first three coefficients $c_n = \int_0^\infty f(\rho)L_n^1(\rho)\rho e^{-\rho}\,d\rho / \int_0^\infty [L_n^1(\rho)]^2\rho e^{-\rho}\,d\rho$. (c) Verify that the partial sum $c_0 L_0^1 + c_1 L_1^1 + c_2 L_2^1$ reproduces $\rho^2$ exactly (not just approximately) and explain why only finitely many terms are needed.
   *Tests: computing Laguerre polynomials explicitly; carrying out a Sturm-Liouville expansion by projection; recognizing that polynomial functions expand exactly in finitely many polynomial basis functions.*

---

## References

Legendre, A.-M. (1785). Recherches sur l'attraction des sphéroïdes homogènes. *Mémoires de Mathématiques et de Physique*, 10.

Hermite, C. (1864). [Polynomials arising in the study of the harmonic oscillator eigenstates; also appears in his 1873 proof of the transcendence of $e$.] [verify exact 1864 publication]

Bessel, F. W. (1824). [Systematization of the Bessel functions from planetary-perturbation calculations.] [verify exact publication]

Sturm, J. C. F., & Liouville, J. (1836–1837). Papers founding Sturm-Liouville theory. *Journal de Mathématiques Pures et Appliquées*, 1–2.

Condon, E. U., & Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press.

Griffiths, D. J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Section 4.2.

Abramowitz, M., & Stegun, I. A. (1964). *Handbook of Mathematical Functions*. National Bureau of Standards.
