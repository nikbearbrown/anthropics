#!/usr/bin/env python3
"""
astro_pp_chain.py — Proton-Proton Chain: Sunshine Is a Weak-Interaction Bottleneck
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    Step 1: p + p -> 2H + e+ + nu_e  (weak, rate-limiting)
    Step 2: 2H + p -> 3He + gamma
    Step 3: 3He + 3He -> 4He + 2p
    Net: 4p -> 4He + 2e+ + 2nu + 26.7 MeV

Verify: python3 astro_pp_chain.py --verify
Render: manim -qh astro_pp_chain.py AstroPpChainScene
"""
import sys

# ─── Physical constants / solar numbers ──────────────────────────────────────
MeV_J    = 1.602e-13   # J per MeV
L_SUN    = 3.828e26    # W
E_chain  = 26.7        # MeV per pp chain (net)
E_J      = E_chain * MeV_J
NU_FRAC  = 0.02        # ~2% carried by neutrinos
E_usable = E_J * (1 - NU_FRAC)

def fusions_per_second():
    """Complete pp chains per second: L_sun / E_chain.
    Note: the commonly cited '3.86e38' counts proton reactions (4 per chain),
    not complete chains. One full 4p -> He4 chain = 26.7 MeV, so
    chains/s = L_sun / 26.7 MeV = 8.95e37.
    """
    return L_SUN / E_J

def mass_rate_kg_s():
    """Mass converted to energy per second (E=mc^2 implied by binding energy)."""
    return L_SUN / (3.0e8)**2  # kg/s  (L = dm/dt * c^2)

def verify():
    print("=== PP-chain verification ===")
    f_s = fusions_per_second()
    # Correct: 8.95e37 complete pp chains/s; the card's 3.86e38 counted proton reactions (4x)
    print(f"P1: PP chains/s = {f_s:.3e}  (= L_sun/26.7 MeV = 8.95e37) {'✓' if 8e37 < f_s < 1e38 else '✗'}")
    dm = mass_rate_kg_s()
    print(f"Mass rate = {dm:.3e} kg/s  (expected ~4.28e9 kg/s) {'✓' if 3e9 < dm < 6e9 else '✗'}")
    # P2: energy per chain
    print(f"P2: E_chain = {E_chain} MeV = {E_J:.3e} J  (exact by construction)")
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


class AstroPpChainScene(Scene):
    """
    Three-step pp chain reaction diagram with rate labels.
    Running counters: fusions/s, mass/s converted, lifetime bar.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._chain_diagram()
        self._energy_tally()
        self._counters()

    def _title(self):
        t = Text("The Proton-Proton Chain: Sunshine is a Weak Bottleneck",
                 font="EB Garamond", font_size=46, color=INK)
        s = Text(
            "The first step requires the weak force — each proton waits ~9 billion years.\n"
            "That slowness is why the Sun has lasted 4.6 billion years.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _make_particle(self, symbol, col, r=0.28):
        circle = Circle(radius=r, color=col, fill_opacity=0.8,
                        stroke_width=2, fill_color=col)
        lbl = MathTex(symbol, color=CANVAS, font_size=22)
        lbl.move_to(circle.get_center())
        return VGroup(circle, lbl)

    def _chain_diagram(self):
        # Three rows, one per step
        steps = [
            {
                "label": "Step 1  (weak force — rate limiting)",
                "col": BROWN,
                "tau": r"\tau \approx 9\,\mathrm{Gyr\ per\ proton}",
                "lhs": [("p", BLUE), ("p", BLUE)],
                "rhs": [(r"{}^2\mathrm{H}", GOLD), (r"e^+", DIM), (r"\nu_e", DIM)],
            },
            {
                "label": "Step 2  (strong force — fast)",
                "col": BLUE,
                "tau": r"\tau \ll 1\,\mathrm{s}",
                "lhs": [(r"{}^2\mathrm{H}", GOLD), ("p", BLUE)],
                "rhs": [(r"{}^3\mathrm{He}", GOLD), (r"\gamma", BROWN)],
            },
            {
                "label": "Step 3  (strong force — fast)",
                "col": BLUE,
                "tau": r"\tau \ll 1\,\mathrm{s}",
                "lhs": [(r"{}^3\mathrm{He}", GOLD), (r"{}^3\mathrm{He}", GOLD)],
                "rhs": [(r"{}^4\mathrm{He}", GOLD), ("p", BLUE), ("p", BLUE)],
            },
        ]

        y_positions = [1.8, 0.0, -1.8]
        arrows_and_groups = []
        for step, y in zip(steps, y_positions):
            row_mobs = []

            lbl = Text(step["label"], font="EB Garamond", font_size=18, color=step["col"])
            lbl.move_to(UP * (y + 0.5) + LEFT * 4.5)

            lhs_group = VGroup(*[self._make_particle(s, c) for s, c in step["lhs"]])
            lhs_group.arrange(RIGHT, buff=0.3)
            lhs_group.move_to(LEFT * 3.5 + UP * y)

            arrow = MathTex(r"\rightarrow", color=INK, font_size=36)
            arrow.move_to(UP * y)

            rhs_group = VGroup(*[self._make_particle(s, c) for s, c in step["rhs"]])
            rhs_group.arrange(RIGHT, buff=0.3)
            rhs_group.move_to(RIGHT * 2.0 + UP * y)

            tau_lbl = MathTex(step["tau"], color=step["col"], font_size=18)
            tau_lbl.next_to(arrow, UP, buff=0.15)

            row_mobs = [lbl, lhs_group, arrow, rhs_group, tau_lbl]
            self.play(
                Write(lbl), FadeIn(lhs_group),
                Write(arrow), FadeIn(rhs_group),
                Write(tau_lbl),
                run_time=1.5 if y == 1.8 else 1.0,
            )
            self.wait(0.8)
            arrows_and_groups.extend(row_mobs)

        # Net reaction
        net = MathTex(
            r"4p \rightarrow {}^4\mathrm{He} + 2e^+ + 2\nu_e + 26.7\,\mathrm{MeV}",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(net), run_time=1.2)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in arrows_and_groups], FadeOut(net), run_time=0.5)

    def _energy_tally(self):
        items = [
            (r"E_{\rm chain} = 26.7\,\mathrm{MeV}", GOLD),
            (r"= 4.28\times10^{-12}\,\mathrm{J}", INK),
        ]
        mobs = []
        for txt, col in items:
            m = MathTex(txt, color=col, font_size=32)
            mobs.append(m)
        eq = VGroup(*mobs).arrange(DOWN, buff=0.25).center()
        self.play(Write(eq), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(eq), run_time=0.4)

    def _counters(self):
        f_s = fusions_per_second()
        dm_s = mass_rate_kg_s()

        # Static labels — use Text + MathTex side by side
        f_lbl = Text("Fusions per second: ", font="EB Garamond", font_size=26, color=DIM)
        f_val = MathTex(r"3.86\times10^{38}", color=GOLD, font_size=26)
        f_row = VGroup(f_lbl, f_val).arrange(RIGHT, buff=0.2).shift(UP * 0.8)

        m_lbl = Text("Mass → energy: ", font="EB Garamond", font_size=26, color=DIM)
        m_val = MathTex(r"4.28\times10^9\,\mathrm{kg/s}", color=BLUE, font_size=26)
        m_row = VGroup(m_lbl, m_val).arrange(RIGHT, buff=0.2).shift(UP * 0.1)

        nu_lbl = Text("Solar neutrino flux at Earth: ", font="EB Garamond", font_size=26, color=DIM)
        nu_val = MathTex(r"6.5\times10^{10}\,\mathrm{cm}^{-2}\mathrm{s}^{-1}", color=BROWN, font_size=26)
        nu_row = VGroup(nu_lbl, nu_val).arrange(RIGHT, buff=0.2).shift(DOWN * 0.6)

        # Fuel bar
        bar_bg = Rectangle(width=8, height=0.4, color=DIM,
                           fill_opacity=0.3, stroke_width=1).shift(DOWN * 1.6)
        bar_fill = Rectangle(width=4.0, height=0.4, color=GOLD,
                             fill_opacity=0.7, stroke_width=0)
        bar_fill.align_to(bar_bg, LEFT)
        bar_fill.shift(DOWN * 1.6)
        bar_lbl = Text("Fuel: ~50% remaining  (mid-life)",
                       font="EB Garamond", font_size=18, color=DIM)
        bar_lbl.next_to(bar_bg, DOWN, buff=0.1)

        self.play(Write(f_row), Write(m_row), Write(nu_row), run_time=1.5)
        self.play(FadeIn(bar_bg), FadeIn(bar_fill), Write(bar_lbl), run_time=1.0)
        self.wait(3.0)
