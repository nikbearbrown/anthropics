#!/usr/bin/env python3
"""
classical_angular_momentum_skater.py — Figure Skater: L conserved, KE not
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    I_i = 4.0 kg·m², ω_i = 1.5 rev/s → 9.42 rad/s
    I_f = 1.0 kg·m², ω_f = 6.0 rev/s → 37.7 rad/s
    KE_i = 177 J, KE_f = 710 J, ΔKE = 533 J (muscle work)
    L = 37.7 kg·m²/s throughout

Render:
    cd physics-classical-mechanics/youtube/classical-angular-momentum-skater
    manim -qh classical_angular_momentum_skater.py AngularMomentumSkaterScene
"""
import sys
import numpy as np

I_I  = 4.0    # kg·m²
W_I  = 1.5 * 2 * np.pi   # rad/s
I_F  = 1.0
W_F  = I_I * W_I / I_F
KE_I = 0.5 * I_I * W_I**2
KE_F = 0.5 * I_F * W_F**2
L    = I_I * W_I


def verify():
    print("=== Angular Momentum Skater verification ===")
    print(f"  ω_i = {W_I:.4f} rad/s  (1.5 rev/s × 2π)")
    print(f"  ω_f = {W_F:.4f} rad/s  (expected 6.0 × 2π = {6*2*np.pi:.4f})")
    print(f"  KE_i = {KE_I:.2f} J  (expected 177 J)")
    print(f"  KE_f = {KE_F:.2f} J  (expected 710 J)")
    print(f"  ΔKE = {KE_F-KE_I:.2f} J  (muscle work, expected 533 J)")
    print(f"  L_i = {L:.4f},  L_f = {I_F*W_F:.4f}  (should match)")
    # P1
    assert abs(W_F/W_I - I_I/I_F) < 1e-8, "P1: ω ratio"
    # P2
    ratio = KE_F/KE_I
    print(f"  KE_f/KE_i = {ratio:.4f}  (expected {I_I/I_F:.1f})")
    assert abs(ratio - I_I/I_F) < 0.01, "P2: KE ratio"
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class AngularMomentumSkaterScene(Scene):
    """Skater arm pull → ω rises 4×; L stays flat; KE climbs 4×."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._skater_animation()
        self._gauges()

    def _title(self):
        t1 = Text("Figure Skater Spin", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("Angular momentum is conserved — kinetic energy is not",
                  font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"L = I\omega = \mathrm{const}\qquad \Delta KE = \mathrm{muscle\ work}",
                     color=GOLD, font_size=28)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _skater_animation(self):
        """Top-down view: body dot + two arm lines, arms retract."""
        body = Circle(radius=0.25, color=INK, fill_color=INK, fill_opacity=0.9).center()
        arm_len_i = 1.4
        arm_len_f = 0.35
        arm_L = Line(ORIGIN, LEFT*arm_len_i, color=BLUE, stroke_width=6)
        arm_R = Line(ORIGIN, RIGHT*arm_len_i, color=BLUE, stroke_width=6)

        lbl_I = Text(f"I = {I_I:.1f} kg·m²  ω = 1.5 rev/s",
                     font="EB Garamond", font_size=20, color=BLUE).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(body, arm_L, arm_R), Write(lbl_I), run_time=0.8)

        # Spin at slow ω
        for ang in np.linspace(0, 2*np.pi, 30):
            arm_L.put_start_and_end_on(ORIGIN, arm_len_i*np.array([-np.cos(ang), np.sin(ang), 0]))
            arm_R.put_start_and_end_on(ORIGIN, arm_len_i*np.array([np.cos(ang), -np.sin(ang), 0]))
            self.wait(0.025)

        # Arms retract
        lbl_If = Text(f"I = {I_F:.1f} kg·m²  ω = 6.0 rev/s  (4× faster)",
                      font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.5)
        self.play(
            arm_L.animate.put_start_and_end_on(ORIGIN, LEFT*arm_len_f),
            arm_R.animate.put_start_and_end_on(ORIGIN, RIGHT*arm_len_f),
            FadeOut(lbl_I), Write(lbl_If),
            run_time=1.5,
        )

        # Spin at fast ω
        for ang in np.linspace(0, 4*np.pi, 60):
            arm_L.put_start_and_end_on(ORIGIN, arm_len_f*np.array([-np.cos(ang), np.sin(ang), 0]))
            arm_R.put_start_and_end_on(ORIGIN, arm_len_f*np.array([np.cos(ang), -np.sin(ang), 0]))
            self.wait(0.018)

        self.wait(0.5)
        self.play(FadeOut(body, arm_L, arm_R, lbl_If), run_time=0.4)

    def _gauges(self):
        """L stays flat; KE climbs 4×."""
        ax = Axes(
            x_range=[0, 2.0, 0.5],
            y_range=[0, 800, 200],
            x_length=10,
            y_length=5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.4)
        lx = Text("time (arm pulls in at t=1 s)", font="EB Garamond", font_size=18, color=INK)
        lx.next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("J or kg·m²/s", font="EB Garamond", font_size=18, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("KE rises — L stays pinned",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        # L = constant throughout
        ts = np.linspace(0, 2.0, 200)
        L_vals = np.full_like(ts, L)
        KE_vals = np.where(ts < 1.0, KE_I, KE_F)

        pts_L  = np.array([ax.c2p(t, l) for t, l in zip(ts, L_vals)])
        pts_KE = np.array([ax.c2p(t, k) for t, k in zip(ts, KE_vals)])

        crv_L  = VMobject(color=BLUE,  stroke_width=2.8).set_points_smoothly(pts_L)
        crv_KE = VMobject(color=GOLD,  stroke_width=2.8).set_points_smoothly(pts_KE)

        lbl_L  = MathTex(r"L = 37.7\;\mathrm{kg\cdot m^2/s}", color=BLUE, font_size=20).move_to(ax.c2p(1.5, L+20))
        lbl_KE = MathTex(r"KE", color=GOLD, font_size=20).move_to(ax.c2p(1.5, KE_F+25))

        self.play(Create(crv_L), Create(crv_KE), Write(lbl_L), Write(lbl_KE), run_time=2.0)

        # Muscle work annotation
        arr = Arrow(ax.c2p(1.1, KE_I), ax.c2p(1.1, KE_F), color=BROWN, buff=0)
        muscle_lbl = MathTex(r"+533\,\mathrm{J}", color=BROWN, font_size=22).next_to(arr, RIGHT, buff=0.1)
        self.play(GrowArrow(arr), Write(muscle_lbl), run_time=0.8)

        final = Text(
            "L is free — the energy cost is muscle work against centrifugal load",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
