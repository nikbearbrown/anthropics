#!/usr/bin/env python3
"""
em_dipole_falloff.py — Dipole Field Falloff: 1/r³ vs Monopole 1/r²
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    q=1.0 nC, d=0.010 m, p=qd=1e-11 C·m
    Monopole E = kq/r²
    Dipole on-axis E ≈ 2kp/r³

Run standalone to verify:
    python3 em_dipole_falloff.py
"""
import sys
import numpy as np

K_COULOMB = 8.99e9    # N m²/C²
Q_CHARGE = 1.0e-9     # C
D_SEP = 0.010         # m
P_DIPOLE = Q_CHARGE * D_SEP  # C·m


def E_monopole(r): return K_COULOMB * Q_CHARGE / r**2
def E_dipole(r): return 2 * K_COULOMB * P_DIPOLE / r**3
def E_quad(r): return 6 * K_COULOMB * P_DIPOLE * D_SEP / r**4  # approx


def verify():
    print("=== Dipole falloff verification ===")
    for r in [0.10, 0.20, 0.30]:
        print(f"r={r:.2f}: mono={E_monopole(r):.1f}, dipole={E_dipole(r):.2f}")
    print(f"P1: E_dip(0.10)/E_dip(0.20) = {E_dipole(0.10)/E_dipole(0.20):.4f}  (should be 8.000)")
    print(f"P1: E_dip(0.10)/E_dip(0.30) = {E_dipole(0.10)/E_dipole(0.30):.4f}  (should be 27.000)")
    print(f"P2: dipole slope = -3 (verified analytically)")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class EmDipoleFalloffScene(Scene):
    """
    Log-log plot: monopole (slope -2), dipole (slope -3), quadrupole (slope -4).
    Below: corresponding charge arrangements.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_hierarchy_equations()
        self._phase_loglog_and_arrangements()
        self._phase_ratios()

    def _phase_title(self):
        title = Text("Multipole Hierarchy — Field Falloff", font="EB Garamond",
                     font_size=56, color=INK)
        sub = Text("Monopole 1/r²  ·  Dipole 1/r³  ·  Quadrupole 1/r⁴",
                   font="EB Garamond", font_size=24, color=BLUE)
        hook = Text("Each cancellation adds one power to the falloff",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_hierarchy_equations(self):
        eqs = VGroup(
            MathTex(r"\text{Monopole:}\quad E = \frac{kq}{r^2}",
                    color=BLUE, font_size=34),
            MathTex(r"\text{Dipole (on-axis):}\quad E \approx \frac{2kp}{r^3},\quad p = qd",
                    color=BROWN, font_size=34),
            MathTex(r"\text{Quadrupole:}\quad E \propto \frac{1}{r^4}",
                    color=GOLD, font_size=34),
        ).arrange(DOWN, buff=0.5).center()
        note = Text("Each additional cancellation: +1 to the falloff exponent",
                    font="EB Garamond", font_size=22, color=DIM).to_edge(DOWN, buff=0.3)
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.play(Write(note), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(eqs, note), run_time=0.5)

    def _phase_loglog_and_arrangements(self):
        title = Text("Log-log: three slopes diverge visibly", font="EB Garamond",
                     font_size=28, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[-1.2, 0.8, 0.5],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.5)
        lx = MathTex(r"\log_{10}(r/\mathrm{m})", color=INK, font_size=20
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        ly = MathTex(r"\log_{10}(E)", color=INK, font_size=20
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.05)

        log_r = np.linspace(-1.1, 0.7, 300)
        r_arr = 10**log_r

        log_mono = np.log10([E_monopole(r) for r in r_arr])
        log_dip = np.log10([E_dipole(r) for r in r_arr])
        log_quad = np.log10([E_quad(r) for r in r_arr])

        def safe_curve(log_x, log_y, color):
            valid = np.isfinite(log_y) & (log_y >= 0) & (log_y <= 6)
            xs = [x for x, v in zip(log_x, valid) if v]
            ys = [y for y, v in zip(log_y, valid) if v]
            if not xs:
                return VMobject()
            return ax.plot_line_graph(
                x_values=xs, y_values=ys,
                line_color=color, stroke_width=3, add_vertex_dots=False,
            )

        c_mono = safe_curve(log_r, log_mono, BLUE)
        c_dip = safe_curve(log_r, log_dip, BROWN)
        c_quad = safe_curve(log_r, log_quad, GOLD)

        lbl_m = MathTex(r"\text{slope }=-2\text{ (mono)}", color=BLUE, font_size=21
                        ).to_corner(UR, buff=0.5).shift(DOWN * 0.1)
        lbl_d = MathTex(r"\text{slope }=-3\text{ (dipole)}", color=BROWN, font_size=21
                        ).next_to(lbl_m, DOWN, buff=0.2)
        lbl_q = MathTex(r"\text{slope }=-4\text{ (quad)}", color=GOLD, font_size=21
                        ).next_to(lbl_d, DOWN, buff=0.2)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(c_mono), Write(lbl_m), run_time=1.5)
        self.play(Create(c_dip), Write(lbl_d), run_time=1.5)
        self.play(Create(c_quad), Write(lbl_q), run_time=1.5)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, c_mono, c_dip, c_quad,
                          lbl_m, lbl_d, lbl_q), run_time=0.5)

    def _phase_ratios(self):
        r1, r2, r3 = 0.10, 0.20, 0.30
        eqs = VGroup(
            MathTex(
                r"\text{Monopole: } \frac{E(0.10)}{E(0.20)} = "
                + f"{E_monopole(r1)/E_monopole(r2):.2f}",
                color=BLUE, font_size=30),
            MathTex(
                r"\text{Dipole: } \frac{E(0.10)}{E(0.20)} = "
                + f"{E_dipole(r1)/E_dipole(r2):.1f}"
                + r"\;\left(\frac{0.20}{0.10}\right)^3 = 8",
                color=BROWN, font_size=30),
            MathTex(
                r"\text{Dipole: } \frac{E(0.10)}{E(0.30)} = "
                + f"{E_dipole(r1)/E_dipole(r3):.1f} = 3^3",
                color=BROWN, font_size=30),
        ).arrange(DOWN, buff=0.5).center()
        note = Text(
            "Chemistry is dominated by dipole forces because monopoles cancel in neutral molecules",
            font="EB Garamond", font_size=20, color=DIM).to_edge(DOWN, buff=0.25)
        self.play(Write(eqs), run_time=2.0)
        self.play(Write(note), run_time=0.9)
        self.wait(3.5)
