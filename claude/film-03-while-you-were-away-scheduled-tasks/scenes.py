"""scenes.py — While You Were Away: Scheduled Tasks (Film 3 of the Claude at Work series).
14 Manim scenes, M01–M14. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat. Paper background set in EVERY construct."""
from manim import *
import numpy as np
config.pixel_width = 1920
config.pixel_height = 1080
INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"
GOLD = "#E8B93C"


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.25, width=11.5, height=2.6,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = VGroup(plate, t)
    if sub is not None:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.3)
        g.add(s)
    return g


def bullet(pos, color=ACCENT, r=0.12):
    return Dot(point=[pos[0], pos[1], 0], radius=r, color=color)


def check_mark(pos, scale=1.0, color=GREEN):
    return VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4, color=color, stroke_width=10),
    ).scale(scale).move_to(pos)


def labeled_box(label, pos, w=3.4, h=1.6, box_color=INK, label_size=36):
    box = Rectangle(width=w, height=h, stroke_color=box_color, stroke_width=4,
                    fill_color=CARD, fill_opacity=1).move_to(pos)
    lab = Text(label, font_size=label_size, color=INK).move_to(box.get_center())
    return VGroup(box, lab)


def clock_face(pos, r=1.1, color=ACCENT):
    face = Circle(radius=r, color=color, stroke_width=6).move_to(pos)
    hour = Line(pos, pos + np.array([r * 0.45, r * 0.25, 0]), color=color, stroke_width=8)
    minute = Line(pos, pos + np.array([r * 0.1, r * 0.75, 0]), color=color, stroke_width=6)
    return VGroup(face, hour, minute)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        plate = RoundedRectangle(corner_radius=0.3, width=12.4, height=6.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        hook = Text("while you were away?", font_size=56, color=INK)
        hook2 = Text("the task ran itself", font_size=56, color=ACCENT)
        hook.move_to([0, 2.2, 0])
        hook2.next_to(hook, DOWN, buff=0.25)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=GREY, stroke_width=4).move_to([0, 1.0, 0])
        self.play(Write(hook), Create(rule))
        self.play(Write(hook2))
        clk = clock_face([-4.2, -1.4, 0], r=1.15)
        self.play(Create(clk))
        rows = ["check the drive", "group by client", "save the digest"]
        for i, ln in enumerate(rows):
            y = -0.6 - i * 0.85
            cm = check_mark([0.6, y, 0], scale=0.6)
            t = Text(ln, font_size=28, color=INK).move_to([1.3, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("Three terms", font_size=48, color=INK).to_edge(UP, buff=0.7)
        head_rule = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
        head_rule.next_to(head, DOWN, buff=0.25)
        self.play(Write(head), Create(head_rule))
        terms = [
            ("scheduled task", "runs on a clock, not your say-so", ACCENT),
            ("cadence", "hourly · daily · weekdays · manual", BLUE),
            ("run", "one execution — a fresh session", GREEN),
        ]
        xs = [-4.0, 0.0, 4.0]
        for i, (term, gloss, color) in enumerate(terms):
            x = xs[i]
            card = RoundedRectangle(corner_radius=0.2, width=3.7, height=2.6,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=4).move_to([x, -0.4, 0])
            dot = bullet([x - 1.45, 0.45, 0], color=color)
            t = Text(term, font_size=28, color=INK).move_to([x + 0.1, 0.45, 0])
            g = Text(gloss, font_size=19, color=GREY).move_to([x, -0.85, 0])
            self.play(FadeIn(card), FadeIn(dot), Write(t), Write(g))
        self.wait(1.2)


class M03_B01(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        left = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.6,
                                fill_color="#E4E1D8", fill_opacity=1,
                                stroke_color=GREY, stroke_width=3).move_to([-3.2, 0.4, 0])
        lt = Text("steer it live", font_size=34, color=GREY).move_to([-3.2, 0.4, 0])
        lsub = Text("(film two)", font_size=26, color=GREY).move_to([-3.2, -0.5, 0])
        self.play(FadeIn(left), Write(lt), Write(lsub))
        right = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=4).move_to([3.2, 0.4, 0])
        rt = Text("runs on a clock", font_size=34, color=ACCENT).move_to([3.2, 1.4, 0])
        self.play(FadeIn(right), Write(rt))
        clk = clock_face([3.2, -0.3, 0], r=0.85)
        self.play(Create(clk))
        cap = Text("the clock does the managing", font_size=34, color=INK).move_to([0, -2.6, 0])
        cdot = bullet([-3.3, -2.6, 0], color=ACCENT)
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M04_B02(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("one sentence of intent", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rows = [
            "check the drive",
            "note who changed what",
            "summarize what's new",
            "group by client",
            "save to daily updates",
        ]
        for i, ln in enumerate(rows):
            y = 1.2 - i * 0.95
            cm = check_mark([-4.4, y, 0], scale=0.65)
            t = Text(ln, font_size=30, color=INK).move_to([-3.7, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        foot = Text("the whole job, in one sentence", font_size=32, color=ACCENT).move_to([0, -2.7, 0])
        fdot = bullet([-3.9, -2.7, 0], color=ACCENT)
        self.play(FadeIn(fdot), Write(foot))
        self.wait(1.2)


class M05_B03(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.25, width=8.8, height=2.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to([0, 1.8, 0])
        lab = Text("draft — you review", font_size=40, color=INK).move_to(card.get_center())
        self.play(FadeIn(card), Write(lab))
        chips = ["hourly", "daily", "weekdays", "manual"]
        xs = [-4.2, -1.4, 1.4, 4.2]
        for i, ch in enumerate(chips):
            chip = RoundedRectangle(corner_radius=0.35, width=2.4, height=1.0,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=BLUE, stroke_width=3).move_to([xs[i], -0.2, 0])
            t = Text(ch, font_size=28, color=INK).move_to(chip.get_center())
            self.play(Create(chip), Write(t))
        tick = check_mark([0, -1.8, 0], scale=1.0)
        acc = Text("accept", font_size=34, color=GREEN).move_to([1.4, -1.8, 0])
        self.play(Create(tick[0]), Create(tick[1]), Write(acc))
        cap = Text("cadence is a dial, not a contract", font_size=32, color=INK).move_to([0, -2.9, 0])
        cdot = bullet([-4.4, -2.9, 0])
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M06_B04(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        bar = RoundedRectangle(corner_radius=0.15, width=2.6, height=5.8,
                               fill_color="#E4E1D8", fill_opacity=1,
                               stroke_color=INK, stroke_width=3).move_to([-4.8, 0, 0])
        self.play(FadeIn(bar))
        sched = Text("Scheduled", font_size=30, color=CARD).move_to([-4.8, 1.8, 0])
        sched_bg = RoundedRectangle(corner_radius=0.15, width=2.3, height=0.8,
                                    fill_color=ACCENT, fill_opacity=1,
                                    stroke_color=ACCENT, stroke_width=2).move_to([-4.8, 1.8, 0])
        self.play(FadeIn(sched_bg), Write(sched))
        row = RoundedRectangle(corner_radius=0.2, width=6.8, height=1.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3).move_to([1.0, 0.6, 0])
        rt = Text("drive digest · hourly", font_size=30, color=INK).move_to([1.0, 1.0, 0])
        rn = Text("next run: top of the hour", font_size=24, color=GREY).move_to([1.0, 0.2, 0])
        self.play(FadeIn(row), Write(rt), Write(rn))
        lab = Text("mission control", font_size=36, color=ACCENT).move_to([1.0, -1.8, 0])
        ldot = bullet([-1.6, -1.8, 0], color=ACCENT)
        self.play(FadeIn(ldot), Write(lab))
        self.wait(1.2)


class M07_B05(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        for i, (name, x) in enumerate([("run one", -3.2), ("run two", 3.2)]):
            card = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.4,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=GREEN, stroke_width=4).move_to([x, 0.6, 0])
            t = Text(name, font_size=34, color=INK).move_to([x, 1.4, 0])
            stamp = RoundedRectangle(corner_radius=0.3, width=3.4, height=0.9,
                                     fill_color=GREEN, fill_opacity=1,
                                     stroke_color=GREEN, stroke_width=2).move_to([x, 0.0, 0])
            st = Text("fresh context", font_size=24, color=CARD).move_to(stamp.get_center())
            self.play(FadeIn(card), Write(t))
            self.play(FadeIn(stamp), Write(st))
        files = []
        for x in [-1.2, 0.0, 1.2]:
            f = Rectangle(width=0.9, height=1.2, stroke_color=GREY, stroke_width=3,
                          fill_color="#E4E1D8", fill_opacity=1).move_to([x, -2.0, 0])
            files.append(f)
            self.play(FadeIn(f))
        self.play(*[f.animate.set_fill(CARD, opacity=1) for f in files], run_time=0.8)
        cap = Text("the latest state of your files", font_size=32, color=INK).move_to([0, -3.0, 0])
        cdot = bullet([-3.6, -3.0, 0], color=GREEN)
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M08_B06(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.2, width=7.6, height=1.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to([0, 2.0, 0])
        t = Text("awake + app open", font_size=36, color=INK).move_to([-0.6, 2.0, 0])
        tick = check_mark([2.8, 2.0, 0], scale=0.9)
        self.play(FadeIn(card), Write(t), Create(tick[0]), Create(tick[1]))
        line = Line([-5.5, -0.4, 0], [5.5, -0.4, 0], color=GREY, stroke_width=4)
        self.play(Create(line))
        miss = Dot(point=[-3.4, -0.4, 0], radius=0.28, color=GREY)
        m_lab = Text("missed", font_size=28, color=GREY).move_to([-3.4, -1.3, 0])
        self.play(FadeIn(miss), Write(m_lab))
        back = Text("you're back", font_size=28, color=INK).move_to([0.2, -1.3, 0])
        self.play(Write(back))
        run = Dot(point=[3.4, -0.4, 0], radius=0.32, color=ACCENT)
        r_lab = Text("runs now", font_size=28, color=ACCENT).move_to([3.4, -1.3, 0])
        tag = RoundedRectangle(corner_radius=0.3, width=2.0, height=0.8,
                               fill_color=ACCENT, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=2).move_to([3.4, -2.3, 0])
        tag_t = Text("delayed", font_size=24, color=CARD).move_to(tag.get_center())
        self.play(FadeIn(run), Write(r_lab))
        self.play(FadeIn(tag), Write(tag_t))
        cap = Text("nothing is lost", font_size=34, color=INK).move_to([0.6, -2.9, 0])
        cdot = bullet([-3.4, -2.9, 0], color=ACCENT)
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M09_B07(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("you stay in charge", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rows = [
            "review past runs",
            "edit instructions",
            "change cadence",
            "run now — don't wait for the clock",
        ]
        for i, ln in enumerate(rows):
            y = 1.1 - i * 1.1
            card = RoundedRectangle(corner_radius=0.2, width=8.6, height=0.9,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=BLUE, stroke_width=3).move_to([0, y, 0])
            t = Text(ln, font_size=30, color=INK).move_to(card.get_center())
            d = bullet([-3.9, y, 0], color=BLUE)
            self.play(FadeIn(card), FadeIn(d), Write(t))
        foot = Text("choosing when you exercise control", font_size=32, color=INK).move_to([0, -2.8, 0])
        fdot = bullet([-4.2, -2.8, 0], color=BLUE)
        self.play(FadeIn(fdot), Write(foot))
        self.wait(1.2)


class M10_B08(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.25, width=7.8, height=4.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to([-1.6, 0.4, 0])
        head = Text("toolbox", font_size=40, color=INK).move_to([-1.6, 1.9, 0])
        self.play(FadeIn(card), Write(head))
        chips = ["calendar", "drive", "Slack"]
        for i, ch in enumerate(chips):
            y = 0.9 - i * 1.05
            chip = RoundedRectangle(corner_radius=0.35, width=4.2, height=0.85,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=GREEN, stroke_width=3).move_to([-1.6, y, 0])
            t = Text(ch, font_size=28, color=INK).move_to(chip.get_center())
            self.play(Create(chip), Write(t))
        clk = clock_face([4.6, 0.4, 0], r=1.2)
        self.play(Create(clk))
        cap = Text("the clock doesn't shrink the toolbox", font_size=32, color=INK).move_to([0, -2.7, 0])
        cdot = bullet([-4.6, -2.7, 0], color=GREEN)
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M11_B09(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        folder = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.8,
                                  fill_color="#E8B93C", fill_opacity=0.35,
                                  stroke_color=INK, stroke_width=4).move_to([-3.6, 0.2, 0])
        fl = Text("daily updates", font_size=32, color=INK).move_to([-3.6, 1.5, 0])
        self.play(FadeIn(folder), Write(fl))
        doc = RoundedRectangle(corner_radius=0.15, width=5.6, height=3.8,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=4).move_to([2.6, 0.2, 0])
        self.play(FadeIn(doc))
        clients = ["client A — 3 changes", "client B — 1 change", "client C — 5 changes"]
        for i, ln in enumerate(clients):
            y = 1.1 - i * 1.0
            cm = check_mark([0.6, y, 0], scale=0.6)
            t = Text(ln, font_size=26, color=INK).move_to([1.3, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        cap = Text("the whole film in one folder", font_size=34, color=INK).move_to([0, -2.7, 0])
        cdot = bullet([-3.9, -2.7, 0], color=ACCENT)
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M12_B10(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        left = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=4).move_to([-3.2, 0.6, 0])
        lt = Text("clock work", font_size=36, color=GREEN).move_to([-3.2, 1.7, 0])
        lg = Text("recurring, same steps", font_size=24, color=GREY).move_to([-3.2, 0.9, 0])
        tick = check_mark([-3.2, -0.3, 0], scale=1.0)
        self.play(FadeIn(left), Write(lt), Write(lg))
        self.play(Create(tick[0]), Create(tick[1]))
        right = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=4).move_to([3.2, 0.6, 0])
        rt = Text("steering work", font_size=36, color=ACCENT).move_to([3.2, 1.7, 0])
        rg = Text("needs your judgment", font_size=24, color=GREY).move_to([3.2, 0.9, 0])
        steer = Arrow([-4.4 + 6.4, -0.3, 0], [-3.6 + 6.4, -0.3, 0], color=ACCENT, stroke_width=8)
        self.play(FadeIn(right), Write(rt), Write(rg))
        self.play(GrowArrow(steer))
        cap = Text("clock work versus steering work", font_size=34, color=INK).move_to([0, -2.4, 0])
        cdot = bullet([-4.1, -2.4, 0])
        self.play(FadeIn(cdot), Write(cap))
        self.wait(1.2)


class M13_B11(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("Claude at Work", font_size=48, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        dots = []
        for i in range(10):
            x = -5.4 + i * 1.2
            color = ACCENT if i == 2 else GREY
            d = Dot(point=[x, 0.6, 0], radius=0.3, color=color)
            dots.append(d)
            self.play(FadeIn(d))
        three = Text("3", font_size=30, color=CARD).move_to(dots[2].get_center())
        self.play(Write(three))
        titles = ["Tag Claude In", "The Verification Loop", "A Year of Claude Code"]
        for i, t in enumerate(titles):
            lab = Text(t, font_size=24, color=GREY).move_to([-5.4 + (i + 3) * 1.2, -0.5, 0])
            self.play(Write(lab))
        nxt = Text("Next: Tag Claude In \u2014 the team channel", font_size=34, color=ACCENT).move_to([0, -1.9, 0])
        ndot = bullet([-5.0, -1.9, 0], color=ACCENT)
        self.play(FadeIn(ndot), Write(nxt))
        self.wait(1.2)


class M14_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # --- recap: four lines ---
        plate = RoundedRectangle(corner_radius=0.25, width=12.2, height=6.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        recap_lines = [
            "a scheduled task runs on a clock",
            "each run is a fresh session on today's files",
            "missed runs catch up when you're back",
            "review, edit, or run on demand",
        ]
        recap_mobs = []
        for i, ln in enumerate(recap_lines):
            y = 1.9 - i * 1.15
            d = bullet([-5.5, y, 0])
            t = Text(ln, font_size=28, color=INK).move_to([-4.9, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            recap_mobs.extend([d, t])
            self.play(FadeIn(d), Write(t))
        # --- your turn ---
        self.play(*[FadeOut(m) for m in recap_mobs], FadeOut(plate))
        yt_card = RoundedRectangle(corner_radius=0.25, width=11.6, height=4.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=ACCENT, stroke_width=4).move_to(ORIGIN)
        yt_head = Text("Your turn.", font_size=48, color=ACCENT).move_to([0, 1.5, 0])
        self.play(FadeIn(yt_card), Write(yt_head))
        steps = [
            "Pick one recurring chore. Write the one sentence.",
            "Clock work or steering work?",
        ]
        step_mobs = []
        for i, s in enumerate(steps):
            y = 0.3 - i * 1.0
            cm = check_mark([-5.0, y, 0], scale=0.8)
            t = Text(s, font_size=30, color=INK).move_to([-4.2, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            step_mobs.extend([cm, t])
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        # --- outro ---
        self.play(*[FadeOut(m) for m in step_mobs], FadeOut(yt_card), FadeOut(yt_head))
        out = title_card("While You Were Away", "@NikBearBrown")
        self.play(FadeIn(out[0]), Write(out[1]), Write(out[2]))
        nxt = Text("Next: Tag Claude In", font_size=36, color=GREY).move_to([0, -2.6, 0])
        ndot = bullet([-2.4, -2.6, 0], color=ACCENT)
        self.play(FadeIn(ndot), Write(nxt))
        self.wait(1.2)
