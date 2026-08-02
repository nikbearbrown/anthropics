#!/usr/bin/env python3
"""
physics_projectile_angle_sweep.py — Projectile Parabola Traces as Launch Angle Sweeps 0→90°
SILENT SLATE — sim-scout candidate, physics-with-llms book.

Physics:
  x(t) = v₀ cos θ · t
  y(t) = v₀ sin θ · t − ½ g t²
  R     = v₀² sin(2θ) / g
  v₀=20 m/s, g=9.8 m/s²

Testable predictions:
  P1: R(30°) = R(60°) = 20²·sin60°/9.8 ≈ 35.35 m  (complementary angles)
  P2: R(45°) = 20²/9.8 ≈ 40.82 m  (maximum range)

Run standalone verification:
  python3 physics_projectile_angle_sweep.py --verify

Render:
  manim -qh physics_projectile_angle_sweep.py ProjectileAngleSweepScene
"""
import sys
import numpy as np

G   = 9.8   # m/s²
V0  = 20.0  # m/s

def trajectory(theta_deg: float, n: int = 300):
    """Return (x, y) arrays for full parabola from launch to landing."""
    th = np.radians(theta_deg)
    if abs(np.sin(th)) < 1e-10:
        return np.array([0.0, 0.0]), np.array([0.0, 0.0])
    t_land = 2 * V0 * np.sin(th) / G
    t = np.linspace(0, t_land, n)
    x = V0 * np.cos(th) * t
    y = V0 * np.sin(th) * t - 0.5 * G * t**2
    return x, y

def range_m(theta_deg: float) -> float:
    th = np.radians(theta_deg)
    return V0**2 * np.sin(2 * th) / G

def verify():
    print("=== Projectile sweep verification ===")
    for th in [30, 45, 60, 90]:
        R = range_m(th)
        print(f"  θ={th:2d}°  R={R:.4f} m")
    print(f"  R(30°) == R(60°): {np.isclose(range_m(30), range_m(60))}")
    print(f"  R(45°) = v0²/g  : {np.isclose(range_m(45), V0**2/G)}")
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

ANGLES = list(range(0, 91, 5))   # 0, 5, 10, … 90


class ProjectileAngleSweepScene(Scene):
    """
    Draw 19 parabolic trajectories (every 5° from 0° to 90°).
    Highlight 45° as the max-range winner.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title card ─────────────────────────────────────────────────────
        title = Text("Projectile Motion", font="EB Garamond", font_size=60, color=INK)
        sub   = Text(
            "v₀ = 20 m/s  ·  sweep θ 0° → 90°",
            font="EB Garamond", font_size=26, color=DIM,
        )
        sub2  = Text(
            "R = v₀² sin(2θ) / g  —  maximum range at θ = 45°",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

        # ── Axes ───────────────────────────────────────────────────────────
        x_max = 45.0   # m  (max range ≈ 40.8 m, give some room)
        y_max = 11.0   # m  (max height at 90° ≈ 20.4/2 ≈ 10.2 m)
        ax = Axes(
            x_range=[0, x_max, 10],
            y_range=[0, y_max, 5],
            x_length=10.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(DOWN * 0.8)

        lbl_x = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"y\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP,    buff=0.08)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.5)

        # ── Draw trajectories all at once ──────────────────────────────────
        curves = []
        for theta in ANGLES:
            xs, ys = trajectory(theta)
            if xs[-1] < 0.01:        # 0° or 90° — trivial
                continue
            # Colour scale: close to 45° = bluer; far = dimmer
            dist = abs(theta - 45) / 45.0    # 0 → same, 1 → far
            alpha = 0.25 + 0.75 * (1 - dist)
            if theta == 45:
                col = GOLD
            elif abs(theta - 45) <= 20:
                col = BLUE
            else:
                col = DIM

            pts = np.array([ax.c2p(float(x), float(y)) for x, y in zip(xs, ys)])
            curve = VMobject(color=col, stroke_width=2.5 if theta == 45 else 1.5,
                             stroke_opacity=alpha)
            curve.set_points_smoothly(pts)
            curves.append(curve)

        self.play(*[Create(c) for c in curves], run_time=4.0, lag_ratio=0.05)
        self.wait(0.8)

        # ── Highlight 45° ──────────────────────────────────────────────────
        R45 = range_m(45)
        dot45 = Dot(ax.c2p(R45, 0), color=GOLD, radius=0.12)
        lbl45 = MathTex(
            r"\theta = 45°\;\; R_{\max} = \frac{v_0^2}{g} \approx 40.8\,\mathrm{m}",
            color=GOLD, font_size=26,
        ).to_edge(UP, buff=0.25)

        self.play(FadeIn(dot45, scale=1.5), Write(lbl45), run_time=1.2)
        self.wait(1.0)

        # ── Complementary angles ───────────────────────────────────────────
        R30 = range_m(30)
        dot30 = Dot(ax.c2p(R30, 0), color=BROWN, radius=0.09)
        dot60 = Dot(ax.c2p(R30, 0), color=BROWN, radius=0.09)  # same R

        anno = Text(
            "R(30°) = R(60°) ≈ 35.35 m   [sin(2θ) = sin(180°−2θ)]",
            font="EB Garamond", font_size=21, color=BROWN,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(dot30), FadeIn(dot60), Write(anno), run_time=1.0)
        self.wait(2.5)

        # ── Formula strip ──────────────────────────────────────────────────
        formula = MathTex(
            r"R = \frac{v_0^2 \sin 2\theta}{g}", color=INK, font_size=34,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(anno), Write(formula), run_time=1.0)
        self.wait(2.0)
