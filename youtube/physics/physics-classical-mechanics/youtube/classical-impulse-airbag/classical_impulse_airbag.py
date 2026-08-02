#!/usr/bin/env python3
"""
classical_impulse_airbag.py — Impulse and the Airbag: Same Δp, Longer Δt, Smaller Force
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    J = F·Δt = Δp = m·v₀ = 75×15 = 1125 N·s
    Dashboard Δt=0.01 s → F=112,500 N ≈ 153 g
    Airbag   Δt=0.15 s → F=7,500 N ≈ 10 g

Render:
    cd physics-classical-mechanics/youtube/classical-impulse-airbag
    manim -qh classical_impulse_airbag.py ImpulseAirbagScene
"""
import sys
import numpy as np

M    = 75.0   # kg
V0   = 15.0   # m/s
G    = 9.80   # m/s²
DP   = M * V0  # N·s = 1125

SCENARIOS = [
    ("Dashboard",  0.01,  "#CD853F"),
    ("Seat belt",  0.08,  "#8A8780"),
    ("Airbag",     0.15,  "#58C4DD"),
]
INJURY_G = 35.0


def avg_force(dt): return DP / dt
def g_force(dt):   return avg_force(dt) / (M * G)


def verify():
    print("=== Impulse Airbag verification ===")
    print(f"  Δp = m×v₀ = {DP:.1f} N·s")
    for name, dt, _ in SCENARIOS:
        F   = avg_force(dt)
        gf  = g_force(dt)
        print(f"  {name} (Δt={dt:.2f}s): F_avg={F:.1f} N = {gf:.1f} g")
    # P1: integral check
    for name, dt, _ in SCENARIOS:
        integral = avg_force(dt) * dt
        err = abs(integral - DP)
        print(f"  ∫F dt = {integral:.2f} N·s (expected {DP:.1f}, err={err:.4f})")
        assert err < 1e-8, f"P1 failed for {name}"
    # P2: ratio of forces airbag vs seatbelt = 8/15
    F_airbag  = avg_force(0.15)
    F_seatbelt = avg_force(0.08)
    print(f"  F_airbag/F_seatbelt = {F_airbag/F_seatbelt:.4f}  (expected {8/15:.4f} = 8/15)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class ImpulseAirbagScene(Scene):
    """Three F-t panels side by side; same area (Δp), different peaks; injury threshold."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._ft_panels()

    def _title(self):
        t1 = Text("Impulse and the Airbag", font="EB Garamond", font_size=58, color=INK)
        t2 = Text("Same Δp — fifteen times longer Δt — fifteen times smaller force",
                  font="EB Garamond", font_size=23, color=DIM)
        t3 = MathTex(r"J = F\Delta t = \Delta p = m v_0 = 1125\,\mathrm{N\cdot s}",
                     color=GOLD, font_size=28)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _ft_panels(self):
        """Three side-by-side F-t plots."""
        panel_positions = [LEFT*4.2, ORIGIN, RIGHT*4.2]
        x_end = 0.20  # s common x range for display
        F_max_display = 120000

        axes_all = []
        for (name, dt, col), pos in zip(SCENARIOS, panel_positions):
            ax = Axes(
                x_range=[0, x_end, 0.05],
                y_range=[0, F_max_display, 30000],
                x_length=3.6,
                y_length=4.2,
                axis_config=dict(color=INK, stroke_width=1.2, include_ticks=True, tip_length=0.15),
            ).move_to(pos + DOWN*0.3)
            lx = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=14).next_to(ax.x_axis.get_end(), RIGHT, buff=0.04)
            ly = MathTex(r"F\;(\mathrm{N})", color=INK, font_size=14).next_to(ax.y_axis.get_end(), UP, buff=0.04)
            hdr = Text(name, font="EB Garamond", font_size=18, color=col).next_to(ax, UP, buff=0.12)
            self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=0.6)

            # Rectangular force pulse
            F_avg = avg_force(dt)
            F_clipped = min(F_avg, F_max_display * 0.95)
            rect = Polygon(
                ax.c2p(0, 0), ax.c2p(dt, 0), ax.c2p(dt, F_clipped), ax.c2p(0, F_clipped),
                color=col, fill_color=col, fill_opacity=0.35, stroke_width=2
            )
            self.play(FadeIn(rect), run_time=0.5)

            # Area label (Δp)
            area_lbl = MathTex(r"1125\,\mathrm{N\cdot s}", color=col, font_size=14)
            area_lbl.move_to(ax.c2p(dt/2, F_clipped/3))
            self.play(Write(area_lbl), run_time=0.3)

            # g-force label
            gf = g_force(dt)
            gf_lbl = Text(f"{gf:.0f} g", font="EB Garamond", font_size=16, color=col)
            gf_lbl.next_to(ax.c2p(dt, F_clipped), UR, buff=0.05)
            self.play(Write(gf_lbl), run_time=0.3)

            axes_all.append(ax)

        # Injury threshold horizontal line across all panels
        for ax, (name, dt, col) in zip(axes_all, SCENARIOS):
            F_injury = INJURY_G * M * G
            if F_injury < F_max_display:
                dash = DashedLine(
                    ax.c2p(0, F_injury), ax.c2p(x_end, F_injury),
                    color=GOLD, stroke_width=1.5, dash_length=0.12
                )
                self.play(Create(dash), run_time=0.3)

        threshold_lbl = Text("── 35 g injury threshold",
                             font="EB Garamond", font_size=17, color=GOLD).to_edge(DOWN, buff=0.42)
        final = Text(
            "Same area (= Δp) every time — only the peak force changes",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.18)
        self.play(Write(threshold_lbl), Write(final), run_time=0.8)
        self.wait(2.5)
