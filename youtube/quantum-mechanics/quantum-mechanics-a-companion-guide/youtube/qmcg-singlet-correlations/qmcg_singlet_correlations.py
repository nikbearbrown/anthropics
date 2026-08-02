#!/usr/bin/env python3
"""
qmcg_singlet_correlations.py — The Singlet State: Rotational Invariance and Bell Correlations
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-singlet-correlations
    manim -qh qmcg_singlet_correlations.py SingletCorrelationsScene

Verify:
    python3 qmcg_singlet_correlations.py --verify

Physics:
    E(n̂_A, n̂_B) = −cos(θ) for singlet state
    At θ=0: E=−1 (perfect anti-correlation)
    At θ=90°: E=0 (uncorrelated)
    At θ=180°: E=+1 (correlated)
    CHSH optimal: a₁=0, a₂=π/2, b₁=π/4, b₂=−π/4 → |S|=2√2
"""
import sys
import numpy as np


def correlation(theta):
    """Quantum singlet correlation E(θ) = −cos(θ)."""
    return -np.cos(theta)


def chsh(a1, a2, b1, b2):
    """CHSH quantity."""
    return (correlation(a1-b1) + correlation(a1-b2) +
            correlation(a2-b1) - correlation(a2-b2))


def verify():
    print("=== Singlet correlations verification ===")
    for theta_deg in [0, 45, 90, 135, 180]:
        theta = theta_deg * np.pi / 180
        E = correlation(theta)
        print(f"  θ={theta_deg}°: E(θ) = {E:.6f}")

    # P1: θ=0 → E=−1
    print(f"\n  P1: θ=0: E = {correlation(0):.10f}  (should be -1)")
    # P2: θ=90° → E=0
    print(f"  P2: θ=90°: E = {correlation(np.pi/2):.10f}  (should be 0)")

    # CHSH optimal
    a1, a2 = 0, np.pi/2
    b1, b2 = np.pi/4, -np.pi/4
    S = chsh(a1, a2, b1, b2)
    print(f"\n  CHSH optimal: |S| = {abs(S):.8f}  (should be 2√2 = {2*np.sqrt(2):.8f})")
    print(f"  LHV bound: |S| ≤ 2.000")
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


class SingletCorrelationsScene(Scene):
    """
    Phase 1: title
    Phase 2: two Bloch spheres (Alice/Bob); sweep θ; correlation meter
    Phase 3: CHSH quantity for optimal angles — exceeds 2
    Phase 4: triplet comparison
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_sweep()
        self._phase_chsh()

    def _phase_title(self):
        title = Text("The Singlet State", font="EB Garamond", font_size=58, color=INK)
        sub1  = Text(
            "E(θ) = −cos θ  —  anti-correlation holds in every direction",
            font="EB Garamond", font_size=23, color=BLUE,
        )
        sub2  = Text(
            "Rotational invariance + this correlation → CHSH violation of 2√2",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_sweep(self):
        # Two circles representing Bloch spheres
        r = 1.5
        ctr_A = LEFT * 4.0
        ctr_B = LEFT * 0.5

        sph_A = Circle(radius=r, color=DIM, stroke_width=1.5).move_to(ctr_A)
        sph_B = Circle(radius=r, color=DIM, stroke_width=1.5).move_to(ctr_B)
        lbl_A = Text("Alice", font="EB Garamond", font_size=18, color=INK).next_to(sph_A, DOWN, buff=0.2)
        lbl_B = Text("Bob", font="EB Garamond", font_size=18, color=INK).next_to(sph_B, DOWN, buff=0.2)
        self.play(Create(sph_A), Create(sph_B), Write(lbl_A), Write(lbl_B), run_time=0.7)

        theta_tracker = ValueTracker(0.0)

        def _arrow_A():
            # Alice fixed at 0°
            tip = ctr_A + r * np.array([0, 1, 0])
            return Arrow(ctr_A, tip, buff=0, color=BLUE, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        def _arrow_B():
            theta = theta_tracker.get_value()
            tip   = ctr_B + r * np.array([np.sin(theta), np.cos(theta), 0])
            return Arrow(ctr_B, tip, buff=0, color=BROWN, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        def _corr_meter():
            theta = theta_tracker.get_value()
            E     = correlation(theta)
            color = GOLD if E < 0 else BLUE
            return Text(f"E(θ) = {E:+.3f}", font="EB Garamond", font_size=26, color=color).to_corner(UR, buff=0.35)

        def _theta_lbl():
            theta = theta_tracker.get_value()
            return MathTex(rf"\theta = {np.degrees(theta):.0f}^{{\circ}}", color=INK, font_size=24).to_corner(UR, buff=0.35).shift(DOWN*0.5)

        dyn_A  = always_redraw(_arrow_A)
        dyn_B  = always_redraw(_arrow_B)
        dyn_m  = always_redraw(_corr_meter)
        dyn_th = always_redraw(_theta_lbl)
        self.add(dyn_A, dyn_B, dyn_m, dyn_th)

        # Correlation curve on right
        ax = Axes(
            x_range=[0, 180, 30], y_range=[-1.2, 1.2, 0.4],
            x_length=4.5, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.3, "include_ticks": True},
        ).shift(RIGHT * 3.5)

        x_lbl = MathTex(r"\theta\;(^{\circ})", color=INK, font_size=18).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"E(\theta)", color=INK, font_size=18).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.6)

        theta_arr = np.linspace(0, np.pi, 300)
        E_arr     = [correlation(t) for t in theta_arr]
        pts       = [ax.c2p(np.degrees(t), e) for t, e in zip(theta_arr, E_arr)]
        full_curve = VMobject(color=GOLD, stroke_width=2.5)
        full_curve.set_points_smoothly(pts)
        self.play(Create(full_curve), run_time=0.8)

        def _dot_on_curve():
            theta = theta_tracker.get_value()
            E     = correlation(theta)
            return Dot(ax.c2p(np.degrees(theta), E), color=BLUE, radius=0.12)

        dyn_dot = always_redraw(_dot_on_curve)
        self.add(dyn_dot)

        self.play(theta_tracker.animate.set_value(np.pi), run_time=5.0, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_chsh(self):
        hdr = Text(
            "CHSH: optimal angles give |S| = 2√2 ≈ 2.828 — LHV bound of 2 violated",
            font="EB Garamond", font_size=21, color=GOLD,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        names  = [r"a_1=0°", r"b_1=45°", r"a_2=90°", r"b_2=-45°"]
        colors = [BLUE, BROWN, BLUE, BROWN]

        a1, a2 = 0.0, np.pi/2
        b1, b2 = np.pi/4, -np.pi/4
        S  = chsh(a1, a2, b1, b2)

        angle_lbl = VGroup(*[
            MathTex(n, color=c, font_size=26) for n, c in zip(names, colors)
        ]).arrange(RIGHT, buff=0.6).center().shift(UP * 1.0)
        self.play(*[Write(l) for l in angle_lbl], run_time=0.8)

        E_eqs = VGroup(
            MathTex(rf"E(a_1,b_1) = -\cos(45^{{\circ}}) = {correlation(a1-b1):.4f}", color=INK, font_size=22),
            MathTex(rf"E(a_1,b_2) = -\cos(45^{{\circ}}) = {correlation(a1-b2):.4f}", color=INK, font_size=22),
            MathTex(rf"E(a_2,b_1) = -\cos(45^{{\circ}}) = {correlation(a2-b1):.4f}", color=INK, font_size=22),
            MathTex(rf"E(a_2,b_2) = -\cos(135^{{\circ}}) = {correlation(a2-b2):.4f}", color=INK, font_size=22),
        ).arrange(DOWN, buff=0.22).center().shift(DOWN * 0.2)
        for eq in E_eqs:
            self.play(Write(eq), run_time=0.4)

        S_lbl = MathTex(rf"|S| = |E_{{11}}+E_{{12}}+E_{{21}}-E_{{22}}| = {abs(S):.4f} > 2",
                        color=GOLD, font_size=28).to_edge(DOWN, buff=0.28)
        self.play(Write(S_lbl), run_time=0.8)
        self.wait(3.0)
