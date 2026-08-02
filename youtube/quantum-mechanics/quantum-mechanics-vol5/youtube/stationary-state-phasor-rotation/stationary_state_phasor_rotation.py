#!/usr/bin/env python3
"""
stationary_state_phasor_rotation.py — Rotating Phase, Frozen Probability
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/stationary-state-phasor-rotation
    manim -qh stationary_state_phasor_rotation.py StationaryStatePhasorScene

Verify:
    python3 stationary_state_phasor_rotation.py --verify

Physics (L=1 nm infinite square well, electron):
    E_n = n²π²ℏ²/(2mL²)
    E₁ ≈ 0.376 eV,  ω₁ = E₁/ℏ ≈ 5.70×10¹⁴ rad/s
    ψ_n(x,t) = ψ_n(x)·e^{-iEₙt/ℏ}
    |ψ_n(x,t)|² = |ψ_n(x)|²  (time-independent)
    superposition ψ₁+ψ₂: |ψ|² oscillates at (E₂-E₁)/ℏ = 3ω₁
"""
import sys
import numpy as np

HBAR  = 1.0545718e-34   # J·s
ME    = 9.10938e-31     # kg
EV    = 1.60218e-19     # J per eV
L     = 1e-9            # m, well width


def energy(n: int) -> float:
    """E_n in Joules."""
    return n**2 * np.pi**2 * HBAR**2 / (2 * ME * L**2)


def verify():
    print("=== Stationary state phasor verification ===")
    for n in range(1, 4):
        En = energy(n)
        omn = En / HBAR
        print(f"  n={n}: E_{n} = {En/EV:.4f} eV,  ω_{n} = {omn:.3e} rad/s")
    E1 = energy(1)
    E2 = energy(2)
    omega_beat = (E2 - E1) / HBAR
    freq_beat  = omega_beat / (2 * np.pi)
    print(f"\n  Beat frequency (n=1,2): (E₂-E₁)/h = {freq_beat:.3e} Hz")
    print(f"  Beat period: T = {1/freq_beat:.3e} s = {1/freq_beat*1e15:.2f} fs")
    # P1: for single eigenstate, |ψ(x,t)|² is exactly constant
    x = np.linspace(0, L, 100)
    psi1 = np.sqrt(2/L) * np.sin(np.pi * x / L)
    t_vals = [0, 1e-16, 5e-16]
    for t in t_vals:
        psi_t = psi1 * np.exp(-1j * energy(1) * t / HBAR)
        prob  = np.abs(psi_t)**2
        print(f"  t={t:.1e}: max |ψ|²={prob.max():.8f}, min={prob.min():.8f}")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class StationaryStatePhasorScene(Scene):
    """
    Left: phasor tips tracing unit circles at rates E_n/ℏ for n=1,2,3.
    Right: |ψ_n|² bars frozen in time.
    Bottom: superposition n=1+n=2 shows |ψ|² oscillating at beat frequency.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_single_eigenstates()
        self._phase_superposition()

    # ── Phase 1: Title ────────────────────────────────────────────────────────

    def _phase_title(self):
        title = Text("Rotating Phase, Frozen Probability", font="EB Garamond", font_size=54, color=INK)
        sub   = Text(
            "ψ(x,t) = ψ(x) · e^{−iEt/ℏ}  ·  |ψ(x,t)|² = |ψ(x)|²",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    # ── Phase 2: Three eigenstates spinning at different rates ────────────────

    def _phase_single_eigenstates(self):
        # Three phasor circles (small), stacked vertically on the left
        circle_radius = 0.75
        colors        = [BLUE, GOLD, BROWN]
        n_vals        = [1, 2, 3]
        E_vals        = [energy(n) for n in n_vals]
        omega_vals    = [E / HBAR for E in E_vals]
        # Normalise so ω₁ = 1 (display units)
        omega_disp    = [om / omega_vals[0] for om in omega_vals]

        y_positions   = [1.8, 0.0, -1.8]
        phasor_centers = [np.array([-4.5, y, 0]) for y in y_positions]

        # Draw static circles and |ψ_n|² bar skeletons on right
        circles = []
        for i, (n, col, ctr) in enumerate(zip(n_vals, colors, phasor_centers)):
            c = Circle(radius=circle_radius, color=DIM, stroke_width=1.2).move_to(ctr)
            lbl = MathTex(f"n={n}", color=col, font_size=24).next_to(c, LEFT, buff=0.2)
            self.play(Create(c), Write(lbl), run_time=0.5)
            circles.append(c)

        # Bars for |ψ_n|² on right side
        x_bar = np.linspace(0, 1, 200)
        bar_groups = []
        for i, (n, col) in enumerate(zip(n_vals, colors)):
            psi_n = np.sqrt(2) * np.sin(n * np.pi * x_bar)
            prob  = psi_n**2
            # Build bar as ParametricFunction in axes
            ax_right = Axes(
                x_range=[0, 1, 0.5], y_range=[0, 2.2, 1.0],
                x_length=3.2, y_length=1.2,
                axis_config={"color": INK, "stroke_width": 1.0, "include_ticks": False},
            ).shift(RIGHT * 2.8 + UP * y_positions[i])
            prob_pts = [ax_right.c2p(x, p) for x, p in zip(x_bar, prob)]
            curve = VMobject(color=col, stroke_width=2.5)
            curve.set_points_smoothly(prob_pts)
            lbl2 = MathTex(r"|\psi_%d|^2" % n, color=col, font_size=20).next_to(ax_right, LEFT, buff=0.1)
            self.play(Create(curve), Write(lbl2), run_time=0.7)
            bar_groups.append((ax_right, curve, lbl2))

        # Animate phasors spinning for a few revolutions
        trackers = [ValueTracker(0.0) for _ in n_vals]
        arrows   = []
        for i, (n, col, ctr, om_d) in enumerate(zip(n_vals, colors, phasor_centers, omega_disp)):
            def _make_arrow(tracker=trackers[i], c=ctr, r=circle_radius, col=col):
                th = tracker.get_value()
                tip = c + r * np.array([np.cos(th), np.sin(th), 0])
                return Arrow(c, tip, buff=0, color=col, stroke_width=2.5, max_tip_length_to_length_ratio=0.25)
            arr = always_redraw(_make_arrow)
            self.add(arr)
            arrows.append(arr)

        frozen_lbl = Text(
            "Phase rotates — probability density never changes",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(frozen_lbl), run_time=0.6)

        # Animate: n=1 makes ~2 full rotations; n=2 makes ~4, n=3 makes ~6
        self.play(
            trackers[0].animate.set_value(4 * np.pi),
            trackers[1].animate.set_value(8 * np.pi),
            trackers[2].animate.set_value(12 * np.pi),
            run_time=5.0, rate_func=linear,
        )
        self.wait(1.0)
        # Clean up
        all_objs = [c for c in circles] + [arr for arr in arrows]
        for ax_r, cv, lb in bar_groups:
            all_objs += [cv, lb]
        self.play(FadeOut(*all_objs, frozen_lbl), run_time=0.5)

    # ── Phase 3: Superposition ψ₁+ψ₂ — beating ───────────────────────────────

    def _phase_superposition(self):
        hdr = Text(
            "Superposition ψ = (ψ₁ + ψ₂)/√2 :  |ψ|² now breathes at beat frequency",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.7)

        E1  = energy(1)
        E2  = energy(2)
        omega_beat = (E2 - E1) / HBAR   # rad/s
        # Normalise time so one beat period = 4 seconds display
        T_beat_disp = 4.0               # seconds of animation per beat
        omega_norm  = 2 * np.pi / T_beat_disp

        x_arr = np.linspace(0, 1, 300)
        psi1  = np.sqrt(2) * np.sin(np.pi * x_arr)
        psi2  = np.sqrt(2) * np.sin(2 * np.pi * x_arr)

        ax = Axes(
            x_range=[0, 1, 0.5], y_range=[-0.05, 2.2, 0.5],
            x_length=9.0, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.5, "include_ticks": False},
        ).center().shift(DOWN * 0.3)

        t_tracker = ValueTracker(0.0)

        def _prob_curve():
            t  = t_tracker.get_value()
            ph = np.exp(-1j * omega_norm * t)
            psi_t = (psi1 + psi2 * ph) / np.sqrt(2)
            prob  = np.abs(psi_t)**2
            pts   = [ax.c2p(x, p) for x, p in zip(x_arr, prob)]
            c = VMobject(color=GOLD, stroke_width=2.8)
            c.set_points_smoothly(pts)
            return c

        prob_curve = always_redraw(_prob_curve)
        self.add(ax, prob_curve)

        beat_eq = MathTex(
            r"\omega_{\rm beat} = \frac{E_2 - E_1}{\hbar} = 3\omega_1",
            color=BLUE, font_size=28,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(beat_eq), run_time=0.8)

        # Animate 2 full beat periods
        self.play(t_tracker.animate.set_value(2 * T_beat_disp), run_time=8.0, rate_func=linear)
        self.wait(1.5)

        final = Text(
            "Single eigenstate: phase spins invisibly.  Mix two: interference oscillates.",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(beat_eq), Write(final), run_time=0.8)
        self.wait(2.5)
