#!/usr/bin/env python3
"""
thin_lens_image_position_sweep.py — Thin Lens: Image Position Tracing Reciprocal Curve
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/thin-lens-image-position-sweep
    manim -qh thin_lens_image_position_sweep.py ThinLensImagePositionScene

Numpy verification (run standalone):
    python3 thin_lens_image_position_sweep.py --verify

Physics (checkable):
    1/d_o + 1/d_i = 1/f  →  d_i = f·d_o / (d_o − f)
    Magnification m = −d_i / d_o

    P1: f=10cm, d_o=20cm → d_i=20cm, m=−1 ✓
    P2: f=10cm, d_o=8cm  → d_i=−40cm, m=+5 ✓
"""
import sys
import numpy as np

F_CM = 20.0   # cm, converging lens focal length (matching task spec)


def image_distance(do_cm, f_cm=F_CM):
    """d_i = f·d_o/(d_o − f). Returns inf at d_o=f."""
    denom = do_cm - f_cm
    if abs(denom) < 1e-8:
        return float('inf')
    return f_cm * do_cm / denom


def magnification(do_cm, f_cm=F_CM):
    di = image_distance(do_cm, f_cm)
    if not np.isfinite(di):
        return float('inf')
    return -di / do_cm


def verify():
    print("=== Thin-lens image position verification ===")
    print(f"f = {F_CM} cm")
    # Use f=10cm for P1/P2 as per card spec
    f = 10.0
    # P1
    do1 = 20.0
    di1 = f * do1 / (do1 - f)
    m1 = -di1 / do1
    print(f"P1: d_o={do1}cm → d_i={di1:.1f}cm, m={m1:.2f}  (should be d_i=20, m=-1)")
    # P2
    do2 = 8.0
    di2 = f * do2 / (do2 - f)
    m2 = -di2 / do2
    print(f"P2: d_o={do2}cm → d_i={di2:.1f}cm, m={m2:.2f}  (should be d_i=-40, m=+5)")
    # Scene values with F=20cm
    print(f"\nScene values (f={F_CM}cm):")
    for do in [25, 40, 60, 100, 200]:
        di = image_distance(do, F_CM)
        m = magnification(do, F_CM)
        print(f"  d_o={do}cm → d_i={di:.1f}cm, m={m:.2f}")
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

F = F_CM  # cm


class ThinLensImagePositionScene(Scene):
    """
    Thin-lens equation: 1/d_o + 1/d_i = 1/f.
    Left panel: object+lens+image geometry.
    Right panel: d_i vs d_o hyperbola.
    Object sweeps from far to near focal point.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_dual_panel()

    def _phase_title(self):
        title = Text("Thin-Lens Equation", font="EB Garamond", font_size=60, color=INK)
        eq = MathTex(
            r"\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}",
            color=BLUE, font_size=40,
        )
        sub = Text(
            "f = 20 cm  ·  object sweeps from far to focal length  — image traces a hyperbola",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(title, eq, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(eq), run_time=0.9)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, eq, sub), run_time=0.4)

    def _phase_dual_panel(self):
        # ── Right panel: d_i vs d_o plot ─────────────────────────────────────
        ax = Axes(
            x_range=[20, 220, 40],
            y_range=[-20, 200, 40],
            x_length=5.8,
            y_length=5.8,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.12),
            x_axis_config=dict(numbers_to_include=[40, 80, 120, 160, 200]),
            y_axis_config=dict(numbers_to_include=[0, 40, 80, 120, 160]),
        ).shift(RIGHT * 3.2 + DOWN * 0.2)

        lbl_ax = MathTex(r"d_o\;(\mathrm{cm})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_ay = MathTex(r"d_i\;(\mathrm{cm})", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.05)
        hdr_r = Text("d_i vs d_o", font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.08)

        # Hyperbola trace (d_o from 22 to 200 cm)
        do_range = np.linspace(22, 210, 600)
        di_range = np.array([image_distance(do, F) for do in do_range])
        # Only real visible part
        mask = (di_range > -25) & (di_range < 210)
        do_vis = do_range[mask]
        di_vis = di_range[mask]
        hyp_pts = [ax.c2p(do, di) for do, di in zip(do_vis, di_vis)]
        hyp_curve = VMobject(color=GOLD, stroke_width=2.5)
        hyp_curve.set_points_smoothly(hyp_pts)

        # Asymptote at d_o = f
        asym = DashedLine(
            ax.c2p(F, -25), ax.c2p(F, 200),
            color=DIM, stroke_width=1.2, dash_length=0.12,
        )
        asym_lbl = MathTex(r"d_o = f", color=DIM, font_size=18).next_to(ax.c2p(F, 180), RIGHT, buff=0.05)

        self.play(
            Create(ax), Write(lbl_ax), Write(lbl_ay), Write(hdr_r),
            Create(hyp_curve), Create(asym), Write(asym_lbl),
            run_time=2.0,
        )

        # ── Left panel: optical geometry ─────────────────────────────────────
        # Simple: lens as vertical line at x=0, object on left, image on right
        SCALE = 0.035  # cm → scene units
        lens_x_scene = -2.2
        LENS_H = 2.8

        lens_line = Line(
            [lens_x_scene, -LENS_H / 2, 0],
            [lens_x_scene, LENS_H / 2, 0],
            color=BLUE, stroke_width=3.5,
        )
        # Converging lens symbol (arrows)
        lens_arrow_top = Arrow(
            start=[lens_x_scene - 0.18, LENS_H / 2 - 0.02, 0],
            end=[lens_x_scene + 0.18, LENS_H / 2 - 0.02, 0],
            color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.3,
        )
        lens_arrow_bot = Arrow(
            start=[lens_x_scene + 0.18, -LENS_H / 2 + 0.02, 0],
            end=[lens_x_scene - 0.18, -LENS_H / 2 + 0.02, 0],
            color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.3,
        )
        lens_lbl = Text("f = 20 cm", font="EB Garamond", font_size=18, color=BLUE)
        lens_lbl.next_to(lens_line, UP, buff=0.1)

        # Optical axis
        opt_axis = Line(LEFT * 5.5 + [lens_x_scene, 0, 0], RIGHT * 2.5 + [lens_x_scene, 0, 0],
                        color=DIM, stroke_width=1.0)

        self.play(
            Create(lens_line), Create(lens_arrow_top), Create(lens_arrow_bot),
            Write(lens_lbl), Create(opt_axis),
            run_time=1.0,
        )

        # Readout labels
        do_row = VGroup(
            MathTex(r"d_o = ", color=ORANGE, font_size=26),
            DecimalNumber(200.0, num_decimal_places=0, color=ORANGE, font_size=26),
            MathTex(r"\mathrm{cm}", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.08).move_to([-5.0, -2.7, 0])

        di_row = VGroup(
            MathTex(r"d_i = ", color=GOLD, font_size=26),
            DecimalNumber(image_distance(200, F), num_decimal_places=0, color=GOLD, font_size=26),
            MathTex(r"\mathrm{cm}", color=GOLD, font_size=26),
        ).arrange(RIGHT, buff=0.08).move_to([-5.0, -3.2, 0])

        m_row = VGroup(
            MathTex(r"m = ", color=BROWN, font_size=24),
            DecimalNumber(magnification(200, F), num_decimal_places=2, color=BROWN, font_size=24),
        ).arrange(RIGHT, buff=0.08).move_to([-5.0, -3.65, 0])

        self.play(FadeIn(do_row), FadeIn(di_row), FadeIn(m_row), run_time=0.6)

        # Object arrow (left of lens)
        obj_h = 0.8  # height in scene units

        def object_x(do_cm):
            return lens_x_scene - do_cm * SCALE

        def image_x(do_cm):
            di = image_distance(do_cm, F)
            return lens_x_scene + di * SCALE

        def image_h(do_cm):
            m = magnification(do_cm, F)
            if not np.isfinite(m):
                return 0.0
            return np.clip(obj_h * m, -3.0, 3.0)

        # Dot tracer on hyperbola
        tracer_dot = Dot(ax.c2p(200, image_distance(200, F)), color=GOLD, radius=0.12)
        self.add(tracer_dot)

        # Initial object arrow
        do_init = 200.0
        obj_arr = Arrow(
            start=[object_x(do_init), 0, 0],
            end=[object_x(do_init), obj_h, 0],
            color=ORANGE, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.2,
        )
        di_init = image_distance(do_init, F)
        img_col_init = BLUE if di_init > 0 else DIM
        img_arr = Arrow(
            start=[image_x(do_init), 0, 0],
            end=[image_x(do_init), image_h(do_init), 0],
            color=img_col_init, stroke_width=3.5, buff=0,
            max_tip_length_to_length_ratio=0.2,
        )

        self.play(Create(obj_arr), Create(img_arr), run_time=0.8)

        # Scripted d_o sweep
        do_stops = [200, 100, 60, 40, 25.5]
        for do_new in do_stops[1:]:
            di_new = image_distance(do_new, F)
            m_new = magnification(do_new, F)
            img_col = BLUE if di_new > 0 else DIM
            di_disp = di_new if abs(di_new) < 9000 else 9999

            new_obj = Arrow(
                start=[object_x(do_new), 0, 0],
                end=[object_x(do_new), obj_h, 0],
                color=ORANGE, stroke_width=4, buff=0,
                max_tip_length_to_length_ratio=0.2,
            )
            ih = image_h(do_new)
            new_img = Arrow(
                start=[image_x(do_new), 0, 0],
                end=[image_x(do_new), ih, 0],
                color=img_col, stroke_width=3.5, buff=0,
                max_tip_length_to_length_ratio=0.2,
            )
            # Clamp dot to axis range
            dot_x = np.clip(do_new, 20, 210)
            dot_y = np.clip(di_new, -25, 210)
            new_dot = Dot(ax.c2p(dot_x, dot_y), color=GOLD, radius=0.12)

            img_type = "real, inverted" if di_new > 0 else "virtual, upright"
            cap = Text(
                f"d_o={do_new:.0f}cm  d_i={di_disp:.0f}cm  m={m_new:.2f}  ({img_type})",
                font="EB Garamond", font_size=19, color=INK,
            ).to_edge(UP, buff=0.22)

            self.play(
                Transform(obj_arr, new_obj),
                Transform(img_arr, new_img),
                Transform(tracer_dot, new_dot),
                ChangeDecimalToValue(do_row[1], do_new),
                ChangeDecimalToValue(di_row[1], di_disp),
                ChangeDecimalToValue(m_row[1], m_new if np.isfinite(m_new) else 999.0),
                Write(cap),
                run_time=1.5,
            )
            self.wait(0.9)
            self.play(FadeOut(cap), run_time=0.2)

        # Payoff
        payoff = MathTex(
            r"d_i = \frac{f\,d_o}{d_o - f} \;\;\;\text{— a hyperbola in } (d_o,\,d_i) \text{ space}",
            color=INK, font_size=28,
        ).to_edge(DOWN, buff=0.28)
        payoff2 = Text(
            "Singularity at d_o = f: image jumps to ∞ then re-appears as virtual",
            font="EB Garamond", font_size=19, color=DIM,
        ).next_to(payoff, DOWN, buff=0.15)
        self.play(Write(payoff), Write(payoff2), run_time=1.2)
        self.wait(3.0)
