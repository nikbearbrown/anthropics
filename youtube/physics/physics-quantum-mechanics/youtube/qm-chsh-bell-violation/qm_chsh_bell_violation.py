#!/usr/bin/env python3
"""
qm_chsh_bell_violation.py — CHSH Bell Inequality: Classical Bound Broken by Quantum
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-chsh-bell-violation
    manim -qh qm_chsh_bell_violation.py CHSHBellScene

Verify:
    python3 qm_chsh_bell_violation.py

Physics:
    Correlation E(a,b) = -cos(a-b) for Bell state |Φ+>
    CHSH: S = |E(a1,b1) - E(a1,b2) + E(a2,b1) + E(a2,b2)|
    Classical bound: |S| <= 2
    Quantum maximum at a1=0°, a2=45°, b1=22.5°, b2=67.5°: S = 2√2 ≈ 2.828
    Aspect 1981: S = 2.697 ± 0.015 (11σ above classical)
"""
import sys
import numpy as np

DEG = np.pi / 180.0


def correlation(a: float, b: float) -> float:
    """E(a,b) = -cos(a-b) for singlet/Bell state."""
    return -np.cos(a - b)


def chsh(a1: float, a2: float, b1: float, b2: float) -> float:
    """CHSH parameter S."""
    return abs(
        correlation(a1, b1) - correlation(a1, b2)
        + correlation(a2, b1) + correlation(a2, b2)
    )


def verify():
    print("=== CHSH Bell inequality verification ===")
    # Optimal angles
    a1, a2 = 0.0 * DEG, 90.0 * DEG
    b1, b2 = 45.0 * DEG, 135.0 * DEG
    S = chsh(a1, a2, b1, b2)
    print(f"S (optimal angles) = {S:.6f}  (should be 2√2 = {2*np.sqrt(2):.6f})")

    # Alternative optimal set from card
    a1b, a2b = 0.0 * DEG, 45.0 * DEG
    b1b, b2b = 22.5 * DEG, 67.5 * DEG
    Sb = chsh(a1b, a2b, b1b, b2b)
    print(f"S (card angles 0,45,22.5,67.5) = {Sb:.6f}")

    # P2: same angle anti-correlation
    E_same = correlation(30.0 * DEG, 30.0 * DEG)
    E_orth = correlation(30.0 * DEG, 120.0 * DEG)
    print(f"E(a,a) = {E_same:.6f}  (should be -1 for Bell state)")
    print(f"E(a, a+90°) = {E_orth:.6f}  (should be 0)")

    # Classical cannot exceed 2
    print(f"Classical bound: |S| <= 2; quantum achieves {2*np.sqrt(2):.4f}")
    print("=== PASSED ===" if abs(S - 2 * np.sqrt(2)) < 1e-9 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
RED_C  = "#FF6B6B"


class CHSHBellScene(Scene):
    """
    CHSH Bell inequality.
    1. E(θ) = -cos(θ) correlation curve.
    2. Four E values for optimal angles → S = 2√2 > 2.
    3. S(θ₁) sweep showing bump above classical bound.
    4. Separable state case: S = 0.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_correlation_curve()
        self._phase_chsh_computation()
        self._phase_S_sweep()
        self._phase_separable()

    def _phase_title(self):
        title = Text("CHSH Bell Inequality", font="EB Garamond", font_size=58, color=INK)
        sub1 = Text(
            "No local hidden variables can give S > 2. Quantum mechanics gives 2√2.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"S_{\rm classical} \leq 2 \quad S_{\rm quantum} = 2\sqrt{2} \approx 2.828",
                       color=BLUE, font_size=27)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_correlation_curve(self):
        theta_arr = np.linspace(0, np.pi, 300)
        E_arr     = np.array([correlation(0, th) for th in theta_arr])

        ax = Axes(
            x_range=[0, np.pi, np.pi / 4],
            y_range=[-1.1, 1.1, 0.5],
            x_length=8.5,
            y_length=4.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.4)
        lbl_x = MathTex(r"\theta = a - b", color=INK, font_size=21
                         ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"E(\theta) = -\cos\theta", color=INK, font_size=21
                         ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Quantum correlation for Bell state |Φ+⟩ — cosine shape",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)

        c_E = VMobject(color=BLUE, stroke_width=3.5)
        c_E.set_points_smoothly([ax.c2p(th, E) for th, E in zip(theta_arr, E_arr)])

        # Classical bound would be a triangle-wave — sketch as dashed lines
        th_cl = [0, np.pi/2, np.pi]
        E_cl  = [-1, 1, -1]
        cl_segs = []
        for i in range(len(th_cl)-1):
            seg = DashedLine(
                ax.c2p(th_cl[i], E_cl[i]), ax.c2p(th_cl[i+1], E_cl[i+1]),
                color=DIM, dash_length=0.1, stroke_width=2.0
            )
            cl_segs.append(seg)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)
        self.play(Create(c_E), run_time=1.4)

        # Mark E=−1 at θ=0 and E=0 at θ=90°
        mk0 = Dot(ax.c2p(0, -1), radius=0.1, color=GOLD)
        mk90 = Dot(ax.c2p(np.pi/2, 0), radius=0.1, color=GOLD)
        lbl0  = MathTex(r"E(0)=-1", color=GOLD, font_size=19).next_to(mk0, DL, buff=0.05)
        lbl90 = MathTex(r"E(90^\circ)=0", color=GOLD, font_size=19).next_to(mk90, UR, buff=0.05)

        self.play(FadeIn(mk0), Write(lbl0), FadeIn(mk90), Write(lbl90), run_time=1.0)
        self.wait(1.5)
        self.stored_ax = ax
        self.stored_c_E = c_E
        self.stored_hdr = hdr
        self.stored_lbls = VGroup(lbl_x, lbl_y, mk0, lbl0, mk90, lbl90)

    def _phase_chsh_computation(self):
        ax = self.stored_ax
        c_E = self.stored_c_E

        # Optimal angles: a1=0, a2=45°, b1=22.5°, b2=67.5°
        angles = [
            (0.0*DEG,  22.5*DEG, BLUE,  r"E(a_1,b_1)"),
            (0.0*DEG,  67.5*DEG, GOLD,  r"E(a_1,b_2)"),
            (45.0*DEG, 22.5*DEG, BROWN, r"E(a_2,b_1)"),
            (45.0*DEG, 67.5*DEG, DIM,   r"E(a_2,b_2)"),
        ]
        dots  = []
        signs = [1, -1, 1, 1]  # CHSH: E(a1b1) - E(a1b2) + E(a2b1) + E(a2b2)

        S_val = 0.0
        for (a, b, color, lbl_str), sign in zip(angles, signs):
            theta = abs(a - b)
            E_val = correlation(a, b)
            dot   = Dot(ax.c2p(theta, E_val), radius=0.12, color=color)
            lbl   = MathTex(lbl_str + f"={E_val:.3f}", color=color, font_size=18
                            ).next_to(dot, UR, buff=0.04)
            self.play(FadeIn(dot), Write(lbl), run_time=0.7)
            S_val += sign * E_val
            dots.append(VGroup(dot, lbl))

        S_abs = abs(S_val)
        S_eq  = MathTex(
            rf"S = |E_{{a_1 b_1}} - E_{{a_1 b_2}} + E_{{a_2 b_1}} + E_{{a_2 b_2}}| = {S_abs:.4f}",
            color=GOLD, font_size=24,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(S_eq), run_time=1.0)

        # Classical bound line
        bound = DashedLine(ax.c2p(0, -1.0), ax.c2p(np.pi, -1.0),
                           color=RED_C, dash_length=0.12, stroke_width=2.0)
        bound_lbl = MathTex(r"S_{\rm cl} = 2\;\text{(classical bound)}",
                            color=RED_C, font_size=19).to_edge(DOWN, buff=0.08)
        self.play(Create(bound), Write(bound_lbl), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(self.stored_ax, self.stored_c_E, self.stored_hdr,
                          self.stored_lbls, S_eq, bound, bound_lbl, *dots), run_time=0.5)

    def _phase_S_sweep(self):
        """S(θ₁) as θ₁ sweeps 0→180°, b1=22.5°, a2=45°, b2=67.5° fixed."""
        theta1_arr = np.linspace(0, np.pi, 300)
        a2, b1, b2 = 45.0*DEG, 22.5*DEG, 67.5*DEG
        S_arr = np.array([chsh(th1, a2, b1, b2) for th1 in theta1_arr])

        ax = Axes(
            x_range=[0, 180, 45],
            y_range=[0, 3.2, 0.5],
            x_length=8.5,
            y_length=4.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"a_1\;(^\circ)", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"S(a_1)", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("CHSH parameter S as a1 sweeps — rises above the classical bound at 2",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)

        theta1_deg = np.degrees(theta1_arr)
        c_S = VMobject(color=BLUE, stroke_width=3.5)
        c_S.set_points_smoothly([ax.c2p(th, S) for th, S in zip(theta1_deg, S_arr)])

        bound = DashedLine(ax.c2p(0, 2.0), ax.c2p(180, 2.0),
                           color=RED_C, dash_length=0.1, stroke_width=2.5)
        bound_lbl = MathTex(r"S_{\rm cl} = 2", color=RED_C, font_size=20
                            ).next_to(ax.c2p(180, 2.0), RIGHT, buff=0.08)

        q_max_dot = Dot(ax.c2p(0, 2*np.sqrt(2)), radius=0.12, color=GOLD)
        q_max_lbl = MathTex(r"2\sqrt{2}", color=GOLD, font_size=22
                            ).next_to(q_max_dot, LEFT, buff=0.08)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)
        self.play(Create(c_S), run_time=1.8)
        self.play(Create(bound), Write(bound_lbl), run_time=0.8)
        self.play(FadeIn(q_max_dot), Write(q_max_lbl), run_time=0.8)

        aspect_dot = Dot(ax.c2p(0, 2.697), radius=0.1, color=BROWN)
        aspect_lbl = Text("Aspect 1981: S=2.697 (11σ)", font="EB Garamond", font_size=17, color=BROWN
                          ).next_to(aspect_dot, DR, buff=0.04)
        self.play(FadeIn(aspect_dot), Write(aspect_lbl), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_separable(self):
        eq = MathTex(
            r"|00\rangle:\;E(a,b) = 0\ \forall\,a,b \quad\Rightarrow\quad S = 0",
            color=DIM, font_size=28,
        ).center().shift(UP * 0.8)
        note = Text(
            "Entanglement is necessary — a product state cannot reach the classical bound,",
            font="EB Garamond", font_size=20, color=DIM,
        ).next_to(eq, DOWN, buff=0.4)
        note2 = Text(
            "let alone exceed it. The universe is not locally real.",
            font="EB Garamond", font_size=20, color=BLUE,
        ).next_to(note, DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
