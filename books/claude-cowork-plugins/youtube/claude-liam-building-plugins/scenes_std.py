from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 24


class Scene_B01_ClaudeLiamBuilding(Scene):
    """Beat B01 — SHOW: bar/proportion chart. Narration: The official catalog covers the functions most businesses share — marketing, sal"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT  I":
            act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison: generic catalog coverage vs your specific workflow
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars
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

        lbl1 = Text("Generic functions", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Your workflow", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("No off-the-shelf plugin knows your specific workflow.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 12.50))


class Scene_B12_ClaudeLiamBuilding(Scene):
    """Beat B12 — SHOW: bar/proportion chart. Narration: Here\'s the part that sounds technical and isn\'t. You don\'t write code. You don\'t"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT  III":
            act = Text("ACT  III", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison: perceived complexity vs actual ease (no-code)
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Bar1 = perceived complexity (short); Bar2 = actual ease (tall, favored)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 30)
        pt2 = ax.c2p(2, 70)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Seems technical", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Plain language", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("No code, no config — a conversation builds the plugin.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.40))


class Scene_B02_ClaudeLiamBuilding(Scene):
    """Beat B02 — transfer: process in head lifts out into encoded package. (15.2s)"""
    def construct(self):
        self.camera.background_color = BG
        # Head circle (left) with scattered dots → clean package (right)
        head = Circle(radius=1.2, color=INK, stroke_width=3).shift(LEFT * 3.2)
        pkg  = RoundedRectangle(corner_radius=0.2, width=2.4, height=1.6,
                                color=INK, stroke_width=3).shift(RIGHT * 3.2)
        lbl_head = Text("Process", font=FONT, font_size=36, color=INK).next_to(head, DOWN, 0.2)
        lbl_pkg  = Text("Plugin", font=FONT, font_size=36, color=INK).next_to(pkg, DOWN, 0.2)

        self.play(Create(head), Write(lbl_head), run_time=0.5)

        dots = VGroup(*[Dot(point=head.get_center() + np.array([
            np.random.uniform(-0.7, 0.7), np.random.uniform(-0.6, 0.6), 0]), radius=0.08,
            color=INK) for _ in range(8)])
        self.play(FadeIn(dots), run_time=0.4)

        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=4)
        self.play(GrowArrow(arrow), run_time=0.5)

        ordered = VGroup(*[Dot(point=pkg.get_center() + np.array([
            (-0.5 + i * 0.33), 0.3 - (i // 3) * 0.35, 0]), radius=0.08, color=TERRA)
            for i in range(6)])
        self.play(Create(pkg), Write(lbl_pkg), run_time=0.5)
        self.play(Transform(dots, ordered), run_time=0.8)

        caption = Text("The process, transferred.", font=FONT, font_size=28, color=INK)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 11.60))


class Scene_B05_ClaudeLiamBuilding(Scene):
    """Beat B05 — converge: scattered results → one tight aligned column. (13.4s)"""
    def construct(self):
        self.camera.background_color = BG
        np.random.seed(7)
        n = 8
        scatter = VGroup(*[Dot(point=np.array([
            np.random.uniform(-4.5, 4.5), np.random.uniform(-2.5, 2.5), 0]),
            radius=0.12, color=INK) for _ in range(n)])
        self.play(FadeIn(scatter), run_time=0.5)

        target = VGroup(*[Dot(point=np.array([0.0, -1.4 + i * 0.42, 0]),
                              radius=0.12, color=TERRA) for i in range(n)])
        bar = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=3).shift(LEFT * 0.6)
        lbl = Text("One standard", font=FONT, font_size=26, color=INK).shift(RIGHT * 2.0)

        self.play(Transform(scatter, target), run_time=1.0)
        self.play(Create(bar), Write(lbl), run_time=0.5)

        caption = Text("Scatter to converge.", font=FONT, font_size=36, color=INK)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 10.50))


class Scene_B11_ClaudeLiamBuilding(Scene):
    """Beat B11 — branch/fan-out: one ask → three workers → one result. (14.1s)"""
    def construct(self):
        self.camera.background_color = BG
        src  = RoundedRectangle(corner_radius=0.2, width=2.0, height=0.9,
                                color=INK, fill_color=INK, fill_opacity=0.12, stroke_width=2)
        src.shift(LEFT * 4.0)
        src_lbl = Text("Your ask", font=FONT, font_size=24, color=INK).move_to(src)

        workers_data = ["Folders", "Email", "Tracker"]
        workers = VGroup(*[
            RoundedRectangle(corner_radius=0.2, width=2.0, height=0.8,
                             color=INK, fill_color=INK, fill_opacity=0.10, stroke_width=2
                             ).shift(np.array([0.0, (1 - i) * 1.3, 0]))
            for i in range(3)])
        worker_lbls = VGroup(*[
            Text(workers_data[i], font=FONT, font_size=22, color=INK).move_to(workers[i])
            for i in range(3)])

        out = RoundedRectangle(corner_radius=0.2, width=2.2, height=0.9,
                               color=INK, fill_color=INK, fill_opacity=0.12, stroke_width=2)
        out.shift(RIGHT * 4.0)
        out_lbl = Text("One result", font=FONT, font_size=24, color=INK).move_to(out)

        self.play(Create(src), Write(src_lbl), run_time=0.4)
        fan_arrows = VGroup(*[Arrow(src.get_right(), w.get_left(),
                                   color=INK, stroke_width=2, buff=0.1) for w in workers])
        self.play(GrowArrow(fan_arrows[0]), GrowArrow(fan_arrows[1]),
                  GrowArrow(fan_arrows[2]), run_time=0.5)
        self.play(Create(workers), Write(worker_lbls), run_time=0.5)

        merge = VGroup(*[Arrow(w.get_right(), out.get_left(),
                               color=TERRA, stroke_width=2, buff=0.1) for w in workers])
        self.play(Create(out), Write(out_lbl), run_time=0.4)
        self.play(*[GrowArrow(a) for a in merge], run_time=0.5)

        caption = Text("Many steps, one result.", font=FONT, font_size=28, color=INK)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 10.40))


class Scene_B14_ClaudeLiamBuilding(Scene):
    """Beat B14 — accumulate: Describe → Answer → Refine → Use tiles stack. (12.8s)"""
    def construct(self):
        self.camera.background_color = BG
        steps = ["Describe", "Answer", "Refine", "Use"]
        tiles = VGroup()
        for i, s in enumerate(steps):
            lbl = Text(s, font=FONT, font_size=40, color=INK)
            lbl.move_to(UP * (1.5 - i * 1.1))
            tiles.add(lbl)
        accent = Line(LEFT * 0.7, RIGHT * 0.7, color=TERRA, stroke_width=3)
        accent.next_to(tiles[-1], DOWN, buff=0.12)

        caption = Text("Four passes.", font=FONT, font_size=28, color=INK)
        caption.to_edge(DOWN, buff=0.5)

        for tile in tiles:
            self.play(FadeIn(tile, shift=RIGHT * 0.3), run_time=0.45)
        self.play(Create(accent), run_time=0.25)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 9.80))


class Scene_B16_ClaudeLiamBuilding(Scene):
    """Beat B16 — compress: one-hour bar shrinks; minutes bar stands. (15.5s)"""
    def construct(self):
        self.camera.background_color = BG
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": INK, "stroke_width": 2}, tips=False)
        ax.shift(DOWN * 0.4)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt_tall = ax.c2p(1, 90)
        pt_short = ax.c2p(2, 20)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt_tall[1] - origin[1]),
                         color=INK, fill_color=INK, fill_opacity=0.85, stroke_width=0)
        bar1.move_to([(pt_tall[0] + origin[0]) / 2 + bar_w / 2,
                      (pt_tall[1] + origin[1]) / 2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt_short[1] - origin[1]),
                         color=TERRA, fill_color=TERRA, fill_opacity=0.85, stroke_width=0)
        bar2.move_to([(pt_short[0] + origin[0]) / 2 + bar_w / 2,
                      (pt_short[1] + origin[1]) / 2, 0])

        lbl1 = Text("By hand", font=FONT, font_size=22, color=INK)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("One command", font=FONT, font_size=22, color=INK)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.5)

        caption = Text("Hours to minutes.", font=FONT, font_size=36, color=INK)
        caption.to_edge(DOWN, buff=0.4)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 12.50))


class Scene_B19_ClaudeLiamBuilding(Scene):
    """Beat B19 — replicate: one 'you' tile expands into a row of identical runs. (12.8s)"""
    def construct(self):
        self.camera.background_color = BG
        def make_tile(label, color=INK):
            box = RoundedRectangle(corner_radius=0.18, width=1.6, height=1.0,
                                   color=color, fill_color=color, fill_opacity=0.12,
                                   stroke_width=2)
            txt = Text(label, font=FONT, font_size=24, color=INK)
            return VGroup(box, txt).arrange(ORIGIN)

        origin_tile = make_tile("you", INK).shift(LEFT * 3.5)
        self.play(FadeIn(origin_tile), run_time=0.4)

        copies = VGroup(*[make_tile("you", TERRA).shift(np.array([
            -0.8 + i * 1.8, 0, 0])) for i in range(4)])
        copies.shift(RIGHT * 0.4)

        self.play(Transform(origin_tile.copy(), copies[0]), run_time=0.4)
        for i in range(1, 4):
            self.play(FadeIn(copies[i], shift=RIGHT * 0.3), run_time=0.3)

        caption = Text("Clone the routine.", font=FONT, font_size=28, color=INK)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 9.80))


class Scene_B20_ClaudeLiamBuilding(Scene):
    """Beat B20 — divergence: work splits into automate and keep-judgment paths. (13.1s)"""
    def construct(self):
        self.camera.background_color = BG
        src_lbl = Text("Your work", font=FONT, font_size=32, color=INK)
        src_lbl.move_to(LEFT * 3.5)
        auto_lbl = Text("Automate", font=FONT, font_size=32, color=INK)
        auto_lbl.move_to(RIGHT * 2.5 + UP * 1.0)
        keep_lbl = Text("Keep judgment", font=FONT, font_size=32, color=INK)
        keep_lbl.move_to(RIGHT * 2.5 + DOWN * 1.0)

        fork = np.array([-1.3, 0.0, 0])
        conn = Line(np.array([-2.4, 0.0, 0]), fork, color=INK, stroke_width=3)
        a1 = Arrow(fork, np.array([1.1, 1.0, 0]), color=TERRA, stroke_width=3, buff=0)
        a2 = Arrow(fork, np.array([1.1, -1.0, 0]), color=INK, stroke_width=3, buff=0)

        caption = Text("Automate scaffolding.", font=FONT, font_size=36, color=INK)
        caption.to_edge(DOWN, buff=0.5)

        self.play(Write(src_lbl), run_time=0.4)
        self.play(Create(conn), run_time=0.3)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.5)
        self.play(Write(auto_lbl), run_time=0.4)
        self.play(Write(keep_lbl), run_time=0.4)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 10.10))


class Scene_B24_ClaudeLiamBuilding(Scene):
    """Beat B24 — accumulate/evolve: plugin gains refinements over timeline. (11.7s)"""
    def construct(self):
        self.camera.background_color = BG
        versions = ["v1", "+ fix", "+ refine", "sharper"]
        colors = [INK, INK, INK, TERRA]
        boxes = VGroup()
        for i, (v, c) in enumerate(zip(versions, colors)):
            box = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.0,
                                   color=c, fill_color=c, fill_opacity=0.10, stroke_width=2)
            lbl = Text(v, font=FONT, font_size=28, color=c)
            grp = VGroup(box, lbl).arrange(ORIGIN)
            grp.move_to(np.array([-3.3 + i * 2.2, 0.5, 0]))
            boxes.add(grp)

        arrow = Line(LEFT * 3.8, RIGHT * 3.8, color=INK, stroke_width=2).shift(DOWN * 0.5)
        arr_tip = Arrow(LEFT * 3.8, RIGHT * 3.8, color=INK, stroke_width=2).shift(DOWN * 0.5)
        self.play(GrowArrow(arr_tip), run_time=0.4)

        for b in boxes:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.35)

        caption = Text("A living document.", font=FONT, font_size=28, color=INK)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 8.60))


class Scene_B07_ClaudeLiamBuilding(Scene):
    """Beat B07 — folder tree: a plugin as a directory of plain text files. (15.0s)"""
    def construct(self):
        self.camera.background_color = BG

        title = Text("A plugin is a folder.", font=FONT, font_size=34, color=INK)
        title.to_edge(UP, buff=0.6)

        tree_labels = [
            ("client-onboarding/", True),
            ("  SKILL.md", False),
            ("  skills/", False),
            ("  commands/", False),
            ("  connectors/", False),
            ("  subagents/", False),
        ]
        tree_group = VGroup()
        for label, bold in tree_labels:
            w = BOLD if bold else NORMAL
            sz = 30 if bold else 26
            t = Text(label, font=FONT, font_size=sz, color=INK, weight=w)
            tree_group.add(t)
        tree_group.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        tree_group.move_to(np.array([0.0, -0.3, 0]))

        caption = Text("Plain text. Easy to share, easy to change.", font=FONT, font_size=24, color=INK)
        caption.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=0.5)
        for item in tree_group:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.28)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 12.4))


class Scene_B09_ClaudeLiamBuilding(Scene):
    """Beat B09 — slash commands: two triggers that fire the plugin. (11.5s)"""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Commands are shortcuts.", font=FONT, font_size=34, color=INK)
        title.shift(UP * 2.2)

        accent = Line(LEFT * 3.5, RIGHT * 3.5, color=TERRA, stroke_width=3)
        accent.next_to(title, DOWN, buff=0.25)

        cmd1 = Text("/new-proposal", font=FONT, font_size=42, color=INK, weight=BOLD)
        cmd1.shift(UP * 0.6)
        sub1 = Text("runs your full proposal workflow", font=FONT, font_size=22, color=INK)
        sub1.next_to(cmd1, DOWN, buff=0.15)

        cmd2 = Text("/client-onboard", font=FONT, font_size=42, color=INK, weight=BOLD)
        cmd2.shift(DOWN * 1.1)
        sub2 = Text("kicks off your onboarding sequence", font=FONT, font_size=22, color=INK)
        sub2.next_to(cmd2, DOWN, buff=0.15)

        caption = Text("One slash, one job.", font=FONT, font_size=28, color=INK)
        caption.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=0.5)
        self.play(Create(accent), run_time=0.3)
        self.play(FadeIn(cmd1), run_time=0.4)
        self.play(FadeIn(sub1, shift=RIGHT * 0.15), run_time=0.3)
        self.play(FadeIn(cmd2), run_time=0.4)
        self.play(FadeIn(sub2, shift=RIGHT * 0.15), run_time=0.3)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 8.9))
