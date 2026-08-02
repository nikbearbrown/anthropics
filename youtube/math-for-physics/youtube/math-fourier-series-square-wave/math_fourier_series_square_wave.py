#!/usr/bin/env python3
"""
math_fourier_series_square_wave.py — Fourier Series Building a Square Wave
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_fourier_series_square_wave.py --verify

Math (checkable):
    Square wave: f(x) = Σ (4/π)(1/n)sin(nπx)  for odd n = 1,3,5,7,9,11
    First partial sum amplitude: 4/π ≈ 1.2732
    Gibbs overshoot at N=13: ≈ 8.9% above 1.0 (Wilbraham-Gibbs constant ≈ 1.0895)
"""
import sys
import numpy as np

ODD_HARMONICS = [1, 3, 5, 7, 9, 11]


def fourier_partial_sum(x, harmonics):
    """Sum of (4/π)(1/n)sin(nπx) for n in harmonics."""
    total = np.zeros_like(x, dtype=float)
    for n in harmonics:
        total += (4.0 / (np.pi * n)) * np.sin(n * np.pi * x)
    return total


def gibbs_overshoot(n_terms):
    """Peak of partial sum near first jump, normalized to square wave height 1."""
    x_fine = np.linspace(0.0, 0.1, 10000)
    harmonics = list(range(1, 2 * n_terms, 2))  # first n odd harmonics
    peak = np.max(fourier_partial_sum(x_fine, harmonics))
    return peak


def verify():
    print("=== Fourier square wave verification ===")
    print(f"First harmonic amplitude: 4/π = {4.0/np.pi:.4f}  (expect 1.2732)")
    print()
    x_test = np.linspace(0.0, 2.0, 5000)
    for i, n in enumerate(ODD_HARMONICS):
        partial = fourier_partial_sum(x_test, ODD_HARMONICS[:i+1])
        peak = np.max(partial)
        print(f"  N up to {n}: peak = {peak:.4f}")
    print()
    # Gibbs at N=13 (7 terms)
    g = gibbs_overshoot(7)
    print(f"Gibbs overshoot (N=13, 7 terms): {g:.4f}  (expect ≈ 1.0895, i.e. 8.9% above 1)")
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

HARMONIC_COLORS = [BLUE, BROWN, GOLD, "#E87040", "#A0D0A0", "#C080C0"]


class FourierSquareWaveScene(Scene):
    """
    Dashed square wave in background. Add odd harmonics one at a time (n=1,3,5,7,9,11).
    Each addition snaps partial sum closer. Gibbs overshoot persists.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        ax = self._phase_axes()
        self._phase_square_wave(ax)
        self._phase_build_harmonics(ax)
        self._phase_gibbs(ax)

    def _phase_title(self):
        title = Text("Fourier Series: Square Wave", font="EB Garamond", font_size=58, color=INK)
        sub1 = Text(
            "f(x) = (4/π)[sin(πx) + (1/3)sin(3πx) + (1/5)sin(5πx) + …]",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2 = Text(
            "odd harmonics only — amplitudes fall as 1/n",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0.0, 2.1, 0.5],
            y_range=[-1.6, 1.6, 0.5],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.2, include_numbers=True,
                             font_size=16, decimal_number_config={"color": DIM}),
        ).shift(DOWN * 0.3)
        lbl_x = MathTex(r"x", color=INK, font_size=40).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"f(x)", color=INK, font_size=40).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)
        return ax

    def _phase_square_wave(self, ax):
        """Draw the ideal square wave as dashed lines."""
        segs = []
        # Square wave: +1 for x in [0,1), -1 for x in [1,2)
        for x0, x1, y in [(0.0, 1.0, 1.0), (1.0, 2.0, -1.0)]:
            seg = ax.plot(lambda x, _y=y: _y, x_range=[x0, x1 - 0.001], color=DIM,
                          stroke_width=1.5, stroke_opacity=0.7)
            segs.append(seg)
        # Vertical connectors
        v1 = DashedLine(ax.c2p(1.0, 1.0), ax.c2p(1.0, -1.0), color=DIM, stroke_opacity=0.5)
        self.play(*[Create(s) for s in segs], Create(v1), run_time=0.8)
        lbl = Text("ideal square wave", font="EB Garamond", font_size=18, color=DIM)
        lbl.next_to(ax.c2p(1.8, 1.0), UP, buff=0.15)
        self.play(Write(lbl), run_time=0.4)
        self.wait(0.3)

    def _phase_build_harmonics(self, ax):
        x_vals = np.linspace(0.001, 1.999, 800)

        current_sum = np.zeros_like(x_vals)
        current_curve = None
        header_lbl = None

        for idx, n in enumerate(ODD_HARMONICS):
            harmonic = (4.0 / (np.pi * n)) * np.sin(n * np.pi * x_vals)
            current_sum = current_sum + harmonic

            # Draw the new harmonic briefly
            xs = list(x_vals)
            ys_h = list(harmonic)
            harm_curve = ax.plot_line_graph(
                x_values=xs, y_values=ys_h,
                line_color=HARMONIC_COLORS[idx], stroke_width=1.5, add_vertex_dots=False,
            )

            ys_s = list(current_sum)
            sum_curve = ax.plot_line_graph(
                x_values=xs, y_values=ys_s,
                line_color=INK, stroke_width=2.5, add_vertex_dots=False,
            )

            new_lbl = Text(
                f"+ (4/π)·(1/{n})·sin({n}πx)   →   {idx+1} term{'s' if idx else ''}",
                font="EB Garamond", font_size=20, color=HARMONIC_COLORS[idx],
            ).to_edge(UP, buff=0.25)

            anims = [Create(harm_curve), Write(new_lbl)]
            if current_curve:
                anims.append(FadeOut(current_curve))
            if header_lbl:
                anims.append(FadeOut(header_lbl))

            self.play(*anims, run_time=1.0)
            self.wait(0.3)
            self.play(
                FadeOut(harm_curve),
                FadeIn(sum_curve),
                run_time=0.8,
            )
            self.wait(0.6)

            current_curve = sum_curve
            header_lbl = new_lbl

        self.wait(0.5)

    def _phase_gibbs(self, ax):
        x_vals = np.linspace(0.001, 1.999, 2000)
        # 7 terms (N=1,3,5,7,9,11,13)
        harmonics_13 = [1, 3, 5, 7, 9, 11, 13]
        y_13 = sum((4.0 / (np.pi * n)) * np.sin(n * np.pi * x_vals) for n in harmonics_13)
        peak_x = x_vals[np.argmax(y_13[:1000])]
        peak_y = np.max(y_13[:1000])

        curve_13 = ax.plot_line_graph(
            x_values=list(x_vals), y_values=list(y_13),
            line_color=GOLD, stroke_width=2.5, add_vertex_dots=False,
        )
        self.play(FadeIn(curve_13), run_time=1.0)

        # Mark Gibbs peak
        peak_dot = Dot(ax.c2p(peak_x, peak_y), color=GOLD, radius=0.1)
        gibbs_lbl = Text("Gibbs overshoot ≈ 8.9%", font="EB Garamond", font_size=20, color=GOLD)
        gibbs_lbl.next_to(ax.c2p(peak_x, peak_y), UP + RIGHT, buff=0.15)
        arrow = Arrow(gibbs_lbl.get_bottom(), ax.c2p(peak_x, peak_y), color=GOLD, buff=0.05, stroke_width=2)

        formula = MathTex(
            r"\lim_{N\to\infty}\text{overshoot} \approx 8.9\%  \text{ (Wilbraham--Gibbs)}",
            color=INK, font_size=40,
        ).to_edge(DOWN, buff=0.3)

        self.play(FadeIn(peak_dot), Write(gibbs_lbl), Create(arrow), run_time=1.0)
        self.play(Write(formula), run_time=1.0)
        self.wait(2.5)
