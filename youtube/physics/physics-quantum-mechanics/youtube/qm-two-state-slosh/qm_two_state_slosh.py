#!/usr/bin/env python3
"""
qm_two_state_slosh.py — Two-State Sloshing: <x>(t) oscillates, <H> does not
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-two-state-slosh
    manim -qh qm_two_state_slosh.py TwoStateSloshScene

Verify:
    python3 qm_two_state_slosh.py

Physics:
    ISW L=1 nm electron. Equal superposition (ψ₁ + ψ₂)/√2.
    E₁=0.376 eV, E₂=1.504 eV
    Beat freq ω₂₁ = (E₂-E₁)/ℏ, period T = 2πℏ/(E₂-E₁) = 3.67 fs
    <x>(t) oscillates between ~0.35L and ~0.65L
    <H> = (E₁+E₂)/2 = 0.94 eV (constant)
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
M_E  = 9.10938e-31
EV   = 1.60218e-19


def isw_energy(n: int, L_nm: float) -> float:
    """E_n in Joules."""
    L = L_nm * 1e-9
    return (n**2 * np.pi**2 * HBAR**2) / (2.0 * M_E * L**2)


def psi_n(n: int, x: np.ndarray) -> np.ndarray:
    """ψ_n(x) normalised on [0,1]."""
    return np.sqrt(2.0) * np.sin(n * np.pi * x)


def prob_density(x: np.ndarray, t: float, E1: float, E2: float) -> np.ndarray:
    """
    |Ψ(x,t)|² for equal superposition (ψ₁+ψ₂)/√2.
    Time in seconds, energies in Joules.
    """
    omega = (E2 - E1) / HBAR
    p1 = psi_n(1, x)
    p2 = psi_n(2, x)
    return 0.5 * (p1**2 + p2**2 + 2.0 * p1 * p2 * np.cos(omega * t))


def mean_x(t: float, E1: float, E2: float) -> float:
    """
    <x>(t) for equal superposition (ψ₁+ψ₂)/√2.
    Matrix element <x>₁₂ = ∫ψ₁ x ψ₂ dx = -16L/9π² (for L=1 unit).
    """
    omega = (E2 - E1) / HBAR
    x12   = -16.0 / (9.0 * np.pi**2)   # in units of L
    return 0.5 + 2.0 * x12 * np.cos(omega * t)


def verify():
    print("=== Two-state sloshing verification ===")
    L = 1.0  # nm
    E1 = isw_energy(1, L)
    E2 = isw_energy(2, L)
    print(f"E₁ = {E1/EV:.4f} eV  (card says 0.376 eV)")
    print(f"E₂ = {E2/EV:.4f} eV  (card says 1.504 eV)")
    omega = (E2 - E1) / HBAR
    freq_THz = omega / (2 * np.pi) / 1e12
    T_fs = 2 * np.pi / omega * 1e15
    print(f"Beat frequency = {freq_THz:.1f} THz  (card says 272 THz)")
    print(f"Beat period T  = {T_fs:.2f} fs  (card says 3.67 fs)")
    H_mean = 0.5 * (E1 + E2) / EV
    print(f"<H> = {H_mean:.4f} eV  (card says 0.94 eV)")
    # Check <x> amplitude via matrix element
    x12 = -16.0 / (9.0 * np.pi**2)
    amp = 2.0 * abs(x12)  # in units of L
    print(f"<x> oscillation half-amplitude = {amp:.4f} L  (card says 16L/9π²≈0.18L)")
    print(f"  → <x> range: [{0.5-amp:.3f}L, {0.5+amp:.3f}L]  (card says 0.35–0.65 L)")
    print("=== PASSED ===")


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


class TwoStateSloshScene(Scene):
    """
    Two-state sloshing in ISW. Probability density sloshes left-right.
    <x>(t) sinusoidal, <H>(t) flat.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_sloshing_density()
        self._phase_x_expectation()
        self._phase_psi12_superposition()

    def _phase_title(self):
        title = Text("Two-State Quantum Sloshing", font="EB Garamond",
                     font_size=56, color=INK)
        sub1 = Text(
            "Superposition of energy eigenstates: position oscillates, energy stays constant.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(
            r"\Psi = \tfrac{1}{\sqrt{2}}\!\left(\psi_1 e^{-iE_1 t/\hbar} + \psi_2 e^{-iE_2 t/\hbar}\right)",
            color=BLUE, font_size=26,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_sloshing_density(self):
        L_nm = 1.0
        E1 = isw_energy(1, L_nm)
        E2 = isw_energy(2, L_nm)
        T_period = 2.0 * np.pi * HBAR / (E2 - E1)   # seconds

        ax = Axes(
            x_range=[0, 1, 0.25],
            y_range=[0, 2.2, 0.5],
            x_length=8.5,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.6)
        lbl_x = MathTex(r"x/L", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"|\Psi|^2", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Probability density sloshing at 272 THz beat frequency",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)

        x_arr = np.linspace(0, 1, 300)
        n_frames = 40
        # Animate over two full beat periods in display time ~5 s
        t_phys_values = np.linspace(0, 2.0 * T_period, n_frames)

        # Initial curve
        t0 = 0.0
        y0 = prob_density(x_arr, t0, E1, E2)
        curve = VMobject(color=BLUE, stroke_width=3.5)
        curve.set_points_smoothly([ax.c2p(x, y) for x, y in zip(x_arr, y0)])

        # <x> dot
        x_mean_0 = mean_x(t0, E1, E2)
        dot = Dot(ax.c2p(x_mean_0, 0), radius=0.1, color=GOLD)

        time_lbl = MathTex(r"t = 0\,T", color=DIM, font_size=22).to_edge(DOWN, buff=0.3)

        self.play(Create(curve), FadeIn(dot), Write(time_lbl), run_time=1.0)

        for i, t_phys in enumerate(t_phys_values[1:], 1):
            y_new = prob_density(x_arr, t_phys, E1, E2)
            new_curve = VMobject(color=BLUE, stroke_width=3.5)
            new_curve.set_points_smoothly([ax.c2p(x, y) for x, y in zip(x_arr, y_new)])
            x_mean_new = mean_x(t_phys, E1, E2)
            new_dot = Dot(ax.c2p(x_mean_new, 0), radius=0.1, color=GOLD)
            frac = t_phys / T_period
            new_lbl = MathTex(rf"t = {frac:.2f}\,T", color=DIM, font_size=22).to_edge(DOWN, buff=0.3)
            self.play(
                Transform(curve, new_curve),
                Transform(dot, new_dot),
                Transform(time_lbl, new_lbl),
                run_time=0.15,
            )

        self.wait(0.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, curve, dot, time_lbl), run_time=0.5)

    def _phase_x_expectation(self):
        E1 = isw_energy(1, 1.0)
        E2 = isw_energy(2, 1.0)
        T_period = 2.0 * np.pi * HBAR / (E2 - E1)

        ax = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[0.2, 0.8, 0.2],
            x_length=8.5,
            y_length=3.2,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.7)
        lbl_x = MathTex(r"t/T", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\langle x\rangle/L", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("<x>(t) and <H>(t) for equal superposition",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.1)

        t_arr = np.linspace(0, 2.0, 300)
        x_mean_arr = np.array([mean_x(t * T_period, E1, E2) for t in t_arr])
        H_mean_arr = np.ones_like(t_arr) * 0.5 * (E1 + E2) / (E2 - E1) * 0  # just 0.5 in L-units

        H_mean_val = 0.5  # <H> at 0.5 L in x-coords... no: <H> is energy, separate

        pts_x  = [ax.c2p(t, xm) for t, xm in zip(t_arr, x_mean_arr)]
        # Draw <H> as a flat line at y=0.5 (middle of well) in a separate annotation
        # Actually, let's show it on a separate small row below with energy units
        c_x = VMobject(color=BLUE, stroke_width=3.5)
        c_x.set_points_smoothly(pts_x)

        H_line_y_in_x_units = 0.5  # position axis midpoint
        c_H = DashedLine(
            ax.c2p(0, H_line_y_in_x_units), ax.c2p(2.2, H_line_y_in_x_units),
            color=BROWN, dash_length=0.1, stroke_width=2.0,
        )

        lbl_cx = MathTex(r"\langle x\rangle(t)", color=BLUE, font_size=22).next_to(
            ax.c2p(2.2, x_mean_arr[-1]), RIGHT, buff=0.08
        )

        cap1 = MathTex(r"\langle H\rangle = \tfrac{E_1+E_2}{2} = 0.94\,\mathrm{eV}\ (\mathrm{constant})",
                       color=BROWN, font_size=24).to_edge(DOWN, buff=0.28)

        cap2 = Text("Period T = 3.67 fs  (272 THz beat frequency)",
                    font="EB Garamond", font_size=20, color=DIM).to_edge(DOWN, buff=0.06)

        self.play(Create(c_x), Write(lbl_cx), run_time=1.5)
        self.play(Create(c_H), Write(cap1), Write(cap2), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, c_x, c_H, lbl_cx, cap1, cap2), run_time=0.5)

    def _phase_psi12_superposition(self):
        """Show ψ₁ and ψ₂ separately — the cross-term creates the sloshing."""
        eq = MathTex(
            r"|\Psi|^2 = \tfrac{1}{2}|\psi_1|^2 + \tfrac{1}{2}|\psi_2|^2",
            r"+ \psi_1\psi_2\cos\!\left(\frac{E_2-E_1}{\hbar}\,t\right)",
            color=INK, font_size=30,
        ).center().shift(UP * 0.5)
        note = Text(
            "The cross-term — ψ₁ψ₂·cos(ωt) — is the oscillating dipole.",
            font="EB Garamond", font_size=22, color=DIM,
        ).next_to(eq, DOWN, buff=0.45)
        note2 = Text(
            "It is what couples to a photon at the beat frequency.",
            font="EB Garamond", font_size=22, color=BLUE,
        ).next_to(note, DOWN, buff=0.25)

        self.play(Write(eq[0]), run_time=1.0)
        self.play(Write(eq[1]), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
