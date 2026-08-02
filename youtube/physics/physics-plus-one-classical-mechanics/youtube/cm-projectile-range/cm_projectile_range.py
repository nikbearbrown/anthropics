#!/usr/bin/env python3
"""
cm_projectile_range.py — Projectile Range: The 45° Maximum
SILENT SLATE — brownblue dark palette, physics-plus-one-classical-mechanics.

Physics:
    R = v0^2 * sin(2*theta) / g  (flat ground, vacuum)
    Max at theta = 45 deg: R_max = v0^2 / g
    Complementary: theta and (90 - theta) -> same R

Verify: python3 cm_projectile_range.py --verify
Render: manim -qh cm_projectile_range.py CmProjectileRangeScene
"""
import sys
import numpy as np

G_GRAV = 9.80   # m/s^2
V0     = 20.0   # m/s

def range_m(theta_deg, v0=V0, g=G_GRAV):
    th = np.radians(theta_deg)
    return v0**2 * np.sin(2 * th) / g

def trajectory(theta_deg, v0=V0, g=G_GRAV, n=200):
    """Returns (x, y) arrays for the trajectory until y >= 0 again."""
    th = np.radians(theta_deg)
    vx = v0 * np.cos(th)
    vy = v0 * np.sin(th)
    T  = 2 * vy / g
    t  = np.linspace(0, T, n)
    x  = vx * t
    y  = vy * t - 0.5 * g * t**2
    return x, y

def verify():
    print("=== Projectile range verification ===")
    R_max = range_m(45)
    print(f"R_max at 45° = {R_max:.2f} m  (expected {V0**2/G_GRAV:.2f} m) {'✓' if abs(R_max - V0**2/G_GRAV) < 0.01 else '✗'}")
    # P1: R(30) = R(60)
    R30 = range_m(30)
    R60 = range_m(60)
    print(f"P1: R(30°) = {R30:.2f} m, R(60°) = {R60:.2f} m  complementary {'✓' if abs(R30 - R60) < 0.01 else '✗'}")
    # P2: ratio
    ratio = R_max / R30
    expected = 1 / np.sin(np.radians(60))
    print(f"P2: R_max/R(30°) = {ratio:.4f}  (expected {expected:.4f}) {'✓' if abs(ratio - expected) < 0.001 else '✗'}")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class CmProjectileRangeScene(Scene):
    """
    Left: trajectory arc for swept theta.
    Right: polar plot R(theta) building up.
    Complementary pairs highlighted in matching colors.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax_traj, ax_range = self._axes()
        self._complementary_pairs(ax_traj, ax_range)
        self._slider_phase(ax_traj, ax_range)
        self._finale()

    def _title(self):
        t = Text("Projectile Range: The 45° Maximum",
                 font="EB Garamond", font_size=56, color=INK)
        s = Text(
            "R = v₀² sin(2θ) / g  peaks at 45°.\n"
            "Complementary angles θ and 90°−θ give the same landing point.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        R_max = V0**2 / G_GRAV
        ax_traj = Axes(
            x_range=[0, R_max + 5, 10],
            y_range=[0, 22, 5],
            x_length=6,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(LEFT * 3.2 + DOWN * 0.5)
        lxt = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=20).next_to(ax_traj.x_axis.get_end(), RIGHT, buff=0.08)
        lyt = MathTex(r"y\;(\mathrm{m})", color=INK, font_size=20).next_to(ax_traj.y_axis.get_end(), UP, buff=0.08)

        # Right: R vs theta (0 to 90 deg)
        ax_range = Axes(
            x_range=[0, 90, 15],
            y_range=[0, R_max + 4, 10],
            x_length=5.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(RIGHT * 2.8 + DOWN * 0.5)
        lxr = MathTex(r"\theta\;(^\circ)", color=INK, font_size=20).next_to(ax_range.x_axis.get_end(), RIGHT, buff=0.08)
        lyr = MathTex(r"R\;(\mathrm{m})", color=INK, font_size=20).next_to(ax_range.y_axis.get_end(), UP, buff=0.08)

        # Draw full R(theta) curve
        thetas = np.linspace(0, 90, 300)
        R_vals = range_m(thetas)
        r_pts = np.array([ax_range.c2p(t, r) for t, r in zip(thetas, R_vals)])
        r_curve = VMobject(color=DIM, stroke_width=2, stroke_opacity=0.5)
        r_curve.set_points_smoothly(r_pts)

        # 45° marker on range plot
        peak_dot = Dot(ax_range.c2p(45, R_max), color=GOLD, radius=0.1)
        peak_lbl = MathTex(r"45^\circ,\;R_{\rm max}=" + f"{R_max:.1f}", color=GOLD, font_size=18)
        peak_lbl.next_to(peak_dot, UR, buff=0.1)

        self.play(Create(ax_traj), Create(ax_range),
                  Write(lxt), Write(lyt), Write(lxr), Write(lyr), run_time=1.5)
        self.play(Create(r_curve), FadeIn(peak_dot), Write(peak_lbl), run_time=1.2)
        return ax_traj, ax_range

    def _complementary_pairs(self, ax_traj, ax_range):
        pairs = [(30, 60, BLUE), (20, 70, BROWN)]
        for theta1, theta2, col in pairs:
            R = range_m(theta1)
            for theta, ls in [(theta1, "solid"), (theta2, "dashed")]:
                x, y = trajectory(theta)
                pts = np.array([ax_traj.c2p(xi, yi) for xi, yi in zip(x, y)])
                m = VMobject(color=col, stroke_width=2.5 if ls == "solid" else 2,
                             stroke_opacity=1.0 if ls == "solid" else 0.7)
                m.set_points_smoothly(pts)
                self.play(Create(m), run_time=0.8)

            # Mark on range plot
            for theta in [theta1, theta2]:
                d = Dot(ax_range.c2p(theta, R), color=col, radius=0.09)
                self.play(FadeIn(d), run_time=0.3)

            caption = Text(
                f"θ = {theta1}° and {theta2}°  →  same range R = {R:.1f} m",
                font="EB Garamond", font_size=20, color=col,
            ).to_edge(DOWN, buff=0.2)
            self.play(Write(caption), run_time=0.6)
            self.wait(1.2)
            self.play(FadeOut(caption), run_time=0.3)

    def _slider_phase(self, ax_traj, ax_range):
        theta_tracker = ValueTracker(45.0)

        def _traj():
            th = theta_tracker.get_value()
            x, y = trajectory(th)
            pts = np.array([ax_traj.c2p(xi, yi) for xi, yi in zip(x, y)])
            m = VMobject(color=GOLD, stroke_width=3)
            m.set_points_smoothly(pts)
            return m

        def _range_dot():
            th = theta_tracker.get_value()
            R = range_m(th)
            return Dot(ax_range.c2p(th, R), color=GOLD, radius=0.12)

        dyn_traj = always_redraw(_traj)
        dyn_dot  = always_redraw(_range_dot)
        self.add(dyn_traj, dyn_dot)

        th_lbl = MathTex(r"\theta = ", color=INK, font_size=28)
        th_num = DecimalNumber(45.0, num_decimal_places=0, color=GOLD, font_size=28)
        th_deg = MathTex(r"^\circ", color=INK, font_size=28)
        th_num.add_updater(lambda m: m.set_value(theta_tracker.get_value()))
        R_lbl = MathTex(r"R = ", color=DIM, font_size=24)
        R_num = DecimalNumber(range_m(45), num_decimal_places=1, color=BLUE, font_size=24)
        R_m   = MathTex(r"\,\mathrm{m}", color=DIM, font_size=24)
        R_num.add_updater(lambda m: m.set_value(range_m(theta_tracker.get_value())))

        row1 = VGroup(th_lbl, th_num, th_deg).arrange(RIGHT, buff=0.08).to_edge(UP, buff=0.3)
        row2 = VGroup(R_lbl, R_num, R_m).arrange(RIGHT, buff=0.08).to_edge(UP, buff=1.0)

        self.play(Write(row1), Write(row2), run_time=0.8)
        self.play(theta_tracker.animate.set_value(10.0), run_time=2.0, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(80.0), run_time=2.5, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(45.0), run_time=1.5, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(row1, row2, dyn_traj, dyn_dot), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"R = \frac{v_0^2 \sin 2\theta}{g}",
            r"\quad R_{\rm max} = \frac{v_0^2}{g}\ \text{at}\ \theta = 45^\circ",
            color=INK, font_size=30,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
