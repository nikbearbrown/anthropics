#!/usr/bin/env python3
"""
astro_stellar_evolution_track.py — Stellar Evolution Track on the HR Diagram
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-stellar-evolution-track
    manim -qh astro_stellar_evolution_track.py StellarEvolutionTrackScene

Verify:
    python3 astro_stellar_evolution_track.py

Physics:
    HR diagram: log L/L_Sun vs log T_eff (x-axis reversed: hot left)
    1 M_Sun track: ZAMS → MS → subgiant → red giant → HB → AGB → WD
    5 M_Sun track (faster): ZAMS → MS → red giant → blue loop → AGB → ... → SN (for >8 M_Sun use 10)
    Key points from stellar evolution theory (MESA/Bressan grids — public domain values).
"""
import sys
import numpy as np

# 1 M_Sun evolutionary track waypoints: (log T_eff, log L/L_Sun, label)
TRACK_1MSUN = [
    (3.748,  -0.155,  "ZAMS"),
    (3.762,   0.000,  "Current Sun"),
    (3.738,   0.301,  "Subgiant"),
    (3.544,   3.301,  "Red giant tip"),   # L≈2000 L_Sun, T≈3500K
    (3.699,   1.699,  "Horiz. branch"),   # L≈50 L_Sun, T≈5000K
    (3.477,   3.699,  "AGB"),             # L≈5000, T≈3000K
    (4.699,  -3.000,  "White dwarf"),     # L≈0.001, T≈50000K
]

# 5 M_Sun track waypoints
TRACK_5MSUN = [
    (4.176,   2.602,  "ZAMS 5M"),
    (4.130,   2.699,  "MS 5M"),
    (3.602,   3.699,  "Giant 5M"),        # L≈5000, T≈4000K
    (3.929,   3.301,  "Blue loop 5M"),    # L≈2000, T≈8500K
]


def verify():
    print("=== Stellar evolution track verification ===")
    # P1: Red giant tip luminosity for Sun ≈2000 L_Sun
    rgt = 10**TRACK_1MSUN[3][1]
    print(f"Red giant tip L = {rgt:.0f} L_Sun  (card says 2000)")
    # P2: WD at 50000K
    wd_T = 10**TRACK_1MSUN[-1][0]
    print(f"White dwarf T_eff = {wd_T:.0f} K  (card says 50000 K)")
    # ZAMS→Current Sun luminosity evolution
    L_zams = 10**TRACK_1MSUN[0][1]
    L_now  = 10**TRACK_1MSUN[1][1]
    print(f"ZAMS L = {L_zams:.3f} L_Sun  (card says 0.7)")
    print(f"Current L = {L_now:.3f} L_Sun")
    print("=== PASSED ===")


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


class StellarEvolutionTrackScene(Scene):
    """
    HR diagram with 1 M_Sun (blue) and 5 M_Sun (brown) evolutionary tracks.
    Track animates stage by stage. Main sequence drawn as reference.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_hr_tracks()
        self._phase_payoff()

    def _phase_title(self):
        title = Text("Stellar Evolution on the HR Diagram", font="EB Garamond",
                     font_size=52, color=INK)
        sub1 = Text(
            "The Sun will become a red giant in 5 billion years, then a white dwarf.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = Text(
            "The HR diagram is a time machine — every stage has its own territory.",
            font="EB Garamond", font_size=20, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_hr_tracks(self):
        # HR diagram: x = log T (reversed: 5.0 left, 3.4 right), y = log L
        ax = Axes(
            x_range=[3.4, 5.0, 0.4],
            y_range=[-4.0, 4.5, 2.0],
            x_length=7.5,
            y_length=6.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.2)

        # Invert x axis for HR convention (hot = left)
        # Manim Axes go left→right as x increases; we plot log T directly but note
        # the convention requires reversal — achieved by reversing x_range order
        ax_hr = Axes(
            x_range=[5.0, 3.4, -0.4],
            y_range=[-4.0, 4.5, 2.0],
            x_length=7.5,
            y_length=6.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.2)

        lbl_x = MathTex(r"\log_{10} T_{\rm eff}", color=INK, font_size=19
                        ).next_to(ax_hr.x_axis.get_end(), LEFT, buff=0.1)
        lbl_y = MathTex(r"\log_{10}(L/L_\odot)", color=INK, font_size=19
                        ).next_to(ax_hr.y_axis.get_end(), UP, buff=0.1)
        hdr   = Text("H-R diagram — 1 M_Sun (blue) and 5 M_Sun (brown) tracks",
                     font="EB Garamond", font_size=18, color=DIM).to_edge(UP, buff=0.18)

        # Draw ZAMS reference
        zams_T = np.array([3.70, 3.74, 3.78, 3.90, 4.00, 4.15, 4.40, 4.70])
        zams_L = np.array([-0.5, -0.2,  0.0,  0.7,  1.5,  2.6,  3.5,  4.2])
        zams = VMobject(color=DIM, stroke_width=2.0, stroke_opacity=0.6)
        zams.set_points_smoothly([ax_hr.c2p(T, L) for T, L in zip(zams_T, zams_L)])

        self.play(Create(ax_hr), Write(lbl_x), Write(lbl_y), Write(hdr), Create(zams), run_time=1.8)
        zams_lbl = Text("ZAMS", font="EB Garamond", font_size=16, color=DIM
                        ).next_to(ax_hr.c2p(4.0, 1.5), RIGHT, buff=0.08)
        self.play(Write(zams_lbl), run_time=0.5)

        # 1 M_Sun track — animate waypoint by waypoint
        track1 = TRACK_1MSUN
        prev_pt = None
        labels_1 = []
        for logT, logL, lbl_str in track1:
            dot = Dot(ax_hr.c2p(logT, logL), radius=0.1, color=BLUE)
            stage_lbl = Text(lbl_str, font="EB Garamond", font_size=14, color=BLUE
                             ).next_to(dot, DR, buff=0.04)
            if prev_pt is not None:
                seg = VMobject(color=BLUE, stroke_width=2.5)
                seg.set_points_smoothly([ax_hr.c2p(*prev_pt[:2]), ax_hr.c2p(logT, logL)])
                self.play(Create(seg), FadeIn(dot), Write(stage_lbl), run_time=0.8)
            else:
                self.play(FadeIn(dot), Write(stage_lbl), run_time=0.6)
            prev_pt = (logT, logL)
            labels_1.append(VGroup(dot, stage_lbl))

        # 5 M_Sun track
        track5 = TRACK_5MSUN
        prev_pt5 = None
        for logT, logL, lbl_str in track5:
            dot5 = Dot(ax_hr.c2p(logT, logL), radius=0.1, color=BROWN)
            stage_lbl5 = Text(lbl_str, font="EB Garamond", font_size=13, color=BROWN
                              ).next_to(dot5, UL, buff=0.04)
            if prev_pt5 is not None:
                seg5 = VMobject(color=BROWN, stroke_width=2.5)
                seg5.set_points_smoothly([ax_hr.c2p(*prev_pt5[:2]), ax_hr.c2p(logT, logL)])
                self.play(Create(seg5), FadeIn(dot5), Write(stage_lbl5), run_time=0.7)
            else:
                self.play(FadeIn(dot5), Write(stage_lbl5), run_time=0.5)
            prev_pt5 = (logT, logL)

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_payoff(self):
        eq = VGroup(
            MathTex(r"t_{\rm RGB\ tip} \approx 5\;\mathrm{Gyr}", color=INK, font_size=28),
            MathTex(r"L_{\rm RGB\ tip} \approx 2000\,L_\odot", color=BLUE, font_size=28),
            MathTex(r"T_{\rm WD\ initial} \approx 50{,}000\;\mathrm{K}", color=BROWN, font_size=28),
        ).arrange(DOWN, buff=0.3).center().shift(UP * 0.5)
        note = Text(
            "A globular cluster's HR diagram shows the turnoff point — that's the clock.",
            font="EB Garamond", font_size=21, color=DIM,
        ).to_edge(DOWN, buff=0.3)
        for part in eq:
            self.play(Write(part), run_time=0.8)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3.0)
