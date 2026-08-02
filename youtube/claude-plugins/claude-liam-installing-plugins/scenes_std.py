from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamInstalling(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: Open the plugin section and you get a library — an official collection plus comm"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT I":
            act = Text("ACT I", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Open the plugin section and you get a library - an official ":
            line1 = Text("Open the plugin section and you get a library - an official ", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Each listing tells you what it does, what domain it covers, ":
            line2 = Text("Each listing tells you what it does, what domain it covers, ", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Browse by function; find the ones that fit your work":
            line3 = Text("Browse by function; find the ones that fit your work", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Open the plugin section and you get a library - an official ":
            uline = Line(LEFT * min(4.0, len("Open the plugin section and you get a library - an official ") * 0.18), RIGHT * min(4.0, len("Open the plugin section and you get a library - an official ") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.80))


class Scene_B02_ClaudeLiamInstalling(Scene):
    """Beat B02 — SHOW: bar/proportion chart. Narration: Click install. It downloads, activates, and it\'s ready — no setup wizard, no con"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT I":
            act = Text("ACT I", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Click install"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("It downloads, activates, and it\'s ready - no setup wizard, n"[:30] if "It downloads, activates, and it\'s ready - no setup wizard, n" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "If you\'ve ever added an app from a store, you already have t":
            note = Text("If you\'ve ever added an app from a store, you already have t"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.40))


class Scene_B05_ClaudeLiamInstalling(Scene):
    """Beat B05 — SHOW: pipeline / handoff flow. Narration: Out of the box, a plugin runs on sensible defaults — generic best practices for """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "ACT II":
            act = Text("ACT II", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Out of the box, a plugin runs on sensible defaults - generic", "But you don\'t do generic work", "You have your own process, your own terminology, your own wa"] if t]
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

        self.wait(max(0.01, 10.40))


class Scene_B06_ClaudeLiamInstalling(Scene):
    """Beat B06 — SHOW: pipeline / handoff flow. Narration: Click customize and Cowork doesn\'t open a settings panel — it starts a conversat"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "ACT II":
            act = Text("ACT II", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Click customize and Cowork doesn\'t open a settings panel - i", "It asks about your workflow, your preferences, your tools", "You answer in plain language"] if t]
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

        self.wait(max(0.01, 10.80))


class Scene_B07_ClaudeLiamInstalling(Scene):
    """Beat B07 — SHOW: bar/proportion chart. Narration: The pattern never changes: Claude asks, you answer, the plugin calibrates. Ask a"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT II":
            act = Text("ACT II", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("The pattern never changes: Claude asks, you answer, the plug"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Ask again, answer again, it tightens"[:30] if "Ask again, answer again, it tightens" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "It\'s the same loop whether you spend two questions or twenty":
            note = Text("It\'s the same loop whether you spend two questions or twenty"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 7.70))


class Scene_B09_ClaudeLiamInstalling(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: You install marketing and click customize. First question: what does your busine"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT III":
            act = Text("ACT III", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "You install marketing and click customize":
            line1 = Text("You install marketing and click customize", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "First question: what does your business do, and who are your":
            line2 = Text("First question: what does your business do, and who are your", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "You install marketing and click customize":
            uline = Line(LEFT * min(4.0, len("You install marketing and click customize") * 0.18), RIGHT * min(4.0, len("You install marketing and click customize") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.70))


class Scene_B13_ClaudeLiamInstalling(Scene):
    """Beat B13 — SHOW: two-column comparison. Narration: Now the output diverges. Ask for a content calendar and you get posts and newsle"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT III":
            act = Text("ACT III", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Left column
        left_box = RoundedRectangle(width=5.5, height=3.5, color="#3D3929", stroke_width=2,
                                     fill_color="#F2F0E9", fill_opacity=1).shift(LEFT * 3.2)
        left_text = Text("Now the output diverges"[:50], font_size=22, color="#3D3929", font=font)
        left_text.scale(min(1.0, 5.0 / max(0.1, left_text.width)))
        left_text.move_to(left_box)

        # Right column
        right_box = RoundedRectangle(width=5.5, height=3.5, color="#D97757", stroke_width=2,
                                      fill_color="#F2F0E9", fill_opacity=1).shift(RIGHT * 3.2)
        right_text = Text("Ask for a content calendar and you get posts and newsletter "[:50] if "Ask for a content calendar and you get posts and newsletter " else "Result", font_size=22, color="#3D3929", font=font)
        right_text.scale(min(1.0, 5.0 / max(0.1, right_text.width)))
        right_text.move_to(right_box)

        # Divider
        divider = Line(UP * 2, DOWN * 2, color="#3D3929", stroke_width=1.5)

        self.play(FadeIn(left_box), FadeIn(right_box), Create(divider), run_time=0.5)
        self.play(Write(left_text), Write(right_text), run_time=0.8)

        if "A competitive scan targets other web studios, not enterprise":
            note = Text("A competitive scan targets other web studios, not enterprise"[:60], font_size=20, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.3)
            self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.01, 13.20))


class Scene_B14_ClaudeLiamInstalling(Scene):
    """Beat B14 — SHOW: concept illustration card. Narration: Some plugins are self-contained — the productivity plugin works out of the box, """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT IV":
            act = Text("ACT IV", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Some plugins are self-contained - the productivity plugin wo":
            line1 = Text("Some plugins are self-contained - the productivity plugin wo", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Others get dramatically more useful the moment you plug them":
            line2 = Text("Others get dramatically more useful the moment you plug them", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Some plugins are self-contained - the productivity plugin wo":
            uline = Line(LEFT * min(4.0, len("Some plugins are self-contained - the productivity plugin wo") * 0.18), RIGHT * min(4.0, len("Some plugins are self-contained - the productivity plugin wo") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B15_ClaudeLiamInstalling(Scene):
    """Beat B15 — SHOW: concept illustration card. Narration: The sales plugin researches a prospect from public information alone — decent. C"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT IV":
            act = Text("ACT IV", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The sales plugin researches a prospect from public informati":
            line1 = Text("The sales plugin researches a prospect from public informati", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Connect it to your CRM and it pulls your relationship histor":
            line2 = Text("Connect it to your CRM and it pulls your relationship histor", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The reach jumps":
            line3 = Text("The reach jumps", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The sales plugin researches a prospect from public informati":
            uline = Line(LEFT * min(4.0, len("The sales plugin researches a prospect from public informati") * 0.18), RIGHT * min(4.0, len("The sales plugin researches a prospect from public informati") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.10))


class Scene_B18_ClaudeLiamInstalling(Scene):
    """Beat B18 — SHOW: bar/proportion chart. Narration: Want Claude to focus? Disable a plugin without removing it — your customization """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT V":
            act = Text("ACT V", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Want Claude to focus? Disable a plugin without removing it -"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Flip it back on when you need it"[:30] if "Flip it back on when you need it" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Nothing you taught it is lost":
            note = Text("Nothing you taught it is lost"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.00))


class Scene_B19_ClaudeLiamInstalling(Scene):
    """Beat B19 — SHOW: concept illustration card. Narration: Plugins improve over time — Anthropic and the community add features and fix iss"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT V":
            act = Text("ACT V", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Plugins improve over time - Anthropic and the community add ":
            line1 = Text("Plugins improve over time - Anthropic and the community add ", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Worth checking in occasionally to see what\'s new that you mi":
            line2 = Text("Worth checking in occasionally to see what\'s new that you mi", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Plugins improve over time - Anthropic and the community add ":
            uline = Line(LEFT * min(4.0, len("Plugins improve over time - Anthropic and the community add ") * 0.18), RIGHT * min(4.0, len("Plugins improve over time - Anthropic and the community add ") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B20_ClaudeLiamInstalling(Scene):
    """Beat B20 — SHOW: concept illustration card. Narration: Loading up on plugins doesn\'t slow Claude down or confuse it — but in practice m"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT V":
            act = Text("ACT V", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Loading up on plugins doesn\'t slow Claude down or confuse it":
            line1 = Text("Loading up on plugins doesn\'t slow Claude down or confuse it", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The rest stay installed and disabled, ready the moment a job":
            line2 = Text("The rest stay installed and disabled, ready the moment a job", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Loading up on plugins doesn\'t slow Claude down or confuse it":
            uline = Line(LEFT * min(4.0, len("Loading up on plugins doesn\'t slow Claude down or confuse it") * 0.18), RIGHT * min(4.0, len("Loading up on plugins doesn\'t slow Claude down or confuse it") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.40))
