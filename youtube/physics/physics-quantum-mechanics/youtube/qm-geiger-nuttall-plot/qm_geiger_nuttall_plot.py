#!/usr/bin/env python3
"""
qm_geiger_nuttall_plot.py — Geiger-Nuttall: 24 Decades of Half-Life from One Line
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-geiger-nuttall-plot
    manim -qh qm_geiger_nuttall_plot.py GeigerNuttallScene

Verify:
    python3 qm_geiger_nuttall_plot.py

Physics:
    Data from published nuclear data tables (public domain).
    Geiger-Nuttall: log10(t_1/2/s) = A/sqrt(E_alpha/MeV) + B
    Nuclides used (Z~82-92 range, known half-lives):
    232Th, 238U, 226Ra, 222Rn, 210Po, 214Po, 212Po
    Gamow factor G ≈ π Z1 Z2 e² / (ℏ v_alpha)
"""
import sys
import numpy as np

# Alpha-emitter data: (nuclide, Z, E_alpha/MeV, t_half/s, log10(t_half/s))
ALPHA_DATA = [
    ("²³²Th", 90, 4.082, 1.405e17, np.log10(1.405e17)),   # 4.45e9 yr
    ("²³⁸U",  92, 4.270, 1.410e17, np.log10(1.410e17)),   # 4.47e9 yr
    ("²²⁶Ra", 88, 4.871, 5.055e10, np.log10(5.055e10)),   # 1602 yr
    ("²²²Rn", 86, 5.590, 3.303e5,  np.log10(3.303e5)),    # 3.82 days
    ("²¹⁰Po", 84, 5.307, 1.194e7,  np.log10(1.194e7)),    # 138 days
    ("²¹⁴Po", 84, 7.687, 1.643e-4, np.log10(1.643e-4)),   # 164 μs
    ("²¹²Po", 84, 8.785, 2.99e-7,  np.log10(2.99e-7)),    # 299 ns
]


def gn_fit(data):
    """Linear fit: log10(t_half) = A / sqrt(E) + B."""
    x = np.array([1.0 / np.sqrt(d[2]) for d in data])
    y = np.array([d[4] for d in data])
    A, B = np.polyfit(x, y, 1)
    return A, B


def verify():
    print("=== Geiger-Nuttall plot verification ===")
    for name, Z, E, t, log_t in ALPHA_DATA:
        print(f"  {name}: E={E:.3f} MeV, t1/2={t:.3e} s, log10={log_t:.2f}")

    A, B = gn_fit(ALPHA_DATA)
    print(f"\nGN fit: A = {A:.2f} MeV^0.5, B = {B:.2f}")
    print(f"Span: log10 from {min(d[4] for d in ALPHA_DATA):.1f} to {max(d[4] for d in ALPHA_DATA):.1f}")
    span = max(d[4] for d in ALPHA_DATA) - min(d[4] for d in ALPHA_DATA)
    print(f"Decade span: {span:.1f}  (card says 24 decades)")

    # P2: 0.43 MeV increase (Ra226 → Po210) → ~4 orders of magnitude
    t_ra = dict((d[0], d) for d in ALPHA_DATA)["²²⁶Ra"]
    t_po = dict((d[0], d) for d in ALPHA_DATA)["²¹⁰Po"]
    ratio = t_ra[3] / t_po[3]
    print(f"\nRa226/Po210 half-life ratio: {ratio:.0f}× ≈ 10^{np.log10(ratio):.1f}  (card says ~4 orders)")
    print("=== PASSED ===" if span > 20 else "=== CHECK ===")


if __name__ == "__main__":
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


class GeigerNuttallScene(Scene):
    """
    Geiger-Nuttall plot: log t_{1/2} vs 1/sqrt(E_alpha).
    Data points appear one by one; best-fit line extends to meet each.
    24-decade span annotated.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_gn_plot()
        self._phase_gamow_connection()

    def _phase_title(self):
        title = Text("Geiger-Nuttall Law", font="EB Garamond", font_size=60, color=INK)
        sub1 = Text(
            "24 orders of magnitude of half-lives collapse onto one straight line.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"\log_{10} t_{1/2} = \frac{A}{\sqrt{E_\alpha}} + B",
                       color=BLUE, font_size=30)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_gn_plot(self):
        A_fit, B_fit = gn_fit(ALPHA_DATA)

        # Axis ranges
        x_vals = [1.0 / np.sqrt(d[2]) for d in ALPHA_DATA]
        y_vals = [d[4] for d in ALPHA_DATA]
        x_min, x_max = 0.33, 0.51
        y_min, y_max = -8.0, 18.0

        ax = Axes(
            x_range=[x_min, x_max, 0.04],
            y_range=[y_min, y_max, 5.0],
            x_length=8.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.1)
        lbl_x = MathTex(r"E_\alpha^{-1/2}\;(\mathrm{MeV}^{-1/2})", color=INK, font_size=19
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        lbl_y = MathTex(r"\log_{10}(t_{1/2}/\mathrm{s})", color=INK, font_size=19
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Geiger-Nuttall plot — alpha emitters (Z=84–92)",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.2)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.5)

        # GN line (running fit)
        x_line = np.linspace(x_min, x_max, 200)
        colors_pts = [BLUE, GOLD, BROWN, BLUE, GOLD, BROWN, DIM]

        # Draw points one by one, updating best-fit line
        all_pts_x = []
        all_pts_y = []
        gn_line_obj = None

        for i, (name, Z, E, t, log_t) in enumerate(ALPHA_DATA):
            x_pt = 1.0 / np.sqrt(E)
            y_pt = log_t
            all_pts_x.append(x_pt)
            all_pts_y.append(y_pt)

            dot = Dot(ax.c2p(x_pt, y_pt), radius=0.12, color=colors_pts[i])
            # Label: name + half-life order
            hl_str = f"{name}"
            dot_lbl = Text(hl_str, font="EB Garamond", font_size=16, color=colors_pts[i]
                           ).next_to(dot, UR, buff=0.04)

            if len(all_pts_x) >= 2:
                fit_A, fit_B = np.polyfit(1.0 / np.sqrt(np.array(
                    [d[2] for d in ALPHA_DATA[:i+1]])), all_pts_y, 1)
                y_line = fit_A * x_line + fit_B
                new_line = VMobject(color=GOLD, stroke_width=2.5, stroke_opacity=0.7)
                new_line.set_points_smoothly([ax.c2p(x, y) for x, y in zip(x_line, y_line)])
                if gn_line_obj is None:
                    gn_line_obj = new_line
                    self.play(FadeIn(dot), Write(dot_lbl), Create(gn_line_obj), run_time=1.0)
                else:
                    self.play(FadeIn(dot), Write(dot_lbl),
                              Transform(gn_line_obj, new_line), run_time=0.9)
            else:
                self.play(FadeIn(dot), Write(dot_lbl), run_time=0.8)

        # Annotate 24-decade span
        span_line = DashedLine(
            ax.c2p(x_vals[-1] - 0.005, y_vals[-1]),
            ax.c2p(x_vals[-1] - 0.005, y_vals[0]),
            color=INK, dash_length=0.08, stroke_width=1.5,
        )
        span_lbl = MathTex(r"24\ \text{decades}", color=INK, font_size=20
                           ).next_to(ax.c2p(x_vals[-1] - 0.005, (y_vals[0] + y_vals[-1]) / 2), LEFT, buff=0.1)
        self.play(Create(span_line), Write(span_lbl), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, gn_line_obj, span_line, span_lbl,
                          *self.mobjects), run_time=0.5)

    def _phase_gamow_connection(self):
        eq = MathTex(
            r"T \approx e^{-2G},\quad G \approx \frac{\pi Z_1 Z_2 e^2}{\hbar v_\alpha}",
            color=INK, font_size=30,
        ).center().shift(UP * 0.8)
        eq2 = MathTex(
            r"\Rightarrow \log t_{1/2} \propto \frac{Z}{\sqrt{E_\alpha}}",
            color=BLUE, font_size=28,
        ).next_to(eq, DOWN, buff=0.4)
        note = Text(
            "Geiger-Nuttall (1911) found the line empirically.\n"
            "Gamow (1928, age 24) derived it from quantum tunneling.",
            font="EB Garamond", font_size=20, color=DIM,
        ).next_to(eq2, DOWN, buff=0.45)
        self.play(Write(eq), run_time=1.0)
        self.play(Write(eq2), run_time=1.0)
        self.play(FadeIn(note), run_time=0.9)
        self.wait(3.0)
