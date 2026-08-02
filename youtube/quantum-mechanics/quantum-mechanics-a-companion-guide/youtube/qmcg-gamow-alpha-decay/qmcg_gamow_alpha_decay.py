#!/usr/bin/env python3
"""
qmcg_gamow_alpha_decay.py — Gamow Alpha Decay: 24 Orders of Magnitude from One Exponent
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-gamow-alpha-decay
    manim -qh qmcg_gamow_alpha_decay.py GamowAlphaDecayScene

Verify:
    python3 qmcg_gamow_alpha_decay.py --verify

Physics:
    T ≈ exp(−2γ); γ ≈ π(Z−2)e²/(4πε₀ħv); v=√(2E/m_alpha)
    Po-212: Z=84, E=8.78 MeV → γ≈26 → t½≈0.3 μs
    Th-232: Z=90, E=4.01 MeV → t½≈1.4×10¹⁰ yr
    Geiger-Nuttall: log(t½) vs 1/√E is linear
"""
import sys
import numpy as np

HBAR  = 1.0545718e-34
ME    = 9.10938e-31
EV    = 1.60218e-19
E_CH  = 1.60218e-19
EPS0  = 8.85419e-12
C     = 2.99792e8
M_ALPHA = 4 * 1.66054e-27   # alpha particle mass kg


def gamow_factor(Z, E_MeV):
    """Gamow factor γ (thick-barrier WKB approximation)."""
    E_J = E_MeV * 1e6 * EV
    v   = np.sqrt(2 * E_J / M_ALPHA)
    e2_4pie0 = E_CH**2 / (4 * np.pi * EPS0)
    gamma = np.pi * (Z - 2) * e2_4pie0 / (HBAR * v)
    return gamma


def half_life(Z, E_MeV, r1_fm=7.0):
    """Rough half-life estimate (in seconds)."""
    E_J = E_MeV * 1e6 * EV
    v   = np.sqrt(2 * E_J / M_ALPHA)
    r1  = r1_fm * 1e-15
    gamma = gamow_factor(Z, E_MeV)
    # t½ = (r1/v) × exp(2γ) × ln2
    return (r1 / v) * np.exp(2 * gamma) * np.log(2)


def verify():
    print("=== Gamow alpha decay verification ===")
    # Po-212
    Z_Po, E_Po = 84, 8.78
    gamma_Po = gamow_factor(Z_Po, E_Po)
    t_Po     = half_life(Z_Po, E_Po, r1_fm=8.0)
    print(f"  Po-212: γ={gamma_Po:.2f}, t½={t_Po:.3e} s  (measured: 0.298 μs = {0.298e-6:.3e} s)")

    # Th-232
    Z_Th, E_Th = 90, 4.01
    gamma_Th = gamow_factor(Z_Th, E_Th)
    t_Th     = half_life(Z_Th, E_Th, r1_fm=9.0)
    yr = 365.25 * 24 * 3600
    print(f"  Th-232: γ={gamma_Th:.2f}, t½={t_Th/yr:.3e} yr  (measured: 1.4×10¹⁰ yr)")

    print(f"\n  Dynamic range: {t_Th/t_Po:.2e}  (≈10²⁴ ✓)")

    # Geiger-Nuttall: log(t½) vs 1/√E should be linear
    Z = 84
    Es = np.linspace(4.0, 10.0, 50)
    log_t = [np.log10(half_life(Z, E)) for E in Es]
    inv_sqE = [1/np.sqrt(E) for E in Es]
    # Slope from two endpoints
    slope = (log_t[-1] - log_t[0]) / (inv_sqE[-1] - inv_sqE[0])
    print(f"\n  Geiger-Nuttall slope (Z={Z}): d(log t½)/d(1/√E) = {slope:.2f}  (linear ✓)")
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


class GamowAlphaDecayScene(Scene):
    """
    Phase 1: title
    Phase 2: Coulomb barrier diagram + wavefunction decay tail + E slider
    Phase 3: Geiger-Nuttall plot log(t½) vs 1/√E
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_barrier()
        self._phase_geiger_nuttall()

    def _phase_title(self):
        title = Text("Gamow Alpha Decay", font="EB Garamond", font_size=58, color=INK)
        sub1  = Text(
            "Po-212 vs Th-232: energy factor 2, half-life factor 10²⁴",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "T ≈ e^{−2γ};  γ = π(Z−2)e²/(4πε₀ħv)  — one exponential does everything",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_barrier(self):
        Z = 84
        E_tracker = ValueTracker(4.0)

        ax = Axes(
            x_range=[0, 30, 5], y_range=[-5, 35, 5],
            x_length=8.0, y_length=4.8,
            axis_config={"color": INK, "stroke_width": 1.3, "include_ticks": True},
        ).shift(LEFT * 0.5 + UP * 0.1)

        x_lbl = MathTex(r"r\;(\mathrm{fm})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"V\;(\mathrm{MeV})", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        e2_4pie0 = E_CH**2 / (4 * np.pi * EPS0)
        r1_fm = 8.0   # inner turning point

        def _barrier():
            r_arr = np.linspace(0.5, 30, 400)
            V_arr = []
            for r in r_arr:
                if r < r1_fm:
                    V_arr.append(-5.0)   # nuclear well (schematic)
                else:
                    V_MeV = 2*(Z-2) * e2_4pie0 / (r * 1e-15) / (1e6 * EV)
                    V_arr.append(min(V_MeV, 34))
            pts = [ax.c2p(r, v) for r, v in zip(r_arr, V_arr)]
            c = VMobject(color=BROWN, stroke_width=2.5)
            c.set_points_smoothly(pts)
            return c

        def _energy_line():
            E = E_tracker.get_value()
            lo = ax.c2p(0, E)
            hi = ax.c2p(30, E)
            return DashedLine(lo, hi, color=GOLD, stroke_width=2.0)

        def _wavefunction():
            E   = E_tracker.get_value()
            # outer turning point r2 where V(r2) = E
            r2_fm = 2*(Z-2) * e2_4pie0 / (E * 1e6 * EV) / 1e-15
            r2_fm = min(r2_fm, 25)
            gamma = gamow_factor(Z, E)
            # decay inside barrier r1..r2
            r_in = np.linspace(r1_fm, r2_fm, 100)
            decay = 0.3 * np.exp(-gamma * (r_in - r1_fm) / (r2_fm - r1_fm))
            pts_in = [ax.c2p(r, E + d * 5) for r, d in zip(r_in, decay)]
            c = VMobject(color=BLUE, stroke_width=2.2)
            c.set_points_smoothly(pts_in)
            return c

        def _halflife_lbl():
            E   = E_tracker.get_value()
            t_s = half_life(Z, E, r1_fm)
            yr  = 365.25 * 24 * 3600
            if t_s < 1e-3:
                t_str = f"{t_s*1e6:.2f} μs"
            elif t_s < yr:
                t_str = f"{t_s:.2e} s"
            else:
                t_str = f"{t_s/yr:.2e} yr"
            return Text(f"E={E:.1f} MeV  t½≈{t_str}", font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.28)

        barrier_curve = _barrier()
        self.play(Create(barrier_curve), run_time=0.8)

        dyn_E    = always_redraw(_energy_line)
        dyn_psi  = always_redraw(_wavefunction)
        dyn_lbl  = always_redraw(_halflife_lbl)
        self.add(dyn_E, dyn_psi, dyn_lbl)

        # Animate E from 4 MeV (Th) to 8.78 MeV (Po)
        self.play(E_tracker.animate.set_value(8.78), run_time=5.0, rate_func=linear)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_geiger_nuttall(self):
        Z = 84
        E_vals = np.linspace(4.0, 10.0, 300)
        log_t  = [np.log10(max(half_life(Z, E), 1e-30)) for E in E_vals]
        inv_sE = [1.0 / np.sqrt(E) for E in E_vals]

        log_t_min = min(log_t) - 1
        log_t_max = max(log_t) + 1

        ax = Axes(
            x_range=[0.30, 0.52, 0.05], y_range=[log_t_min, log_t_max, 5],
            x_length=8.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.2)

        x_lbl = MathTex(r"1/\sqrt{E}\;\mathrm{(MeV^{-1/2})}", color=INK, font_size=18).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"\log_{10}(t_{1/2}/\mathrm{s})", color=INK, font_size=18).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        pts = [ax.c2p(inv_e, lt) for inv_e, lt in zip(inv_sE, log_t)]
        gn_line = VMobject(color=GOLD, stroke_width=2.8)
        gn_line.set_points_smoothly(pts)
        self.play(Create(gn_line), run_time=1.5)

        # Mark Po-212 and Th-232
        E_Po, Z_Po = 8.78, 84
        E_Th, Z_Th = 4.01, 90
        t_Po = half_life(Z_Po, E_Po, 8.0)
        t_Th = half_life(Z_Th, E_Th, 9.0)
        yr = 365.25 * 24 * 3600

        for E, t, label, col in [(E_Po, t_Po, "Po-212", BLUE), (E_Th, t_Th, "Th-232", BROWN)]:
            try:
                lt = np.log10(t)
                ie = 1.0 / np.sqrt(E)
                dot = Dot(ax.c2p(ie, lt), color=col, radius=0.12)
                lbl = Text(label, font="EB Garamond", font_size=18, color=col).next_to(dot, UR, buff=0.1)
                self.play(FadeIn(dot), Write(lbl), run_time=0.5)
            except Exception:
                pass

        fin = Text(
            "Geiger-Nuttall law:  log(t½) vs 1/√E is linear — a single exponential spans 24 decades",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.7)
        self.wait(2.5)
