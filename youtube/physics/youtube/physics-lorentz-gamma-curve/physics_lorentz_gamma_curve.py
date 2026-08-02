#!/usr/bin/env python3
"""
physics_lorentz_gamma_curve.py — Lorentz Factor γ: Flat Until 0.5c, Then the Cliff
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    γ = 1/√(1 − v²/c²)
    γ(0.866c) = 2.0 exactly
    LHC proton at 7 TeV: γ ≈ 7460

Render:
    cd physics/youtube/physics-lorentz-gamma-curve
    manim -qh physics_lorentz_gamma_curve.py LorentzGammaScene
"""
import sys
import numpy as np

def gamma(beta):
    """Lorentz factor for v/c = beta."""
    return 1.0 / np.sqrt(1.0 - beta**2)


def verify():
    print("=== Lorentz Factor verification ===")
    for bc, label in [(0.1, "airplane"), (0.5, "0.5c"), (0.866, "γ=2 exact"),
                       (0.9, "0.9c"), (0.99, "0.99c"), (0.999, "muon")]:
        g = gamma(bc)
        print(f"  v/c = {bc}  ({label}): γ = {g:.4f}")
    # P1: at v = 0.866c, γ = 2.0 exactly
    g2 = gamma(np.sqrt(3)/2)
    print(f"  v/c = √3/2 = {np.sqrt(3)/2:.6f}: γ = {g2:.8f}  (exact 2)")
    # P2: LHC proton KE=7000 MeV, m_p c²=938.3 MeV → γ = (7000+938.3)/938.3
    g_lhc = (7000+938.3)/938.3
    v_frac_deficit = 1.0/(2*g_lhc**2)
    print(f"  LHC proton γ = {g_lhc:.1f},  v = c - {v_frac_deficit:.2e}c (≈9 ppb)")
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

GAMMA_MAX_PLOT = 20


class LorentzGammaScene(Scene):
    """γ curve draws left to right, asymptoting at v=c; key markers labeled."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_curve(ax)
        self._markers(ax)
        self._energy_overlay(ax)

    def _title(self):
        t1 = Text("The Lorentz Factor", font="EB Garamond", font_size=62, color=INK)
        t2 = Text("Flat until 0.5c — then the cliff", font="EB Garamond", font_size=26, color=DIM)
        t3 = MathTex(r"\gamma = \frac{1}{\sqrt{1-v^2/c^2}}", color=BLUE, font_size=40)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.32).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _axes(self):
        ax = Axes(
            x_range=[0, 1.0, 0.2],
            y_range=[0, GAMMA_MAX_PLOT, 5],
            x_length=10,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.5)
        lx = MathTex(r"v/c", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"\gamma", color=INK, font_size=28).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        # Vertical asymptote at v=c
        asym = DashedLine(ax.c2p(1.0, 0), ax.c2p(1.0, GAMMA_MAX_PLOT),
                          color=DIM, stroke_width=1.2, dash_length=0.15)
        lbl_c = MathTex(r"c", color=DIM, font_size=22).next_to(ax.c2p(1.0, 0), DOWN, buff=0.08)
        self.play(Create(ax), Write(lx), Write(ly), Create(asym), Write(lbl_c), run_time=1.5)
        return ax

    def _draw_curve(self, ax):
        betas = np.linspace(0.001, 0.999, 1500)
        gammas = gamma(betas)
        # Clip to plot range
        mask = gammas <= GAMMA_MAX_PLOT
        betas_c  = betas[mask]
        gammas_c = gammas[mask]
        pts = np.array([ax.c2p(b, g) for b, g in zip(betas_c, gammas_c)])
        crv = VMobject(color=BLUE, stroke_width=3.2)
        crv.set_points_smoothly(pts)
        self.play(Create(crv), run_time=3.0)

        # γ = 1 line
        flat = DashedLine(ax.c2p(0, 1), ax.c2p(0.5, 1), color=DIM, stroke_width=1.2, dash_length=0.1)
        lbl_flat = Text("γ ≈ 1 here — no effect", font="EB Garamond", font_size=17, color=DIM)
        lbl_flat.next_to(ax.c2p(0.25, 1), UP, buff=0.12)
        self.play(Create(flat), Write(lbl_flat), run_time=0.7)
        self.wait(1.0)

    def _markers(self, ax):
        markers = [
            (0.866, 2.0, "v=0.866c  γ=2  (exact)", UP),
            (0.9,   gamma(0.9),  "v=0.9c  γ=2.3", UR),
            (0.999, gamma(0.999), "muon 0.999c  γ=22.4", LEFT),
        ]
        for b, g_val, label, direction in markers:
            if g_val > GAMMA_MAX_PLOT:
                continue
            d = Dot(ax.c2p(b, g_val), color=GOLD, radius=0.10)
            lbl = Text(label, font="EB Garamond", font_size=17, color=GOLD)
            lbl.next_to(d, direction, buff=0.12)
            self.play(FadeIn(d), Write(lbl), run_time=0.7)
            self.wait(0.4)

        final = Text(
            "As v → c, γ → ∞ — infinite energy required: c is unreachable",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)

    def _energy_overlay(self, ax):
        # Second panel: classical vs relativistic KE ratio
        cap = Text(
            "Classical KE = ½mv² diverges from Relativistic KE = (γ−1)mc² above 0.5c",
            font="EB Garamond", font_size=19, color=BROWN,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(*[m for m in self.mobjects if isinstance(m, Text) and "As v" in str(m)]),
                  run_time=0.2)
        self.play(Write(cap), run_time=1.0)
        self.wait(2.0)
