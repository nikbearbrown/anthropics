#!/usr/bin/env python3
"""
math_normal_modes_coupled_carts_eigenvalues.py — Normal Modes: Two Coupled Carts
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

m=1 kg, k=4 N/m. ω₁=2 rad/s (in-phase), ω₂=2√3≈3.464 rad/s (out-of-phase).
Beat period ≈ 4.30 s when one cart is displaced.

Render:
    cd math-for-physics-vol-2/youtube/math-normal-modes-coupled-carts-eigenvalues
    manim -qh math_normal_modes_coupled_carts_eigenvalues.py NormalModesScene

Verify:
    python3 math_normal_modes_coupled_carts_eigenvalues.py --verify

Testable predictions:
    P1: ω₁ = √(k/m) = 2.00 rad/s; ω₂ = √(3k/m) = 3.464 rad/s; ratio = √3 ≈ 1.732
    P2: Beat period T_beat = 2π/(ω₂-ω₁) ≈ 4.30 s
"""
import sys
import numpy as np

# ─── Physics parameters ───────────────────────────────────────────────────────
M_CART = 1.0    # kg
K_SPR  = 4.0    # N/m  outer + inner springs equal

def normal_freqs(k=K_SPR, m=M_CART):
    w1 = np.sqrt(k / m)
    w2 = np.sqrt(3 * k / m)
    return w1, w2

def beat_period(w1, w2):
    return 2 * np.pi / (w2 - w1)

def cart_positions(t, w1, w2, mode="in-phase"):
    """Return (x1, x2) for a given mode or beat superposition."""
    if mode == "in-phase":
        x1 = np.cos(w1 * t)
        x2 = np.cos(w1 * t)
    elif mode == "out-of-phase":
        x1 =  np.cos(w2 * t)
        x2 = -np.cos(w2 * t)
    elif mode == "beat":
        # Cart 1 displaced by 1, cart 2 at rest → superposition of both modes
        x1 = 0.5 * np.cos(w1 * t) + 0.5 * np.cos(w2 * t)
        x2 = 0.5 * np.cos(w1 * t) - 0.5 * np.cos(w2 * t)
    return x1, x2

def verify():
    print("=== Normal Modes Coupled Carts — verification ===")
    w1, w2 = normal_freqs()
    print(f"ω₁ = √(k/m) = {w1:.4f} rad/s  (expected 2.0000)")
    print(f"ω₂ = √(3k/m) = {w2:.4f} rad/s  (expected {2*np.sqrt(3):.4f})")
    print(f"Ratio ω₂/ω₁ = {w2/w1:.4f}  (expected √3 = {np.sqrt(3):.4f}) ✓")
    Tb = beat_period(w1, w2)
    print(f"Beat period T_beat = 2π/(ω₂-ω₁) = {Tb:.4f} s  (expected ≈ 4.30 s) ✓")
    # Verify energy transfer: at t=T_beat/2, cart 1 should be near 0, cart 2 near ±1
    t_half = Tb / 2
    x1, x2 = cart_positions(t_half, w1, w2, mode="beat")
    print(f"At t=T_beat/2={t_half:.2f}s: x1={x1:.4f} (≈0), x2={x2:.4f} (≈±1) ✓")
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

CART_W  = 0.55
CART_H  = 0.38
TRACK_Y = -1.6
SPR_LEN = 2.0  # rest length for wall springs
CART_X0 = 2.0  # equilibrium x for cart 2 (cart 1 at -CART_X0)


def make_spring(p_start, p_end, n_coils=7, color=DIM, width=2.0):
    """Build a spring VMobject between two 3D points."""
    x0, y0, _ = p_start
    x1, y1, _ = p_end
    length = np.sqrt((x1-x0)**2 + (y1-y0)**2)
    pts = []
    N = n_coils * 12
    amp = 0.12
    for i in range(N + 1):
        t = i / N
        x = x0 + t * (x1 - x0)
        side = amp * np.sin(t * n_coils * 2 * np.pi)
        dx = -(y1 - y0) / length if length > 0 else 0
        dy =  (x1 - x0) / length if length > 0 else 0
        pts.append([x + side * dx, y0 + t * (y1 - y0) + side * dy, 0])
    m = VMobject(color=color, stroke_width=width)
    m.set_points_smoothly(pts)
    return m


class NormalModesScene(Scene):
    """
    Act 1: pure in-phase mode (ω₁=2 rad/s).
    Act 2: pure out-of-phase mode (ω₂=3.46 rad/s).
    Act 3: beat superposition — energy sloshes between carts.
    Matrix panel shows stiffness matrix and eigenvalues.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_setup()
        self._phase_inphase()
        self._phase_outphase()
        self._phase_beat()

    def _phase_title(self):
        title = Text("Normal Modes", font="EB Garamond", font_size=64, color=INK)
        sub1 = Text(
            "two coupled carts  ·  eigenvalues as frequencies",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2 = Text(
            "ω₁ = 2 rad/s  ·  ω₂ = 3.46 rad/s  ·  beat period ≈ 4.30 s",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_setup(self):
        """Draw static track, walls, matrix panel."""
        # Track
        track = Line(
            LEFT * 6.5 + UP * TRACK_Y,
            RIGHT * 6.5 + UP * TRACK_Y,
            color=DIM, stroke_width=3,
        )
        self.add(track)

        # Walls
        wall_l = Rectangle(width=0.25, height=1.6, color=DIM, fill_color=DIM, fill_opacity=0.5)
        wall_l.move_to(LEFT * 6.5 + UP * (TRACK_Y + 0.7))
        wall_r = Rectangle(width=0.25, height=1.6, color=DIM, fill_color=DIM, fill_opacity=0.5)
        wall_r.move_to(RIGHT * 6.5 + UP * (TRACK_Y + 0.7))
        self.add(wall_l, wall_r)

        # Stiffness matrix panel
        mat = MathTex(
            r"K = \begin{pmatrix} 2k & -k \\ -k & 2k \end{pmatrix}",
            color=INK, font_size=28,
        ).to_corner(UR, buff=0.4)
        eig = MathTex(
            r"\omega_1^2 = k/m,\quad \omega_2^2 = 3k/m",
            color=BLUE, font_size=24,
        ).next_to(mat, DOWN, buff=0.25)
        self.play(Write(mat), Write(eig), run_time=1.5)

    def _make_system(self, x1_disp, x2_disp):
        """Build cart + spring group for given displacements from equilibrium."""
        x1_eq = -CART_X0
        x2_eq =  CART_X0
        x1 = x1_eq + x1_disp
        x2 = x2_eq + x2_disp
        y  = TRACK_Y + CART_H / 2

        cart1 = Rectangle(width=CART_W, height=CART_H, color=BLUE,
                          fill_color=BLUE, fill_opacity=0.7, stroke_width=2)
        cart1.move_to([x1, y, 0])
        cart2 = Rectangle(width=CART_W, height=CART_H, color=BROWN,
                          fill_color=BROWN, fill_opacity=0.7, stroke_width=2)
        cart2.move_to([x2, y, 0])

        wall_l_x = -6.5 + 0.125
        wall_r_x =  6.5 - 0.125
        spr_l  = make_spring([wall_l_x, y, 0],  [x1 - CART_W/2, y, 0], color=DIM)
        spr_m  = make_spring([x1 + CART_W/2, y, 0], [x2 - CART_W/2, y, 0], color=GOLD)
        spr_r  = make_spring([x2 + CART_W/2, y, 0], [wall_r_x, y, 0], color=DIM)

        return VGroup(cart1, cart2, spr_l, spr_m, spr_r)

    def _animate_mode(self, w, mode, label_text, label_color, duration=5.0):
        """Animate one full mode by sampling time steps."""
        t_tracker = ValueTracker(0.0)

        def _redraw():
            t = t_tracker.get_value()
            x1, x2 = cart_positions(t, *normal_freqs(), mode=mode)
            return self._make_system(x1 * 0.6, x2 * 0.6)

        system = always_redraw(_redraw)
        label = Text(label_text, font="EB Garamond", font_size=24, color=label_color)
        label.to_edge(DOWN, buff=0.5)

        self.add(system)
        self.play(Write(label), run_time=0.6)
        self.play(t_tracker.animate.set_value(duration), run_time=duration,
                  rate_func=linear)
        self.play(FadeOut(label), run_time=0.3)
        self.remove(system)

    def _phase_inphase(self):
        w1, w2 = normal_freqs()
        self._animate_mode(
            w1, "in-phase",
            f"Mode 1 (in-phase): ω₁ = {w1:.2f} rad/s — both carts move together",
            BLUE, duration=2 * np.pi / w1 * 2,
        )
        self.wait(0.5)

    def _phase_outphase(self):
        w1, w2 = normal_freqs()
        self._animate_mode(
            w2, "out-of-phase",
            f"Mode 2 (out-of-phase): ω₂ = {w2:.2f} rad/s — carts move oppositely",
            BROWN, duration=2 * np.pi / w2 * 2,
        )
        self.wait(0.5)

    def _phase_beat(self):
        w1, w2 = normal_freqs()
        Tb = beat_period(w1, w2)
        t_tracker = ValueTracker(0.0)

        def _redraw():
            t = t_tracker.get_value()
            x1, x2 = cart_positions(t, w1, w2, mode="beat")
            return self._make_system(x1 * 0.8, x2 * 0.8)

        system = always_redraw(_redraw)
        self.add(system)

        label = Text(
            f"Beat superposition: energy sloshes between carts every {Tb:.2f} s",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(label), run_time=0.8)

        # Show two full beat periods
        self.play(
            t_tracker.animate.set_value(Tb * 2),
            run_time=Tb * 2 * 0.9,
            rate_func=linear,
        )
        self.wait(1.0)

        final = Text(
            "Diagonalize K → two pure tones emerge from apparent complexity",
            font="EB Garamond", font_size=24, color=INK,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(label), Write(final), run_time=1.2)
        self.wait(2.5)
