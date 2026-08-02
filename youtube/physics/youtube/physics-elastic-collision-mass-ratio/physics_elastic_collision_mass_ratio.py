#!/usr/bin/env python3
"""
physics_elastic_collision_mass_ratio.py — Elastic Collision Mass-Ratio Morph
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    v1f = (m1-m2)/(m1+m2) * v1
    v2f = 2*m1/(m1+m2) * v1
    m1 = m2 = 1 kg, v1 = 2 m/s → v1f=0, v2f=2 m/s (cue ball stops)
    m1=10, m2=1 → v1f=1.636, v2f=3.636
    m1=1, m2=10 → v1f=-1.636, v2f=0.364

Render:
    cd physics/youtube/physics-elastic-collision-mass-ratio
    manim -qh physics_elastic_collision_mass_ratio.py ElasticCollisionScene
"""
import sys
import numpy as np

V1_INIT = 2.0  # m/s

def v1f(m1, m2): return (m1-m2)/(m1+m2) * V1_INIT
def v2f(m1, m2): return 2*m1/(m1+m2) * V1_INIT
def ke(m, v):    return 0.5*m*v**2


def verify():
    print("=== Elastic Collision verification ===")
    cases = [(1,1,"equal"), (10,1,"heavy bullet"), (1,10,"light bullet")]
    for m1,m2,name in cases:
        vf1 = v1f(m1,m2)
        vf2 = v2f(m1,m2)
        p_before = m1*V1_INIT
        p_after  = m1*vf1 + m2*vf2
        ke_before = ke(m1,V1_INIT)
        ke_after  = ke(m1,vf1) + ke(m2,vf2)
        print(f"  {name}: v1f={vf1:.4f}, v2f={vf2:.4f}")
        print(f"    Δp={p_after-p_before:.6f}  ΔKE={ke_after-ke_before:.6f}")
    # P1: equal mass v1f=0 exact
    assert abs(v1f(1,1)) < 1e-10, "P1 failed"
    # P2: r=100 (heavy bullet), v2f → 2v1
    vf2_r100 = v2f(100,1)
    print(f"  r=100: v2f={vf2_r100:.4f} m/s  (expected ≈3.960, limit=4.0)")
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


class ElasticCollisionScene(Scene):
    """Three scenarios + KE transfer curve vs mass ratio."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._three_scenarios()
        self._ke_transfer_curve()

    def _title(self):
        t1 = Text("Elastic Collision", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("Mass ratio determines everything — three regimes", font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(
            r"v_{1f} = \frac{m_1-m_2}{m_1+m_2}v_1\qquad v_{2f} = \frac{2m_1}{m_1+m_2}v_1",
            color=BLUE, font_size=28)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _three_scenarios(self):
        cases = [
            (1, 1, "m₁ = m₂  (Newton's cradle): v₁f = 0, v₂f = 2.0 m/s"),
            (10, 1, "m₁ = 10m₂ (heavy bullet): v₁f = 1.64, v₂f = 3.64 m/s"),
            (1, 10, "m₁ = m₂/10 (ping-pong on wall): v₁f = −1.64, v₂f = 0.36 m/s"),
        ]
        for m1, m2, desc in cases:
            vf1 = v1f(m1, m2)
            vf2 = v2f(m1, m2)
            # Draw block animation schematically
            ax = NumberLine(x_range=[-5, 10, 2], length=10, color=INK,
                            include_tip=True, tip_length=0.2).shift(UP*0.4)
            self.play(Create(ax), run_time=0.6)

            b1 = Square(side_length=0.7, color=BLUE, fill_color=BLUE, fill_opacity=0.6).move_to(ax.n2p(-2))
            b2 = Square(side_length=0.7*(m2/m1)**0.33, color=BROWN, fill_color=BROWN, fill_opacity=0.6).move_to(ax.n2p(3))
            arr1_pre = Arrow(b1.get_right(), b1.get_right()+RIGHT*1.0, color=BLUE, buff=0, stroke_width=2)
            arr2_pre = Text("rest", font="EB Garamond", font_size=16, color=DIM).next_to(b2, UP, buff=0.1)
            info = Text(desc, font="EB Garamond", font_size=19, color=INK).to_edge(DOWN, buff=0.22)
            self.play(FadeIn(b1, b2, arr1_pre, arr2_pre), Write(info), run_time=0.8)
            # Move b1 toward b2
            self.play(b1.animate.move_to(ax.n2p(2.3)), arr1_pre.animate.move_to(ax.n2p(1.0)+UP*0.35),
                      run_time=0.7)
            # After collision: update arrows
            self.play(FadeOut(arr1_pre, arr2_pre), run_time=0.1)
            sign1 = "→" if vf1 >= 0 else "←"
            sign2 = "→"
            lbl1 = Text(f"{sign1} {abs(vf1):.2f} m/s", font="EB Garamond", font_size=17, color=BLUE).next_to(b1, UP, buff=0.1)
            lbl2 = Text(f"{sign2} {abs(vf2):.2f} m/s", font="EB Garamond", font_size=17, color=BROWN).next_to(b2, UP, buff=0.1)
            self.play(Write(lbl1), Write(lbl2), run_time=0.7)
            self.wait(1.0)
            self.play(FadeOut(ax, b1, b2, lbl1, lbl2, info), run_time=0.4)

    def _ke_transfer_curve(self):
        ax = Axes(
            x_range=[-2, 2, 1],  # log10 of mass ratio
            y_range=[0, 1.1, 0.25],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.5)
        lx = Text("log₁₀(m₂/m₁)", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("KE transferred", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Fraction of KE transferred to target", font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        log_rs = np.linspace(-2, 2, 500)
        rs = 10**log_rs
        # fraction = 4r/(1+r)² where r = m2/m1
        fracs = 4*rs / (1+rs)**2
        pts = np.array([ax.c2p(lr, f) for lr, f in zip(log_rs, fracs)])
        crv = VMobject(color=GOLD, stroke_width=3.0).set_points_smoothly(pts)
        self.play(Create(crv), run_time=2.0)

        # Peak at r=1
        peak_dot = Dot(ax.c2p(0, 1.0), color=BLUE, radius=0.11)
        peak_lbl = Text("r=1: 100% transfer (cue ball stops)", font="EB Garamond", font_size=18, color=BLUE)
        peak_lbl.next_to(peak_dot, UR, buff=0.12)
        self.play(FadeIn(peak_dot), Write(peak_lbl), run_time=0.8)

        final = Text(
            "Peak KE transfer at equal masses — the physics behind Newton's cradle",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
