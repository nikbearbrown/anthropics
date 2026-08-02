from manim import *

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"

# Guardian positions: top, middle, bottom
GY_POS = [
    [-2.2,  2.0, 0],
    [-2.2,  0.0, 0],
    [-2.2, -2.0, 0],
]

GUARDIAN_W = 2.8
GUARDIAN_H = 1.35
NOTCH_W    = 0.55
NOTCH_H    = 0.50


def _guardian(pos):
    return RoundedRectangle(
        width=GUARDIAN_W, height=GUARDIAN_H,
        corner_radius=0.20,
        color=BLUE, fill_color=BLUE, fill_opacity=0.16,
        stroke_width=3.2,
    ).move_to(pos)


def _notch_cover(pos):
    """White rectangle that simulates a notch cut on the right edge."""
    return Rectangle(
        width=NOTCH_W, height=NOTCH_H,
        color=WHITE, fill_color=WHITE, fill_opacity=1.0,
        stroke_width=0,
    ).move_to([pos[0] + GUARDIAN_W / 2 - NOTCH_W / 2 + 0.02, pos[1], 0])


def _captive_wedge(cx, cy, color, size=0.30):
    """Triangle wedge pointing right."""
    return Polygon(
        [cx - size, cy - size * 0.7, 0],
        [cx - size, cy + size * 0.7, 0],
        [cx + size, cy, 0],
        color=color, fill_color=color, fill_opacity=0.80,
        stroke_width=2.0,
    )


def _trigger_circle():
    return Circle(
        radius=0.42,
        color=GREEN, fill_color=GREEN, fill_opacity=0.28,
        stroke_width=3.0,
    ).move_to([3.2, -0.5, 0])


# ============================================================
# B05_BclSelectivity — initial animation
#   guardians → captives → plug + arrows → trigger
# ============================================================
class B05_BclSelectivity(Scene):
    def construct(self):
        # 1. Three BLUE guardian rectangles (LaggedStart)
        guardians = [_guardian(p) for p in GY_POS]
        notches   = [_notch_cover(p) for p in GY_POS]

        self.play(
            LaggedStart(*[FadeIn(g) for g in guardians],
                        lag_ratio=0.22, run_time=1.0)
        )
        # Notches appear immediately after guardians
        self.play(*[FadeIn(n) for n in notches], run_time=0.4)

        # 2. SKY captive wedges inside top and bottom guardians (held)
        sky_top = _captive_wedge(
            GY_POS[0][0] + 0.90, GY_POS[0][1], SKY)
        sky_bot = _captive_wedge(
            GY_POS[2][0] + 0.90, GY_POS[2][1], SKY)
        self.play(FadeIn(sky_top), FadeIn(sky_bot), run_time=0.5)

        # 3. VERM displaced captive next to middle guardian
        verm_cap = _captive_wedge(-0.10, GY_POS[1][1], VERM)
        self.play(FadeIn(verm_cap), run_time=0.4)

        # 4. ORANGE plug at far right
        plug = _captive_wedge(4.2, GY_POS[1][1], ORANGE, size=0.38)
        self.play(FadeIn(plug, shift=RIGHT * 0.5), run_time=0.4)

        # 5. Plug arrow: plug → middle guardian notch
        plug_arrow = Arrow(
            start=[4.2, GY_POS[1][1], 0],
            end=[-0.80, GY_POS[1][1], 0],
            color=ORANGE, buff=0.50,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(GrowArrow(plug_arrow), run_time=0.7)

        # 6. Displaced captive arrow → GREEN trigger
        trigger = _trigger_circle()
        disp_arrow = Arrow(
            start=[-0.10, GY_POS[1][1], 0],
            end=[2.75, -0.5, 0],
            color=VERM, buff=0.45,
            stroke_width=3.0,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(GrowArrow(disp_arrow), run_time=0.6)
        self.play(
            FadeIn(trigger),
            Flash(
                trigger.get_center(),
                color=GREEN, line_length=0.28,
                num_lines=8, flash_radius=0.65,
            ),
            run_time=0.6,
        )
        self.wait(0.8)


# ============================================================
# B07_BclSelectivityFit — revised: plug moves, captive travels, trigger bounces
# ============================================================
class B07_BclSelectivityFit(Scene):
    def construct(self):
        # 1. Build all three guardians with captives
        guardians = [_guardian(p) for p in GY_POS]
        notches   = [_notch_cover(p) for p in GY_POS]

        self.play(
            LaggedStart(*[FadeIn(g) for g in guardians],
                        lag_ratio=0.20, run_time=0.9)
        )
        self.play(*[FadeIn(n) for n in notches], run_time=0.35)

        # SKY captives in top and bottom (they will stay still)
        sky_top = _captive_wedge(
            GY_POS[0][0] + 0.90, GY_POS[0][1], SKY)
        sky_bot = _captive_wedge(
            GY_POS[2][0] + 0.90, GY_POS[2][1], SKY)
        # VERM captive INSIDE middle guardian (to be displaced)
        verm_inside = _captive_wedge(
            GY_POS[1][0] + 0.90, GY_POS[1][1], VERM)

        self.play(
            FadeIn(sky_top), FadeIn(sky_bot), FadeIn(verm_inside),
            run_time=0.5,
        )

        # ORANGE plug — starts at right, will move to notch
        plug_start_x = 4.2
        plug_end_x   = -0.75      # entering the notch area
        plug = _captive_wedge(plug_start_x, GY_POS[1][1], ORANGE, size=0.38)
        self.play(FadeIn(plug, shift=RIGHT * 0.5), run_time=0.4)

        # 2. Plug moves from right into middle notch
        self.play(
            plug.animate.move_to([plug_end_x, GY_POS[1][1], 0]),
            run_time=0.9,
        )

        # 3. Middle captive (VERM) pushed out — moves toward trigger
        trigger_pos = [3.2, -0.5, 0]
        trigger = _trigger_circle()

        self.play(
            verm_inside.animate.move_to([-0.10, GY_POS[1][1], 0]),
            run_time=0.5,
        )
        self.play(
            verm_inside.animate.move_to(trigger_pos),
            run_time=0.75,
        )

        # 4. Top and bottom captives — emphasize they DON'T MOVE
        # Brief highlight (slight scale pulse then back)
        self.play(
            sky_top.animate.scale(1.18),
            sky_bot.animate.scale(1.18),
            run_time=0.35,
        )
        self.play(
            sky_top.animate.scale(1 / 1.18),
            sky_bot.animate.scale(1 / 1.18),
            run_time=0.30,
        )

        # 5. Trigger assembles with scale bounce
        self.play(FadeIn(trigger, scale=0.5), run_time=0.35)
        self.play(trigger.animate.scale(1.25), run_time=0.25)
        self.play(trigger.animate.scale(1 / 1.25), run_time=0.20)

        # Flash on trigger
        self.play(
            Flash(
                trigger.get_center(),
                color=GREEN, line_length=0.30,
                num_lines=10, flash_radius=0.70,
            ),
            run_time=0.5,
        )
        self.wait(0.8)

class STD_B01_claude_liam_bcl_selectivi(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-bcl-selectivity.
    Narration: 'The BCL-2 family has multiple anti-death guardians, and each holds a different p'
    Duration: 15.6s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "BCL Selectivity"
        body_lines = ["The BCL-2 family has multiple anti-death", "guardians, and each holds a different pro-", "death\u2026", "To trigger apoptosis you have to displace", "a specific captive from a specific", "guardian"]
        spark_str = "The plate shows the lock-and-key geometry: only one plug fit"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.47)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_bcl_selectivi(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-bcl-selectivity.
    Narration: 'Venetoclax is selective for BCL-2 specifically — not BCL-XL, not MCL-1. That sel'
    Duration: 17.9s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "BCL Selectivity"
        body_lines = ["Venetoclax is selective for BCL-2 specifically \u2014", "not BCL-XL, not MCL-1", "That selectivity is the whole mechanism", "It displaces only the captive held by BCL-2,", "freeing it to trigger the death cascade"]
        spark_str = "Cells that depend on BCL-2 die; cells that depend on other g"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.43)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_bcl_selectivi(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-bcl-selectivity.
    Narration: 'Three locks, one key that fits only one. The motion showed what selectivity mean'
    Duration: 21.2s  Lines: 7  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "BCL Selectivity"
        body_lines = ["Three locks, one key that fits only one", "The motion showed what selectivity means", "physically: the plug engages one notch, one\u2026", "Claude ported the plate geometry in one prompt", "and added the animated displacement in one\u2026", "The pattern: build the locks, move the key, show", "what doesn't move"]
        spark_str = "Strip that and you can animate any receptor-ligand selectivi"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.91)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
