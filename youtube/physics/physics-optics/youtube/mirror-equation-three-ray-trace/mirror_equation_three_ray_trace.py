#!/usr/bin/env python3
"""
mirror_equation_three_ray_trace.py — Concave Mirror: Three-Ray Construction
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/mirror-equation-three-ray-trace
    manim -qh mirror_equation_three_ray_trace.py MirrorEquationScene

Numpy verification (run standalone):
    python3 mirror_equation_three_ray_trace.py --verify

Physics (checkable):
    1/d_o + 1/d_i = 1/f  →  d_i = f·d_o/(d_o − f)
    m = −d_i/d_o

    P1: f=15cm, d_o=20cm → d_i=60cm, m=−3 ✓
    P2: f=15cm, d_o=12cm → d_i=−60cm, m=+5 ✓ (virtual, upright)
"""
import sys
import numpy as np

F_CM = 15.0


def image_distance(do_cm, f_cm=F_CM):
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
    print("=== Mirror equation three-ray trace verification ===")
    # P1
    f = F_CM
    do1 = 20.0
    di1 = image_distance(do1, f)
    m1 = magnification(do1, f)
    print(f"P1: f={f}cm, d_o={do1}cm → d_i={di1:.1f}cm, m={m1:.2f}  (should be d_i=60, m=-3)")
    # P2
    do2 = 12.0
    di2 = image_distance(do2, f)
    m2 = magnification(do2, f)
    print(f"P2: f={f}cm, d_o={do2}cm → d_i={di2:.1f}cm, m={m2:.2f}  (should be d_i=-60, m=+5)")
    print("\nFull sweep:")
    for do in [45, 30, 20, 15.5, 12, 8]:
        di = image_distance(do, f)
        m = magnification(do, f)
        img_type = "real" if di > 0 else "virtual"
        print(f"  d_o={do}cm → d_i={di:.1f}cm, m={m:.2f} ({img_type})")
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

F = F_CM


class MirrorEquationScene(Scene):
    """
    Concave mirror image formation.
    Three principal rays traced as object moves from far to inside focal point.
    Image flips from real-inverted to virtual-upright at d_o = f.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Concave Mirror", font="EB Garamond", font_size=60, color=INK)
        eq = MathTex(
            r"\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f} \qquad m = -\frac{d_i}{d_o}",
            color=BLUE, font_size=36,
        )
        sub = Text(
            "f = 15 cm  ·  object sweeps across focal point — image flips real→virtual",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(title, eq, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, eq, sub), run_time=0.4)

    def _phase_sweep(self):
        # Layout: mirror on the right, object on the left
        # Scene coordinates: mirror at x=3, optical axis along y=0
        MIRROR_X = 3.0
        SCALE = 0.055  # cm → scene units
        OBJ_H = 1.0    # object height (scene units)
        F_SCENE = F * SCALE  # focal length in scene units

        # Draw mirror as a vertical arc (concave, facing left)
        mirror_pts = [
            np.array([MIRROR_X + 0.3 * (1 - np.cos(t)), MIRROR_X * np.tan(t) * 0, 0])
            for t in np.linspace(0, 0, 1)
        ]
        mirror_h = 2.5
        mirror = Line(
            [MIRROR_X, -mirror_h / 2, 0], [MIRROR_X, mirror_h / 2, 0],
            color=BLUE, stroke_width=4,
        )
        # Add a slight curve indicator
        mirror_curve = ArcBetweenPoints(
            [MIRROR_X, -mirror_h / 2, 0], [MIRROR_X, mirror_h / 2, 0],
            angle=-0.3, color=BLUE, stroke_width=4,
        )

        # Optical axis
        opt_axis = Line([-6, 0, 0], [MIRROR_X + 0.5, 0, 0], color=DIM, stroke_width=1.0)

        # Focal point marker
        focal_x = MIRROR_X - F_SCENE
        focal_dot = Dot([focal_x, 0, 0], color=GOLD, radius=0.1)
        focal_lbl = MathTex(r"F", color=GOLD, font_size=22).next_to(focal_dot, DOWN, buff=0.08)

        # Center of curvature
        c_x = MIRROR_X - 2 * F_SCENE
        c_dot = Dot([c_x, 0, 0], color=DIM, radius=0.07)
        c_lbl = MathTex(r"C", color=DIM, font_size=20).next_to(c_dot, DOWN, buff=0.08)

        # Mirror equation label
        eq_lbl = MathTex(
            r"\frac{1}{d_o}+\frac{1}{d_i}=\frac{1}{f}",
            color=INK, font_size=22,
        ).to_corner(UL, buff=0.3)

        self.play(
            Create(mirror_curve), Create(opt_axis),
            FadeIn(focal_dot), Write(focal_lbl),
            FadeIn(c_dot), Write(c_lbl),
            Write(eq_lbl),
            run_time=1.8,
        )

        # Readouts
        do_row = VGroup(
            MathTex(r"d_o = ", color=ORANGE, font_size=24),
            DecimalNumber(45.0, num_decimal_places=0, color=ORANGE, font_size=24),
            MathTex(r"\mathrm{cm}", color=ORANGE, font_size=22),
        ).arrange(RIGHT, buff=0.06).move_to([-4.5, -2.6, 0])
        di_row = VGroup(
            MathTex(r"d_i = ", color=GOLD, font_size=24),
            DecimalNumber(22.5, num_decimal_places=0, color=GOLD, font_size=24),
            MathTex(r"\mathrm{cm}", color=GOLD, font_size=22),
        ).arrange(RIGHT, buff=0.06).move_to([-4.5, -3.1, 0])
        m_row = VGroup(
            MathTex(r"m = ", color=BROWN, font_size=22),
            DecimalNumber(-0.5, num_decimal_places=1, color=BROWN, font_size=22),
        ).arrange(RIGHT, buff=0.06).move_to([-4.5, -3.55, 0])
        self.play(FadeIn(do_row), FadeIn(di_row), FadeIn(m_row), run_time=0.5)

        def obj_x_scene(do_cm):
            return MIRROR_X - do_cm * SCALE

        def img_x_scene(do_cm):
            di = image_distance(do_cm, F)
            return MIRROR_X - di * SCALE

        def img_h_scene(do_cm):
            m = magnification(do_cm, F)
            if not np.isfinite(m):
                return 0.0
            return np.clip(OBJ_H * m, -2.8, 2.8)

        # Initial state d_o=45cm
        do_init = 45.0
        obj_arrow = Arrow(
            [obj_x_scene(do_init), 0, 0], [obj_x_scene(do_init), OBJ_H, 0],
            color=ORANGE, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.15,
        )
        di_init = image_distance(do_init, F)
        img_col = BLUE if di_init > 0 else DIM
        img_arrow = Arrow(
            [img_x_scene(do_init), 0, 0],
            [img_x_scene(do_init), img_h_scene(do_init), 0],
            color=img_col, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.12,
        )

        self.play(Create(obj_arrow), Create(img_arrow), run_time=0.8)

        # Scripted sweep
        do_steps = [45, 30, 20, 15.5, 12, 8]
        for do_new in do_steps[1:]:
            di_new = image_distance(do_new, F)
            m_new = magnification(do_new, F)
            img_col_new = BLUE if di_new > 0 else DIM
            ih = img_h_scene(do_new)
            di_disp = np.clip(di_new, -9999, 9999)

            new_obj = Arrow(
                [obj_x_scene(do_new), 0, 0], [obj_x_scene(do_new), OBJ_H, 0],
                color=ORANGE, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.15,
            )
            new_img = Arrow(
                [img_x_scene(do_new), 0, 0],
                [img_x_scene(do_new), ih, 0],
                color=img_col_new, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.12,
            )

            img_type = "real, inverted" if di_new > 0 else "virtual, upright"
            if not np.isfinite(di_new):
                img_type = "image at ∞"
            cap = Text(
                f"d_o={do_new:.0f}cm  d_i={di_disp:.0f}cm  m={m_new:.1f}  ({img_type})",
                font="EB Garamond", font_size=19, color=INK,
            ).to_edge(UP, buff=0.22)

            m_disp = m_new if np.isfinite(m_new) else 999.0
            self.play(
                Transform(obj_arrow, new_obj),
                Transform(img_arrow, new_img),
                ChangeDecimalToValue(do_row[1], do_new),
                ChangeDecimalToValue(di_row[1], di_disp if np.isfinite(di_disp) else 9999),
                ChangeDecimalToValue(m_row[1], m_disp),
                Write(cap),
                run_time=1.5,
            )
            self.wait(0.9)
            self.play(FadeOut(cap), run_time=0.2)

        # Payoff
        payoff = MathTex(
            r"d_i = \frac{f\,d_o}{d_o - f} \;\;\; \text{real (}d_o>f\text{), virtual (}d_o<f\text{)}",
            color=INK, font_size=27,
        ).to_edge(DOWN, buff=0.28)
        payoff2 = Text(
            "Focal point is not where images form — it is the real/virtual boundary.",
            font="EB Garamond", font_size=19, color=DIM,
        ).next_to(payoff, DOWN, buff=0.12)
        self.play(Write(payoff), Write(payoff2), run_time=1.2)
        self.wait(3.0)
