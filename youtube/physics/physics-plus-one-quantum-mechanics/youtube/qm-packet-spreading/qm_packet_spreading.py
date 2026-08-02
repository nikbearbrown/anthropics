#!/usr/bin/env python3
"""
qm_packet_spreading.py — Free Packet Spreading: σ_x(t) Grows as √(1 + (t/t_spread)²)
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-quantum-mechanics book.

Render:
    cd physics-plus-one-quantum-mechanics/youtube/qm-packet-spreading
    manim -qh qm_packet_spreading.py PacketSpreadingScene

Physics:
    σ_x(t) = σ_0 √(1 + (t/t_spread)²)
    t_spread = 2m σ_0² / ℏ
    Electron, σ_0=1nm: t_spread = 2×9.109e-31×(1e-9)²/1.055e-34 = 17.3 fs
    At t=t_spread: σ_x = √2 × σ_0 = 1.41 nm
    Proton: t_spread × 1836 = 31.8 ps
"""
import sys
import numpy as np

HBAR   = 1.055e-34
M_ELEC = 9.109e-31
M_PROT = 1.673e-27
SIGMA0 = 1.0e-9     # 1 nm


def t_spread(sigma0, m):
    return 2 * m * sigma0**2 / HBAR


def sigma_x(t, sigma0, m):
    ts = t_spread(sigma0, m)
    return sigma0 * np.sqrt(1 + (t / ts)**2)


if __name__ == "__main__":
    print("=== Wave Packet Spreading Verification ===")
    ts_e = t_spread(SIGMA0, M_ELEC)
    ts_p = t_spread(SIGMA0, M_PROT)
    print(f"t_spread (electron) = {ts_e*1e15:.1f} fs  (expect 17.3 fs)")
    print(f"t_spread (proton)   = {ts_p*1e12:.2f} ps  (expect 31.8 ps)")
    assert abs(ts_e - 17.3e-15) < 0.5e-15, f"FAIL: {ts_e*1e15:.1f} fs"
    # P1: at t=t_spread, σ_x = √2 σ_0
    sx = sigma_x(ts_e, SIGMA0, M_ELEC)
    print(f"P1: σ_x(t_spread) = {sx*1e9:.3f} nm  (expect {np.sqrt(2):.3f} nm)")
    assert abs(sx - np.sqrt(2) * SIGMA0) < 1e-12, "P1 FAIL"
    # P2: proton spreads 1836x slower
    ratio = ts_p / ts_e
    print(f"P2: t_spread ratio proton/electron = {ratio:.0f}  (expect 1836)")
    assert abs(ratio - M_PROT/M_ELEC) < 5, "P2 FAIL"
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

TS_ELEC = t_spread(SIGMA0, M_ELEC) if False else 17.3e-15
TS_PROT = t_spread(SIGMA0, M_PROT) if False else 31.8e-12


def spread_scene_sigma(t_over_ts):
    return np.sqrt(1 + t_over_ts**2)  # normalized units


class PacketSpreadingScene(Scene):
    """Gaussian spreading + σ_x(t) curve + proton comparison."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_spreading()
        self._phase_sigma_curve()

    def _phase_title(self):
        title = Text("Free Wave Packet Spreading", font="EB Garamond",
                     font_size=52, color=INK)
        sub = MathTex(r"\sigma_x(t)=\sigma_0\sqrt{1+(t/t_{\rm spread})^2}",
                      color=BLUE, font_size=32)
        sub2 = Text("Narrow → wide: the uncertainty principle evolving in time",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_spreading(self):
        t_track = ValueTracker(0.01)

        ax = Axes(
            x_range=[-6, 6, 2],
            y_range=[0, 1.2, 0.5],
            x_length=9.5,
            y_length=3.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(UP * 0.5)
        x_lbl = MathTex(r"x\;(\sigma_0)", color=INK, font_size=22).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"|\psi|^2\;(\mathrm{norm.})", color=INK, font_size=22).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.2)

        def _psi2():
            t = t_track.get_value()
            sigma = spread_scene_sigma(t)
            x_arr = np.linspace(-6, 6, 400)
            psi2  = np.exp(-x_arr**2 / (2 * sigma**2)) / sigma  # normalize peak
            pts   = [ax.c2p(x, y) for x, y in zip(x_arr, psi2)]
            m = VMobject(color=BLUE, stroke_width=2.8)
            m.set_points_smoothly(pts)
            return m

        dyn_psi2 = always_redraw(_psi2)
        self.add(dyn_psi2)

        t_lbl  = MathTex(r"t/t_{\rm spread} = ", color=DIM, font_size=28)
        t_num  = DecimalNumber(0.01, num_decimal_places=2, color=DIM, font_size=28)
        t_num.add_updater(lambda m: m.set_value(t_track.get_value()))
        sx_lbl = MathTex(r"\sigma_x = ", color=GOLD, font_size=28)
        sx_num = DecimalNumber(1.0, num_decimal_places=3, color=GOLD, font_size=28)
        sx_num.add_updater(lambda m: m.set_value(spread_scene_sigma(t_track.get_value())))
        sx_u   = MathTex(r"\sigma_0", color=GOLD, font_size=28)

        row1 = VGroup(t_lbl, t_num).arrange(RIGHT, buff=0.08)
        row2 = VGroup(sx_lbl, sx_num, sx_u).arrange(RIGHT, buff=0.08)
        VGroup(row1, row2).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.25)

        hdr = Text("Electron packet, σ₀ = 1 nm — spreading under free evolution",
                   font="EB Garamond", font_size=20, color=INK).to_edge(UP, buff=0.18)
        self.play(Write(hdr), FadeIn(row1), FadeIn(row2), run_time=0.8)
        self.play(t_track.animate.set_value(5.0), run_time=6.0, rate_func=smooth)
        self.wait(1.0)
        self.play(FadeOut(hdr, row1, row2, ax, x_lbl, y_lbl, dyn_psi2), run_time=0.5)

    def _phase_sigma_curve(self):
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 11, 2],
            x_length=9.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.2)
        x_lbl = MathTex(r"t/t_{\rm spread}", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"\sigma_x/\sigma_0", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.2)

        t_arr = np.linspace(0, 10, 400)
        sx_e  = np.sqrt(1 + t_arr**2)        # electron
        sx_p  = np.sqrt(1 + (t_arr/1836)**2) # proton (1836× slower)

        pts_e = [ax.c2p(t, s) for t, s in zip(t_arr, sx_e) if s <= 10.5]
        pts_p = [ax.c2p(t, s) for t, s in zip(t_arr, sx_p) if s <= 10.5]

        curve_e = VMobject(color=BLUE, stroke_width=3.0)
        curve_e.set_points_smoothly(pts_e)
        curve_p = VMobject(color=BROWN, stroke_width=2.5)
        curve_p.set_points_smoothly(pts_p)

        # √2 at t=t_spread
        pt_sqrt2 = Dot(ax.c2p(1.0, np.sqrt(2)), color=GOLD, radius=0.1)
        lbl_sqrt2 = MathTex(r"\sqrt{2}\,\sigma_0\;\text{at }t=t_{\rm spread}",
                            color=GOLD, font_size=20).next_to(pt_sqrt2, RIGHT, buff=0.1)

        e_lbl = Text("Electron", font="EB Garamond",
                     font_size=18, color=BLUE).move_to(ax.c2p(3.0, 3.5))
        p_lbl = Text("Proton (1836× slower)", font="EB Garamond",
                     font_size=18, color=BROWN).move_to(ax.c2p(6.0, 1.25))

        hdr = Text("σ_x(t) — hyperbolic growth, not linear",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(curve_e), Create(curve_p), run_time=2.0)
        self.play(FadeIn(pt_sqrt2), Write(lbl_sqrt2), run_time=0.8)
        self.play(Write(e_lbl), Write(p_lbl), run_time=0.7)
        final = Text("Momentum width σ_p stays constant — free evolution doesn't change momentum",
                     font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
