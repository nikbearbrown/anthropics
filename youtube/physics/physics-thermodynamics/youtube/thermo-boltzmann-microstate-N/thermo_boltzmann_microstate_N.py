#!/usr/bin/env python3
"""
thermo_boltzmann_microstate_N.py — Boltzmann Microstate Counting: Why the Second Law Is Statistics
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics (verified at module level):
    Ω(n) = C(N,n) = N!/(n!(N-n)!)
    N=20: Ω_max = C(20,10) = 184756, S_max/k_B = ln(184756) ≈ 12.13
    N=100: C(100,50) ≈ 10^29 (from Stirling)
    P(all left) = 1/2^N

Render:
    cd physics-thermodynamics/youtube/thermo-boltzmann-microstate-N
    manim -qh thermo_boltzmann_microstate_N.py BoltzmannMicrostateNScene
"""
import sys
import numpy as np
from scipy.special import comb

# ─── Physics ──────────────────────────────────────────────────────────────────
K_B = 1.380649e-23   # J/K

def omega(N: int, n: int) -> float:
    return float(comb(N, n, exact=True))

def S_over_kB(N: int, n: int) -> float:
    om = omega(N, n)
    if om <= 0:
        return 0.0
    return np.log(om)

# ─── Verification ─────────────────────────────────────────────────────────────
def _verify():
    print("=== Boltzmann Microstate verification ===")
    N20 = 20
    om20 = omega(N20, 10)
    print(f"N=20: Ω_max = C(20,10) = {om20:.0f}  (expected 184756)")
    print(f"  S_max/k_B = ln(Ω_max) = {np.log(om20):.2f}  (expected 12.13)")
    print(f"  P(all left) = 1/2^20 = {1/2**20:.2e}")
    # N=100
    import math
    log_om100 = math.lgamma(101) - 2*math.lgamma(51)  # ln C(100,50)
    print(f"N=100: ln Ω_max = {log_om100:.2f}, Ω_max ≈ 10^{log_om100/np.log(10):.1f}")
    print(f"  P(all left) = 1/2^100 = {1/2**100:.2e}")
    # FWHM check for N=20
    ns20 = np.arange(0, 21)
    oms20 = np.array([omega(20, n) for n in ns20])
    half_max = oms20.max() / 2
    fwhm_ns = ns20[oms20 >= half_max]
    print(f"N=20: FWHM ≈ {fwhm_ns.max()-fwhm_ns.min()} units, relative FWHM = {(fwhm_ns.max()-fwhm_ns.min())/20*100:.0f}%  (expected ≈ 45%)")
    print("=== PASSED ===")

_verify()
if __name__ == "__main__":
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"

N_SEQUENCE = [4, 10, 20, 50, 100]


class BoltzmannMicrostateNScene(Scene):
    """
    Phase 1: Title.
    Phase 2: N=4 — show all seven macrostates as bars, label extremes.
    Phase 3: N steps from 4 to 100 — distribution sharpens.
    Phase 4: Final punchline text.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._build_axes()
        self._phase_step_N(ax)
        self._phase_punchline()

    def _phase_title(self):
        title = Text("Boltzmann Microstate Counting", font="EB Garamond", font_size=56, color=INK)
        sub1 = MathTex(
            r"\Omega(n) = \binom{N}{n} = \frac{N!}{n!\,(N-n)!}",
            color=BLUE, font_size=34,
        )
        sub2 = Text(
            "The second law is not a prohibition — it is overwhelming statistics",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub1), run_time=0.9)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _build_axes(self):
        ax = Axes(
            x_range=[0, 1.05, 0.25],     # x = n/N (fraction)
            y_range=[0, 1.1, 0.25],      # y = Ω(n)/Ω_max (normalized)
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.4)
        lbl_x = MathTex(r"n/N", color=INK, font_size=26).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\Omega(n)/\Omega_{\rm max}", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)
        return ax

    def _bars_for_N(self, N: int, ax):
        """Return a VGroup of normalized bar chart for given N."""
        ns  = np.arange(0, N + 1)
        oms = np.array([omega(N, n) for n in ns])
        om_max = oms.max()
        bars = VGroup()
        bar_w = 0.9 / (N + 1) * 10.0   # in scene units
        for n, om in zip(ns, oms):
            frac_n = n / N
            frac_om = om / om_max
            h = frac_om * 5.5   # height in scene units
            rect = Rectangle(
                width=max(bar_w * 0.85, 0.03),
                height=max(h, 0.01),
                color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=0,
            )
            # Align bottom to axis
            rect.move_to(ax.c2p(frac_n, frac_om / 2))
            bars.add(rect)
        return bars

    def _phase_step_N(self, ax):
        hdr = Text("N = 4  —  all macrostates visible",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(hdr), run_time=0.6)

        bars_4 = self._bars_for_N(4, ax)
        self.play(Create(bars_4), run_time=1.5)

        # Annotate extremes for N=4
        N = 4
        prob_extreme = 1.0 / 2**N
        ann_4 = Text(
            f"P(all left) = P(n=0) = 1/2^{N} = {prob_extreme:.4f}  —  happens every 16 draws",
            font="EB Garamond", font_size=21, color=GOLD,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(ann_4), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(ann_4), run_time=0.3)

        # Step through N values
        N_labels = {10: "10", 20: "20", 50: "50", 100: "100"}
        N_notes = {
            10:  f"N=10:  P(all left) = 1/2^10 ≈ 10⁻³",
            20:  f"N=20:  P(all left) = 1/2^20 ≈ 10⁻⁶  |  Ω_max = 184,756",
            50:  f"N=50:  P(all left) = 1/2^50 ≈ 10⁻¹⁵  —  already macroscopically irreversible",
            100: f"N=100: P(all left) = 1/2^100 ≈ 10⁻³⁰  —  wait 10²⁹ draws for Ω_max",
        }
        N_hdr = {
            10:  "N = 10  —  distribution narrows",
            20:  "N = 20  —  wings almost invisible",
            50:  "N = 50  —  extremes machine-zero",
            100: "N = 100  —  effectively a spike at n = 50",
        }

        current_bars = bars_4
        for N in [10, 20, 50, 100]:
            new_bars = self._bars_for_N(N, ax)
            new_hdr  = Text(N_hdr[N], font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)
            new_note = Text(N_notes[N], font="EB Garamond", font_size=21, color=DIM).to_edge(DOWN, buff=0.28)

            # Entropy annotation at peak
            S_ann = MathTex(
                rf"S_{{max}}/k_B = \ln\Omega_{{max}} \approx {S_over_kB(N, N//2):.1f}",
                color=GOLD, font_size=22,
            ).to_edge(DOWN, buff=0.55)

            self.play(
                FadeOut(current_bars, hdr if N == 10 else VGroup()),
                FadeIn(new_bars),
                Transform(hdr if N == 10 else hdr, new_hdr),
                run_time=1.2,
            )
            self.play(Write(new_note), Write(S_ann), run_time=0.8)
            self.wait(1.5)
            self.play(FadeOut(new_note, S_ann), run_time=0.3)
            current_bars = new_bars

    def _phase_punchline(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)
        lines = [
            ("N = 4:", "P(all left) = 6.25%  —  wait 16 draws"),
            ("N = 20:", "P(all left) = 10⁻⁶  —  wait 1,000,000 draws"),
            ("N = 100:", "P(all left) = 10⁻³⁰  —  wait longer than the Solar System's lifetime"),
            ("N = 10²³:", "wait 10^(10²² ) draws  —  longer than the age of the universe × 10^(10²²)"),
        ]
        title = Text("The second law is counting, not prohibition",
                     font="EB Garamond", font_size=30, color=INK).to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)

        group = VGroup()
        for N_str, explanation in lines:
            row = VGroup(
                Text(N_str, font="EB Garamond", font_size=24, color=GOLD),
                Text(explanation, font="EB Garamond", font_size=24, color=INK),
            ).arrange(RIGHT, buff=0.3)
            group.add(row)
        group.arrange(DOWN, buff=0.35, aligned_edge=LEFT).center()

        for row in group:
            self.play(FadeIn(row), run_time=0.7)
        self.wait(3.5)
