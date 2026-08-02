#!/usr/bin/env python3
"""
physics_projectile_range_curve.py — Projectile Range: 45° Wins, Complementary Pairs Tie
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    v₀ = 20 m/s, g = 9.80 m/s²
    R = v₀²sin(2θ)/g
    R(45°) = 40.8 m (max), R(30°) = R(60°) = 35.3 m, R(15°) = R(75°) = 20.4 m

Render:
    cd physics/youtube/physics-projectile-range-curve
    manim -qh physics_projectile_range_curve.py ProjectileRangeScene
"""
import sys
import numpy as np

# ── Physics constants ─────────────────────────────────────────────────────────
V0   = 20.0   # m/s
G    = 9.80   # m/s²
THETAS = [15, 30, 45, 60, 75]


def range_m(v0, theta_deg, g=G):
    th = np.radians(theta_deg)
    return v0**2 * np.sin(2*th) / g


def trajectory(v0, theta_deg, g=G, n=200):
    th = np.radians(theta_deg)
    R  = range_m(v0, theta_deg, g)
    T  = 2 * v0 * np.sin(th) / g
    t  = np.linspace(0, T, n)
    x  = v0 * np.cos(th) * t
    y  = v0 * np.sin(th) * t - 0.5 * g * t**2
    return x, y


def verify():
    print("=== Projectile Range Curve verification ===")
    for th in THETAS:
        R = range_m(V0, th)
        print(f"  θ={th:3d}°: R = {R:.2f} m")
    print(f"  R_max at 45° = v₀²/g = {V0**2/G:.2f} m")
    print(f"  Complementary: R(30°)={range_m(V0,30):.2f} == R(60°)={range_m(V0,60):.2f}")
    print(f"  Complementary: R(15°)={range_m(V0,15):.2f} == R(75°)={range_m(V0,75):.2f}")
    y_max = V0**2 * np.sin(np.radians(45))**2 / (2*G)
    print(f"  Peak height at 45°: {y_max:.2f} m")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
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

ARC_COLORS = [BROWN, GOLD, BLUE, GOLD, BROWN]


class ProjectileRangeScene(Scene):
    """Five arcs draw sequentially, complementary pairs highlighted,
    then the full R(θ) curve traces out from 0° to 90°."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_arcs(ax)
        self._range_curve(ax)

    def _title(self):
        t1 = Text("Projectile Range", font="EB Garamond", font_size=62, color=INK)
        t2 = Text("45° wins — complementary pairs tie", font="EB Garamond", font_size=26, color=DIM)
        t3 = MathTex(r"R = \frac{v_0^2 \sin 2\theta}{g}", color=BLUE, font_size=36)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.35).center()
        self.play(Write(t1), run_time=1.2)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[0, 55, 10],
            y_range=[0, 15, 5],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.2),
        ).to_edge(DOWN, buff=0.9)
        lx = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"y\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        hdr = Text("Trajectories  (v₀ = 20 m/s)", font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.15)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.5)
        return ax

    def _draw_arcs(self, ax):
        arcs_on_screen = []
        for i, th in enumerate(THETAS):
            col = ARC_COLORS[i]
            xs, ys = trajectory(V0, th)
            pts = np.array([ax.c2p(x, y) for x, y in zip(xs, ys)])
            curve = VMobject(color=col, stroke_width=2.8)
            curve.set_points_smoothly(pts)

            R = range_m(V0, th)
            lbl = MathTex(rf"{th}°", color=col, font_size=22).move_to(ax.c2p(R/2, ys.max() + 0.6))

            info = Text(
                f"θ = {th}°   R = {R:.1f} m",
                font="EB Garamond", font_size=20, color=col,
            ).to_edge(DOWN, buff=0.18)
            self.play(Create(curve), Write(lbl), Write(info), run_time=1.4)
            self.wait(0.5)
            self.play(FadeOut(info), run_time=0.2)
            arcs_on_screen.append((curve, lbl))

        # Complementary-pair highlights
        pair_caption = Text(
            "R(30°) = R(60°) = 35.3 m  — complementary angles tie",
            font="EB Garamond", font_size=20, color=GOLD,
        ).to_edge(DOWN, buff=0.18)
        # bracket connecting landing dots of 30 and 60
        r30 = range_m(V0, 30)
        r60 = range_m(V0, 60)
        land_30 = ax.c2p(r30, 0)
        land_60 = ax.c2p(r60, 0)
        arrow = DoubleArrow(land_30, land_60, color=GOLD, buff=0, stroke_width=2.5, tip_length=0.18)
        self.play(GrowArrow(arrow), Write(pair_caption), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(arrow, pair_caption), run_time=0.4)

    def _range_curve(self, ax_traj):
        # New axes for R vs θ on top half
        self.play(FadeOut(ax_traj), run_time=0.6)
        ax = Axes(
            x_range=[0, 90, 15],
            y_range=[0, 45, 10],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, tip_length=0.2),
        ).to_edge(DOWN, buff=0.9)
        lx = MathTex(r"\theta\;(°)", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"R\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        hdr = Text("Range vs launch angle", font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        ths = np.linspace(0.1, 89.9, 400)
        Rs  = V0**2 * np.sin(np.radians(2*ths)) / G
        pts = np.array([ax.c2p(th, R) for th, R in zip(ths, Rs)])
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=2.5)

        # Mark peak at 45°
        peak = ax.c2p(45, V0**2/G)
        dot45 = Dot(peak, color=GOLD, radius=0.1)
        lbl45 = MathTex(r"\theta=45°,\;R=40.8\,\mathrm{m}", color=GOLD, font_size=22).next_to(dot45, UR, buff=0.1)
        self.play(FadeIn(dot45), Write(lbl45), run_time=0.8)

        # Mark complementary pairs
        for th_a, th_b in [(30, 60), (15, 75)]:
            R_pair = range_m(V0, th_a)
            da = Dot(ax.c2p(th_a, R_pair), color=BROWN, radius=0.08)
            db = Dot(ax.c2p(th_b, R_pair), color=BROWN, radius=0.08)
            dbl = DoubleArrow(ax.c2p(th_a, R_pair), ax.c2p(th_b, R_pair),
                              color=BROWN, buff=0, stroke_width=1.8, tip_length=0.15)
            self.play(FadeIn(da, db), GrowArrow(dbl), run_time=0.6)

        final = Text(
            "45° is maximum — only angle with no complementary twin",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
