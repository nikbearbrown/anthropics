# Bear's Doodles — Video Candidates: Quantum Mechanics Vol. 5 (Mathematical Methods)

**Scouted:** 18 modules (M-01 through M-18) — a math-methods refresher volume.

**Selectivity note.** This volume teaches *technique*: complex arithmetic, ODE solving, matrix diagonalization, Fourier machinery, combinatorics, dimensional analysis. Most of it teaches by manipulation (algebra, integration by parts, characteristic polynomials) — the learner reasons through steps rather than watching something move. I rejected the pure-derivation zones (Sturm-Liouville proofs, Dirac-notation type grammar, Cauchy–Schwarz algebra, determinant cofactor expansion, Legendre/Laguerre/Bessel catalogues) and kept only ideas where **motion carries the teaching**. The result is a tighter slate than the physics volumes — 14 candidates, not 19-21. Where a concept recurs from an earlier volume (spinor 720°, tunneling, beats, entanglement dimension), I anchor it to Vol. 5's specific mathematical framing and flag the overlap so you can decide whether to build it once.

---

## 01 — The phasor that spins but never changes anything

- **Source:** Vol. 5, M-01 (Complex Numbers and the Complex Exponential), "In the Quantum Series" — stationary-state phasor
- **Production mode:** Manim visualization
- **Hook:** An energy eigenstate is called "stationary" — so why is it rotating?
- **Core idea:** The time factor $e^{-iEt/\hbar}$ is a unit arrow spinning at rate $E/\hbar$ in the complex plane. Because its length is always 1, the probability density $|\psi|^2$ is dead flat in time even though $\psi$ itself never stops turning. "Stationary" means the *observable* is frozen, not the state.
- **Visual object:** A rotating arrow on the unit circle (left), wired to a row of $|\psi|^2$ bars (right) that stay exactly level as the arrow sweeps around.
- **Manim move:** rotate (the phasor) + hold (the bars) — the contrast IS the lesson
- **Short-form fit:** Strong
- **Prerequisites:** complex number as a point in the plane; $|\psi|^2$ = probability
- **Exclusions:** don't drift into full time-dependent Schrödinger evolution; keep to one eigenstate
- **Score:** 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-phasor-stationary/vox-phasor-stationary-review.mp4`

---

## 02 — Squeeze the position, the momentum spreads (uncertainty is just Fourier)

- **Source:** Vol. 5, M-06 (The Fourier Transform), "Bandwidth Relation and the Uncertainty Principle" + Gaussian minimum-uncertainty
- **Production mode:** Manim visualization
- **Hook:** Heisenberg's uncertainty principle isn't quantum — it's a fact about *every* wave.
- **Core idea:** A function and its Fourier transform have reciprocal widths: $\Delta x\,\Delta k \geq \tfrac12$. Narrow a Gaussian in position and its transform fattens in exactly reciprocal proportion. Multiply by $p=\hbar k$ and you have $\Delta x\,\Delta p \geq \hbar/2$ — the "quantum" mystery is a theorem about transform pairs that would apply to sound or light equally.
- **Visual object:** Two coupled Gaussians — a position bump and a momentum bump — tied by a slider. Pinch one; the other visibly bloats.
- **Manim move:** slosh/spread (reciprocal breathing of the two curves)
- **Short-form fit:** Strong
- **Prerequisites:** a wave has a width; Fourier = "which pure waves are inside"
- **Exclusions:** skip the Robertson/commutator route entirely — that's a *different* proof and belongs in its own card
- **Score:** 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-fourier-uncertainty/vox-fourier-uncertainty-review.mp4`

---

## 03 — Eigenvectors: the directions a matrix can't turn

- **Source:** Vol. 5, M-08 (Eigenvalues and Diagonalization), "The Eigenvalue Problem: Invariant Directions"
- **Production mode:** Manim visualization
- **Hook:** A matrix spins almost every arrow — except a special few it can only stretch.
- **Core idea:** Apply a linear map to a fan of vectors and watch them rotate and scale chaotically. Two directions come out pointing exactly where they went in, only longer or shorter — the eigenvectors. Everything downstream (measurement outcomes, quantum numbers, time evolution) is built on finding these invariant directions.
- **Visual object:** A ring of arrows swept by the matrix; all rotate off-axis except the eigen-directions, which glow and slide along their own line.
- **Manim move:** transform (the fan) with the invariant directions highlighted
- **Short-form fit:** Strong
- **Prerequisites:** a matrix acts on a vector
- **Exclusions:** don't compute a characteristic polynomial on screen — this is the *picture*, not the algebra
- **Score:** 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-eigen-directions/vox-eigen-directions-review.mp4`

---

## 04 — Every valley is a parabola if you lean in close enough

- **Source:** Vol. 5, M-04 (Series Expansions and Approximation), "Every Smooth Potential Near a Minimum Is a Harmonic Oscillator"
- **Production mode:** Manim visualization
- **Hook:** Why is the harmonic oscillator *everywhere* in physics? Because every potential lies about being complicated.
- **Core idea:** Taylor-expand any smooth potential about its minimum: the linear term dies, and the leading survivor is a quadratic. Zoom into the bottom of any lopsided well and it becomes a clean parabola with $k_\text{eff}=V''(x_0)$ — which is why the quantum harmonic oscillator is the universal reference for molecular bonds, lattice sites, and trapped atoms.
- **Visual object:** A lumpy asymmetric potential; the camera dives toward its minimum while a fitted parabola locks on and the two curves merge.
- **Manim move:** scan/zoom (the merge of well and parabola)
- **Short-form fit:** Strong
- **Prerequisites:** a potential well; the shape of a parabola
- **Exclusions:** don't work the full Taylor coefficients; the zoom is the argument
- **Score:** 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-potential-parabola/vox-potential-parabola-review.mp4`

---

## 05 — Quantum revival: the shape that falls apart and reassembles

- **Source:** Vol. 5, M-05 (Fourier Series and the Wave Equation), worked example — parabolic state in the square well
- **Production mode:** Manim visualization
- **Hook:** Scramble a wavefunction into noise, wait, and it rebuilds itself perfectly.
- **Core idea:** An initial shape in a box is a sum of eigenmodes, each spinning its phase at rate $\propto n^2$. The modes dephase and the probability density churns into a mess — but because the frequencies are commensurable ($n^2$ ratios), at special revival times they snap back into alignment and the original shape reforms. Revival is constructive interference of many clocks.
- **Visual object:** A parabola in a well dissolving into a jittering blob, then coalescing back to the parabola at $t_\text{rev}$.
- **Manim move:** decay → accumulate (dephase, then rephase)
- **Short-form fit:** Strong
- **Prerequisites:** a wavefunction is a sum of standing modes; each mode has its own frequency
- **Exclusions:** don't derive the coefficients; the collapse-and-return is the payoff
- **Score:** 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-quantum-revival/vox-quantum-revival-review.mp4`

---

## 06 — All paths at once, and only the classical one survives

- **Source:** Vol. 5, M-15 (Calculus of Variations), "The Path Integral: Why $L=T-V$"
- **Production mode:** Manim visualization
- **Hook:** Nature doesn't take the path of least action. It takes *all* of them — they just cancel.
- **Core idea:** Feynman's sum over paths weights each trajectory by a phasor $e^{iS/\hbar}$. Paths far from the stationary one have wildly spinning phases that destructively cancel; near the stationary path the phase barely changes, so those phasors line up and add. The classical trajectory is the one that survives the interference — "least action" is what's left standing.
- **Visual object:** A swarm of wiggly paths between two points, each carrying a little phasor; the off-paths' arrows point every which way and sum to nothing, while the near-classical arrows align into a fat resultant.
- **Manim move:** accumulate (phasor sum) with cancellation vs. reinforcement
- **Short-form fit:** Strong
- **Prerequisites:** action along a path; a phasor as a little clock
- **Exclusions:** no Euler–Lagrange derivation; this is the "why nature extremizes" punchline only
- **Score:** 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-path-integral/vox-path-integral-review.mp4`

---

## 07 — Equilibrium is just counting (the peak becomes a needle)

- **Source:** Vol. 5, M-14 (Combinatorics and Multiplicity), "Multiplicity of a Two-State System" + Stirling sharpening
- **Production mode:** Manim visualization
- **Hook:** The second law of thermodynamics isn't a law — it's arithmetic that gets ruthless as things get big.
- **Core idea:** Count microstates of $N$ coins by number of heads: the multiplicity $\binom{N}{N_\uparrow}$ peaks at half-and-half. For $N=6$ the peak is soft; for $N=100$ it's sharper; for $N=10^{23}$ it's a knife-edge. Equilibrium isn't imposed — it's just where essentially all the microstates pile up.
- **Visual object:** A binomial bar-histogram that sharpens from a gentle hump to a single towering spike as $N$ ratchets up.
- **Manim move:** morph (the distribution narrowing) with an $N$ counter climbing
- **Short-form fit:** Strong
- **Prerequisites:** counting arrangements; "most likely" macrostate
- **Exclusions:** skip Stirling's formula on screen; the sharpening animation is the whole idea
- **Score:** 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-multiplicity-peak/vox-multiplicity-peak-review.mp4`

---

## 08 — Build any shape out of pure waves

- **Source:** Vol. 5, M-05 (Fourier Series and the Wave Equation), "Fourier Series: The General Solution"
- **Production mode:** Manim visualization
- **Hook:** Give me enough sine waves and I'll draw you anything — even a square corner.
- **Core idea:** Any shape on an interval is a sum of sine modes; adding successive harmonics, the running total hugs the target ever more tightly. This is exactly the energy-eigenstate expansion of a wavefunction — and the coefficient of each mode is a *projection*, the same operation the Born rule performs.
- **Visual object:** A target curve (parabola, then a square wave) with sine modes stacking one by one, the partial sum snapping toward the target.
- **Manim move:** accumulate (mode-by-mode buildup)
- **Short-form fit:** Strong
- **Prerequisites:** a sine wave; adding functions
- **Exclusions:** a very common "Fourier" visual — differentiate by tying each mode to an eigenstate/Born-rule projection so it earns its place in a QM series; otherwise it's generic
- **Score:** 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-fourier-buildup/vox-fourier-buildup-review.mp4`

---

## 09 — Turn a spinor all the way around and it comes back wrong

- **Source:** Vol. 5, M-01 (Complex Exponential), "Spin: phase factors and spinors" + M-12 spinor rotation
- **Production mode:** Manim visualization
- **Hook:** Rotate an electron a full 360° and it remembers — it's now the *negative* of what it was.
- **Core idea:** The rotation operator carries $e^{\pm i\phi/2}$. A $2\pi$ turn sends the argument to $\pm i\pi$, so the spinor picks up a factor of $-1$; only a $720°$ turn restores it. The half-angle is the whole story, and it has no classical analogue.
- **Visual object:** A spinor arrow (or belt/ribbon) tracked through one full turn landing at $-1$, then a second full turn returning to $+1$, with the $e^{i\phi/2}$ dial ticking at half speed beside it.
- **Manim move:** rotate (object at full speed, phase dial at half speed)
- **Short-form fit:** Strong
- **Prerequisites:** rotation by an angle; a phase factor
- **Exclusions:** overlaps Vol. 2 (Spin) treatments — anchor to Vol. 5's *half-angle in the exponent* framing; don't re-explain spin measurement
- **Score:** 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-spinor-720/vox-spinor-720-review.mp4`

---

## 10 — A packet spreads because its fast parts run ahead

- **Source:** Vol. 5, M-06 (Fourier Transform), "Position and momentum as conjugate Fourier variables (I·8)"
- **Production mode:** Manim visualization
- **Hook:** A quantum particle can't hold its shape — the narrower you make it, the faster it smears.
- **Core idea:** A localized packet is a bundle of momentum components; a narrow $\Delta x$ forces a wide $\Delta p$, and since each momentum travels at its own speed $v=p/m$, the fast and slow parts separate and the packet broadens as $\Delta x(t)=\Delta x(0)\sqrt{1+(t\hbar/m\Delta x(0)^2)^2}$. It's kinematics plus Fourier, not a new postulate.
- **Visual object:** A tight Gaussian packet moving right while visibly flattening and widening, faint color-coded momentum components fanning out inside it.
- **Manim move:** slosh/spread (the packet broadening as components separate)
- **Short-form fit:** Strong
- **Prerequisites:** a wave packet; different momenta move at different speeds
- **Exclusions:** overlaps Vol. 1 (wave packets) — frame it via the Fourier bandwidth cause; pair naturally with card 02
- **Score:** 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-packet-spread/vox-packet-spread-review.mp4`

---

## 11 — Fill in the comb: how a sum becomes an integral

- **Source:** Vol. 5, M-06 (Fourier Transform), "The Transform as the $L\to\infty$ Limit"
- **Production mode:** Manim visualization
- **Hook:** Stretch a box to infinity and the discrete spectrum melts into a continuous one.
- **Core idea:** A periodic function has a Fourier *series* — a discrete comb of allowed wavenumbers spaced $2\pi/L$. Let the period $L$ grow and the comb teeth crowd together until, in the limit, the sum over modes becomes an integral: the Fourier *transform*. Discrete bound states and continuous free states are the two ends of one construction.
- **Visual object:** A spectral comb whose teeth slide together as an $L$ slider grows, densifying into a smooth continuous envelope.
- **Manim move:** morph (comb densifying into a continuum)
- **Short-form fit:** Medium
- **Prerequisites:** Fourier series as a set of discrete frequencies
- **Exclusions:** keep it to the visual limit; no $\Delta k = 2\pi/L$ bookkeeping on screen
- **Score:** 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-fourier-continuum/vox-fourier-continuum-review.mp4`

---

## 12 — Square the integral, spin it into polar coordinates

- **Source:** Vol. 5, M-02 (Probability, Normalization, Expectation), "The Gaussian Integral"
- **Production mode:** Mixed (Doodle setup + Manim reveal)
- **Hook:** You can't integrate $e^{-x^2}$ the normal way — so square it and rotate.
- **Core idea:** $\int e^{-x^2}dx$ has no elementary antiderivative. Square it into a 2D integral over the plane, switch to polar coordinates, and the pesky $r$ from the area element makes it trivially integrable — out drops $\sqrt{\pi}$. This one trick underlies every normalization and every $\langle x^2\rangle$ in quantum mechanics.
- **Visual object:** A flat bell curve lifted into a 2D bell surface, then a sweeping polar grid replacing the square grid, collapsing the volume to a single clean number.
- **Manim move:** rotate (Cartesian grid morphing to polar) + accumulate (volume under the surface)
- **Short-form fit:** Medium
- **Prerequisites:** area under a curve; polar coordinates exist
- **Exclusions:** self-contained math gem — resist adding QM context; it stands alone
- **Score:** 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-gaussian-polar/vox-gaussian-polar-review.mp4`

---

## 13 — Why $m$ has to be a whole number

- **Source:** Vol. 5, M-10 (Multivariable Calculus and Separation of Variables), "Regularity quantizes $m$"
- **Production mode:** Manim visualization
- **Hook:** The magnetic quantum number is an integer — and nobody had to postulate it.
- **Core idea:** The azimuthal part of a wavefunction is $\Phi(\phi)=e^{im\phi}$. Walk once around the atom ($\phi\to\phi+2\pi$) and the wave must meet itself smoothly, which forces $e^{2\pi im}=1$ — so $m$ must be a whole number. Quantization here is nothing but single-valuedness: the wave has to close up on itself.
- **Visual object:** A phase wave wrapped around a ring; integer $m$ closes seamlessly, a non-integer $m$ leaves a visible jump/discontinuity where the ends fail to meet.
- **Manim move:** trace (wave winding the ring) with a mismatch snap for non-integer values
- **Short-form fit:** Strong
- **Prerequisites:** a wave has a phase; going around a circle returns you to the start
- **Exclusions:** note the spin caveat (SU(2) allows half-integers) in one line, don't expand it
- **Score:** 7/10

---

## 14 — Tunneling: one ångstrom, one order of magnitude

- **Source:** Vol. 5, M-13 (Logarithms, Exponentials, and Scales), "The Exponential in the Classically Forbidden Region" + STM example
- **Production mode:** Manim visualization
- **Hook:** Move an STM tip by the width of one atom and the current drops tenfold.
- **Core idea:** Transmission through a barrier is $T=e^{-2\kappa L}$ — exponential in width. Every $2.3$ units of $2\kappa L$ costs a factor of ten, so a barrier a couple of atoms wider goes from "leaky" to "opaque." That savage sensitivity is exactly what lets a scanning tunneling microscope resolve single atoms: current changes by a factor of $e$ per ångstrom of tip height.
- **Visual object:** A decaying exponential inside a barrier whose tail height plunges on a log-scaled meter as a width slider nudges outward; paired STM tip creeping over an atomic bump with the current needle swinging.
- **Manim move:** scan (width slider) with a log-scale transmission readout collapsing
- **Short-form fit:** Strong
- **Prerequisites:** particles can cross a barrier they "shouldn't"; exponential decay
- **Exclusions:** overlaps Vol. 1 (barrier penetration) — this card's angle is the *exponential-sensitivity/STM* framing, not the tunneling setup itself
- **Score:** 7/10

---

---

slate cut 

## Candidate 15 — Why Three Particles in Two States Give Only One Arrangement
- Source: `quantum-mechanics-vol5/chapters/14-combinatorics-and-multiplicity.md`
- Topic: QUANTUM MECHANICS
- Hook: Two identical particles in two states should have four arrangements — but for electrons there is only one.
- Key case: Two electrons, two spin states: the naive count gives four configurations (both up, both down, one each twice). For fermions the Pauli exclusion principle collapses this to one: one in each state. Period.
- The Question: Classical probability theory predicts four arrangements for two particles in two slots. Place quantum electrons in the same setup and the count drops to one. Why?
- Core idea: Identical fermions are not distinguishable — swapping them creates no new microstate, and an antisymmetric wavefunction (Slater determinant) vanishes identically when two particles occupy the same state, making double-occupancy literally impossible.
- Visual object: A three-row comparison grid — four squares for distinguishable particles, three for bosons, one for fermions — with occupied states shown as filled circles arriving one by one into each row
- Manim move: accumulate
- Example seed: A physics instructor assigns 2 indistinguishable students to 2 chairs; she lists 4 seating charts on the board, then realizes identical-particle quantum rules delete 3 of them, leaving only the antisymmetric one.
- Length band: 2–3 min
- Still lanes: geo (grid of state slots), c2v (particle icons)
- Prerequisites: what a quantum state is; that electrons are identical
- Exclusions: no Slater determinant algebra on screen; no Gibbs paradox derivation; no connection to superconductivity or Bose-Einstein condensation
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-fermion-counting/vox-fermion-counting-review.mp4`

## Candidate 16 — Why the Electron Wave Moves at Half the Electron's Speed
- Source: `quantum-mechanics-vol5/chapters/18-trigonometry-waves-and-the-harmonic-model.md`
- Topic: QUANTUM MECHANICS
- Hook: A quantum matter wave has two speeds — and the one you can see is the wrong one.
- Key case: An electron moving at speed $v$ has a de Broglie wave. Track the wave crests: they advance at $v/2$. Track the envelope of a wave packet: it advances at $v$. Two different speeds, same particle, same moment.
- The Question: A de Broglie wave is supposed to represent a moving electron. Its phase velocity works out to $v/2$ — half the electron's speed. If the wave represents the particle, why is it moving at the wrong speed?
- Core idea: The particle's position is carried by the envelope (group velocity), not the wave crests (phase velocity). The envelope is formed by the beat between nearby momentum components and travels at $d\omega/dk = p/m = v$; the crests travel at $\omega/k = p/2m$. The electron rides the envelope, not the crests.
- Visual object: A moving wave packet with visible crests drifting slowly through the faster-moving envelope, a reference pin anchored to the peak of the envelope tracking at full speed while crests slip backward through it
- Manim move: compare
- Example seed: An electron accelerated through 100 V has speed roughly $6 \times 10^6$ m/s. Its wave crests move at $3 \times 10^6$ m/s. A detector placed 1 cm away at the packet peak position clicks at the right time; a detector tracking the crests would predict the electron arrives at the wrong position.
- Length band: 2–3 min
- Still lanes: geo (wave packet with crest and envelope marked separately)
- Prerequisites: a wave has crests; a wave packet is a localized bundle; de Broglie relates wavelength to momentum
- Exclusions: no derivation of the full dispersion relation; no relativistic case; no connection to the Schrödinger equation's time evolution
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-group-velocity/vox-group-velocity-review.mp4`

slate cut 

## Candidate 17 — Why the Band Gap Width Is Just a Fourier Coefficient
- Source: `quantum-mechanics-vol5/chapters/05-fourier-series-and-the-wave-equation.md`
- Topic: QUANTUM MECHANICS
- Hook: The size of a forbidden energy gap in a crystal is not a complicated many-body result — it's one number from a Fourier table.
- Key case: Two free-electron plane waves with momenta $\hbar k$ and $\hbar(k - 2\pi/a)$ have the same kinetic energy at the first Brillouin zone boundary. A periodic crystal potential with Fourier coefficient $V_1 = -0.5$ eV at the matching spatial frequency mixes them. The resulting energy gap is exactly $2|V_1| = 1.0$ eV — no more, no less.
- The Question: Free electrons at the Brillouin zone boundary are degenerate — two states, same energy. Add a weak periodic potential and a gap appears. The gap width should depend on the complicated details of the lattice. Here it only depends on one Fourier coefficient. Why?
- Core idea: The periodic potential scatters only plane-wave pairs that differ in momentum by a reciprocal lattice vector; the matrix element for that scattering is the corresponding Fourier coefficient $V_n$. Only $V_1$ mixes the degenerate pair at the first zone boundary, so the gap splits by exactly $2|V_1|$ — Fourier decomposition selects the one relevant coupling.
- Visual object: A parabolic free-electron dispersion curve that develops a kink and a gap at the zone boundary as a "potential Fourier dial" is turned up, with the gap width reading out as $2|V_1|$
- Manim move: split
- Example seed: A 1D model crystal with lattice spacing 0.3 nm has $V_1 = -0.4$ eV. Students predict the first energy gap is 0.8 eV wide before opening any textbook on band theory.
- Length band: 3–5 min
- Still lanes: geo (dispersion curve, zone boundary, gap bracket), c2v (crystal lattice schematic)
- Prerequisites: free-electron kinetic energy; what a periodic potential is; Fourier series exists
- Exclusions: no Bloch theorem derivation; no tight-binding model; no second or higher Brillouin zones; no many-band effects
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-band-gap-fourier/vox-band-gap-fourier-review.mp4`

slate cut 

## Candidate 18 — Why Measuring Spin in One Direction Destroys What You Knew About Another
- Source: `quantum-mechanics-vol5/chapters/12-matrices-determinants-and-linear-systems.md`
- Topic: QUANTUM MECHANICS
- Hook: You measure an electron's spin along the x-axis and get a definite answer. Now measure along z — and the x answer is gone forever.
- Key case: An electron is prepared in the $|\uparrow_z\rangle$ state (spin-up along z). A student measures spin along x and gets $+\hbar/2$. The state collapses to $|{+x}\rangle = (|{\uparrow}\rangle + |{\downarrow}\rangle)/\sqrt2$. She then measures z again and gets a random answer, 50/50.
- The Question: A spin eigenstate along x is an equal superposition of up and down along z. Measuring x should not affect z-information — the two axes are perpendicular and classically independent. Yet after the x measurement, the z-spin is completely random. Why?
- Core idea: The $\sigma_x$ and $\sigma_z$ Pauli matrices do not commute: $[\sigma_x, \sigma_z] = -2i\sigma_y \ne 0$. Non-zero commutator means no shared eigenbasis: an eigenstate of $\sigma_x$ cannot simultaneously be an eigenstate of $\sigma_z$, so definite x-spin forces indefinite z-spin. Measuring x projects into a basis that scrambles z entirely.
- Visual object: A Bloch sphere where a state starts on the north pole, a measurement arrow points along x and rotates the state to the equator, then a second z-arrow shows the state is now on the equator — equidistant from north and south
- Manim move: rotate
- Example seed: A quantum cryptography lab prepares 1000 photons with vertical polarization. An eavesdropper measures diagonal polarization on each one, getting definite answers. The receiver then checks vertical polarization and finds it randomly 50/50 — the eavesdropper's definite answers destroyed the original information.
- Length band: 2–3 min
- Still lanes: geo (Bloch sphere with measurement axes), c2v (measurement apparatus icon)
- Prerequisites: spin has two possible outcomes along any axis; eigenstates and superpositions; what a measurement does in QM
- Exclusions: no derivation of Pauli algebra; no Robertson inequality; no entanglement; no Bell inequalities
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol5/youtube/vox-spin-measurement/vox-spin-measurement-review.mp4`

slate cut 

## Candidate 19 — Why Quantum Numbers Are Not Postulates
- Source: `quantum-mechanics-vol5/chapters/10-multivariable-calculus-and-separation-of-variables.md`
- Topic: QUANTUM MECHANICS
- Hook: The quantum numbers $n$, $\ell$, $m$ look like labels someone invented — but they fall out of one wave-closure argument, three times in a row.
- Key case: The azimuthal wavefunction is $\Phi(\phi) = e^{im\phi}$. Walk once around the atom ($\phi$ from 0 to $2\pi$) and the wave must close on itself: $\Phi(2\pi) = \Phi(0)$. This forces $e^{2\pi im} = 1$, which can only hold if $m$ is an integer. No postulate was used — only the requirement that the wave has a single value at each point in space.
- The Question: Textbooks list the magnetic quantum number $m$ as an integer by rule. The Schrödinger equation does not contain the word "integer." Where does $m \in \mathbb{Z}$ actually come from?
- Core idea: Single-valuedness — a wavefunction that takes multiple values at the same physical point is unphysical. The azimuthal factor $e^{im\phi}$ wraps around a circle; closing the circle without a phase jump forces $m$ to be a whole number. This is not a postulate: it is a regularity condition, the same argument that enforces nodal patterns in a vibrating drum head.
- Visual object: A phase wave wound around a ring; integer $m$ shows the wave closing seamlessly after one lap; a fractional $m$ shows a visible kink where the end fails to meet the start
- Manim move: trace
- Example seed: A student trying $m = 0.7$ draws the wavefunction around the azimuthal ring and finds a step discontinuity where the wave re-enters its starting point — the wavefunction is multivalued, rejected by physics.
- Length band: 2–3 min
- Still lanes: geo (ring with wound phase wave, closure vs. discontinuity), c2v (atom with ring path highlighted)
- Prerequisites: a wave has a phase; going around a circle returns you to the start; what a wavefunction is
- Exclusions: do not extend to spin-½ half-integer case (SU(2) requires a separate treatment); do not derive the associated Legendre equation; no mention of $n$ or $\ell$ quantization mechanisms
- Score: 7/10

---

## Cutting-room floor (rejected — technique, not motion)

Deliberately excluded because the teaching happens through algebraic manipulation, not by watching something move: Dirac bra–ket type grammar (M-09), the adjoint/Hermitian proofs and Robertson-from-Cauchy–Schwarz (M-09), matrix/determinant/trace mechanics and the Pauli algebra tables (M-12), the characteristic-equation ODE recipe (M-03), Gram–Schmidt bookkeeping (M-07), the Sturm–Liouville orthogonality proof and the special-function catalogue — Hermite/Legendre/Laguerre/Bessel (M-11), tensor-product/Kronecker mechanics and partial trace (M-16, already covered visually in Vol. 4), dimensional-analysis exponent-matching and the Bohr-radius derivation (M-17), the Euler–Lagrange integration-by-parts derivation itself (M-15), and the convolution-theorem proof (M-06). Several of these are excellent *written* explainers; none of them earn a motion-carries-the-teaching video.
