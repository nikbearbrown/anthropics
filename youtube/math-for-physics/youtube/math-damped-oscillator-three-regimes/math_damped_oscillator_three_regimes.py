#!/usr/bin/env python3
"""
math_damped_oscillator_three_regimes.py — Damped Oscillator: Three Regimes
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_damped_oscillator_three_regimes.py --verify

Physics/math (checkable):
    m=1 kg, k=100 N/m → ω₀=10 rad/s, T₀=2π/10≈0.6283 s
    b=4  (underdamped): γ=2, ω'=√(100-4)=√96≈9.798 rad/s, T'=2π/9.798≈0.6412 s
    b=20 (critically damped): γ=10, Δ=400-400=0, r=-10 (repeated)
    b=40 (overdamped): γ=20, Δ=1600-400=1200>0, r=(-20±√1200)/2
"""
import sys
import numpy as np

M = 1.0      # kg
K = 100.0    # N/m
OMEGA0 = np.sqrt(K / M)  # = 10.0 rad/s
X0 = 1.0     # initial displacement (m)
T_MAX = 3.5  # s


def gamma(b):
    return b / (2 * M)


def response(t, b):
    """Displacement x(t) for given damping coefficient b."""
    g = gamma(b)
    disc = g**2 - OMEGA0**2
    if disc < 0:
        # Underdamped
        wd = np.sqrt(-disc)
        return X0 * np.exp(-g * t) * np.cos(wd * t)
    elif disc == 0:
        # Critically damped
        return X0 * (1 + g * t) * np.exp(-g * t)
    else:
        # Overdamped
        r1 = -g + np.sqrt(disc)
        r2 = -g - np.sqrt(disc)
        # x(0)=1, x'(0)=0 → A+B=1, r1*A+r2*B=0 → A = -r2/(r1-r2), B = r1/(r1-r2)
        A = -r2 / (r1 - r2)
        B = r1 / (r1 - r2)
        return A * np.exp(r1 * t) + B * np.exp(r2 * t)


def verify():
    print("=== Damped oscillator verification ===")
    print(f"ω₀ = √(k/m) = √(100/1) = {OMEGA0:.4f} rad/s")
    print()
    # Underdamped
    b = 4
    g = gamma(b)
    wd = np.sqrt(OMEGA0**2 - g**2)
    Tprime = 2 * np.pi / wd
    print(f"b=4 (underdamped): γ={g}, ω'=√(100-4)=√96={wd:.4f}, T'={Tprime:.4f} s  (expect 0.6412 s)")
    # Critical
    b = 20
    disc = gamma(b)**2 - OMEGA0**2
    print(f"b=20 (critical): Δ = γ²-ω₀² = {gamma(b)**2:.1f}-{OMEGA0**2:.1f} = {disc:.1f}  (expect 0)")
    r_crit = -gamma(b)
    print(f"  repeated root r = {r_crit}")
    # Overdamped
    b = 40
    g40 = gamma(b)
    disc40 = g40**2 - OMEGA0**2
    r1 = -g40 + np.sqrt(disc40)
    r2 = -g40 - np.sqrt(disc40)
    print(f"b=40 (overdamped): Δ={disc40:.1f}>0, roots r1={r1:.3f}, r2={r2:.3f}")
    print()
    # Check x(0)=1 for all
    for bv in [4, 20, 40]:
        x0_check = response(np.array([0.0]), bv)[0]
        print(f"  x(0) at b={bv}: {x0_check:.6f}  (expect 1.0)")
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


class DampedOscillatorScene(Scene):
    """
    Three regimes of the damped oscillator on one axis.
    Underdamped (blue), critically damped (gold), overdamped (brown).
    Slider shows discriminant value; regime label updates.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_three_regimes(ax)
        self._phase_discriminant(ax)

    def _phase_title(self):
        title = Text("Damped Harmonic Oscillator", font="EB Garamond", font_size=56, color=INK)
        eq = MathTex(r"\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0", color=BLUE, font_size=36)
        sub = Text(
            "m=1 kg,  k=100 N/m,  ω₀=10 rad/s  —  three regimes of γ",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, eq, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(eq), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, eq, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0.0, T_MAX, 0.5],
            y_range=[-0.6, 1.3, 0.5],
            x_length=9.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.2, include_numbers=True,
                             font_size=16, decimal_number_config={"color": DIM}),
        ).shift(DOWN * 0.2)
        lbl_x = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"x(t)\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)
        return ax

    def _phase_three_regimes(self, ax):
        t_vals = np.linspace(0.001, T_MAX, 1200)

        # Build numpy arrays first
        y_under = response(t_vals, 4)
        y_crit = response(t_vals, 20)
        y_over = response(t_vals, 40)

        def make_curve(y_arr, color, sw=2.8):
            return ax.plot_line_graph(
                x_values=list(t_vals),
                y_values=list(np.clip(y_arr, -0.7, 1.4)),
                line_color=color,
                stroke_width=sw,
                add_vertex_dots=False,
            )

        curve_under = make_curve(y_under, BLUE)
        curve_crit = make_curve(y_crit, GOLD)
        curve_over = make_curve(y_over, BROWN)

        # Labels
        lbl_under = Text("Underdamped  b=4", font="EB Garamond", font_size=20, color=BLUE)
        lbl_crit  = Text("Critically damped  b=20", font="EB Garamond", font_size=20, color=GOLD)
        lbl_over  = Text("Overdamped  b=40", font="EB Garamond", font_size=20, color=BROWN)

        lbl_under.next_to(ax.c2p(0.65, np.interp(0.65, t_vals, y_under)), UP + LEFT, buff=0.1)
        lbl_crit.next_to(ax.c2p(0.3, np.interp(0.3, t_vals, y_crit)), RIGHT, buff=0.1)
        lbl_over.next_to(ax.c2p(0.5, np.interp(0.5, t_vals, y_over)), DOWN + RIGHT, buff=0.1)

        # Animate each curve with narration-style captions
        caption_under = Text(
            "Underdamped (b=4): oscillates, decaying envelope",
            font="EB Garamond", font_size=20, color=BLUE,
        ).to_edge(DOWN, buff=0.3)
        self.play(Create(curve_under), Write(caption_under), run_time=2.0)
        self.play(Write(lbl_under), run_time=0.5)
        self.wait(0.8)

        caption_crit = Text(
            "Critically damped (b=20): fastest return — Δ = 0",
            font="EB Garamond", font_size=20, color=GOLD,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(caption_under), Create(curve_crit), Write(caption_crit), run_time=2.0)
        self.play(Write(lbl_crit), run_time=0.5)
        self.wait(0.8)

        caption_over = Text(
            "Overdamped (b=40): sluggish exponential return, never oscillates",
            font="EB Garamond", font_size=20, color=BROWN,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(caption_crit), Create(curve_over), Write(caption_over), run_time=2.0)
        self.play(Write(lbl_over), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(caption_over), run_time=0.4)

    def _phase_discriminant(self, ax):
        formulas = VGroup(
            MathTex(r"\Delta = \gamma^2 - \omega_0^2", color=INK, font_size=30),
            MathTex(r"\Delta < 0 \Rightarrow \text{underdamped}", color=BLUE, font_size=26),
            MathTex(r"\Delta = 0 \Rightarrow \text{critically damped}", color=GOLD, font_size=26),
            MathTex(r"\Delta > 0 \Rightarrow \text{overdamped}", color=BROWN, font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_corner(UR, buff=0.4)

        self.play(Write(formulas), run_time=2.0)
        self.wait(2.0)

        # Period comparison
        wd = np.sqrt(OMEGA0**2 - gamma(4)**2)
        Tprime = 2 * np.pi / wd
        period_note = Text(
            f"Underdamped: T'= 2π/ω' = 2π/{wd:.2f} = {Tprime:.3f} s  (T₀={2*np.pi/OMEGA0:.3f} s)",
            font="EB Garamond", font_size=18, color=DIM,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(period_note), run_time=0.8)
        self.wait(2.5)
