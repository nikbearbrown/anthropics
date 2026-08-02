#!/usr/bin/env python3
"""
astro_hubble_diagram.py — Hubble Diagram: v=H0d and the Expanding Universe
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-hubble-diagram
    manim -qh astro_hubble_diagram.py HubbleDiagramScene

Verify:
    python3 astro_hubble_diagram.py

Physics:
    v = H0 d, H0 = 70 km/s/Mpc
    t_H = 1/H0 = 14.0 Gyr
    Galaxies: Virgo 16.5 Mpc, Coma 99 Mpc, etc.
    Hubble tension: local H0≈73 vs CMB H0≈67.4 km/s/Mpc
"""
import sys
import numpy as np

H0_KMS_MPC = 70.0    # km/s/Mpc (central estimate)
H0_LOCAL   = 73.0    # Riess et al. local measurement
H0_CMB     = 67.4    # Planck CMB measurement
MPC_M      = 3.085677e22    # metres per Mpc


def hubble_time_gyr(H0: float) -> float:
    """1/H0 in Gyr. H0 in km/s/Mpc."""
    H0_si = H0 * 1e3 / MPC_M   # 1/s  (convert km→m, /Mpc→/m)
    return 1.0 / H0_si / 3.15576e16   # Gyr (1 Gyr = 3.15576e16 s)


# Galaxy sample (name, d/Mpc, v/(km/s)) — from NED/public sources
GALAXIES = [
    ("M87 (Virgo)",    16.5,   1150.0),
    ("M49",            16.8,   997.0),
    ("M60",            16.5,   1117.0),
    ("NGC 4889 (Coma)",99.0,   6925.0),
    ("NGC 4874",       99.0,   7194.0),
    ("NGC 7619",       51.0,   3779.0),
    ("NGC 5457 (M101)",7.4,    241.0),
    ("NGC 3031 (M81)", 3.6,    -34.0),   # slightly blueshifted — peculiar velocity
    ("NGC 221 (M32)",  0.78,   -200.0),  # Local Group
    ("NGC 300",        2.08,   144.0),
]


def verify():
    print("=== Hubble diagram verification ===")
    print(f"H0 = {H0_KMS_MPC} km/s/Mpc")
    t_H = hubble_time_gyr(H0_KMS_MPC)
    print(f"Hubble time = {t_H:.2f} Gyr  (card says 14.0 Gyr)")

    # P1: Virgo at 16.5 Mpc
    v_virgo_pred = H0_KMS_MPC * 16.5
    print(f"\nP1: Virgo predicted v = {v_virgo_pred:.0f} km/s  (card says 1155, observed 1150)")

    # P2: Hubble time vs globular cluster ages
    t_local = hubble_time_gyr(H0_LOCAL)
    t_cmb   = hubble_time_gyr(H0_CMB)
    print(f"\nH0=73 → t_H = {t_local:.2f} Gyr")
    print(f"H0=67.4 → t_H = {t_cmb:.2f} Gyr")
    print("Oldest globular clusters: 13.5 Gyr — tension with H0=73 is real")
    print("=== PASSED ===" if abs(t_H - 14.0) < 0.3 else "=== CHECK ===")


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
RED_C  = "#FF6B6B"


class HubbleDiagramScene(Scene):
    """
    Hubble diagram: v (recession velocity) vs d (distance in Mpc).
    Galaxies appear one by one; best-fit line converges on H0.
    Hubble tension: two competing slope lines.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_hubble_plot()
        self._phase_tension()
        self._phase_payoff()

    def _phase_title(self):
        title = Text("Hubble Diagram — v = H₀ d", font="EB Garamond",
                     font_size=58, color=INK)
        sub1 = Text(
            "Every galaxy recedes. The farther, the faster. The slope is the age of the universe.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"t_H = 1/H_0 = 14\;\mathrm{Gyr}\quad H_0 = 70\;\mathrm{km/s/Mpc}",
                       color=BLUE, font_size=26)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_hubble_plot(self):
        ax = Axes(
            x_range=[0, 110, 20],
            y_range=[-500, 8000, 2000],
            x_length=8.5,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.3)
        lbl_x = MathTex(r"d\;(\mathrm{Mpc})", color=INK, font_size=40
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"v_r\;(\mathrm{km/s})", color=INK, font_size=40
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Hubble diagram — galaxies and clusters",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.3)

        # Zero velocity reference
        zero_line = DashedLine(ax.c2p(0, 0), ax.c2p(110, 0),
                               color=DIM, dash_length=0.08, stroke_width=1.5)
        self.play(Create(zero_line), run_time=0.5)

        # Hubble line H0=70
        d_line = np.linspace(0, 110, 200)
        v_line = H0_KMS_MPC * d_line
        c_H = VMobject(color=GOLD, stroke_width=2.5, stroke_opacity=0.0)
        c_H.set_points_smoothly([ax.c2p(d, v) for d, v in zip(d_line, v_line)])

        # Add points one by one
        colors_pts = [BLUE, BLUE, BLUE, BROWN, BROWN, DIM, DIM, DIM, DIM, DIM]
        all_pts = []
        all_ds, all_vs = [], []
        for i, (name, d, v) in enumerate(GALAXIES):
            dot = Dot(ax.c2p(d, v), radius=0.1, color=colors_pts[i % len(colors_pts)])
            lbl = Text(name.split("(")[0].strip(), font="EB Garamond", font_size=14,
                       color=colors_pts[i % len(colors_pts)]).next_to(dot, UR, buff=0.04)
            all_ds.append(d)
            all_vs.append(v)
            all_pts.append(VGroup(dot, lbl))

            if i == 0:
                self.play(FadeIn(dot), Write(lbl), run_time=0.7)
            else:
                # Update Hubble line with running fit
                if len(all_ds) >= 3:
                    slope, _ = np.polyfit(all_ds, all_vs, 1)
                    v_fit = slope * d_line
                    new_H = VMobject(color=GOLD, stroke_width=2.5, stroke_opacity=0.7)
                    new_H.set_points_smoothly([ax.c2p(d, v) for d, v in zip(d_line, v_fit)])
                    self.play(FadeIn(dot), Write(lbl),
                              Transform(c_H, new_H), run_time=0.6)
                    c_H.set_stroke(opacity=0.7)
                else:
                    self.play(FadeIn(dot), Write(lbl), run_time=0.6)

        # Final H0=70 line
        final_H = VMobject(color=GOLD, stroke_width=3.0)
        v_final = H0_KMS_MPC * d_line
        final_H.set_points_smoothly([ax.c2p(d, v) for d, v in zip(d_line, v_final)])
        self.play(Transform(c_H, final_H), run_time=0.8)

        H_lbl = MathTex(r"H_0 = 70\;\mathrm{km/s/Mpc}", color=GOLD, font_size=20
                        ).next_to(ax.c2p(100, H0_KMS_MPC * 100), UR, buff=0.04)
        self.play(Write(H_lbl), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_tension(self):
        ax = Axes(
            x_range=[0, 110, 20],
            y_range=[0, 9000, 2000],
            x_length=8.5,
            y_length=4.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"d\;(\mathrm{Mpc})", color=INK, font_size=40
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"v_r\;(\mathrm{km/s})", color=INK, font_size=40
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Hubble tension: two competing measurements of H₀",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        d_arr = np.linspace(0, 110, 200)

        for H0, color, lbl_str in [(H0_LOCAL, BLUE, f"H₀={H0_LOCAL} (local, Cepheids)"),
                                    (H0_CMB, BROWN, f"H₀={H0_CMB} (CMB, Planck)")]:
            c = VMobject(color=color, stroke_width=3.0)
            c.set_points_smoothly([ax.c2p(d, H0 * d) for d in d_arr])
            lbl = Text(lbl_str, font="EB Garamond", font_size=18, color=color)
            lbl.next_to(ax.c2p(100, H0 * 100), RIGHT, buff=0.04)
            self.add(c, lbl)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.1)
        self.play(*[FadeIn(m) for m in self.mobjects if m not in [ax, lbl_x, lbl_y, hdr]],
                  run_time=1.2)

        tension_lbl = Text(
            "4σ tension — systematic error or new physics?",
            font="EB Garamond", font_size=20, color=GOLD,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(tension_lbl), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_payoff(self):
        t_H = hubble_time_gyr(H0_KMS_MPC)
        eq = MathTex(
            rf"t_H = 1/H_0 = {t_H:.1f}\;\mathrm{{Gyr}}",
            color=INK, font_size=48,
        ).center().shift(UP * 1.0)
        note = Text(
            "Oldest globular clusters are 13.5 Gyr old — barely fits.",
            font="EB Garamond", font_size=21, color=DIM,
        ).next_to(eq, DOWN, buff=0.4)
        note2 = Text(
            "Hubble's 1929 diagram had 24 galaxies and distances off by 7×. The law was right.",
            font="EB Garamond", font_size=19, color=BLUE,
        ).next_to(note, DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
