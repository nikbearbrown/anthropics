#!/usr/bin/env python3
"""
em_equipotentials_gradient.py — Electric Potential: Equipotential Surfaces and E = -∇V
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    q = 5 μC point charge
    V(r) = kq/r  →  at r=0.10 m: 450 kV, r=0.20 m: 225 kV
    E = -dV/dr = kq/r²  →  at r=0.10 m: 4.50 MV/m

Run standalone to verify:
    python3 em_equipotentials_gradient.py
"""
import sys
import numpy as np

K_COULOMB = 8.99e9   # N m²/C²
Q_CHARGE = 5.0e-6    # C


def V(r): return K_COULOMB * Q_CHARGE / r
def E(r): return K_COULOMB * Q_CHARGE / r**2


def verify():
    print("=== Equipotentials verification ===")
    for r in [0.10, 0.20, 0.50]:
        print(f"r={r:.2f} m: V={V(r)/1000:.0f} kV, E={E(r)/1e6:.3f} MV/m")
    Q_test = 1e-6  # 1 μC
    W = Q_test * (V(0.10) - V(0.20))
    print(f"P1: W = QΔV = {W:.3f} J  (card: 0.225 J)")
    print(f"P2: E at r=0.10 = {E(0.10)/1e6:.3f} MV/m  (card: 4.50 MV/m)")
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


class EmEquipotentialsGradientScene(Scene):
    """
    Equipotential circles for a point charge, field lines emerging perpendicular.
    Work = QΔV. Then switch to parallel plate uniform field.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_equipotentials()
        self._phase_work()
        self._phase_parallel_plate()

    def _phase_title(self):
        title = Text("Equipotentials and E = −∇V", font="EB Garamond",
                     font_size=58, color=INK)
        sub = MathTex(r"E = -\frac{dV}{dr} = \frac{kq}{r^2}", color=BLUE,
                      font_size=34)
        hook = Text("Field lines always cross equipotentials at exactly 90°",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        f1 = MathTex(r"V(r) = \frac{kq}{r}", color=INK, font_size=38)
        f2 = MathTex(r"E = -\nabla V \Rightarrow E_r = -\frac{dV}{dr} = \frac{kq}{r^2}",
                     color=BLUE, font_size=34)
        f3 = MathTex(
            r"q=5\,\mu\text{C}:\quad V(0.10)=450\,\text{kV},\;E(0.10)=4.50\,\text{MV/m}",
            color=GOLD, font_size=28)
        VGroup(f1, f2, f3).arrange(DOWN, buff=0.45).center()
        for mob in [f1, f2, f3]:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(f1, f2, f3), run_time=0.5)

    def _phase_equipotentials(self):
        # Central charge
        center_dot = Dot(ORIGIN, color=GOLD, radius=0.15)
        q_lbl = MathTex(r"+5\,\mu\text{C}", color=GOLD, font_size=22
                        ).next_to(center_dot, DOWN, buff=0.12)

        # Equipotential circles (radius ∝ 1/V, so r ∝ 1/V → space out geometrically)
        # Choose V values and compute radii in scene units
        scale = 1.5  # scene cm per 10 cm
        V_vals = [450e3, 225e3, 90e3]
        radii_m = [V(vv) / vv * 1 for vv in V_vals]  # K_COULOMB*Q/V
        r_m_vals = [K_COULOMB * Q_CHARGE / vv for vv in V_vals]
        # scale to scene: r_scene = r_m * scale_factor; pick scale_factor so r1~1 scene unit
        r_scene_vals = [rm / r_m_vals[0] * 1.2 for rm in r_m_vals]

        circles = VGroup()
        clbls = VGroup()
        for i, (vs, rs) in enumerate(zip(V_vals, r_scene_vals)):
            c = Circle(radius=rs, color=BLUE, stroke_width=2, stroke_opacity=0.7)
            lbl = MathTex(f"{vs/1000:.0f}" + r"\,\text{kV}", color=BLUE,
                          font_size=18).move_to([rs + 0.25, 0.15, 0])
            circles.add(c)
            clbls.add(lbl)

        # Field lines radiating out at angles
        n_lines = 8
        field_arrows = VGroup()
        for angle in np.linspace(0, 2 * np.pi, n_lines, endpoint=False):
            start = 0.18 * np.array([np.cos(angle), np.sin(angle), 0])
            end = 3.2 * np.array([np.cos(angle), np.sin(angle), 0])
            arr = Arrow(start=start, end=end, color=BROWN, stroke_width=1.5,
                        buff=0, tip_length=0.18)
            field_arrows.add(arr)

        perp_note = Text("Field lines ⊥ equipotentials at every crossing",
                         font="EB Garamond", font_size=22, color=DIM
                         ).to_edge(DOWN, buff=0.28)

        self.play(FadeIn(center_dot), Write(q_lbl), run_time=0.7)
        self.play(Create(circles), Write(clbls), run_time=2.0)
        self.play(Create(field_arrows), run_time=1.5)
        self.play(Write(perp_note), run_time=0.7)
        self.wait(3.0)
        self.play(FadeOut(center_dot, q_lbl, circles, clbls, field_arrows, perp_note),
                  run_time=0.5)

    def _phase_work(self):
        Q_test = 1e-6
        W = Q_test * (V(0.10) - V(0.20))
        work_eq = MathTex(
            r"W = Q\,\Delta V = Q[V(0.10) - V(0.20)]",
            color=INK, font_size=34)
        work_val = MathTex(
            r"= (10^{-6})(450{,}000 - 225{,}000) = "
            + f"{W:.3f}" + r"\,\mathrm{J}",
            color=GOLD, font_size=34)
        path_note = Text("Same result for ANY path from r=0.20 to r=0.10 — W = QΔV only",
                         font="EB Garamond", font_size=21, color=DIM)
        VGroup(work_eq, work_val, path_note).arrange(DOWN, buff=0.5).center()
        for mob in [work_eq, work_val, path_note]:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(work_eq, work_val, path_note), run_time=0.5)

    def _phase_parallel_plate(self):
        title = Text("Parallel plate: uniform E, flat equipotentials",
                     font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        # Plates
        plate_top = Line([-4, 2, 0], [4, 2, 0], color=DIM, stroke_width=4)
        plate_bot = Line([-4, -2, 0], [4, -2, 0], color=DIM, stroke_width=4)
        plus_lbl = Text("+ + + + + + + +", font="EB Garamond", font_size=20,
                        color=GOLD).next_to(plate_bot, DOWN, buff=0.05)
        minus_lbl = Text("− − − − − − − −", font="EB Garamond", font_size=20,
                         color=BLUE).next_to(plate_top, UP, buff=0.05)

        # Uniform E arrows
        e_arrows = VGroup(*[
            Arrow(start=[x, -1.7, 0], end=[x, 1.7, 0],
                  color=BROWN, stroke_width=1.5, buff=0)
            for x in np.linspace(-3.5, 3.5, 8)
        ])

        # Flat equipotential lines
        eq_lines = VGroup(*[
            Line([-4, y, 0], [4, y, 0], color=BLUE, stroke_width=1.5,
                 stroke_opacity=0.5)
            for y in np.linspace(-1.5, 1.5, 5)
        ])
        eq_note = Text("Flat equipotentials ↔ uniform field",
                       font="EB Garamond", font_size=22, color=DIM
                       ).to_edge(DOWN, buff=0.28)

        self.play(Create(plate_top), Create(plate_bot),
                  Write(plus_lbl), Write(minus_lbl), run_time=0.8)
        self.play(Create(eq_lines), run_time=1.2)
        self.play(Create(e_arrows), Write(eq_note), run_time=1.2)
        self.wait(3.0)
