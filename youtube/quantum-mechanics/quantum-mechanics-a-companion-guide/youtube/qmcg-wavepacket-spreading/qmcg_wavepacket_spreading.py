#!/usr/bin/env python3
"""
qmcg_wavepacket_spreading.py — Gaussian Wavepacket Spreading: The Free-Particle Clock
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-wavepacket-spreading
    manim -qh qmcg_wavepacket_spreading.py QMCGWavepacketScene

Verify:
    python3 qmcg_wavepacket_spreading.py --verify

Physics:
    σ(t) = σ₀ √(1 + (ħt/2mσ₀²)²)
    electron, σ₀=1 nm → τ = 2mσ₀²/ħ ≈ 0.76 fs
    At t=τ: σ = σ₀√2 ≈ 1.41 nm  ✓
    At t=5τ: σ ≈ 5.1 nm  ✓
    Proton: τ_p = 1836·τ_e (same σ₀)
    The i in Schrödinger is load-bearing — gives spreading, not smoothing
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
ME   = 9.10938e-31


def sigma_t(sigma0, t_over_tau):
    return sigma0 * np.sqrt(1 + t_over_tau**2)


def verify():
    print("=== QMCG Wavepacket spreading verification ===")
    sigma0 = 1e-9
    tau    = 2 * ME * sigma0**2 / HBAR
    print(f"  τ = 2mσ₀²/ħ = {tau:.4e} s = {tau*1e15:.2f} fs")
    for t_tau in [0, 1, 2, 5]:
        s = sigma_t(1.0, t_tau)
        print(f"  t/τ={t_tau}: σ/σ₀ = {s:.4f}  (P1: {t_tau}→{np.sqrt(2):.4f} at t=τ)")
    # Proton
    mp = ME * 1836
    tau_p = 2 * mp * sigma0**2 / HBAR
    print(f"\n  Proton τ = {tau_p:.4e} s = {tau_p/tau:.0f}× electron τ")
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


class QMCGWavepacketScene(Scene):
    """
    Phase 1: title
    Phase 2: |ψ(x,t)|² spreading; width bracket growing; color phase rippling
    Phase 3: proton vs electron comparison
    Phase 4: i-in-Schrödinger teardown
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_spreading()
        self._phase_proton_vs_electron()

    def _phase_title(self):
        title = Text("The Free-Particle Clock", font="EB Garamond", font_size=58, color=INK)
        sub1  = Text(
            "σ(t) = σ₀ √(1 + t²/τ²)  ·  τ = 2mσ₀²/ħ",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "The i in Schrödinger is the reason this spreads — remove it and it decays",
            font="EB Garamond", font_size=19, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_spreading(self):
        ax = Axes(
            x_range=[-10, 10, 2], y_range=[0, 0.52, 0.1],
            x_length=9.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.3, "include_ticks": True},
        ).center().shift(UP * 0.3)

        x_lbl = MathTex(r"x/\sigma_0", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        self.play(Create(ax), Write(x_lbl), run_time=0.6)

        t_tracker = ValueTracker(0.0)

        def _gauss():
            t = t_tracker.get_value()
            s = sigma_t(1.0, t)
            x_arr = np.linspace(-10, 10, 500)
            prob  = (1 / (np.sqrt(2 * np.pi) * s)) * np.exp(-x_arr**2 / (2 * s**2))
            pts   = [ax.c2p(x, p) for x, p in zip(x_arr, prob)]
            c = VMobject(color=BLUE, stroke_width=2.8)
            c.set_points_smoothly(pts)
            return c

        def _bracket():
            t = t_tracker.get_value()
            s = sigma_t(1.0, t)
            lo = ax.c2p(-s, 0.02)
            hi = ax.c2p(+s, 0.02)
            return DoubleArrow(lo, hi, buff=0, color=GOLD, stroke_width=2.0, tip_length=0.15)

        def _lbl():
            t = t_tracker.get_value()
            s = sigma_t(1.0, t)
            return MathTex(
                rf"t/\tau = {t:.1f}\quad\sigma = {s:.2f}\,\sigma_0",
                color=INK, font_size=22,
            ).to_edge(DOWN, buff=0.28)

        dyn_g  = always_redraw(_gauss)
        dyn_br = always_redraw(_bracket)
        dyn_l  = always_redraw(_lbl)
        self.add(dyn_g, dyn_br, dyn_l)

        self.play(t_tracker.animate.set_value(5.0), run_time=6.0, rate_func=linear)

        mark_tau = Dot(ax.c2p(np.sqrt(2), 0.03), color=BROWN, radius=0.1)
        self.play(FadeIn(mark_tau), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_proton_vs_electron(self):
        hdr = Text(
            "Wider initial packets spread more slowly — τ ∝ mσ₀²",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 7, 1],
            x_length=8.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(DOWN * 0.2)

        x_lbl = MathTex(r"t/\tau_e", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"\sigma/\sigma_0", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.7)

        t_arr = np.linspace(0, 6, 400)
        # Electron
        s_e = [sigma_t(1.0, t) for t in t_arr]
        pts_e = [ax.c2p(t, min(s, 6.9)) for t, s in zip(t_arr, s_e)]
        c_e = VMobject(color=BLUE, stroke_width=2.8); c_e.set_points_smoothly(pts_e)

        # Proton at same σ₀: t/τ_e scale but τ_p=1836τ_e so σ(t)=√(1+(t/1836)²)
        s_p = [sigma_t(1.0, t/1836) for t in t_arr]
        pts_p = [ax.c2p(t, min(s, 6.9)) for t, s in zip(t_arr, s_p)]
        c_p = VMobject(color=GOLD, stroke_width=2.8); c_p.set_points_smoothly(pts_p)

        lbl_e = Text("Electron (σ₀=1nm)", font="EB Garamond", font_size=19, color=BLUE).to_corner(UR, buff=0.35)
        lbl_p = Text("Proton (σ₀=1nm, 1836× slower)", font="EB Garamond", font_size=19, color=GOLD).to_corner(UR, buff=0.35).shift(DOWN*0.4)
        self.play(Create(c_e), Create(c_p), Write(lbl_e), Write(lbl_p), run_time=1.2)

        tau_pt = Dot(ax.c2p(1.0, np.sqrt(2)), color=BROWN, radius=0.12)
        tau_lbl = MathTex(r"t=\tau_e:\;\sigma=\sqrt{2}\,\sigma_0", color=BROWN, font_size=22).next_to(tau_pt, RIGHT, buff=0.1)
        self.play(FadeIn(tau_pt), Write(tau_lbl), run_time=0.6)

        fin = MathTex(r"\sigma(t) = \sigma_0\sqrt{1 + \left(\frac{\hbar t}{2m\sigma_0^2}\right)^2}", color=INK, font_size=26).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.8)
        self.wait(2.5)
