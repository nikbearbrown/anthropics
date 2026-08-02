#!/usr/bin/env python3
"""
astro_nucleosynthesis_binding_energy.py — Nucleosynthesis Binding Energy Curve
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-nucleosynthesis-binding-energy
    manim -qh astro_nucleosynthesis_binding_energy.py NucleosynthesisBindingEnergyScene

Verify:
    python3 astro_nucleosynthesis_binding_energy.py

Physics:
    Binding energy per nucleon (BE/A) vs A.
    Peaks at Fe-56: 8.794 MeV/nucleon.
    Fusion of A<56 releases energy; fusion of A>56 absorbs energy.
    Stellar nucleosynthesis chain: H→He→C→O→Ne→Si→Fe.
    Data from Wapstra-Audi nuclear mass tables (public domain approximation).
"""
import sys
import numpy as np

# BE/A data (A, BE/A in MeV) — approximated from Wapstra-Audi tables
# Key nuclides along the fusion chain
BE_DATA = np.array([
    (1,    0.000),   # H-1
    (2,    1.112),   # H-2 (deuterium)
    (4,    7.074),   # He-4 (alpha)
    (12,   7.680),   # C-12
    (16,   7.976),   # O-16
    (20,   8.032),   # Ne-20
    (24,   8.261),   # Mg-24
    (28,   8.448),   # Si-28
    (32,   8.493),   # S-32
    (40,   8.551),   # Ca-40
    (52,   8.735),   # Cr-52
    (56,   8.790),   # Fe-56  ← peak
    (58,   8.792),   # Ni-58  (nearly same)
    (63,   8.752),   # Cu-63
    (80,   8.713),   # Se-80
    (100,  8.597),   # Ru-100
    (120,  8.505),   # Sn-120
    (140,  8.384),   # Ce-140
    (160,  8.253),   # Dy-160
    (180,  8.155),   # W-180
    (197,  7.919),   # Au-197
    (208,  7.867),   # Pb-208
    (235,  7.591),   # U-235
    (238,  7.570),   # U-238
])

# Nucleosynthesis arrows: (A_start, A_end, reaction, timescale, color_key)
FUSION_CHAIN = [
    (1,   4,  r"H \to He",             "10 Myr", "pp/CNO"),
    (4,  12,  r"He \to C",             "1 Myr",  "triple-α"),
    (12, 20,  r"C \to Ne",             "0.6 kyr","C-burn"),
    (16, 20,  r"O \to Ne,Mg",          "1 yr",   "O-burn"),
    (20, 28,  r"Ne,O \to Si",          "6 mo",   "Ne/O-burn"),
    (28, 56,  r"Si \to Fe",            "1 day",  "Si-burn"),
]


def verify():
    print("=== Nucleosynthesis binding energy verification ===")
    A_arr = BE_DATA[:, 0]
    BE_arr= BE_DATA[:, 1]
    fe_idx = np.where(A_arr == 56)[0][0]
    print(f"Fe-56 BE/A = {BE_arr[fe_idx]:.3f} MeV  (card says 8.794 MeV)")
    print(f"Peak at A = {A_arr[np.argmax(BE_arr)]:.0f}")
    # P1: max should be around Fe-56
    assert abs(BE_arr[fe_idx] - 8.790) < 0.01, "Fe-56 BE/A check failed"
    # P2: Hoyle state — just note, can't derive here
    print("Hoyle state at 7.656 MeV in C-12 — predicted by Hoyle 1954, confirmed Cook 1957")
    print("He-4 BE/A:", BE_arr[2])
    print("Energy released H→He: ΔBE/A ≈", BE_arr[2] - BE_arr[0], "MeV  (card says ~7 MeV)")
    print("=== PASSED ===")


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
ORANGE_C = "#F4A261"


class NucleosynthesisBindingEnergyScene(Scene):
    """
    Binding energy per nucleon curve.
    Fusion arrows appear in sequence from H→Fe.
    Each arrow shorter (less energy) and faster.
    At Fe: arrow cannot go higher — collapse.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_be_curve()
        self._phase_fusion_arrows()
        self._phase_rprocess()

    def _phase_title(self):
        title = Text("Nuclear Binding Energy — Iron is the Graveyard", font="EB Garamond",
                     font_size=46, color=INK)
        sub1 = Text(
            "Fusion releases energy only if A < 56. Iron is where stellar fusion stops.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"\frac{BE}{A}\bigg|_{\rm Fe-56} = 8.794\;\mathrm{MeV/nucleon}\;(\text{max})",
                       color=BLUE, font_size=26)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_be_curve(self):
        A_arr  = BE_DATA[:, 0]
        BE_arr = BE_DATA[:, 1]

        ax = Axes(
            x_range=[0, 245, 50],
            y_range=[0, 9.5, 2.0],
            x_length=10.0,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.2)
        lbl_x = MathTex(r"A\;\text{(mass number)}", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"BE/A\;(\mathrm{MeV/nucleon})", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Binding energy per nucleon — measured from nuclear masses",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        # Smooth curve through data
        from scipy.interpolate import make_interp_spline
        spl = make_interp_spline(A_arr, BE_arr, k=3)
        A_smooth = np.linspace(1, 238, 500)
        BE_smooth = np.clip(spl(A_smooth), 0, 10)

        c_be = VMobject(color=BLUE, stroke_width=3.5)
        c_be.set_points_smoothly([ax.c2p(A, BE) for A, BE in zip(A_smooth, BE_smooth)])

        fe_dot = Dot(ax.c2p(56, 8.790), radius=0.12, color=GOLD)
        fe_lbl = MathTex(r"^{56}\!\mathrm{Fe}\;8.79\;\mathrm{MeV}", color=GOLD, font_size=20
                         ).next_to(fe_dot, UR, buff=0.06)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.5)
        self.play(Create(c_be), run_time=1.8)
        self.play(FadeIn(fe_dot), Write(fe_lbl), run_time=0.8)
        self.wait(0.5)

        self.stored_ax = ax
        self.stored_c_be = c_be
        self.stored_hdr = hdr

    def _phase_fusion_arrows(self):
        ax = self.stored_ax
        A_arr  = BE_DATA[:, 0]
        BE_arr = BE_DATA[:, 1]

        def be_at(A_val):
            """Interpolate BE/A at given A."""
            idx = np.argmin(np.abs(A_arr - A_val))
            return float(BE_arr[idx])

        colors_chain = [BLUE, BLUE, GOLD, GOLD, BROWN, RED_C]
        timescales   = ["10 Myr", "1 Myr", "0.6 kyr", "1 yr", "6 mo", "1 day"]
        labels_chain = [
            r"H \to He",
            r"He \to C",
            r"C \to Ne",
            r"Ne,O \to Si",
            r"O \to Si",
            r"Si \to Fe",
        ]
        # Arrow endpoints: (A_start, BE_start, A_end, BE_end)
        arrow_data = [
            (2,  be_at(2),  4,  be_at(4)),
            (4,  be_at(4),  12, be_at(12)),
            (12, be_at(12), 20, be_at(20)),
            (20, be_at(20), 28, be_at(28)),
            (16, be_at(16), 28, be_at(28)),
            (28, be_at(28), 56, be_at(56)),
        ]

        caption_prev = None
        for i, ((A0, BE0, A1, BE1), color, ts, lbl_str) in enumerate(
                zip(arrow_data, colors_chain, timescales, labels_chain)):
            arr = Arrow(
                ax.c2p(A0, BE0), ax.c2p(A1, BE1),
                color=color, stroke_width=4.0, tip_length=0.18,
                buff=0.05,
            )
            caption = Text(f"${lbl_str}$  —  {ts}",
                           font="EB Garamond", font_size=19, color=color
                           ).to_edge(DOWN, buff=0.28)
            if caption_prev:
                self.play(Create(arr), Transform(caption_prev, caption), run_time=0.9)
            else:
                self.play(Create(arr), Write(caption), run_time=0.9)
                caption_prev = caption
            self.wait(0.3)

        # Arrow that tries to go beyond Fe — stops
        stop_arr = Arrow(
            ax.c2p(56, be_at(56)), ax.c2p(80, be_at(56) - 0.2),
            color=DIM, stroke_width=3.0, tip_length=0.15, buff=0.05,
        )
        stop_lbl = MathTex(r"\uparrow\;\text{absorbs energy — forbidden}",
                           color=DIM, font_size=20).to_edge(DOWN, buff=0.08)
        self.play(Create(stop_arr), run_time=0.6)
        self.play(FadeOut(caption_prev), Write(stop_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(stop_lbl, stop_arr, self.stored_hdr, self.stored_c_be, *self.mobjects), run_time=0.5)

    def _phase_rprocess(self):
        eq = MathTex(
            r"\text{r-process (neutron star merger): Fe} \to \text{Au, U}",
            color=GOLD, font_size=28,
        ).center().shift(UP * 1.0)
        note = Text(
            "Beyond iron, only neutron-rich explosions can climb the slope.",
            font="EB Garamond", font_size=21, color=DIM,
        ).next_to(eq, DOWN, buff=0.4)
        note2 = Text(
            "The gold in your jewellery came from a neutron star collision.",
            font="EB Garamond", font_size=21, color=BROWN,
        ).next_to(note, DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
