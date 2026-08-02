#!/usr/bin/env python3
"""
snells_law_geometry_sweep.py — Snell's Law Geometry: Ray Bending as n₂/n₁ Ratio Sweeps
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/snells-law-geometry-sweep
    manim -qh snells_law_geometry_sweep.py SnellsLawGeometrySweepScene

Numpy verification (run standalone):
    python3 snells_law_geometry_sweep.py --verify

Physics (checkable):
    n₁sinθ₁ = n₂sinθ₂  →  θ₂ = arcsin(n₁sinθ₁/n₂)

    P1: n₁=1.0, n₂=1.5, θ₁=30°: θ₂=arcsin(sin30°/1.5)=arcsin(0.333)=19.47° ✓
    P2: n₁=1.5, n₂=1.0, θ₁=45°: sinθ₂=1.5×sin45°=1.06>1 → TIR ✓
"""
import sys
import numpy as np


def refracted_angle(theta1_deg: float, n1: float, n2: float):
    """θ₂ from Snell's law. Returns None for TIR."""
    val = n1 * np.sin(np.radians(theta1_deg)) / n2
    if abs(val) > 1.0:
        return None
    return np.degrees(np.arcsin(val))


def verify():
    print("=== Snell's Law geometry sweep verification ===")
    # P1
    t2 = refracted_angle(30.0, 1.0, 1.5)
    print(f"P1: n1=1.0, n2=1.5, θ1=30° → θ2={t2:.2f}° (should be ≈19.47°)")
    # P2
    t2_tir = refracted_angle(45.0, 1.5, 1.0)
    print(f"P2: n1=1.5, n2=1.0, θ1=45° → θ2={t2_tir} (should be None/TIR)")
    # Fixed θ1=45°, sweep n2/n1
    print("\nSweep n2/n1 at θ1=45°, n1=1.0:")
    for ratio in [0.5, 0.75, 1.0, 1.33, 1.5, 2.42]:
        t2 = refracted_angle(45.0, 1.0, ratio)
        label = f"{t2:.2f}°" if t2 is not None else "TIR"
        print(f"  n2/n1={ratio:.2f}  →  θ2={label}")
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
ORANGE = "#FF9800"

THETA1 = 45.0   # fixed incident angle (degrees)
N1 = 1.0
RAY_LEN = 3.0


def make_refracted_ray(origin, ratio, length=RAY_LEN):
    """Build a refracted ray arrow below the interface."""
    t2 = refracted_angle(THETA1, N1, ratio)
    if t2 is None:
        return None
    ref_x = np.sin(np.radians(t2)) * length
    ref_y = -np.cos(np.radians(t2)) * length
    return Arrow(
        start=origin, end=origin + np.array([ref_x, ref_y, 0]),
        color=BLUE, stroke_width=4.5, buff=0,
        max_tip_length_to_length_ratio=0.1,
    )


class SnellsLawGeometrySweepScene(Scene):
    """
    Fixed interface with incident ray at 45°.
    n2/n1 sweeps through scripted stops — refracted ray animated step by step.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Snell's Law", font="EB Garamond", font_size=64, color=INK)
        sub = Text(
            "n₁ sin θ₁ = n₂ sin θ₂  ·  incident angle fixed at 45°",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2 = Text(
            "Sweep n₂/n₁ from 0.5 to 2.42  — ray reverses bend direction at ratio = 1",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_sweep(self):
        origin = np.array([0, 0, 0])

        # Interface line
        interface = Line(LEFT * 6, RIGHT * 6, color=DIM, stroke_width=2.0)
        # Normal (dashed)
        normal = DashedLine(UP * 2.8, DOWN * 2.8, color=DIM, stroke_width=1.2, dash_length=0.15)
        normal_lbl = Text("Normal", font="EB Garamond", font_size=16, color=DIM)
        normal_lbl.next_to(normal.get_top(), RIGHT, buff=0.08).shift(DOWN * 0.3)

        # Medium labels
        n1_lbl = Text("n₁ = 1.0", font="EB Garamond", font_size=22, color=BROWN)
        n1_lbl.move_to([-4.8, 1.4, 0])

        self.play(Create(interface), Create(normal), Write(normal_lbl), Write(n1_lbl), run_time=1.2)

        # Incident ray (fixed at 45°)
        inc_s = np.array([
            -np.sin(np.radians(THETA1)) * RAY_LEN,
            np.cos(np.radians(THETA1)) * RAY_LEN, 0,
        ])
        inc_ray = Arrow(start=inc_s, end=origin, color=ORANGE, stroke_width=4.5, buff=0,
                        max_tip_length_to_length_ratio=0.1)
        t1_lbl = MathTex(r"\theta_1 = 45°", color=ORANGE, font_size=26).move_to([0.9, 1.2, 0])

        self.play(Create(inc_ray), Write(t1_lbl), run_time=0.8)

        # Reflected ray (fixed, weak)
        refl_end = np.array([
            np.sin(np.radians(THETA1)) * RAY_LEN,
            np.cos(np.radians(THETA1)) * RAY_LEN, 0,
        ])
        reflected = Arrow(start=origin, end=refl_end, color=DIM, stroke_width=2.0, buff=0,
                          max_tip_length_to_length_ratio=0.08)
        self.play(Create(reflected), run_time=0.5)

        # Scripted stops: (ratio, label, color)
        stops = [
            (0.75, "n₂/n₁ = 0.75  →  less dense: ray bends AWAY from normal", DIM),
            (1.00, "n₂/n₁ = 1.00  →  same density: ray passes straight through", GOLD),
            (1.33, "n₂/n₁ = 1.33  →  denser (air→water): bend toward normal", BLUE),
            (1.50, "n₂/n₁ = 1.50  →  air→glass: θ₂ = 28.1°", BLUE),
            (2.42, "n₂/n₁ = 2.42  →  air→diamond: θ₂ = 17.0°", BROWN),
        ]

        # Build initial refracted ray at ratio=0.5 (which is TIR — show reflected only)
        # Start at ratio=0.75 for first visible case
        ratio_init = 0.75
        ref_ray = make_refracted_ray(origin, ratio_init)
        if ref_ray is None:
            ref_ray = Arrow(start=origin, end=origin + RIGHT * 0.001, color=BLUE, stroke_width=0, buff=0)

        n2_lbl = Text(f"n₂ = {ratio_init:.2f}", font="EB Garamond", font_size=22, color=BLUE)
        n2_lbl.move_to([-4.8, -1.8, 0])
        t2_val = refracted_angle(THETA1, N1, ratio_init)
        t2_lbl = MathTex(
            rf"\theta_2 = {t2_val:.1f}°" if t2_val is not None else r"\theta_2 = \text{TIR}",
            color=BLUE, font_size=26,
        ).move_to([-4.5, -0.6, 0])
        cap0 = Text(stops[0][1], font="EB Garamond", font_size=21, color=stops[0][2]).to_edge(UP, buff=0.22)

        self.play(Create(ref_ray), Write(n2_lbl), Write(t2_lbl), Write(cap0), run_time=1.0)
        self.wait(0.9)

        for ratio, text, col in stops[1:]:
            t2_new = refracted_angle(THETA1, N1, ratio)
            new_ref = make_refracted_ray(origin, ratio)
            if new_ref is None:
                new_ref = Arrow(start=origin, end=origin + RIGHT * 0.001, color=BLUE, stroke_width=0, buff=0)

            new_n2 = Text(f"n₂ = {ratio:.2f}", font="EB Garamond", font_size=22, color=BLUE).move_to([-4.8, -1.8, 0])
            new_t2 = MathTex(
                rf"\theta_2 = {t2_new:.1f}°" if t2_new is not None else r"\theta_2 = \text{TIR}",
                color=BLUE, font_size=26,
            ).move_to([-4.5, -0.6, 0])
            new_cap = Text(text, font="EB Garamond", font_size=21, color=col).to_edge(UP, buff=0.22)

            self.play(
                Transform(ref_ray, new_ref),
                Transform(n2_lbl, new_n2),
                Transform(t2_lbl, new_t2),
                Transform(cap0, new_cap),
                run_time=1.5, rate_func=smooth,
            )
            self.wait(0.9)

        # Final payoff
        payoff = MathTex(
            r"n_1 \sin\theta_1 = n_2 \sin\theta_2 \;\Longrightarrow\; "
            r"\theta_2 = \arcsin\!\left(\frac{n_1}{n_2}\sin\theta_1\right)",
            color=INK, font_size=28,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(cap0), Write(payoff), run_time=1.2)
        self.wait(3.0)
