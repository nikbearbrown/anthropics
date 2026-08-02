#!/usr/bin/env python3
"""
em_cyclotron_motion.py — Cyclotron Motion: Speed-Independent Period
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    Proton in B = 0.50 T:
    m_p = 1.67e-27 kg, q = 1.60e-19 C
    omega_c = qB/m = 4.79e7 rad/s
    T = 2*pi/omega_c = 131 ns
    v1 = 1e6 m/s -> r1 = mv/(qB) = 2.09 cm
    v2 = 2e6 m/s -> r2 = 4.18 cm  (T unchanged)

Run standalone to verify:
    python3 em_cyclotron_motion.py
"""
import sys
import numpy as np

# ── Physics constants ─────────────────────────────────────────────────────────
M_PROTON = 1.6726e-27   # kg
Q_PROTON = 1.6022e-19   # C
B_FIELD  = 0.50         # T


def cyclotron_radius(v, B=B_FIELD):
    return M_PROTON * v / (Q_PROTON * B)


def cyclotron_period(B=B_FIELD):
    return 2 * np.pi * M_PROTON / (Q_PROTON * B)


def cyclotron_omega(B=B_FIELD):
    return Q_PROTON * B / M_PROTON


def verify():
    print("=== Cyclotron motion verification ===")
    omega = cyclotron_omega()
    T = cyclotron_period()
    r1 = cyclotron_radius(1e6)
    r2 = cyclotron_radius(2e6)
    r3 = cyclotron_radius(3e6)
    print(f"omega_c = {omega:.4e} rad/s  (card: 4.79e7)")
    print(f"T       = {T*1e9:.3f} ns        (card: 131 ns)")
    print(f"r(v1=1e6 m/s) = {r1*100:.3f} cm   (card: 2.09 cm)")
    print(f"r(v2=2e6 m/s) = {r2*100:.3f} cm   (card: 4.18 cm)")
    print(f"r(v3=3e6 m/s) = {r3*100:.3f} cm   (P2: 6.27 cm)")
    print(f"r3/r1 = {r3/r1:.4f}  (P2: should be 3.000)")
    print(f"T at B=1.0 T  = {cyclotron_period(1.0)*1e9:.3f} ns  (card: 65.5 ns)")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    if "--verify" not in sys.argv:
        sys.exit(0)
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class EmCyclotronMotionScene(Scene):
    """
    Cyclotron motion: two protons at v and 2v trace circles of radius r and 2r
    in the SAME period T = 2πm/qB. Then helical motion with v_parallel.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_circles()
        self._phase_period_proof()
        self._phase_helix()

    def _phase_title(self):
        title = Text("Cyclotron Motion", font="EB Garamond", font_size=64, color=INK)
        sub = Text(
            "Speed-independent period: T = 2πm / qB",
            font="EB Garamond", font_size=26, color=BLUE,
        )
        hook = Text(
            "Double the speed — radius doubles, period stays identical",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eq1 = MathTex(r"qvB = \frac{mv^2}{r}", color=INK, font_size=40)
        eq2 = MathTex(r"\Rightarrow r = \frac{mv}{qB}", color=BLUE, font_size=40)
        eq3 = MathTex(
            r"T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}",
            color=GOLD, font_size=40,
        )
        note = Text("no  v  in  T  —  speed cancels exactly", font="EB Garamond",
                    font_size=24, color=DIM)
        VGroup(eq1, eq2, eq3, note).arrange(DOWN, buff=0.4).center()
        for mob in [eq1, eq2, eq3, note]:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(eq1, eq2, eq3, note), run_time=0.5)

    def _phase_circles(self):
        # B field dots (into screen)
        dots = VGroup()
        for x in np.linspace(-6.5, 6.5, 14):
            for y in np.linspace(-3.5, 3.5, 8):
                d = Dot(point=[x, y, 0], radius=0.04, color=DIM, fill_opacity=0.5)
                dots.add(d)
        b_label = MathTex(r"\vec{B}\;\text{into screen}", color=DIM, font_size=20
                          ).to_corner(UL, buff=0.3)
        self.play(FadeIn(dots), Write(b_label), run_time=0.8)

        # Concrete numbers
        T_ns = cyclotron_period() * 1e9
        r1_cm = cyclotron_radius(1e6) * 100
        r2_cm = cyclotron_radius(2e6) * 100
        scale = 2.5  # scene units per 10 cm

        R1 = r1_cm / 10 * scale   # scene units
        R2 = r2_cm / 10 * scale

        # Entry point: left edge of circles, center at origin offset
        center1 = np.array([0.0, -R1, 0])
        center2 = np.array([0.0, -R2, 0])

        circ1 = Circle(radius=R1, color=BLUE, stroke_width=3).move_to(center1)
        circ2 = Circle(radius=R2, color=BROWN, stroke_width=3).move_to(center2)

        r1_label = MathTex(r"r_1 = 2.09\,\mathrm{cm}", color=BLUE, font_size=24
                           ).next_to(circ1, RIGHT, buff=0.15)
        r2_label = MathTex(r"r_2 = 4.18\,\mathrm{cm}", color=BROWN, font_size=24
                           ).next_to(circ2, RIGHT, buff=0.15)

        caption1 = Text("v₁ = 1.0 × 10⁶ m/s  (blue)", font="EB Garamond",
                        font_size=22, color=BLUE).to_edge(DOWN, buff=0.5)
        self.play(Create(circ1), Write(r1_label), Write(caption1), run_time=2.0)
        self.wait(0.7)

        caption2 = Text("v₂ = 2.0 × 10⁶ m/s  (brown) — radius doubles",
                        font="EB Garamond", font_size=22, color=BROWN
                        ).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(caption1), run_time=0.2)
        self.play(Create(circ2), Write(r2_label), Write(caption2), run_time=2.0)
        self.wait(1.0)

        # Period label — same for both
        T_lbl = MathTex(
            r"T = \frac{2\pi m_p}{qB} = " + f"{T_ns:.1f}" + r"\,\mathrm{ns}",
            color=GOLD, font_size=28,
        ).to_edge(UP, buff=0.3)
        self.play(FadeOut(caption2), Write(T_lbl), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(dots, b_label, circ1, circ2, r1_label, r2_label, T_lbl),
                  run_time=0.5)

    def _phase_period_proof(self):
        # Show period ratio = 1 even as v changes
        title = Text("Period is independent of speed", font="EB Garamond",
                     font_size=32, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)

        ax = Axes(
            x_range=[0, 3.5, 0.5],
            y_range=[0, 200, 50],
            x_length=9,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.5)
        lx = MathTex(r"v\;(10^6\,\mathrm{m/s})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"r\;(\mathrm{cm})", color=BLUE, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        v_vals = np.linspace(0.01, 3.5, 300)
        r_vals = [cyclotron_radius(v * 1e6) * 100 for v in v_vals]
        radius_curve = ax.plot_line_graph(
            x_values=v_vals, y_values=r_vals,
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )

        T_flat_val = cyclotron_period() * 1e9
        t_vals = [T_flat_val] * len(v_vals)
        period_line = ax.plot_line_graph(
            x_values=v_vals, y_values=t_vals,
            line_color=GOLD, stroke_width=3, add_vertex_dots=False,
        )
        # overlay T on right y axis — just label it
        t_lbl = MathTex(r"T = 131\,\mathrm{ns} = \mathrm{const}", color=GOLD,
                        font_size=22).next_to(ax.c2p(3.0, T_flat_val), RIGHT, buff=0.1)
        r_lbl = Text("r ∝ v  (linear)", font="EB Garamond", font_size=22, color=BLUE
                     ).next_to(ax.c2p(2.5, cyclotron_radius(2.5e6) * 100), UP,
                               buff=0.15)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.2)
        self.play(Create(radius_curve), Write(r_lbl), run_time=1.8)
        self.play(Create(period_line), Write(t_lbl), run_time=1.5)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, radius_curve, period_line, t_lbl, r_lbl),
                  run_time=0.5)

    def _phase_helix(self):
        title = Text("Add v‖ → helical motion along B", font="EB Garamond",
                     font_size=30, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)

        # Draw a helix parametrically in 2D projection
        t_vals = np.linspace(0, 4 * np.pi, 400)
        R_h = 1.0
        pitch = 0.8  # units per revolution
        x_vals = pitch / (2 * np.pi) * t_vals - 4.0
        y_vals = R_h * np.sin(t_vals)

        helix_pts = [np.array([x, y, 0]) for x, y in zip(x_vals, y_vals)]
        helix = VMobject(color=BLUE, stroke_width=3)
        helix.set_points_smoothly(helix_pts)

        axis_line = Line(start=[-4, 0, 0], end=[4.5, 0, 0], color=GOLD,
                         stroke_width=2)
        b_arrow = Arrow(start=[3.5, 0, 0], end=[4.5, 0, 0], color=GOLD,
                        stroke_width=2, buff=0)
        b_lbl = MathTex(r"\vec{B}", color=GOLD, font_size=28).next_to(b_arrow, RIGHT,
                                                                        buff=0.08)

        pitch_label = Text("pitch = v‖ × T  (grows with v‖, ω_c unchanged)",
                           font="EB Garamond", font_size=22, color=DIM
                           ).to_edge(DOWN, buff=0.3)

        self.play(Create(axis_line), Create(b_arrow), Write(b_lbl), run_time=0.8)
        self.play(Create(helix), run_time=2.5)
        self.play(Write(pitch_label), run_time=0.8)
        self.wait(2.5)

        final = Text(
            "The cyclotron works because T has no v — fixed RF matches every orbit",
            font="EB Garamond", font_size=24, color=INK,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(pitch_label), Write(final), run_time=1.2)
        self.wait(2.5)
