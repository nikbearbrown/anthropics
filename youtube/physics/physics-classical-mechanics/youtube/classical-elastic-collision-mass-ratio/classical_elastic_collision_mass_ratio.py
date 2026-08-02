#!/usr/bin/env python3
"""
classical_elastic_collision_mass_ratio.py — Elastic Collision: Mass-Ratio Spectrum
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    v1f = (m1-m2)/(m1+m2)*v1
    v2f = 2m1/(m1+m2)*v1
    m1=1.0 kg, v1=5.0 m/s

Render:
    cd physics-classical-mechanics/youtube/classical-elastic-collision-mass-ratio
    manim -qh classical_elastic_collision_mass_ratio.py ElasticCollisionClassScene
"""
import sys
import numpy as np

V1 = 5.0

def v1f(m1, m2): return (m1-m2)/(m1+m2)*V1
def v2f(m1, m2): return 2*m1/(m1+m2)*V1
def ke_frac(r):  return 4*r/(1+r)**2   # fraction of KE transferred (r = m2/m1)


def verify():
    print("=== Elastic Collision (Classical Mechanics) verification ===")
    for m1, m2, label in [(1,1,"equal"), (1,10,"r=10"), (0.1,1,"r=10 inv")]:
        vf1 = v1f(m1, m2)
        vf2 = v2f(m1, m2)
        p_cons = abs(m1*V1 - m1*vf1 - m2*vf2) < 1e-8
        ke_cons= abs(0.5*m1*V1**2 - 0.5*m1*vf1**2 - 0.5*m2*vf2**2) < 1e-6
        print(f"  {label}: v1f={vf1:.4f}, v2f={vf2:.4f}, p_cons={p_cons}, ke_cons={ke_cons}")
    # P1: r=1 → v1f=0
    assert abs(v1f(1,1)) < 1e-10, "P1"
    # P2: r=10 → KE_frac=4×10/121
    r10 = ke_frac(10)
    print(f"  r=10: KE_frac={r10:.6f}  (expected {4*10/121:.6f})")
    print(f"  Peak KE transfer at r=1: {ke_frac(1):.4f}  (expected 1.0)")
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


class ElasticCollisionClassScene(Scene):
    """Ball collision + KE-transfer curve vs mass ratio."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._collision_demo()
        self._ke_transfer_curve()

    def _title(self):
        t1 = Text("Elastic Collision", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("One equation — three completely different outcomes",
                  font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"v_{2f} = \frac{2m_1}{m_1+m_2}v_1 \qquad f = \frac{4r}{(1+r)^2}\text{ peaks at }r=1",
                     color=BLUE, font_size=24)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _collision_demo(self):
        for m2, label_str, col in [(1, "r=1 (equal masses): bullet stops",
                                     GOLD),
                                    (10, "r=10 (heavy target): bullet slows",
                                     BROWN),
                                    (0.1, "r=0.1 (light target): target flies at 2v",
                                     BLUE)]:
            m1 = 1.0
            vf1 = v1f(m1, m2)
            vf2 = v2f(m1, m2)

            ax = NumberLine(x_range=[-5,12,2], length=12, color=INK,
                            include_tip=True, tip_length=0.2).shift(UP*0.5)
            self.play(Create(ax), run_time=0.4)

            b1 = Circle(radius=0.3, color=BLUE, fill_color=BLUE, fill_opacity=0.7).move_to(ax.n2p(-2))
            r_size = min(0.3 * m2**0.25, 0.8)
            b2 = Circle(radius=r_size, color=BROWN, fill_color=BROWN, fill_opacity=0.7).move_to(ax.n2p(4))
            lbl = Text(label_str, font="EB Garamond", font_size=19, color=col).to_edge(DOWN, buff=0.22)

            self.play(FadeIn(b1, b2), Write(lbl), run_time=0.5)
            # Slide b1 to collision
            self.play(b1.animate.move_to(ax.n2p(4-0.3-r_size)), run_time=0.8, rate_func=linear)
            # After collision
            target_b1 = ax.n2p(4-0.3-r_size + max(vf1*0.5, -3))
            target_b2 = ax.n2p(4 + vf2*0.6)
            self.play(
                b1.animate.move_to(target_b1),
                b2.animate.move_to(target_b2),
                run_time=1.0, rate_func=smooth,
            )
            v_lbl1 = Text(f"v₁f = {vf1:.2f} m/s", font="EB Garamond", font_size=16, color=BLUE).next_to(b1, UP, buff=0.1)
            v_lbl2 = Text(f"v₂f = {vf2:.2f} m/s", font="EB Garamond", font_size=16, color=BROWN).next_to(b2, UP, buff=0.1)
            self.play(Write(v_lbl1), Write(v_lbl2), run_time=0.5)
            self.wait(1.0)
            self.play(FadeOut(ax, b1, b2, lbl, v_lbl1, v_lbl2), run_time=0.3)

    def _ke_transfer_curve(self):
        ax = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 1.1, 0.25],
            x_length=10,
            y_length=5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.4)
        lx = Text("log₁₀(m₂/m₁)", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("KE fraction transferred", font="EB Garamond", font_size=18, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("KE transfer peaks at equal masses (r=1)",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        log_rs = np.linspace(-2, 2, 500)
        rs     = 10**log_rs
        fracs  = ke_frac(rs)
        pts    = np.array([ax.c2p(lr, f) for lr, f in zip(log_rs, fracs)])
        crv    = VMobject(color=GOLD, stroke_width=3.0).set_points_smoothly(pts)
        self.play(Create(crv), run_time=2.0)

        peak = Dot(ax.c2p(0, 1.0), color=BLUE, radius=0.11)
        peak_lbl = Text("r=1: 100% transfer", font="EB Garamond", font_size=19, color=BLUE).next_to(peak, UR, buff=0.1)
        nmod_lbl = Text("r=12 (C moderator): 33%", font="EB Garamond", font_size=17, color=BROWN)
        nmod_lbl.move_to(ax.c2p(1.1, ke_frac(12)+0.05))

        self.play(FadeIn(peak), Write(peak_lbl), run_time=0.7)

        nmod_dot = Dot(ax.c2p(np.log10(12), ke_frac(12)), color=BROWN, radius=0.09)
        self.play(FadeIn(nmod_dot), Write(nmod_lbl), run_time=0.6)

        final = Text(
            "Nuclear reactor: hydrogen (r≈1) slows neutrons in one hit; carbon (r≈12) needs ten",
            font="EB Garamond", font_size=19, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
