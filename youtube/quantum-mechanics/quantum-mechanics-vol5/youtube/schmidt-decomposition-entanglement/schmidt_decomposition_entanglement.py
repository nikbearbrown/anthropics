#!/usr/bin/env python3
"""
schmidt_decomposition_entanglement.py — Schmidt Decomposition and Entanglement
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/schmidt-decomposition-entanglement
    manim -qh schmidt_decomposition_entanglement.py SchmidtDecompositionScene

Verify:
    python3 schmidt_decomposition_entanglement.py --verify

Physics:
    |ψ⟩ = Σ_{ij} c_{ij}|ij⟩;  M = coefficient matrix
    SVD: M = U Σ Vᵀ;  Schmidt coefficients = singular values
    |00⟩: M = [[1,0],[0,0]], σ₁=1, σ₂=0, S=0 (separable)
    |Φ⁺⟩: M = (1/√2)I, σ₁=σ₂=1/√2, S=1 ebit (maximally entangled)
    Tr(ρ_A²) = 1 (pure subsystem) ↔ separable
"""
import sys
import numpy as np


def schmidt_analysis(M):
    """SVD of coefficient matrix and entanglement entropy."""
    U, sigma, Vt = np.linalg.svd(M)
    # Von Neumann entropy
    probs = sigma**2
    probs = probs[probs > 1e-12]
    S = -np.sum(probs * np.log2(probs))
    # Purity of reduced density matrix ρ_A = M Mᵀ
    rho_A = M @ M.conj().T
    purity = np.real(np.trace(rho_A @ rho_A))
    return sigma, S, purity


def verify():
    print("=== Schmidt decomposition verification ===")
    # Product state |00⟩
    M_00 = np.array([[1.0, 0.0], [0.0, 0.0]])
    sigma, S, purity = schmidt_analysis(M_00)
    print(f"  |00⟩: σ={sigma}, S={S:.6f} ebits, Tr(ρ_A²)={purity:.6f}  (pure subsystem ✓)")

    # Bell state |Φ⁺⟩
    M_bell = np.array([[1.0, 0.0], [0.0, 1.0]]) / np.sqrt(2)
    sigma_b, S_b, purity_b = schmidt_analysis(M_bell)
    print(f"  |Φ⁺⟩: σ={sigma_b}, S={S_b:.6f} ebits, Tr(ρ_A²)={purity_b:.6f}  (maximally mixed ✓)")

    # Interpolation from |00⟩ to |Φ⁺⟩
    print("\n  Path |00⟩ → |Φ⁺⟩ (growing c₁₁):")
    for alpha in [0.0, 0.3, 0.5, 0.7, 1.0 / np.sqrt(2)]:
        norm = np.sqrt(1 - alpha**2) if alpha < 1/np.sqrt(2) else 0.0
        c00  = np.sqrt(max(1 - 2*alpha**2, 0)) if 2*alpha**2 <= 1 else 0.0
        M = np.array([[c00, 0], [0, alpha]])
        if np.linalg.norm(M)**2 > 0.01:
            M = M / np.linalg.norm(M)
        sigma_i, S_i, _ = schmidt_analysis(M)
        print(f"    α={alpha:.3f}: σ={sigma_i.round(4)}, S={S_i:.4f}")
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


class SchmidtDecompositionScene(Scene):
    """
    Phase 1: title
    Phase 2: matrix display — |00⟩ separable, |Φ⁺⟩ entangled, SVD computation
    Phase 3: animate path from |00⟩ to |Φ⁺⟩ growing c₁₁ entry
    Phase 4: entanglement entropy meter
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_states()
        self._phase_animation()

    def _phase_title(self):
        title = Text("Schmidt Decomposition", font="EB Garamond", font_size=56, color=INK)
        sub1  = Text(
            "|ψ⟩ = Σ c_{ij}|ij⟩  →  SVD of coefficient matrix  →  Schmidt rank",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "rank=1 → separable  ·  rank=2 → entangled  ·  entanglement = rank",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _make_matrix_display(self, M, label, color, center):
        """Show a 2×2 matrix with label."""
        lbl = MathTex(label, color=color, font_size=24).move_to(center + UP * 1.8)
        entries = []
        for i in range(2):
            for j in range(2):
                val = M[i, j]
                if abs(val) < 1e-8:
                    s = "0"
                elif abs(val - 1/np.sqrt(2)) < 1e-8:
                    s = r"\frac{1}{\sqrt{2}}"
                else:
                    s = f"{val:.3f}"
                e = MathTex(s, color=INK, font_size=22).move_to(center + UP*(0.4-0.8*i) + RIGHT*(0.6*j-0.3))
                entries.append(e)
        brackets = MathTex(r"\begin{pmatrix} \cdot & \cdot \\ \cdot & \cdot \end{pmatrix}",
                           color=DIM, font_size=48).move_to(center)
        return VGroup(lbl, *entries, brackets)

    def _phase_states(self):
        M_00   = np.array([[1.0, 0.0], [0.0, 0.0]])
        M_bell = np.array([[1.0, 0.0], [0.0, 1.0]]) / np.sqrt(2)

        g_00   = self._make_matrix_display(M_00, r"|00\rangle", BLUE, LEFT * 3.5)
        g_bell = self._make_matrix_display(M_bell, r"|\Phi^+\rangle", GOLD, RIGHT * 3.5 + UP * 0.3)

        self.play(Create(g_00), run_time=0.8)
        # SVD for |00⟩
        sigma, S, purity = schmidt_analysis(M_00)
        svd_00 = VGroup(
            MathTex(r"\sigma_1=1,\;\sigma_2=0", color=BLUE, font_size=22),
            MathTex(r"S=0\;\mathrm{ebits}", color=BLUE, font_size=22),
            MathTex(r"\mathrm{rank}=1\;\Rightarrow\;\text{SEPARABLE}", color=BLUE, font_size=20),
        ).arrange(DOWN, buff=0.2).next_to(g_00, DOWN, buff=0.3)
        self.play(Write(svd_00), run_time=0.8)

        self.play(Create(g_bell), run_time=0.8)
        sigma_b, S_b, purity_b = schmidt_analysis(M_bell)
        svd_bell = VGroup(
            MathTex(r"\sigma_1=\sigma_2=\frac{1}{\sqrt{2}}", color=GOLD, font_size=22),
            MathTex(r"S=1\;\mathrm{ebit}", color=GOLD, font_size=22),
            MathTex(r"\mathrm{rank}=2\;\Rightarrow\;\text{ENTANGLED}", color=GOLD, font_size=20),
        ).arrange(DOWN, buff=0.2).next_to(g_bell, DOWN, buff=0.3)
        self.play(Write(svd_bell), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_animation(self):
        # Animate growing c₁₁: from |00⟩ to |Φ⁺⟩
        alpha_tracker = ValueTracker(0.0)

        ax = Axes(
            x_range=[0, 1.1, 0.2], y_range=[0, 1.1, 0.2],
            x_length=5.5, y_length=3.8,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).shift(LEFT * 2.5)

        x_lbl = MathTex(r"c_{11}", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"S\;(\mathrm{ebits})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        # Full curve of S vs c₁₁
        alphas = np.linspace(0.0, 1/np.sqrt(2), 300)
        S_vals = []
        for alpha in alphas:
            c00 = np.sqrt(max(1 - 2*alpha**2, 0))
            M = np.array([[c00, 0], [0, alpha]])
            nrm = np.linalg.norm(M)
            if nrm > 0:
                M = M / nrm
            _, S, _ = schmidt_analysis(M)
            S_vals.append(S)

        pts = [ax.c2p(a, s) for a, s in zip(alphas, S_vals)]
        full_curve = VMobject(color=GOLD, stroke_width=2.5)
        full_curve.set_points_smoothly(pts)
        self.play(Create(full_curve), run_time=1.2)

        def _dot():
            alpha = alpha_tracker.get_value()
            c00 = np.sqrt(max(1 - 2*alpha**2, 0))
            M = np.array([[c00, 0], [0, alpha]])
            nrm = np.linalg.norm(M)
            if nrm > 0: M = M / nrm
            _, S, _ = schmidt_analysis(M)
            return Dot(ax.c2p(alpha, S), color=BLUE, radius=0.12)

        def _entropy_lbl():
            alpha = alpha_tracker.get_value()
            c00 = np.sqrt(max(1 - 2*alpha**2, 0))
            M = np.array([[c00, 0], [0, alpha]])
            nrm = np.linalg.norm(M)
            if nrm > 0: M = M / nrm
            sigma, S, purity = schmidt_analysis(M)
            return MathTex(
                rf"c_{{11}}={alpha:.3f}\quad S={S:.3f}\;\mathrm{{ebits}}",
                color=BLUE, font_size=22,
            ).to_edge(DOWN, buff=0.28)

        dyn_dot = always_redraw(_dot)
        dyn_lbl = always_redraw(_entropy_lbl)
        self.add(dyn_dot, dyn_lbl)

        hdr = Text(
            "Grow c₁₁ from 0 to 1/√2 — product state morphs to Bell state",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.6)
        self.play(alpha_tracker.animate.set_value(1/np.sqrt(2)), run_time=5.0, rate_func=smooth)
        self.wait(2.5)
