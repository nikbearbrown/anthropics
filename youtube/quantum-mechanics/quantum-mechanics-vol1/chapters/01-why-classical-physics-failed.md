# Chapter 1 — Why Classical Physics Failed: Blackbody, Photoelectric, and the Photon

When iron is heated in a forge, it glows red, then orange, then yellow-white. The color depends only on the temperature, not on the particular piece of iron. Any iron, any ceramic, any object at the same temperature glows the same color and emits the same spectrum. By 1900, Lummer and Pringsheim had measured these spectral curves with great precision: smooth, hump-shaped, and reproducible to within a percent. The trouble was that the best theory of the time predicted those curves badly, and physicists across Europe knew exactly how badly.

The classical prediction was not "a lot of energy." It was infinite energy. Taken literally, it implied that a hot poker left in a room should flood you with ultraviolet radiation from the walls. That this plainly does not happen told everyone something fundamental was missing.

---

## How You Get Infinite Energy from Perfectly Good Physics

The classical argument is clean and easy to follow. Inside a cavity at temperature $T$, the electromagnetic field can vibrate at any frequency. If we count the available modes, we find

$$\frac{8\pi\nu^2}{c^3}$$

modes per unit volume per unit frequency interval. This count is correct — it is a geometric fact about standing waves in a box, and nobody disputes it.

The next step is to assign an energy to each mode. The classical rule is equipartition: every degree of freedom in thermal equilibrium at temperature $T$ carries average energy $\frac{1}{2}k_BT$. An electromagnetic mode has two quadratic terms — electric field energy and magnetic field energy — so it carries $k_BT$. Multiplying by the mode count gives

$$u(\nu, T) = \frac{8\pi\nu^2}{c^3}\,k_BT.$$

This is the Rayleigh–Jeans law. It matches measurement at long wavelengths. At short wavelengths, though, the mode count grows as $\nu^2$ while each mode still carries a fixed $k_BT$, so the product grows without bound. Integrate over all frequencies and the total energy is infinite. This failure was named the ultraviolet catastrophe.

It is worth being precise about which assumption breaks. The mode counting is not wrong. Equipartition is not wrong in general — it works beautifully for ideal gases, setting aside the separate issue of low-temperature heat capacities. The fatal assumption is that energy can be distributed *continuously* among the modes. There is no smallest chunk; any mode, however high its frequency, can hold any energy from zero upward, and on average it holds $k_BT$. That continuity is what produces the catastrophe.

---

## Planck's Desperate Remedy

Max Planck was not trying to invent quantum mechanics. He was trying to fit a curve. He had the experimental data from Lummer and Pringsheim and wanted a formula that matched it. Working backward from the data — a perfectly respectable approach, as long as you are honest about it — he found that the only route to a finite total energy was to modify the entropy of a resonator in a very specific way.

What that modification amounted to was this: suppose the oscillators in the cavity walls cannot hold arbitrary energies. Suppose instead they are limited to the values $0, h\nu, 2h\nu, 3h\nu, \ldots$ — discrete multiples of a basic unit $h\nu$, where $h$ is a new constant. Then, instead of integrating over a continuous distribution (which returns $k_BT$), we sum a discrete geometric series and obtain

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_BT} - 1}.$$

This is the Planck average energy per mode. Multiplying by the mode density gives the **Planck distribution**:

$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_BT} - 1}.$$

Two limits are worth checking right away. At low frequencies, where $h\nu \ll k_BT$, the exponential expands as $e^{h\nu/k_BT} \approx 1 + h\nu/k_BT$, the denominator becomes $h\nu/k_BT$, and the whole expression reduces to $k_BT$. We recover the Rayleigh–Jeans law exactly — Planck's formula agrees with classical physics precisely where classical physics already worked. At high frequencies, where $h\nu \gg k_BT$, the exponential is enormous, the $-1$ is negligible, and $u$ falls off like $e^{-h\nu/k_BT}$. The exponential overwhelms the polynomial, and there is no catastrophe.

![Planck distribution vs. Rayleigh–Jeans law showing the ultraviolet catastrophe](../images/01-why-classical-physics-failed-fig-01.png)
*Figure 1.1 — Planck spectral distribution compared with the Rayleigh–Jeans law: the two curves agree at low frequencies, but the classical prediction diverges while the Planck curve falls exponentially in the ultraviolet.*

The value Planck fitted to the Berlin data was $h = 6.55 \times 10^{-34}$ J·s. The currently accepted value is $6.626 \times 10^{-34}$ J·s, so his first fit was within one percent.

One point is crucial. Planck quantized the *oscillators in the walls*, not the electromagnetic field itself. In his picture the field remained classical. The oscillators could exchange energy with the field only in chunks of $h\nu$, but between exchanges the field did whatever Maxwell's equations said it should. Planck himself was uneasy about this. For years he tried to find a way to recover his formula without the discrete energies, and he never succeeded, because it cannot be done. But the further step — declaring that *the field itself* comes in discrete packets, that light is made of particles — was not one he was prepared to take.

---

## What the Spectral Peak Tells You

From the Planck distribution we can derive Wien's displacement law by locating where $\partial u/\partial\nu = 0$. The algebra is manageable: it leads to a transcendental equation whose solution is $x = h\nu/k_BT \approx 2.821$, so

$$\nu_\text{max} = 2.821\,\frac{k_BT}{h}.$$

The peak frequency is proportional to temperature. Double the temperature and you double the peak frequency, halving the peak wavelength. At $T = 5778$ K (the Sun's photosphere), the peak wavelength is about 501 nm — green. At $T = 3000$ K (a tungsten filament), the peak sits near 966 nm — infrared. Most of the light from an incandescent bulb is invisible, which is one reason we stopped making them.

There is a subtlety worth flagging. The peak *in frequency* and the peak *in wavelength* do not fall at the same place. Convert $\nu_\text{max}$ to a wavelength using $\lambda = c/\nu$, and you do not get $\lambda_\text{max}$ from Wien's law in its wavelength form. This is not a contradiction; it follows from the fact that $d\nu$ and $d\lambda$ are not proportional. The spectral density per unit frequency and the spectral density per unit wavelength are simply different functions. Both are legitimate descriptions of the spectrum, written in different coordinates.

---

## Worked Example — Twenty Orders of Magnitude

Let us measure the failure. At $T = 3000$ K and $\nu = 3 \times 10^{15}$ Hz, in the ultraviolet, just how wrong is Rayleigh–Jeans?

Both formulas carry the same mode density $8\pi\nu^2/c^3$, so the ratio of Planck to Rayleigh–Jeans reduces to the ratio of the average energies per mode:

$$\frac{u_\text{Planck}}{u_\text{RJ}} = \frac{h\nu/k_BT}{e^{h\nu/k_BT} - 1}.$$

Working out the pieces: $h\nu = (6.626\times10^{-34})(3\times10^{15}) = 1.988\times10^{-18}$ J $= 12.4$ eV, while $k_BT = (1.381\times10^{-23})(3000) = 4.14\times10^{-20}$ J $= 0.259$ eV. Their ratio is $x = h\nu/k_BT \approx 47.9$.

Then $e^{47.9} \approx 7\times10^{20}$, and

$$\frac{u_\text{Planck}}{u_\text{RJ}} \approx \frac{47.9}{7\times10^{20}} \approx 7\times10^{-20}.$$

That is twenty orders of magnitude. At ultraviolet frequencies and ordinary temperatures, classical physics is not approximately wrong — it is completely wrong. The quantity that controls the discrepancy is $x = h\nu/k_BT$. When $x \ll 1$, the two theories agree; when $x \gg 1$, they diverge by factors that grow like $e^x$. The crossover, $h\nu \sim k_BT$, marks the boundary where quantization begins to matter.

![Regime map of the dimensionless parameter x = hν/k_BT](../images/01-why-classical-physics-failed-fig-03.png)
*Figure 1.3 — Regime map of the dimensionless ratio x = hν/k_BT: the classical and quantum regimes are separated at x = 1, with representative values from deep infrared (x ≈ 0.1), the transition boundary, and the ultraviolet catastrophe case (x ≈ 48) from the worked example.*

---

## A Completely Different Crisis

While Planck was fitting curves in Berlin, Heinrich Hertz had noticed something strange. In 1887 — the same year he demonstrated electromagnetic waves and confirmed Maxwell — he found that ultraviolet light striking a metal surface caused it to emit sparks. By 1902, Philipp Lenard had established that the sparks were electrons, and by 1914 Robert Millikan had measured every feature of the phenomenon. The data said three things, each impossible to explain with wave theory:

**First**, there is a threshold frequency. Below a certain $\nu_0$ that depends on the metal, no electrons are emitted — ever, at any intensity. A blinding arc lamp at red frequencies liberates nothing from sodium. A dim UV lamp liberates electrons immediately. Intensity is irrelevant; frequency is everything.

**Second**, the maximum kinetic energy of the ejected electrons depends on frequency but not on intensity. Double the brightness of the light, and you get twice as many electrons per second, but each electron has the same energy as before.

**Third**, emission begins with no measurable time delay — within nanoseconds, at any intensity above the threshold.

Each of these is inexplicable in the classical picture. There, energy is delivered continuously and uniformly across the surface, so there should be no threshold: given enough time, any frequency at sufficient intensity ought to accumulate the energy needed to free an electron. The time delay should grow as intensity falls. And the kinetic energy should depend on how hard the wave pushes — that is, on intensity. Classical physics gets every detail of this experiment wrong.

---

## Einstein's Light Quanta

In 1905, Einstein proposed something radical. He went beyond Planck, who had only said that oscillators exchange energy in discrete units. Einstein proposed that light energy is *not continuously distributed at all*. It arrives in discrete packets, each carrying energy

$$E = h\nu.$$

He called them *Lichtquanten* — light quanta. We call them photons.

A single photon, arriving at a metal surface, is absorbed by a single electron. If $h\nu$ is less than the energy needed to pull the electron free of the metal — the **work function** $\Phi$ — the electron cannot escape, no matter how many photons per second strike the surface. If $h\nu > \Phi$, the electron escapes, and the excess energy becomes kinetic energy:

$$K_\text{max} = h\nu - \Phi.$$

That relation is Einstein's photoelectric equation. The **stopping potential** $V_\text{stop}$ — the reverse voltage just sufficient to halt the fastest electrons — then satisfies

$$eV_\text{stop} = K_\text{max} = h\nu - \Phi.$$

Everything now follows. There is a threshold because a photon with $h\nu < \Phi$ simply cannot do the job — not "almost, if you add the next one up," but genuinely cannot, ever, because each photon acts alone. The kinetic energy depends on frequency because it depends on the photon energy $h\nu$, which frequency fixes by itself. Intensity controls only how many photons arrive per second. And the absence of any time delay is natural: one photon, one electron, immediate.

Around 1914, Millikan set out to disprove this. He thought the photon idea was absurd. For two years he made extraordinarily careful measurements with freshly scraped metal surfaces in vacuum, recording $V_\text{stop}$ as a function of $\nu$ for sodium, lithium, and potassium. Every metal gave the same slope: $h/e = 4.136\times10^{-15}$ V·s. Einstein's equation fit perfectly. Millikan published his confirmation in 1916, remarking that the result was "obtained in spite of my personal conviction," and won the Nobel Prize in 1923 specifically for this measurement of $h$. Einstein won the Nobel Prize in 1921 specifically for the photoelectric effect — not for special relativity.

![Stopping potential vs. frequency for three metals showing identical slopes](../images/01-why-classical-physics-failed-fig-02.png)
*Figure 1.2 — Stopping potential as a function of frequency for sodium, aluminum, and copper: three parallel line segments with identical slope h/e and different threshold frequencies set by each metal's work function.*

---

## Worked Example — Stopping Potential for UV on Sodium

Suppose ultraviolet light at wavelength $\lambda = 300$ nm falls on sodium, whose work function is $\Phi = 2.28$ eV. What stopping potential results?

The shortcut $hc = 1240$ eV·nm gets us there quickly:

$$E = \frac{1240\ \text{eV}\cdot\text{nm}}{300\ \text{nm}} = 4.13\ \text{eV}.$$

Then $K_\text{max} = 4.13 - 2.28 = 1.85$ eV, and

$$V_\text{stop} = 1.85\ \text{V}.$$

Now try green light at $\lambda = 546$ nm. Here $E = 1240/546 \approx 2.27$ eV, a hair below $\Phi = 2.28$ eV. The result is no electrons — not one, not even from a 10,000-watt lamp. The photon energy falls just short of threshold, and stacking up sub-threshold photons never produces one that crosses it.

---

## Wave and Particle — Not an Either/Or

By 1905, the wave nature of light was not a hypothesis. Young's 1801 double-slit experiment, Maxwell's 1865 electromagnetic theory, and Hertz's 1887 demonstration of radio waves — half a century of evidence — had established that light is a wave. Interference, diffraction, and polarization are all impossible for bullets. And yet here was Einstein saying that light comes in particles.

The resolution is not that light "sometimes" behaves as a wave and "sometimes" as a particle, switching between modes depending on the experiment. That framing makes it sound as though light has two personalities it alternates between, which is not what happens. In the quantum mechanical description, light is always described by a probability amplitude — a wave. The amplitude tells you where detection events are likely; the detection events themselves are discrete and localized. The wave is real, and the particle is real. They are not two separate things.

Arthur Compton's 1923 experiment closed the remaining loopholes. When X-rays scatter from graphite, the scattered X-rays come out with a longer wavelength than the incident ones. The wavelength shift is

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta),$$

where $\theta$ is the scattering angle and $h/(m_e c) = 2.426\times10^{-12}$ m is the Compton wavelength of the electron. This formula follows from treating the photon as a particle with momentum $p = h/\lambda = E/c$ and working out the elastic collision with an electron using relativistic kinematics. Classical wave theory predicts no wavelength shift at all. The experiment is unambiguous, and Compton won the Nobel Prize in 1927.

---

## The Constant That Tells You When Quantum Mechanics Matters

Two numbers define the quantum scale:

$$h = 6.62607015\times10^{-34}\ \text{J}\cdot\text{s}, \qquad \hbar = \frac{h}{2\pi} = 1.054571817\times10^{-34}\ \text{J}\cdot\text{s}.$$

The unit is J·s — energy times time, or equivalently momentum times length. This is the unit of **action**, the same quantity that appears in Lagrangian mechanics. Planck's constant is not an energy. The energy is $h\nu$; the momentum is $h/\lambda$. Planck's constant is the factor you multiply frequency by, or divide wavelength into, to get an energy or a momentum.

For any physical system, quantum mechanics becomes important when the relevant action — momentum times distance, or energy times time — is comparable to $h$. For an electron in a 1-nanometer potential well, the ground-state kinetic energy is of order $\hbar^2/(2m_e L^2) \approx 0.4$ eV: measurable and important. For a 1-gram marble in a 10-centimeter box, the corresponding energy is roughly $10^{-65}$ J. Quantum mechanics is not wrong for macroscopic objects; it is exact for them. It is simply that for objects of large mass and large size, the quantum energy scales are so unimaginably small that classical mechanics is indistinguishable from the correct theory.

---

## What Planck Did Not Know

It is worth being clear about what actually happened in 1900, because the history is often garbled. Planck did not discover quantum mechanics. He found a formula that matched a curve, and he found a derivation for that formula that required discrete energy levels in the oscillators. In his original paper and for years afterward, he was explicit that he hoped the discrete energies were a mathematical trick — an artifact of his combinatorial counting — that might eventually be derived from classical physics without requiring discreteness in nature. He was wrong, but he did not know he was wrong, and he resisted the photon idea for years after Einstein proposed it.

Einstein's 1905 step was different in kind. Where Planck quantized the material oscillators at the boundary of the cavity, Einstein quantized the electromagnetic field itself. That is a far more radical claim: not merely that matter exchanges energy with the field in chunks, but that the field energy is intrinsically discrete regardless of the matter it interacts with. Planck was unwilling to say this; Einstein was. His discomfort with his own discovery is a useful reminder that finding the right formula and understanding what it means are two very different achievements.

A genuine physical understanding of *why* oscillators carry discrete energy levels had to wait for quantum mechanics proper, which arrived in 1925 and 1926 with Heisenberg and Schrödinger. Planck had the formula in hand in 1900; the mechanism underneath it would not appear for another quarter century.

<!-- → [TABLE: Work functions of common metals in eV — Cs 2.1, Na 2.28, K 2.3, Mg 3.7, Al 4.1, Ag 4.3, Fe 4.5, Cu 4.7, Ni 5.0, Au 5.1, Pt 6.35] -->

![Work functions of eleven common metals as a dot-plot](../images/01-why-classical-physics-failed-fig-04.png)
*Figure 1.4 — Work functions of eleven metals ranked by threshold energy: metals below the 4.13 eV reference line (the photon energy at 300 nm) emit electrons under the sodium worked example; those above do not.*

---

## References

- Planck, M. (1901). "Ueber das Gesetz der Energieverteilung im Normalspectrum." *Annalen der Physik* 4, 553–563. — The original blackbody quantization paper.
- Einstein, A. (1905). "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Annalen der Physik* 17, 132–148. — The photoelectric effect paper introducing photons.
- Millikan, R.A. (1916). "A direct photoelectric determination of Planck's h." *Physical Review* 7(3), 355–388. [doi:10.1103/PhysRev.7.355](https://doi.org/10.1103/PhysRev.7.355)
- Compton, A.H. (1923). "A quantum theory of the scattering of X-rays by light elements." *Physical Review* 21(5), 483–502. [doi:10.1103/PhysRev.21.483](https://doi.org/10.1103/PhysRev.21.483)
- NIST CODATA 2018 recommended values of fundamental physical constants. [physics.nist.gov/constants](https://physics.nist.gov/cgi-bin/cuu/Value?h)
- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.2.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §1.3–1.4.
- Krane, K.S. (2019). *Modern Physics* (4th ed.). Wiley. Chapter 3.
- Nobel Prize facts: Einstein 1921 — [nobelprize.org/prizes/physics/1921/einstein/facts/](https://www.nobelprize.org/prizes/physics/1921/einstein/facts/); Millikan 1923 — [nobelprize.org/prizes/physics/1923/millikan/facts/](https://www.nobelprize.org/prizes/physics/1923/millikan/facts/); Compton 1927 — [nobelprize.org/prizes/physics/1927/compton/facts/](https://www.nobelprize.org/prizes/physics/1927/compton/facts/).
- Hake, R.R. (1998). "Interactive-engagement versus traditional methods." *Am. J. Phys.* 66(1), 64–74. [doi:10.1119/1.18809](https://pubs.aip.org/aapt/ajp/article/66/1/64/1055076/Interactive-engagement-versus-traditional-methods)

---

*Chapter 2 follows: de Broglie turns the argument around and asks whether the particle-nature of light implies a wave-nature of matter. If photons have momentum* $p = h/\lambda$, *what is the wavelength of an electron?*

