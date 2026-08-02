from manim import *

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"

# Meter geometry constants
COL_H  = 4.5
COL_W  = 1.4
THR_Y  = 1.2    # threshold y-position (in scene coords)
LX     = -2.5   # left meter x
RX     =  2.5   # right meter x


def _meter_column(cx):
    """Tall rounded column outline (GRAY, no fill)."""
    return RoundedRectangle(
        width=COL_W, height=COL_H, corner_radius=0.22,
        color=GRAY, fill_opacity=0, stroke_width=3,
    ).move_to([cx, 0, 0])


def _meter_fill(cx, frac, col):
    """Filled rectangle inside the column — frac of column height."""
    h   = COL_H * frac - 0.15
    col_rect = _meter_column(cx)
    bot = col_rect.get_bottom()[1]
    fill = Rectangle(
        width=COL_W - 0.14, height=h,
        color=col, fill_color=col, fill_opacity=0.55, stroke_width=0.8,
    )
    fill.move_to([cx, bot + h / 2 + 0.07, 0])
    return fill


def _threshold_line(cx):
    """Dashed threshold line at THR_Y."""
    return DashedLine(
        [cx - 0.75, THR_Y, 0], [cx + 0.75, THR_Y, 0],
        color=GRAY, stroke_width=2.5, dash_length=0.12,
    )


def _death_glyph(cx, cy):
    """VERM irregular hexagonal death glyph."""
    return Polygon(
        [cx - 0.40,  cy + 0.55, 0],
        [cx + 0.10,  cy + 0.25, 0],
        [cx - 0.10,  cy - 0.05, 0],
        [cx + 0.25,  cy - 0.25, 0],
        [cx + 0.00,  cy - 0.30, 0],
        [cx - 0.25,  cy - 0.08, 0],
        color=VERM, fill_color=VERM, fill_opacity=0.50, stroke_width=2.4,
    )


# ============================================================
# B05_VenetoclaxPriming — initial animation
#   left meter: SKY fill below threshold + BLUE clamp + ORANGE plug
#   center arrow
#   right meter: VERM fill above threshold + death glyph
# ============================================================
class B05_VenetoclaxPriming(Scene):
    def construct(self):
        # ── Left meter ──
        l_col   = _meter_column(LX)
        l_fill  = _meter_fill(LX, 0.72, SKY)
        l_thr   = _threshold_line(LX)
        clamp   = Rectangle(
            width=COL_W + 0.22, height=0.42,
            color=BLUE, fill_color=BLUE, fill_opacity=0.60, stroke_width=3,
        ).move_to([LX, l_col.get_top()[1] - 0.02, 0])
        plug    = Triangle(
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.80, stroke_width=2,
        ).scale(0.36).rotate(-PI / 2).move_to([LX - 1.85, 0.80, 0])
        plug_arr = Arrow(
            [LX - 1.45, 0.80, 0], [LX - 0.78, clamp.get_center()[1], 0],
            buff=0.05, color=ORANGE, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
        )

        # ── Center arrow ──
        c_arr = Arrow(
            [LX + 0.82, 0, 0], [RX - 0.82, 0, 0], buff=0,
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.18,
        )

        # ── Right meter ──
        r_col   = _meter_column(RX)
        r_fill  = _meter_fill(RX, 0.96, VERM)
        r_thr   = _threshold_line(RX)
        glyph   = _death_glyph(RX + 0.90, 1.20)
        g_arr   = Arrow(
            [RX + 0.05, r_fill.get_top()[1], 0],
            [RX + 0.65, 1.35, 0],
            buff=0.05, color=VERM, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
        )

        # ── Animation ──
        self.play(Create(l_col), run_time=0.45)
        self.play(FadeIn(l_fill), Create(l_thr), run_time=0.5)
        self.play(FadeIn(clamp), FadeIn(plug), GrowArrow(plug_arr), run_time=0.60)
        self.play(GrowArrow(c_arr), run_time=0.50)
        self.play(Create(r_col), run_time=0.40)
        self.play(FadeIn(r_fill), Create(r_thr), run_time=0.5)
        self.play(
            Flash(
                glyph.get_center(), color=VERM,
                line_length=0.28, num_lines=10, flash_radius=0.55,
            ),
            FadeIn(glyph, scale=0.80),
            GrowArrow(g_arr),
            run_time=0.55,
        )
        self.wait(0.9)


# ============================================================
# B07_VenetoclaxPrimingTip — revised animation
#   plug animates toward clamp → clamp FadeOut
#   fill rises from SKY→VERM (animate height) → threshold flashes
#   center arrow → right meter → death glyph assembles from fragments
# ============================================================
class B07_VenetoclaxPrimingTip(Scene):
    def construct(self):
        # ── Left meter (primed state) ──
        l_col   = _meter_column(LX)
        # Start with SKY fill at 72%
        l_fill_h_start = COL_H * 0.72 - 0.15
        l_col_bot       = l_col.get_bottom()[1]
        l_fill  = Rectangle(
            width=COL_W - 0.14, height=l_fill_h_start,
            color=SKY, fill_color=SKY, fill_opacity=0.55, stroke_width=0.8,
        ).move_to([LX, l_col_bot + l_fill_h_start / 2 + 0.07, 0])
        l_thr   = _threshold_line(LX)
        clamp   = Rectangle(
            width=COL_W + 0.22, height=0.42,
            color=BLUE, fill_color=BLUE, fill_opacity=0.60, stroke_width=3,
        ).move_to([LX, l_col.get_top()[1] - 0.02, 0])
        plug    = Triangle(
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.80, stroke_width=2,
        ).scale(0.36).rotate(-PI / 2).move_to([LX - 1.85, 0.80, 0])
        plug_arr = Arrow(
            [LX - 1.45, 0.80, 0], [LX - 0.78, clamp.get_center()[1], 0],
            buff=0.05, color=ORANGE, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
        )

        # ── Center arrow + right meter ──
        c_arr   = Arrow(
            [LX + 0.82, 0, 0], [RX - 0.82, 0, 0], buff=0,
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.18,
        )
        r_col   = _meter_column(RX)
        r_thr   = _threshold_line(RX)
        # Right fill starts at same 72% SKY, will become VERM and rise
        r_fill_init = Rectangle(
            width=COL_W - 0.14, height=l_fill_h_start,
            color=SKY, fill_color=SKY, fill_opacity=0.55, stroke_width=0.8,
        ).move_to([LX, l_col_bot + l_fill_h_start / 2 + 0.07, 0])

        # ── Death glyph fragments ──
        glyph_cx, glyph_cy = RX + 0.90, 1.20
        glyph_pts = [
            [glyph_cx - 0.40, glyph_cy + 0.55, 0],
            [glyph_cx + 0.10, glyph_cy + 0.25, 0],
            [glyph_cx - 0.10, glyph_cy - 0.05, 0],
            [glyph_cx + 0.25, glyph_cy - 0.25, 0],
            [glyph_cx + 0.00, glyph_cy - 0.30, 0],
            [glyph_cx - 0.25, glyph_cy - 0.08, 0],
        ]
        glyph_frags = VGroup(*[
            Polygon(
                glyph_pts[i],
                glyph_pts[(i + 1) % 6],
                glyph_pts[(i + 2) % 6],
                color=VERM, fill_color=VERM, fill_opacity=0.50, stroke_width=2.4,
            ) for i in range(0, 6, 2)
        ])

        # ── Phase 1: build primed left meter ──
        self.play(Create(l_col), run_time=0.40)
        self.play(FadeIn(l_fill), Create(l_thr), run_time=0.50)
        self.play(FadeIn(clamp), FadeIn(plug), GrowArrow(plug_arr), run_time=0.55)
        self.wait(0.15)

        # ── Phase 2: plug moves to clamp, clamp disappears ──
        self.play(
            plug.animate.move_to([LX - 0.82, clamp.get_center()[1], 0]),
            plug_arr.animate.set_opacity(0.0),
            run_time=0.65,
        )
        self.play(FadeOut(clamp), run_time=0.40)
        self.wait(0.10)

        # ── Phase 3: fill rises (animate height), threshold flashes when crossed ──
        # Target fill: 96% of column height, VERM
        l_fill_h_end = COL_H * 0.96 - 0.15
        l_fill_target = Rectangle(
            width=COL_W - 0.14, height=l_fill_h_end,
            color=VERM, fill_color=VERM, fill_opacity=0.55, stroke_width=0.8,
        ).move_to([LX, l_col_bot + l_fill_h_end / 2 + 0.07, 0])
        self.play(
            Transform(l_fill, l_fill_target),
            run_time=0.90,
        )
        # Flash threshold as fill crossed it
        self.play(
            Flash(
                [LX, THR_Y, 0], color=VERM,
                line_length=0.35, num_lines=8, flash_radius=0.70,
            ),
            l_thr.animate.set_color(VERM),
            run_time=0.50,
        )
        self.wait(0.10)

        # ── Phase 4: center arrow → right meter ──
        self.play(GrowArrow(c_arr), run_time=0.45)
        self.play(Create(r_col), run_time=0.38)
        # Right meter shows final VERM fill above threshold
        r_fill_final = _meter_fill(RX, 0.96, VERM)
        self.play(FadeIn(r_fill_final), Create(r_thr), run_time=0.50)

        # Arrow to death glyph
        g_arr = Arrow(
            [RX + 0.05, r_fill_final.get_top()[1], 0],
            [RX + 0.65, glyph_cy + 0.35, 0],
            buff=0.05, color=VERM, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
        )
        self.play(GrowArrow(g_arr), run_time=0.42)

        # ── Phase 5: death glyph assembles from fragments ──
        self.play(
            LaggedStart(*[FadeIn(f, scale=0.65) for f in glyph_frags],
                        lag_ratio=0.22, run_time=0.70),
        )
        self.wait(0.9)
