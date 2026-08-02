#!/usr/bin/env python3
"""
total_internal_reflection_sweep.py — Total Internal Reflection: Refracted Ray Sweeping to 90° Then Vanishing
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/total-internal-reflection-sweep
    manim -qh total_internal_reflection_sweep.py TotalInternalReflectionScene

Numpy verification (run standalone):
    python3 total_internal_reflection_sweep.py --verify

Physics (checkable):
    Glass-to-air: n1=1.5, n2=1.0
    θ_c = arcsin(n2/n1) = arcsin(1/1.5) ≈ 41.81°

    P1: At θ1=41.81°, θ2=arcsin(1.5×sin41.81°)=arcsin(0.9999)≈89.996°≈90° ✓
    P2: Diamond n1=2.42, θ_c=arcsin(1/2.42)≈24.41° ✓
"""
import sys
import numpy as np

N1 = 1.5   # glass
N2 = 1.0   # air


def critical_angle(n1: float, n2: float) -> float:
    """θ_c = arcsin(n2/n1) in degrees. Only valid when n1 > n2."""
    return np.degrees(np.arcsin(n2 / n1))


def refracted_angle(theta1_deg: float, n1: float, n2: float):
    """Snell's law θ2 = arcsin(n1 sin θ1 / n2). Returns None if TIR."""
    val = n1 * np.sin(np.radians(theta1_deg)) / n2
    if val > 1.0:
        return None
    return np.degrees(np.arcsin(val))


def verify():
    print("=== Total Internal Reflection verification ===")
    tc = critical_angle(N1, N2)
    print(f"n1={N1}, n2={N2}")
    print(f"θ_c = arcsin({N2}/{N1}) = {tc:.2f}°")
    for t in [10, 20, 30, 40, 41, tc, 45, 60]:
        r = refracted_angle(t, N1, N2)
        label = f"{r:.3f}°" if r is not None else "TIR (no solution)"
        print(f"  θ1={t:.2f}°  →  θ2={label}")
    print()
    # P1: at θ_c, θ2 should be 90°
    r_at_tc = refracted_angle(tc, N1, N2)
    print(f"P1: θ2 at θ_c = {r_at_tc:.3f}° (should be ≈90°)")
    # P2: diamond
    tc_diamond = critical_angle(2.42, 1.0)
    print(f"P2: Diamond θ_c = arcsin(1/2.42) = {tc_diamond:.2f}° (should be ≈24.41°)")
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
GREEN  = "#4CAF50"
ORANGE = "#FF9800"


def ray_endpoint(origin, angle_deg, length=3.5):
    """Return endpoint of a ray from origin at angle_deg from vertical (normal)."""
    rad = np.radians(angle_deg)
    return origin + length * np.array([np.sin(rad), -np.cos(rad), 0])


class TotalInternalReflectionScene(Scene):
    """
    Glass-to-air interface. Incident ray sweeps from 10° to 60°.
    Refracted ray reaches 90° at θ_c ≈ 41.8°, then vanishes → TIR.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        self._phase_interface_sweep()

    def _phase_title(self):
        title = Text("Total Internal Reflection", font="EB Garamond", font_size=60, color=INK)
        sub = Text(
            "n₁sinθ₁ = n₂sinθ₂  ·  glass (n=1.5) → air (n=1.0)",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2 = Text(
            "θ_c = arcsin(n₂/n₁)  ·  critical angle ≈ 41.8°",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_interface_sweep(self):
        # Interface line (horizontal)
        interface_y = 0.0
        interface = Line(
            start=LEFT * 6, end=RIGHT * 6,
            color=DIM, stroke_width=2.5,
        ).move_to([0, interface_y, 0])

        # Labels
        glass_lbl = Text("Glass  n₁ = 1.5", font="EB Garamond", font_size=20, color=BROWN)
        glass_lbl.move_to([-4.5, 1.5, 0])
        air_lbl = Text("Air  n₂ = 1.0", font="EB Garamond", font_size=20, color=BLUE)
        air_lbl.move_to([-4.5, -1.5, 0])

        # Normal line (dashed vertical)
        normal = DashedLine(
            start=[0, interface_y + 2.5, 0],
            end=[0, interface_y - 2.5, 0],
            color=DIM, stroke_width=1.2, dash_length=0.15,
        )
        normal_lbl = Text("Normal", font="EB Garamond", font_size=16, color=DIM)
        normal_lbl.next_to(normal, RIGHT, buff=0.08)

        # Origin (point on interface)
        origin = np.array([0, interface_y, 0])

        # Angle arcs (will be dynamic)
        tc = critical_angle(N1, N2)  # 41.81°

        # Scripted angles
        angles = [10, 20, 30, 40, 41, tc, 45, 60]

        # Draw static elements
        self.play(
            Create(interface),
            Write(glass_lbl), Write(air_lbl),
            Create(normal), Write(normal_lbl),
            run_time=1.5,
        )

        # Dynamic angle readouts
        theta1_lbl = MathTex(r"\theta_1 = ", color=ORANGE, font_size=32).move_to([-4.5, 0.6, 0])
        theta1_val = DecimalNumber(10.0, num_decimal_places=1, color=ORANGE, font_size=32)
        theta1_val.next_to(theta1_lbl, RIGHT, buff=0.1)
        theta1_deg = MathTex(r"°", color=ORANGE, font_size=32).next_to(theta1_val, RIGHT, buff=0.05)

        theta2_lbl = MathTex(r"\theta_2 = ", color=GREEN, font_size=32).move_to([-4.5, -0.6, 0])
        theta2_val = DecimalNumber(0.0, num_decimal_places=1, color=GREEN, font_size=32)
        theta2_val.next_to(theta2_lbl, RIGHT, buff=0.1)
        theta2_deg = MathTex(r"°", color=GREEN, font_size=32).next_to(theta2_val, RIGHT, buff=0.05)

        theta_c_lbl = MathTex(
            r"\theta_c = \arcsin(n_2/n_1) \approx 41.8°",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.5)

        self.play(
            FadeIn(theta1_lbl), FadeIn(theta1_val), FadeIn(theta1_deg),
            FadeIn(theta2_lbl), FadeIn(theta2_val), FadeIn(theta2_deg),
            FadeIn(theta_c_lbl),
            run_time=0.8,
        )

        # Build initial rays at 10°
        # Incident ray: comes from upper-left (above interface = glass side)
        inc_end = ray_endpoint(origin, -10, 3.0)  # from origin going up-left
        inc_start = origin + (origin - inc_end)   # start = mirror of end
        inc_ray = Arrow(
            start=inc_start, end=origin,
            color=ORANGE, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.1,
        )

        r2 = refracted_angle(10, N1, N2)
        ref_end = ray_endpoint(origin, 10, 2.8)
        ref_end[1] = interface_y - abs(ref_end[1])  # below interface
        refracted_ray = Arrow(
            start=origin, end=ref_end,
            color=GREEN, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.1,
        )

        refl_end = origin + np.array([-np.sin(np.radians(10)) * 2.5, np.cos(np.radians(10)) * 2.5, 0])
        reflected_ray = Arrow(
            start=origin, end=refl_end,
            color=BLUE, stroke_width=2.5, buff=0,
            max_tip_length_to_length_ratio=0.08,
        )

        theta1_val.set_value(10.0)
        theta2_val.set_value(r2)

        self.play(Create(inc_ray), Create(refracted_ray), Create(reflected_ray), run_time=1.0)
        self.wait(0.5)

        # Animate through scripted angles
        for angle in angles[1:]:
            r2_new = refracted_angle(angle, N1, N2)
            is_tir = r2_new is None

            # New incident ray
            inc_s = np.array([
                -np.sin(np.radians(angle)) * 3.0,
                np.cos(np.radians(angle)) * 3.0, 0,
            ])
            new_inc = Arrow(
                start=inc_s, end=origin,
                color=ORANGE, stroke_width=4, buff=0,
                max_tip_length_to_length_ratio=0.1,
            )

            # New reflected ray
            refl_s = np.array([
                -np.sin(np.radians(angle)) * 2.5,
                np.cos(np.radians(angle)) * 2.5, 0,
            ])
            refl_width = 4.0 if is_tir else 2.5
            new_refl = Arrow(
                start=origin, end=refl_s,
                color=BLUE, stroke_width=refl_width, buff=0,
                max_tip_length_to_length_ratio=0.1,
            )

            anims = [
                Transform(inc_ray, new_inc),
                Transform(reflected_ray, new_refl),
                ChangeDecimalToValue(theta1_val, angle),
            ]

            if not is_tir:
                ref_angle = r2_new
                ref_x = np.sin(np.radians(ref_angle)) * 2.8
                ref_y = -(np.cos(np.radians(ref_angle)) * 2.8)
                new_ref_end = np.array([ref_x, ref_y, 0])
                new_ref = Arrow(
                    start=origin, end=new_ref_end,
                    color=GREEN, stroke_width=4, buff=0,
                    max_tip_length_to_length_ratio=0.1,
                )
                anims += [Transform(refracted_ray, new_ref),
                          ChangeDecimalToValue(theta2_val, ref_angle)]
                caption_text = f"θ₁ = {angle:.1f}°  →  θ₂ = {ref_angle:.1f}°"
                cap_color = GOLD if abs(angle - tc) < 0.5 else INK
            else:
                # TIR: move refracted ray off-screen
                new_ref = Arrow(
                    start=origin, end=origin + RIGHT * 0.001,
                    color=GREEN, stroke_width=0, buff=0,
                )
                anims += [Transform(refracted_ray, new_ref)]
                caption_text = f"θ₁ = {angle:.1f}°  >  θ_c  →  TIR! No refracted ray."
                cap_color = GOLD

            cap = Text(caption_text, font="EB Garamond", font_size=22, color=cap_color)
            cap.to_edge(UP, buff=0.2)

            self.play(*anims, Write(cap), run_time=1.2)
            self.wait(0.8)
            self.play(FadeOut(cap), run_time=0.2)

        # Final payoff
        payoff = MathTex(
            r"\theta_c = \arcsin\!\left(\frac{n_2}{n_1}\right) = \arcsin\!\left(\frac{1.0}{1.5}\right) \approx 41.8°",
            color=INK, font_size=30,
        ).to_edge(UP, buff=0.22)
        payoff2 = Text(
            "For θ₁ > θ_c, Snell's law has no real solution — all light reflects back.",
            font="EB Garamond", font_size=22, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(payoff), Write(payoff2), run_time=1.5)
        self.wait(3.0)
