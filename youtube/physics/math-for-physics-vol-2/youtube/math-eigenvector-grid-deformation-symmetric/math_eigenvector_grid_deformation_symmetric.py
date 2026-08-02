#!/usr/bin/env python3
"""
math_eigenvector_grid_deformation_symmetric.py — Eigenvector Grid Deformation
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

A = [[2,1],[1,2]]. λ₁=3, λ₂=1. Eigenvectors at 45°.
Grid deforms; eigenvector directions only stretch — never rotate.

Render:
    cd math-for-physics-vol-2/youtube/math-eigenvector-grid-deformation-symmetric
    manim -qh math_eigenvector_grid_deformation_symmetric.py EigenvectorGridScene

Verify:
    python3 math_eigenvector_grid_deformation_symmetric.py --verify

Testable predictions:
    P1: Av₁ = 3v₁ (no angular change, magnitude tripled)
    P2: det(A) = λ₁×λ₂ = 3; tr(A) = λ₁+λ₂ = 4
"""
import sys
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 2.0]])

def get_eigensystem():
    evals, evecs = np.linalg.eigh(A)
    return evals, evecs  # evals sorted ascending: [1, 3]

def apply_matrix(v):
    return A @ v

def verify():
    print("=== Eigenvector Grid Deformation — verification ===")
    evals, evecs = get_eigensystem()
    print(f"Matrix A = [[2,1],[1,2]]")
    print(f"Eigenvalues: λ₁={evals[0]:.1f}, λ₂={evals[1]:.1f}  (expected 1, 3) {'✓' if list(evals)==[1,3] else '✗'}")
    print(f"Eigenvectors: v₁={evecs[:,0]}, v₂={evecs[:,1]}")

    v1 = evecs[:, 1]  # λ=3 eigenvector (index 1 in ascending sort)
    v2 = evecs[:, 0]  # λ=1 eigenvector
    Av1 = apply_matrix(v1)
    Av2 = apply_matrix(v2)
    print(f"P1: A·v₁ = {Av1}  =? 3·v₁ = {3*v1}  {'✓' if np.allclose(Av1, 3*v1) else '✗'}")
    print(f"    A·v₂ = {Av2}  =? 1·v₂ = {1*v2}  {'✓' if np.allclose(Av2, 1*v2) else '✗'}")

    # Generic vector
    v_gen = np.array([1.0, 0.0])
    Av_gen = apply_matrix(v_gen)
    angle_in  = np.arctan2(v_gen[1], v_gen[0]) * 180 / np.pi
    angle_out = np.arctan2(Av_gen[1], Av_gen[0]) * 180 / np.pi
    print(f"Generic v=(1,0): angle before={angle_in:.1f}°, after={angle_out:.1f}° (ROTATED ✓)")

    print(f"P2: det(A) = {np.linalg.det(A):.1f}  (= λ₁×λ₂ = 3) {'✓' if abs(np.linalg.det(A)-3)<1e-9 else '✗'}")
    print(f"    tr(A)  = {np.trace(A):.1f}   (= λ₁+λ₂ = 4) {'✓' if abs(np.trace(A)-4)<1e-9 else '✗'}")
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


class EigenvectorGridScene(Scene):
    """
    2D grid before → after transformation by A=[[2,1],[1,2]].
    Eigenvector arrows shown: only stretch, never rotate.
    Generic vector visibly rotates+stretches.
    """

    GRID_RANGE = 2.5
    SCALE = 1.4  # screen units per unit vector

    def _vec_to_screen(self, v, origin=ORIGIN):
        return origin + np.array([v[0] * self.SCALE, v[1] * self.SCALE, 0])

    def _make_grid(self, transform=None, color=DIM, opacity=0.35):
        """Build a grid of lines; optionally apply 2×2 transform to all points."""
        lines = []
        N = int(self.GRID_RANGE)
        for i in range(-N, N + 1):
            # Horizontal line at y=i
            p1 = np.array([float(-self.GRID_RANGE), float(i)])
            p2 = np.array([float(self.GRID_RANGE),  float(i)])
            p3 = np.array([float(i), float(-self.GRID_RANGE)])
            p4 = np.array([float(i), float(self.GRID_RANGE)])
            if transform is not None:
                p1 = transform @ p1
                p2 = transform @ p2
                p3 = transform @ p3
                p4 = transform @ p4
            lines.append(Line(
                self._vec_to_screen(p1), self._vec_to_screen(p2),
                color=color, stroke_opacity=opacity, stroke_width=1.2,
            ))
            lines.append(Line(
                self._vec_to_screen(p3), self._vec_to_screen(p4),
                color=color, stroke_opacity=opacity, stroke_width=1.2,
            ))
        return VGroup(*lines)

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_grid_transform()
        self._phase_eigenvectors()
        self._phase_generic_vector()

    def _phase_title(self):
        title = Text("Eigenvector Grid Deformation", font="EB Garamond", font_size=54, color=INK)
        sub1 = Text(
            "A = [[2,1],[1,2]]  ·  λ₁ = 3, λ₂ = 1  ·  eigenvectors at 45°",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "The two special directions only stretch — every other direction rotates",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_grid_transform(self):
        grid_before = self._make_grid(color=BLUE, opacity=0.30)
        grid_after  = self._make_grid(transform=A, color=BROWN, opacity=0.30)

        mat_lbl = MathTex(
            r"A = \begin{pmatrix}2&1\\1&2\end{pmatrix}\;\lambda_1=3,\;\lambda_2=1",
            color=INK, font_size=26,
        ).to_corner(UR, buff=0.45)

        self.play(Create(grid_before), Write(mat_lbl), run_time=1.8)
        before_lbl = Text("Before", font="EB Garamond", font_size=22, color=BLUE).to_edge(DOWN, buff=0.6)
        self.play(Write(before_lbl), run_time=0.5)
        self.wait(0.8)

        self.play(
            ReplacementTransform(grid_before, grid_after),
            FadeOut(before_lbl),
            run_time=2.5,
        )
        after_lbl = Text("After: A·(grid)", font="EB Garamond", font_size=22, color=BROWN).to_edge(DOWN, buff=0.6)
        self.play(Write(after_lbl), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(after_lbl, grid_after), run_time=0.5)

        self._mat_lbl = mat_lbl

    def _phase_eigenvectors(self):
        evals, evecs = get_eigensystem()
        v1 = evecs[:, 1]  # λ=3
        v2 = evecs[:, 0]  # λ=1

        origin = ORIGIN

        # Before arrows
        arr1_before = Arrow(
            origin, self._vec_to_screen(v1),
            color=GOLD, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )
        arr2_before = Arrow(
            origin, self._vec_to_screen(v2),
            color=BROWN, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )

        lbl1_b = MathTex(r"\mathbf{v}_1\;(\lambda=3)", color=GOLD, font_size=22)
        lbl1_b.next_to(self._vec_to_screen(v1), UR, buff=0.1)
        lbl2_b = MathTex(r"\mathbf{v}_2\;(\lambda=1)", color=BROWN, font_size=22)
        lbl2_b.next_to(self._vec_to_screen(v2), DR, buff=0.1)

        # After arrows: Av1 = 3v1, Av2 = 1v2
        Av1 = A @ v1
        Av2 = A @ v2
        arr1_after = Arrow(
            origin, self._vec_to_screen(Av1),
            color=GOLD, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )
        arr2_after = Arrow(
            origin, self._vec_to_screen(Av2),
            color=BROWN, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )

        self.play(Create(arr1_before), Create(arr2_before),
                  Write(lbl1_b), Write(lbl2_b), run_time=1.2)
        self.wait(0.8)

        caption_before = Text(
            "Eigenvector arrows — before transformation",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(caption_before), run_time=0.6)
        self.wait(0.7)

        self.play(
            Transform(arr1_before, arr1_after),
            Transform(arr2_before, arr2_after),
            run_time=2.0,
        )
        caption_after = Text(
            "After A: v₁ stretched ×3, v₂ unchanged — both arrows still point at 45°",
            font="EB Garamond", font_size=21, color=GOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(caption_before), Write(caption_after), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(arr1_before, arr2_before, lbl1_b, lbl2_b, caption_after),
            run_time=0.5,
        )

    def _phase_generic_vector(self):
        origin = ORIGIN
        v_gen = np.array([1.0, 0.0])
        Av_gen = A @ v_gen

        arr_before = Arrow(
            origin, self._vec_to_screen(v_gen),
            color=BLUE, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )
        arr_after = Arrow(
            origin, self._vec_to_screen(Av_gen),
            color=BLUE, stroke_width=4, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )

        angle_in  = 0.0
        angle_out = np.arctan2(Av_gen[1], Av_gen[0]) * 180 / np.pi

        lbl_b = MathTex(r"\mathbf{v}=(1,0)", color=BLUE, font_size=24)
        lbl_b.next_to(self._vec_to_screen(v_gen), RIGHT, buff=0.15)
        lbl_a = MathTex(r"A\mathbf{v}=(2,1)", color=BLUE, font_size=24)
        lbl_a.next_to(self._vec_to_screen(Av_gen), UR, buff=0.12)

        caption = Text(
            f"Generic v=(1,0): direction rotates {angle_in:.0f}° → {angle_out:.1f}° AND stretches",
            font="EB Garamond", font_size=21, color=BLUE,
        ).to_edge(DOWN, buff=0.5)

        self.play(Create(arr_before), Write(lbl_b), run_time=0.8)
        self.play(Write(caption), run_time=0.6)
        self.play(Transform(arr_before, arr_after), FadeOut(lbl_b), Write(lbl_a), run_time=1.8)
        self.wait(1.5)

        final = Text(
            "Eigenvectors: the only directions a matrix cannot rotate",
            font="EB Garamond", font_size=26, color=GOLD,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(caption, arr_before, lbl_a, self._mat_lbl), Write(final), run_time=1.2)
        self.wait(2.5)
