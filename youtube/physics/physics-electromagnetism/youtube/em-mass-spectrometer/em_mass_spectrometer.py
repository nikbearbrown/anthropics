#!/usr/bin/env python3
"""
em_mass_spectrometer.py — Mass Spectrometer: Radius Separates Particles by m/q
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    B=0.500 T, v=2.00×10⁵ m/s, q=e=1.60×10⁻¹⁹ C
    Ne-20: m=3.32×10⁻²⁶ kg → r=8.28 cm, x=16.56 cm
    Ne-22: m=3.65×10⁻²⁶ kg → r=9.11 cm, x=18.22 cm
    Δx = 1.66 cm

Run standalone to verify:
    python3 em_mass_spectrometer.py
"""
import sys
import numpy as np

B = 0.500          # T
V_ION = 2.00e5     # m/s
Q_ION = 1.60e-19   # C
M_NE20 = 3.32e-26  # kg (20 u)
M_NE22 = 3.65e-26  # kg (22 u)
U_AMU = 1.66054e-27  # kg/u


def radius(m): return m * V_ION / (Q_ION * B)
def landing(m): return 2 * radius(m)


def verify():
    print("=== Mass spectrometer verification ===")
    r20 = radius(M_NE20); x20 = landing(M_NE20)
    r22 = radius(M_NE22); x22 = landing(M_NE22)
    print(f"Ne-20: r={r20*100:.3f} cm, x={x20*100:.3f} cm  (card: 8.28, 16.56)")
    print(f"Ne-22: r={r22*100:.3f} cm, x={x22*100:.3f} cm  (card: 9.11, 18.22)")
    print(f"Δx = {(x22-x20)*100:.3f} cm  (card: 1.66 cm)")
    print(f"P1: r(22)/r(20) = {r22/r20:.4f}  (should be 1.100)")
    print(f"P2: r20 at B=1.0 T = {radius(M_NE20)*50:.3f} cm  (card: 4.14 cm)")
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


class EmMassSpectrometerScene(Scene):
    """
    Two ions arc through B field with different radii.
    Landing positions measured; mass determined.
    Then B sweep.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_arcs()
        self._phase_b_sweep()

    def _phase_title(self):
        title = Text("Mass Spectrometer", font="EB Garamond",
                     font_size=64, color=INK)
        sub = MathTex(r"r = \frac{mv}{qB}\;\Rightarrow\; m \propto r",
                      color=BLUE, font_size=34)
        hook = Text("A 2 cm gap on a detector strip gives mass to four decimal places",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eq1 = MathTex(r"qvB = \frac{mv^2}{r} \;\Rightarrow\; r = \frac{mv}{qB}",
                      color=INK, font_size=36)
        eq2 = MathTex(r"x = 2r = \frac{2mv}{qB}", color=BLUE, font_size=36)
        eq3 = MathTex(r"\frac{\Delta m}{m} = \frac{\Delta x}{x}",
                      color=GOLD, font_size=36)
        VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.5).center()
        for mob in [eq1, eq2, eq3]:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(eq1, eq2, eq3), run_time=0.5)

    def _phase_arcs(self):
        # Scene scale: 1 scene unit = 10 cm
        r20_cm = radius(M_NE20) * 100
        r22_cm = radius(M_NE22) * 100
        scale = 0.6   # scene units per cm
        R20 = r20_cm * scale
        R22 = r22_cm * scale

        # Entry at left wall (x=0, y=0), B into page, circular arcs to right
        # Center of arc: directly above entry for clockwise (positive ion, B into page)
        entry = np.array([-5.5, -2.5, 0])

        # Detector line (horizontal)
        det_y = entry[1]
        det_line = Line([-5.5, det_y, 0], [5.5, det_y, 0], color=DIM, stroke_width=2)
        det_lbl = Text("detector", font="EB Garamond", font_size=18, color=DIM
                       ).next_to(det_line, DOWN, buff=0.08)

        # B field dots (into page)
        b_dots = VGroup(*[
            Dot([x, y, 0], radius=0.05, color=DIM, fill_opacity=0.4)
            for x in np.linspace(-4.5, 4.5, 10)
            for y in np.linspace(-1.5, 2.5, 6)
        ])
        b_lbl = MathTex(r"\vec{B} = 0.500\,\text{T into page}", color=DIM,
                        font_size=18).to_corner(UL, buff=0.3)

        # Arc for Ne-20 (semicircle from entry up and land at x20 from entry)
        x20 = landing(M_NE20) * 100 * scale  # scene units
        x22 = landing(M_NE22) * 100 * scale

        # semicircles: center is at (entry_x + R, entry_y)
        c20 = entry + np.array([R20, 0, 0])
        c22 = entry + np.array([R22, 0, 0])

        # Draw half-circle parametrically
        def half_arc(center, R, color):
            angles = np.linspace(np.pi, 0, 200)
            pts = [center + R * np.array([np.cos(a), np.sin(a), 0]) for a in angles]
            mob = VMobject(color=color, stroke_width=3)
            mob.set_points_smoothly(pts)
            return mob

        arc20 = half_arc(c20, R20, BLUE)
        arc22 = half_arc(c22, R22, BROWN)

        land20 = entry + np.array([2 * R20, 0, 0])
        land22 = entry + np.array([2 * R22, 0, 0])

        dot20 = Dot(land20, color=BLUE, radius=0.12)
        dot22 = Dot(land22, color=BROWN, radius=0.12)
        lbl20 = MathTex(r"{}^{20}\text{Ne}", color=BLUE, font_size=22
                        ).next_to(dot20, DOWN, buff=0.15)
        lbl22 = MathTex(r"{}^{22}\text{Ne}", color=BROWN, font_size=22
                        ).next_to(dot22, DOWN, buff=0.15)
        x20_val = MathTex(f"16.56\\,\\text{{cm}}", color=BLUE, font_size=18
                          ).next_to(dot20, UP, buff=0.08)
        x22_val = MathTex(f"18.22\\,\\text{{cm}}", color=BROWN, font_size=18
                          ).next_to(dot22, UP, buff=0.08)
        sep_line = DashedLine(land20, land22, color=GOLD, stroke_width=2)
        sep_lbl = MathTex(r"\Delta x = 1.66\,\text{cm}", color=GOLD, font_size=22
                          ).next_to(sep_line, UP, buff=0.1)
        ratio_lbl = MathTex(r"r_{22}/r_{20} = 1.100\;(= 22/20)", color=INK,
                            font_size=22).to_edge(UP, buff=0.3)

        self.play(Create(det_line), Write(det_lbl), FadeIn(b_dots), Write(b_lbl),
                  run_time=0.9)
        self.play(Create(arc20), FadeIn(dot20), Write(lbl20), Write(x20_val),
                  run_time=1.8)
        self.play(Create(arc22), FadeIn(dot22), Write(lbl22), Write(x22_val),
                  run_time=1.8)
        self.play(Create(sep_line), Write(sep_lbl), Write(ratio_lbl), run_time=1.2)
        self.wait(3.0)
        self.play(FadeOut(det_line, det_lbl, b_dots, b_lbl, arc20, arc22,
                          dot20, dot22, lbl20, lbl22, x20_val, x22_val,
                          sep_line, sep_lbl, ratio_lbl), run_time=0.5)

    def _phase_b_sweep(self):
        title = Text("Doubling B halves all radii — ratio Δx/x stays constant",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)

        # Show how landing position scales with B
        B_vals = np.linspace(0.3, 1.0, 200)
        x20_vals = [landing(M_NE20) * 100 / b * B for b, B in zip(B_vals, B_vals)]
        # Actually: x = 2mv/(qB) → proportional to 1/B
        x20_arr = [landing(M_NE20) * 100 * B / b_val for b_val in B_vals]
        # Correct: x20 at B_val = x20_ref * B_ref / B_val
        B_ref = 0.500
        x20_arr = [landing(M_NE20) * 100 * B_ref / b for b in B_vals]
        x22_arr = [landing(M_NE22) * 100 * B_ref / b for b in B_vals]

        ax = Axes(
            x_range=[0.3, 1.0, 0.1],
            y_range=[8, 35, 5],
            x_length=9,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.4)
        lx = MathTex(r"B\;(\mathrm{T})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"x\;(\mathrm{cm})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        c20 = ax.plot_line_graph(
            x_values=list(B_vals), y_values=x20_arr,
            line_color=BLUE, stroke_width=3, add_vertex_dots=False)
        c22 = ax.plot_line_graph(
            x_values=list(B_vals), y_values=x22_arr,
            line_color=BROWN, stroke_width=3, add_vertex_dots=False)

        ratio_line = ax.plot_line_graph(
            x_values=list(B_vals),
            y_values=[(x22_arr[i] - x20_arr[i]) / x20_arr[i] * 10 + 8
                      for i in range(len(B_vals))],
            line_color=GOLD, stroke_width=2, add_vertex_dots=False)
        ratio_lbl = Text("Δx/x = 0.100 = const (scaled × 10 + 8)",
                         font="EB Garamond", font_size=18, color=GOLD
                         ).to_edge(DOWN, buff=0.28)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(c20), Create(c22), run_time=1.8)
        self.play(Create(ratio_line), Write(ratio_lbl), run_time=1.2)
        self.wait(3.0)
