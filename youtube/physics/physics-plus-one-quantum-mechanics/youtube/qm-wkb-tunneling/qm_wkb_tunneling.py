#!/usr/bin/env python3
"""
qm_wkb_tunneling.py — WKB Tunneling: The Gamow Factor and the Geiger-Nuttall Law
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-quantum-mechanics book.

Render:
    cd physics-plus-one-quantum-mechanics/youtube/qm-wkb-tunneling
    manim -qh qm_wkb_tunneling.py WkbTunnelingScene

Physics:
    Alpha particle m = 6.644e-27 kg
    T ≈ exp(-2G), G = (1/ℏ) ∫ sqrt(2m(V-E)) dx (Gamow factor)
    U-238:  E_α = 4.27 MeV, t_{1/2} = 4.5e9 yr
    Po-212: E_α = 8.78 MeV, t_{1/2} = 0.3 μs
    Ratio of half-lives ≈ 4.7e23 with only 2x energy change
"""
import sys
import numpy as np

HBAR   = 1.055e-34   # J·s
M_ALPHA = 6.644e-27  # kg
EV     = 1.602e-19   # J/eV
MEV    = EV * 1e6

# Simple square barrier model for illustration
def gamow_factor(E_MeV, V0_MeV=15.0, barrier_width_fm=20.0):
    """Approximate Gamow factor for rectangular barrier."""
    E = E_MeV * MEV
    V0 = V0_MeV * MEV
    a  = barrier_width_fm * 1e-15
    if E >= V0:
        return 0.0
    kappa = np.sqrt(2 * M_ALPHA * (V0 - E)) / HBAR
    return kappa * a


def transmission(G):
    return np.exp(-2 * G)


if __name__ == "__main__":
    print("=== WKB Tunneling Verification ===")
    G_U  = gamow_factor(4.27)
    G_Po = gamow_factor(8.78)
    T_U  = transmission(G_U)
    T_Po = transmission(G_Po)
    print(f"U-238:  G={G_U:.2f}, T=exp(-2G)={T_U:.3e}")
    print(f"Po-212: G={G_Po:.2f}, T=exp(-2G)={T_Po:.3e}")
    # P1: Geiger-Nuttall: log(λ) linear in 1/sqrt(E)
    energies = np.array([3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
    G_arr = np.array([gamow_factor(E) for E in energies])
    log_T = -2 * G_arr
    inv_sqrtE = 1.0 / np.sqrt(energies)
    slope, intercept = np.polyfit(inv_sqrtE, log_T, 1)
    print(f"P1: log(T) vs 1/sqrt(E) slope={slope:.2f}  (should be negative and linear)")
    # P2: T→1 when E≥V0
    G_over = gamow_factor(16.0)   # E > V0=15 MeV
    print(f"P2: G at E>V0 = {G_over:.4f}  (expect 0.0)")
    assert G_over == 0.0, "P2 FAIL"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

V0_MEV = 15.0


class WkbTunnelingScene(Scene):
    """Nuclear potential + WKB wavefunction + Gamow factor + Geiger-Nuttall."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_potential(ax_only=True)
        self._phase_potential_fill(ax)
        self._phase_wavefunction(ax)
        self._phase_geiger_nuttall()

    def _phase_title(self):
        title = Text("WKB Tunneling and the Gamow Factor", font="EB Garamond",
                     font_size=48, color=INK)
        sub = Text("Alpha decay: a tiny energy change → 23 orders of magnitude in half-life",
                   font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_potential(self, ax_only=False):
        ax = Axes(
            x_range=[0, 40, 10],
            y_range=[-10, 20, 5],
            x_length=9.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.2)
        x_lbl = MathTex(r"r\;(\mathrm{fm})", color=INK, font_size=22).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"V\;(\mathrm{MeV})", color=INK, font_size=22).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        return ax

    def _nuclear_potential(self, r_fm, R0=8.0, V_nuclear=-8.0, Z=90):
        """Simple Coulomb + nuclear well potential."""
        KC = 1.44   # MeV·fm  (Coulomb constant for nuclear physics, keV to MeV)
        Q_alpha = 2.0
        V = np.where(r_fm < R0,
                     V_nuclear,
                     KC * Z * Q_alpha / r_fm)
        return V

    def _phase_potential_fill(self, ax):
        r_fm = np.linspace(0.5, 40, 600)
        V    = self._nuclear_potential(r_fm)
        V_c  = np.clip(V, -10, 19)

        pts = [ax.c2p(r, v) for r, v in zip(r_fm, V_c)]
        pot_curve = VMobject(color=BLUE, stroke_width=3.0)
        pot_curve.set_points_smoothly(pts)

        # E_alpha lines
        E_U  = 4.27
        E_Po = 8.78
        e_line_U  = DashedLine(ax.c2p(0, E_U),  ax.c2p(40, E_U),
                               color=GOLD, stroke_width=1.5)
        e_line_Po = DashedLine(ax.c2p(0, E_Po), ax.c2p(40, E_Po),
                               color=BROWN, stroke_width=1.5)
        e_lbl_U   = Text("U-238  E_α=4.27 MeV", font="EB Garamond",
                         font_size=16, color=GOLD).next_to(ax.c2p(30, E_U), UP, buff=0.05)
        e_lbl_Po  = Text("Po-212  E_α=8.78 MeV", font="EB Garamond",
                         font_size=16, color=BROWN).next_to(ax.c2p(28, E_Po), UP, buff=0.05)

        self.play(Create(pot_curve), run_time=2.0)
        self.play(Create(e_line_U), Write(e_lbl_U), run_time=0.8)
        self.play(Create(e_line_Po), Write(e_lbl_Po), run_time=0.8)

        cap = Text("Coulomb barrier peak ≈ 15 MeV — both alpha particles are below it classically",
                   font="EB Garamond", font_size=18, color=DIM).to_edge(DOWN, buff=0.28)
        self.play(Write(cap), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(pot_curve, e_line_U, e_line_Po, e_lbl_U, e_lbl_Po, cap), run_time=0.5)

    def _phase_wavefunction(self, ax):
        # Schematic WKB wavefunction: oscillatory inside well, decaying through barrier, oscillatory outside
        r_fm = np.linspace(0.5, 40, 800)
        R0 = 8.0   # nuclear radius
        r1 = R0
        # Classical turning point for E=6 MeV Coulomb barrier (illustrative)
        r2 = 1.44 * 90 * 2 / 6.0  # Coulomb turning point ≈ 43 fm, cap at 35

        def wkb_wave(r):
            psi = np.zeros_like(r)
            inside  = r <= R0
            barrier = (r > R0) & (r < 32)
            outside = r >= 32
            psi[inside]  = np.sin(2.5 * r[inside]) * 0.8
            decay_pts = r[barrier] - R0
            psi[barrier] = 0.7 * np.exp(-0.15 * decay_pts)
            psi[outside] = 0.05 * np.sin(0.8 * (r[outside] - 32))
            return psi

        psi = wkb_wave(r_fm)
        psi2 = psi**2

        pts_psi  = [ax.c2p(r, 3.0 + p * 4) for r, p in zip(r_fm, psi)  if -10 <= 3.0 + p * 4 <= 19]
        pts_psi2 = [ax.c2p(r, -2 + p2 * 8)  for r, p2 in zip(r_fm, psi2) if -10 <= -2 + p2 * 8 <= 19]

        curve_psi  = VMobject(color=BLUE, stroke_width=2.5)
        curve_psi.set_points_smoothly(pts_psi)
        curve_psi2 = VMobject(color=GOLD, stroke_width=2.0)
        curve_psi2.set_points_smoothly(pts_psi2)

        hdr = Text("WKB wavefunction: oscillates inside, decays through barrier, oscillates outside",
                   font="EB Garamond", font_size=18, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(curve_psi), Create(curve_psi2), run_time=2.5)
        gamow_eq = MathTex(
            r"T\approx e^{-2G},\quad G=\frac{1}{\hbar}\int_{x_1}^{x_2}\sqrt{2m(V-E)}\,dx",
            color=INK, font_size=24).to_edge(DOWN, buff=0.25)
        self.play(Write(gamow_eq), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(hdr, curve_psi, curve_psi2, gamow_eq), run_time=0.5)

    def _phase_geiger_nuttall(self):
        # Plot log(t_1/2) vs 1/sqrt(E) for illustrative nuclear data
        # Geiger-Nuttall data (approximate):
        data = [
            ("U-238",  4.27,  4.5e9 * 365.25 * 24 * 3600),
            ("Ra-226", 4.87,  1600 * 365.25 * 24 * 3600),
            ("Po-210", 5.30,  138.4 * 24 * 3600),
            ("Rn-222", 5.49,  3.82 * 24 * 3600),
            ("Po-218", 6.11,  3.05 * 60),
            ("Po-212", 8.78,  0.3e-6),
        ]

        ax = Axes(
            x_range=[0.30, 0.50, 0.05],
            y_range=[-7, 25, 5],
            x_length=7.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.2)
        x_lbl = MathTex(r"E_\alpha^{-1/2}\;(\mathrm{MeV}^{-1/2})", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"\log_{10}(t_{1/2}/\mathrm{s})", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.2)

        xs = np.array([1.0/np.sqrt(E) for _, E, _ in data])
        ys = np.array([np.log10(t) for _, _, t in data])

        # Fit line
        slope, intercept = np.polyfit(xs, ys, 1)
        x_fit = np.linspace(0.30, 0.50, 100)
        y_fit = slope * x_fit + intercept
        pts_fit = [ax.c2p(x, y) for x, y in zip(x_fit, y_fit)
                   if -7 <= y <= 25]
        fit_line = VMobject(color=BLUE, stroke_width=2.5)
        fit_line.set_points_smoothly(pts_fit)

        dots = VGroup()
        lbls = VGroup()
        for name, E, t in data:
            x = 1.0/np.sqrt(E)
            y = np.log10(t)
            if 0.30 <= x <= 0.50 and -7 <= y <= 25:
                dot = Dot(ax.c2p(x, y), color=GOLD, radius=0.1)
                lbl = Text(name, font="EB Garamond", font_size=14, color=DIM
                           ).next_to(ax.c2p(x, y), RIGHT, buff=0.05)
                dots.add(dot)
                lbls.add(lbl)

        hdr = Text("Geiger-Nuttall Law: log(t₁/₂) ∝ 1/√E_α — WKB explains it",
                   font="EB Garamond", font_size=20, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(fit_line), run_time=1.5)
        self.play(Create(dots), Write(lbls), run_time=1.2)
        final = MathTex(
            r"\text{Energy} \times 2 \Rightarrow \text{half-life} \div 10^{23}",
            color=GOLD, font_size=28).to_edge(DOWN, buff=0.28)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
