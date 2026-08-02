from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
PURPLE = "#CC79A7"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"
INK    = "#333333"

# ============================================================
# Layout constants (Manim frame ±7.11 wide, ±4.0 tall)
# Source:  x=-4.8, y=0
# Brakes:  x=+0.5, y=+1.55 (upper), y=-1.55 (lower)
# Output:  x=+5.0, y=0
# ============================================================

SRC_X   = -4.8
SRC_Y   =  0.0
BRK_X   =  0.5
BRK_YU  =  1.55   # upper brake
BRK_YL  = -1.55   # lower brake
OUT_X   =  5.0
OUT_Y   =  0.0

SRC_R   = 0.72   # scale of heptagon
BRK_R   = 0.62   # scale of octagon


def make_source():
    return RegularPolygon(
        n=7, color=PURPLE, fill_color=PURPLE, fill_opacity=0.28,
        stroke_width=3.2,
    ).scale(SRC_R).move_to([SRC_X, SRC_Y, 0])


def make_brake(y):
    return RegularPolygon(
        n=8, color=BLUE, fill_color=BLUE, fill_opacity=0.22,
        stroke_width=3.0,
    ).scale(BRK_R).move_to([BRK_X, y, 0])


def make_xmark(cx, cy, size=0.32):
    """VERM X-mark centred at (cx, cy)."""
    return VGroup(
        Line([cx - size, cy + size, 0], [cx + size, cy - size, 0],
             color=VERM, stroke_width=8),
        Line([cx - size, cy - size, 0], [cx + size, cy + size, 0],
             color=VERM, stroke_width=8),
    )


def make_output_cluster():
    """6 GREEN circles in a 3×2 hex arrangement centred at OUT_X, OUT_Y."""
    offsets = [
        (-0.32, 0.38), (0.32, 0.38), (0.64, 0.0),
        (0.32, -0.38), (-0.32, -0.38), (-0.64, 0.0),
    ]
    return VGroup(*[
        Circle(radius=0.24, color=GREEN, fill_color=GREEN,
               fill_opacity=0.70, stroke_width=1.8)
        .move_to([OUT_X + dx, OUT_Y + dy, 0])
        for dx, dy in offsets
    ])


def div_arrow(y_brake):
    """Diverging arrow: source → brake."""
    start = np.array([SRC_X + SRC_R + 0.12, SRC_Y, 0])
    end   = np.array([BRK_X - BRK_R - 0.12, y_brake, 0])
    return Arrow(start, end, color=GRAY, stroke_width=2.8,
                 max_tip_length_to_length_ratio=0.16,
                 max_stroke_width_to_length_ratio=6)


def conv_arrow(y_brake):
    """Converging arrow: brake → output."""
    start = np.array([BRK_X + BRK_R + 0.12, y_brake, 0])
    end   = np.array([OUT_X - 0.80, OUT_Y, 0])
    return Arrow(start, end, color=GRAY, stroke_width=2.8,
                 max_tip_length_to_length_ratio=0.16,
                 max_stroke_width_to_length_ratio=6)


# ============================================================
# B05_HpvDualHit — initial animation
#   Source → diverge → both brakes + X-marks → converge → output
# ============================================================
class B05_HpvDualHit(Scene):
    def construct(self):
        source = make_source()
        brake_U = make_brake(BRK_YU)
        brake_L = make_brake(BRK_YL)
        xmark_U = make_xmark(BRK_X, BRK_YU)
        xmark_L = make_xmark(BRK_X, BRK_YL)
        cluster = make_output_cluster()

        div_arr_U = div_arrow(BRK_YU)
        div_arr_L = div_arrow(BRK_YL)
        conv_arr_U = conv_arrow(BRK_YU)
        conv_arr_L = conv_arrow(BRK_YL)

        # 1. Source
        self.play(FadeIn(source), run_time=0.40)
        self.wait(0.15)

        # 2. Diverging arrows (LaggedStart)
        self.play(
            LaggedStart(GrowArrow(div_arr_U), GrowArrow(div_arr_L),
                        lag_ratio=0.25, run_time=0.90)
        )

        # 3. Both brakes appear simultaneously
        self.play(
            LaggedStart(FadeIn(brake_U), FadeIn(brake_L),
                        lag_ratio=0.12, run_time=0.55)
        )

        # 4. X-marks appear: upper first, then lower (slight stagger)
        self.play(
            LaggedStart(FadeIn(xmark_U), FadeIn(xmark_L),
                        lag_ratio=0.40, run_time=0.70)
        )
        self.wait(0.25)

        # 5. Converging arrows
        self.play(
            LaggedStart(GrowArrow(conv_arr_U), GrowArrow(conv_arr_L),
                        lag_ratio=0.25, run_time=0.85)
        )

        # 6. Output cluster
        self.play(FadeIn(cluster), run_time=0.45)
        self.wait(0.80)


# ============================================================
# B07_HpvDualHitTiming — revised: sequential brake strikes, output Flash
#   Source → diverge → brake U (Flash) → brake L (Flash) → converge → output Flash
# ============================================================
class B07_HpvDualHitTiming(Scene):
    def construct(self):
        source = make_source()
        brake_U = make_brake(BRK_YU)
        brake_L = make_brake(BRK_YL)
        xmark_U = make_xmark(BRK_X, BRK_YU)
        xmark_L = make_xmark(BRK_X, BRK_YL)
        cluster = make_output_cluster()

        div_arr_U = div_arrow(BRK_YU)
        div_arr_L = div_arrow(BRK_YL)
        conv_arr_U = conv_arrow(BRK_YU)
        conv_arr_L = conv_arrow(BRK_YL)

        # 1. Source
        self.play(FadeIn(source), run_time=0.40)
        self.wait(0.15)

        # 2. Both diverging arrows grow (source fans out to both brakes)
        self.play(
            LaggedStart(GrowArrow(div_arr_U), GrowArrow(div_arr_L),
                        lag_ratio=0.22, run_time=0.85)
        )

        # 3. UPPER brake appears + X-mark with Flash (E6 hits p53)
        self.play(FadeIn(brake_U), run_time=0.35)
        self.play(
            FadeIn(xmark_U),
            Flash(np.array([BRK_X, BRK_YU, 0]),
                  color=VERM, line_length=0.30, num_lines=12,
                  flash_radius=0.75),
            run_time=0.50,
        )
        self.wait(0.35)  # hold — E6 hit is distinct

        # 4. LOWER brake appears + X-mark with Flash (E7 hits Rb)
        self.play(FadeIn(brake_L), run_time=0.35)
        self.play(
            FadeIn(xmark_L),
            Flash(np.array([BRK_X, BRK_YL, 0]),
                  color=VERM, line_length=0.30, num_lines=12,
                  flash_radius=0.75),
            run_time=0.50,
        )
        self.wait(0.30)  # both cuts complete

        # 5. Converging arrows — only now that BOTH are struck
        self.play(
            LaggedStart(GrowArrow(conv_arr_U), GrowArrow(conv_arr_L),
                        lag_ratio=0.22, run_time=0.80)
        )

        # 6. Output cluster appears, then Flashes GREEN (unchecked division)
        self.play(FadeIn(cluster), run_time=0.40)
        self.play(
            Flash(np.array([OUT_X, OUT_Y, 0]),
                  color=GREEN, line_length=0.38, num_lines=14,
                  flash_radius=0.95),
            run_time=0.55,
        )
        self.wait(0.80)
