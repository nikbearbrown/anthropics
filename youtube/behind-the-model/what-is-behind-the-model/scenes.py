from manim import *
import math
import random

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_MoodFallacy(Scene):
    """B01 — wrong model: quality vs mood labels is pure noise."""
    def construct(self):
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 10, 2],
                    x_length=7, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 2},
                    tips=False)
        mood_labels = ["lazy", "tired", "okay", "good", "sharp"]
        for i, label in enumerate(mood_labels):
            t = Text(label, font_size=24, color=INK, font=FONT).next_to(axes.coords_to_point(i + 0.5, 0), DOWN, buff=0.25)
            self.play(FadeIn(t), run_time=0.15)

        x_label = Text("Perceived mood", font_size=24, color=INK, font=FONT).next_to(axes, DOWN, buff=0.5)
        y_label = Text("Output quality", font_size=24, color=INK, font=FONT).rotate(PI/2).next_to(axes, LEFT, buff=0.25)
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.4)

        rng = random.Random(42)
        dots = VGroup(*[
            Dot(axes.coords_to_point(rng.uniform(0.1, 4.9), rng.uniform(0.5, 9.5)),
                color=INK, radius=0.09)
            for _ in range(18)
        ])
        self.play(FadeIn(dots), run_time=0.4)

        wobble_line = axes.plot(lambda x: 5 + 2 * math.sin(x * 2), x_range=[0, 5], color=TERRA, stroke_width=2.5)
        self.play(Create(wobble_line), run_time=0.5)
        self.play(FadeOut(wobble_line), run_time=0.3)

        noise = Text("Pure noise.", font_size=38, color=INK, weight=BOLD, font=FONT).shift(DOWN*3.4)
        self.play(Write(noise), run_time=0.5)
        self.wait(0.9)


class B02_ContextWindowSlide(Scene):
    """B02 — right model: context window slides, early turns fall off left."""
    def construct(self):
        window_width = 8
        window = RoundedRectangle(width=window_width, height=2.2, color=INK, stroke_width=3).shift(UP*1.2)
        win_label = Text("Context window", font_size=24, color=INK, font=FONT).next_to(window, UP, buff=0.2)
        self.play(FadeIn(window), Write(win_label), run_time=0.4)

        turns = ["Turn 1", "Turn 2", "Turn 3", "Turn 4", "Turn 5", "Turn 6", "Turn 7"]
        turn_mobs = []
        for i, t in enumerate(turns):
            mob = RoundedRectangle(width=1.6, height=1.6, color=INK, stroke_width=1.5).set_fill("#EAE7DC", opacity=1)
            mob.move_to(window.get_left() + RIGHT*(1.0 + i*2.0))
            label_t = Text(t, font_size=24, color=INK, font=FONT).move_to(mob)
            grp = VGroup(mob, label_t)
            turn_mobs.append(grp)

        # Show first 4 inside window
        for mob in turn_mobs[:4]:
            self.play(FadeIn(mob), run_time=0.2)

        # Slide in new turns; fade the exiting one simultaneously to avoid off-frame audit errors
        active = list(turn_mobs[:4])  # currently visible mobs
        for i in range(3):
            new_mob = turn_mobs[4 + i]
            new_mob.move_to(window.get_right() + RIGHT*1.0)
            exiting = active[0]
            staying = active[1:]
            self.play(
                *[mob.animate.shift(LEFT*2) for mob in staying],
                FadeOut(exiting),
                FadeIn(new_mob),
                run_time=0.4,
            )
            active = staying + [new_mob]

        answer = Text("Answer changes as source material leaves.", font_size=26, color=INK, font=FONT).shift(DOWN*2)
        self.play(Write(answer), run_time=0.5)
        self.wait(0.9)


class B04_ConfidenceIsNotWorld(Scene):
    """B04 — do this now: model confidence vs world-agreement diverge."""
    def construct(self):
        axes = Axes(x_range=[0, 8, 1], y_range=[0, 1.1, 0.2],
                    x_length=9, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 2},
                    tips=False)
        x_label = Text("Time / usage", font_size=24, color=INK, font=FONT).next_to(axes, DOWN, buff=0.2)
        self.play(Create(axes), Write(x_label), run_time=0.4)

        confidence = axes.plot(lambda x: 0.9, x_range=[0, 8], color=INK, stroke_width=2.5)
        # Labels placed inside the plot to avoid right-edge overflow
        conf_label = Text("Model confidence", font_size=24, color=INK, font=FONT).next_to(axes.coords_to_point(4, 0.9), UP, buff=0.12)
        self.play(Create(confidence), Write(conf_label), run_time=0.5)

        world = axes.plot(lambda x: max(0.1, 0.9 - x * 0.1), x_range=[0, 8], color=TERRA, stroke_width=2.5)
        world_label = Text("World-agreement", font_size=24, color=INK, weight=BOLD, font=FONT).next_to(axes.coords_to_point(4, 0.4), DOWN, buff=0.12)
        self.play(Create(world), Write(world_label), run_time=0.6)

        gap_line = DoubleArrow(axes.coords_to_point(6, 0.9), axes.coords_to_point(6, 0.3), color=TERRA, stroke_width=2)
        gap_label = Text("gap", font_size=24, color=INK, font=FONT).next_to(gap_line, RIGHT, buff=0.15)
        self.play(Create(gap_line), Write(gap_label), run_time=0.4)

        # FadeOut x_label before key_line to avoid text-on-text overlap at DOWN*3.1
        self.play(FadeOut(x_label), run_time=0.2)
        key_line = Text("Confidence: a property of the model,\nnot the world.", font_size=26, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.9)
        self.play(Write(key_line), run_time=0.6)
        self.wait(0.8)
