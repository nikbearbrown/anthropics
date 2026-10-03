"""scenes.py — Memory, Skills, and Guardrails (Film 10). Manim visuals, house template."""
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080

INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def check_mark(pos, scale=0.35, color=GREEN):
    """Two-Line check mark (checker's stub has no Checkmark)."""
    l1 = Line(LEFT * 0.2 * scale, ORIGIN, color=color, stroke_width=int(8 * scale / 0.35))
    l2 = Line(ORIGIN, RIGHT * 0.45 * scale + UP * 0.45 * scale, color=color,
              stroke_width=int(8 * scale / 0.35))
    return VGroup(l1, l2).move_to(pos)


def cross_mark(pos, scale=0.35, color=ACCENT):
    """Two crossing Lines = X mark."""
    w = int(8 * scale / 0.35)
    l1 = Line(LEFT * 0.35 * scale + DOWN * 0.35 * scale,
              RIGHT * 0.35 * scale + UP * 0.35 * scale, color=color, stroke_width=w)
    l2 = Line(LEFT * 0.35 * scale + UP * 0.35 * scale,
              RIGHT * 0.35 * scale + DOWN * 0.35 * scale, color=color, stroke_width=w)
    return VGroup(l1, l2).move_to(pos)


def bullet(pos, color=ACCENT):
    return Dot(pos, radius=0.09, color=color)


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.3, width=9.5, height=3.2,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.4)
    grp = VGroup(plate, t)
    if sub:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.35)
        grp.add(s)
    return grp


def term_card(term, gloss, pos):
    plate = RoundedRectangle(corner_radius=0.18, width=5.2, height=1.7,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(term, font_size=36, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = Text(gloss, font_size=24, color=GREY).move_to(plate.get_center() + DOWN * 0.4)
    return VGroup(plate, t, g)


def file_card(label, pos, width=3.4, height=1.6):
    plate = RoundedRectangle(corner_radius=0.16, width=width, height=height,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3).move_to(pos)
    t = Text(label, font_size=38, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


def mini_card(label, pos, width=2.8, height=0.9):
    plate = RoundedRectangle(corner_radius=0.12, width=width, height=height,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(label, font_size=30, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("teach it once. it remembers.")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        mem = RoundedRectangle(corner_radius=0.2, width=2.6, height=1.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3).shift(LEFT * 2.2 + DOWN * 0.4)
        gl = VGroup(*[Line(LEFT * 0.8 + UP * (0.4 - 0.3 * k),
                           RIGHT * 0.8 + UP * (0.4 - 0.3 * k),
                           color=GREY, stroke_width=4) for k in range(3)]).move_to(mem.get_center())
        sess = Dot(RIGHT * 2.2 + DOWN * 0.4, radius=0.35, color=GREEN)
        self.play(FadeIn(mem), FadeIn(gl), FadeIn(sess))
        arrow = Arrow(mem.get_right(), sess.get_left(), color=INK, buff=0.2, stroke_width=6)
        self.play(Create(arrow))
        ring = Circle(radius=0.55, color=ACCENT, stroke_width=6).move_to(sess.get_center())
        self.play(Create(ring))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        cards = [
            ("Memory", "notes read every session", LEFT * 3.1 + UP * 0.9),
            ("Skill", "a bundle the agent calls", RIGHT * 3.1 + UP * 0.9),
            ("Approval mode", "who says yes", LEFT * 3.1 + DOWN * 1.1),
            ("MCP", "plugs to outside tools", RIGHT * 3.1 + DOWN * 1.1),
        ]
        for term, gloss, pos in cards:
            c = term_card(term, gloss, pos)
            d = bullet(pos + DOWN * 1.25, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Memory(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        fc = file_card("memory.md", LEFT * 3.8)
        self.play(FadeIn(fc, shift=RIGHT * 0.3))
        for i in range(3):
            dot = Dot(RIGHT * (0.6 + i * 1.7) + UP * 0.6, radius=0.3, color=GREEN)
            arrow = Arrow(fc[0].get_right() + UP * 0.6, dot.get_center(),
                          color=INK, buff=0.25, stroke_width=5)
            self.play(Create(arrow), FadeIn(dot, scale=0.5))
        self.wait(1.2)


class M04_B02Css(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        plate = RoundedRectangle(corner_radius=0.16, width=3.6, height=2.0,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).shift(LEFT * 3.6)
        t1 = Text("memory.md", font_size=36, color=INK).move_to(plate.get_center() + UP * 0.45)
        t2 = Text("the CSS rule", font_size=32, color=ACCENT).move_to(plate.get_center() + DOWN * 0.45)
        self.play(FadeIn(plate), Write(t1))
        self.play(Write(t2))
        arrow = Arrow(plate.get_right(), LEFT * 0.6, color=INK, buff=0.2, stroke_width=6)
        self.play(Create(arrow))
        out = RoundedRectangle(corner_radius=0.16, width=4.4, height=2.0,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3).shift(RIGHT * 2.6)
        gl = VGroup(*[Line(LEFT * 1.2 + UP * (0.5 - 0.4 * k),
                           RIGHT * 0.6 + UP * (0.5 - 0.4 * k),
                           color=GREY, stroke_width=5) for k in range(3)]).move_to(out.get_center() + LEFT * 0.4)
        self.play(FadeIn(out), FadeIn(gl))
        self.play(FadeIn(check_mark(out.get_center() + RIGHT * 1.5, scale=0.7)))
        self.wait(1.2)


class M05_B03Where(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        p1 = RoundedRectangle(corner_radius=0.18, width=4.4, height=2.2,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).shift(LEFT * 2.7 + UP * 0.2)
        t1a = Text("project", font_size=36, color=INK).move_to(p1.get_center() + UP * 0.5)
        t1b = Text("memory.md", font_size=34, color=GREY).move_to(p1.get_center() + DOWN * 0.45)
        self.play(FadeIn(p1), Write(t1a), Write(t1b))
        self.play(FadeIn(check_mark(p1.get_center() + DOWN * 1.55), scale=0.7))
        p2 = RoundedRectangle(corner_radius=0.18, width=4.4, height=2.2,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).shift(RIGHT * 2.7 + UP * 0.2)
        t2 = Text("global", font_size=36, color=INK).move_to(p2.get_center())
        d2 = bullet(p2.get_center() + DOWN * 1.55, color=BLUE)
        self.play(FadeIn(p2), Write(t2), FadeIn(d2))
        self.wait(1.2)


class M06_B04Skill(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        labels = ["name", "description", "steps"]
        y = 1.6
        stack = VGroup()
        for lab in labels:
            mc = mini_card(lab, LEFT * 3.4 + UP * y, width=3.2)
            d = bullet(LEFT * 5.4 + UP * y, color=BLUE)
            self.play(FadeIn(mc, shift=RIGHT * 0.3), FadeIn(d))
            stack.add(mc)
            y -= 1.5
        arrow = Arrow(LEFT * 1.4, RIGHT * 0.2, color=INK, buff=0.2, stroke_width=6)
        self.play(Create(arrow))
        belt = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).shift(RIGHT * 2.8)
        bt = Text("toolbelt", font_size=38, color=INK).move_to(belt.get_center() + UP * 1.15)
        self.play(FadeIn(belt), Write(bt))
        for i, lab in enumerate(labels):
            chip = mini_card(lab, RIGHT * 2.8 + UP * (0.45 - i * 1.0), width=2.6, height=0.8)
            self.play(FadeIn(chip, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.2)


class M07_B05Trigger(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        dc = mini_card("description", LEFT * 4.0, width=3.4)
        self.play(FadeIn(dc, shift=RIGHT * 0.3))
        bell = Circle(radius=0.6, color=ACCENT, stroke_width=6).move_to(LEFT * 0.4)
        bt = Text("trigger", font_size=28, color=INK).next_to(bell, DOWN, buff=0.25)
        self.play(Create(bell), Write(bt))
        for k in range(2):
            ring = Circle(radius=0.85 + k * 0.3, color=ACCENT, stroke_width=4).move_to(bell.get_center())
            self.play(Create(ring), run_time=0.4)
            self.play(FadeOut(ring), run_time=0.2)
        agent = Dot(RIGHT * 3.6, radius=0.4, color=BLUE)
        arrow = Arrow(bell.get_right(), agent.get_center(), color=INK, buff=0.3, stroke_width=6)
        self.play(FadeIn(agent, scale=0.5), Create(arrow))
        self.play(FadeIn(check_mark(agent.get_center() + UP * 0.85), scale=0.7))
        self.wait(1.2)


class M08_B06Plugin(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        frame = RoundedRectangle(corner_radius=0.25, width=6.4, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).shift(RIGHT * 1.4)
        ft = Text("plugin", font_size=40, color=INK).move_to(frame.get_center() + UP * 1.25)
        self.play(FadeIn(frame), Write(ft))
        for i in range(4):
            chip = mini_card("skill", LEFT * 6.3 + UP * (1.0 - i * 0.0), width=2.2, height=0.8)
            target = RIGHT * 1.4 + LEFT * (1.8 - (i % 2) * 3.2) + DOWN * (0.35 + (i // 2) * 1.1)
            self.play(FadeIn(chip, shift=RIGHT * 0.5))
            self.play(chip.animate.move_to(target), run_time=0.6)
        self.wait(1.2)


class M09_B07Approvals(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("approval modes", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        modes = ["on request", "untrusted", "never"]
        cols = [ACCENT, BLUE, GREEN]
        y = 1.5
        for m, col in zip(modes, cols):
            plate = RoundedRectangle(corner_radius=0.16, width=4.6, height=1.1,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2).move_to(UP * y)
            t = Text(m, font_size=36, color=INK).move_to(plate.get_center())
            d = bullet(LEFT * 2.9 + UP * y, color=col)
            self.play(FadeIn(plate), Write(t), FadeIn(d))
            y -= 1.7
        self.wait(1.2)


class M10_B08Sandbox(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        box = RoundedRectangle(corner_radius=0.25, width=5.2, height=3.4,
                               stroke_color=BLUE, stroke_width=8,
                               fill_opacity=0).shift(LEFT * 2.9 + DOWN * 0.2)
        bt = Text("sandbox", font_size=36, color=BLUE).next_to(box, UP, buff=0.2)
        term = RoundedRectangle(corner_radius=0.14, width=3.6, height=2.2,
                                fill_color=INK, fill_opacity=1,
                                stroke_width=0).move_to(box.get_center())
        gl = VGroup(*[Line(LEFT * 1.2 + UP * (0.55 - 0.4 * k),
                           RIGHT * 0.4 + UP * (0.55 - 0.4 * k),
                           color=GREY, stroke_width=5) for k in range(3)]).move_to(term.get_center())
        cur = Dot(term.get_left() + RIGHT * 0.35 + UP * 0.55, radius=0.09, color=GREEN)
        self.play(Create(box), Write(bt))
        self.play(FadeIn(term), FadeIn(gl), FadeIn(cur))
        yp = RoundedRectangle(corner_radius=0.18, width=4.2, height=2.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).shift(RIGHT * 3.4 + DOWN * 0.2)
        yt = Text("YOLO mode", font_size=38, color=INK).move_to(yp.get_center())
        self.play(FadeIn(yp), Write(yt))
        self.play(FadeIn(cross_mark(yp.get_center() + DOWN * 1.45), scale=0.8))
        self.wait(1.2)


class M11_B09Mcp(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("MCP", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        plug_body = RoundedRectangle(corner_radius=0.15, width=1.8, height=1.2,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=4).shift(LEFT * 2.6 + DOWN * 0.3)
        prong1 = Line(LEFT * 2.6 + RIGHT * 0.9 + UP * 0.05 + DOWN * 0.3,
                      LEFT * 2.6 + RIGHT * 1.7 + UP * 0.05 + DOWN * 0.3, color=INK, stroke_width=6)
        prong2 = Line(LEFT * 2.6 + RIGHT * 0.9 + DOWN * 0.35 + DOWN * 0.3,
                      LEFT * 2.6 + RIGHT * 1.7 + DOWN * 0.35 + DOWN * 0.3, color=INK, stroke_width=6)
        plug = VGroup(plug_body, prong1, prong2)
        socket = Circle(radius=0.9, color=INK, stroke_width=6).shift(RIGHT * 0.6 + DOWN * 0.3)
        self.play(FadeIn(plug, shift=RIGHT * 0.4), FadeIn(socket))
        self.play(plug.animate.shift(RIGHT * 1.6), run_time=1.0)
        for i in range(3):
            dot = Dot(socket.get_center() + RIGHT * (1.3 + i * 0.9) + UP * (0.5 - i * 0.5),
                      radius=0.28, color=BLUE)
            edge = Line(socket.get_center(), dot.get_center(), color=GREY, stroke_width=4)
            self.play(Create(edge), FadeIn(dot, scale=0.5), run_time=0.5)
        self.wait(1.2)


class M12_B10Duck(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        c1 = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.2,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).shift(LEFT * 2.9 + DOWN * 0.3)
        t1 = Text("MCP", font_size=40, color=INK).move_to(c1.get_center())
        self.play(FadeIn(c1), Write(t1))
        self.play(FadeIn(check_mark(c1.get_center() + DOWN * 1.5), scale=0.8))
        c2 = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.2,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).shift(RIGHT * 2.9 + DOWN * 0.3)
        t2 = Text("the source", font_size=36, color=INK).move_to(c2.get_center() + UP * 0.3)
        self.play(FadeIn(c2), Write(t2))
        drop = Circle(radius=0.28, color=GREY, fill_opacity=0.5, stroke_width=3).move_to(
            c2.get_center() + DOWN * 0.35)
        self.play(FadeIn(drop, scale=0.6))
        self.play(FadeIn(cross_mark(c2.get_center() + DOWN * 1.5), scale=0.8))
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: recap
        plate = RoundedRectangle(corner_radius=0.2, width=9.6, height=4.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3)
        head = Text("recap", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head), FadeIn(plate))
        recaps = ["project memory: teach it once",
                  "skills: the description is the trigger",
                  "guardrails: approval modes, sandbox, MCP"]
        y = 1.05
        recap_grp = VGroup()
        for r in recaps:
            d = bullet(LEFT * 4.2 + UP * y)
            t = Text(r, font_size=30, color=INK).next_to(d, RIGHT, buff=0.3)
            self.play(FadeIn(d), Write(t))
            recap_grp.add(d, t)
            y -= 1.3
        self.wait(0.8)
        self.play(FadeOut(plate), FadeOut(recap_grp), FadeOut(head))
        # Phase 2: your turn
        card = title_card("your turn", "one memory rule. one skill. watch it trigger.")
        self.play(FadeIn(card, shift=UP * 0.3))
        pencil = Line(LEFT * 0.5, RIGHT * 0.5, color=ACCENT, stroke_width=8).next_to(card, DOWN, buff=0.4)
        self.play(Create(pencil))
        self.wait(0.8)
        self.play(FadeOut(card), FadeOut(pencil))
        # Phase 3: outro
        outro = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(outro, shift=DOWN * 0.3))
        nxt = Text("Next film: Capstone - Ship a Full-Stack App", font_size=32, color=BLUE).next_to(
            outro, DOWN, buff=0.4)
        bar = Line(LEFT * 1.5, RIGHT * 1.5, color=BLUE, stroke_width=6).next_to(nxt, DOWN, buff=0.25)
        self.play(Write(nxt), Create(bar))
        self.wait(1.2)
