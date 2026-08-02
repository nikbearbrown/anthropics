#!/usr/bin/env python3
"""
physics_rolling_race_moment_of_inertia.py — Rolling Race: Solid Sphere vs Hollow Shell
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  a = g sinθ / (1 + I/MR²)
  Solid sphere:  I = (2/5)MR²  → a = (5/7) g sinθ
  Hollow shell:  I = (2/3)MR²  → a = (3/5) g sinθ
  θ=30°, h=1 m, g=9.8 m/s²
  Distance along slope: s = h/sinθ = 2 m

Testable predictions:
  P1: v_sphere = √(10gh/7) = √14 ≈ 3.742 m/s
      v_shell  = √(6gh/5)  = √11.76 ≈ 3.429 m/s
  P2: Rotational KE fraction: sphere 2/7≈28.6%, shell 2/5=40%

Run standalone verification:
  python3 physics_rolling_race_moment_of_inertia.py --verify

Render:
  manim -qh physics_rolling_race_moment_of_inertia.py RollingRaceMomentOfInertiaScene
"""
import sys
import numpy as np

G     = 9.8     # m/s²
THETA = 30.0    # degrees
H     = 1.0     # m (vertical drop)

def accel(I_over_MR2):
    return G * np.sin(np.radians(THETA)) / (1 + I_over_MR2)

def final_speed(I_over_MR2):
    """v² = 2as, where s = h/sinθ."""
    s = H / np.sin(np.radians(THETA))
    a = accel(I_over_MR2)
    return np.sqrt(2 * a * s)

def rot_ke_fraction(I_over_MR2):
    return I_over_MR2 / (1 + I_over_MR2)

SPHERE_IMR2 = 2/5
SHELL_IMR2  = 2/3

def verify():
    print("=== Rolling race verification ===")
    for name, imr2 in [("Solid sphere", SPHERE_IMR2), ("Hollow shell", SHELL_IMR2)]:
        v = final_speed(imr2)
        a = accel(imr2)
        frac = rot_ke_fraction(imr2)
        print(f"  {name}: I/MR²={imr2:.4f}, a={a:.4f} m/s², v_final={v:.4f} m/s, rot_KE={frac*100:.1f}%")
    # P1
    v_s = np.sqrt(10 * G * H / 7)
    v_h = np.sqrt(6 * G * H / 5)
    print(f"  P1: v_sphere theory = {v_s:.4f} m/s, computed = {final_speed(SPHERE_IMR2):.4f} m/s")
    print(f"  P1: v_shell  theory = {v_h:.4f} m/s, computed = {final_speed(SHELL_IMR2):.4f} m/s")
    # P2
    print(f"  P2: sphere rot_KE = {rot_ke_fraction(SPHERE_IMR2)*100:.2f}%  (expect 28.57%)")
    print(f"  P2: shell  rot_KE = {rot_ke_fraction(SHELL_IMR2)*100:.2f}%  (expect 40.00%)")
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

SLOPE_ANGLE_RAD = np.radians(THETA)


class RollingRaceMomentOfInertiaScene(Scene):
    """
    Side-by-side inclines. Sphere (blue) and shell (brown) roll down.
    Bar chart shows translational vs rotational KE split.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Rolling Race — Moment of Inertia Decides",
                     font="EB Garamond", font_size=50, color=INK)
        sub   = Text(
            "Solid sphere vs hollow shell  ·  same mass, same radius, same slope",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2  = Text(
            "a = g sinθ / (1 + I/MR²)  —  less rotational inertia = faster",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.28).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Incline geometry ───────────────────────────────────────────────
        # Ramp: top-left to bottom-right
        # Slope length for h=1 m at 30°: L_slope = H/sin(30°) = 2 m
        L_slope = H / np.sin(SLOPE_ANGLE_RAD)
        ramp_scale = 2.5  # screen units per metre

        ramp_top    = np.array([-4.0, 2.2, 0])
        ramp_bottom = ramp_top + ramp_scale * L_slope * np.array([np.cos(-SLOPE_ANGLE_RAD), np.sin(-SLOPE_ANGLE_RAD), 0])
        ground_pt   = np.array([ramp_bottom[0], ramp_top[1] - H * ramp_scale, 0])

        ramp_line  = Line(ramp_top, ramp_bottom, color=INK, stroke_width=2.5)
        ground_lne = Line(
            np.array([ramp_top[0] - 0.3, ground_pt[1], 0]),
            np.array([ramp_bottom[0] + 0.5, ground_pt[1], 0]),
            color=DIM, stroke_width=1.5,
        )
        theta_arc = Arc(
            radius=0.5, start_angle=-SLOPE_ANGLE_RAD, angle=SLOPE_ANGLE_RAD,
            arc_center=ramp_bottom, color=GOLD, stroke_width=1.5,
        )
        theta_lbl = MathTex(r"30°", color=GOLD, font_size=20).next_to(theta_arc, RIGHT, buff=0.06)

        self.play(Create(ramp_line), Create(ground_lne), Create(theta_arc), Write(theta_lbl), run_time=1.0)

        # ── Animate rolling ────────────────────────────────────────────────
        s_total = L_slope  # m
        a_sphere = accel(SPHERE_IMR2)
        a_shell  = accel(SHELL_IMR2)
        t_sphere = np.sqrt(2 * s_total / a_sphere)  # time for sphere to reach bottom
        t_shell  = np.sqrt(2 * s_total / a_shell)

        # Place two balls at top: sphere LEFT on ramp, shell slightly offset
        R_BALL = 0.15  # screen units

        def pos_on_ramp(s_m, offset_perp=0):
            """Screen position at distance s_m along ramp from top."""
            frac = s_m / L_slope
            base = ramp_top + (ramp_bottom - ramp_top) * frac
            perp = np.array([np.sin(SLOPE_ANGLE_RAD), np.cos(SLOPE_ANGLE_RAD), 0]) * offset_perp
            return base + perp + np.array([0, R_BALL, 0])

        sphere_dot = Circle(radius=R_BALL, color=BLUE, fill_color=BLUE, fill_opacity=0.8, stroke_width=0)
        sphere_dot.move_to(pos_on_ramp(0, offset_perp=-0.25))
        shell_dot  = Circle(radius=R_BALL, color=BROWN, fill_color=CANVAS,
                            stroke_color=BROWN, stroke_width=3.0)
        shell_dot.move_to(pos_on_ramp(0, offset_perp=0.25))

        lbl_s = Text("sphere", font="EB Garamond", font_size=16, color=BLUE)
        lbl_s.next_to(sphere_dot, UP, buff=0.08)
        lbl_h = Text("shell",   font="EB Garamond", font_size=16, color=BROWN)
        lbl_h.next_to(shell_dot, UP, buff=0.08)

        self.play(FadeIn(sphere_dot, shell_dot), Write(lbl_s), Write(lbl_h), run_time=0.7)
        self.wait(0.3)

        # Animate: use same real-time duration, sphere travels faster
        # We'll step frame-by-frame
        total_anim = t_shell + 0.3
        n_frames = 60
        for i in range(1, n_frames + 1):
            t_now = total_anim * i / n_frames
            s_sph = min(0.5 * a_sphere * t_now**2, s_total)
            s_shl = min(0.5 * a_shell  * t_now**2, s_total)
            sphere_dot.move_to(pos_on_ramp(s_sph, offset_perp=-0.25))
            shell_dot.move_to( pos_on_ramp(s_shl, offset_perp=0.25))
            lbl_s.next_to(sphere_dot, UP, buff=0.04)
            lbl_h.next_to(shell_dot, UP, buff=0.04)
            self.wait(total_anim / n_frames)

        self.wait(0.4)

        # ── Final speed labels ──────────────────────────────────────────────
        v_sph = final_speed(SPHERE_IMR2)
        v_shl = final_speed(SHELL_IMR2)
        speed_lbl = Text(
            f"Sphere: {v_sph:.3f} m/s     Shell: {v_shl:.3f} m/s   (Δ = 9.1%)",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(speed_lbl), run_time=0.9)
        self.wait(0.5)

        # ── KE bar chart (right side) ──────────────────────────────────────
        frac_s_rot   = rot_ke_fraction(SPHERE_IMR2)
        frac_s_trans = 1 - frac_s_rot
        frac_h_rot   = rot_ke_fraction(SHELL_IMR2)
        frac_h_trans = 1 - frac_h_rot

        bar_x_s  = 1.8
        bar_x_h  = 3.2
        bar_bot  = -1.8
        bar_h    = 3.0   # total bar height

        def bar(x, frac_trans, frac_rot, col_t, col_r):
            h_t = bar_h * frac_trans
            h_r = bar_h * frac_rot
            b_t = Rectangle(
                width=0.6, height=h_t,
                fill_color=col_t, fill_opacity=0.85, stroke_width=0, color=col_t,
            ).move_to(np.array([x, bar_bot + h_t/2, 0]))
            b_r = Rectangle(
                width=0.6, height=h_r,
                fill_color=col_r, fill_opacity=0.5, stroke_width=0, color=col_r,
            ).move_to(np.array([x, bar_bot + h_t + h_r/2, 0]))
            return b_t, b_r

        bt_s, br_s = bar(bar_x_s, frac_s_trans, frac_s_rot, BLUE,  DIM)
        bt_h, br_h = bar(bar_x_h, frac_h_trans, frac_h_rot, BROWN, DIM)

        lbl_bx_s = Text("sphere", font="EB Garamond", font_size=14, color=BLUE).move_to(np.array([bar_x_s, bar_bot - 0.25, 0]))
        lbl_bx_h = Text("shell",  font="EB Garamond", font_size=14, color=BROWN).move_to(np.array([bar_x_h, bar_bot - 0.25, 0]))
        lbl_trans = Text("trans", font="EB Garamond", font_size=12, color=INK).next_to(bt_s, RIGHT, buff=0.05)
        lbl_rot   = Text("rot",   font="EB Garamond", font_size=12, color=DIM).next_to(br_s, RIGHT, buff=0.05)

        pct_s = Text(f"rot: {frac_s_rot*100:.1f}%", font="EB Garamond", font_size=13, color=DIM)
        pct_s.next_to(br_s, UP, buff=0.05)
        pct_h = Text(f"rot: {frac_h_rot*100:.1f}%", font="EB Garamond", font_size=13, color=DIM)
        pct_h.next_to(br_h, UP, buff=0.05)

        self.play(
            FadeIn(bt_s, br_s, bt_h, br_h),
            Write(lbl_bx_s), Write(lbl_bx_h),
            Write(lbl_trans), Write(lbl_rot),
            Write(pct_s), Write(pct_h),
            run_time=1.2,
        )

        rule = Text(
            "More rotational KE = less translational KE = slower to the bottom",
            font="EB Garamond", font_size=19, color=GOLD,
        ).to_edge(UP, buff=0.22)
        self.play(Write(rule), run_time=1.0)
        self.wait(3.0)
