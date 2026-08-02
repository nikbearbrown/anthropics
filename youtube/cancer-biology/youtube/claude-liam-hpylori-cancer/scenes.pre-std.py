from manim import *
import numpy as np
import random

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"

# Shared seeded random — ensures deterministic dot positions
_RND = random.Random(7)

# 6 patch x-centres across the frame
_XS = np.linspace(-5.2, 5.2, 6)


def _make_patch(i, x):
    """RoundedRectangle tissue patch for stage i at x-position."""
    col = ORANGE if i == 5 else SKY
    return RoundedRectangle(
        width=1.65, height=2.2,
        corner_radius=0.18,
        color=col,
        fill_color=col,
        fill_opacity=0.14,
        stroke_width=2.8,
    ).move_to(np.array([x, -0.8, 0.0]))


def _make_dots(i, x, rnd=None):
    """VGroup of seeded dots for stage i at x-position."""
    if rnd is None:
        rnd = random.Random(7 + i * 13)
    n = 4 + i * 3
    spread = i * 0.11
    col = ORANGE if i == 5 else BLUE
    return VGroup(*[
        Dot(
            point=np.array([
                x - 0.52 + (k % 4) * 0.34 + rnd.uniform(-spread, spread),
                -1.30 + (k // 4) * 0.34 + rnd.uniform(-spread, spread),
                0.0,
            ]),
            radius=0.07,
            color=col,
        )
        for k in range(n)
    ])


def _make_bacterium():
    """VERM curved rod (5-point polyline) above the first three patches."""
    bact_pts = [
        np.array([-5.0, 2.20, 0.0]),
        np.array([-2.8, 1.80, 0.0]),
        np.array([-0.4, 2.00, 0.0]),
        np.array([ 2.0, 1.80, 0.0]),
        np.array([ 3.5, 2.10, 0.0]),
    ]
    bact = VMobject(color=VERM, stroke_width=9)
    bact.set_points_smoothly(bact_pts)
    return bact


def _make_down_arrows():
    """3 downward arrows from bacterium to first 3 patch tops."""
    arrows = []
    for j in range(3):
        x = _XS[j]
        arrows.append(
            Arrow(
                np.array([x, 1.55, 0.0]),
                np.array([x, 0.25, 0.0]),
                color=VERM,
                stroke_width=2.4,
                max_tip_length_to_length_ratio=0.18,
            )
        )
    return arrows


# ============================================================
# B05_HpyloriCancer — initial animation
#   6 patches appear L→R, bacterium draws in, 3 arrows descend
# ============================================================
class B05_HpyloriCancer(Scene):
    def construct(self):
        rnd = random.Random(7)
        patches = []
        all_dots = []

        for i, x in enumerate(_XS):
            patches.append(_make_patch(i, x))
            all_dots.append(_make_dots(i, x, rnd=rnd))

        bact = _make_bacterium()
        down_arrows = _make_down_arrows()

        # 1. Patches + dots appear left to right
        self.play(
            LaggedStart(
                *[AnimationGroup(FadeIn(patches[i]), FadeIn(all_dots[i]))
                  for i in range(6)],
                lag_ratio=0.18,
                run_time=2.0,
            )
        )

        # 2. Bacterium rod draws in
        self.play(Create(bact), run_time=0.7)

        # 3. 3 arrows descend onto first 3 patches
        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in down_arrows],
                lag_ratio=0.20,
                run_time=0.9,
            )
        )

        # 4. Final cancer patch brightens with Flash
        self.play(
            Flash(
                np.array([_XS[5], -0.8, 0.0]),
                color=ORANGE,
                line_length=0.4,
                num_lines=12,
                flash_radius=1.2,
            ),
            run_time=0.5,
        )
        self.wait(0.8)


# ============================================================
# B07_HpyloriProgression — revised animation with progression dynamics
#   Arrow glow on each hit → patch Flash → dot rearrangement
#   Final cancer patch transforms SKY → ORANGE with Flash
# ============================================================
class B07_HpyloriProgression(Scene):
    def construct(self):
        rnd = random.Random(7)
        patches = []
        all_dots = []

        for i, x in enumerate(_XS):
            patches.append(_make_patch(i, x))
            all_dots.append(_make_dots(i, x, rnd=rnd))

        bact = _make_bacterium()
        down_arrows = _make_down_arrows()

        # 1. Static layout — all patches and dots appear
        self.play(
            LaggedStart(
                *[AnimationGroup(FadeIn(patches[i]), FadeIn(all_dots[i]))
                  for i in range(6)],
                lag_ratio=0.18,
                run_time=1.8,
            )
        )
        self.play(Create(bact), run_time=0.6)

        # 2. Each arrow lands → yellow glow pulse → patch Flash → dots shift
        rnd2 = random.Random(99)
        for j in range(3):
            # Grow arrow
            self.play(GrowArrow(down_arrows[j]), run_time=0.45)

            # Yellow glow pulse on arrow (Indicate approximated by Flash at arrow tip)
            tip_pos = np.array([_XS[j], 0.25, 0.0])
            self.play(
                Flash(tip_pos, color=ORANGE, line_length=0.25, num_lines=8, flash_radius=0.5),
                run_time=0.3,
            )

            # Patch Flash
            self.play(
                Flash(
                    np.array([_XS[j], -0.8, 0.0]),
                    color=SKY,
                    line_length=0.3,
                    num_lines=10,
                    flash_radius=0.9,
                ),
                run_time=0.3,
            )

            # Dots rearrange to more disordered positions (next-stage scatter)
            extra_spread = (j + 1) * 0.10
            new_dots = VGroup(*[
                Dot(
                    point=np.array([
                        _XS[j] - 0.52 + (k % 4) * 0.34 + rnd2.uniform(-extra_spread, extra_spread),
                        -1.30 + (k // 4) * 0.34 + rnd2.uniform(-extra_spread, extra_spread),
                        0.0,
                    ]),
                    radius=0.07,
                    color=BLUE,
                )
                for k in range(4 + j * 3)
            ])
            self.play(
                Transform(all_dots[j], new_dots),
                run_time=0.35,
            )

        # 3. Patches 4 and 5 progress without bacterium arrows (autonomous)
        for j in range(3, 5):
            self.play(
                Flash(
                    np.array([_XS[j], -0.8, 0.0]),
                    color=SKY,
                    line_length=0.25,
                    num_lines=8,
                    flash_radius=0.75,
                ),
                run_time=0.3,
            )

        # 4. Final cancer patch transforms to ORANGE with Flash
        patches[5].set_fill(ORANGE, opacity=0.35)
        patches[5].set_stroke(ORANGE)
        self.play(
            FadeIn(patches[5]),
            run_time=0.4,
        )
        self.play(
            Flash(
                np.array([_XS[5], -0.8, 0.0]),
                color=ORANGE,
                line_length=0.45,
                num_lines=14,
                flash_radius=1.3,
            ),
            run_time=0.5,
        )
        self.wait(0.8)
