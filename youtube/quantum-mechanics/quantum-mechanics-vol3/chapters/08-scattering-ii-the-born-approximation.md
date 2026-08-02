# Chapter 8 — Scattering II: The Born Approximation

In 1911, Ernest Rutherford calculated the scattering of alpha particles off gold nuclei using classical mechanics. He modeled the alpha particle as a point charge moving on a hyperbolic orbit under the $1/r$ Coulomb force, computed the deflection angle as a function of impact parameter, and converted that relationship into a differential cross-section. His formula matched the Geiger-Marsden data and established the nuclear model of the atom.

Fourteen years later, quantum mechanics arrived. The classical derivation became uncertain: alpha particles are waves, not billiard balls, and hyperbolic orbits are not solutions of the wave equation. The first quantum-mechanical calculation of Coulomb scattering, using the Born approximation, gave the same formula — exactly the same, not approximately.

This is not a coincidence that applies to all potentials. For most potentials, the Born approximation is an approximation — it works at high energy, fails at low energy, and breaks down near resonances and bound states. For the Coulomb potential, the agreement with the classical result is exact at the level of the differential cross-section, for a specific structural reason. Understanding that reason — and understanding when the Born approximation fails — is the subject of this chapter.

---

## The Lippmann-Schwinger Equation

The time-independent Schrödinger equation for scattering is

$$\left(-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right)\psi = E\psi.$$

Rearranging by moving the potential to the right:

$$\left(\nabla^2 + k^2\right)\psi = \frac{2m}{\hbar^2}V\psi, \qquad k^2 = \frac{2mE}{\hbar^2}.$$

This is the Helmholtz equation with a source term proportional to $V\psi$. We solve it using the Green's function for the Helmholtz operator — the function $G(\mathbf{r},\mathbf{r}')$ satisfying $(\nabla^2+k^2)G = -\delta^3(\mathbf{r}-\mathbf{r}')$. The outgoing-wave Green's function is

$$G_+(\mathbf{r},\mathbf{r}') = -\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|},$$

and using it to invert the Helmholtz equation and adding the incident plane wave $e^{ikz}$ as the homogeneous solution:

$$\boxed{\psi(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} - \frac{m}{2\pi\hbar^2}\int\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|}\,V(\mathbf{r}')\,\psi(\mathbf{r}')\,d^3r'.}$$

This is the **Lippmann-Schwinger equation** in position space. It is exact. The total wave function at $\mathbf{r}$ is the incident plane wave plus contributions from every point $\mathbf{r}'$ where the potential acts: the potential scatters probability at $\mathbf{r}'$, which propagates outward as a spherical wave $e^{ik|\mathbf{r}-\mathbf{r}'|}/|\mathbf{r}-\mathbf{r}'|$ to the observation point.

The equation is exact but requires knowing $\psi(\mathbf{r}')$ — the very quantity we are trying to find. Solving it requires either an exact treatment (possible only for special potentials) or an iterative approximation.

Far from the scatterer ($r \gg r'$), the approximation $|\mathbf{r}-\mathbf{r}'| \approx r - \hat{r}\cdot\mathbf{r}'$ simplifies the Green's function kernel to $(e^{ikr}/r)e^{-i\mathbf{k}'\cdot\mathbf{r}'}$, where $\mathbf{k}' = k\hat{r}$ is the outgoing wavevector. The wave function takes the asymptotic form $\psi \to e^{i\mathbf{k}\cdot\mathbf{r}} + f(\mathbf{k},\mathbf{k}')e^{ikr}/r$, with the **exact** scattering amplitude:

$$f(\mathbf{k},\mathbf{k}') = -\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf{k}'\cdot\mathbf{r}'}V(\mathbf{r}')\,\psi(\mathbf{r}')\,d^3r'.$$

This expression is still exact, and still requires knowing $\psi(\mathbf{r}')$ inside the scattering region.

<!-- → [FIGURE: schematic of the Lippmann-Schwinger geometry — incident plane wave from the left, scattering region with potential V(r') in the center, outgoing spherical wave propagating to detector at position r; label the incident wavevector k, outgoing k', and the source point r' inside the potential; arrows should show the path from source point to observation point with the label |r - r'|] -->

![schematic of the Lippmann-Schwinger geometry — incident plane wave from the left, scattering region with potential V(r') in the center,…](../images/08-scattering-ii-the-born-approximation-fig-01.png)
*Figure 8.1 — schematic of the Lippmann-Schwinger geometry — incident plane wave from the left, scattering region with potential V(r') in the center,…*

---

## The First Born Approximation

The **first Born approximation** replaces $\psi(\mathbf{r}')$ in the integrand by the incident wave $e^{i\mathbf{k}\cdot\mathbf{r}'}$. This substitution is valid when the wave function inside the scattering region is barely disturbed from the incoming plane wave — that is, when the potential is weak or the particle moves fast enough that it does not slow down significantly inside the scattering region.

Substituting:

$$f_B(\theta) = -\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf{k}'\cdot\mathbf{r}'}V(\mathbf{r}')\,e^{i\mathbf{k}\cdot\mathbf{r}'}\,d^3r' = -\frac{m}{2\pi\hbar^2}\int e^{i\mathbf{q}\cdot\mathbf{r}'}V(\mathbf{r}')\,d^3r',$$

where $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ is the **momentum transfer**. The result is:

$$\boxed{f_B(\theta) = -\frac{m}{2\pi\hbar^2}\,\widetilde{V}(\mathbf{q}),}$$

where $\widetilde{V}(\mathbf{q})$ is the **3D Fourier transform** of the potential evaluated at the momentum transfer.

The central result is this: **the Born scattering amplitude is proportional to the Fourier transform of the potential evaluated at the momentum transfer.** Large scattering amplitude occurs when $\widetilde{V}(\mathbf{q})$ is large at the relevant $\mathbf{q}$.

The magnitude of the momentum transfer: for elastic scattering $|\mathbf{k}| = |\mathbf{k}'| = k$, so

$$q = |\mathbf{q}| = 2k\sin(\theta/2).$$

At $\theta = 0$ (forward scattering), $q = 0$: we probe $\widetilde{V}(0) = \int V\,d^3r$, the volume integral of the potential — its long-range behavior. At $\theta = \pi$ (backscattering), $q = 2k$: we probe the high-frequency Fourier components, the short-range structure of the potential. Each scattering angle measures a different Fourier mode. In this sense, the Born approximation describes a diffraction experiment on the potential.

<!-- → [FIGURE: vector triangle for momentum transfer — showing k (incident), k' (scattered), and q = k - k'; label the angle θ between k and k', and show that |q| = 2k sin(θ/2) from the geometry of the isoceles triangle; two cases should be shown: θ small (q small, forward peak) and θ large (q ~ 2k, backscattering)] -->

![vector triangle for momentum transfer — showing k (incident), k' (scattered), and q = k - k'](../images/08-scattering-ii-the-born-approximation-fig-02.png)
*Figure 8.2 — vector triangle for momentum transfer — showing k (incident), k' (scattered), and q = k - k'*

---

## The Yukawa Potential: An Analytic Born Calculation

$$V(r) = \frac{V_0\,e^{-\mu r}}{\mu r}.$$

This potential has range $1/\mu$ and is the standard example for a Born calculation. For a spherically symmetric potential, the 3D Fourier transform reduces to a 1D sine transform. The angular integration over the spherical $d^3r'$ gives:

$$\widetilde{V}(q) = \frac{4\pi}{q}\int_0^\infty r\,V(r)\sin(qr)\,dr.$$

For the Yukawa potential, the integral is elementary:

$$\widetilde{V}_\text{Yukawa}(q) = \frac{4\pi V_0}{\mu}\cdot\frac{1}{q^2+\mu^2}.$$

The Born scattering amplitude is:

$$f_B(\theta) = -\frac{2mV_0}{\hbar^2\mu}\cdot\frac{1}{q^2+\mu^2} = -\frac{2mV_0}{\hbar^2\mu}\cdot\frac{1}{4k^2\sin^2(\theta/2)+\mu^2},$$

and the differential cross-section is:

$$\boxed{\frac{d\sigma}{d\Omega} = \left(\frac{2mV_0}{\hbar^2\mu}\right)^2\frac{1}{\left[4k^2\sin^2(\theta/2)+\mu^2\right]^2}.}$$

Several features are worth noting. The cross-section is strongly forward-peaked: as $\theta \to 0$, $q \to 0$ and the denominator approaches $\mu^4$, giving a finite maximum. As $\theta$ increases, $q$ grows and the denominator grows as $q^4 \propto \sin^4(\theta/2)$, so the cross-section falls steeply. The angular distribution becomes more forward-peaked as $k$ increases, because the denominator is dominated by the $4k^2\sin^2(\theta/2)$ term at large $k$. The range parameter $\mu$ sets the angular scale at which the cross-section begins to fall: the forward peak has angular half-width $\sim \mu/k$, narrowing at high energy.

<!-- → [CHART: Born differential cross-section dσ/dΩ vs θ for the Yukawa potential at three values of ka — showing the forward peak sharpening as ka increases; log scale on y-axis; the three curves should be labeled with ka = 0.5, 2, 5; this makes the energy dependence of the angular distribution visible] -->

![Born differential cross-section dσ/dΩ vs θ for the Yukawa potential at three values of ka — showing the forward peak sharpening as ka…](../images/08-scattering-ii-the-born-approximation-fig-03.png)
*Figure 8.3 — Born differential cross-section dσ/dΩ vs θ for the Yukawa potential at three values of ka — showing the forward peak sharpening as ka…*

---

## Worked Example: Screened Coulomb to Rutherford

We take $\mu \to 0$ in the Yukawa formula with $V_0/\mu \to ZZ'e^2/(4\pi\epsilon_0)$. The potential becomes the pure Coulomb potential $V(r) = ZZ'e^2/(4\pi\epsilon_0 r)$. The cross-section becomes:

$$\frac{d\sigma}{d\Omega} = \left(\frac{ZZ'e^2}{4\pi\epsilon_0}\right)^2\frac{m^2}{\hbar^4\cdot 4k^4\sin^4(\theta/2)} = \left(\frac{ZZ'e^2}{16\pi\epsilon_0 E}\right)^2\frac{1}{\sin^4(\theta/2)},$$

where $E = \hbar^2k^2/2m$ is the kinetic energy. This is the **Rutherford formula** — the same result Rutherford obtained from classical orbits in 1911. [verify: Rutherford (1911), Philosophical Magazine 21, 669]

For alpha particles ($Z = 2$) on gold ($Z' = 79$) at $E = 5$ MeV, the cross-section at $90°$ is:

$$\frac{d\sigma}{d\Omega}\bigg|_{90°} = 4\left(\frac{2\times79\times1.44\,\text{MeV·fm}}{4\times5\,\text{MeV}}\right)^2 \approx 520\,\text{fm}^2/\text{sr.}$$

The factor of 4 comes from $\sin^4(45°) = 1/4$. The Geiger-Marsden experiments confirmed this formula across a range of energies and target materials, establishing the nuclear model of the atom. [verify: Geiger & Marsden (1913), Philosophical Magazine 25, 604]

**Why is Born exact for Coulomb?** For any other potential, the Born amplitude is an approximation — the true amplitude $f$ differs from $f_B$. For the Coulomb potential, the exact quantum-mechanical scattering amplitude is:

$$f_\text{exact}(\theta) = -\frac{ZZ'e^2}{4\pi\epsilon_0\cdot 4E\sin^2(\theta/2)}\,e^{-i\eta\ln\sin^2(\theta/2)}\cdot\frac{\Gamma(1+i\eta)}{\Gamma(1-i\eta)},$$

where $\eta = ZZ'e^2/(4\pi\epsilon_0\hbar v)$ is the Sommerfeld parameter. When we compute $|f_\text{exact}|^2$, the exponential factor satisfies $|e^{-i\eta\ln\sin^2(\theta/2)}|^2 = 1$, and $|\Gamma(1+i\eta)/\Gamma(1-i\eta)| = 1$ since the argument is purely imaginary. The phases cancel and the differential cross-section is purely Rutherford — identical to the Born result.

This agreement is not approximate. It is exact. The Born approximation gives the correct modulus of the amplitude for the Coulomb potential because the Coulomb potential has a special structure — scale invariance with no intrinsic length scale — that causes all phase corrections to cancel in $|f|^2$. No other potential shares this property. The classical-quantum agreement is a consequence of the SO(4) symmetry of the Coulomb problem, the same hidden symmetry that makes hydrogen's energy levels depend only on $n$.

**Forward divergence.** As $\theta \to 0$, $d\sigma/d\Omega \to \infty$. The total cross-section $\sigma_\text{tot} = \int (d\sigma/d\Omega)\,d\Omega = \infty$ for the pure Coulomb potential. This is the correct result for an infinite-range potential: every particle, regardless of how distant, is deflected by some infinitesimal angle. Summing over all impact parameters gives an infinite total cross-section.

In a real experiment, atomic electrons screen the nuclear charge beyond the Bohr radius $a_0$. With Yukawa screening parameter $\mu \sim a_0^{-1}Z^{1/3}$, the total cross-section is finite. At large angles ($q \gg \mu$), screening is irrelevant and the Rutherford formula holds. At small angles ($q \ll \mu$), the cross-section saturates and the Coulomb divergence is cut off. The physical observable is the screened result; the pure Coulomb divergence is an idealization.

---

## Validity of the Born Approximation

The Born approximation replaces $\psi(\mathbf{r}') \approx e^{i\mathbf{k}\cdot\mathbf{r}'}$ inside the Lippmann-Schwinger integral. This substitution is valid when the scattered wave is small compared to the incident wave in the scattering region. Evaluating the Lippmann-Schwinger integral at $\mathbf{r} = 0$ for the Yukawa potential yields two validity conditions.

**Low energy** ($k \ll \mu$):

$$\frac{2m|V_0|}{\hbar^2\mu^2} \ll 1.$$

The potential must be weak in absolute terms: its integral over the range must be small compared to the kinetic energy at scale $\mu$.

**High energy** ($k \gg \mu$):

$$\frac{2m|V_0|}{\hbar^2\mu k} \ll 1.$$

This condition improves as $k$ increases — Born becomes more accurate at higher energies. However, the label "high-energy approximation" can be misleading: the potential must also be weak. A strong potential that supports bound states will have $2m|V_0|/\hbar^2\mu^2 \gtrsim 1$ regardless of energy, and the low-energy condition fails near threshold.

**Practical rule:** if the potential is strong enough to support a bound state, Born fails at low energy even if it eventually works at high energy. If the potential is too weak to bind, Born works throughout. The failure of Born near a resonance is qualitative, not merely quantitative: it predicts no resonance structure at all, because it assumes the wave function is barely perturbed. Near a resonance, the wave function inside the scattering region is dramatically enhanced — exactly the behavior that Born ignores.

<!-- → [FIGURE: Born validity diagram — a 2D plot with Born parameter ξ = 2m|V₀|/ℏ²μ² on the vertical axis (log scale, 0.01 to 100) and ka on the horizontal axis (log scale, 0.1 to 10); shade the Born-valid region (ξ < 1 or ka > ξ) in light green and the invalid region in light red; draw the boundary curve ka = ξ as a dashed line; mark with red stars the locations of s-wave resonances (exact cross-section peaks that Born misses); the diagram should make the two-parameter structure of Born validity visually clear] -->

![Born validity diagram — a 2D plot with Born parameter ξ = 2m|V₀|/ℏ²μ² on the vertical axis (log scale, 0.01 to 100) and ka on the…](../images/08-scattering-ii-the-born-approximation-fig-04.png)
*Figure 8.4 — Born validity diagram — a 2D plot with Born parameter ξ = 2m|V₀|/ℏ²μ² on the vertical axis (log scale, 0.01 to 100) and ka on the…*

The Born series — iterating the Lippmann-Schwinger equation — generates systematic corrections to the first Born term:

$$f = f_B^{(1)} + f_B^{(2)} + \cdots, \quad f_B^{(2)} = -\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf{k}'\cdot\mathbf{r}'}V(\mathbf{r}')\,G_+(\mathbf{r}',\mathbf{r}'')\,V(\mathbf{r}'')\,e^{i\mathbf{k}\cdot\mathbf{r}''}\,d^3r'\,d^3r''.$$

Each successive term is suppressed by one power of the Born parameter $\xi$. When $\xi \ll 1$, the series converges rapidly. When $\xi \sim 1$, convergence is slow. When $\xi > 1$ and $ka$ is not large, the series diverges. The formal structure is identical to perturbation theory in bound-state problems: the Born series is perturbation theory in $V$, applied to scattering states. The first Born term corresponds to single-scattering; the second Born term to double-scattering. The Born parameter is the scattering-theory analogue of the coupling constant.

---

## Form Factors: When the Target Has Structure

The Born approximation extends naturally to targets with internal structure. If the scattering target is not a point charge but an extended charge distribution $\rho(\mathbf{r})$ (normalized to 1), the Born cross-section factors as:

$$\frac{d\sigma}{d\Omega} = \left(\frac{d\sigma}{d\Omega}\right)_\text{point} \times |F(\mathbf{q})|^2,$$

where

$$F(\mathbf{q}) = \int e^{i\mathbf{q}\cdot\mathbf{r}}\rho(\mathbf{r})\,d^3r$$

is the **nuclear form factor** — the Fourier transform of the charge distribution. At $\mathbf{q} = 0$: $F(0) = \int\rho\,d^3r = 1$ always. At large $q$: if $\rho$ is localized within radius $R$, then $F(\mathbf{q}) \to 0$ for $qR \gg 1$. The form factor suppresses scattering at large angles (large $q$) relative to the point-particle prediction — the extended target is "softer" than a point.

The first zero of $|F(q)|^2$ occurs at $qR \sim 4.49$ for a uniform sphere (the first zero of the spherical Bessel function $j_1$). Measuring this zero from the angular distribution directly gives the nuclear radius $R$. This is how Robert Hofstadter measured the proton charge radius in 1956, work that earned him the 1961 Nobel Prize. [verify: Hofstadter (1956), Reviews of Modern Physics 28, 214]

The form factor approach is the Born approximation at its most useful: any target whose charge distribution can be Fourier-transformed can be analyzed this way. It applies to nuclei, protons, neutrons, and in a generalized sense to inelastic processes where the target transitions between quantum states. Deep inelastic scattering — the experiments that established the quark substructure of protons at SLAC in the late 1960s — used exactly this logic.

![Nuclear form factor |F(q)|² vs. dimensionless momentum transfer qR for a uniform sphere, showing oscillating diffraction pattern with first zero at qR ≈ 4.49](../images/08-scattering-ii-the-born-approximation-fig-05.png)
*Figure 8.5 — Nuclear form factor $|F(q)|^2$ for a uniform sphere as a function of $qR$, starting at unity, oscillating with decreasing envelope, and reaching its first zero at $qR\approx4.49$; the position of this zero gives the nuclear radius $R$ from electron-scattering data.*

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the structure of the Born formula.*
   State the Lippmann-Schwinger equation in position space, identifying (a) the incident wave term, (b) the Green's function kernel, and (c) what approximation converts it into the first Born approximation. Then state the Born result $f_B(\theta) = $ [fill in], identify $\mathbf{q}$, and compute $|\mathbf{q}|$ as a function of $\theta$ and $k$ for elastic scattering.
   *Tests: command of the Lippmann-Schwinger structure and the Born approximation step.*

2. *Difficulty: Warm-up — tests the Fourier reduction for spherical potentials.*
   For a spherically symmetric potential $V(r)$, reduce the 3D Fourier transform to a 1D integral by performing the $\phi'$ and $\theta'$ angular integrations in spherical coordinates. Your result should take the form $\widetilde{V}(q) = (4\pi/q)\int_0^\infty r\,V(r)\sin(qr)\,dr$. For the Gaussian potential $V(r) = V_0 e^{-r^2/a^2}$, evaluate $\widetilde{V}(q)$ analytically and sketch $d\sigma/d\Omega$ vs. $\theta$. Is the angular distribution narrower or wider than for the Yukawa potential of the same range?
   *Tests: angular integration technique; Gaussian Fourier transform; comparison of angular widths.*

3. *Difficulty: Warm-up — tests Born validity conditions.*
   For the Yukawa potential, write the two Born validity conditions (low energy and high energy) in terms of the dimensionless parameters $\xi = 2m|V_0|/\hbar^2\mu^2$ and $ka = k/\mu$. (a) For $V_0 = \hbar^2\mu^2/(2m)$ ($\xi = 1$), at what $ka$ does the high-energy condition become satisfied to within 10%? (b) Sketch the boundary between Born-valid and Born-invalid regions in the $(\xi, ka)$ plane.
   *Tests: extracting the validity conditions and drawing the two-parameter diagram.*

**Application**

4. *Difficulty: Application — Yukawa total cross-section.*
   Integrate the Yukawa Born differential cross-section $d\sigma/d\Omega = (2mV_0/\hbar^2\mu)^2[4k^2\sin^2(\theta/2)+\mu^2]^{-2}$ over solid angle to find $\sigma_\text{tot}$. Use the substitution $u = \cos\theta$ to reduce to $\int_{-1}^1 du/(A+B(1-u))^2$ with appropriate $A$, $B$. Show that as $\mu \to 0$ (Coulomb limit), $\sigma_\text{tot} \to \infty$, and interpret this physically.
   *Tests: explicit integration; the Coulomb divergence as a physical result.*

5. *Difficulty: Application — Rutherford scattering numerics.*
   Alpha particles ($Z = 2$, $A = 4$, $E = 8$ MeV) on silver ($Z' = 47$). Using $e^2/(4\pi\epsilon_0) = 1.44$ MeV·fm: (a) compute $d\sigma/d\Omega$ at $\theta = 30°$, $60°$, $90°$, $120°$, $150°$ in $\text{fm}^2$/sr; (b) at which angle does the cross-section fall to 1% of its $\theta = 10°$ value? (c) Estimate the angle at which the de Broglie wavelength becomes comparable to the classical distance of closest approach; above this angle, nuclear forces become important and Rutherford fails.
   *Tests: numerical command of the Rutherford formula; identifying the regime of validity.*

6. *Difficulty: Application — nuclear form factor.*
   For a uniform sphere of radius $R$ and charge distribution $\rho(r) = 3/(4\pi R^3)$ for $r \leq R$, zero otherwise: (a) compute the form factor $F(q) = \int e^{i\mathbf{q}\cdot\mathbf{r}}\rho(r)\,d^3r$ analytically; (b) at what $qR$ does $|F(q)|^2$ first reach zero? (c) If electron scattering off a nucleus first shows a zero in $|F|^2$ at momentum transfer $q_0 = 0.5$ $\text{fm}^{-1}$, estimate the nuclear radius. (d) How does the angular distribution $d\sigma/d\Omega \propto |F(q)|^2/q^4$ differ from the point-nucleus Rutherford formula at large $\theta$?
   *Tests: computing a form factor analytically; extracting radius from the first zero; comparing to point-nucleus prediction.*

**Synthesis**

7. *Difficulty: Synthesis — Born vs. exact comparison.*
   For a square well $V(r) = -V_0$ for $r < a$, zero outside: (a) compute the Born scattering amplitude analytically using the 1D sine transform formula; (b) compare the Born total cross-section to the exact s-wave result (from the phase-shift formula of Chapter 7) at $ka = 1$ and $ka = 5$, for $V_0 = \hbar^2/(2ma^2)$ ($\xi \approx 1$); (c) identify whether there is a resonance in the exact result that Born misses; (d) characterize the Born error: is it a factor-of-2 discrepancy, or does Born predict the wrong qualitative behavior?
   *Tests: Born calculation for a new potential; comparison with exact result; identifying qualitative failure near resonance.*

8. *Difficulty: Synthesis — Coulomb phase and identical particle scattering.*
   For two identical spinless particles scattering via Coulomb repulsion, the amplitude is $f(\theta) + f(\pi-\theta)$ (symmetrized) rather than $f(\theta)$ alone (indistinguishable particles). (a) In the Born approximation, where $f_B(\theta) = -\eta/(2k\sin^2(\theta/2))$ (in units where $\hbar = 2m = 1$), write out $|f_B(\theta) + f_B(\pi-\theta)|^2$ and show it equals $|f_B(\theta)|^2 + |f_B(\pi-\theta)|^2 + 2\text{Re}[f_B(\theta)f_B^*(\pi-\theta)]$. (b) The interference term depends on the relative phase between $f(\theta)$ and $f(\pi-\theta)$. In Born, these are both real, so the interference is purely real. In the exact Coulomb amplitude, both acquire the Coulomb phase $e^{-i\eta\ln\sin^2(\theta/2)}$. Compute the interference term using the exact phases and show it differs from the Born result. (c) Explain why the Coulomb phase, though invisible in $|f|^2$ for distinguishable particles, becomes observable in identical-particle scattering.
   *Tests: interference of Born amplitudes; the Coulomb phase enters through indistinguishability; connects to quantum statistics.*

**Challenge**

9. *Difficulty: Challenge — the eikonal approximation as a resummation of the Born series.*
   The eikonal approximation applies when $ka \gg 1$ (large impact parameters dominate) and gives the scattering amplitude as a phase integral along straight-line paths. For the Yukawa potential, the eikonal amplitude is $f_\text{eik}(\theta) = ik\int_0^\infty b\,J_0(q b)\,(e^{i\chi(b)}-1)\,db$, where $b$ is the impact parameter, $q = 2k\sin(\theta/2)$, and $\chi(b) = -(m/\hbar^2 k)\int_{-\infty}^\infty V(\sqrt{b^2+z^2})\,dz$ is the eikonal phase. (a) For a Yukawa potential, compute $\chi(b)$ for $\mu b \ll 1$ (small impact parameter compared to range). (b) Expand $e^{i\chi} \approx 1 + i\chi$ (valid when $|\chi| \ll 1$, i.e., weak potential). Show that this recovers the Born approximation. (c) For $|\chi| \gg 1$ (strong potential), the full $e^{i\chi}$ must be kept. Interpret the eikonal approximation as a resummation of the Born series to all orders at fixed impact parameter.
   *Tests: eikonal calculation; Born as leading term of the eikonal; the resummation interpretation connects to field theory.*

---

## References

Lippmann, B. A., & Schwinger, J. (1950). Variational principles for scattering processes. I. *Physical Review*, 79, 469–480. [verify]

Rutherford, E. (1911). The scattering of $\alpha$ and $\beta$ particles by matter and the structure of the atom. *Philosophical Magazine*, 21, 669–688.

Geiger, H., & Marsden, E. (1913). The laws of deflexion of $\alpha$ particles through large angles. *Philosophical Magazine*, 25, 604–623.

Hofstadter, R. (1956). Electron scattering and nuclear structure. *Reviews of Modern Physics*, 28, 214–254.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Ch. 11.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. Ch. 6.

Fitzpatrick, R. *Introductory Quantum Mechanics* (LibreTexts / UT Austin), §§14.1–14.2.

