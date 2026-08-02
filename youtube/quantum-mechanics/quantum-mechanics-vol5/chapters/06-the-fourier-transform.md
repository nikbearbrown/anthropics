# Module M-06 — The Fourier Transform
*Refresher for QM chapters: I·8 (wave packets), III·5 (transitions), III·8 (Born approximation)*

In Chapter I·8 we build a wave packet by superposing plane waves with a momentum-space envelope — that superposition is the inverse Fourier transform. In Chapter III·8, the Born approximation writes the scattering amplitude as $\int V(\mathbf{r})\,e^{i\mathbf{q}\cdot\mathbf{r}}\,d^3r$ — the Fourier transform of the potential evaluated at the momentum transfer. These two operations are the same. Recognizing them as such makes both chapters a single calculation instead of two separate formulas to memorize.

---

## The Transform as the $L \to \infty$ Limit of the Fourier Series

Module M-05 expanded a periodic function of period $L$ in complex Fourier modes:

$$f(x) = \sum_{n=-\infty}^{\infty} c_n\, e^{ik_n x}, \qquad c_n = \frac{1}{L}\int_{-L/2}^{L/2} f(x)\, e^{-ik_n x}\,dx, \qquad k_n = \frac{2\pi n}{L}.$$

The spectrum is a discrete comb of wavenumbers spaced $\Delta k = 2\pi/L$ apart. As the period grows without bound, $L \to \infty$, the spacing $\Delta k \to 0$, the comb fills in, and the sum over $n$ becomes an integral over a continuous variable $k$. Substituting $1/L = \Delta k/2\pi$ and taking the limit defines the Fourier transform pair:

$$\boxed{\tilde f(k) = \int_{-\infty}^{\infty} f(x)\, e^{-ikx}\,dx} \qquad \text{(forward: position $\to$ wavenumber)}$$

$$\boxed{f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \tilde f(k)\, e^{ikx}\,dk} \qquad \text{(inverse: wavenumber $\to$ position)}$$

The Fourier transform is the Fourier series taken to continuous frequency. The function $\tilde f(k)$ is the continuous spectrum of $f$ — it describes how much of each pure wave $e^{ikx}$ the function contains.

![Three stacked panels showing discrete Fourier series comb densifying into continuous Fourier transform](../images/06-the-fourier-transform-fig-01.png)
*Figure 6.1 — Fourier series to Fourier transform as L → ∞: (top) sparse discrete comb at large spacing Δk; (middle) denser comb at Δk/2; (bottom) smooth continuous envelope with faint ghost comb, illustrating the limit in which the sum becomes an integral.*

---

## The Quantum Convention: Position and Momentum

In quantum mechanics the natural variable is momentum $p = \hbar k$, and the conventional choice is the symmetric split with $1/\sqrt{2\pi\hbar}$ on each side:

$$\tilde\psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty} \psi(x)\, e^{-ipx/\hbar}\,dx, \qquad \psi(x) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty} \tilde\psi(p)\, e^{ipx/\hbar}\,dp.$$

This is the change of basis between position and momentum eigenstates. Inserting the continuous resolution of the identity $\int |x\rangle\langle x|\,dx = \hat I$ into $\langle p|\psi\rangle$ gives exactly the Fourier integral:

$$\tilde\psi(p) = \langle p|\psi\rangle = \int \langle p|x\rangle\langle x|\psi\rangle\,dx = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\,\psi(x)\,dx,$$

where $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$ is the momentum eigenstate in position representation — a pure wave with wavenumber $k = p/\hbar$. The Fourier transform is not a computational trick layered on top of the quantum formalism: it is the inner product between position and momentum eigenstates, with the plane wave as the overlap kernel.

**Convention warning.** The factor of $2\pi$ can be placed entirely on the inverse transform (the mathematical convention above), split symmetrically as $1/\sqrt{2\pi}$ or $1/\sqrt{2\pi\hbar}$ (QM convention), or removed by using ordinary frequency $\nu$ with $e^{-2\pi i\nu x}$. The sign of the exponent can also vary between fields. No convention is more correct; inconsistency between a QM text, a math reference, and a physics paper is the source of most mysterious factors of $2\pi$ or $\hbar$. We should write the convention explicitly every time.

---

## Plancherel: The Transform Preserves Probability

**Plancherel's theorem:** $\int|f(x)|^2\,dx = \frac{1}{2\pi}\int|\tilde f(k)|^2\,dk$. In the symmetric QM convention, a normalized position-space wavefunction $\int|\psi(x)|^2\,dx = 1$ gives a normalized momentum-space wavefunction $\int|\tilde\psi(p)|^2\,dp = 1$. Total probability is the same in either basis. This is the analysis-level statement of the fact that a unitary change of basis preserves norms.

---

## The Convolution Theorem

The convolution of two functions smears one with the other:

$$(f * g)(x) = \int_{-\infty}^{\infty} f(x')\,g(x - x')\,dx'.$$

The convolution theorem states that this operation becomes simple multiplication in Fourier space:

$$\boxed{\widetilde{f * g}(k) = \tilde f(k)\cdot\tilde g(k).}$$

Proof: substitute $g(x - x')$, change variable $u = x - x'$, and the two integrals separate into $\tilde f(k)\cdot\tilde g(k)$. Equivalently (by swapping roles): multiplication in real space is convolution in Fourier space.

In quantum mechanics: when a perturbation is a product of two factors — a spatial envelope times an oscillation — the transition matrix element is the convolution of their transforms. In scattering, the double-slit amplitude is the single-slit transform times the two-delta transform; the two-slit structure is a convolution, so the diffraction pattern is a product.

---

## The Bandwidth Relation and the Uncertainty Principle

We define the rms spatial width $\Delta x$ of $|f|^2$ and the rms spectral width $\Delta k$ of $|\tilde f|^2$. For any function:

$$\boxed{\Delta x\,\Delta k \geq \tfrac{1}{2}.}$$

This is a theorem about any Fourier pair, with no quantum mechanics involved. The scaling property $f(x) \mapsto f(ax)$ compresses the function by factor $a$ while stretching its transform by the same factor — squeeze in $x$ and the spectrum spreads in $k$.

Rescaling to momentum via $p = \hbar k$ converts this to $\Delta x\,\Delta p \geq \hbar/2$. There are two routes to this inequality, and it is worth keeping them distinct.

**Fourier route:** $\Delta x\,\Delta k \geq \tfrac{1}{2}$ (pure mathematics of transform pairs) $\overset{p = \hbar k}{\longrightarrow}$ $\Delta x\,\Delta p \geq \tfrac{\hbar}{2}$.

**Robertson route:** For any two observables with commutator $[\hat A, \hat B]$: $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat A,\hat B]\rangle|$. For $[\hat x, \hat p] = i\hbar$: $\sigma_x\sigma_p \geq \tfrac{\hbar}{2}$.

Both reproduce $\sigma_x\sigma_p \geq \hbar/2$, but they are not the same statement. The energy–time relation $\Delta E\,\Delta t \sim \hbar$ is the Fourier route applied to time and frequency — not the Robertson route, because time is not an operator in standard quantum mechanics. Treating $\Delta E\,\Delta t$ as a Robertson commutator is an error that Chapter III·5 can tempt students into.

---

## The Gaussian: Minimum Uncertainty and Its Own Transform

The Gaussian $f(x) = e^{-x^2/2a^2}$ transforms to another Gaussian:

$$\tilde f(k) = a\sqrt{2\pi}\,e^{-a^2 k^2/2}.$$

The proof: complete the square in the exponent of $\int e^{-x^2/2a^2}e^{-ikx}\,dx$, then use the standard Gaussian integral $\int e^{-u^2/2a^2}\,du = a\sqrt{2\pi}$.

The Gaussian is the unique shape that saturates the bandwidth bound: $\Delta x\,\Delta k = \tfrac{1}{2}$ exactly. For the normalized QM Gaussian $\psi(x) = (\pi a^2)^{-1/4}e^{-x^2/2a^2}$, the position width is $\Delta x = a/\sqrt{2}$ and the momentum width is $\Delta p = \hbar/(a\sqrt{2})$, giving $\Delta x\,\Delta p = \hbar/2$. This is why the Gaussian wave packet is the **minimum-uncertainty state** — the most classical-like quantum state, with position and momentum uncertainties balanced as tightly as nature permits. Small $a$ (localized in $x$) forces large $\Delta p$, and vice versa, in exact reciprocal proportion.

![2×2 grid: narrow x-space Gaussian paired with wide p-space Gaussian, and wide x-space Gaussian paired with narrow p-space Gaussian](../images/06-the-fourier-transform-fig-02.png)
*Figure 6.2 — Position–momentum trade-off: (top-left) narrow |ψ(x)|² and (bottom-left) correspondingly wide |φ̃(p)|² for a localized state; (top-right) wide |ψ(x)|² and (bottom-right) narrow |φ̃(p)|² for a delocalized state — Fourier reciprocity enforces the uncertainty product.*

---

## The Dirac Delta: The Continuous Kronecker

To handle continuous bases we need an object that selects a single point. The Dirac delta is defined by its action under integration:

$$\int_{-\infty}^{\infty} \delta(x - x_0)\,f(x)\,dx = f(x_0).$$

It is not an ordinary function — it is a distribution in Schwartz's sense — and manipulating it outside an integral leads to undefined results. It arises as the Fourier transform of a constant:

$$\delta(x - x') = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ik(x - x')}\,dk.$$

This is the continuous analogue of the Kronecker delta $\delta_{mn}$, and it is what makes the continuous resolution of the identity work: $\langle x|x'\rangle = \delta(x - x')$ is the continuous-basis version of $\langle e_m|e_n\rangle = \delta_{mn}$.

---

## Worked Example: Gaussian Wave Packet from Position to Momentum Space

We take the normalized Gaussian $\psi(x) = (\pi a^2)^{-1/4}e^{-x^2/2a^2}$ (centered at $x=0$, zero mean momentum). The momentum wavefunction is:

$$\tilde\psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty} (\pi a^2)^{-1/4} e^{-x^2/2a^2}\, e^{-ipx/\hbar}\,dx.$$

Completing the square: $-x^2/2a^2 - ipx/\hbar = -\frac{1}{2a^2}(x + ipa^2/\hbar)^2 - \frac{p^2 a^2}{2\hbar^2}$. The completed-square integral is a standard Gaussian shifted to a complex center (the shift does not affect the value for analytic functions — justified by contour deformation):

$$\tilde\psi(p) = \left(\frac{a^2}{\pi\hbar^2}\right)^{1/4}\exp\!\left(-\frac{a^2 p^2}{2\hbar^2}\right).$$

This is a Gaussian in $p$ with width $\Delta p = \hbar/(a\sqrt{2})$. Position width: $\Delta x = a/\sqrt{2}$. Product: $\Delta x\,\Delta p = \hbar/2$ — saturation.

Large $a$: the particle is spread out in space with a narrow, well-defined momentum. Small $a$: localized in space, wide momentum distribution. The Fourier transform enforces this trade-off automatically.

---

## The 3D Transform and Born Scattering

The Fourier transform generalizes to three dimensions:

$$\tilde f(\mathbf{k}) = \int f(\mathbf{r})\, e^{-i\mathbf{k}\cdot\mathbf{r}}\,d^3r, \qquad f(\mathbf{r}) = \frac{1}{(2\pi)^3}\int \tilde f(\mathbf{k})\, e^{i\mathbf{k}\cdot\mathbf{r}}\,d^3k.$$

For a spherically symmetric potential $V(r)$, choosing $\hat z \parallel \mathbf{q}$ (momentum transfer $\mathbf{q} = \mathbf{k}_i - \mathbf{k}_f$) and integrating over angles:

$$\tilde V(q) = \frac{4\pi}{q}\int_0^\infty V(r)\,r\sin(qr)\,dr,$$

reducing a 3D transform to a 1D integral.

The first Born approximation for the scattering amplitude is:

$$f(\theta) = -\frac{m}{2\pi\hbar^2}\int V(\mathbf{r})\, e^{i\mathbf{q}\cdot\mathbf{r}}\,d^3r = -\frac{m}{2\pi\hbar^2}\,\tilde V(\mathbf{q}),$$

where $q = 2k\sin(\theta/2)$ and $k = |\mathbf{k}_i| = |\mathbf{k}_f|$ (elastic scattering). The Born scattering amplitude is the Fourier transform of the potential evaluated at the momentum transfer. For the Yukawa potential $V(r) = V_0 e^{-r/a}/r$, its 3D transform is $\tilde V(q) = 4\pi V_0/(q^2 + a^{-2})$ — a Lorentzian in $q$ — giving the screened-Coulomb differential cross-section directly.

---

## Where These Methods Appear in the Quantum Series

**Position and momentum as conjugate Fourier variables (I·8).** A free-particle wave packet is built by superposing momentum eigenstates with weight $\tilde\psi(p)$:

$$\psi(x, 0) = \frac{1}{\sqrt{2\pi\hbar}}\int \tilde\psi(p)\, e^{ipx/\hbar}\,dp.$$

Time evolution is simplest in momentum space: each component $\tilde\psi(p)$ acquires phase $e^{-ip^2 t/2m\hbar}$ (since $E = p^2/2m$). For a Gaussian $\tilde\psi(p)$, completing the square yields the time-evolved $\psi(x,t)$ — a Gaussian that spreads: $\Delta x(t) = \Delta x(0)\sqrt{1 + (t\hbar/m\Delta x(0)^2)^2}$.

Wave packet spreading follows from the Fourier bandwidth relation: a narrow $\Delta x$ at $t=0$ requires a wide $\Delta p$, and different momentum components travel at different speeds $v = p/m$, so the packet broadens. This is kinematics plus Fourier, not a new quantum principle.

![Three-panel figure showing Gaussian wave packet broadening at successive times](../images/06-the-fourier-transform-fig-03.png)
*Figure 6.3 — Wave packet spreading in time: three snapshots at t₁ < t₂ < t₃ showing the Gaussian broadening and flattening while the center advances at constant group velocity, with width brackets growing at each step.*

The group velocity of the packet, $v_g = d\omega/dk|_{k_0}$, gives the speed of the packet center. For a quantum particle $\omega = \hbar k^2/2m$, so $v_g = \hbar k_0/m = p_0/m$ (the classical particle velocity) while the phase velocity $v_\phi = \hbar k_0/2m = p_0/2m$ — half the classical speed. The packet center moves classically; the individual wave crests do not.

**Transitions and the time–frequency bandwidth (III·5).** Time-dependent perturbation theory computes transition amplitudes as:

$$c_{f \leftarrow i}(t) \propto \int_0^t \langle f|\hat V(t')| i\rangle\, e^{i\omega_{fi} t'}\,dt',$$

where $\omega_{fi} = (E_f - E_i)/\hbar$. For a perturbation that turns on at $t = 0$ and runs for time $T$, the integral is the Fourier transform of the matrix element as a function of time, evaluated at the transition frequency $\omega_{fi}$. The transition probability is large when the Fourier spectrum of the perturbation has significant weight at $\omega_{fi}$ — energy conservation stated in Fourier language.

For a perturbation of duration $T$, its Fourier spectrum has width $\Delta\omega \sim 1/T$ (the bandwidth relation in time–frequency). This gives $\Delta E \sim \hbar/T$ — the energy–time uncertainty relation as a Fourier theorem, not a Robertson commutator. The longer the interaction lasts, the more sharply defined the energy transfer.

**The Born amplitude is a Fourier transform (III·8).** As derived above, $f(\theta) \propto \tilde V(\mathbf{q})$. Every feature of the Born cross-section is a feature of the potential's Fourier transform. Forward scattering ($q = 0$): $\tilde V(0) = \int V(\mathbf{r})\,d^3r$ — the spatial integral of the potential. Large-angle scattering (large $q$): determined by the $\text{high-}q$ components, which fall off rapidly for smooth potentials and persist for sharp ones. Diffraction dips in nuclear scattering (e.g., $^{12}\text{C}$): the Fourier transform of a uniform sphere is $\propto j_1(qR)/qR$, a spherical Bessel function with zeros at definite angles — the same mathematics as single-slit diffraction.

Reading Born scattering through the Fourier lens converts an opaque integral into a physical picture: we are measuring the spatial frequency content of the potential at the spatial frequency set by the momentum transfer.

![Two-panel figure: scattering geometry with incident and scattered vectors and the differential cross-section curve](../images/06-the-fourier-transform-fig-04.png)
*Figure 6.4 — Born scattering as a Fourier transform: (left) incident k_i and scattered k_f vectors with momentum transfer arc q and scattering angle θ; (right) forward-peaked differential cross-section dσ/dΩ falling monotonically from θ = 0 to π, reflecting the high-q suppression of the potential's Fourier transform.*

---

## Conventions and Pitfalls

**The** $2\pi$ **placement.** Three common conventions are in active use: $1/2\pi$ on the inverse only (standard math); $1/\sqrt{2\pi}$ on each side (quantum optics and signal processing); $1/\sqrt{2\pi\hbar}$ on each side with $p = \hbar k$ (Griffiths-style QM). State the convention explicitly and do not switch mid-calculation. Mixing conventions introduces factors of $2\pi$ or $\hbar$ that are difficult to trace.

**Sign of the exponent.** Physics convention: $e^{-ikx}$ in the forward transform. Engineering convention: $e^{+ikx}$. The sign affects the transform of $f'(x)$: under physics convention $\widetilde{f'} = ik\tilde f$; under engineering $\widetilde{f'} = -ik\tilde f$. This matters when computing momentum-space representations of derivatives.

**The delta is defined by integration, not by a picture.** $\delta(x)$ is not a "very tall, very thin spike." It is defined by $\int\delta(x-x_0)f(x)\,dx = f(x_0)$. Multiplying two deltas together, or evaluating $\delta(x)$ at a point, are undefined operations.

**Bandwidth** $\neq$ **Robertson for energy and time.** The energy–time uncertainty $\Delta E\,\Delta t \sim \hbar$ is the Fourier bandwidth relation applied to time and energy, with $E = \hbar\omega$. It is not Robertson's theorem applied to $\hat H$ and $\hat t$, because $\hat t$ is not a self-adjoint operator in standard quantum mechanics. The correct statement: a system that interacts for time $\Delta t$ cannot exchange energy more sharply than $\Delta E \sim \hbar/\Delta t$.

**Plancherel normalization factor.** In the asymmetric convention, $\int|f|^2\,dx = \frac{1}{2\pi}\int|\tilde f|^2\,dk$ — there is a $1/2\pi$ on the right. In the symmetric convention both integrals are equal. Checking normalization of $\tilde\psi(p)$ using the wrong convention gives an answer off by $2\pi\hbar$.

**Completing the square with complex shifts.** The key step in the Gaussian transform — replacing $x$ with $x + ipa^2/\hbar$ — involves a complex shift of the integration variable. This is valid because $e^{-z^2/2a^2}$ is entire, so Cauchy's theorem guarantees the contour can be shifted. Students uncertain about this step can treat it as a formal manipulation and verify the result by checking that $|\tilde\psi(p)|^2$ integrates to 1.

---

## Quick Practice

1. **Transform a top hat.** Compute the Fourier transform $\tilde f(k)$ of $f(x) = 1$ for $|x| < a/2$, zero otherwise. Identify the result as a sinc function, locate its first zero, and explain why narrowing $a$ (smaller slit) widens the diffraction pattern.

2. **Gaussian saturation.** For $\psi(x) = (\pi a^2)^{-1/4}e^{-x^2/2a^2}$, compute $\Delta x = \sqrt{\langle x^2\rangle - \langle x\rangle^2}$ directly from $|\psi(x)|^2$, and compute $\Delta p$ from $|\tilde\psi(p)|^2$. Verify $\Delta x\,\Delta p = \hbar/2$. If $a$ is halved, by what factor does $\Delta p$ change?

3. **Born scattering for a Yukawa potential.** The Yukawa potential is $V(r) = V_0 e^{-\mu r}/r$; its 3D Fourier transform is $\tilde V(q) = 4\pi V_0/(q^2 + \mu^2)$. (a) Write the Born differential cross-section $d\sigma/d\Omega \propto |f(\theta)|^2$ as a function of $\theta$ using $q = 2k\sin(\theta/2)$. (b) Take $\mu \to 0$ to recover the Rutherford cross-section for Coulomb scattering. (c) Explain physically why $\text{large-}q$ (wide-angle) scattering is suppressed for a screened potential.

---

## Go Deeper

The full derivation — the $L\to\infty$ limit of the Fourier series, Plancherel's theorem, the convolution theorem with the substitution proof, the bandwidth relation, the single-slit sinc, the double-slit by convolution, the Gaussian packet, and the Dirac delta — is in *Mathematics for Physics Vol 2, Ch 6*. The present module condenses those results and extends them to the three QM applications (wave packets, transitions, Born scattering) that the source chapter does not cover.

---

## References

Fourier, J. (1822). *Théorie analytique de la chaleur*. Paris. The founding work: heat-equation solutions as trigonometric series and, on the infinite line, the integral transform.

Plancherel, M. (1910). Contribution à l'étude de la représentation d'une fonction arbitraire par des intégrales définies. *Rendiconti del Circolo Matematico di Palermo*, 30, 289–335.

Dirac, P. A. M. (1930). *The Principles of Quantum Mechanics*. Oxford University Press. Introduced the delta function as the continuum analogue of the Kronecker delta.

Schwartz, L. (1950–51). *Théorie des distributions*. Hermann, Paris. Placed the Dirac delta on rigorous mathematical ground as a distribution.

Gabor, D. (1946). Theory of communication. *Journal of the Institution of Electrical Engineers*, 93 (Part III), 429–441. The time–frequency bandwidth relation and the Gaussian as the minimum-uncertainty signal.

Born, M. (1926). Zur Quantenmechanik der Stossvorgänge. *Zeitschrift für Physik*, 37, 863–867.

Heisenberg, W. (1927). Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. *Zeitschrift für Physik*, 43, 172–198. The original uncertainty-relation paper; Heisenberg's argument was the Fourier width relation, not Robertson's commutator bound.
