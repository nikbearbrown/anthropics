#!/usr/bin/env python3
"""
math_shm_amplitude_independence.py — SHM: Period Independent of Amplitude
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_shm_amplitude_independence.py --verify

Physics (checkable):
    m=2.00 kg, k=32.0 N/m → ω=√(k/m)=√16=4.00 rad/s
    T = 2π/ω = 2π/4 = π/2 ≈ 1.5708 s  (ALL amplitudes)
    A=0.020 m: v_max = Aω = 0.020·4 = 0.080 m/s
    A=0.040 m: v_max = 0.040·4 = 0.160 m/s
    A=0.080 m: v_max = 0.080·4 = 0.320 m/s
"""
import sys
import numpy as np

M = 2.00   # kg
K = 32.0   # N/m
OMEGA = np.sqrt(K / M)  # = 4.0 rad/s
T_PERIOD = 2 * np.pi / OMEGA
AMPLITUDES = [0.020, 0.040, 0.080]


def x_shm(A, t):
    return A * np.cos(OMEGA * t)


def verify():
    print("=== SHM amplitude-independence verification ===")
    print(f"ω = √(k/m) = √({K}/{M}) = {OMEGA:.4f} rad/s")
    print(f"T = 2π/ω = {T_PERIOD:.6f} s  (≈ π/2 = {np.pi/2:.6f} s)")
    print()
    for A in AMPLITUDES:
        vmax = A * OMEGA
        print(f"A={A:.3f} m:  T={T_PERIOD:.4f} s  (same!),  v_max={vmax:.4f} m/s")
    print()
    # Check: all return to x=A at t=T
    for A in AMPLITUDES:
        x_at_T = x_shm(A, T_PERIOD)
        print(f"A={A:.3f}: x(T) = {x_at_T:.8f}  (expect {A:.3f})")
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

AMP_COLORS = [BLUE, GOLD, BROWN]


class SHMAmplitudeScene(Scene):
    """
    Three cosine curves (A=0.020, 0.040, 0.080 m) launch simultaneously.
    All complete first cycle at identical time T = π/2 s.
    Vertical period-tick lines sweep to mark identical crossings.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_three_curves(ax)
        self._phase_period_lines(ax)
        self._phase_vmax(ax)

    def _phase_title(self):
        title = Text("SHM: Period Independent of Amplitude", font="EB Garamond", font_size=52, color=INK)
        eq = MathTex(
            r"x(t) = A\cos(\omega t), \quad T = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{k/m}}",
            color=BLUE, font_size=32,
        )
        sub = Text(
            "m=2 kg,  k=32 N/m,  ω=4 rad/s,  T=π/2 ≈ 1.571 s",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, eq, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(eq), run_time=0.9)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, eq, sub), run_time=0.5)

    def _phase_axes(self):
        t_max = 2.0 * T_PERIOD
        ax = Axes(
            x_range=[0.0, t_max * 1.05, T_PERIOD / 2],
            y_range=[-0.10, 0.10, 0.04],
            x_length=9.5,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.2, include_numbers=True,
                             font_size=16, decimal_number_config={"color": DIM, "num_decimal_places": 2}),
        ).shift(DOWN * 0.3)
        lbl_x = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)
        return ax

    def _phase_three_curves(self, ax):
        t_max = 2.0 * T_PERIOD
        t_vals = np.linspace(0.0, t_max, 800)

        curves = []
        lbls = []
        for i, A in enumerate(AMPLITUDES):
            y_vals = x_shm(A, t_vals)
            curve = ax.plot_line_graph(
                x_values=list(t_vals),
                y_values=list(y_vals),
                line_color=AMP_COLORS[i],
                stroke_width=2.8,
                add_vertex_dots=False,
            )
            lbl = Text(
                f"A = {A*100:.0f} cm  ({AMP_COLORS[i]})",
                font="EB Garamond", font_size=19, color=AMP_COLORS[i],
            )
            curves.append(curve)
            lbls.append(lbl)

        legend = VGroup(*lbls).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_corner(UR, buff=0.4)

        self.play(
            *[Create(c) for c in curves],
            *[Write(l) for l in lbls],
            run_time=2.0,
        )
        self.wait(1.0)

    def _phase_period_lines(self, ax):
        t_max = 2.0 * T_PERIOD
        caption = Text(
            f"T = π/2 ≈ {T_PERIOD:.4f} s  — identical for ALL amplitudes",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=0.8)

        for k in [1, 2]:
            t_tick = k * T_PERIOD
            y_lo = ax.c2p(t_tick, -0.095)
            y_hi = ax.c2p(t_tick, 0.095)
            line = DashedLine(y_lo, y_hi, color=GOLD, stroke_width=2.5, dash_length=0.1)
            tick_lbl = MathTex(
                rf"t = {k}T",
                color=GOLD, font_size=20,
            ).next_to(y_hi, UP, buff=0.08)
            self.play(Create(line), Write(tick_lbl), run_time=0.7)
            self.wait(0.5)

        self.wait(1.5)

    def _phase_vmax(self, ax):
        rows = []
        for i, A in enumerate(AMPLITUDES):
            vmax = A * OMEGA
            row = MathTex(
                rf"A={A*100:.0f}\;\mathrm{{cm}}: \;v_{{\max}}=A\omega={vmax*100:.1f}\;\mathrm{{cm/s}}",
                color=AMP_COLORS[i], font_size=24,
            )
            rows.append(row)
        rows_grp = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        note = Text("Speed varies, period does not.", font="EB Garamond", font_size=22, color=INK)
        VGroup(rows_grp, note).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=0.25)
        self.play(Write(rows_grp), run_time=1.0)
        self.play(Write(note), run_time=0.6)
        self.wait(2.5)
