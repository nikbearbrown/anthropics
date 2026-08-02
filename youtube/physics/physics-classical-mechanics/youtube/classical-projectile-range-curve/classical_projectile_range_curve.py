#!/usr/bin/env python3
"""
classical_projectile_range_curve.py — Projectile Range: 45° Max and Complementary Pairs
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    v₀ = 30.0 m/s, g = 9.80 m/s²
    R = v₀²sin(2θ)/g
    R(45°) = 91.84 m,  R(30°)=R(60°)=79.53 m

Render:
    cd physics-classical-mechanics/youtube/classical-projectile-range-curve
    manim -qh classical_projectile_range_curve.py ClassicalProjectileRangeScene
"""
import sys
import numpy as np

V0 = 30.0
G  = 9.80
THETAS = [15, 20, 30, 45, 60, 70, 75]


def range_m(theta_deg): return V0**2 * np.sin(2*np.radians(theta_deg)) / G
def height_m(theta_deg): return V0**2 * np.sin(np.radians(theta_deg))**2 / (2*G)
def trajectory(theta_deg, n=200):
    th = np.radians(theta_deg)
    T  = 2*V0*np.sin(th)/G
    t  = np.linspace(0, T, n)
    return V0*np.cos(th)*t, V0*np.sin(th)*t - 0.5*G*t**2


def verify():
    print("=== Classical Projectile Range verification ===")
    for th in THETAS:
        R = range_m(th)
        H = height_m(th)
        print(f"  θ={th:2d}°: R={R:.2f} m, H={H:.2f} m")
    # P1: R(45°) = v₀²/g
    R45 = range_m(45)
    assert abs(R45 - V0**2/G) < 1e-8, "P1"
    print(f"  R_max = v₀²/g = {V0**2/G:.2f} m  ✓")
    # P2: R(30°) = R(60°)
    assert abs(range_m(30) - range_m(60)) < 1e-8, "P2 complementary"
    print(f"  R(30°) = R(60°) = {range_m(30):.2f} m  ✓")
    print(f"  H(30°) = {height_m(30):.2f} m,  H(60°) = {height_m(60):.2f} m  (ratio 1:3)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

ANGLE_COLORS = {15: DIM, 20: BROWN, 30: BROWN, 45: GOLD, 60: BLUE, 70: BLUE, 75: DIM}


class ClassicalProjectileRangeScene(Scene):
    """Range arcs + R(θ) curve; complementary pairs highlighted."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax_traj = self._draw_arcs()
        self._range_curve(ax_traj)

    def _title(self):
        t1 = Text("Projectile Range", font="EB Garamond", font_size=64, color=INK)
        t2 = Text("45° wins — 30° and 60° land at the same spot",
                  font="EB Garamond", font_size=26, color=DIM)
        t3 = MathTex(r"R = \frac{v_0^2\sin 2\theta}{g}\qquad v_0=30\,\mathrm{m/s}",
                     color=BLUE, font_size=30)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _draw_arcs(self):
        ax = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 50, 10],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).to_edge(DOWN, buff=0.9)
        lx = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"y\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Trajectories  (v₀ = 30 m/s)", font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.15)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        for th in THETAS:
            col = ANGLE_COLORS[th]
            xs, ys = trajectory(th)
            pts = np.array([ax.c2p(x, y) for x, y in zip(xs, ys)])
            crv = VMobject(color=col, stroke_width=2.2).set_points_smoothly(pts)
            lbl = MathTex(rf"{th}°", color=col, font_size=20)
            lbl.move_to(ax.c2p(xs.max()/2, ys.max() + 1.5))
            self.play(Create(crv), Write(lbl), run_time=0.8)

        # Complementary pair bracket
        r30 = range_m(30)
        r60 = range_m(60)
        dbl = DoubleArrow(ax.c2p(r30, 0), ax.c2p(r60, 0), color=GOLD, buff=0, stroke_width=2, tip_length=0.16)
        cap = Text("R(30°) = R(60°) = 79.5 m", font="EB Garamond", font_size=19, color=GOLD).to_edge(DOWN, buff=0.22)
        self.play(GrowArrow(dbl), Write(cap), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(cap), run_time=0.3)
        return ax

    def _range_curve(self, ax_traj):
        self.play(FadeOut(ax_traj), run_time=0.4)
        ax = Axes(
            x_range=[0, 90, 15],
            y_range=[0, 100, 20],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).to_edge(DOWN, buff=0.9)
        lx = MathTex(r"\theta\;(°)", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"R\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Range vs angle  — symmetric about 45°",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        ths = np.linspace(0.1, 89.9, 400)
        Rs  = V0**2 * np.sin(np.radians(2*ths)) / G
        pts = np.array([ax.c2p(th, R) for th, R in zip(ths, Rs)])
        crv = VMobject(color=BLUE, stroke_width=3.0).set_points_smoothly(pts)
        self.play(Create(crv), run_time=2.0)

        # 45° peak
        peak = Dot(ax.c2p(45, range_m(45)), color=GOLD, radius=0.10)
        peak_lbl = MathTex(r"45°: R=91.8\,\mathrm{m}", color=GOLD, font_size=22).next_to(peak, UR, buff=0.1)
        self.play(FadeIn(peak), Write(peak_lbl), run_time=0.7)

        # Complementary pair 30/60
        d30 = Dot(ax.c2p(30, range_m(30)), color=BROWN, radius=0.09)
        d60 = Dot(ax.c2p(60, range_m(60)), color=BROWN, radius=0.09)
        dbl2 = DoubleArrow(ax.c2p(30, range_m(30)), ax.c2p(60, range_m(60)),
                           color=BROWN, buff=0, stroke_width=1.8, tip_length=0.15)
        self.play(FadeIn(d30, d60), GrowArrow(dbl2), run_time=0.6)

        final = Text(
            "Below 45°: air drag pushes the optimum even lower for real projectiles",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
