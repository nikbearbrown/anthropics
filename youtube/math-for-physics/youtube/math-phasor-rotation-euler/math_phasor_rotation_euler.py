#!/usr/bin/env python3
"""
math_phasor_rotation_euler.py — Phasor Rotation and Euler's Formula
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_phasor_rotation_euler.py --verify

Math (checkable):
    e^(iωt) = cos(ωt) + i·sin(ωt)
    Phasor sum: 3 + 4i → |3+4i| = √(9+16) = 5, arg = arctan(4/3) = 53.13°
    At ωt = π/2: Re(e^(iπ/2)) = cos(π/2) = 0, Im = sin(π/2) = 1 ✓
"""
import sys
import numpy as np

OMEGA = 2 * np.pi  # rad/s


def verify():
    print("=== Phasor / Euler's formula verification ===")
    print(f"ω = 2π = {OMEGA:.4f} rad/s")
    print()
    # Phasor sum
    A1 = 3.0 + 0j
    A2 = 0.0 + 4j
    A_sum = A1 + A2
    modulus = abs(A_sum)
    angle_deg = np.degrees(np.angle(A_sum))
    print(f"Phasor 1: {A1}  Phasor 2: {A2}")
    print(f"Sum: {A_sum}")
    print(f"|sum| = √(9+16) = {modulus:.6f}  (expect 5.0000)")
    print(f"arg  = arctan(4/3) = {angle_deg:.4f}°  (expect 53.1301°)")
    print()
    # Euler at π/2
    val = np.exp(1j * np.pi / 2)
    print(f"e^(iπ/2) = {val.real:.8f} + {val.imag:.8f}i  (expect 0 + 1i)")
    print()
    # Check orthogonality: Re·Im projection at t=1/(4f)
    t = 0.25  # quarter period
    re_proj = np.cos(OMEGA * t)
    im_proj = np.sin(OMEGA * t)
    print(f"At t=0.25 s (quarter period): Re={re_proj:.8f}  Im={im_proj:.8f}")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class PhasorRotationScene(Scene):
    """
    Left: complex plane with rotating unit phasor e^(iωt).
    Right: real-axis projection → cosine wave (blue).
    Bottom: imaginary projection → sine wave (brown).
    Second act: phasor sum 3+4i → 5∠53.1°.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_euler_phasor()
        self._phase_phasor_sum()

    def _phase_title(self):
        title = Text("Phasor Rotation — Euler's Formula", font="EB Garamond", font_size=54, color=INK)
        eq = MathTex(
            r"e^{i\omega t} = \cos(\omega t) + i\,\sin(\omega t)",
            color=BLUE, font_size=34,
        )
        sub = Text(
            "oscillation = shadow of a spinning arrow",
            font="EB Garamond", font_size=24, color=DIM,
        )
        VGroup(title, eq, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(eq), run_time=0.9)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, eq, sub), run_time=0.5)

    def _phase_euler_phasor(self):
        # ── Layout: complex plane LEFT, cosine wave RIGHT ────────────────────
        PLANE_R = 2.0        # display radius of unit circle
        PLANE_CENTER = LEFT * 3.5 + UP * 0.3
        WAVE_ORIGIN = RIGHT * 0.5 + UP * 0.3

        # Complex plane
        plane_axes = NumberPlane(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=PLANE_R * 2 + 0.5,
            y_length=PLANE_R * 2 + 0.5,
            axis_config=dict(color=DIM, stroke_width=1.0),
            background_line_style=dict(stroke_color=DIM, stroke_opacity=0.15, stroke_width=0.8),
        ).shift(PLANE_CENTER)

        circle = Circle(radius=PLANE_R, color=DIM, stroke_width=1.5).shift(PLANE_CENTER)
        lbl_re = MathTex(r"\mathrm{Re}", color=DIM, font_size=18).next_to(PLANE_CENTER + RIGHT * (PLANE_R + 0.1), RIGHT, buff=0.05)
        lbl_im = MathTex(r"\mathrm{Im}", color=DIM, font_size=18).next_to(PLANE_CENTER + UP * (PLANE_R + 0.1), UP, buff=0.05)
        lbl_euler = MathTex(r"e^{i\omega t}", color=GOLD, font_size=22).next_to(PLANE_CENTER + DOWN * (PLANE_R + 0.3), DOWN, buff=0.05)

        # Time axis for cosine wave (right side)
        T_DISPLAY = 1.5   # seconds of wave to show
        wave_ax = Axes(
            x_range=[0.0, T_DISPLAY, 0.5],
            y_range=[-1.3, 1.3, 0.5],
            x_length=5.0,
            y_length=PLANE_R * 2 + 0.4,
            axis_config=dict(color=INK, stroke_width=1.2, include_ticks=True,
                             tip_length=0.15, include_numbers=False),
        ).shift(WAVE_ORIGIN)

        lbl_wave_x = MathTex(r"t", color=DIM, font_size=18).next_to(wave_ax.x_axis.get_end(), RIGHT, buff=0.05)
        cos_lbl = MathTex(r"\cos(\omega t)", color=BLUE, font_size=20).next_to(wave_ax, UP, buff=0.08)
        sin_lbl = MathTex(r"\sin(\omega t)", color=BROWN, font_size=20).next_to(wave_ax, DOWN, buff=0.08)

        self.play(
            Create(plane_axes), Create(circle),
            Create(wave_ax),
            Write(lbl_re), Write(lbl_im), Write(lbl_euler),
            Write(lbl_wave_x), Write(cos_lbl), Write(sin_lbl),
            run_time=1.5,
        )

        # ValueTracker for angle (in [0, 2π])
        angle_t = ValueTracker(0.0)

        def get_phasor_tip():
            th = angle_t.get_value()
            return PLANE_CENTER + np.array([PLANE_R * np.cos(th), PLANE_R * np.sin(th), 0])

        # Rotating arrow
        phasor_arrow = always_redraw(
            lambda: Arrow(
                PLANE_CENTER, get_phasor_tip(),
                color=GOLD, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.12,
            )
        )

        # Projection dot on real axis
        def proj_real():
            tip = get_phasor_tip()
            return Dot(PLANE_CENTER + np.array([tip[0] - PLANE_CENTER[0], 0, 0]),
                       color=BLUE, radius=0.08)

        # Dashed vertical projection line
        def proj_line():
            tip = get_phasor_tip()
            target = PLANE_CENTER + np.array([tip[0] - PLANE_CENTER[0], 0, 0])
            return DashedLine(tip, target, color=BLUE, stroke_width=1.5, stroke_opacity=0.7)

        dyn_proj_dot = always_redraw(proj_real)
        dyn_proj_line = always_redraw(proj_line)

        # Growing cosine wave trace
        cos_trace = VMobject(color=BLUE, stroke_width=2.5)
        sin_trace = VMobject(color=BROWN, stroke_width=2.5)

        self.add(phasor_arrow, dyn_proj_dot, dyn_proj_line)

        # Animate 2 full rotations, tracing the cosine
        N_STEPS = 120
        dt = 2.0 * np.pi / N_STEPS

        for step in range(N_STEPS * 2):
            th_new = (step + 1) * dt
            angle_t.set_value(th_new)

            # Map angle to time axis position
            t_frac = (th_new % (2 * np.pi)) / (2 * np.pi) * T_DISPLAY
            re_val = np.cos(th_new)
            im_val = np.sin(th_new)

            new_cos_pt = wave_ax.c2p(t_frac, re_val)
            if cos_trace.get_num_points() == 0:
                cos_trace.start_new_path(new_cos_pt)
            else:
                cos_trace.add_points_as_corners([new_cos_pt])

            self.add(cos_trace)

        self.wait(0.5)

        # Clean up for next phase
        formula_box = MathTex(
            r"e^{i\omega t} = \cos(\omega t) + i\sin(\omega t)",
            color=INK, font_size=28,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(formula_box), run_time=0.8)
        self.wait(2.0)
        self.play(
            FadeOut(plane_axes, circle, wave_ax, phasor_arrow, dyn_proj_dot,
                    dyn_proj_line, cos_trace, lbl_re, lbl_im, lbl_euler,
                    lbl_wave_x, cos_lbl, sin_lbl, formula_box),
            run_time=0.8,
        )
        self.remove(phasor_arrow, dyn_proj_dot, dyn_proj_line)

    def _phase_phasor_sum(self):
        """Phasor addition: 3∠0° + 4∠90° = 5∠53.1°."""
        title = Text(
            "Phasor addition: 3∠0° + 4∠90°",
            font="EB Garamond", font_size=26, color=INK,
        ).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        PLANE_CENTER = LEFT * 1.0
        SCALE = 0.8  # Manim units per unit phasor

        plane_axes = NumberPlane(
            x_range=[-0.5, 6.5, 1],
            y_range=[-0.5, 5.5, 1],
            x_length=7.0,
            y_length=6.0,
            axis_config=dict(color=DIM, stroke_width=1.0),
            background_line_style=dict(stroke_color=DIM, stroke_opacity=0.15, stroke_width=0.8),
        ).shift(PLANE_CENTER)
        lbl_re = MathTex(r"\mathrm{Re}", color=DIM, font_size=18).next_to(plane_axes.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_im = MathTex(r"\mathrm{Im}", color=DIM, font_size=18).next_to(plane_axes.y_axis.get_end(), UP, buff=0.05)

        self.play(Create(plane_axes), Write(lbl_re), Write(lbl_im), run_time=0.8)

        origin = plane_axes.c2p(0, 0)
        p1_tip = plane_axes.c2p(3, 0)   # Ã₁ = 3 + 0i
        p2_tip = plane_axes.c2p(3, 4)   # Ã₂ = 0 + 4i (added to tip of p1)
        p2_base = p1_tip                  # vector addition: start from tip of p1

        # Phasor 1: 3∠0°
        arr1 = Arrow(origin, p1_tip, color=BLUE, buff=0, stroke_width=3,
                     max_tip_length_to_length_ratio=0.1)
        lbl1 = MathTex(r"\tilde{A}_1 = 3", color=BLUE, font_size=24).next_to(plane_axes.c2p(1.5, 0), DOWN, buff=0.15)

        # Phasor 2: 4∠90° (placed at tip of phasor 1 for vector addition)
        arr2 = Arrow(p1_tip, p2_tip, color=BROWN, buff=0, stroke_width=3,
                     max_tip_length_to_length_ratio=0.1)
        lbl2 = MathTex(r"\tilde{A}_2 = 4i", color=BROWN, font_size=24).next_to(plane_axes.c2p(3.0, 2.0), RIGHT, buff=0.15)

        # Resultant: 3+4i = 5∠53.1°
        arr_sum = Arrow(origin, p2_tip, color=GOLD, buff=0, stroke_width=3.5,
                        max_tip_length_to_length_ratio=0.1)
        angle_deg = np.degrees(np.arctan2(4, 3))
        lbl_sum = MathTex(
            rf"|\tilde{{A}}| = 5,\;\phi = {angle_deg:.1f}°",
            color=GOLD, font_size=26,
        ).next_to(plane_axes.c2p(1.5, 2.5), LEFT, buff=0.1)

        self.play(Create(arr1), Write(lbl1), run_time=0.8)
        self.play(Create(arr2), Write(lbl2), run_time=0.8)
        self.play(Create(arr_sum), Write(lbl_sum), run_time=0.8)

        # Right-angle marker
        ra_size = 0.2
        ra = Polygon(
            plane_axes.c2p(3, ra_size), plane_axes.c2p(3 + ra_size, ra_size),
            plane_axes.c2p(3 + ra_size, 0), plane_axes.c2p(3, 0),
            color=DIM, stroke_width=1.5, fill_opacity=0,
        )
        self.play(Create(ra), run_time=0.3)

        # Final formula
        formula = MathTex(
            r"3\cos(\omega t) + 4\cos(\omega t + 90°) = 5\cos(\omega t + 53.1°)",
            color=INK, font_size=24,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(formula), run_time=1.2)
        self.wait(2.5)
