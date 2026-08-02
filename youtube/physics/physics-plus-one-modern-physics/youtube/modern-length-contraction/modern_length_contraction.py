#!/usr/bin/env python3
"""
modern_length_contraction.py — Length Contraction: The Muon's Atmosphere Is Only 0.52 km Thick
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-modern-physics book.

Render:
    cd physics-plus-one-modern-physics/youtube/modern-length-contraction
    manim -qh modern_length_contraction.py LengthContractionScene

Physics:
    L = L0/γ = L0 * sqrt(1 - β²)
    Muon: β=0.9994, γ=28.9
    L0 = 15 km (atmosphere, Earth frame)
    L = 15/28.9 = 0.519 km (muon frame)
    Travel time in muon frame: 0.519 km / 0.9994c = 1.73 μs < 2.2 μs  ✓
"""
import sys
import numpy as np

C_LIGHT = 3.0e8
BETA    = 0.9994
GAMMA   = 1.0 / np.sqrt(1 - BETA**2)
L0_KM   = 15.0
L_KM    = L0_KM / GAMMA
T_REST  = 2.2e-6   # s
T_TRAVEL_MUON = L_KM * 1e3 / (BETA * C_LIGHT)


if __name__ == "__main__":
    print("=== Length Contraction Verification ===")
    print(f"γ = {GAMMA:.2f}")
    print(f"P1: L = {L0_KM} km / {GAMMA:.2f} = {L_KM:.3f} km  (expect 0.52 km)")
    assert abs(L_KM - 0.519) < 0.01, f"P1 FAIL: {L_KM:.3f}"
    print(f"P2: travel time in muon frame = {T_TRAVEL_MUON*1e6:.2f} μs  (expect < 2.2 μs)")
    assert T_TRAVEL_MUON < T_REST, "P2 FAIL"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class LengthContractionScene(Scene):
    """Split screen: Earth frame (L0=15km) vs muon frame (L=0.52km)."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_split_screen()
        self._phase_formula()
        self._phase_ruler()

    def _phase_title(self):
        title = Text("Length Contraction", font="EB Garamond", font_size=58, color=INK)
        sub = Text("In the muon's frame, the atmosphere is only 0.52 km thick",
                   font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_split_screen(self):
        # Divider
        div = Line(UP * 3.5, DOWN * 3.5, color=DIM, stroke_width=1.0)

        # Earth frame (left)
        earth_hdr = Text("Earth Frame", font="EB Garamond",
                         font_size=24, color=BLUE).move_to(LEFT * 3.3 + UP * 3.0)
        atm_bar = Rectangle(width=0.4, height=3.5, color=BLUE, fill_color=BLUE,
                            fill_opacity=0.3).move_to(LEFT * 3.3 + UP * 0.5)
        atm_lbl = Text("L₀ = 15 km", font="EB Garamond",
                       font_size=20, color=BLUE).next_to(atm_bar, RIGHT, buff=0.15)
        muon_e = Dot(LEFT * 3.3 + UP * 3.5, color=GOLD, radius=0.15)
        muon_e_lbl = Text("muon", font="EB Garamond",
                          font_size=16, color=GOLD).next_to(muon_e, RIGHT, buff=0.08)
        tau_e = MathTex(r"\Delta t=63.5\,\mu\mathrm{s}", color=GOLD, font_size=20
                        ).next_to(atm_bar, DOWN, buff=0.15)

        # Muon frame (right)
        muon_hdr = Text("Muon Frame", font="EB Garamond",
                        font_size=24, color=GOLD).move_to(RIGHT * 3.3 + UP * 3.0)
        atm_bar_m = Rectangle(width=0.4, height=0.52 * 3.5 / 15, color=BLUE,
                              fill_color=BLUE, fill_opacity=0.3
                              ).move_to(RIGHT * 3.3 + UP * 0.5)
        atm_lbl_m = Text("L = 0.52 km", font="EB Garamond",
                         font_size=20, color=GOLD).next_to(atm_bar_m, RIGHT, buff=0.15)
        sea_level = Line(RIGHT * 1.8, RIGHT * 4.8, color=DIM, stroke_width=1.5
                         ).move_to(RIGHT * 3.3 + DOWN * 1.2)
        tau_m = MathTex(r"\Delta t_0=2.2\,\mu\mathrm{s}", color=GOLD, font_size=20
                        ).next_to(atm_bar_m, DOWN, buff=0.15)
        survive = Text("muon survives (1.73 μs < 2.2 μs)", font="EB Garamond",
                       font_size=16, color=GOLD).next_to(sea_level, DOWN, buff=0.15)

        self.play(Create(div), run_time=0.4)
        self.play(Write(earth_hdr), Write(muon_hdr), run_time=0.6)
        self.play(FadeIn(atm_bar), Write(atm_lbl), FadeIn(muon_e), Write(muon_e_lbl), run_time=0.8)
        self.play(Write(tau_e), run_time=0.5)
        self.play(FadeIn(atm_bar_m), Write(atm_lbl_m), Create(sea_level), run_time=0.8)
        self.play(Write(tau_m), Write(survive), run_time=0.7)
        # Animate muon falling in Earth frame
        self.play(muon_e.animate.move_to(LEFT * 3.3 + DOWN * 0.0), run_time=2.0)
        agree = Text("Both frames: muon reaches sea level", font="EB Garamond",
                     font_size=20, color=INK).to_edge(DOWN, buff=0.25)
        self.play(Write(agree), run_time=0.8)
        self.wait(2.0)
        all_mobs = [div, earth_hdr, muon_hdr, atm_bar, atm_lbl, muon_e, muon_e_lbl,
                    tau_e, atm_bar_m, atm_lbl_m, sea_level, tau_m, survive, agree, muon_e]
        self.play(FadeOut(*all_mobs), run_time=0.5)

    def _phase_formula(self):
        rows = [
            MathTex(r"L=\frac{L_0}{\gamma}=L_0\sqrt{1-\beta^2}", color=BLUE, font_size=36),
            MathTex(r"L=\frac{15\,\mathrm{km}}{28.9}=0.52\,\mathrm{km}", color=GOLD, font_size=34),
            MathTex(r"t_{\rm travel}=\frac{0.52\,\mathrm{km}}{0.9994c}=1.73\,\mu\mathrm{s}<2.2\,\mu\mathrm{s}",
                    color=INK, font_size=28),
        ]
        VGroup(*rows).arrange(DOWN, buff=0.55).center()
        for r in rows:
            self.play(Write(r), run_time=1.0)
            self.wait(0.5)
        self.wait(2.0)
        self.play(FadeOut(*rows), run_time=0.5)

    def _phase_ruler(self):
        # Animate a ruler being length-contracted as β increases
        beta_t = ValueTracker(0.01)

        def _ruler():
            beta = beta_t.get_value()
            gam  = 1.0 / np.sqrt(1 - beta**2)
            L    = 5.0 / gam   # normalized, 5.0 = rest length in scene units
            bar  = Rectangle(width=max(L, 0.05), height=0.35,
                             color=BLUE, fill_color=BLUE, fill_opacity=0.4)
            return bar

        dyn = always_redraw(_ruler)
        self.add(dyn)

        beta_lbl = MathTex(r"\beta = ", color=DIM, font_size=30)
        beta_num = DecimalNumber(0.01, num_decimal_places=4, color=DIM, font_size=30)
        beta_num.add_updater(lambda m: m.set_value(beta_t.get_value()))
        row = VGroup(beta_lbl, beta_num).arrange(RIGHT, buff=0.08).to_edge(DOWN, buff=0.3)

        hdr = Text("Ruler contracts as β → 1", font="EB Garamond",
                   font_size=24, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), FadeIn(row), run_time=0.8)
        self.play(beta_t.animate.set_value(0.9994), run_time=5.0, rate_func=smooth)
        self.wait(1.5)
        final = Text("Length contraction and time dilation are the same event — two frames",
                     font="EB Garamond", font_size=22, color=INK).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(row), Write(final), run_time=1.2)
        self.wait(2.5)
