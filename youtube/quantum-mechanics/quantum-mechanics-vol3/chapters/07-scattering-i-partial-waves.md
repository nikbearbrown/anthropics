# Chapter 7 — Scattering I: Partial Waves

Consider a hard sphere of radius $a$ placed in the laboratory. A beam of particles streams toward it. In classical mechanics, every particle whose impact parameter is less than $a$ bounces off and every other particle misses, giving a total cross-section of $\pi a^2$ — the geometric shadow area.

In quantum mechanics, the answer depends on energy. At low energy the total cross-section is $4\pi a^2$, four times the geometric value. At high energy it is $2\pi a^2$, twice the classical result. Both values follow directly from the wave nature of quantum particles: diffraction, interference, and the fact that a wave cannot be blocked without scattering in the forward direction. To calculate these results we develop the **partial-wave expansion**, a framework that separates the scattering problem into angular-momentum channels and assigns each channel a single real number called the phase shift. Once this framework is in place, every elastic scattering problem with spherical symmetry reduces to determining the phase shifts.

---

## The Scattering Amplitude

We work in the center-of-mass frame. A steady beam with energy $E = \hbar^2 k^2/2m$ propagates along $\hat{z}$. Far from the scatterer, the total wave function satisfies the **scattering boundary condition**:

$$\psi(\mathbf{r}) \overset{r\to\infty}{\longrightarrow} e^{ikz} + f(\theta)\,\frac{e^{ikr}}{r}.$$

The first term is the incident plane wave; the second is an outgoing spherical wave with angular modulation $f(\theta)$. We assume azimuthal symmetry (central potential), so there is no $\phi$ dependence. The single complex function $f(\theta)$ is called the **scattering amplitude**, and from it we can determine the total cross-section, the differential cross-section, and resonance properties.

![Scattering boundary condition: incident plane wave, central scatterer, outgoing spherical wavefronts](../images/07-scattering-i-partial-waves-fig-01.png)
*Figure 7.1 — Scattering geometry showing the incident plane wave, the scatterer at the origin, and outgoing spherical wavefronts with angular modulation $f(\theta)$ in the far field.*

The probability current in the incident wave is $j_\text{inc} = \hbar k/m$. The current scattered into solid angle $d\Omega$ is proportional to $|f(\theta)|^2$. Their ratio defines the **differential cross-section**:

$$\frac{d\sigma}{d\Omega} = |f(\theta)|^2.$$

Integrating over all solid angles gives the **total cross-section**:

$$\sigma_\text{tot} = \int|f(\theta)|^2\,d\Omega = 2\pi\int_0^\pi|f(\theta)|^2\sin\theta\,d\theta.$$

---

## The Partial-Wave Expansion

For a central potential, angular momentum is conserved and the problem separates by angular-momentum quantum number $\ell$. The incident plane wave has the Rayleigh expansion:

$$e^{ikz} = \sum_{\ell=0}^\infty(2\ell+1)\,i^\ell\,j_\ell(kr)\,P_\ell(\cos\theta).$$

Far from the scatterer, spherical Bessel functions behave as $j_\ell(kr) \to \sin(kr - \ell\pi/2)/kr$. The potential shifts each partial wave by a phase, so the asymptotic radial solution for angular momentum $\ell$ becomes:

$$u_\ell(r) \overset{r\to\infty}{\longrightarrow} \frac{\sin(kr - \ell\pi/2 + \delta_\ell)}{kr}.$$

The real number $\delta_\ell$ is the **phase shift** for the $\ell$-th partial wave. Assembling all partial waves and matching to the boundary condition, we obtain the scattering amplitude:

$$\boxed{f(\theta) = \frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta).}$$

Using the orthogonality of Legendre polynomials, the total cross-section becomes:

$$\sigma_\text{tot} = \frac{4\pi}{k^2}\sum_{\ell=0}^\infty(2\ell+1)\sin^2\delta_\ell.$$

Each partial wave contributes $\sigma_\ell = (4\pi/k^2)(2\ell+1)\sin^2\delta_\ell$, which is bounded by the **unitarity limit** $4\pi(2\ell+1)/k^2$. No such bound exists in classical mechanics.

![Partial-wave cross-section σ_ℓ ∝ sin²δ_ℓ vs. phase shift δ_ℓ, showing unitarity maximum at δ_ℓ = π/2](../images/07-scattering-i-partial-waves-fig-03.png)
*Figure 7.3 — Partial-wave cross-section $\sigma_\ell \propto \sin^2\delta_\ell$ as a function of phase shift $\delta_\ell \in [-\pi,\pi]$, reaching the unitarity bound at $\delta_\ell = \pm\pi/2$ (resonance) and vanishing at $\delta_\ell = 0, \pm\pi$ (Ramsauer-Townsend zeros).*

The phase shift has a direct physical interpretation: it is the phase by which the potential has shifted the outgoing wave relative to a free particle. An attractive potential draws the wave closer to the origin, advancing the phase, so $\delta_\ell > 0$. A repulsive potential pushes the wave outward, so $\delta_\ell < 0$.

![Free radial wave vs. phase-shifted wave for attractive (top) and repulsive (bottom) potentials](../images/07-scattering-i-partial-waves-fig-02.png)
*Figure 7.2 — Free radial wave $\sin(kr)$ (dashed) compared to the phase-shifted wave $\sin(kr+\delta_\ell)$ (solid) for an attractive potential ($\delta_\ell>0$, top) and a repulsive potential ($\delta_\ell<0$, bottom), with the potential range $a$ marked.*

---

## The Optical Theorem

We evaluate $f(\theta)$ at $\theta = 0$, using $P_\ell(1) = 1$:

$$f(0) = \frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell.$$

Taking the imaginary part:

$$\operatorname{Im}[f(0)] = \frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)\sin^2\delta_\ell = \frac{k}{4\pi}\sigma_\text{tot}.$$

Rearranging:

$$\boxed{\sigma_\text{tot} = \frac{4\pi}{k}\,\operatorname{Im}[f(0)].}$$

This result is known as the **optical theorem**. It states that the total cross-section equals the imaginary part of the forward scattering amplitude multiplied by $4\pi/k$. The physical content of this relation is as follows: whenever the potential removes probability from the forward beam by scattering to other directions, the forward-scattered wave must interfere destructively with the incident wave to create a shadow. That destructive interference requires a specific imaginary component in $f(0)$. The optical theorem is a consequence of unitarity and holds for inelastic scattering as well, where $\sigma_\text{tot}$ includes every process.

We can use it as a self-consistency check: compute $\sigma_\text{tot}$ from the partial-wave sum, independently compute $\operatorname{Im}[f(0)]$, and verify that the relation holds. If it does not, there is an error somewhere in the calculation.

---

## Low-Energy Scattering and the Scattering Length

A classical particle with angular momentum $\ell\hbar$ and momentum $\hbar k$ has impact parameter $b = \ell/k$. Only particles approaching within the range $a$ of the potential are affected: $b \lesssim a$ means $\ell \lesssim ka$. At low energy, when $ka \ll 1$, only the $\ell = 0$ term survives. The scattering amplitude and total cross-section reduce to:

$$f(\theta) \approx \frac{e^{i\delta_0}\sin\delta_0}{k}, \qquad \sigma_\text{tot} \approx \frac{4\pi}{k^2}\sin^2\delta_0.$$

As $k \to 0$, the phase shift goes to zero linearly: $\delta_0 \to -a_s k$, where $a_s$ is the **scattering length**. Then:

$$\sigma_\text{tot} \overset{k\to 0}{\longrightarrow} \frac{4\pi}{k^2}\sin^2(a_s k) \approx 4\pi a_s^2.$$

The low-energy total cross-section is $4\pi a_s^2$, independent of energy and four times the "classical" area $\pi a_s^2$. This factor of four is not an error. A spherically symmetric scatterer of characteristic size $a_s$ scatters isotropically into all $4\pi$ steradians, and that isotropy produces the factor of four.

The scattering length encodes information about the bound-state spectrum of the potential. If the potential is just deep enough to support a bound state at threshold (binding energy $\to 0$), then $a_s \to +\infty$. Just below threshold $a_s$ is large and negative; just above it is large and positive. This relationship is expressed by the Levinson theorem: the scattering length diverges whenever a new bound state appears at threshold and its sign changes. In nuclear physics, the neutron-proton triplet s-wave scattering length is $a_t \approx 5.4$ fm and the singlet is $a_s \approx -23.7$ fm. The large negative singlet value indicates a virtual bound state of the np system sitting just above threshold. In ultracold atomic physics, Feshbach resonances allow the scattering length to be tuned from $-\infty$ to $+\infty$ by adjusting a magnetic field.

---

## Resonances

When the potential supports a quasi-bound state just above threshold, the s-wave phase shift passes through $\pi/2$, causing $\sin^2\delta_0 \to 1$, and the partial cross-section reaches the unitarity limit $4\pi/k^2$. This is a **scattering resonance**.

Near a resonance at energy $E_R$, the phase shift takes the Breit-Wigner form:

$$\tan\delta_0(k) = \frac{\Gamma/2}{E_R - E},$$

where $\Gamma$ is the width of the resonance. The s-wave cross-section near the resonance is a Breit-Wigner Lorentzian in energy, peaking at $4\pi/k_R^2$ at $E = E_R$. Narrow resonances correspond to long-lived quasi-bound states; wide resonances correspond to weakly-trapped states that escape quickly. The analogy with a driven oscillator is useful: the cross-section peaks when the incoming energy matches the natural frequency of a quasi-stationary state inside the potential.

![Breit-Wigner resonance: narrow and wide Lorentzian cross-sections σ_0(E) near resonance energy E_R](../images/07-scattering-i-partial-waves-fig-06.png)
*Figure 7.6 — Breit-Wigner resonance profile: s-wave cross-section $\sigma_0(E)$ as a function of energy near $E_R$, showing a narrow resonance (solid) at the unitarity limit and a broader resonance (dashed, $\Gamma'=3\Gamma$) with lower peak and wider width, illustrating the inverse relationship between width and quasi-bound-state lifetime.*

---

## Worked Example — Hard-Sphere Scattering at Low and High Energy

**Setup.** We consider the hard-sphere potential: $V = \infty$ for $r < a$, $V = 0$ for $r \geq a$. The boundary condition is $\psi(a) = 0$.

**Exact s-wave phase shift.** The radial equation outside the sphere is the free-particle equation: $u_0'' + k^2 u_0 = 0$. The general solution is $u_0(r) = A\sin(kr + \delta_0)$. Applying the boundary condition $u_0(a) = 0$ requires $\sin(ka + \delta_0) = 0$, which gives:

$$\delta_0 = -ka.$$

This result is exact for all $k$. The phase shift is negative (consistent with a repulsive potential) and grows linearly with momentum.

**Low-energy cross-section.** With $\delta_0 = -ka$ and $ka \ll 1$, we have $\sin(ka) \approx ka$, so:

$$\frac{d\sigma}{d\Omega} \approx a^2 \quad\text{(isotropic)}, \qquad \sigma_\text{tot} \approx 4\pi a^2.$$

The scattering is isotropic and the cross-section is four times the geometric value. This is a purely quantum-mechanical result. The classical value $\pi a^2$ is smaller by a factor of four because the classical picture assumes particles travel in straight lines, while the quantum wave diffracts around the sphere and scatters uniformly in all directions at low energy.

**High-energy cross-section.** At $ka \gg 1$, many partial waves contribute — up to $\ell_\text{max} \approx ka$. The exact phase shifts $\delta_\ell$ for the hard sphere oscillate rapidly over the occupied channels and average to $\langle\sin^2\delta_\ell\rangle \to 1/2$. Summing over all channels:

$$\sigma_\text{tot} \approx \frac{4\pi}{k^2}\sum_{\ell=0}^{ka}(2\ell+1)\cdot\frac{1}{2} \approx 2\pi a^2.$$

This is twice the geometric cross-section. The extra $\pi a^2$ contribution is diffractive: blocking the beam requires the forward-scattered wave to interfere destructively with the incident wave and create a shadow. That forward-scattered wave carries probability and contributes $\pi a^2$ to the total cross-section in addition to the $\pi a^2$ from sideways scattering. A shadow requires scattering, and the scattering that produces the shadow is counted just as much as the scattering that deflects particles sideways. This is the quantum version of Babinet's principle.

![Hard-sphere total cross-section σ_tot/(πa²) vs. ka, starting at 4, oscillating, and approaching 2 at high energy](../images/07-scattering-i-partial-waves-fig-04.png)
*Figure 7.4 — Hard-sphere total cross-section $\sigma_\text{tot}/(\pi a^2)$ vs. $ka$, starting at the low-energy limit of 4 (isotropic s-wave), oscillating through intermediate energies, and asymptoting to the high-energy limit of 2 (forward diffraction).*

**Square-well phase shift for reference.** For a finite spherical square well of depth $V_0$ and radius $a$, the interior wave vector is $\kappa = \sqrt{k^2 + 2mV_0/\hbar^2}$. Matching the logarithmic derivative at $r = a$:

$$\delta_0 = \arctan\!\left(\frac{k}{\kappa}\tan(\kappa a)\right) - ka.$$

The scattering length at $k \to 0$:

$$a_s = a\!\left[1 - \frac{\tan(\kappa_0 a)}{\kappa_0 a}\right], \qquad \kappa_0 = \sqrt{2mV_0/\hbar^2}.$$

When $\kappa_0 a = (n + 1/2)\pi$, we have $\tan(\kappa_0 a) \to \infty$ and $a_s \to \pm\infty$. A new bound state appears at threshold, the cross-section diverges, and the wave can barely distinguish the potential from a true bound state.

![Scattering length a_s vs. well depth V_0, showing divergences at bound-state thresholds](../images/07-scattering-i-partial-waves-fig-05.png)
*Figure 7.5 — Scattering length $a_s$ of the spherical square well as a function of well depth $V_0$ (in natural units), diverging to $\pm\infty$ each time a new bound state appears at threshold, with sign-change zeros between successive divergences.*

---

## References

- Fitzpatrick, R. *Introductory Quantum Mechanics* (LibreTexts), Ch. 14. [verify URL active]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 11. [verify]
- Murayama, H. *Physics 221B Lecture Notes, Scattering Theory* (UC Berkeley, 2022). [verify URL active]
- Sakurai, J.J. and Napolitano, J. (2020). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 6. [verify]
- Efimov, V. (1970). "Energy levels arising from resonant two-body forces in a three-body system." *Physics Letters B*, 33, 563–564. [verify]
- Kraemer, T. et al. (2006). "Evidence for Efimov quantum states in an ultracold gas of caesium atoms." *Nature*, 440, 315–318. [verify]

---

*Chapter 8 follows: Born approximation. Instead of expanding in angular-momentum channels, expand in powers of the potential. The result is a Fourier transform of* $V(\mathbf{r})$ *evaluated at the momentum transfer* $\mathbf{q} = \mathbf{k}_f - \mathbf{k}_i$ — *Rutherford scattering falls out as the leading term.*

