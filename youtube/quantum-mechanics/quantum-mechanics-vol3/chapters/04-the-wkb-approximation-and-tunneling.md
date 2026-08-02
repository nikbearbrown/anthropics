# Chapter 4 — The WKB Approximation and Tunneling

Polonium-212 has a half-life of about $3\times10^{-7}$ seconds. Thorium-232 has a half-life of about $1.4\times10^{10}$ years — longer than the current age of the universe. Both decay by emitting an alpha particle through the same mechanism: tunneling through a Coulomb barrier.

The ratio of their half-lives is roughly $10^{24}$. Twenty-four orders of magnitude from one mechanism.

In 1911, Hans Geiger and John Nuttall observed that for alpha emitters the logarithm of the half-life is approximately linear in $1/\sqrt{E_\alpha}$ — a clean empirical relationship. The observation was precise. The theoretical explanation was not yet available. [verify: Geiger & Nuttall, Phil. Mag. 22, 613 (1911)]

The difficulty is this: an alpha particle inside a nucleus sees a potential barrier with a height of around 30 MeV. The emitted alpha has only around 5 MeV. Classically, the alpha cannot escape over the top of the barrier. And yet it does escape.

In 1928, George Gamow in Göttingen computed the probability of the alpha tunneling through the Coulomb barrier using wave mechanics. Within days, Ronald Gurney and Edward Condon at Princeton published the same result independently. [verify] Both found that the tunneling probability is exponentially sensitive to barrier height, width, and particle energy. That exponential sensitivity produces the 24-decade dynamic range. The Geiger-Nuttall line is a plot of that exponent as a function of alpha energy.

This chapter develops the approximation method that produces this result.

---

## The WKB Ansatz

The time-independent Schrödinger equation in one dimension is

$$-\frac{\hbar^2}{2m}\psi'' + V(x)\psi = E\psi.$$

We define the local classical momentum $p(x) = \sqrt{2m(E - V(x))}$, real in the classically allowed region ($E > V$), imaginary in the forbidden region ($E < V$). Writing $\psi(x) = e^{iS(x)/\hbar}$ — an exact rewriting, not yet an approximation — and substituting gives:

$$\frac{(S')^2}{2m} - \frac{i\hbar}{2m}S'' = E - V(x).$$

We expand $S$ in powers of $\hbar$: $S = S_0 + (\hbar/i)S_1 + \cdots$. At zeroth order: $(S_0')^2/2m = E - V$, so $S_0'(x) = \pm p(x)$. At first order: $S_1 = \frac{i}{2}\ln p + \text{const}$.

Assembling the leading two terms in the classically allowed region:

$$\psi_\text{WKB}(x) \approx \frac{C}{\sqrt{p(x)}}\,\exp\!\left[\frac{i}{\hbar}\int p\,dx'\right] + \frac{D}{\sqrt{p(x)}}\,\exp\!\left[-\frac{i}{\hbar}\int p\,dx'\right],$$

and in the forbidden region where $p = i|p|$:

$$\psi_\text{WKB}(x) \approx \frac{A}{\sqrt{|p(x)|}}\,\exp\!\left[\frac{1}{\hbar}\int|p|\,dx'\right] + \frac{B}{\sqrt{|p(x)|}}\,\exp\!\left[-\frac{1}{\hbar}\int|p|\,dx'\right].$$

**The** $1/\sqrt{p}$ **factor has a physical interpretation.** The classical probability of finding the particle near $x$ is proportional to the time it spends there — proportional to $1/v \propto 1/p$. So $|\psi|^2 \propto 1/p$: the wave function is large where the classical particle moves slowly, small where it moves fast. The amplitude tracks classical mechanics; the phase oscillates quantum-mechanically. This is the sense in which the approximation is "semiclassical."

![WKB wavefunction: oscillating with amplitude envelope ∝ 1/√p in the classically allowed region (swelling near turning points, contracting near the potential minimum) and exponentially decaying tails in the forbidden zones on both sides](../images/04-the-wkb-approximation-and-tunneling-fig-01.png)
*Figure 4.1 — WKB wavefunction in allowed and forbidden regions: amplitude is large where the classical particle moves slowly (near turning points) and small where it moves fast, with exponential decay outside the classical turning points a and b.*

The expansion is controlled by $\hbar$ relative to the classical action $\int p\,dx$. When $\int p\,dx \gg \hbar$ — when the particle traverses many de Broglie wavelengths — the higher-order terms are small and the approximation is reliable.

---

## Validity and Its Failure

Working through the algebra, the condition for the WKB expansion to be controlled reduces to

$$\left|\frac{d\lambda_\text{dB}}{dx}\right| \ll 1,$$

where $\lambda_\text{dB}(x) = h/p(x)$ is the local de Broglie wavelength. The potential must vary slowly on the scale of one wavelength.

This condition fails at a **classical turning point** $x_0$ where $E = V(x_0)$ and $p(x_0) \to 0$. As the particle slows, $\lambda_\text{dB}$ grows without bound. The $1/\sqrt{p}$ prefactor diverges. The WKB forms on each side cannot be matched naively.

**The fix: Airy functions.** Near the turning point, we linearize: $V(x) \approx V(x_0) + V'(x_0)(x-x_0)$. The Schrödinger equation reduces to $\psi'' = z\psi$ where $z \propto (x - x_0)$ — the **Airy equation**. The regular solution $\text{Ai}(z)$ oscillates on the allowed side and decays on the forbidden side:

$$\text{Ai}(z) \sim \begin{cases} \frac{1}{2\sqrt{\pi}}|z|^{-1/4}\cos\!\left(\tfrac{2}{3}|z|^{3/2} - \tfrac{\pi}{4}\right) & z\to-\infty \\ \frac{1}{2\sqrt{\pi}}z^{-1/4}e^{-\frac{2}{3}z^{3/2}} & z\to+\infty \end{cases}.$$

The $\pi/4$ phase shift on the allowed side is the **Maslov index** — a topological property of the connection across a turning point, not a fitting parameter. Each turning point contributes this phase shift. Matching the Airy asymptotics to the WKB solutions on each side gives the connection formulas that thread solutions through the turning points.

![Airy function connection at a classical turning point: linearized potential through x₀, oscillatory Ai(z) with π/4 phase shift on the allowed side, smooth single-lobe decay on the forbidden side, with a shaded matching zone centered on x₀](../images/04-the-wkb-approximation-and-tunneling-fig-02.png)
*Figure 4.2 — Classical turning point and Airy function connection: the Maslov π/4 phase shift emerges from matching the Airy function asymptotics across the intermediate zone where neither WKB form is valid.*

---

## Bound States: Bohr-Sommerfeld

A particle bound between two classical turning points $a$ and $b$ oscillates inside and decays outside. Threading the WKB solution through both turning points, applying the connection formula at each, and requiring a self-consistent solution gives the **Bohr-Sommerfeld quantization condition**:

$$\boxed{\oint p(x)\,dx = 2\int_a^b p(x)\,dx = \left(n + \frac{1}{2}\right)h, \quad n = 0, 1, 2, \ldots}$$

The $1/2$ is the combined Maslov correction from both turning points ($\pi/4$ each, totaling $h/2$). The original 1913-1916 Bohr-Sommerfeld rule had $nh$ without this correction; the correct $n + 1/2$ emerges from the Airy analysis.

**A notable special case.** For the harmonic oscillator $V = \frac{1}{2}m\omega^2 x^2$, the classical orbit at energy $E$ is an ellipse in phase space with area $2\pi E/\omega$. The condition gives:

$$\frac{2\pi E}{\omega} = \left(n+\frac{1}{2}\right)h \quad\Longrightarrow\quad E_n = \left(n+\frac{1}{2}\right)\hbar\omega.$$

This is the *exact* quantum-mechanical spectrum — not an approximation. The same exactness holds for the Coulomb potential and hydrogen. These are potentials with hidden algebraic symmetries (the Fock $\mathrm{SU}(2)$ symmetry for the oscillator, the Runge-Lenz vector for hydrogen) that cause the WKB expansion to terminate. For most other potentials, Bohr-Sommerfeld is a leading-order estimate that improves at large $n$.

The $1/2$ in the Bohr-Sommerfeld condition is not a small correction. For $n = 0$, it is the only term — without it, the predicted ground-state energy is zero. The zero-point energy of the harmonic oscillator is a Maslov correction.

![Bohr-Sommerfeld phase-space orbits: three nested ellipses for n=0, 1, 2 in the (x, p) plane with shaded interiors showing enclosed area ∝ (n+½)h, and classical turning points marked where p=0](../images/04-the-wkb-approximation-and-tunneling-fig-03.png)
*Figure 4.3 — Bohr-Sommerfeld quantization in phase space: the enclosed area of each elliptical orbit equals (n+½)h, with the n=0 ellipse nonzero — the entire zero-point energy is a Maslov correction.*

---

## Worked Example — WKB Tunneling and Rectangular Barrier

**Part I: Quantitative comparison.** An electron ($m_e = 9.11\times10^{-31}$ kg) with kinetic energy $E = 1$ eV hits a rectangular barrier of height $V_0 = 5$ eV and width $L = 5$ Å.

We compute $\kappa = \sqrt{2m_e(V_0-E)}/\hbar$: with $V_0 - E = 4$ eV,

$$\kappa = \frac{\sqrt{2\times9.11\times10^{-31}\times4\times1.6\times10^{-19}}}{1.055\times10^{-34}} \approx 1.02\ \text{Å}^{-1}.$$

The Gamow factor: $\gamma = \kappa L = 1.02\times5 = 5.10$. The WKB transmission coefficient:

$$T_\text{WKB} = e^{-2\gamma} = e^{-10.2} \approx 3.7\times10^{-5}.$$

The exact result from matching boundary conditions:

$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0-E)}\right]^{-1} \approx 9.5\times10^{-5}.$$

The ratio is $T_\text{exact}/T_\text{WKB} \approx 2.56$. The analytical prediction for this prefactor is $16E(V_0-E)/V_0^2 = 16\times1\times4/25 = 2.56$. Agreement within rounding.

WKB gets the exponent correct. It misses the prefactor $16E(V_0-E)/V_0^2$ by an $O(1)$ factor that depends smoothly on $E/V_0$. On a log plot, $T_\text{exact}$ and $T_\text{WKB}$ run parallel — same slope, constant offset. For physics spanning 24 orders of magnitude, the $O(1)$ prefactor is invisible.

**Limit of validity:** when $E \to V_0$, $\kappa \to 0$, $T \to 1$, and the WKB tunneling formula breaks down. The exact result interpolates smoothly through the barrier top; WKB has a kink there. The approximation applies when $\kappa L \gg 1$ — deep sub-barrier tunneling.

**Part II: Bohr-Sommerfeld for a linear potential.** The "bouncing ball" potential $V(x) = mgx$ for $x > 0$ with a hard wall at $x = 0$. The hard wall contributes a Maslov phase of $\pi/2$ (equivalent to $1/2$) rather than $\pi/4$ — because it reflects with no penetration, unlike a smooth turning point. The smooth turning point at $x_0 = E/(mg)$ contributes $\pi/4$ as usual. The combined factor gives $3/4$ instead of $1/2$ on the right side of the quantization condition:

$$\int_0^{x_0}\sqrt{2m(E-mgx)}\,dx = \left(n + \frac{3}{4}\right)\frac{h}{2}.$$

Working through the integral: $E_n \propto (n + 3/4)^{2/3}$. This matches the exact results in terms of zeros of the Airy function $\text{Ai}$ to better than 1% even for $n = 0$.

---

## The Gamow Factor

A particle with energy $E$ encounters a barrier $V(x) > E$ between turning points $a$ and $b$. Threading through the connection formulas and computing the ratio of transmitted to incident probability current gives the transmission coefficient:

$$\boxed{T \approx e^{-2\gamma}, \qquad \gamma = \frac{1}{\hbar}\int_a^b\sqrt{2m(V(x)-E)}\,dx.}$$

The integral $\gamma$ is the **Gamow factor**. Three properties follow directly.

First, $T$ is *exponential* in $\gamma$. A small change in barrier height, width, or particle energy is amplified into a large change in $T$. This is the source of the 24-decade dynamic range in alpha-decay half-lives.

Second, the barrier shape enters automatically. Any $V(x)$ receives the same treatment — just integrate $\sqrt{2m(V-E)}$ over the forbidden region. Rectangular, triangular, parabolic, Coulomb — all handled by the same formula.

Third, in the thick-barrier limit $\gamma \gg 1$, the exponential carries essentially all the information. The $O(1)$ prefactors from connection-formula details are swamped by the exponential.

![Gamow factor tunneling diagram: potential barrier above the energy line with shaded forbidden zone, incoming and reflected waves on the left, decaying exponential inside the barrier, transmitted wave of smaller amplitude on the right, and a three-barrier comparison strip showing rectangular, triangular, and Coulomb shapes](../images/04-the-wkb-approximation-and-tunneling-fig-04.png)
*Figure 4.4 — Tunneling transmission and the Gamow factor: the transmitted amplitude is exponentially suppressed by e^{−2γ}, where γ is the integral of √(2m(V−E)) over the forbidden region — the same formula regardless of barrier shape.*

---

## Alpha Decay and the Geiger-Nuttall Law

We model an alpha particle as a pre-formed cluster inside a heavy nucleus. Inside ($r < R$, nuclear radius), the strong force holds it. Outside, it sees the Coulomb repulsion from the daughter nucleus with charge $Z' = Z - 2$:

$$V(r) = \frac{2Z'e^2}{4\pi\epsilon_0 r}, \quad r > R.$$

The barrier extends from $r = R$ out to the classical turning point $r_c = 2Z'e^2/(4\pi\epsilon_0 E_\alpha)$. For uranium-238 ($Z' = 90$, $E_\alpha \approx 4.2$ MeV, $R \approx 7.4$ fm), $r_c \approx 60$ fm — the alpha must tunnel through a barrier eight times the nuclear diameter.

The Gamow integral over the Coulomb barrier evaluates (via the substitution $r = r_c\sin^2\theta$) in the limit $R \ll r_c$ to a leading term proportional to $Z'/\sqrt{E_\alpha}$. Taking the logarithm of the half-life $\tau_{1/2} \sim \nu_0^{-1}e^{2\gamma}$, where $\nu_0 \sim 10^{21}$ Hz is the attempt frequency:

$$\log_{10}\tau_{1/2} \approx A(Z') + \frac{B(Z')}{\sqrt{E_\alpha}}.$$

This is the **Geiger-Nuttall law**: log half-life linear in $1/\sqrt{E_\alpha}$ for fixed daughter charge. The empirical observation from 1911 is derived from the WKB tunneling formula. Every point on the Geiger-Nuttall line is a different nuclide; every nuclide lies on the same straight line.

**Numerics for** $^{238}\text{U}$. With the numbers above: $\gamma \approx 43$, $e^{-2\gamma} \approx 4\times10^{-38}$, half-life estimate roughly $5\times10^8$ years. The experimental value is $4.5\times10^9$ years — off by a factor of 10. On a quantity spanning $10^{24}$, this is excellent agreement. The remaining discrepancy comes from the alpha pre-formation probability and from the prefactors we dropped.

![Geiger-Nuttall law: scatter plot of log₁₀(half-life) vs. 1/√E_α with six to eight data points lying on a straight line, two distinguished points marking the short-lived and long-lived extremes, and the best-fit Geiger-Nuttall line through all points spanning ~33 decades on the vertical axis](../images/04-the-wkb-approximation-and-tunneling-fig-05.png)
*Figure 4.5 — Geiger-Nuttall law: log half-life is linear in 1/√E_α across 33 decades of dynamic range, the entire span explained by the exponential sensitivity of the Gamow tunneling factor.*

---

## The Exponential in Other Contexts

The Gamow factor is not specific to nuclear physics. The same structure appears across a wide range of phenomena.

**Scanning tunneling microscope.** A metal tip held a few ångströms above a conducting surface. Electrons tunnel through the vacuum gap; the current goes as $I \propto e^{-2\kappa d}$ where $\kappa \approx 1$ $\text{Å}^{-1}$ for a typical work function of 4-5 eV. A 1 Å change in tip-surface distance changes the current by $e^2 \approx 7$. A surface feature of sub-ångström height produces a measurable current swing. This exponential transduction turns atomic-scale topography into macroscopic current variation, enabling the STM to image individual atoms. [verify: Binnig & Rohrer, PRL 49, 57 (1982)]

**Stellar fusion.** In the solar core at $kT \sim 1$ keV, the proton-proton Coulomb barrier is of order 1 MeV. Most fusion occurs at the **Gamow peak energy** $E_G$, where the Maxwell-Boltzmann thermal tail (growing with $E$) and the Gamow tunneling factor (decreasing with $E$) together peak. For solar conditions, $E_G \approx 6$ keV — six times $kT$. Every star burns by tunneling. [verify: Atkinson & Houtermans, Z. Phys. 54, 656 (1929)]

**Flash memory.** Electrons tunnel through a thin $\text{SiO}_2$ layer under a high electric field, giving a triangular barrier — Fowler-Nordheim tunneling. The write speed and data retention time of every USB stick are controlled by the Gamow factor for that triangular barrier. [verify: Fowler & Nordheim, Proc. R. Soc. A 119, 173 (1928)]

**Cold fusion falsification.** Martin Fleischmann and Stanley Pons claimed in 1989 to have achieved deuterium-deuterium fusion at room temperature. The Gamow factor at $kT \approx 0.025$ eV for a D-D Coulomb barrier gives $\gamma \sim 1000$, so $e^{-2\gamma} \sim 10^{-900}$. Even a factor of $10^{50}$ enhancement from the palladium lattice would leave the claim short by $10^{850}$. Computing the Gamow factor is sufficient to evaluate quantitatively any claim of "novel nuclear effects at ambient conditions."

![Four physical contexts for the Gamow exponential: a 2×2 grid of schematic panels — STM tip over a surface with a vacuum gap, alpha particle exiting a Coulomb barrier from a nucleus, two protons approaching a Coulomb hill in stellar fusion, and a layered flash-memory structure with a thin SiO₂ tunneling layer](../images/04-the-wkb-approximation-and-tunneling-fig-06.png)
*Figure 4.6 — The Gamow exponential across physical contexts: STM, alpha decay, stellar fusion, and flash memory all share the same e^{−2γ} structure — only the barrier geometry and particle mass change.*

---

## The Langer Correction for 3D

In three dimensions, the radial Schrödinger equation for $u(r) = rR(r)$ with angular momentum $\ell$ is

$$-\frac{\hbar^2}{2m}u'' + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u = Eu.$$

This looks like a 1D problem with effective potential $V_\text{eff} = V + \hbar^2\ell(\ell+1)/(2mr^2)$, and one might apply WKB directly. Near $r = 0$, however, the centrifugal term diverges and the validity condition fails. The correct semiclassical quantization requires the **Langer correction**: replace $\ell(\ell+1)$ by $(\ell+\frac{1}{2})^2$:

$$2\int_{r_1}^{r_2}\sqrt{2m\!\left[E - V(r) - \frac{\hbar^2(\ell+\frac{1}{2})^2}{2mr^2}\right]}\,dr = \left(n_r + \frac{1}{2}\right)h.$$

The correction accounts for the additional phase accumulated near the origin, where the centrifugal barrier acts as a hard wall with a half-integer Maslov contribution. [verify: Langer, Phys. Rev. 51, 669 (1937)]

For the Coulomb potential, the Langer-corrected condition gives the exact hydrogen energy levels $E_n = -13.6$ $\text{eV}/n^2$. Without the correction, the $\ell = 0$ states are wrong. The correction matters primarily for $\text{low-}\ell$ states and is negligible for $\text{high-}\ell$ states at large radii, where $\ell(\ell+1) \approx (\ell+\frac{1}{2})^2$ already.

---

## References

- Gamow, G. (1928). "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik*, 51, 204–212. [verify]
- Gurney, R.W. and Condon, E.U. (1928). "Wave Mechanics and Radioactive Disintegration." *Nature*, 122, 439. [verify]
- Geiger, H. and Nuttall, J.M. (1911). "The ranges of the α particles from various radioactive substances." *Philosophical Magazine*, 22, 613–621. [verify]
- Langer, R.E. (1937). "On the connection formulas and the solutions of the wave equation." *Physical Review*, 51, 669–676. [verify]
- Binnig, G. and Rohrer, H. (1982). "Scanning tunneling microscopy." *Physical Review Letters*, 49, 57–61. [verify]
- Atkinson, R. and Houtermans, F.G. (1929). "Zur Frage der Aufbaumöglichkeit der Elemente in Sternen." *Zeitschrift für Physik*, 54, 656–665. [verify]
- Fowler, R.H. and Nordheim, L. (1928). "Electron Emission in Intense Electric Fields." *Proceedings of the Royal Society A*, 119, 173–181. [verify]
- Eckle, P. et al. (2008). "Attosecond Ionization and Tunneling Delay Time Measurements in Helium." *Science*, 322, 1525–1529. [verify]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §9.1–9.3. [verify]
- Bender, C.M. and Orszag, S.A. (1978). *Advanced Mathematical Methods for Scientists and Engineers*. McGraw-Hill. Ch. 10. [verify]

---

Chapter 5 covers time-dependent perturbation theory. Where the methods so far apply to stationary states and energy levels, time-dependent perturbation theory addresses transitions between states driven by a time-varying perturbation. It is the framework for absorption and emission, selection rules, and Fermi's golden rule.

