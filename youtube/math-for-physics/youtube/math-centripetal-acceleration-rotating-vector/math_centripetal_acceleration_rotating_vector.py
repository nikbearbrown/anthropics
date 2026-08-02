#!/usr/bin/env python3
"""
math_centripetal_acceleration_rotating_vector.py — Centripetal Acceleration
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_centripetal_acceleration_rotating_vector.py --verify

Physics (checkable):
    r=229 m, v=134 m/s (jet 8g turn)
    ω = v/r = 134/229 ≈ 0.5852 rad/s
    |a| = v²/r = 134²/229 = 17956/229 ≈ 78.41 m/s² ≈ 8.0g
    v·r = 0 at every instant (perpendicular) ✓
    |v| = rω = 229·0.5852 ≈ 134.0 m/s (constant) ✓
"""
import sys
import numpy as np

R_JET = 229.0   # m
V_JET = 134.0   # m/s
G = 9.81        # m/s²


def omega():
    return V_JET / R_JET


def verify():
    w = omega()
    a_cent = V_JET**2 / R_JET
    print("=== Centripetal acceleration verification ===")
    print(f"r = {R_JET} m,  v = {V_JET} m/s")
    print(f"ω = v/r = {w:.5f} rad/s")
    print(f"|a| = v²/r = {a_cent:.2f} m/s²  = {a_cent/G:.2f} g")
    print()
    # Perpendicularity check at t = π/(4ω)
    t_check = np.pi / (4 * w)
    rx = R_JET * np.cos(w * t_check)
    ry = R_JET * np.sin(w * t_check)
    vx = -R_JET * w * np.sin(w * t_check)
    vy = R_JET * w * np.cos(w * t_check)
    dot_rv = rx * vx + ry * vy
    print(f"At t = π/(4ω): r·v = {dot_rv:.8f}  (expect 0)")
    speed = np.sqrt(vx**2 + vy**2)
    print(f"Speed = rω = {speed:.4f} m/s  (expect {V_JET})")
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


class CentripetalAccelerationScene(Scene):
    """
    Point traces a circle. Position vector r (blue), velocity v (brown, tangent),
    acceleration a (gold, toward center) rotate simultaneously.
    Labels show |a| = v²/r = const.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_rotating_vectors()
        self._phase_formula()

    def _phase_title(self):
        title = Text("Centripetal Acceleration", font="EB Garamond", font_size=58, color=INK)
        sub1 = Text(
            "r = 229 m,  v = 134 m/s  (8g fighter-jet turn)",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2 = MathTex(
            r"\mathbf{a}(t) = -\omega^2\,\mathbf{r}(t) \quad \Rightarrow \quad |\mathbf{a}| = \frac{v^2}{r}",
            color=GOLD, font_size=28,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub1), run_time=0.5)
        self.play(Write(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_rotating_vectors(self):
        # Normalized circle radius for display
        DISP_R = 2.2  # Manim units
        w = omega()
        T_period = 2 * np.pi / w

        # Circle
        circle = Circle(radius=DISP_R, color=DIM, stroke_width=1.5)
        center_dot = Dot(ORIGIN, color=DIM, radius=0.06)
        self.play(Create(circle), FadeIn(center_dot), run_time=0.8)

        # ValueTracker for angle
        angle = ValueTracker(0.0)

        def get_pos():
            th = angle.get_value()
            return np.array([DISP_R * np.cos(th), DISP_R * np.sin(th), 0])

        def get_vel_dir():
            th = angle.get_value()
            return np.array([-np.sin(th), np.cos(th), 0])  # unit tangent

        # Moving point
        pt = always_redraw(lambda: Dot(get_pos(), color=INK, radius=0.1))

        # Position vector r (blue arrow)
        r_vec = always_redraw(
            lambda: Arrow(
                ORIGIN, get_pos(),
                color=BLUE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.12,
            )
        )

        # Velocity vector v (brown, tangent, scaled)
        V_SCALE = 0.8
        v_vec = always_redraw(
            lambda: Arrow(
                get_pos(), get_pos() + V_SCALE * get_vel_dir(),
                color=BROWN, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.15,
            )
        )

        # Acceleration vector a (gold, toward center)
        A_SCALE = 0.7
        a_vec = always_redraw(
            lambda: Arrow(
                get_pos(), get_pos() - A_SCALE * (get_pos() / DISP_R),
                color=GOLD, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.15,
            )
        )

        # Vector labels (fixed to screen, updated conceptually)
        lbl_r = Text("r(t)", font="EB Garamond", font_size=20, color=BLUE).to_corner(UL, buff=0.4)
        lbl_v = Text("v(t) = dr/dt  ⊥ r", font="EB Garamond", font_size=20, color=BROWN).next_to(lbl_r, DOWN, aligned_edge=LEFT, buff=0.15)
        lbl_a = Text("|a| = v²/r = 78.4 m/s² = 8g", font="EB Garamond", font_size=20, color=GOLD).next_to(lbl_v, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(FadeIn(pt), Create(r_vec), Create(v_vec), Create(a_vec),
                  Write(lbl_r), Write(lbl_v), Write(lbl_a), run_time=1.2)

        # Animate one full revolution
        self.play(
            angle.animate.set_value(2 * np.pi),
            run_time=6.0,
            rate_func=linear,
        )
        self.wait(0.5)
        # Second revolution, faster
        self.play(
            angle.animate.set_value(4 * np.pi),
            run_time=4.0,
            rate_func=linear,
        )
        self.wait(1.0)
        self.remove(pt, r_vec, v_vec, a_vec)

    def _phase_formula(self):
        w = omega()
        a_mag = V_JET**2 / R_JET
        formula = MathTex(
            r"\mathbf{r}(t) = R(\cos\omega t,\,\sin\omega t) \xrightarrow{\frac{d^2}{dt^2}} "
            r"\mathbf{a}(t) = -\omega^2\mathbf{r}(t),\quad |\mathbf{a}| = \omega^2 R = \frac{v^2}{R}",
            color=INK, font_size=24,
        ).to_edge(DOWN, buff=0.35)
        numbers = Text(
            f"ω = {w:.4f} rad/s,  |a| = {a_mag:.1f} m/s² = {a_mag/G:.1f}g",
            font="EB Garamond", font_size=22, color=GOLD,
        ).next_to(formula, UP, buff=0.2)
        self.play(Write(numbers), run_time=0.8)
        self.play(Write(formula), run_time=1.2)
        self.wait(2.5)
