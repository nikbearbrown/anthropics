from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B02_NbbOneSentence(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: Writing one sentence should be fast. Seth had been thinking about this project f"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE QUESTION":
            act = Text("THE QUESTION", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Writing one sentence should be fast":
            line1 = Text("Writing one sentence should be fast", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Seth had been thinking about this project for three days":
            line2 = Text("Seth had been thinking about this project for three days", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Why did it take fourteen minutes and two refusals to produce":
            line3 = Text("Why did it take fourteen minutes and two refusals to produce", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Writing one sentence should be fast":
            uline = Line(LEFT * min(4.0, len("Writing one sentence should be fast") * 0.18), RIGHT * min(4.0, len("Writing one sentence should be fast") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B03_NbbOneSentence(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: The one-sentence constraint is not about writing style. It is an elevator test f"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The one-sentence constraint is not about writing style":
            line1 = Text("The one-sentence constraint is not about writing style", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It is an elevator test for whether you know what you\'re buil":
            line2 = Text("It is an elevator test for whether you know what you\'re buil", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "A sentence with two ands is two systems dressed as one - dif":
            line3 = Text("A sentence with two ands is two systems dressed as one - dif", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The one-sentence constraint is not about writing style":
            uline = Line(LEFT * min(4.0, len("The one-sentence constraint is not about writing style") * 0.18), RIGHT * min(4.0, len("The one-sentence constraint is not about writing style") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B04_NbbOneSentence(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: The sentence that passes names one system, one user, one done-condition — and co"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PRACTICE":
            act = Text("THE PRACTICE", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The sentence that passes names one system, one user, one don":
            line1 = Text("The sentence that passes names one system, one user, one don", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The sentence that passes is the moment you take ownership of":
            line2 = Text("The sentence that passes is the moment you take ownership of", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Everything Claude produces from there gets measured against ":
            line3 = Text("Everything Claude produces from there gets measured against ", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The sentence that passes names one system, one user, one don":
            uline = Line(LEFT * min(4.0, len("The sentence that passes names one system, one user, one don") * 0.18), RIGHT * min(4.0, len("The sentence that passes names one system, one user, one don") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))
