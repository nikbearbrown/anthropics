#!/usr/bin/env python3
"""
math_standing_waves_guitar_string.py — Standing Waves on a Guitar String
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_standing_waves_guitar_string.py --verify

Physics (checkable):
    L=0.65 m, v=427 m/s (guitar E-string)
    f₁ = v/(2L) = 427/(1.30) ≈ 328.5 Hz ≈ 329 Hz  ✓
    f₂ = 2·f₁ ≈ 657 Hz, f₃ ≈ 985 Hz, f₄ ≈ 1314 Hz
    Mode n has (n-1) interior nodes
    Mode 4 nodes at x = L/4, L/2, 3L/4  →  sin(4π·x/L)=0 ✓
"""
import sys
import numpy as np

L = 0.65    # m
V = 427.0   # m/s


def f_n(n):
    return n * V / (2 * L)


def mode_y(n, x, t):
    return np.sin(n * np.pi * x / L) * np.cos(n * np.pi * V * t / L)


def verify():
    print("=== Standing waves verification ===")
    for n in [1, 2, 3, 4]:
        fn = f_n(n)
        print(f"Mode {n}: f={fn:.1f} Hz  ({n-1} interior nodes)")
    print()
    # Check nodes of mode 4
    print("Mode 4 node positions (sin(4πx/L)=0):")
    for frac in [0.25, 0.5, 0.75]:
        x_node = frac * L
        y = np.sin(4 * np.pi * x_node / L)
        print(f"  x = {frac}L = {x_node:.4f} m → sin(...) = {y:.8f}  (expect 0)")
    print()
    # Frequency ratios
    print(f"f2/f1 = {f_n(2)/f_n(1):.4f}  (expect 2)")
    print(f"f3/f1 = {f_n(3)/f_n(1):.4f}  (expect 3)")
    print(f"f4/f1 = {f_n(4)/f_n(1):.4f}  (expect 4)")
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

MODE_COLORS = [BLUE, GOLD, BROWN, "#A0D0A0"]


class StandingWavesScene(Scene):
    """
    Animate standing wave modes n=1,2,3,4 on a guitar string.
    Show node positions. Final beat: all four modes superimposed.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_modes()
        self._phase_superposition()

    def _phase_title(self):
        title = Text("Standing Waves — Guitar String", font="EB Garamond", font_size=56, color=INK)
        sub1 = Text("L = 0.65 m,  v = 427 m/s  (E-string)", font="EB Garamond", font_size=24, color=BLUE)
        sub2 = MathTex(
            r"y_n(x,t) = \sin\!\left(\frac{n\pi x}{L}\right)\cos\!\left(\frac{n\pi v t}{L}\right)",
            color=DIM, font_size=28,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub1), run_time=0.5)
        self.play(Write(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_modes(self):
        x_vals = np.linspace(0, L, 300)

        for n in [1, 2, 3, 4]:
            # Title
            fn = f_n(n)
            mode_title = Text(
                f"Mode n={n}  →  f={fn:.0f} Hz  ({n-1} interior node{'s' if n > 2 else ''})",
                font="EB Garamond", font_size=24, color=MODE_COLORS[n - 1],
            ).to_edge(UP, buff=0.3)

            # Create axes for this mode
            ax = Axes(
                x_range=[0.0, L * 1.05, L / 4],
                y_range=[-1.3, 1.3, 0.5],
                x_length=8.5,
                y_length=3.5,
                axis_config=dict(color=INK, stroke_width=1.2, include_ticks=False,
                                 tip_length=0.15),
            ).shift(DOWN * 0.5)

            # Endpoints (fixed boundary)
            end_l = Dot(ax.c2p(0, 0), color=INK, radius=0.08)
            end_r = Dot(ax.c2p(L, 0), color=INK, radius=0.08)

            # Axis label
            lbl_x = MathTex(r"x\;(\mathrm{m})", color=DIM, font_size=18).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)

            self.play(Create(ax), FadeIn(end_l), FadeIn(end_r), Write(mode_title), Write(lbl_x), run_time=0.8)

            # Animate oscillation using ValueTracker for time
            t_tracker = ValueTracker(0.0)
            T_period = 2 * L / (n * V)

            def make_wave_curve(ax_ref, n_ref, t_ref):
                def _curve():
                    t = t_ref.get_value()
                    y = mode_y(n_ref, x_vals, t)
                    return ax_ref.plot_line_graph(
                        x_values=list(x_vals),
                        y_values=list(y),
                        line_color=MODE_COLORS[n_ref - 1],
                        stroke_width=3.0,
                        add_vertex_dots=False,
                    )
                return _curve

            wave = always_redraw(make_wave_curve(ax, n, t_tracker))
            self.add(wave)

            # Mark nodes
            node_dots = []
            for k in range(1, n):
                x_node = k * L / n
                nd = Dot(ax.c2p(x_node, 0.0), color=GOLD, radius=0.1)
                node_dots.append(nd)

            if node_dots:
                self.play(*[FadeIn(nd) for nd in node_dots], run_time=0.4)

            # Animate oscillation for ~ 2 periods
            anim_duration = max(2.5, 2.0 * T_period * 60)  # at least 2.5s
            self.play(
                t_tracker.animate.set_value(2.0 * T_period),
                run_time=2.5,
                rate_func=linear,
            )
            self.wait(0.5)

            # Frequency label
            freq_eq = MathTex(
                rf"f_{n} = \frac{{{n} \cdot v}}{{2L}} = {fn:.0f}\;\mathrm{{Hz}}",
                color=MODE_COLORS[n - 1], font_size=26,
            ).to_edge(DOWN, buff=0.3)
            self.play(Write(freq_eq), run_time=0.6)
            self.wait(0.8)

            self.play(
                FadeOut(ax, wave, mode_title, lbl_x, end_l, end_r, freq_eq,
                        *node_dots),
                run_time=0.5,
            )
            self.remove(wave)

    def _phase_superposition(self):
        ax = Axes(
            x_range=[0.0, L * 1.05, L / 4],
            y_range=[-2.5, 2.5, 1.0],
            x_length=8.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.2, include_ticks=False, tip_length=0.15),
        ).shift(DOWN * 0.3)

        title = Text(
            "All four modes superimposed — the rich waveform of a real guitar string",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.3)

        self.play(Create(ax), Write(title), run_time=1.0)

        x_vals = np.linspace(0, L, 300)
        t_tracker = ValueTracker(0.0)

        def super_curve():
            t = t_tracker.get_value()
            y = sum(mode_y(n, x_vals, t) * (1.0 / n) for n in [1, 2, 3, 4])
            return ax.plot_line_graph(
                x_values=list(x_vals),
                y_values=list(y),
                line_color=GOLD,
                stroke_width=3.0,
                add_vertex_dots=False,
            )

        super_wave = always_redraw(super_curve)
        self.add(super_wave)

        formula = MathTex(
            r"y = \sum_{n=1}^{4} \frac{1}{n}\sin\!\left(\frac{n\pi x}{L}\right)\cos\!\left(\frac{n\pi v t}{L}\right)",
            color=DIM, font_size=24,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(formula), run_time=0.8)

        self.play(t_tracker.animate.set_value(2.0 / f_n(1)), run_time=3.0, rate_func=linear)
        self.wait(2.0)
        self.remove(super_wave)
