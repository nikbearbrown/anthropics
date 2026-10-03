from manim import *

BG    = "#FAF9F5"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


def _write_lines(scene, lines, sizes, y_positions, run_times):
    for text, size, y, rt in zip(lines, sizes, y_positions, run_times):
        t = Text(text, font_size=size, color=INK, font=FONT)
        t.scale(min(1.0, 13.0 / max(0.1, t.width)))
        t.move_to([0, y, 0])
        scene.play(Write(t), run_time=rt)


class Scene_B02_NbbOneSentence(Scene):
    """B02 — THE QUESTION. Duration target ~9.6s."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("THE QUESTION", font_size=32, color=INK, font=FONT)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.4)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=4)
        spark.shift(UP * 1.6)
        self.play(Create(spark), run_time=0.3)

        _write_lines(
            self,
            [
                "One sentence should be fast.",
                "Why did it take 14 minutes?",
            ],
            [72, 56],
            [0.4, -1.2],
            [0.9, 0.9],
        )
        self.wait(6.0)


class Scene_B03_NbbOneSentence(Scene):
    """B03 — THE MECHANISM. Duration target ~21.4s."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("THE MECHANISM", font_size=32, color=INK, font=FONT)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.4)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=4)
        spark.shift(UP * 1.9)
        self.play(Create(spark), run_time=0.3)

        _write_lines(
            self,
            [
                "One sentence with two ands",
                "= two projects disguised as one.",
                "The 'and' is a tell.",
            ],
            [72, 60, 60],
            [0.9, -0.4, -1.9],
            [1.0, 1.0, 1.0],
        )

        underline = Line(
            LEFT * 3.5, RIGHT * 3.5, color=TERRA, stroke_width=3
        ).shift(UP * 0.2)
        self.play(Create(underline), run_time=0.5)
        self.wait(15.5)


class Scene_B04_NbbOneSentence(Scene):
    """B04 — THE PRACTICE. Duration target ~17.7s."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("THE PRACTICE", font_size=32, color=INK, font=FONT)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.4)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=4)
        spark.shift(UP * 1.9)
        self.play(Create(spark), run_time=0.3)

        _write_lines(
            self,
            [
                "One system. One user. One done-condition.",
                "No ands.",
                "That sentence is your project.",
            ],
            [64, 72, 60],
            [0.9, -0.4, -1.9],
            [1.1, 0.9, 1.0],
        )

        underline = Line(
            LEFT * 3.5, RIGHT * 3.5, color=TERRA, stroke_width=3
        ).shift(UP * 0.2)
        self.play(Create(underline), run_time=0.5)
        self.wait(11.5)
