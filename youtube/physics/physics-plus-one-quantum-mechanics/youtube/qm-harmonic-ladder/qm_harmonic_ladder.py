#!/usr/bin/env python3
"""
qm_harmonic_ladder.py — Harmonic Oscillator Ladder: Energy Levels E_n = (n + ½)ℏω
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-quantum-mechanics book.

Render:
    cd physics-plus-one-quantum-mechanics/youtube/qm-harmonic-ladder
    manim -qh qm_harmonic_ladder.py HarmonicLadderScene

Physics:
    ω = 2π × 10¹² rad/s (optical phonon)
    ℏ = 1.055e-34 J·s
    E_n = (n + 1/2)ℏω
    E₀ = 3.31e-22 J = 2.07 meV
    Spacing ℏω = 4.14 meV (uniform)
    σ_0 = sqrt(ℏ/2mω)  m = 1.67e-27 kg (proton-like)
"""
import sys
import numpy as np
from math import factorial

HBAR = 1.055e-34     # J·s
OMEGA = 2 * np.pi * 1e12  # rad/s
MASS  = 1.67e-27     # kg  (proton, as representative)
MEV   = 1.602e-22    # J per meV


def energy_level(n):
    return (n + 0.5) * HBAR * OMEGA


def sigma_0():
    """Ground state spatial width."""
    return np.sqrt(HBAR / (2 * MASS * OMEGA))


def psi_n(x, n, sigma):
    """Harmonic oscillator wavefunction (unnormalized |psi|^2 for plotting)."""
    xi = x / sigma
    # Hermite polynomial H_n via recursion
    H = [np.ones_like(xi), 2 * xi]
    for k in range(2, n + 1):
        H.append(2 * xi * H[-1] - 2 * (k - 1) * H[-2])
    Hn = H[n]
    psi = Hn * np.exp(-xi**2 / 2)
    norm = psi**2
    return norm / norm.max()


if __name__ == "__main__":
    print("=== Harmonic Oscillator Ladder Verification ===")
    E0 = energy_level(0)
    E1 = energy_level(1)
    spacing = E1 - E0
    print(f"E₀ = {E0/MEV:.3f} meV  (expect 2.07 meV)")
    print(f"E₁ = {E1/MEV:.3f} meV  (expect 6.21 meV)")
    print(f"Spacing ℏω = {spacing/MEV:.3f} meV  (expect 4.14 meV)")
    assert abs(E0/MEV - 2.07) < 0.02, "E0 FAIL"
    # P1: uniform spacing
    for n in range(1, 5):
        sp = energy_level(n) - energy_level(n-1)
        assert abs(sp - HBAR * OMEGA) < 1e-36, f"P1 FAIL at n={n}"
    print("P1: spacing uniform ✓")
    # P2: sigma_0
    s0 = sigma_0()
    print(f"P2: σ₀ = {s0*1e12:.3f} pm  (ground state width)")
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


class HarmonicLadderScene(Scene):
    """Parabolic well + equally-spaced energy levels + ψ² overlays."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_well_and_levels(ax)
        self._phase_wavefunctions(ax)
        self._phase_ladder_operators()

    def _phase_title(self):
        title = Text("Quantum Harmonic Oscillator", font="EB Garamond",
                     font_size=50, color=INK)
        sub = MathTex(r"E_n=(n+\tfrac{1}{2})\hbar\omega\quad n=0,1,2,\ldots",
                      color=BLUE, font_size=32)
        sub2 = Text("Zero-point energy: the ground state cannot sit still",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 5.5, 1],
            x_length=9.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.2)
        x_lbl = MathTex(r"x\;(\sigma_0\;\text{units})", color=INK, font_size=22).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"E\;(\hbar\omega\;\text{units})", color=INK, font_size=22).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        return ax

    def _phase_well_and_levels(self, ax):
        # Parabola V(x) = x^2 in ℏω units
        x_arr = np.linspace(-3.3, 3.3, 300)
        v_arr = x_arr**2 * 0.5    # V = ½x² → in units of ℏω when x in σ_0

        pts = [ax.c2p(x, v) for x, v in zip(x_arr, v_arr) if v <= 5.3]
        parabola = VMobject(color=DIM, stroke_width=2.5)
        parabola.set_points_smoothly(pts)

        self.play(Create(parabola), run_time=1.5)

        # Energy levels E_n = (n+0.5) in ℏω units
        colors_n = [BLUE, GOLD, BROWN, BLUE, GOLD]
        level_mobs = []
        for n in range(5):
            E = n + 0.5
            # Horizontal extent: classical turning points at x = sqrt(2E)
            x_tp = np.sqrt(2 * E)
            x_tp = min(x_tp, 3.3)
            line = Line(ax.c2p(-x_tp, E), ax.c2p(x_tp, E),
                        color=colors_n[n], stroke_width=2.5)
            lbl = MathTex(rf"E_{n}={(n+0.5):.1f}\hbar\omega", color=colors_n[n],
                          font_size=18).next_to(ax.c2p(x_tp, E), RIGHT, buff=0.08)
            self.play(Create(line), Write(lbl), run_time=0.5)
            level_mobs.append((line, lbl))

        # Zero-point callout
        zpe_arrow = Arrow(ax.c2p(2.5, 0.0), ax.c2p(2.5, 0.5),
                          color=GOLD, stroke_width=2)
        zpe_lbl = MathTex(r"\tfrac{1}{2}\hbar\omega", color=GOLD, font_size=20
                          ).next_to(ax.c2p(2.5, 0.25), RIGHT, buff=0.08)
        self.play(Create(zpe_arrow), Write(zpe_lbl), run_time=0.8)
        self.wait(2.0)

        self._level_mobs = level_mobs
        self._parabola   = parabola
        self._zpe_arrow  = zpe_arrow
        self._zpe_lbl    = zpe_lbl

    def _phase_wavefunctions(self, ax):
        x_arr = np.linspace(-3.3, 3.3, 400)
        sigma = 1.0   # σ₀ units

        wf_grp = VGroup()
        for n in range(5):
            E = n + 0.5
            psi2 = psi_n(x_arr, n, sigma)
            # Scale to fit between level and E+0.8
            psi2_s = psi2 * 0.7
            pts = [ax.c2p(x, E + p) for x, p in zip(x_arr, psi2_s)]
            wf = VMobject(color=GOLD, stroke_width=1.8, fill_opacity=0.0)
            wf.set_points_smoothly(pts)
            wf_grp.add(wf)

        self.play(Create(wf_grp), run_time=2.5)
        hdr = Text("|ψ_n(x)|²: n nodes in state n — ground state is Gaussian",
                   font="EB Garamond", font_size=20, color=GOLD).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(wf_grp, hdr, self._zpe_arrow, self._zpe_lbl), run_time=0.5)
        for line, lbl in self._level_mobs:
            self.remove(line, lbl)
        self.remove(self._parabola)

    def _phase_ladder_operators(self):
        rows = [
            MathTex(r"\hat{a}_+|n\rangle=\sqrt{n+1}\,|n+1\rangle", color=BLUE, font_size=34),
            MathTex(r"\hat{a}_-|n\rangle=\sqrt{n}\,|n-1\rangle",   color=BROWN, font_size=34),
            MathTex(r"[\hat{a}_-,\hat{a}_+]=1\;\Rightarrow\;E_n=(n+\tfrac{1}{2})\hbar\omega",
                    color=INK, font_size=28),
        ]
        VGroup(*rows).arrange(DOWN, buff=0.55).center()
        hdr = Text("Ladder operators — the entire spectrum from one algebraic move",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.5)
        for r in rows:
            self.play(Write(r), run_time=1.1)
            self.wait(0.5)
        self.wait(2.0)
        final = Text("Liquid helium never freezes at 1 atm — zero-point energy is the reason",
                     font="EB Garamond", font_size=22, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(final), run_time=1.2)
        self.wait(2.5)
