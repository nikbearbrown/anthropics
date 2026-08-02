#!/usr/bin/env python3
"""
em_gauss_three_symmetries.py — Gauss's Law: Three Field Geometries
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    Sphere:   E = kQ/r²,     Q=10 nC
    Cylinder: E = λ/(2πε₀r), λ=100 nC/m
    Plane:    E = σ/(2ε₀),   σ=10 μC/m²

Run standalone to verify:
    python3 em_gauss_three_symmetries.py
"""
import sys
import numpy as np

K_COULOMB = 8.99e9    # N m²/C²
EPS0 = 8.854e-12      # F/m
Q_SPHERE = 10e-9      # C
LAMBDA = 100e-9       # C/m
SIGMA = 10e-6         # C/m²


def E_sphere(r): return K_COULOMB * Q_SPHERE / r**2
def E_cylinder(r): return LAMBDA / (2 * np.pi * EPS0 * r)
def E_plane(): return SIGMA / (2 * EPS0)


def verify():
    print("=== Gauss Three Symmetries verification ===")
    r1, r2 = 0.10, 0.20
    print(f"Sphere:   E({r1})={E_sphere(r1):.1f} N/C,  E({r2})={E_sphere(r2):.1f} N/C")
    print(f"  ratio = {E_sphere(r2)/E_sphere(r1):.4f}  (P1: should be 0.250)")
    print(f"Cylinder: E({r1})={E_cylinder(r1):.1f} N/C,  E({r2})={E_cylinder(r2):.1f} N/C")
    print(f"  ratio = {E_cylinder(r2)/E_cylinder(r1):.4f}  (P1: should be 0.500)")
    print(f"Plane:    E = {E_plane():.0f} N/C everywhere  ratio = 1.000")
    # Log-log slopes
    r_arr = np.array([0.10, 1.00, 10.0])
    print(f"\nLog-log slopes:")
    print(f"  Sphere:   ln(E(1)/E(10)) / ln(10/1) = {np.log(E_sphere(1)/E_sphere(10))/np.log(10):.3f}")
    print(f"  Cylinder: {np.log(E_cylinder(1)/E_cylinder(10))/np.log(10):.3f}")
    print("  Plane:    0.000")
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

RED_COLOR = "#E05252"


class EmGaussThreeSymmetriesScene(Scene):
    """
    Three Gaussian geometries side by side, then a log-log plot showing
    slopes −2 (sphere), −1 (cylinder), 0 (plane).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_gauss_law()
        self._phase_three_geometries()
        self._phase_loglog()
        self._phase_ratios()

    def _phase_title(self):
        title = Text("Gauss's Law — Three Symmetries", font="EB Garamond",
                     font_size=56, color=INK)
        eq = MathTex(r"\oint \vec{E}\cdot d\vec{A} = Q_{\rm enc}/\varepsilon_0",
                     color=BLUE, font_size=36)
        hook = Text("One equation — three completely different field laws",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, eq, hook).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(eq), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, eq, hook), run_time=0.5)

    def _phase_gauss_law(self):
        rows = VGroup(
            MathTex(r"\text{Sphere:}\quad E(4\pi r^2)=Q/\varepsilon_0 \;\Rightarrow\; E=\frac{kQ}{r^2}",
                    color=BLUE, font_size=32),
            MathTex(r"\text{Cylinder:}\quad E(2\pi r L)=\lambda L/\varepsilon_0 \;\Rightarrow\; E=\frac{\lambda}{2\pi\varepsilon_0 r}",
                    color=BROWN, font_size=32),
            MathTex(r"\text{Plane:}\quad E(2A)=\sigma A/\varepsilon_0 \;\Rightarrow\; E=\frac{\sigma}{2\varepsilon_0}",
                    color=GOLD, font_size=32),
        ).arrange(DOWN, buff=0.55).center()
        for row in rows:
            self.play(Write(row), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(rows), run_time=0.5)

    def _phase_three_geometries(self):
        # Three panels showing field arrow density at r1 and r2
        r1, r2 = 0.10, 0.20
        defs = [
            ("Sphere\n1/r²", E_sphere(r1), E_sphere(r2), BLUE),
            ("Cylinder\n1/r", E_cylinder(r1), E_cylinder(r2), BROWN),
            ("Plane\nconstant", E_plane(), E_plane(), GOLD),
        ]

        panels = VGroup()
        for i, (name, e1, e2, color) in enumerate(defs):
            x_pos = (i - 1) * 4.5
            lbl = Text(name, font="EB Garamond", font_size=22, color=color).move_to(
                [x_pos, 2.8, 0])
            # Arrow at r1
            arrow1 = Arrow(start=[x_pos - 0.5, 0.4, 0],
                           end=[x_pos - 0.5, 0.4 + min(e1 / 6000, 1.8), 0],
                           color=color, stroke_width=3, buff=0)
            e1_lbl = MathTex(f"{e1:.0f}", color=color, font_size=18
                             ).next_to(arrow1, RIGHT, buff=0.08)
            r1_lbl = Text("r = 0.10 m", font="EB Garamond", font_size=16, color=DIM
                          ).next_to(arrow1, DOWN, buff=0.08)
            # Arrow at r2
            arrow2 = Arrow(start=[x_pos + 0.5, -0.4, 0],
                           end=[x_pos + 0.5, -0.4 + min(e2 / 6000, 1.8), 0],
                           color=color, stroke_width=3, buff=0)
            e2_lbl = MathTex(f"{e2:.0f}", color=color, font_size=18
                             ).next_to(arrow2, RIGHT, buff=0.08)
            r2_lbl = Text("r = 0.20 m", font="EB Garamond", font_size=16, color=DIM
                          ).next_to(arrow2, DOWN, buff=0.08)
            panels.add(lbl, arrow1, e1_lbl, r1_lbl, arrow2, e2_lbl, r2_lbl)

        self.play(FadeIn(panels), run_time=2.0)
        self.wait(3.0)
        self.play(FadeOut(panels), run_time=0.5)

    def _phase_loglog(self):
        title = Text("Log-log: slopes encode the geometry", font="EB Garamond",
                     font_size=30, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)

        ax = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[0, 8, 2],
            x_length=9,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"\log_{10}(r/\mathrm{m})", color=INK, font_size=20
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        ly = MathTex(r"\log_{10}(E/\mathrm{N\,C}^{-1})", color=INK, font_size=20
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.05)

        log_r = np.linspace(-1.4, 1.4, 300)
        r_arr = 10**log_r

        log_Es = np.log10([E_sphere(r) for r in r_arr])
        log_Ec = np.log10([E_cylinder(r) for r in r_arr])
        log_Ep = np.log10([E_plane()] * len(r_arr))

        def make_curve(log_x, log_y, color):
            valid = np.isfinite(log_y) & (log_y >= 0) & (log_y <= 8)
            pts = [(x, y) for x, y, v in zip(log_x, log_y, valid) if v]
            if not pts:
                return VMobject()
            xs, ys = zip(*pts)
            return ax.plot_line_graph(
                x_values=list(xs), y_values=list(ys),
                line_color=color, stroke_width=3, add_vertex_dots=False,
            )

        c_sphere = make_curve(log_r, log_Es, BLUE)
        c_cyl = make_curve(log_r, log_Ec, BROWN)
        c_plane = make_curve(log_r, log_Ep, GOLD)

        lbl_s = MathTex(r"\text{sphere: slope }=-2", color=BLUE, font_size=22
                        ).to_corner(UR, buff=0.4).shift(DOWN * 0.1)
        lbl_c = MathTex(r"\text{cylinder: slope }=-1", color=BROWN, font_size=22
                        ).next_to(lbl_s, DOWN, buff=0.2)
        lbl_p = MathTex(r"\text{plane: slope }=0", color=GOLD, font_size=22
                        ).next_to(lbl_c, DOWN, buff=0.2)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.2)
        self.play(Create(c_sphere), Write(lbl_s), run_time=1.5)
        self.play(Create(c_cyl), Write(lbl_c), run_time=1.5)
        self.play(Create(c_plane), Write(lbl_p), run_time=1.5)
        self.wait(3.5)
        self.play(FadeOut(title, ax, lx, ly, c_sphere, c_cyl, c_plane,
                          lbl_s, lbl_c, lbl_p), run_time=0.5)

    def _phase_ratios(self):
        # Final verification table
        r1, r2 = 0.10, 0.20
        rows = VGroup(
            MathTex(
                r"\text{Sphere: } E(0.20)/E(0.10) = "
                + f"{E_sphere(r2)/E_sphere(r1):.3f}",
                color=BLUE, font_size=32),
            MathTex(
                r"\text{Cylinder: } E(0.20)/E(0.10) = "
                + f"{E_cylinder(r2)/E_cylinder(r1):.3f}",
                color=BROWN, font_size=32),
            MathTex(
                r"\text{Plane: } E(0.20)/E(0.10) = 1.000",
                color=GOLD, font_size=32),
        ).arrange(DOWN, buff=0.5).center()
        note = Text("The geometry of the Gaussian surface encodes the falloff",
                    font="EB Garamond", font_size=22, color=DIM).to_edge(DOWN, buff=0.3)
        self.play(Write(rows), run_time=2.0)
        self.play(Write(note), run_time=0.9)
        self.wait(3.0)
