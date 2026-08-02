#!/usr/bin/env python3
"""
math_power_law_loglog_slope.py — Power Law: Log-Log Straightening
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_power_law_loglog_slope.py --verify

Math (checkable):
    Free-fall: d = 4.9·t²
    At t=1: d=4.9, t=100: d=49000
    log-log slope = (log10(49000)-log10(4.9))/(log10(100)-log10(1))
                  = (4.6902-0.6902)/(2-0) = 4.0/2.0 = 2.000 ✓
    If exponent n=1/2: slope = 0.5 (pendulum T∝√L)
"""
import sys
import numpy as np

T_VALS = np.array([1, 2, 5, 10, 20, 50, 100], dtype=float)


def freefall_d(t):
    return 4.9 * t**2


def verify():
    print("=== Power-law log-log slope verification ===")
    d_vals = freefall_d(T_VALS)
    print("Free-fall d = 4.9t²:")
    for t, d in zip(T_VALS, d_vals):
        print(f"  t={t:.0f} s → d={d:.1f} m  (log t={np.log10(t):.4f}, log d={np.log10(d):.4f})")
    log_t = np.log10(T_VALS)
    log_d = np.log10(d_vals)
    slope, intercept = np.polyfit(log_t, log_d, 1)
    print(f"\nlog-log slope = {slope:.6f}  (expect 2.0000)")
    print(f"log-log intercept = {intercept:.6f}  (= log10(4.9) = {np.log10(4.9):.6f})")
    # Manual check
    manual_slope = (np.log10(49000) - np.log10(4.9)) / (np.log10(100) - np.log10(1))
    print(f"Manual slope check: (log(49000)-log(4.9))/(log(100)-log(1)) = {manual_slope:.6f}")
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


class PowerLawLogLogScene(Scene):
    """
    Left: linear axes showing d=4.9t² (curved).
    Right: log-log axes — same data lands on a straight line, slope=2.
    Slope-measurement triangle appears. Sweep exponent n: slope changes.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_dual_axes()
        self._phase_slope_triangle()
        self._phase_exponent_sweep()

    def _phase_title(self):
        title = Text("Power Laws — Log-Log Straightening", font="EB Garamond", font_size=52, color=INK)
        sub1 = MathTex(r"y = a x^n \quad\Longrightarrow\quad \log y = n\log x + \log a", color=BLUE, font_size=30)
        sub2 = Text(
            "slope on log-log plot = exponent n",
            font="EB Garamond", font_size=24, color=GOLD,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(sub1), run_time=0.9)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_dual_axes(self):
        # ── LEFT: linear axes ────────────────────────────────────────────────
        ax_lin = Axes(
            x_range=[0, 105, 20],
            y_range=[0, 52000, 10000],
            x_length=5.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.15, include_numbers=False),
        ).shift(LEFT * 3.2 + DOWN * 0.3)

        hdr_lin = Text("Linear axes — curve", font="EB Garamond", font_size=19, color=DIM)
        hdr_lin.next_to(ax_lin, UP, buff=0.1)
        lbl_lin_x = MathTex(r"t\;(\mathrm{s})", color=DIM, font_size=18).next_to(ax_lin.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_lin_y = MathTex(r"d\;(\mathrm{m})", color=DIM, font_size=18).next_to(ax_lin.y_axis.get_end(), UP, buff=0.06)

        # ── RIGHT: log-log axes ──────────────────────────────────────────────
        # We draw on log10 scale manually: x in [0, 2], y in [0, 5]
        ax_log = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[0, 5.0, 1.0],
            x_length=5.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.15, include_numbers=True,
                             font_size=14, decimal_number_config={"color": DIM}),
        ).shift(RIGHT * 3.2 + DOWN * 0.3)

        hdr_log = Text("Log-log axes — straight line", font="EB Garamond", font_size=19, color=GOLD)
        hdr_log.next_to(ax_log, UP, buff=0.1)
        lbl_log_x = MathTex(r"\log_{10} t", color=DIM, font_size=18).next_to(ax_log.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_log_y = MathTex(r"\log_{10} d", color=DIM, font_size=18).next_to(ax_log.y_axis.get_end(), UP, buff=0.06)

        self.play(
            Create(ax_lin), Create(ax_log),
            Write(hdr_lin), Write(hdr_log),
            Write(lbl_lin_x), Write(lbl_lin_y),
            Write(lbl_log_x), Write(lbl_log_y),
            run_time=1.5,
        )

        # Plot linear curve d = 4.9 t² for t in [0, 100]
        t_lin = np.linspace(1, 100, 400)
        d_lin = freefall_d(t_lin)
        # Normalize to axes range (0-105, 0-52000)
        lin_pts = [ax_lin.c2p(t, d) for t, d in zip(t_lin, d_lin) if d <= 51000]
        lin_curve = VMobject(color=BLUE, stroke_width=2.5)
        lin_curve.set_points_smoothly(np.array(lin_pts))

        # Plot log-log line
        log_t = np.log10(T_VALS)
        log_d = np.log10(freefall_d(T_VALS))
        log_pts = [ax_log.c2p(lt, ld) for lt, ld in zip(log_t, log_d)]
        log_curve = VMobject(color=GOLD, stroke_width=2.8)
        log_curve.set_points_smoothly(np.array(log_pts))

        # Data dots
        lin_dots = VGroup(*[Dot(ax_lin.c2p(t, freefall_d(t)), color=GOLD, radius=0.08) for t in T_VALS])
        log_dots = VGroup(*[Dot(ax_log.c2p(np.log10(t), np.log10(freefall_d(t))), color=BLUE, radius=0.08) for t in T_VALS])

        caption = Text(
            "Same data: d = 4.9t²  —  curved on linear, straight on log-log",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.3)

        self.play(Create(lin_curve), Create(log_curve), run_time=1.5)
        self.play(FadeIn(lin_dots), FadeIn(log_dots), Write(caption), run_time=0.8)
        self.wait(1.5)

        # Store axes for later use
        self._ax_log = ax_log
        self._ax_lin = ax_lin

    def _phase_slope_triangle(self):
        ax = self._ax_log
        # Triangle: corner at (0, 0.69) to (2, 0.69) to (2, 4.69)
        # log10(4.9)=0.6902, log10(49000)=4.6902, delta_x=2, delta_y=4
        x1, y1 = 0.0, np.log10(4.9)
        x2, y2 = 2.0, np.log10(freefall_d(100))
        corner = [ax.c2p(x2, y1), ax.c2p(x1, y1), ax.c2p(x2, y2)]
        tri = Polygon(*corner, color=BROWN, stroke_width=2.0, fill_opacity=0.0)
        run_lbl = MathTex(r"\Delta\log t = 2", color=BROWN, font_size=18)
        run_lbl.next_to(ax.c2p(1.0, y1), DOWN, buff=0.1)
        rise_lbl = MathTex(r"\Delta\log d = 4", color=BROWN, font_size=18)
        rise_lbl.next_to(ax.c2p(x2, (y1 + y2) / 2), RIGHT, buff=0.1)
        slope_lbl = MathTex(r"\text{slope} = \frac{4}{2} = 2", color=GOLD, font_size=24)
        slope_lbl.to_edge(DOWN, buff=0.3)

        self.play(Create(tri), Write(run_lbl), Write(rise_lbl), run_time=1.0)
        self.play(Write(slope_lbl), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(tri, run_lbl, rise_lbl, slope_lbl), run_time=0.4)

    def _phase_exponent_sweep(self):
        ax = self._ax_log
        n_tracker = ValueTracker(2.0)

        def make_log_line():
            n = n_tracker.get_value()
            # y = log(a) + n·log(t), anchor at (t=1, d=4.9): log(a)=log10(4.9)
            log_a = np.log10(4.9)
            t_log_vals = np.linspace(0.0, 2.0, 80)
            d_log_vals = log_a + n * t_log_vals
            pts = np.array([ax.c2p(lt, ld) for lt, ld in zip(t_log_vals, d_log_vals)
                            if 0.0 <= ld <= 5.0])
            if len(pts) < 2:
                pts = np.array([ax.c2p(0.0, log_a), ax.c2p(0.1, log_a + n * 0.1)])
            m = VMobject(color=BLUE, stroke_width=3.0)
            m.set_points_smoothly(pts)
            return m

        dyn_line = always_redraw(make_log_line)
        slope_readout = always_redraw(
            lambda: MathTex(
                r"\text{slope (exponent) } n = " + f"{n_tracker.get_value():.2f}",
                color=GOLD, font_size=28,
            ).to_edge(DOWN, buff=0.3)
        )

        hdr = Text(
            "Sweep n: slope = exponent every time",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.3)

        self.play(FadeIn(dyn_line), Write(hdr), Write(slope_readout), run_time=0.8)
        self.play(n_tracker.animate.set_value(1.0), run_time=2.5, rate_func=smooth)
        self.wait(0.5)
        self.play(n_tracker.animate.set_value(3.0), run_time=3.0, rate_func=smooth)
        self.wait(0.5)
        self.play(n_tracker.animate.set_value(2.0), run_time=2.0, rate_func=smooth)
        self.wait(2.0)
        self.remove(dyn_line)
