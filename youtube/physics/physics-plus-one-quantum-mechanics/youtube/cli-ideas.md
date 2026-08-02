# Physics Plus One: Quantum Mechanics — CLI Video Ideas ("X with Claude")

---

## Card 1 — Wave Function Probability Density Visualizer

**Source:** Ch 1 (The Wave Function) — Born rule, normalization, Gaussian wave packet evolution

**Lane:** BUILD

**Hook:** "The blue blob isn't the particle — it's a probability density. One command builds the simulation that makes that distinction impossible to forget."

**The artifact:** Animated d3 visualization showing a Gaussian wave packet ψ(x,t) evolving in time: Re ψ (orange), Im ψ (gray dashed), and |ψ|² (blue filled) rendered simultaneously. A probability-in-region gauge shows ∫ₐᵇ |ψ|² dx for a user-draggable interval. Normalization verified in real time (integral displayed). Sliders for initial σ, k₀ (momentum), and time t. Demonstrates spread-without-moving: |ψ|² widens while ⟨x⟩ drifts.

**Prompt seed:** `claude "Build a d3 v7 single-HTML wave-packet visualizer. Gaussian ψ(x,0) = A·exp(−x²/4σ²)·exp(ik₀x). Evolve via free-particle dispersion: ψ(x,t) = ∫ φ(k)exp(ikx−iℏk²t/2m)dk approximated by discrete Fourier sum (64 modes). Render three overlaid curves: Re ψ orange, Im ψ gray dashed, |ψ|² blue filled. Add probability-in-region gauge with two draggable vertical lines showing ∫ |ψ|² dx. Animate with Play/Pause. Sliders for σ (0.5–3 nm), k₀ (0–5 nm⁻¹), time step. Show normalization integral at top. ℏ=1, m=1 atomic units. SVG only, no canvas."`

**Read/check:** Pause at t=0; verify |ψ|² peak coincides with x=0. Advance time; check that peak drifts rightward at group velocity v_g = ℏk₀/m. Check normalization integral stays ≈ 1.000 throughout. Drag region lines; verify gauge updates.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Iterate: change σ from 0.5 nm (narrow packet, broad momentum) to 3 nm (wide packet, slow spread). Watch how the spreading rate scales as 1/σ². Then add a vertical barrier (infinite wall at x = L) and watch reflection and interference fringes form in |ψ|².

**Teardown angle:** "Notice that Im ψ leads Re ψ by exactly 90°. If you tried to set Im ψ = 0 and propagate, the Schrödinger equation rebuilds the imaginary part in the next time step. The phase isn't optional — it carries all the momentum information. Deleting it destroys the physics."

**Exclusions:** Measurement collapse (separate topic). Many-body wave functions. 3D wave packets.

**Score:** 9/10

---

## Card 2 — Infinite Square Well Energy Levels and Superposition

**Source:** Ch 2 (TISE) — infinite square well, energy quantization from boundary conditions, superposition of stationary states

**Lane:** BUILD

**Hook:** "Quantization isn't assumed — it falls out of one requirement: the wave function must be continuous at a hard wall. Build the demo that proves it."

**The artifact:** Animated d3 scene: an infinite square well of width L (adjustable). Left panel shows the first 5 energy levels Eₙ = n²π²ℏ²/(2mL²) on a vertical energy axis, with the user selecting any combination of n=1–5 as a superposition. Right panel animates |ψ(x,t)|² = |Σ cₙψₙ(x)e^{−iEₙt/ℏ}|² in real time. Coefficients cₙ are sliders (normalized automatically). A "charge-and-watch" beat: set c₁=c₂=1/√2; observe the |ψ|² sloshing back and forth at frequency (E₂−E₁)/h.

**Prompt seed:** `claude "Build d3 v7 single-HTML infinite square well simulator. Eigenstates ψₙ(x) = √(2/L)sin(nπx/L), energies Eₙ = n²·E₁ where E₁ = π²ℏ²/(2mL²). Set ℏ=m=1, L=1 by default. Time-evolve superposition ψ(x,t) = Σ cₙψₙ(x)exp(−iEₙt). Render Re ψ (orange), Im ψ (gray dashed), |ψ|² (blue filled) — three curves on same axes. Show 5 coefficient sliders (c₁–c₅, renormalized). Add energy level diagram on left panel; highlight occupied levels with circle size proportional to |cₙ|². Animate with requestAnimationFrame. SVG only, no canvas."`

**Read/check:** Set c₁=1, all others 0. Verify |ψ|² is stationary (only the global phase e^{−iE₁t} rotates Re/Im, but density is static). Set c₁=c₂=1/√2. Verify the density sloshes with period T = h/(E₂−E₁) = 2π/(E₂−E₁) in natural units.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Slide the well width L: all energy levels scale as 1/L². Narrow the well; all levels shoot up. Note that the *ratio* E₂/E₁ = 4 is universal — it doesn't change with L. Then set c₁=c₂=c₃=1/√3 and observe more complex beating.

**Teardown angle:** "Every energy eigenstate is a stationary state — |ψ|² is time-independent, Re and Im oscillate at fixed frequency. The moment you add even one other state, the density starts moving. This is why superposition is the engine of all quantum dynamics."

**Exclusions:** Finite square well (tunneling into classically forbidden region — separate card). 3D box.

**Score:** 8/10

---

## Card 3 — Quantum Harmonic Oscillator: Ladder Operators and Coherent States

**Source:** Ch 3 (Harmonic Oscillator) — ladder operators â₊/â₋, energy levels Eₙ = (n+½)ℏω, coherent states as minimum-uncertainty classical-like oscillation

**Lane:** BUILD

**Hook:** "One commutation relation [â₋, â₊] = 1 generates the entire energy ladder. Build the visualizer that climbs it."

**The artifact:** Animated d3: left panel shows the harmonic potential V(x) = ½mω²x² with the first 6 energy levels and their eigenstates ψₙ(x) (Hermite-Gaussian wavefunctions). Right panel allows the user to build a coherent state |α⟩ = e^{−|α|²/2} Σ (αⁿ/√n!) |n⟩. The coherent state's |ψ(x,t)|² animates as a Gaussian oscillating back and forth without spreading — mimicking classical oscillation. Probability distribution under the curve at every frame. Uncertainty product σₓσₚ shown in real time (should stay at ℏ/2 for coherent states).

**Prompt seed:** `claude "Build d3 v7 single-HTML quantum harmonic oscillator visualizer. Natural units ℏ=m=ω=1. Eigenstates: ψₙ(x) = (1/√(2ⁿn!π^½)) exp(−x²/2) Hₙ(x) where Hₙ are Hermite polynomials (compute up to n=8 recursively). Energy levels Eₙ = n+0.5. Left panel: potential V(x)=x²/2 with eigenstates plotted as offset curves on energy axis. Right panel: coherent state |α⟩ evolved in time — decompose into Fock basis, time-evolve each component, sum. Animate |ψ(x,t)|² as filled blue curve oscillating. Display ⟨x⟩, ⟨p⟩, σx·σp in real time. Slider for |α| (0–3). SVG only."`

**Read/check:** Set α=0 (ground state). Verify the density is stationary and σₓσₚ = 0.5 (minimum uncertainty). Set α=2; verify ⟨x⟩(t) = 2cos(t) (classical oscillation). Verify density shape stays Gaussian and σₓσₚ stays at 0.5.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Increase |α| from 0 to 3. The classical oscillation amplitude grows linearly with |α|. At large |α|, the coherent state looks exactly classical — the quantum blob becomes indistinguishable from a classical oscillating particle. Then switch to a Fock state superposition (c₁=c₃=1/√2) and show that the density now distorts non-classically.

**Teardown angle:** "The zero-point energy E₀ = ℏω/2 is not a rounding error. Casimir force and liquid helium's refusal to freeze at zero pressure are direct macroscopic consequences. The coherent state saturates the uncertainty bound — it's the most 'classical' quantum state possible, but it still can't violate ℏ/2."

**Exclusions:** Anharmonic oscillator. Squeezed states (require complex α). 3D harmonic oscillator.

**Score:** 8/10

---

## Card 4 — Bloch Sphere Spin-½ Simulator with Larmor Precession

**Source:** Ch 6 (Spin) — Pauli matrices, Bloch sphere parameterization, Larmor precession in magnetic field, Born rule on Bloch sphere

**Lane:** BUILD

**Hook:** "A spin-½ state is a point on a sphere. One command builds the 3D Bloch sphere that makes the Born rule geometric."

**The artifact:** Animated d3 scene showing the Bloch sphere (rendered as SVG with projected 3D circles for equator and meridians). User sets state (θ, φ) and analyzer direction (θₙ, φₙ) with sliders. Born rule probability P(+) = cos²(γ/2) displayed numerically and as a color gradient on the sphere. When "Larmor precession" mode enabled, the state vector precesses around the z-axis at ω_L. The azimuthal angle φ(t) = ω_L·t animates in real time. ⟨Sx⟩, ⟨Sy⟩, ⟨Sz⟩ plotted as time series below the sphere.

**Prompt seed:** `claude "Build d3 v7 single-HTML Bloch sphere visualizer. Render the sphere as SVG projection: equator as an ellipse, three meridian arcs, north pole labeled |↑⟩, south pole |↓⟩. Show a state arrow from origin to point (θ, φ) and an analyzer arrow at (θₙ, φₙ) — both draggable via sliders. Compute angle γ between them using cos γ = cos θ·cos θₙ + sin θ·sin θₙ·cos(φ−φₙ). Display P(+) = cos²(γ/2). Add Larmor mode: φ(t) = φ₀ + ω_L·t with adjustable ω_L. Plot ⟨Sx⟩=sin θ cos φ, ⟨Sy⟩=sin θ sin φ, ⟨Sz⟩=cos θ as time-series line chart. SVG only."`

**Read/check:** Place state at north pole (θ=0). Set any analyzer direction. Verify P(+)=1.000. Move state to south pole (θ=π). Verify P(+)=0.000. Set state at equator (θ=π/2) and analyzer at north pole. Verify P(+)=0.500. Enable Larmor precession; verify ⟨Sx⟩ and ⟨Sy⟩ oscillate sinusoidally 90° out of phase while ⟨Sz⟩ is constant.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Iterate: set the Larmor frequency to match the proton NMR frequency ω_L = γ_p B₀ with B₀ = 1 T (γ_p/2π = 42.58 MHz). Show that MRI is just watching millions of proton Bloch vectors precess in unison. Then tilt the initial state to the equator and watch the free precession that is the FID signal.

**Teardown angle:** "A 2π rotation in physical space sends the Bloch vector around the sphere but multiplies the spinor by −1. Only a 4π rotation restores the state identically. This is the spinor double cover: spin lives in SU(2), not SO(3). The sign flip is observable in neutron interferometry."

**Exclusions:** Mixed states / density matrix (requires density matrix formalism). Entangled pairs on separate Bloch spheres. Decoherence.

**Score:** 9/10

---

## Card 5 — Hydrogen Atom Radial Wave Functions and Orbital Densities

**Source:** Ch 7 (Hydrogen Atom) — Laguerre polynomials, radial probability density r²|R_{nl}|², Bohr radius, energy levels Eₙ = −13.6 eV/n²

**Lane:** BUILD

**Hook:** "The Bohr radius wasn't assumed — it fell out of the calculation. Build the radial density plotter that shows exactly where the electron is likely to be."

**The artifact:** Animated d3 multi-panel visualization. Top: radial probability density r²|Rₙₗ(r)|² for any (n, l) pair selected from a dropdown (n=1–4, l=0 to n−1). Shows Bohr radii, the most-probable radius, ⟨r⟩, and the number of radial nodes (n−l−1). Bottom panel: animated "electron cloud" using |Ψₙₗ₀(r,θ)|² rendered as a density heat map in the r-θ plane (axially symmetric, so 2D slice). Side panel: energy level diagram; clicking a level animates the transition from n_i to n_f and computes the photon wavelength λ.

**Prompt seed:** `claude "Build d3 v7 single-HTML hydrogen atom radial probability density visualizer. Compute Rₙₗ(r) using associated Laguerre polynomials Lₙ₋ₗ₋₁^{2l+1}(2r/na₀) (implement recursively for n up to 4). Plot r²|Rₙₗ|² vs r/a₀ for user-selected (n,l) pairs. Mark the most-probable radius, ⟨r⟩=a₀n²[3/2−l(l+1)/(2n²)], and radial nodes with vertical dashed lines. Bottom panel: heat map of |ψₙₗ₀|²=|Rₙₗ(r)|²|Y_l^0(θ)|² in (r·sin θ, r·cos θ) plane, 200×200 grid. Right panel: energy level diagram −13.6/n² eV; click to animate transition arrow and display photon wavelength. SVG only, no canvas."`

**Read/check:** Select (n=1, l=0). Verify peak of r²|R₁₀|² at r = a₀ = 0.529 Å. Select (n=2, l=0). Verify two peaks with one node between them. Select (n=2, l=1). Verify peak at r ≈ 5a₀ with zero at origin. Click transition 3→2: verify λ ≈ 656 nm (Balmer Hα).

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Compare (n=2,l=0) — the 2s state with a lobe at the nucleus — to (n=2,l=1) — the 2p state with zero density at the nucleus. Explain: only s-states can interact with the nucleus through hyperfine coupling. Switch to muonic hydrogen: substitute mμ = 207mₑ into a₀ = ℏ²/μe². Watch the entire density distribution collapse to 1/207 of its normal size.

**Teardown angle:** "The electron never 'orbits' in any classical sense. The 2p orbital is a probability cloud, not a path. The probability density at the nucleus is zero for ℓ≥1 — that's not a feature of hydrogen specifically, it's forced by the centrifugal barrier ℏ²ℓ(ℓ+1)/(2mr²) diverging at r=0."

**Exclusions:** Multi-electron atoms (need Slater determinants). Relativistic corrections (fine structure). Stark/Zeeman effect.

**Score:** 9/10

---

## Card 6 — WKB Tunneling Transmission Through a Potential Barrier

**Source:** Ch 11 (WKB Approximation and Tunneling) — WKB transmission coefficient, Gamow factor, alpha decay lifetimes

**Lane:** BUILD

**Hook:** "Alpha particles escape uranium nuclei by tunneling through a barrier 30 MeV high. The WKB approximation gives the decay lifetime to within an order of magnitude. Build it in 40 lines."

**The artifact:** Animated d3 visualization of a particle (energy E) incident on a potential barrier V(x) of adjustable height V₀ and width a. Left panel: the barrier and the particle energy as horizontal line; classically forbidden region shaded. Right panel: WKB transmission coefficient T = exp(−2∫|κ(x)|dx) where κ(x) = √(2m(V(x)−E))/ℏ, plotted as a function of E/V₀ from 0 to 1. Second chart: T vs. barrier width a (exponential dependence). Alpha-decay application: plug in Coulomb barrier V(r) = 2Ze²/(4πε₀r), get Gamow factor G = 2∫_{R_nucleus}^{R_classical} κ(r)dr and lifetime τ ∝ e^G for different nuclei (U-238, Po-212, Rn-220).

**Prompt seed:** `claude "Build d3 v7 single-HTML WKB tunneling calculator. Left panel: rectangular barrier V(x)=V₀ for 0<x<a, V=0 elsewhere. Draw potential with gray fill in forbidden region. Horizontal line at energy E. Right panel: compute T=exp(−2·κ·a) where κ=sqrt(2m(V₀−E))/ℏ (set m=ℏ=1 atomic units). Plot T vs E/V₀ and vs barrier width a on separate charts. Below: Gamow factor mode — integrate κ(r) numerically over Coulomb barrier 2Ze²/r from nuclear radius R₁ to classical turning point R₂; show G for U-238, Po-212, Rn-220 as bar chart with half-lives labeled. SVG only."`

**Read/check:** Set E = V₀/2, a = 1 atomic unit. Read T from the plot and verify manually against exp(−2·1·√(2·1·0.5)) = exp(−2). For Gamow factor: U-238 (Z=90, A=238) half-life ~4.5 Gyr; Po-212 half-life ~0.3 μs — span of 24 orders of magnitude from barrier geometry alone.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Iterate: slide E from 0 to V₀. Watch T transition from exponentially suppressed to T=1 at E=V₀ (above-barrier transmission). Note the exponential sensitivity: doubling the barrier width halves the exponent and squares T. This is why scanning tunneling microscopes can achieve sub-Ångström vertical resolution — one atomic layer changes the tunneling current by an order of magnitude.

**Teardown angle:** "The WKB result is semiclassical — it treats the particle as a wave only in the forbidden region. It breaks down near the turning points (where E = V and κ → 0) because the wavelength diverges there and the 'slowly varying' approximation fails. Connection formulas patch the solution, but for wide barriers the exponential is overwhelmingly dominant and the WKB result is excellent."

**Exclusions:** Resonant tunneling (double barrier). Parabolic barrier (exact Gamow). Time-dependent tunneling rates.

**Score:** 8/10

---

## Card 7 — Entanglement and Bell Inequality Checker

**Source:** Ch 12 (Entanglement and Quantum Information) — Bell states, CHSH inequality, quantum correlation vs. classical hidden variable bound

**Lane:** BUILD

**Hook:** "Bell proved that no hidden variable theory can reproduce all of quantum mechanics' predictions. Build the simulation that shows exactly where classical physics fails."

**The artifact:** Interactive d3 scene. User selects a two-qubit state: product state or one of the four Bell states (Φ±, Ψ±). Two measurement angles α (Alice) and β (Bob) are independently adjustable. The correlation function E(α,β) = ⟨ψ|σ_α⊗σ_β|ψ⟩ is computed analytically and displayed. The CHSH parameter S = |E(α,β) − E(α,β') + E(α',β) + E(α',β')| is computed for the current four-angle setting. Classical bound: S ≤ 2. Quantum maximum: S = 2√2 ≈ 2.828. Visual: a unit-circle diagram showing where the four measurement axes fall, with CHSH value as large readout. Animation: sweep β from 0° to 360° and watch S cross 2 — into the "forbidden" classical region.

**Prompt seed:** `claude "Build d3 v7 single-HTML Bell inequality simulator. User selects from: product state |00⟩, or Bell states Φ+=(|00⟩+|11⟩)/√2, Φ−=(|00⟩−|11⟩)/√2, Ψ+=(|01⟩+|10⟩)/√2, Ψ−=(|01⟩−|10⟩)/√2. Four angle sliders α, α', β, β' (0°–180°). Compute E(θ_A, θ_B) = cos(2(θ_A−θ_B)) for maximally entangled states. Display CHSH S = |E(α,β)−E(α,β')+E(α',β)+E(α',β')|. Show red line at S=2 (classical bound) and dashed line at S=2√2 (quantum max). Plot E vs angle β as a sweep animation. Unit circle diagram showing all four measurement directions. SVG only."`

**Read/check:** Select Φ+ state. Set α=0°, α'=45°, β=22.5°, β'=67.5° (optimal CHSH angles). Verify S ≈ 2.828 = 2√2. Switch to product state |00⟩. Verify S ≤ 2 for all angle choices.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Sweep β from 0° to 360° and watch S oscillate, peaking at 2√2 at the optimal angles and dipping below 2 elsewhere. Note: S > 2 is a signature of entanglement — no local hidden variable model can produce it. The Aspect experiments (1982) and loophole-free Bell tests (2015) confirmed S > 2 with measurement outcomes.

**Teardown angle:** "The violation of Bell's inequality doesn't mean signals travel faster than light. The correlations are nonlocal in the sense that no pre-agreed strategy can reproduce them — but you need classical communication to compare outcomes and see the correlation. The quantum correlations only become visible after the comparison. Quantum mechanics is nonlocal in correlations, not in signaling."

**Exclusions:** Density matrix / mixed state entanglement. Entanglement entropy. Quantum key distribution (BB84).

**Score:** 9/10

---

## Card 8 — Identical Particles: Fermi-Dirac vs. Bose-Einstein Occupation Statistics

**Source:** Ch 8 (Identical Particles) — exchange symmetry, Pauli exclusion, Slater determinants, Fermi-Dirac and Bose-Einstein distributions

**Lane:** BUILD

**Hook:** "One symmetry requirement — antisymmetry under exchange — and the periodic table is inevitable. Build the simulation that shows why fermions and bosons behave oppositely."

**The artifact:** d3 visualization with two panels side by side. Left panel: fermions. Right panel: bosons. A set of 6 energy levels (evenly spaced) is shown. User selects total particle count N. For fermions: particles fill from the bottom (Pauli exclusion — at most one per level). At finite temperature T, the Fermi-Dirac distribution f(E) = 1/(exp((E−μ)/kT)+1) governs occupation. For bosons: Bose-Einstein distribution f(E) = 1/(exp((E−μ)/kT)−1). Animation: sweep temperature from T=0 to T=5·E₁/k. At T=0 for fermions: sharp Fermi step. At T=0 for bosons: all in ground state (BEC). Show occupation bar chart evolving.

**Prompt seed:** `claude "Build d3 v7 single-HTML Fermi-Dirac vs Bose-Einstein occupation visualizer. Six energy levels E_n = n (n=1..6). Sliders: N particles (2–10), temperature T (0.01–5 in units of E₁/k_B). Left panel (fermions): FD occupation f_n = 1/(exp((E_n−μ_F)/T)+1), find μ_F numerically by solving Σf_n = N using bisection. Right panel (bosons): BE occupation f_n = 1/(exp((E_n−μ_B)/T)−1), find μ_B by bisection (μ_B < E_1). Render horizontal bar chart: bar width = occupation fraction. Label each bar with f_n. At T→0: left panel shows step function; right panel shows all particles in E_1. Animate T sweep. SVG only."`

**Read/check:** Set N=3, T=0.01 (near zero). Fermion panel should show f₁=f₂=f₃=1, f₄=f₅=f₆≈0. Boson panel should show f₁≈3 (all in ground state), all others ≈0. Raise T to 3: verify both distributions broaden. Verify Σf_n = N (displayed) stays at 3.

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Sweep N from 2 to 6 at low T for fermions. Each added particle must step to the next level — Pauli exclusion forces sequential filling. This is the shell structure of atoms: the periodic table is Fermi-Dirac statistics applied to Coulomb potential levels. For bosons at very low T and large N, show the dramatic pileup at the ground state — Bose-Einstein condensation, experimentally achieved in 1995 (Nobel Prize).

**Teardown angle:** "The Slater determinant that antisymmetrizes the N-body fermion wave function has one elegant consequence: if any two particles are in the same state, two rows of the determinant are identical, and the determinant is zero. The Pauli exclusion principle is not a separate postulate — it is a theorem of antisymmetry."

**Exclusions:** Second quantization (field operators). Fractional statistics / anyons. Degenerate electron gas pressure in white dwarfs (though that's in the astronomy card set).

**Score:** 8/10

---

## Card 9 — Time-Independent Perturbation Theory: First-Order Energy Corrections

**Source:** Ch 9 (Time-Independent Perturbation Theory) — first- and second-order corrections, selection rules, degenerate perturbation theory

**Lane:** BUILD

**Hook:** "The hydrogen spectrum isn't perfect — fine structure, Zeeman splitting, Stark shift are all perturbation theory. Build the calculator that shows how small perturbations shift the levels."

**The artifact:** d3 multi-panel visualization. Choose unperturbed system: (1) infinite square well, or (2) harmonic oscillator. Choose perturbation: triangular (H' = ε·x/L), quadratic (H' = ε·x²), or delta spike (H' = ε·δ(x−x₀)). Compute first-order energy corrections Eₙ⁽¹⁾ = ⟨n|H'|n⟩ numerically (matrix elements integrated on a grid). Show the unperturbed spectrum on the left and the shifted spectrum on the right, with correction magnitudes displayed. Slider for perturbation strength ε (0 to 0.5E₁). Second panel: for 2-fold degenerate case (two-level crossing), diagonalize the 2×2 subspace matrix and show avoided crossing.

**Prompt seed:** `claude "Build d3 v7 single-HTML perturbation theory visualizer. Unperturbed: infinite square well, eigenstates ψₙ(x)=√(2/L)sin(nπx/L), energies Eₙ=n²E₁. Perturbation options: triangular H'=ε·x/L, quadratic H'=ε·(x−L/2)², delta H'=ε·δ(x−L/2) (approximate as narrow Gaussian). Compute matrix elements H'_{mn}=∫ψₘ H' ψₙ dx numerically (1000-point grid). Show first-order corrections E_n^(1)=H'_nn as bar chart overlaid on energy diagram. Second-order: Eₙ⁽²⁾=Σ_{m≠n} |H'_{mn}|²/(Eₙ−Eₘ). Sliders: ε (0–0.3), perturbation type, n_max (1–6). SVG only."`

**Read/check:** For triangular perturbation H'=ε·x/L on infinite square well: first-order correction E₁⁽¹⁾ = ε·⟨1|x/L|1⟩ = ε/2 (by symmetry, since ⟨x⟩=L/2 for any symmetric well state). Verify numerically. For even-parity perturbation (quadratic), verify that matrix elements H'_{mn} between even-n and odd-n states are zero (selection rule from parity).

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Sweep ε from 0 to 0.3. Watch all levels shift — some up, some down, depending on the sign of H'_nn. Note that for a triangular perturbation, all corrections are positive (perturbation raises energy on average). Then enable second-order corrections and show which levels shift further — levels closest in energy to others get the largest second-order shifts.

**Teardown angle:** "Perturbation theory fails when two levels are nearly degenerate — the second-order term Σ |H'_{mn}|²/(Eₙ−Eₘ) blows up when Eₙ ≈ Eₘ. The fix is degenerate perturbation theory: diagonalize H' in the degenerate subspace first. The eigenvalues of that 2×2 matrix give the zeroth-order corrections that resolve the degeneracy."

**Exclusions:** Time-dependent perturbation theory (Fermi's golden rule — separate chapter). Variational method. Stark effect on hydrogen (requires spherical harmonics).

**Score:** 7/10

---

## Card 10 — Schrödinger Equation Numerical Solver: Shooting Method

**Source:** Ch 2, 5, 7 (TISE, 3D, Hydrogen) — numerical eigenvalue finding, arbitrary 1D potentials, finite difference shooting method

**Lane:** BUILD

**Hook:** "Most quantum mechanics problems have no analytic solution. Build the numerical solver that finds energy levels for any 1D potential in 40 lines."

**The artifact:** d3 interactive scene. Left panel: a potential V(x) constructed by the user as a piecewise function — presets include square well, harmonic, double well, Morse potential. User adjusts parameters (depth, width, asymmetry). The shooting method: Claude integrates the TISE numerically from x=0 outward, shooting from ψ(0)=0 with a trial energy E. The wave function is displayed growing or diverging. Right panel: plot of ψ(x_max) vs. trial E — zeros of this function are the eigenvalues. Clicking a zero loads that eigenfunction into the left panel. The bound-state count vs. well depth is tracked.

**Prompt seed:** `claude "Build d3 v7 single-HTML 1D Schrödinger equation shooting-method solver. Integrate ψ''(x) = 2m(V(x)−E)/ℏ² · ψ(x) using 4th-order Runge-Kutta (1000 steps, x=0 to L=10, ℏ=m=1). Boundary conditions: ψ(0)=0, ψ'(0)=0.01. Preset potentials: (1) infinite square well V=0 inside, ∞ outside, (2) harmonic V=0.5x², (3) double well V=0.5(x²−a)², (4) Morse V=D(1−exp(−αx))². Right panel: plot ψ(L, E) vs E sweeping from E=0 to E_max=10; mark zeros (eigenvalues) with dots. Click a zero to plot its eigenfunction in left panel. Display node count. Sliders for well parameters. SVG only."`

**Read/check:** Select infinite square well, L=10, E₁_expected = π²ℏ²/(2mL²) = 0.049 in atomic units. Verify first zero of shooting function at E ≈ 0.049. Verify eigenfunction has zero nodes. Select harmonic V=0.5x²; verify zeros at E = 0.5, 1.5, 2.5 (evenly spaced with spacing 1 = ℏω = 1).

**Human supplies:** Nothing — fully synthetic.

**Output medium:** d3 animated HTML (single file, SVG, CDN).

**The change:** Switch to double-well potential V = 0.5(x²−a)²; sweep the barrier height by varying a from 0 to 2. Watch the degenerate pair (ground state and first excited state) split apart as the barrier grows. At large barrier, the two lowest states become nearly degenerate — symmetric and antisymmetric combinations of states localized in each well. This is the quantum tunneling splitting, directly analogous to the inversion doubling in the ammonia molecule (used in the first maser).

**Teardown angle:** "The shooting method works for any smooth 1D potential — the analytic solutions (Hermite functions, Laguerre polynomials, spherical harmonics) are just the shooting method's output for special cases where the recursion terminates. For everything else, this algorithm is what you use."

**Exclusions:** 2D or 3D potentials (require finite elements or matrix diagonalization). Scattering states (need different boundary conditions at both ends). Complex potentials.

**Score:** 8/10

---

| Book | Status | Lane | Candidates |
|------|--------|------|------------|
| physics-plus-one-quantum-mechanics | SCOUTED | BUILD | 10 |
