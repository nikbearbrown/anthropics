from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B02_SlopsquattingHallucinatedPackage(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: A student running pip install on a Claude-suggested package should be safe if th"""
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
        if "A student running pip install on a Claude-suggested package ":
            line1 = Text("A student running pip install on a Claude-suggested package ", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The package existed":
            line2 = Text("The package existed", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "An attacker put it there":
            line3 = Text("An attacker put it there", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A student running pip install on a Claude-suggested package ":
            uline = Line(LEFT * min(4.0, len("A student running pip install on a Claude-suggested package ") * 0.18), RIGHT * min(4.0, len("A student running pip install on a Claude-suggested package ") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B03_SlopsquattingHallucinatedPackage(Scene):
    """Beat B03 — SHOW: bar/proportion chart. Narration: Claude hallucinates package names. Across 576,000 code samples from 16 language """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#2A1A0E", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#2A1A0E", fill_color="#2A1A0E", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#C8102E", fill_color="#C8102E", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Claude hallucinates package names"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Across 576,000 code samples from 16 language models, researc"[:30] if "Across 576,000 code samples from 16 language models, researc" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Most of the time, the install fails loudly and you go fix it":
            note = Text("Most of the time, the install fails loudly and you go fix it"[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 3.00))


class Scene_B04_SlopsquattingHallucinatedPackage(Scene):
    """Beat B04 — SHOW: bar/proportion chart. Narration: The dangerous case is this: 58 percent of hallucinated package names recur acros"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#2A1A0E", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#2A1A0E", fill_color="#2A1A0E", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#C8102E", fill_color="#C8102E", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("The dangerous case is this: 58 percent of hallucinated packa"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("The same wrong name appears again and again, across sessions"[:30] if "The same wrong name appears again and again, across sessions" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "An attacker doesn\'t need to guess what your particular sessi":
            note = Text("An attacker doesn\'t need to guess what your particular sessi"[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 3.00))


class Scene_B05_SlopsquattingHallucinatedPackage(Scene):
    """Beat B05 — SHOW: pipeline / handoff flow. Narration: The attack runs in three steps. First: the model hallucinates a plausible-but-no"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        # Act label at top
        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["The attack runs in three steps", "First: the model hallucinates a plausible-but-nonexistent de", "Second: an attacker, knowing models invent names and that th"] if t]
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
                                   color="#2A1A0E", stroke_width=2,
                                   fill_color="#FFFFFF", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#C8102E", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B06_SlopsquattingHallucinatedPackage(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: This is slopsquatting — a real, documented supply-chain attack. The fabricated n"""
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
        if "This is slopsquatting - a real, documented supply-chain atta":
            line1 = Text("This is slopsquatting - a real, documented supply-chain atta", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The fabricated name no longer fails loudly":
            line2 = Text("The fabricated name no longer fails loudly", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "It resolves - to someone else\'s code":
            line3 = Text("It resolves - to someone else\'s code", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "This is slopsquatting - a real, documented supply-chain atta":
            uline = Line(LEFT * min(4.0, len("This is slopsquatting - a real, documented supply-chain atta") * 0.18), RIGHT * min(4.0, len("This is slopsquatting - a real, documented supply-chain atta") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B07_SlopsquattingHallucinatedPackage(Scene):
    """Beat B07 — SHOW: pipeline / handoff flow. Narration: Fatima\'s case is not the exotic edge case. It is the default workflow this chapt"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        # Act label at top
        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Fatima\'s case is not the exotic edge case", "It is the default workflow this chapter is warning about: Cl", "The entire workflow is exactly what slopsquatting is built t"] if t]
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
                                   color="#2A1A0E", stroke_width=2,
                                   fill_color="#FFFFFF", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#C8102E", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B08_SlopsquattingHallucinatedPackage(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: The defense is concrete and cheap. Before you run pip install or npm install on """
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
        if "The defense is concrete and cheap":
            line1 = Text("The defense is concrete and cheap", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Before you run pip install or npm install on any Claude-sugg":
            line2 = Text("Before you run pip install or npm install on any Claude-sugg", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "org or npmjs":
            line3 = Text("org or npmjs", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The defense is concrete and cheap":
            uline = Line(LEFT * min(4.0, len("The defense is concrete and cheap") * 0.18), RIGHT * min(4.0, len("The defense is concrete and cheap") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))


class Scene_B09_SlopsquattingHallucinatedPackage(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: Slopsquatting exists because the hallucination is predictable. Predictable means"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "RECAP":
            act = Text("RECAP", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Slopsquatting exists because the hallucination is predictabl":
            line1 = Text("Slopsquatting exists because the hallucination is predictabl", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Predictable means targetable":
            line2 = Text("Predictable means targetable", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Targetable means the install succeeds and the code runs and ":
            line3 = Text("Targetable means the install succeeds and the code runs and ", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Slopsquatting exists because the hallucination is predictabl":
            uline = Line(LEFT * min(4.0, len("Slopsquatting exists because the hallucination is predictabl") * 0.18), RIGHT * min(4.0, len("Slopsquatting exists because the hallucination is predictabl") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 3.00))
