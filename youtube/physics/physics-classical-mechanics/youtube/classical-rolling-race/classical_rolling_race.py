#!/usr/bin/env python3
"""
classical_rolling_race.py — Rolling Race: Moment of Inertia Decides
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    v_cm = sqrt(2gh/(1+β))   β = I/(MR²)
    h = 1.0 m, g = 9.8 m/s²
    β: block=0, solid sphere=2/5, disk=1/2, hoop=1

Render:
    cd physics-classical-mechanics/youtube/classical-rolling-race
    manim -qh classical_rolling_race.py RollingRaceScene
"""
import sys
import numpy as np

G = 9.8
H = 1.0

OBJECTS = [
    ("Block (slide)",  0,    "#ECE6D8"),
    ("Solid sphere",   2/5,  "#58C4DD"),
    ("Disk",           1/2,  "#CD853F"),
    ("Hoop",           1,    "#F0E442"),
]


def v_bottom(h, beta, g=G):
    return np.sqrt(2*g*h / (1+beta))


def verify():
    print("=== Rolling Race verification ===")
    for name, beta, _ in OBJECTS:
        v = v_bottom(H, beta)
        KE_rot_frac = beta/(1+beta) if beta > 0 else 0
        print(f"  {name} (β={beta:.3f}): v={v:.4f} m/s  KE_rot/KE_total={KE_rot_frac:.4f}")
    # P1: sphere v = sqrt(10gh/7)
    v_sphere = v_bottom(H, 2/5)
    assert abs(v_sphere - np.sqrt(10*G*H/7)) < 1e-8, "P1 sphere speed"
    # P1: hoop v = sqrt(gh)
    v_hoop = v_bottom(H, 1)
    assert abs(v_hoop - np.sqrt(G*H)) < 1e-8, "P1 hoop speed"
    print(f"  sphere/hoop ratio = {v_sphere/v_hoop:.4f}  (expected 1.1952)")
    # P2: disk KE_rot fraction = 1/(1+1/β) = β/(1+β)
    beta_disk = 1/2
    frac = beta_disk/(1+beta_disk)
    print(f"  Disk rotational KE fraction = {frac:.6f}  (expected 0.333333 = 1/3)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class RollingRaceScene(Scene):
    """Objects roll down a ramp; KE bar chart shows translational vs rotational split."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._ramp_race()
        self._ke_chart()

    def _title(self):
        t1 = Text("Rolling Race", font="EB Garamond", font_size=64, color=INK)
        t2 = Text("Shape wins — mass and size cancel out completely",
                  font="EB Garamond", font_size=26, color=DIM)
        t3 = MathTex(r"v_{\rm cm} = \sqrt{\frac{2gh}{1+\beta}}\qquad \beta = \frac{I}{MR^2}",
                     color=BLUE, font_size=30)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _ramp_race(self):
        # Draw ramp
        ramp_start = np.array([-5.0, 1.8, 0])
        ramp_end   = np.array([5.0, -1.5, 0])
        ramp = Line(ramp_start, ramp_end, color=DIM, stroke_width=3)
        self.play(Create(ramp), run_time=0.6)

        colors = [obj[2] for obj in OBJECTS]
        betas  = [obj[1] for obj in OBJECTS]
        labels = [obj[0] for obj in OBJECTS]

        # Place objects at top of ramp, vertically stacked
        y_starts = [2.4, 1.9, 1.4, 0.9]
        x_start  = -4.5
        dots = []
        dot_lbls = []
        for i, (col, beta, label, y_s) in enumerate(zip(colors, betas, labels, y_starts)):
            d = Circle(radius=0.2, color=col, fill_color=col, fill_opacity=0.7)
            d.move_to(np.array([x_start, y_s, 0]))
            lbl = Text(f"β={beta:.2f}", font="EB Garamond", font_size=15, color=col)
            lbl.next_to(d, UP, buff=0.06)
            dots.append(d)
            dot_lbls.append(lbl)

        self.play(*[FadeIn(d, l) for d, l in zip(dots, dot_lbls)], run_time=0.8)

        # Final x positions (proportional to speed rank)
        speeds  = [v_bottom(H, b) for b in betas]
        max_v   = max(speeds)
        x_final = [x_start + 8.5*(v/max_v) for v in speeds]
        y_final = [-1.0 - 0.35*i for i in range(4)]

        anims = []
        for i, (d, lbl) in enumerate(zip(dots, dot_lbls)):
            target = np.array([x_final[i], y_final[i], 0])
            anims.append(d.animate.move_to(target))
            anims.append(lbl.animate.move_to(target + UP*0.35))

        self.play(*anims, run_time=2.5, rate_func=smooth)

        # Velocity labels
        for i, (col, beta, label, xf, yf) in enumerate(zip(colors, betas, labels, x_final, y_final)):
            v = v_bottom(H, beta)
            v_lbl = Text(f"{v:.2f} m/s", font="EB Garamond", font_size=16, color=col)
            v_lbl.next_to(np.array([xf, yf, 0]), RIGHT, buff=0.12)
            self.play(Write(v_lbl), run_time=0.35)

        final = Text("Hoop always finishes last — it pays the highest rotational tax",
                     font="EB Garamond", font_size=21, color=GOLD).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _ke_chart(self):
        """KE split: translational vs rotational bar chart."""
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.1, 0.25],
            x_length=9,
            y_length=5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).center().shift(DOWN*0.3)
        lx = Text("Object", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("KE fraction", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Fraction of KE stored as rotation",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        for i, (name, beta, col) in enumerate(OBJECTS):
            frac = beta/(1+beta) if beta > 0 else 0
            bar = ax.get_area(
                ax.plot(lambda x: frac, x_range=[i+0.5, i+1.4]),
                x_range=[i+0.5, i+1.4], color=col, opacity=0.7
            )
            lbl_name = Text(name.split()[0], font="EB Garamond", font_size=16, color=col)
            lbl_name.move_to(ax.c2p(i+0.95, -0.08))
            lbl_frac = Text(f"{frac:.2f}", font="EB Garamond", font_size=15, color=col)
            lbl_frac.move_to(ax.c2p(i+0.95, frac+0.05))
            self.play(FadeIn(bar), Write(lbl_name), Write(lbl_frac), run_time=0.7)

        final = Text(
            "Disk: exactly 1/3 in rotation  ·  Hoop: exactly 1/2  ·  independent of mass",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
