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
