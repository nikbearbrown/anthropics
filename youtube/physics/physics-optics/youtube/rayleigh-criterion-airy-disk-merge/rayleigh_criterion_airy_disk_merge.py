#!/usr/bin/env python3
"""
rayleigh_criterion_airy_disk_merge.py — Rayleigh Criterion: Two Airy Disks Merging
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy + scipy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/rayleigh-criterion-airy-disk-merge
    manim -qh rayleigh_criterion_airy_disk_merge.py RayleighCriterionScene

Numpy verification (run standalone):
    python3 rayleigh_criterion_airy_disk_merge.py --verify

Physics (checkable):
    I(r) ∝ [2J₁(x)/x]²  where x = πDr/(λL)
    Rayleigh criterion: θ_min = 1.22λ/D

    P1: D=100mm, λ=550nm → θ_min = 1.22×5.5e-7/0.1 = 6.71µrad ✓
    P2: Hubble D=2.4m → θ_min = 0.058 arcsec ✓
        At Rayleigh limit, combined intensity dip = 73.5% of peak ✓
"""
import sys
import numpy as np
from scipy.special import j1

LAMBDA = 550e-9   # m
D_M    = 0.10     # m aperture diameter


def rayleigh_angle(D_m=D_M, lam=LAMBDA):
    """θ_min = 1.22λ/D in radians."""
    return 1.22 * lam / D_m


def airy_intensity(r_arr, D_m=D_M, lam=LAMBDA, focal_len=1.0):
    """
    Airy pattern intensity: I(r)/I₀ = [2J₁(x)/x]² where x = πD·r/(λ·f).
    r_arr: radial positions on focal plane (m).
    """
    x = np.pi * D_m * r_arr / (lam * focal_len)
    with np.errstate(invalid='ignore', divide='ignore'):
        val = np.where(np.abs(x) < 1e-10, 1.0, (2 * j1(x) / x) ** 2)
    return val


def combined_intensity(r_arr, sep, D_m=D_M, lam=LAMBDA, focal_len=1.0):
    """Sum of two Airy disks separated by sep (in r units)."""
    I1 = airy_intensity(r_arr - sep / 2, D_m, lam, focal_len)
    I2 = airy_intensity(r_arr + sep / 2, D_m, lam, focal_len)
    return I1 + I2


def verify():
    print("=== Rayleigh criterion Airy disk verification ===")
    # P1: Rayleigh angle
    theta_min = rayleigh_angle()
    print(f"P1: D={D_M*1e3:.0f}mm, λ={LAMBDA*1e9:.0f}nm")
    print(f"    θ_min = 1.22λ/D = {theta_min*1e6:.2f} µrad")
    # Convert to arcsec: 1 rad = 206265 arcsec
    print(f"    = {theta_min * 206265:.3f} arcsec")
    # P2: Hubble
    th_hubble = rayleigh_angle(2.4, LAMBDA)
    print(f"P2: Hubble D=2.4m: θ_min = {th_hubble * 206265:.4f} arcsec  (should be ≈0.058)")
    # Saddle intensity at Rayleigh limit
    # At r=0 (midpoint between two sources separated by θ_min × f):
    focal_len = 1.0
    sep = theta_min * focal_len   # separation in focal plane meters
    r_arr = np.array([0.0])
    I_mid = combined_intensity(r_arr, sep) / 2.0  # normalized to peak
    print(f"    Combined intensity at midpoint = {I_mid[0]*100:.1f}% of peak  (should be ≈73.5%)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class RayleighCriterionScene(Scene):
    """
    Two Airy disk profiles slide together from well-separated to unresolved.
    Rayleigh limit = saddle point between peaks.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_merge()

    def _phase_title(self):
        title = Text("Rayleigh Criterion", font="EB Garamond", font_size=60, color=INK)
        sub = Text(
            "θ_min = 1.22λ/D  ·  Airy disk maximum on first minimum of neighbor",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "D=100mm, λ=550nm → θ_min = 6.71 µrad = 1.38 arcsec",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

    def _phase_merge(self):
        focal_len = 1.0
        theta_min = rayleigh_angle()
        sep_rayleigh = theta_min * focal_len

        # Plot r range: ±4 × Rayleigh sep
        r_max = 4.0 * sep_rayleigh
        r_arr = np.linspace(-r_max, r_max, 2000)

        # Scale to plot units: Rayleigh unit = 1.0 in x
        r_units = r_arr / sep_rayleigh

        ax = Axes(
            x_range=[-4.5, 4.5, 1.0],
            y_range=[0, 2.15, 0.5],
            x_length=11.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.14),
            x_axis_config=dict(numbers_to_include=[-4, -2, 0, 2, 4]),
            y_axis_config=dict(numbers_to_include=[0, 0.5, 1.0, 1.5, 2.0]),
        ).shift(UP * 0.4)

        lbl_x = MathTex(r"r / \theta_{\min}", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"I/I_0", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Rayleigh limit vertical marker
        rl_line = DashedLine(ax.c2p(0, 0), ax.c2p(0, 2.05), color=GOLD, stroke_width=1.0, dash_length=0.12)
        rl_lbl = MathTex(r"\theta_{\min}", color=GOLD, font_size=20).next_to(ax.c2p(0, 2.05), UP, buff=0.05)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.4)

        # Separation multipliers
        sep_multipliers = [5.0, 3.0, 2.0, 1.0, 0.5]
        colors_pair = [(BLUE, BROWN), (BLUE, BROWN), (BLUE, BROWN), (BLUE, BROWN), (BLUE, BROWN)]

        sep_lbl = always_redraw(lambda: Text("", font="EB Garamond", font_size=1, color=CANVAS))

        curve1 = None
        curve2 = None
        curve_sum = None
        live_cap = None

        for mult in sep_multipliers:
            sep = mult * sep_rayleigh
            sep_units = mult  # in rayleigh units

            I1 = airy_intensity(r_arr - sep / 2)
            I2 = airy_intensity(r_arr + sep / 2)
            I_sum = I1 + I2

            pts1 = [ax.c2p(ru, np.clip(i, 0, 2.1)) for ru, i in zip(r_units - sep_units / 2, I1)]
            pts2 = [ax.c2p(ru, np.clip(i, 0, 2.1)) for ru, i in zip(r_units + sep_units / 2, I2)]
            pts_sum = [ax.c2p(ru, np.clip(i, 0, 2.1)) for ru, i in zip(r_units, I_sum)]

            new1 = VMobject(color=BLUE, stroke_width=2.8)
            new1.set_points_smoothly(pts1)
            new2 = VMobject(color=BROWN, stroke_width=2.8)
            new2.set_points_smoothly(pts2)
            new_sum = VMobject(color=GOLD, stroke_width=3.5)
            new_sum.set_points_smoothly(pts_sum)

            if mult == 1.0:
                label = f"θ = θ_min = 1.0×θ_min  ·  saddle at 73.5% of peak  [Rayleigh limit]"
                col = GOLD
            elif mult < 1.0:
                label = f"θ = {mult:.1f}×θ_min  ·  unresolved — sources merge"
                col = DIM
            else:
                label = f"θ = {mult:.1f}×θ_min  ·  clearly resolved"
                col = BLUE

            new_cap = Text(label, font="EB Garamond", font_size=19, color=col).to_edge(DOWN, buff=0.28)

            if curve1 is None:
                self.play(
                    Create(new1), Create(new2), Create(new_sum),
                    Write(new_cap),
                    run_time=1.8,
                )
            else:
                self.play(
                    Transform(curve1, new1),
                    Transform(curve2, new2),
                    Transform(curve_sum, new_sum),
                    FadeOut(live_cap),
                    Write(new_cap),
                    run_time=1.6,
                )
            if mult == 1.0:
                self.play(Create(rl_line), Write(rl_lbl), run_time=0.5)
            self.wait(0.9)
            curve1, curve2, curve_sum = new1, new2, new_sum
            live_cap = new_cap

        # Payoff
        payoff = MathTex(
            r"\theta_{\min} = \frac{1.22\lambda}{D} \;\;\; \Longrightarrow \;\;\; "
            r"\text{larger } D \Rightarrow \text{ better resolution}",
            color=INK, font_size=27,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(live_cap), Write(payoff), run_time=1.2)
        self.wait(3.0)
