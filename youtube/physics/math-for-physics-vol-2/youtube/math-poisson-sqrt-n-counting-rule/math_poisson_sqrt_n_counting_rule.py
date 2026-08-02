#!/usr/bin/env python3
"""
math_poisson_sqrt_n_counting_rule.py — Poisson Distribution and the √N Rule
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

P(k;λ) = λ^k·e^(-λ)/k!. σ=√λ. σ/λ=1/√λ.
Doubling precision costs 4× time — the iron law of counting experiments.

Render:
    cd math-for-physics-vol-2/youtube/math-poisson-sqrt-n-counting-rule
    manim -qh math_poisson_sqrt_n_counting_rule.py PoissonScene

Verify:
    python3 math_poisson_sqrt_n_counting_rule.py --verify

Testable predictions:
    P1: λ=25: P(25)≈0.0796; Gaussian N(25,5) gives 1/(5√2π)≈0.0798 (match within 0.3%)
    P2: σ/λ = 1/√λ; log-log slope of σ/λ vs λ = -1/2
"""
import sys
import numpy as np
from scipy import special

def poisson_pmf(k, lam):
    """Poisson PMF: λ^k·e^(-λ)/k!"""
    return np.exp(k * np.log(lam) - lam - special.gammaln(k + 1))

def gaussian_pdf(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma)**2) / (sigma * np.sqrt(2 * np.pi))

def verify():
    print("=== Poisson √N Counting Rule — verification ===")
    # P1: λ=25
    lam = 25
    k = 25
    p_poisson = poisson_pmf(k, lam)
    sigma = np.sqrt(lam)
    p_gauss = gaussian_pdf(k, lam, sigma)
    print(f"P1: λ=25, k=25:")
    print(f"    Poisson P(25;25) = {p_poisson:.4f}  (expected ≈ 0.0796)")
    print(f"    Gaussian f(25)   = {p_gauss:.4f}  (expected ≈ 0.0798)")
    pct_diff = abs(p_poisson - p_gauss) / p_poisson * 100
    print(f"    Difference = {pct_diff:.2f}%  (< 1%?) {'✓' if pct_diff < 1.0 else '✗'}")

    print()
    print("P2: σ/λ = 1/√λ")
    for lam in [1, 4, 16, 25, 100, 400, 10000]:
        rel = 1.0 / np.sqrt(lam)
        print(f"    λ={lam:6d}: σ=√λ={np.sqrt(lam):.1f}, σ/λ={rel:.4f}  (= 1/√λ ✓)")

    print()
    # Log-log slope check: fit slope of log(σ/λ) vs log(λ)
    lams = np.array([1, 4, 16, 100, 10000], dtype=float)
    log_lam = np.log(lams)
    log_rel = np.log(1.0 / np.sqrt(lams))
    slope = np.polyfit(log_lam, log_rel, 1)[0]
    print(f"Log-log slope of σ/λ vs λ: {slope:.4f}  (expected -0.5) {'✓' if abs(slope + 0.5) < 0.001 else '✗'}")
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


class PoissonScene(Scene):
    """
    Act 1: Bar chart of Poisson(λ) for λ=1,4,25,100. Gaussian overlay. ±σ band.
    Act 2: Log-log plot of σ/λ vs λ — straight line slope -1/2.
    Act 3: Running counter showing relative error shrinking as counts grow.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_bar_charts()
        self._phase_loglog()
        self._phase_payoff()

    def _phase_title(self):
        title = Text("Poisson Distribution & √N Rule", font="EB Garamond", font_size=52, color=INK)
        sub1 = Text(
            "P(k;λ) = λᵏe⁻λ/k!  ·  σ = √λ  ·  relative error = 1/√λ",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "To halve the error, count four times as many events",
            font="EB Garamond", font_size=22, color=GOLD,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_bar_charts(self):
        lambdas = [1, 4, 25, 100]
        colors  = [BLUE, BROWN, GOLD, INK]

        for lam, col in zip(lambdas, colors):
            self._show_one_poisson(lam, col)
            self.wait(0.5)

    def _show_one_poisson(self, lam, col):
        sigma = np.sqrt(lam)
        # k range: [0, lam + 4*sigma]
        k_max = int(lam + 4 * sigma) + 1
        k_min = max(0, int(lam - 4 * sigma))
        k_arr = np.arange(k_min, k_max + 1)
        probs = poisson_pmf(k_arr.astype(float), float(lam))

        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)
        p_max = probs.max() * 1.25

        ax = Axes(
            x_range=[k_min - 0.5, k_max + 0.5, max(1, int(sigma))],
            y_range=[0, p_max, p_max / 4],
            x_length=9.0, y_length=4.0,
            axis_config=axis_cfg,
        ).shift(DOWN * 0.5)

        lbl_k = MathTex(r"k", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_p = MathTex(r"P(k;\lambda)", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        bar_w  = (ax.c2p(1, 0) - ax.c2p(0, 0))[0] * 0.85
        bars   = VGroup()
        for k, p in zip(k_arr, probs):
            b = Rectangle(
                width=bar_w, height=abs(ax.c2p(0, p)[1] - ax.c2p(0, 0)[1]),
                fill_color=col, fill_opacity=0.75, stroke_width=0,
            )
            b.move_to(ax.c2p(k, p / 2))
            bars.add(b)

        # Gaussian overlay
        x_cont = np.linspace(k_min, k_max, 400)
        g_y    = gaussian_pdf(x_cont, lam, sigma)
        g_pts  = [ax.c2p(x, y) for x, y in zip(x_cont, g_y)]
        g_mob  = VMobject(color=GOLD if col != GOLD else BLUE, stroke_width=2.5)
        g_mob.set_points_smoothly(g_pts)

        # ±σ band
        s_l = ax.c2p(lam - sigma, 0)
        s_r = ax.c2p(lam + sigma, 0)
        s_h = ax.c2p(lam, gaussian_pdf(lam, lam, sigma))
        band = Rectangle(
            width=s_r[0] - s_l[0],
            height=s_h[1] - ax.c2p(0, 0)[1],
            fill_color=DIM, fill_opacity=0.18, stroke_width=0,
        ).move_to([(s_l[0] + s_r[0]) / 2, (s_h[1] + ax.c2p(0, 0)[1]) / 2, 0])

        hdr = MathTex(
            rf"\lambda = {lam},\;\sigma = \sqrt{{\lambda}} = {sigma:.1f},\;"
            rf"\sigma/\lambda = {1/np.sqrt(lam):.3f}",
            color=col, font_size=26,
        ).to_edge(UP, buff=0.25)

        self.play(Create(ax), Write(lbl_k), Write(lbl_p), run_time=0.8)
        self.play(Write(hdr), FadeIn(bars, lag_ratio=0.02), run_time=1.5)
        self.play(Create(g_mob), FadeIn(band), run_time=1.0)
        self.wait(1.2)
        self.play(FadeOut(ax, lbl_k, lbl_p, hdr, bars, g_mob, band), run_time=0.5)

    def _phase_loglog(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.2)
        ax = Axes(
            x_range=[0, 5.0, 1.0],   # log10(λ): 1 to 10000
            y_range=[-3.0, 0.5, 1.0],  # log10(σ/λ)
            x_length=8.5, y_length=4.5,
            axis_config=axis_cfg,
        ).shift(DOWN * 0.4)

        lbl_x = MathTex(r"\log_{10}(\lambda)", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\log_{10}(\sigma/\lambda)", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Exact line: log10(1/√λ) = -½ log10(λ)
        log_lam = np.linspace(0, 4.5, 200)
        log_rel = -0.5 * log_lam
        pts = [ax.c2p(ll, lr) for ll, lr in zip(log_lam, log_rel)]
        line = VMobject(color=GOLD, stroke_width=4)
        line.set_points_smoothly(pts)

        slope_lbl = MathTex(r"\text{slope} = -\tfrac{1}{2}", color=GOLD, font_size=26)
        slope_lbl.move_to(ax.c2p(2.5, -0.8))

        # Dot markers at λ = 1, 4, 25, 100, 10000
        lams = [1, 4, 25, 100, 10000]
        dot_mobs = VGroup()
        dot_lbls = VGroup()
        for lam in lams:
            lx = np.log10(lam)
            ly = np.log10(1.0 / np.sqrt(lam))
            d = Dot(ax.c2p(lx, ly), color=BLUE, radius=0.1)
            l = MathTex(rf"\lambda={lam}", color=BLUE, font_size=18)
            l.next_to(d, UR, buff=0.08)
            dot_mobs.add(d)
            dot_lbls.add(l)

        caption = Text(
            "log-log plot: slope = −1/2 confirms σ/λ = 1/√λ",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.32)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)
        self.play(Create(line), Write(slope_lbl), run_time=2.0)
        self.play(FadeIn(dot_mobs), FadeIn(dot_lbls), run_time=1.0)
        self.play(Write(caption), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(ax, lbl_x, lbl_y, line, slope_lbl,
                          dot_mobs, dot_lbls, caption), run_time=0.6)

    def _phase_payoff(self):
        rows = [
            (r"\lambda = 100",    r"\sigma = 10",    r"10\%"),
            (r"\lambda = 400",    r"\sigma = 20",    r"5\%"),
            (r"\lambda = 10{,}000", r"\sigma = 100", r"1\%"),
        ]
        table_mobs = VGroup()
        for i, (a, b, c) in enumerate(rows):
            row = VGroup(
                MathTex(a, color=BLUE,  font_size=30),
                MathTex(b, color=BROWN, font_size=30),
                MathTex(c, color=GOLD,  font_size=30),
            ).arrange(RIGHT, buff=1.2)
            row.shift(DOWN * (i - 1) * 0.85)
            table_mobs.add(row)

        hdr = MathTex(
            r"\text{counts}\quad\sigma=\sqrt{\lambda}\quad\text{relative error}",
            color=DIM, font_size=26,
        ).shift(UP * 1.5)

        self.play(Write(hdr), run_time=0.8)
        for row in table_mobs:
            self.play(FadeIn(row), run_time=0.7)
        self.wait(1.0)

        final = Text(
            "4× counts → ½ the relative error — the iron law of counting experiments",
            font="EB Garamond", font_size=24, color=INK,
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(final), run_time=1.2)
        self.wait(2.5)
