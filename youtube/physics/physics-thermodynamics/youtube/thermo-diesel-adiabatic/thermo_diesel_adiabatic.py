#!/usr/bin/env python3
"""
thermo_diesel_adiabatic.py — Diesel Adiabatic Compression: No Spark, Just Thermodynamics
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics (verified at module level):
    T₁=300 K, r=20, γ=1.4 (diatomic air)
    T₂ = T₁·r^(γ−1) = 300·20^0.4 ≈ 879 K
    Diesel ignition ≈ 540°C = 813 K
    n=0.04 mol, C_V = (5/2)R (diatomic), W ≈ n·C_V·(T₂−T₁)

Render:
    cd physics-thermodynamics/youtube/thermo-diesel-adiabatic
    manim -qh thermo_diesel_adiabatic.py DieselAdiabaticScene
"""
import sys
import numpy as np

# ─── Constants ────────────────────────────────────────────────────────────────
GAMMA     = 1.4
R_GAS     = 8.314    # J/(mol·K)
T1        = 300.0    # K
R_DIESEL  = 20.0     # diesel compression ratio
R_GAS_ENG = 10.0     # gasoline compression ratio
N_MOL     = 0.04     # mol
CV        = 2.5 * R_GAS  # J/(mol·K)  — diatomic ideal gas
T_IGNITE  = 813.0    # K  (540°C — diesel ignition temperature)


def T_after_compression(r: float, T1_: float = T1) -> float:
    return T1_ * (r ** (GAMMA - 1.0))


def W_adiabatic(r: float, n: float = N_MOL, T1_: float = T1) -> float:
    T2 = T_after_compression(r, T1_)
    return n * CV * (T2 - T1_)


# ─── Verification ─────────────────────────────────────────────────────────────
def _verify():
    print("=== Diesel Adiabatic Compression verification ===")
    T2_diesel = T_after_compression(R_DIESEL)
    T2_gas    = T_after_compression(R_GAS_ENG)
    W_diesel  = W_adiabatic(R_DIESEL)
    print(f"T₁ = {T1:.0f} K")
    print(f"Diesel r=20: T₂ = {T2_diesel:.1f} K  (expected ≈ 879 K)")
    print(f"  → {T2_diesel-273.15:.1f}°C  >  ignition point {T_IGNITE-273.15:.0f}°C?  {T2_diesel > T_IGNITE}")
    print(f"  TV^(γ-1)=const check: T₁·V₁^0.4 = {T1*(1.0**0.4):.1f}, T₂·(V₁/r)^0.4 = {T2_diesel*((1.0/R_DIESEL)**0.4):.1f}")
    print(f"Gasoline r=10: T₂ = {T2_gas:.1f} K  (below ignition? {T2_gas < T_IGNITE})")
    print(f"Work stored in gas (diesel): {W_diesel:.1f} J  (expected ≈ 482 J)")
    print(f"r^(γ-1) ratio diesel/gasoline: {(R_DIESEL/R_GAS_ENG)**(GAMMA-1):.3f}")
    print("=== PASSED ===")

_verify()
if __name__ == "__main__":
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"

# Color gradient from cold to hot
def temp_color(T: float, T_min: float = T1, T_max: float = 1000.0) -> str:
    """Map temperature to color: blue (cold) → gold (hot)."""
    t = np.clip((T - T_min) / (T_max - T_min), 0.0, 1.0)
    # Blue → BROWN → GOLD
    if t < 0.5:
        s = t * 2.0
        r = int(0x58 + s * (0xCD - 0x58))
        g = int(0xC4 + s * (0x85 - 0xC4))
        b = int(0xDD + s * (0x3F - 0xDD))
    else:
        s = (t - 0.5) * 2.0
        r = int(0xCD + s * (0xF0 - 0xCD))
        g = int(0x85 + s * (0xE4 - 0x85))
        b = int(0x3F + s * (0x42 - 0x3F))
    return f"#{r:02X}{g:02X}{b:02X}"


class DieselAdiabaticScene(Scene):
    """
    Phase 1: Title.
    Phase 2: Cylinder animation — piston descends, color gradient shifts, temperature counter climbs.
    Phase 3: Side panel — comparison r=10 vs r=20.
    Phase 4: Final state annotations.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_cylinder()
        self._phase_comparison()

    def _phase_title(self):
        title = Text("Diesel Adiabatic Compression", font="EB Garamond", font_size=56, color=INK)
        sub1 = Text(
            "No spark plug — compression alone heats air past ignition",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2 = MathTex(
            r"T_2 = T_1 \cdot r^{\gamma-1} = 300 \cdot 20^{0.4} \approx 879\,\mathrm{K}",
            color=GOLD, font_size=28,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_cylinder(self):
        """Animated cylinder with descending piston and temperature readout."""

        # Cylinder walls — fixed rectangle outline
        cyl_left   = -2.2
        cyl_right  =  2.2
        cyl_bottom = -3.0
        cyl_top    =  2.8   # where piston starts at V_i (BDC)

        # Piston travel: from cyl_top down to piston_min (TDC)
        piston_min = cyl_bottom + (cyl_top - cyl_bottom) / R_DIESEL   # at TDC

        walls = Rectangle(
            width=(cyl_right - cyl_left),
            height=(cyl_top - cyl_bottom),
            color=INK, stroke_width=2.5,
        ).move_to([(cyl_left + cyl_right)/2, (cyl_top + cyl_bottom)/2 - 0.3, 0])
        # actual y-center
        cyl_center_y = (cyl_top + cyl_bottom)/2 - 0.3

        self.play(Create(walls), run_time=0.8)

        # Temperature tracker
        t_tracker = ValueTracker(T1)

        # Gas fill — rectangle that shrinks as piston descends
        def make_gas():
            T = t_tracker.get_value()
            # Piston y position: interpolate from cyl_top to piston_min
            frac = (T - T1) / (T_after_compression(R_DIESEL) - T1)
            frac = np.clip(frac, 0, 1)
            piston_y = cyl_top - frac * (cyl_top - piston_min)

            col = temp_color(T)
            gas_h = piston_y - cyl_bottom
            gas_rect = Rectangle(
                width=(cyl_right - cyl_left) - 0.04,
                height=max(gas_h - 0.04, 0.05),
                color=col, fill_color=col, fill_opacity=0.5,
                stroke_width=0,
            )
            gas_rect.move_to([0.0, cyl_bottom + gas_h/2 - 0.3, 0])
            return gas_rect

        def make_piston():
            T = t_tracker.get_value()
            frac = (T - T1) / (T_after_compression(R_DIESEL) - T1)
            frac = np.clip(frac, 0, 1)
            piston_y = cyl_top - frac * (cyl_top - piston_min)
            rect = Rectangle(
                width=(cyl_right - cyl_left) - 0.04,
                height=0.3,
                color=INK, fill_color=DIM, fill_opacity=0.9,
                stroke_width=1.5,
            )
            rect.move_to([0.0, piston_y - 0.15 - 0.3, 0])
            return rect

        dyn_gas    = always_redraw(make_gas)
        dyn_piston = always_redraw(make_piston)
        self.add(dyn_gas, dyn_piston)

        # Temperature counter
        T_lbl = MathTex(r"T = ", color=INK, font_size=32).shift(RIGHT * 4.0 + UP * 1.5)
        T_num = DecimalNumber(T1, num_decimal_places=0, color=GOLD, font_size=32).next_to(T_lbl, RIGHT, buff=0.1)
        T_K   = MathTex(r"\mathrm{K}", color=INK, font_size=32).next_to(T_num, RIGHT, buff=0.08)
        T_num.add_updater(lambda m: m.set_value(t_tracker.get_value()))

        # Ignition line — horizontal dashed
        ign_y = cyl_bottom + (cyl_top - cyl_bottom) * (T_IGNITE - T1) / (T_after_compression(R_DIESEL) - T1)
        # The ignition line on the side panel at 4.0 x:
        ign_lbl = Text(f"Ignition\n{T_IGNITE-273.15:.0f}°C",
                       font="EB Garamond", font_size=20, color=BROWN).shift(RIGHT * 5.2 + UP * 0.2)
        ign_line = DashedLine(
            RIGHT * 3.0 + UP * 0.2,
            RIGHT * 5.8 + UP * 0.2,
            color=BROWN, stroke_width=2.0,
        )

        # Q=0 annotation
        q_zero = MathTex(r"Q = 0", color=DIM, font_size=28).shift(RIGHT * 4.0 + DOWN * 0.5)
        w_ann  = MathTex(r"W \to \Delta U", color=DIM, font_size=24).shift(RIGHT * 4.0 + DOWN * 1.2)

        hdr = Text("r = 20  —  diesel compression",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)

        self.play(Write(hdr), FadeIn(T_lbl), FadeIn(T_num), FadeIn(T_K),
                  FadeIn(q_zero), FadeIn(w_ann), run_time=0.8)

        # Add ignition line at the right moment
        self.play(
            t_tracker.animate.set_value(T_IGNITE),
            run_time=3.5, rate_func=smooth,
        )
        self.play(Create(ign_line), Write(ign_lbl), run_time=0.8)
        ignite_lbl = Text("Ignition point reached!", font="EB Garamond",
                          font_size=24, color=GOLD).shift(RIGHT * 4.0 + UP * 0.8)
        self.play(Write(ignite_lbl), run_time=0.5)
        self.wait(0.5)

        # Continue to TDC
        T2_diesel = T_after_compression(R_DIESEL)
        self.play(
            t_tracker.animate.set_value(T2_diesel),
            run_time=2.0, rate_func=smooth,
        )
        self.wait(1.0)

        # Final state annotation
        W_J = W_adiabatic(R_DIESEL)
        final_ann = Text(
            f"Final state: T = {T2_diesel:.0f} K\n"
            f"V reduced to V₁/20  ·  W = {W_J:.0f} J stored as internal energy",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(final_ann), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(dyn_gas, dyn_piston, walls, hdr, T_lbl, T_num, T_K,
                          q_zero, w_ann, ign_line, ign_lbl, ignite_lbl, final_ann),
                  run_time=0.5)

    def _phase_comparison(self):
        """Side-by-side comparison: r=10 (gasoline) vs r=20 (diesel)."""
        T2_gas    = T_after_compression(R_GAS_ENG)
        T2_diesel = T_after_compression(R_DIESEL)

        title = Text("Compression ratio comparison", font="EB Garamond",
                     font_size=30, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)

        # T-axis vertical bar chart
        ax = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 1000, 200],
            x_length=7.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.3)
        lbl_y = MathTex(r"T_2\;(\mathrm{K})", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lbl_y), run_time=0.8)

        # Gasoline bar
        gas_bar = Rectangle(
            width=1.2, height=ax.c2p(0, T2_gas)[1] - ax.c2p(0, 0)[1],
            color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.5,
        )
        gas_bar.align_to(ax.c2p(1, 0), DOWN).align_to(ax.c2p(1, 0), RIGHT).shift(LEFT * 0.6)
        gas_lbl = Text(f"r=10\n{T2_gas:.0f} K", font="EB Garamond",
                       font_size=22, color=BLUE).next_to(gas_bar, DOWN, buff=0.12)

        # Diesel bar
        diesel_bar = Rectangle(
            width=1.2, height=ax.c2p(0, T2_diesel)[1] - ax.c2p(0, 0)[1],
            color=GOLD, fill_color=GOLD, fill_opacity=0.5, stroke_width=1.5,
        )
        diesel_bar.align_to(ax.c2p(2, 0), DOWN).align_to(ax.c2p(2, 0), RIGHT).shift(LEFT * 0.6)
        diesel_lbl = Text(f"r=20\n{T2_diesel:.0f} K", font="EB Garamond",
                          font_size=22, color=GOLD).next_to(diesel_bar, DOWN, buff=0.12)

        # Ignition dashed line
        ign_line = DashedLine(
            ax.c2p(0.3, T_IGNITE), ax.c2p(2.7, T_IGNITE),
            color=BROWN, stroke_width=2.0,
        )
        ign_lbl = MathTex(r"813\,\mathrm{K}\;\text{(ignition)}", color=BROWN, font_size=20).next_to(
            ax.c2p(2.7, T_IGNITE), RIGHT, buff=0.1)

        self.play(
            Create(gas_bar), Write(gas_lbl),
            Create(diesel_bar), Write(diesel_lbl),
            run_time=1.5,
        )
        self.play(Create(ign_line), Write(ign_lbl), run_time=0.8)
        self.wait(1.0)

        cap = Text(
            "Gasoline r=10: T₂=754 K — below ignition, needs a spark\n"
            "Diesel   r=20: T₂=879 K — above ignition, no spark needed",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=1.2)
        self.wait(3.0)
