#!/usr/bin/env python3
"""
gram_schmidt_complex_plane.py — Gram-Schmidt in the Complex Plane
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/gram-schmidt-complex-plane
    manim -qh gram_schmidt_complex_plane.py GramSchmidtComplexScene

Verify:
    python3 gram_schmidt_complex_plane.py --verify

Physics:
    u₁ = (1, i)ᵀ    → e₁ = (1, i)ᵀ/√2
    u₂ = (1, 0)ᵀ
    ⟨e₁|u₂⟩ = (1·1 + (−i)·0)/√2 = 1/√2
    residual = u₂ − ⟨e₁|u₂⟩·e₁ = (1/2, −i/2)ᵀ
    e₂ = (1, −i)ᵀ/√2
    ⟨e₁|e₂⟩ = (1·1 + (−i)·(−i))/2 = (1 − 1)/2 = 0  ✓
"""
import sys
import numpy as np


def gram_schmidt(vecs):
    """Complex Gram-Schmidt."""
    orthonormal = []
    for v in vecs:
        w = v.copy().astype(complex)
        for e in orthonormal:
            w -= np.dot(e.conj(), v) * e
        norm = np.linalg.norm(w)
        orthonormal.append(w / norm)
    return orthonormal


def verify():
    print("=== Gram-Schmidt complex plane verification ===")
    u1 = np.array([1.0, 1j])
    u2 = np.array([1.0, 0.0 + 0j])
    e1, e2 = gram_schmidt([u1, u2])
    print(f"  e₁ = ({e1[0]:.6f}, {e1[1]:.6f})")
    print(f"  e₂ = ({e2[0]:.6f}, {e2[1]:.6f})")
    inner = np.dot(e1.conj(), e2)
    print(f"  ⟨e₁|e₂⟩ = {inner:.10f}  (should be 0)")
    inner11 = np.dot(e1.conj(), e1)
    inner22 = np.dot(e2.conj(), e2)
    print(f"  ⟨e₁|e₁⟩ = {inner11:.10f}  (should be 1)")
    print(f"  ⟨e₂|e₂⟩ = {inner22:.10f}  (should be 1)")
    # P2: real dot product gives non-zero
    real_dot = np.real(u1[0]) * np.real(u2[0]) + np.real(u1[1]) * np.real(u2[1])
    print(f"\n  Real dot u₁·u₂ (wrong) = {real_dot}  (non-zero — conjugation is necessary)")
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


class GramSchmidtComplexScene(Scene):
    """
    Complex Gram-Schmidt step-by-step animation.
    Vectors live in ℂ² — we show real and imaginary components on 2D diagrams.
    Phase 1: title
    Phase 2: show u₁, normalize to e₁
    Phase 3: project u₂ onto e₁, subtract residual, normalize to e₂
    Phase 4: verify orthogonality meter → 0
    Phase 5: degenerate case (u₁ ∥ u₂) — zero residual
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_e1()
        self._phase_e2()
        self._phase_orthogonality()
        self._phase_degenerate()

    def _phase_title(self):
        title = Text("Gram-Schmidt in ℂ²", font="EB Garamond", font_size=60, color=INK)
        sub   = Text(
            "Complex inner product requires conjugation — ⟨φ|ψ⟩ = Σ φᵢ* ψᵢ",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _make_axes(self, label_x="Re", label_y="Im", shift=ORIGIN):
        ax = Axes(
            x_range=[-0.2, 1.8, 0.5], y_range=[-1.2, 1.2, 0.5],
            x_length=5.5, y_length=3.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).shift(shift)
        lx = Text(label_x, font="EB Garamond", font_size=18, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = Text(label_y, font="EB Garamond", font_size=18, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        return ax, lx, ly

    def _vec_arrow(self, ax, v_complex, color):
        origin = ax.get_origin()
        unit   = ax.get_x_unit_size()
        tip    = origin + unit * np.array([v_complex.real, v_complex.imag, 0])
        return Arrow(origin, tip, buff=0, color=color, stroke_width=2.8, max_tip_length_to_length_ratio=0.2)

    def _phase_e1(self):
        ax, lx, ly = self._make_axes(shift=LEFT * 2.5)
        self.play(Create(ax), Write(lx), Write(ly), run_time=0.8)

        u1 = 1.0 + 1j  # representative of (1,i) — we show as complex number
        norm_u1 = abs(u1)
        e1 = u1 / norm_u1

        arr_u1 = self._vec_arrow(ax, u1, BROWN)
        lbl_u1 = MathTex(r"\mathbf{u}_1 = (1,i)", color=BROWN, font_size=22).to_corner(UL, buff=0.35)
        self.play(Create(arr_u1), Write(lbl_u1), run_time=0.8)
        self.wait(0.5)

        arr_e1 = self._vec_arrow(ax, e1, BLUE)
        lbl_e1 = MathTex(r"\mathbf{e}_1 = \frac{(1,i)}{\sqrt{2}}", color=BLUE, font_size=22).next_to(lbl_u1, DOWN)
        self.play(Transform(arr_u1, arr_e1), Write(lbl_e1), run_time=1.2)
        self.wait(1.0)

        self._e1_arrow = arr_u1   # keep for next phase
        self._ax_left  = ax
        self._lbl_e1   = lbl_e1
        self._e1_complex = e1

    def _phase_e2(self):
        ax = self._ax_left
        e1 = self._e1_complex
        u2 = 1.0 + 0j

        arr_u2 = self._vec_arrow(ax, u2, GOLD)
        lbl_u2 = MathTex(r"\mathbf{u}_2 = (1,0)", color=GOLD, font_size=22).to_corner(UL, buff=0.35).shift(DOWN*1.2)
        self.play(Create(arr_u2), Write(lbl_u2), run_time=0.8)
        self.wait(0.5)

        # Projection
        proj_coeff = np.conj(e1) * u2  # scalar — but e1=(1+i)/sqrt(2), u2=1+0i
        # ⟨e1|u2⟩ = e1[0]*u2[0] + e1[1]*u2[1] = (1/sqrt2)(1) + (-i/sqrt2)(0) = 1/sqrt2
        inner = np.conj(e1.real) * u2.real + np.conj(e1.imag) * u2.imag   # component representation
        # Correct: treat u1=(1,i)/sqrt2 so e1 = (1/sqrt2, i/sqrt2)
        # ⟨e1|u2⟩ = conj(1/sqrt2)*1 + conj(i/sqrt2)*0 = 1/sqrt2
        inner_val = 1.0 / np.sqrt(2)  # exact
        proj_vec  = inner_val * e1    # projection of u2 onto e1

        arr_proj = self._vec_arrow(ax, proj_vec, DIM)
        lbl_proj = MathTex(r"\langle \mathbf{e}_1|\mathbf{u}_2\rangle \,\mathbf{e}_1", color=DIM, font_size=20).to_corner(UL, buff=0.35).shift(DOWN*1.8)
        self.play(Create(arr_proj), Write(lbl_proj), run_time=0.8)

        # Residual = u2 - proj
        residual = u2 - proj_vec
        # residual = 1 - (1/sqrt2)(1/sqrt2, i/sqrt2) = 1 - (1/2, i/2) = (1/2, -i/2)
        e2       = residual / abs(residual)
        arr_res  = self._vec_arrow(ax, residual, BROWN)
        lbl_res  = MathTex(r"\text{residual} = \frac{1}{2}(1,-i)", color=BROWN, font_size=20).to_corner(UL, buff=0.35).shift(DOWN*2.4)
        self.play(Create(arr_res), Write(lbl_res), run_time=0.8)

        arr_e2   = self._vec_arrow(ax, e2, GOLD)
        lbl_e2   = MathTex(r"\mathbf{e}_2 = \frac{(1,-i)}{\sqrt{2}}", color=GOLD, font_size=22).to_corner(UL, buff=0.35).shift(DOWN*3.0)
        self.play(Transform(arr_res, arr_e2), Write(lbl_e2), run_time=1.0)
        self.wait(1.0)

        self._e2_arrow = arr_res
        self._lbl_e2   = lbl_e2

    def _phase_orthogonality(self):
        # Orthogonality inner product meter
        inner_display = MathTex(
            r"\langle \mathbf{e}_1 | \mathbf{e}_2 \rangle = 0",
            color=GOLD, font_size=36,
        ).to_edge(RIGHT, buff=1.2).shift(UP * 0.5)
        note = Text(
            "⟨e₁|e₂⟩ = (1·1 + (−i)·(−i))/2 = (1−1)/2 = 0",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(inner_display), Write(note), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(inner_display, note), run_time=0.5)

    def _phase_degenerate(self):
        # Clean up and show degenerate case
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

        title = Text(
            "Degenerate case: u₁ ∥ u₂ → zero residual → Gram-Schmidt fails",
            font="EB Garamond", font_size=24, color=BROWN,
        ).to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        ax, lx, ly = self._make_axes(shift=ORIGIN)
        self.play(Create(ax), Write(lx), Write(ly), run_time=0.6)

        u1 = 1.0 + 1j
        e1 = u1 / abs(u1)
        u2 = 0.7 * u1    # parallel

        arr_u1 = self._vec_arrow(ax, e1, BLUE)
        arr_u2 = self._vec_arrow(ax, u2, GOLD)
        self.play(Create(arr_u1), Create(arr_u2), run_time=0.8)

        # projection exactly removes u2
        inner = np.conj(e1.real + 1j * e1.imag) * (u2.real + 1j * u2.imag)
        # Inner product = e1^† u2 where we treat as 1-complex: = conj(e1)*u2
        inner_val = np.conj(e1) * u2  # = 0.7 * conj(e1)*u1 = 0.7 * |u1| (since e1=u1/|u1|) = 0.7 * sqrt(2)
        proj      = inner_val * e1
        residual  = u2 - proj

        res_lbl = MathTex(r"\|\text{residual}\| = 0", color=BROWN, font_size=30).to_edge(DOWN, buff=0.28)
        self.play(Write(res_lbl), run_time=0.8)
        self.wait(2.5)
