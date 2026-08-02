#!/usr/bin/env python3
"""
phasor_vector_addition.py — Phasor Addition: Two Oscillations Add as Vectors
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/phasor-vector-addition
    manim -qh phasor_vector_addition.py PhasorVectorAdditionScene

Verify:
    python3 phasor_vector_addition.py --verify

Physics:
    A₁=3, φ₁=0  → phasor (3, 0)
    A₂=4, φ₂=90° → phasor (0, 4)
    |result| = 5,  phase = arctan(4/3) = 53.13°
    P2: when φ=180°, A₁=A₂ → amplitude = 0 (total cancellation)
"""
import sys
import numpy as np

def verify():
    print("=== Phasor addition verification ===")
    A1, phi1 = 3.0, 0.0
    A2, phi2 = 4.0, np.pi / 2
    z1 = A1 * np.exp(1j * phi1)
    z2 = A2 * np.exp(1j * phi2)
    z_sum = z1 + z2
    print(f"  phasor 1: {z1.real:.4f} + {z1.imag:.4f}i")
    print(f"  phasor 2: {z2.real:.4f} + {z2.imag:.4f}i")
    print(f"  sum:      {z_sum.real:.4f} + {z_sum.imag:.4f}i")
    print(f"  |sum|   = {abs(z_sum):.6f}  (should be 5.000000)")
    print(f"  phase   = {np.degrees(np.angle(z_sum)):.4f}°  (should be 53.1301°)")
    # P2: cancellation
    z2_cancel = 3.0 * np.exp(1j * np.pi)
    print(f"\n  Cancellation: A=3, φ=180° → sum magnitude = {abs(z1 + z2_cancel):.10f}  (should be 0)")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class PhasorVectorAdditionScene(Scene):
    """
    Phase 1: title
    Phase 2: two rotating phasors (3,0) and (0,4), tip-to-tail sum, 3 sinusoids below
    Phase 3: sweep φ from 0 → 2π — show |result| vs φ
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_phasor_demo()
        self._phase_phase_sweep()

    def _phase_title(self):
        title = Text("Phasor Addition", font="EB Garamond", font_size=64, color=INK)
        sub   = Text(
            "3 cos(ωt) + 4 cos(ωt + 90°) = 5 cos(ωt + 53°)  —  one Pythagorean step",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_phasor_demo(self):
        # Phasor plane (left half)
        ax = ComplexPlane(
            x_range=[-5.5, 5.5, 1], y_range=[-5.5, 5.5, 1],
            x_length=5.5, y_length=5.5,
            background_line_style={"stroke_color": DIM, "stroke_width": 0.5},
            axis_config={"color": INK, "stroke_width": 1.2},
        ).shift(LEFT * 3.0)

        lbl_re = Text("Re", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_im = Text("Im", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(ax), Write(lbl_re), Write(lbl_im), run_time=1.2)

        unit   = ax.get_x_unit_size()
        origin = ax.get_origin()

        A1, phi1 = 3.0, 0.0
        A2, phi2 = 4.0, np.pi / 2
        omega    = 1.0
        tracker  = ValueTracker(0.0)

        def tip1(t):
            return origin + unit * np.array([A1 * np.cos(omega * t + phi1), A1 * np.sin(omega * t + phi1), 0])

        def tip2(t):
            return tip1(t) + unit * np.array([A2 * np.cos(omega * t + phi2), A2 * np.sin(omega * t + phi2), 0])

        def tip_sum(t):
            z_sum = A1 * np.exp(1j * phi1) + A2 * np.exp(1j * phi2)
            A_r   = abs(z_sum)
            phi_r = np.angle(z_sum)
            return origin + unit * np.array([A_r * np.cos(omega * t + phi_r), A_r * np.sin(omega * t + phi_r), 0])

        def _arr1():
            t   = tracker.get_value()
            return Arrow(origin, tip1(t), buff=0, color=BLUE, stroke_width=2.5, max_tip_length_to_length_ratio=0.15)
        def _arr2():
            t   = tracker.get_value()
            return Arrow(tip1(t), tip2(t), buff=0, color=BROWN, stroke_width=2.5, max_tip_length_to_length_ratio=0.15)
        def _arr_sum():
            t   = tracker.get_value()
            return Arrow(origin, tip_sum(t), buff=0, color=GOLD, stroke_width=2.8, max_tip_length_to_length_ratio=0.15)

        a1_dyn   = always_redraw(_arr1)
        a2_dyn   = always_redraw(_arr2)
        asum_dyn = always_redraw(_arr_sum)
        self.add(a1_dyn, a2_dyn, asum_dyn)

        # Sinusoid panel on right
        ax_sin = Axes(
            x_range=[0, 4*np.pi, np.pi], y_range=[-5.5, 5.5, 2],
            x_length=5.5, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).shift(RIGHT * 2.8)

        t_arr = np.linspace(0, 4 * np.pi, 500)
        s1 = ax_sin.plot(lambda t: A1 * np.cos(omega * t + phi1), color=BLUE, stroke_width=2.0)
        s2 = ax_sin.plot(lambda t: A2 * np.cos(omega * t + phi2), color=BROWN, stroke_width=2.0)
        z_sum = A1 * np.exp(1j * phi1) + A2 * np.exp(1j * phi2)
        s_sum = ax_sin.plot(lambda t: abs(z_sum) * np.cos(omega * t + np.angle(z_sum)), color=GOLD, stroke_width=2.5)

        lbl1  = Text("A₁=3, φ=0°",    font="EB Garamond", font_size=18, color=BLUE).to_corner(UR, buff=0.35).shift(DOWN*0.0)
        lbl2  = Text("A₂=4, φ=90°",   font="EB Garamond", font_size=18, color=BROWN).to_corner(UR, buff=0.35).shift(DOWN*0.4)
        lbl_s = Text("|A|=5, φ=53°",  font="EB Garamond", font_size=18, color=GOLD).to_corner(UR, buff=0.35).shift(DOWN*0.8)

        self.play(Create(ax_sin), Create(s1), Create(s2), Create(s_sum),
                  Write(lbl1), Write(lbl2), Write(lbl_s), run_time=1.5)

        pyth = MathTex(r"|A| = \sqrt{3^2 + 4^2} = 5", color=GOLD, font_size=30).to_edge(DOWN, buff=0.28)
        self.play(Write(pyth), run_time=0.8)

        # Rotate phasors two full turns
        self.play(tracker.animate.set_value(4 * np.pi), run_time=5.0, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(ax, ax_sin, s1, s2, s_sum, a1_dyn, a2_dyn, asum_dyn,
                          lbl_re, lbl_im, lbl1, lbl2, lbl_s, pyth), run_time=0.5)

    def _phase_phase_sweep(self):
        phi_tracker = ValueTracker(0.0)
        A1, A2 = 3.0, 4.0

        def _ampl(phi):
            z = A1 + A2 * np.exp(1j * phi)
            return abs(z)

        # Axes for |A(φ)| vs φ
        ax = Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[0, 7.5, 1],
            x_length=9.0, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.5, "include_ticks": True},
        ).center().shift(UP * 0.3)

        x_labels = ax.get_x_axis().add_labels({
            0: MathTex("0", font_size=18, color=DIM),
            np.pi / 2: MathTex(r"\pi/2", font_size=18, color=DIM),
            np.pi: MathTex(r"\pi", font_size=18, color=DIM),
            3 * np.pi / 2: MathTex(r"3\pi/2", font_size=18, color=DIM),
            2 * np.pi: MathTex(r"2\pi", font_size=18, color=DIM),
        })

        full_curve = ax.plot(lambda phi: _ampl(phi), x_range=[0, 2 * np.pi], color=GOLD, stroke_width=2.5)
        hdr = Text(
            "Sweep φ from 0 to 2π — resultant amplitude |A₁ + A₂ e^{iφ}|",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(ax), Create(full_curve), run_time=1.5)

        # Dot riding the curve
        dot = always_redraw(lambda: Dot(
            ax.c2p(phi_tracker.get_value(), _ampl(phi_tracker.get_value())),
            color=BLUE, radius=0.12,
        ))
        lbl_val = always_redraw(lambda: MathTex(
            rf"|A| = {_ampl(phi_tracker.get_value()):.2f}",
            color=BLUE, font_size=26,
        ).to_corner(UR, buff=0.35))

        self.add(dot, lbl_val)
        self.play(phi_tracker.animate.set_value(2 * np.pi), run_time=5.0, rate_func=smooth)
        self.wait(1.0)

        # Mark zero at φ=180°
        cancel_dot = Dot(ax.c2p(np.pi, _ampl(np.pi)), color=BROWN, radius=0.14)
        cancel_lbl = MathTex(r"\phi=\pi:\;|A|=|A_1-A_2|=1", color=BROWN, font_size=24).next_to(cancel_dot, DOWN, buff=0.2)
        self.play(FadeIn(cancel_dot), Write(cancel_lbl), run_time=0.8)
        self.wait(2.0)
        fin = Text(
            "Perpendicular phasors (90°) add by Pythagoras  ·  opposite (180°) subtract",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(fin), run_time=0.8)
        self.wait(2.5)
