from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"
INK    = "#333333"

# ============================================================
# Layout constants
# Manim frame: ±7.11 wide, ±4.0 tall
# Top state centred at y=+1.65; bottom state at y=-1.60
# Metaphase plate: x=-4.0 to x=+2.6
# Pole dots: left at x=-5.0, right at x=+3.0
# Chromosome pairs at x: [-2.8, -1.3, 0.2, 1.7]
# Anaphase arrow/bar: x=+3.3 onward
# ============================================================

POLE_L  = np.array([-5.0,  0.0, 0])
POLE_R  = np.array([ 3.2,  0.0, 0])
CHR_XS  = [-2.8, -1.3, 0.2, 1.7]
UNATT_IDX = 2   # pair index 2 is unattached

PLATE_X0 = -4.4
PLATE_X1 =  2.8


def pole_dot(x, y):
    return Dot(point=[x, y, 0], radius=0.13, color=GREEN, fill_opacity=0.9)


def chr_pair(x, y):
    """Two BLUE circles side by side representing a chromosome pair."""
    return VGroup(
        Circle(radius=0.22, color=BLUE, fill_color=BLUE,
               fill_opacity=0.30, stroke_width=2.4).move_to([x - 0.25, y, 0]),
        Circle(radius=0.22, color=BLUE, fill_color=BLUE,
               fill_opacity=0.30, stroke_width=2.4).move_to([x + 0.25, y, 0]),
    )


def spindle_lines(x, y, pole_l, pole_r):
    """Gray lines from chromosome centre to both poles."""
    return VGroup(
        Line([x, y, 0], pole_l, color=GRAY, stroke_width=1.6),
        Line([x, y, 0], pole_r, color=GRAY, stroke_width=1.6),
    )


def starburst_mob(cx, cy):
    """VERM starburst (wait signal) — 8 short lines radiating from a point."""
    lines = VGroup()
    for k in range(8):
        angle = k * PI / 4
        start = np.array([cx + 0.12 * np.cos(angle), cy + 0.12 * np.sin(angle), 0])
        end   = np.array([cx + 0.42 * np.cos(angle), cy + 0.42 * np.sin(angle), 0])
        lines.add(Line(start, end, color=VERM, stroke_width=3.5))
    core = Dot(radius=0.10, color=VERM, fill_opacity=0.9).move_to([cx, cy, 0])
    return VGroup(lines, core)


def orange_bar(x, y):
    return Rectangle(
        width=0.32, height=1.0,
        fill_color=ORANGE, fill_opacity=0.70,
        stroke_color=ORANGE, stroke_width=3.0,
    ).move_to([x, y, 0])


def sister_cluster(cx, cy, n=3):
    """Small cluster of BLUE circles representing separated sisters at pole."""
    group = VGroup()
    offsets = [(-0.28, 0.22), (0.0, 0.28), (0.28, 0.22),
               (-0.28, -0.22), (0.0, -0.28), (0.28, -0.22)][:n]
    for dx, dy in offsets:
        group.add(Circle(radius=0.20, color=BLUE, fill_color=BLUE,
                         fill_opacity=0.65, stroke_width=1.8)
                  .move_to([cx + dx, cy + dy, 0]))
    return group


# ============================================================
# B05_SpindleCheckpoint — two-state build (static top, static bottom)
# ============================================================
class B05_SpindleCheckpoint(Scene):
    def construct(self):
        y_top = 1.65
        y_bot = -1.60

        # ---- TOP STATE: BLOCKED ----
        plate_top = DashedLine(
            [PLATE_X0, y_top, 0], [PLATE_X1, y_top, 0],
            color=GRAY, stroke_width=2.2, dash_length=0.18
        )
        pL_top = pole_dot(-5.0, y_top)
        pR_top = pole_dot(3.2, y_top)

        pairs_top = VGroup(*[chr_pair(x, y_top) for x in CHR_XS])

        spindles_top = VGroup()
        for i, x in enumerate(CHR_XS):
            if i != UNATT_IDX:
                spindles_top.add(spindle_lines(x, y_top,
                                               [-5.0, y_top, 0],
                                               [3.2, y_top, 0]))

        # Unattached pair: short free line + starburst
        free_line = Line(
            [CHR_XS[UNATT_IDX], y_top, 0],
            [CHR_XS[UNATT_IDX] - 0.55, y_top - 0.38, 0],
            color=GRAY, stroke_width=1.6
        )
        burst = starburst_mob(CHR_XS[UNATT_IDX] - 0.80, y_top - 0.65)

        # Blocked arrow + bar
        arr_top = Arrow(
            [3.6, y_top, 0], [4.4, y_top, 0],
            color=GRAY, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.20
        )
        bar = orange_bar(4.55, y_top)

        # Animate top state
        self.play(Create(plate_top), FadeIn(pL_top), FadeIn(pR_top), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(p) for p in pairs_top], lag_ratio=0.20, run_time=0.80)
        )
        self.play(Create(spindles_top), run_time=0.50)
        self.play(Create(free_line), FadeIn(burst), run_time=0.45)
        self.play(GrowArrow(arr_top), FadeIn(bar), run_time=0.40)
        self.wait(0.35)

        # Separator
        sep = DashedLine([-6.8, 0.0, 0], [6.8, 0.0, 0],
                         color=GRAY, stroke_width=1.0, dash_length=0.22)
        self.play(Create(sep), run_time=0.35)

        # ---- BOTTOM STATE: RELEASED ----
        plate_bot = DashedLine(
            [PLATE_X0, y_bot, 0], [PLATE_X1, y_bot, 0],
            color=GRAY, stroke_width=2.2, dash_length=0.18
        )
        pL_bot = pole_dot(-5.0, y_bot)
        pR_bot = pole_dot(3.2, y_bot)

        pairs_bot = VGroup(*[chr_pair(x, y_bot) for x in CHR_XS])
        spindles_bot = VGroup(*[
            spindle_lines(x, y_bot, [-5.0, y_bot, 0], [3.2, y_bot, 0])
            for x in CHR_XS
        ])

        # Arrow clears, sisters at far right
        arr_bot = Arrow(
            [3.6, y_bot, 0], [5.2, y_bot, 0],
            color=GRAY, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.16
        )
        sisters_L = sister_cluster(5.6, y_bot - 0.25, n=3)
        sisters_R = sister_cluster(5.6, y_bot + 0.25, n=3)

        self.play(Create(plate_bot), FadeIn(pL_bot), FadeIn(pR_bot), run_time=0.45)
        self.play(
            LaggedStart(*[FadeIn(p) for p in pairs_bot], lag_ratio=0.20, run_time=0.75)
        )
        self.play(Create(spindles_bot), run_time=0.50)
        self.play(GrowArrow(arr_bot), run_time=0.35)
        self.play(
            LaggedStart(
                *[FadeIn(c) for c in [*sisters_L, *sisters_R]],
                lag_ratio=0.14, run_time=0.65
            )
        )
        self.wait(0.80)


# ============================================================
# B07_SpindleCheckpointRelease — animated transition
#   Build blocked state → animate release (starburst out, lines grow,
#   bar lifts, arrow extends, sisters migrate to poles)
# ============================================================
class B07_SpindleCheckpointRelease(Scene):
    def construct(self):
        y = 0.0  # single state centred vertically

        # ---- BUILD BLOCKED STATE ----
        plate = DashedLine(
            [PLATE_X0, y, 0], [PLATE_X1, y, 0],
            color=GRAY, stroke_width=2.2, dash_length=0.18
        )
        pL = pole_dot(-5.0, y)
        pR = pole_dot(3.2, y)

        pairs = VGroup(*[chr_pair(x, y) for x in CHR_XS])

        spindles = VGroup()
        for i, x in enumerate(CHR_XS):
            if i != UNATT_IDX:
                spindles.add(spindle_lines(x, y, [-5.0, y, 0], [3.2, y, 0]))

        free_line = Line(
            [CHR_XS[UNATT_IDX], y, 0],
            [CHR_XS[UNATT_IDX] - 0.55, y - 0.38, 0],
            color=GRAY, stroke_width=1.6
        )
        burst = starburst_mob(CHR_XS[UNATT_IDX] - 0.80, y - 0.65)

        arr = Arrow(
            [3.6, y, 0], [4.4, y, 0],
            color=GRAY, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.20
        )
        bar = orange_bar(4.55, y)

        # Build
        self.play(Create(plate), FadeIn(pL), FadeIn(pR), run_time=0.45)
        self.play(
            LaggedStart(*[FadeIn(p) for p in pairs], lag_ratio=0.18, run_time=0.70)
        )
        self.play(Create(spindles), run_time=0.45)
        self.play(Create(free_line), FadeIn(burst), run_time=0.40)
        self.play(GrowArrow(arr), FadeIn(bar), run_time=0.38)
        self.wait(0.45)  # hold the blocked state

        # ---- TRANSITION: RELEASE ----
        # 1. Starburst fades out
        self.play(FadeOut(burst), FadeOut(free_line), run_time=0.45)

        # 2. Spindle lines grow on the previously unattached pair
        new_lines = spindle_lines(
            CHR_XS[UNATT_IDX], y, [-5.0, y, 0], [3.2, y, 0]
        )
        self.play(Create(new_lines), run_time=0.65)
        self.wait(0.20)

        # 3. ORANGE bar lifts up then fades out
        self.play(bar.animate.shift(UP * 0.80), run_time=0.40)
        self.play(FadeOut(bar), run_time=0.30)

        # 4. Arrow extends past where bar was
        arr_ext = Arrow(
            [3.6, y, 0], [5.2, y, 0],
            color=GRAY, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.16
        )
        self.play(ReplacementTransform(arr, arr_ext), run_time=0.45)

        # 5. Chromosome pairs separate and migrate toward poles
        # Each pair splits: left circle → left pole, right circle → right pole
        left_targets = [
            np.array([CHR_XS[i] - 1.6, y, 0]) for i in range(4)
        ]
        right_targets = [
            np.array([CHR_XS[i] + 1.6, y, 0]) for i in range(4)
        ]

        migrate_anims = []
        for i, pair in enumerate(pairs):
            migrate_anims.append(pair[0].animate.move_to(left_targets[i]))
            migrate_anims.append(pair[1].animate.move_to(right_targets[i]))

        self.play(
            LaggedStart(*migrate_anims, lag_ratio=0.12, run_time=1.10)
        )
        self.wait(0.80)
