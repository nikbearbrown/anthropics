from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamPrompt(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: This is Liam, in for Bear. Seth types: \'write me a login function.\' Eleven secon"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "This is Liam, in for Bear":
            line1 = Text("This is Liam, in for Bear", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Seth types: \'write me a login function":
            line2 = Text("Seth types: \'write me a login function", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "\' Eleven seconds later, he has a function":
            line3 = Text("\' Eleven seconds later, he has a function", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "This is Liam, in for Bear":
            uline = Line(LEFT * min(4.0, len("This is Liam, in for Bear") * 0.18), RIGHT * min(4.0, len("This is Liam, in for Bear") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B02_ClaudeLiamPrompt(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: A prompt should specify the task clearly enough to get the right output. \'Write """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A prompt should specify the task clearly enough to get the r":
            line1 = Text("A prompt should specify the task clearly enough to get the r", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "\'Write me a login function\' is a clear request":
            line2 = Text("\'Write me a login function\' is a clear request", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Why did it produce a function that would fail in production?":
            line3 = Text("Why did it produce a function that would fail in production?", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A prompt should specify the task clearly enough to get the r":
            uline = Line(LEFT * min(4.0, len("A prompt should specify the task clearly enough to get the r") * 0.18), RIGHT * min(4.0, len("A prompt should specify the task clearly enough to get the r") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B03_ClaudeLiamPrompt(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: A prompt is a wish addressed to someone who knows you. When you ask a friend to """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A prompt is a wish addressed to someone who knows you":
            line1 = Text("A prompt is a wish addressed to someone who knows you", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "When you ask a friend to write a login function, the friend ":
            line2 = Text("When you ask a friend to write a login function, the friend ", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "A friend resolves ambiguity by knowing you":
            line3 = Text("A friend resolves ambiguity by knowing you", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A prompt is a wish addressed to someone who knows you":
            uline = Line(LEFT * min(4.0, len("A prompt is a wish addressed to someone who knows you") * 0.18), RIGHT * min(4.0, len("A prompt is a wish addressed to someone who knows you") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B04_ClaudeLiamPrompt(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: Claude filled in the blanks. MD5 is the dominant hash pattern in the training di"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Claude filled in the blanks":
            line1 = Text("Claude filled in the blanks", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "MD5 is the dominant hash pattern in the training distributio":
            line2 = Text("MD5 is the dominant hash pattern in the training distributio", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "A global dict is the simplest user store":
            line3 = Text("A global dict is the simplest user store", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Claude filled in the blanks":
            uline = Line(LEFT * min(4.0, len("Claude filled in the blanks") * 0.18), RIGHT * min(4.0, len("Claude filled in the blanks") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B05_ClaudeLiamPrompt(Scene):
    """Beat B05 — SHOW: concept illustration card. Narration: A specification is a contract. It names the invariants the output must satisfy, """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A specification is a contract":
            line1 = Text("A specification is a contract", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It names the invariants the output must satisfy, the files t":
            line2 = Text("It names the invariants the output must satisfy, the files t", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "It assumes the listener is competent and amnesiac - capable ":
            line3 = Text("It assumes the listener is competent and amnesiac - capable ", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A specification is a contract":
            uline = Line(LEFT * min(4.0, len("A specification is a contract") * 0.18), RIGHT * min(4.0, len("A specification is a contract") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B06_ClaudeLiamPrompt(Scene):
    """Beat B06 — SHOW: pipeline / handoff flow. Narration: Same task, same Claude, same minute — six sentences instead of one. Use bcrypt, """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "":
            act = Text("", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Same task, same Claude, same minute - six sentences instead ", "Use bcrypt, not MD5", "Use the parameterized helper in db"] if t]
        if not labels_text:
            labels_text = ["Input", "Process", "Output"]

        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        boxes = VGroup()
        arrows = VGroup()
        box_mobs = []
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color="#3D3929", stroke_width=2,
                                   fill_color="#F2F0E9", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#3D3929", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#D97757", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B08_ClaudeLiamPrompt(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: Tomas builds a study tracker. He asks Claude to add a login. Claude returns a fu"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Tomas builds a study tracker":
            line1 = Text("Tomas builds a study tracker", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "He asks Claude to add a login":
            line2 = Text("He asks Claude to add a login", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude returns a function storing passwords in plaintext in ":
            line3 = Text("Claude returns a function storing passwords in plaintext in ", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Tomas builds a study tracker":
            uline = Line(LEFT * min(4.0, len("Tomas builds a study tracker") * 0.18), RIGHT * min(4.0, len("Tomas builds a study tracker") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B09_ClaudeLiamPrompt(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: The prompt is what you say to Claude before you have decided what you want. The """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The prompt is what you say to Claude before you have decided":
            line1 = Text("The prompt is what you say to Claude before you have decided", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The specification is what you say to Claude after":
            line2 = Text("The specification is what you say to Claude after", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The decision is the work":
            line3 = Text("The decision is the work", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The prompt is what you say to Claude before you have decided":
            uline = Line(LEFT * min(4.0, len("The prompt is what you say to Claude before you have decided") * 0.18), RIGHT * min(4.0, len("The prompt is what you say to Claude before you have decided") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B10_ClaudeLiamPrompt(Scene):
    """Beat B10 — SHOW: pipeline / handoff flow. Narration: The move has four steps. First: decide what you are actually building — a one-pa"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "":
            act = Text("", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["The move has four steps", "First: decide what you are actually building - a one-paragra", "Second: read what is already there"] if t]
        if not labels_text:
            labels_text = ["Input", "Process", "Output"]

        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        boxes = VGroup()
        arrows = VGroup()
        box_mobs = []
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color="#3D3929", stroke_width=2,
                                   fill_color="#F2F0E9", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#3D3929", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#D97757", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B11_ClaudeLiamPrompt(Scene):
    """Beat B11 — SHOW: bar/proportion chart. Narration: The second attempt took twenty minutes start to finish. The first took six secon"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("The second attempt took twenty minutes start to finish"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("The first took six seconds"[:30] if "The first took six seconds" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "The first was faster and produced a boondoggle - fluent acti":
            note = Text("The first was faster and produced a boondoggle - fluent acti"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.00))


class Scene_B12_ClaudeLiamPrompt(Scene):
    """Beat B12 — SHOW: pipeline / handoff flow. Narration: The prompt is what you wish for. The specification is what you contract for. The"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "":
            act = Text("", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["The prompt is what you wish for", "The specification is what you contract for", "The handoff condition is how you know the contract was kept"] if t]
        if not labels_text:
            labels_text = ["Input", "Process", "Output"]

        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        boxes = VGroup()
        arrows = VGroup()
        box_mobs = []
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color="#3D3929", stroke_width=2,
                                   fill_color="#F2F0E9", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#3D3929", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#D97757", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 9.00))
