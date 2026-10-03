from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbBoondoggleScore(Scene):
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("PROBLEM", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        labels_text = ["Test file", "Count", "Artifact"]
        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        box_mobs = []
        arrows = VGroup()
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color=INK, stroke_width=2,
                                   fill_color=BG, fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=26, color=INK, font=font)
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color=TERRA, stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 8.0))


class Scene_B07_NbbBoondoggleScore(Scene):
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("SUMMARY", font_size=28, color=INK, font=font)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        line1 = Text("A diagnostic before code.", font_size=44, color=INK, font=font)
        line1.shift(UP * 0.3)
        self.play(Write(line1), run_time=0.6)

        line2 = Text("The highest-risk row is the one",
                     font_size=32, color=INK, font=font)
        line2.shift(DOWN * 0.5)
        line3 = Text("every step inherits from.",
                     font_size=32, color=INK, font=font)
        line3.shift(DOWN * 1.15)
        self.play(Write(line2), run_time=0.5)
        self.play(Write(line3), run_time=0.5)

        self.wait(max(0.01, 7.0))


class Scene_B08_NbbBoondoggleScore(Scene):
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("NEXT STEPS", font_size=28, color=INK, font=font)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=3)
        spark.shift(UP * 0.9)
        self.play(Create(spark), run_time=0.2)

        line1 = Text("Run the three-pass",
                     font_size=44, color=INK, font=font)
        line1.shift(UP * 0.0)
        line2 = Text("verification protocol.",
                     font_size=44, color=INK, font=font)
        line2.shift(DOWN * 0.8)
        self.play(Write(line1), run_time=0.5)
        self.play(Write(line2), run_time=0.5)

        self.wait(max(0.01, 1.5))
