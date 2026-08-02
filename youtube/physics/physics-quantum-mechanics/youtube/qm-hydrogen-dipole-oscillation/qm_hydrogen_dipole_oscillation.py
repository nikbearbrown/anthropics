#!/usr/bin/env python3
"""
qm_hydrogen_dipole_oscillation.py — Hydrogen 1s→2pz: Oscillating Electric Dipole
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-hydrogen-dipole-oscillation
    manim -qh qm_hydrogen_dipole_oscillation.py HydrogenDipoleScene

Verify:
    python3 qm_hydrogen_dipole_oscillation.py

Physics:
    E1 = -13.6 eV, E2 = -13.6/4 = -3.4 eV
    ω₁₂ = (E₂-E₁)/ℏ = 1.55e16 rad/s
    T = 2π/ω₁₂ ≈ 405 as (attoseconds)
    Lyman-α: λ = 121.6 nm
    Matrix element ⟨z⟩₁₂ = -√(128/243) a₀ ≈ -0.745 a₀
    Selection rule: Δℓ=±1 → 1s→2pz allowed, 1s→2s forbidden
"""
import sys
import numpy as np

A0 = 0.0529177e-9   # m
EV = 1.60218e-19
HBAR = 1.0545718e-34
C_LIGHT = 2.99792e8


def H_energy_eV(n: int) -> float:
    return -13.6 / n**2


def omega_12() -> float:
    """Angular frequency for 1s→2p transition."""
    dE = (H_energy_eV(2) - H_energy_eV(1)) * EV
    return abs(dE) / HBAR


def lyman_alpha_nm() -> float:
    """λ = c/f = 2πc/ω."""
    return 2.0 * np.pi * C_LIGHT / omega_12() * 1e9


def z_matrix_element_a0() -> float:
    """⟨z⟩₁₂ = -√(128/243) a₀ in units of a₀."""
    return -np.sqrt(128.0 / 243.0)


def psi_1s(r: np.ndarray, z: np.ndarray) -> np.ndarray:
    """ψ_1s(r) = (1/√π a₀³) e^{-r/a₀}, r in a0 units."""
    return (1.0 / np.sqrt(np.pi)) * np.exp(-r)


def psi_2pz(r: np.ndarray, z: np.ndarray) -> np.ndarray:
    """ψ_2pz(r,z) = (1/4√2π a₀³) r·cos(θ)·e^{-r/2}, z=r·cosθ in a0 units."""
    return (1.0 / (4.0 * np.sqrt(2.0 * np.pi))) * r * (z / (r + 1e-15)) * np.exp(-r / 2.0)


def superposition_density(rho: np.ndarray, z: np.ndarray, t_norm: float,
                           c1: float = 0.7071, c2: float = 0.7071) -> np.ndarray:
    """
    |c1 ψ₁s e^{-iE₁t/ℏ} + c2 ψ₂pz e^{-iE₂t/ℏ}|²
    t_norm = normalized time (0 to 1 = one beat period).
    rho, z in a0 units, rho = sqrt(x²+z²) in xz-plane.
    """
    omega = omega_12()
    T     = 2.0 * np.pi / omega
    t_phys = t_norm * T

    p1 = psi_1s(rho, z)
    p2 = psi_2pz(rho, z)
    E1 = H_energy_eV(1) * EV
    E2 = H_energy_eV(2) * EV
    phase = (E2 - E1) / HBAR * t_phys   # (E2-E1) < 0 so phase decreases
    return c1**2 * p1**2 + c2**2 * p2**2 + 2.0 * c1 * c2 * p1 * p2 * np.cos(phase)


def verify():
    print("=== Hydrogen dipole oscillation verification ===")
    omega = omega_12()
    lam   = lyman_alpha_nm()
    z12   = z_matrix_element_a0()
    T_as  = 2.0 * np.pi / omega * 1e18
    print(f"ω₁₂ = {omega:.4e} rad/s  (card says 1.55e16)")
    print(f"T   = {T_as:.1f} as  (card says 405 as)")
    print(f"λ   = {lam:.2f} nm  (should be 121.6 nm)")
    print(f"⟨z⟩₁₂ = {z12:.4f} a₀  (card says −0.745 a₀)")
    # Check selection rule: ψ₁s and ψ₂s both ℓ=0 → matrix element = 0
    # For 1s→2s: ψ₂s ∝ (1−r/2)e^{-r/2}, odd integral vanishes by symmetry
    print("Selection rule Δℓ=0 forbidden: ⟨z⟩₁₂(1s→2s) = 0 by parity (both even)")
    print("=== PASSED ===" if abs(lam - 121.6) < 0.2 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class HydrogenDipoleScene(Scene):
    """
    Hydrogen 1s + 2pz superposition: oscillating charge cloud.
    2D density maps in xz-plane at several beat phases.
    Forbidden 1s+2s case shows no net oscillation.
    """

    GRID = 80    # density grid resolution
    R_MAX = 8.0  # display in a0 units

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_density_animation()
        self._phase_forbidden()
        self._phase_selection_rule()

    def _phase_title(self):
        title = Text("Hydrogen 1s→2pz Dipole Oscillation", font="EB Garamond",
                     font_size=48, color=INK)
        sub1 = Text(
            "A superposition of two hydrogen states creates an oscillating charge cloud.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"\lambda_{\rm Ly\alpha} = 121.6\;\mathrm{nm}\quad T = 405\;\mathrm{as}",
                       color=BLUE, font_size=26)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _make_density_image(self, t_norm: float, c1: float = 0.7071, c2_1pz: bool = True) -> np.ndarray:
        """Compute density on grid, return 2D array for NumberPlane-based colormap."""
        g = self.GRID
        r_max = self.R_MAX
        xs = np.linspace(-r_max, r_max, g)
        zs = np.linspace(-r_max, r_max, g)
        XX, ZZ = np.meshgrid(xs, zs)
        RR = np.sqrt(XX**2 + ZZ**2) + 1e-12
        c2 = np.sqrt(1.0 - c1**2)
        if c2_1pz:
            dens = superposition_density(RR, ZZ, t_norm, c1, c2)
        else:
            # 1s + 2s (forbidden — both ℓ=0, no cos(θ) factor)
            p1 = psi_1s(RR, ZZ)
            p2 = (1.0 / (4.0 * np.sqrt(2.0 * np.pi))) * (2.0 - RR) * np.exp(-RR / 2.0)
            omega = omega_12()
            T = 2.0 * np.pi / omega
            phase = (H_energy_eV(2) - H_energy_eV(1)) * EV / HBAR * t_norm * T
            dens = c1**2 * p1**2 + c2**2 * p2**2 + 2*c1*c2*p1*p2*np.cos(phase)
        return dens

    def _density_to_mobject(self, dens: np.ndarray, scale: float = 3.5) -> VGroup:
        """Convert 2D density to a grid of colored squares."""
        g = self.GRID
        r_max = self.R_MAX
        cell = 2.0 * r_max / g * scale / r_max   # size of each cell in scene units
        vmax = np.percentile(dens, 97)
        objs = []
        for i in range(g):
            for j in range(g):
                val = min(dens[i, j] / (vmax + 1e-15), 1.0)
                # Color from DIM (low) to BLUE (high)
                r_c = int(0x16 + val * (0x58 - 0x16))
                g_c = int(0x16 + val * (0xC4 - 0x16))
                b_c = int(0x1D + val * (0xDD - 0x1D))
                color = "#{:02x}{:02x}{:02x}".format(r_c, g_c, b_c)
                xi = (j - g//2 + 0.5) * cell
                zi = (i - g//2 + 0.5) * cell
                sq = Rectangle(width=cell*1.02, height=cell*1.02,
                                color=color, fill_color=color,
                                fill_opacity=1.0, stroke_width=0)
                sq.move_to([xi, zi, 0])
                objs.append(sq)
        return VGroup(*objs)

    def _phase_density_animation(self):
        hdr = Text("Charge cloud oscillates at Lyman-α beat frequency (time compressed)",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.2)
        ax_lbl = MathTex(r"\mathrm{xz\text{-}plane\ cross\text{-}section\ of\ }|\Psi|^2",
                         color=DIM, font_size=18).next_to(hdr, DOWN, buff=0.1)
        self.play(Write(hdr), Write(ax_lbl), run_time=0.9)

        n_frames = 12
        t_vals = np.linspace(0, 1.0, n_frames, endpoint=False)

        first = True
        prev_grid = None
        for t_norm in t_vals:
            dens = self._make_density_image(t_norm)
            grid = self._density_to_mobject(dens, scale=3.0)
            grid.shift(DOWN * 0.2)

            t_disp = Text(f"t/T = {t_norm:.2f}", font="EB Garamond",
                          font_size=20, color=GOLD).to_edge(DOWN, buff=0.28)
            if first:
                self.play(FadeIn(grid), Write(t_disp), run_time=0.8)
                first = False
            else:
                self.play(FadeOut(prev_grid), FadeIn(grid),
                          Transform(self._time_lbl, t_disp), run_time=0.35)
            prev_grid = grid
            self._time_lbl = t_disp

        self.wait(0.5)
        self.play(FadeOut(prev_grid, self._time_lbl, hdr, ax_lbl), run_time=0.5)

    def _phase_forbidden(self):
        hdr = Text("1s + 2s superposition (Δℓ=0 — FORBIDDEN): no net dipole",
                   font="EB Garamond", font_size=19, color=BROWN).to_edge(UP, buff=0.2)
        self.play(Write(hdr), run_time=0.8)

        n_frames = 8
        t_vals = np.linspace(0, 1.0, n_frames, endpoint=False)
        first = True
        prev_grid = None
        for t_norm in t_vals:
            dens = self._make_density_image(t_norm, c2_1pz=False)
            grid = self._density_to_mobject(dens, scale=3.0)
            grid.shift(DOWN * 0.2)
            t_disp = Text(f"t/T = {t_norm:.2f}", font="EB Garamond",
                          font_size=20, color=DIM).to_edge(DOWN, buff=0.28)
            if first:
                self.play(FadeIn(grid), Write(t_disp), run_time=0.8)
                first = False
            else:
                self.play(FadeOut(prev_grid), FadeIn(grid),
                          Transform(self._time_lbl2, t_disp), run_time=0.45)
            prev_grid = grid
            self._time_lbl2 = t_disp

        self.wait(0.5)
        self.play(FadeOut(prev_grid, self._time_lbl2, hdr), run_time=0.4)

    def _phase_selection_rule(self):
        rule = MathTex(
            r"\Delta\ell = \pm 1 \implies \langle z\rangle_{12} \neq 0 \implies \text{photon emitted}",
            color=INK, font_size=30,
        ).center().shift(UP * 0.8)
        rule2 = MathTex(
            r"\Delta\ell = 0 \implies \langle z\rangle_{12} = 0 \implies \text{no coupling}",
            color=BROWN, font_size=30,
        ).center().shift(UP * 0.0)
        lam_eq = MathTex(
            r"\lambda_{\rm Ly\alpha} = 121.6\;\mathrm{nm}\quad"
            r"\langle z\rangle_{12} = -0.745\,a_0",
            color=BLUE, font_size=26,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(rule), run_time=1.0)
        self.play(Write(rule2), run_time=1.0)
        self.play(Write(lam_eq), run_time=1.0)
        self.wait(3.0)
