#!/usr/bin/env python3
"""
classical_pulsar_spinup.py — Pulsar Spin-Up: Stellar Collapse and Angular Momentum
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    L = Iω = (2/5)MR²ω = const
    ω_f = ω_i × (R_i/R_f)²
    R_i=7e8 m, P_i=25 days → R_f=1e4 m, P_f≈0.44 ms

Render:
    cd physics-classical-mechanics/youtube/classical-pulsar-spinup
    manim -qh classical_pulsar_spinup.py PulsarSpinupScene
"""
import sys
import numpy as np

R_SUN = 7e8     # m
P_I   = 25 * 24 * 3600  # s (25 days)
R_NS  = 1e4     # m (neutron star)

W_I = 2*np.pi/P_I


def omega_after_collapse(R_i, R_f, omega_i):
    return omega_i * (R_i/R_f)**2


def period_after(R_i, R_f, P_i):
    return P_i / (R_i/R_f)**2


def verify():
    print("=== Pulsar Spin-Up verification ===")
    w_f = omega_after_collapse(R_SUN, R_NS, W_I)
    P_f = 2*np.pi/w_f
    print(f"  ω_i = {W_I:.4e} rad/s  (P_i = {P_I/86400:.1f} days)")
    print(f"  ω_f = {w_f:.4e} rad/s  (P_f = {P_f*1000:.4f} ms)")
    print(f"  Compression ratio (R_i/R_f)² = {(R_SUN/R_NS)**2:.4e}")
    # P1: 10× smaller radius → 100× faster
    w_10x = omega_after_collapse(R_SUN, R_SUN/10, W_I)
    P_10x = 2*np.pi/w_10x
    print(f"  10× smaller: P_f = {P_10x/3600:.4f} h  (expected {25*24/100:.4f} h = 6 h)")
    # Crab Pulsar: P = 33 ms
    P_crab = 33e-3  # s
    R_compression = np.sqrt(P_I/P_crab)
    print(f"  Crab Pulsar (33 ms): R_compression ratio = {R_compression:.2e}")
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


class PulsarSpinupScene(Scene):
    """Star collapses, ω gauge climbs, L stays flat."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._collapse_animation()
        self._L_gauge()

    def _title(self):
        t1 = Text("Pulsar Spin-Up", font="EB Garamond", font_size=62, color=INK)
        t2 = Text("A star collapses — angular momentum is the only conserved quantity",
                  font="EB Garamond", font_size=23, color=DIM)
        t3 = MathTex(r"\omega_f = \omega_i \left(\frac{R_i}{R_f}\right)^2 \qquad L=\frac{2}{5}MR^2\omega",
                     color=BLUE, font_size=28)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _collapse_animation(self):
        pivot = ORIGIN
        # Star grows from small to big, then collapses
        star_big   = Circle(radius=2.8, color=GOLD, fill_color=GOLD, fill_opacity=0.5)
        star_small = Circle(radius=0.08, color=BLUE, fill_color=BLUE, fill_opacity=0.9)
        lbl_big   = Text("The Sun: R=7×10⁸ m, P=25 days", font="EB Garamond", font_size=18, color=GOLD)
        lbl_big.to_edge(DOWN, buff=0.5)
        lbl_small = Text("Neutron star: R=10 km, P=0.44 ms", font="EB Garamond", font_size=18, color=BLUE)
        lbl_small.to_edge(DOWN, buff=0.22)

        self.play(FadeIn(star_big), Write(lbl_big), run_time=1.0)

        # Slow rotation indicator for the star
        rot_dot = Dot(star_big.get_right(), color=BROWN, radius=0.15)
        self.play(FadeIn(rot_dot), run_time=0.3)
        # Spin slowly
        for ang in np.linspace(0, np.pi, 30):
            rot_dot.move_to(2.8*np.array([np.cos(ang), np.sin(ang), 0]))
            self.wait(0.06)

        # Collapse!
        self.play(
            Transform(star_big, star_small),
            FadeOut(lbl_big), Write(lbl_small),
            FadeOut(rot_dot),
            run_time=2.0,
        )

        # Fast pulsar blink
        for _ in range(8):
            self.play(star_big.animate.set_fill(BLUE, opacity=1.0), run_time=0.016)
            self.play(star_big.animate.set_fill(BLUE, opacity=0.1), run_time=0.016)
        self.wait(0.5)
        self.play(FadeOut(star_big, lbl_small), run_time=0.4)

    def _L_gauge(self):
        # ω vs R (logarithmic)
        ax = Axes(
            x_range=[4, 9, 1],    # log10(R in m)
            y_range=[-6, 4, 2],   # log10(ω in rad/s)
            x_length=10,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.3)
        lx = Text("log₁₀(R / m)", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("log₁₀(ω / rad·s⁻¹)", font="EB Garamond", font_size=18, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Angular velocity as radius shrinks  (L = const)",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        # ω ∝ 1/R² → log ω = -2 log R + const
        log_Rs = np.linspace(4, 9, 200)
        const  = np.log10(W_I) + 2*np.log10(R_NS)  # from ω_f×R_f² = ω_i×R_i²
        log_ws = const - 2*log_Rs
        pts    = np.array([ax.c2p(lr, lw) for lr, lw in zip(log_Rs, log_ws)])
        crv    = VMobject(color=BLUE, stroke_width=3.0).set_points_smoothly(pts)
        self.play(Create(crv), run_time=2.0)

        # Key points
        log_R_sun = np.log10(R_SUN)
        log_w_sun = const - 2*log_R_sun
        d_sun = Dot(ax.c2p(log_R_sun, log_w_sun), color=GOLD, radius=0.12)
        lbl_sun = Text("Sun (25 day period)", font="EB Garamond", font_size=18, color=GOLD).next_to(d_sun, UR, buff=0.1)

        log_R_ns = np.log10(R_NS)
        log_w_ns = const - 2*log_R_ns
        d_ns = Dot(ax.c2p(log_R_ns, log_w_ns), color=BLUE, radius=0.12)
        lbl_ns = Text("Neutron star (0.44 ms)", font="EB Garamond", font_size=18, color=BLUE).next_to(d_ns, LEFT, buff=0.1)

        self.play(FadeIn(d_sun, d_ns), Write(lbl_sun), Write(lbl_ns), run_time=1.0)

        slope_lbl = MathTex(r"\omega \propto R^{-2}", color=DIM, font_size=26).move_to(ax.c2p(7, 2))
        self.play(Write(slope_lbl), run_time=0.5)

        final = Text(
            "Same algebra as a figure skater — just 10⁹× the compression ratio",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
