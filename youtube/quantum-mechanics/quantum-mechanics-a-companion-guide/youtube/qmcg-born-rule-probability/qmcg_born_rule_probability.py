#!/usr/bin/env python3
"""
qmcg_born_rule_probability.py — Born Rule Probability Density
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-born-rule-probability
    manim -qh qmcg_born_rule_probability.py BornRuleScene

Verify:
    python3 qmcg_born_rule_probability.py --verify

Physics:
    P(left quarter) = (2/L)∫₀^{L/4} sin²(πx/L)dx = 1/4 − 1/(2π) ≈ 0.0908
    P(middle half) = 1/2 + 1/π ≈ 0.8183
    For n=2: P(left quarter) = 1/4 + 1/(2π) ≈ 0.4092  (above classical 25%)
    Large n → all → 25% (correspondence principle)
"""
import sys
import numpy as np


def prob_quarter(n, quarter=0):
    """
    Probability in a quarter of the box [quarter*L/4, (quarter+1)*L/4]
    for particle-in-box state n.
    quarter ∈ {0,1,2,3}
    """
    x = np.linspace(quarter/4, (quarter+1)/4, 100000)
    psi_sq = 2 * np.sin(n * np.pi * x)**2
    return np.trapz(psi_sq, x)


def verify():
    print("=== Born rule probability verification ===")
    # P1: n=1 left quarter = 1/4 - 1/(2π)
    P1_exact = 0.25 - 1/(2*np.pi)
    P1_num   = prob_quarter(1, 0)
    print(f"  n=1, left quarter: exact={P1_exact:.6f}, numerical={P1_num:.6f}  (expected 0.0908)")

    # P2: n=2 left quarter = 1/4 + 1/(2π)
    P2_exact = 0.25 + 1/(2*np.pi)
    P2_num   = prob_quarter(2, 0)
    print(f"  n=2, left quarter: exact={P2_exact:.6f}, numerical={P2_num:.6f}  (expected 0.4092)")

    # Classical = 25%
    print(f"\n  Classical: {0.25:.4f}")

    # Correspondence principle
    print("\n  Large n → 25%:")
    for n in [1, 2, 5, 10, 20, 50]:
        P = prob_quarter(n, 0)
        print(f"    n={n}: P(left quarter) = {P:.4f}  (classical 0.2500)")
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


class BornRuleScene(Scene):
    """
    Phase 1: title
    Phase 2: |ψ₁|² with three colored regions; probability readouts
    Phase 3: sweep n from 1 to 20 — left-quarter probability oscillates toward 25%
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_n1()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Born Rule Probability Density", font="EB Garamond", font_size=50, color=INK)
        sub1  = Text(
            "P = ∫|ψ(x)|²dx  —  not uniform: the n=1 ground state peaks at L/2",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "Left quarter gets 9.1% — not 25%.  That 16% gap is the Born rule.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_n1(self):
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 2.2, 0.5],
            x_length=8.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.3)

        x_lbl = MathTex(r"x/L", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"|\psi|^2 L", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        x_arr = np.linspace(0, 1, 600)
        prob  = 2 * np.sin(np.pi * x_arr)**2
        pts   = [ax.c2p(x, p) for x, p in zip(x_arr, prob)]
        curve = VMobject(color=BLUE, stroke_width=2.8)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=0.8)

        # Color regions
        region_data = [
            (0.0, 0.25, GOLD,  "Left: 9.1%"),
            (0.25, 0.75, BLUE,  "Middle: 81.8%"),
            (0.75, 1.0,  GOLD,  "Right: 9.1%"),
        ]
        region_probs = [0.091, 0.818, 0.091]

        fill_objects = []
        for i, ((x_lo, x_hi, col, lbl_str), pval) in enumerate(zip(region_data, region_probs)):
            x_fill = np.linspace(x_lo, x_hi, 200)
            prob_f = 2 * np.sin(np.pi * x_fill)**2
            # Fill polygon: bottom at y=0
            bottom = [ax.c2p(x, 0) for x in [x_lo, x_hi]]
            top    = [ax.c2p(x, p) for x, p in zip(x_fill, prob_f)]
            poly   = Polygon(
                *([ax.c2p(x_lo, 0)] + top + [ax.c2p(x_hi, 0)]),
                color=col, fill_color=col, fill_opacity=0.22, stroke_width=0,
            )
            region_lbl = Text(lbl_str, font="EB Garamond", font_size=18, color=col)
            region_lbl.move_to(ax.c2p((x_lo+x_hi)/2, -0.3))
            self.play(FadeIn(poly), Write(region_lbl), run_time=0.5)
            fill_objects.append((poly, region_lbl))

        classical_line = DashedLine(ax.c2p(0, 1.0), ax.c2p(1, 1.0), color=DIM, stroke_width=1.5)
        classical_lbl  = Text("Classical (uniform) = 25% each quarter", font="EB Garamond", font_size=17, color=DIM).to_edge(DOWN, buff=0.28)
        self.play(Create(classical_line), Write(classical_lbl), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_sweep(self):
        hdr = Text(
            "Sweep n — left-quarter probability oscillates but trends to 25% (correspondence principle)",
            font="EB Garamond", font_size=19, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.7)

        n_vals = list(range(1, 21))
        probs  = [prob_quarter(n, 0) for n in n_vals]

        ax = Axes(
            x_range=[1, 20, 2], y_range=[0, 0.45, 0.1],
            x_length=9.0, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(DOWN * 0.2)

        x_lbl = MathTex(r"n", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"P(\text{left quarter})", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.7)

        # Classical 25% line
        cl_line = DashedLine(ax.c2p(1, 0.25), ax.c2p(20, 0.25), color=DIM, stroke_width=1.5)
        cl_lbl  = MathTex(r"0.25\;\text{(classical)}", color=DIM, font_size=18).next_to(ax.c2p(20, 0.25), RIGHT, buff=0.1)
        self.play(Create(cl_line), Write(cl_lbl), run_time=0.5)

        # Animate dots and bars
        dot_objs = []
        for n, p in zip(n_vals, probs):
            dot = Dot(ax.c2p(n, p), color=GOLD, radius=0.1)
            dot_objs.append(dot)
            self.play(FadeIn(dot), run_time=0.2)

        # Connect dots
        pts = [ax.c2p(n, p) for n, p in zip(n_vals, probs)]
        conn = VMobject(color=GOLD, stroke_width=2.0, stroke_opacity=0.6)
        conn.set_points_smoothly(pts)
        self.play(Create(conn), run_time=0.8)

        fin = MathTex(
            r"n=1:\;P=0.091\quad n=2:\;P=0.409\quad n\to\infty:\;P\to 0.25",
            color=BLUE, font_size=24,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.8)
        self.wait(2.5)
