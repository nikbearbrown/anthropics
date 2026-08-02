import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', '')
except Exception:
    DUR = {}; TITLE = ''

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

# Build the ladder of rungs at equally spaced energies
def make_ladder(axis_x, n_rungs=5, spacing=1.1, bottom=-2.5):
    rung_ys = [bottom + i * spacing for i in range(n_rungs)]
    rungs = VGroup()
    for i, ry in enumerate(rung_ys):
        r = Line([axis_x - 0.4, ry, 0], [axis_x + 0.4, ry, 0], color=INK, stroke_width=5)
        lbl = ink_txt(f"n={i}", size=20)
        lbl.move_to([axis_x + 1.1, ry, 0])
        rungs.add(r, lbl)
    axis = Arrow([axis_x, bottom - 0.3, 0], [axis_x, bottom + n_rungs * spacing + 0.3, 0],
                 color=INK, stroke_width=3, buff=0)
    e_lbl = ink_txt("E", size=32)
    e_lbl.next_to(axis, UP, buff=0.1)
    return axis, e_lbl, rungs, rung_ys


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("Solve the Harmonic Oscillator\nWithout Solving It", size=50)
        title.move_to(ORIGIN)
        sub = terra_txt("Eₙ = (n + ½)ħω", size=38)
        sub.next_to(title, DOWN, buff=0.7)
        bear = ink_txt("Bear's Notes · Quantum Mechanics", size=26)
        bear.next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(bear), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class H01_ScaryMath(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        lbl = ink_txt("Faced with this\nmonstrous equation…", size=42)
        lbl.to_edge(LEFT, buff=0.8)
        eq = ink_txt("[-ħ²/2m · d²/dx² + ½mω²x²]ψ = Eψ", size=42)
        eq.move_to([1.5, 0.3, 0])
        terror = terra_txt("😱", size=60)
        terror = ink_txt("?!", size=80)
        terror.move_to([5.5, -0.5, 0])
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(FadeIn(eq), run_time=0.6)
        self.play(FadeIn(terror), run_time=0.4)
        self.wait(max(0.1, dur - 1.5))


class H02_ArrowsRelief(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("Just two arrows:\na† raises, a lowers.", size=42)
        lbl.to_edge(LEFT, buff=0.8)
        up_arrow = Arrow([2.0, -0.5, 0], [2.0, 1.5, 0], color=TERRA, buff=0, stroke_width=6)
        up_lbl = ink_txt("a†", size=40)
        up_lbl.next_to(up_arrow, RIGHT, buff=0.3)
        down_arrow = Arrow([4.5, 1.5, 0], [4.5, -0.5, 0], color=INK, buff=0, stroke_width=6)
        down_lbl = ink_txt("a", size=42)
        down_lbl.next_to(down_arrow, RIGHT, buff=0.3)
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(Create(up_arrow), FadeIn(up_lbl), run_time=0.5)
        self.play(Create(down_arrow), FadeIn(down_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


class A01_SingleRung(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        axis_x = 0.0
        axis = Arrow([axis_x, -3.0, 0], [axis_x, 3.5, 0], color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rung_y = -1.5
        rung = Line([axis_x - 0.5, rung_y, 0], [axis_x + 0.5, rung_y, 0],
                    color=INK, stroke_width=5)
        n0_lbl = ink_txt("n = 0", size=28)
        n0_lbl.move_to([axis_x + 1.4, rung_y, 0])
        dot = Dot([axis_x, rung_y, 0], radius=0.18, color=TERRA)
        e0_lbl = ink_txt("E₀ = ½ħω", size=30)
        e0_lbl.move_to([-2.5, rung_y, 0])
        self.play(Create(axis), FadeIn(e_lbl), run_time=0.5)
        self.play(Create(rung), FadeIn(n0_lbl), run_time=0.4)
        self.play(FadeIn(dot), FadeIn(e0_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.3))


class A02_RaiseOperator(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        axis_x = 0.0
        axis = Arrow([axis_x, -3.0, 0], [axis_x, 3.5, 0], color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rung0_y = -2.0
        rung1_y = rung0_y + 1.3
        rung0 = Line([axis_x - 0.5, rung0_y, 0], [axis_x + 0.5, rung0_y, 0], color=INK, stroke_width=5)
        rung1 = Line([axis_x - 0.5, rung1_y, 0], [axis_x + 0.5, rung1_y, 0], color=INK, stroke_width=5)
        lbl0 = ink_txt("n=0", size=22); lbl0.move_to([axis_x + 1.2, rung0_y, 0])
        lbl1 = ink_txt("n=1", size=22); lbl1.move_to([axis_x + 1.2, rung1_y, 0])
        dot = Dot([axis_x, rung0_y, 0], radius=0.18, color=TERRA)
        raise_arrow = Arrow([axis_x - 1.2, rung0_y + 0.1, 0],
                            [axis_x - 1.2, rung1_y - 0.1, 0],
                            color=INK, buff=0, stroke_width=5)
        raise_lbl = ink_txt("a†", size=32)
        raise_lbl.next_to(raise_arrow, LEFT, buff=0.2)
        self.add(axis, e_lbl, rung0, lbl0, dot)
        self.play(Create(rung1), FadeIn(lbl1), run_time=0.4)
        self.play(Create(raise_arrow), FadeIn(raise_lbl), run_time=0.5)
        new_dot = Dot([axis_x, rung1_y, 0], radius=0.18, color=TERRA)
        self.play(Transform(dot, new_dot), run_time=0.5)
        self.bring_to_front(dot)
        self.wait(max(0.1, dur - 1.4))


class A03_LowerOperator(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        axis_x = 0.0
        axis = Arrow([axis_x, -3.0, 0], [axis_x, 3.5, 0], color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rung0_y = -2.0; rung1_y = rung0_y + 1.3; rung2_y = rung1_y + 1.3
        rungs = VGroup()
        for ry, n in [(rung0_y, 0), (rung1_y, 1), (rung2_y, 2)]:
            r = Line([axis_x - 0.5, ry, 0], [axis_x + 0.5, ry, 0], color=INK, stroke_width=5)
            l = ink_txt(f"n={n}", size=22); l.move_to([axis_x + 1.2, ry, 0])
            rungs.add(r, l)
        dot = Dot([axis_x, rung2_y, 0], radius=0.18, color=TERRA)
        lower_arrow = Arrow([axis_x - 1.2, rung2_y - 0.1, 0],
                            [axis_x - 1.2, rung1_y + 0.1, 0],
                            color=INK, buff=0, stroke_width=5)
        lower_lbl = ink_txt("a", size=32)
        lower_lbl.next_to(lower_arrow, LEFT, buff=0.2)
        self.add(axis, e_lbl, rungs, dot)
        self.play(Create(lower_arrow), FadeIn(lower_lbl), run_time=0.5)
        new_dot = Dot([axis_x, rung1_y, 0], radius=0.18, color=TERRA)
        self.play(Transform(dot, new_dot), run_time=0.5)
        self.wait(max(0.1, dur - 1.0))


class A04_StepsToFloor(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        axis_x = 0.0
        axis = Arrow([axis_x, -3.5, 0], [axis_x, 3.5, 0], color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        base = -3.0
        spacing = 1.3
        n_rungs = 4
        rung_ys = [base + i * spacing for i in range(n_rungs)]
        rungs = VGroup()
        for i, ry in enumerate(rung_ys):
            r = Line([axis_x - 0.5, ry, 0], [axis_x + 0.5, ry, 0], color=INK, stroke_width=5)
            l = ink_txt(f"n={i}", size=20); l.move_to([axis_x + 1.2, ry, 0])
            rungs.add(r, l)
        dot = Dot([axis_x, rung_ys[3], 0], radius=0.18, color=TERRA)
        self.add(axis, e_lbl, rungs, dot)
        # Step down twice
        for target_y in [rung_ys[2], rung_ys[0]]:
            lower_arr = Arrow([axis_x - 1.2, dot.get_center()[1] - 0.1, 0],
                              [axis_x - 1.2, target_y + 0.1, 0],
                              color=INK, buff=0, stroke_width=4)
            a_lbl = ink_txt("a", size=28)
            a_lbl.next_to(lower_arr, LEFT, buff=0.2)
            self.play(Create(lower_arr), FadeIn(a_lbl), run_time=0.3)
            new_dot = Dot([axis_x, target_y, 0], radius=0.18, color=TERRA)
            self.play(Transform(dot, new_dot), run_time=0.4)
            self.remove(lower_arr, a_lbl)
        floor_lbl = ink_txt("ground state n=0", size=28)
        floor_lbl.move_to([-3.0, rung_ys[0], 0])
        self.play(FadeIn(floor_lbl), run_time=0.3)
        self.wait(max(0.1, dur - 1.0))


class A05_LowerAtFloor(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        axis_x = 0.0
        axis = Arrow([axis_x, -3.0, 0], [axis_x, 3.5, 0], color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rung0_y = -2.0
        rung0 = Line([axis_x - 0.5, rung0_y, 0], [axis_x + 0.5, rung0_y, 0], color=INK, stroke_width=5)
        n0_lbl = ink_txt("n=0", size=22); n0_lbl.move_to([axis_x + 1.2, rung0_y, 0])
        dot = Dot([axis_x, rung0_y, 0], radius=0.18, color=TERRA)
        lower_arrow = Arrow([axis_x - 1.2, rung0_y - 0.1, 0],
                            [axis_x - 1.2, rung0_y - 1.2, 0],
                            color=INK, buff=0, stroke_width=4)
        a_lbl = ink_txt("a", size=28)
        a_lbl.next_to(lower_arrow, LEFT, buff=0.2)
        x_mark = Cross(color=TERRA, stroke_width=6)
        x_mark.scale(0.5)
        x_mark.move_to([axis_x - 1.2, rung0_y - 1.4, 0])
        stop_lbl = ink_txt("a|0⟩ = 0\n(destroyed!)", size=28)
        stop_lbl.move_to([-3.5, rung0_y - 0.8, 0])
        self.add(axis, e_lbl, rung0, n0_lbl, dot)
        self.play(Create(lower_arrow), FadeIn(a_lbl), run_time=0.5)
        self.play(FadeIn(x_mark), run_time=0.3)
        self.play(FadeIn(stop_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.2))


class A06_BuildLadderUp(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        axis_x = -1.0
        base = -3.0; spacing = 1.1; n_rungs = 6
        axis = Arrow([axis_x, base - 0.3, 0], [axis_x, base + n_rungs * spacing + 0.3, 0],
                     color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rung0 = Line([axis_x - 0.4, base, 0], [axis_x + 0.4, base, 0], color=INK, stroke_width=5)
        lbl0 = ink_txt("n=0", size=20); lbl0.move_to([axis_x + 1.1, base, 0])
        dot = Dot([axis_x, base, 0], radius=0.18, color=TERRA)
        self.add(axis, e_lbl, rung0, lbl0, dot)
        for i in range(1, n_rungs):
            ry = base + i * spacing
            raise_arr = Arrow([axis_x - 1.0, base + (i-1)*spacing + 0.05, 0],
                              [axis_x - 1.0, ry - 0.05, 0],
                              color=INK, buff=0, stroke_width=4)
            a_lbl = ink_txt("a†", size=22)
            a_lbl.next_to(raise_arr, LEFT, buff=0.15)
            new_rung = Line([axis_x - 0.4, ry, 0], [axis_x + 0.4, ry, 0], color=INK, stroke_width=5)
            new_lbl = ink_txt(f"n={i}", size=20); new_lbl.move_to([axis_x + 1.1, ry, 0])
            new_dot = Dot([axis_x, ry, 0], radius=0.18, color=TERRA)
            self.play(Create(raise_arr), FadeIn(a_lbl), run_time=0.2)
            self.play(Create(new_rung), FadeIn(new_lbl), Transform(dot, new_dot), run_time=0.25)
            self.bring_to_front(dot)
            self.remove(raise_arr, a_lbl)
        self.wait(max(0.1, dur - 1.5))


class A07_EqualSpacing(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        axis_x = 0.0
        base = -3.0; spacing = 1.1; n_rungs = 6
        axis = Arrow([axis_x, base - 0.3, 0], [axis_x, base + n_rungs * spacing + 0.3, 0],
                     color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rungs = VGroup()
        rung_ys = []
        for i in range(n_rungs):
            ry = base + i * spacing
            rung_ys.append(ry)
            r = Line([axis_x - 0.4, ry, 0], [axis_x + 0.4, ry, 0], color=INK, stroke_width=5)
            l = ink_txt(f"n={i}", size=20); l.move_to([axis_x + 1.1, ry, 0])
            rungs.add(r, l)
        self.add(axis, e_lbl, rungs)
        braces = VGroup()
        for i in range(n_rungs - 1):
            y1, y2 = rung_ys[i], rung_ys[i+1]
            brace = Brace(Line([axis_x - 1.5, y1, 0], [axis_x - 1.5, y2, 0]),
                          direction=LEFT, color=TERRA)
            hw = ink_txt("ħω", size=18)
            hw.next_to(brace, LEFT, buff=0.1)
            braces.add(brace, hw)
        self.play(Create(braces), run_time=0.8)
        note = ink_txt("all gaps equal ħω", size=28)
        note.move_to([3.0, 0, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.1, dur - 1.2))


class A08_WholeSpectrum(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        axis_x = -2.5
        base = -3.0; spacing = 1.1; n_rungs = 6
        axis = Arrow([axis_x, base - 0.3, 0], [axis_x, base + n_rungs * spacing + 0.3, 0],
                     color=INK, stroke_width=3, buff=0)
        e_lbl = ink_txt("E", size=32)
        e_lbl.next_to(axis, UP, buff=0.1)
        rungs = VGroup()
        for i in range(n_rungs):
            ry = base + i * spacing
            r = Line([axis_x - 0.4, ry, 0], [axis_x + 0.4, ry, 0], color=INK, stroke_width=5)
            l = ink_txt(f"(n+½)ħω" if i == 0 else f"n={i}", size=18 if i == 0 else 20)
            l.move_to([axis_x + 1.5, ry, 0])
            rungs.add(r, l)
        self.add(axis, e_lbl, rungs)
        label = ink_txt("the whole spectrum,\nno equation solved", size=42)
        label.move_to([2.0, 0, 0])
        underline = Line(label.get_left() + DOWN * 0.1,
                         label.get_right() + DOWN * 0.1,
                         color=TERRA, stroke_width=3)
        self.play(Write(label), run_time=0.9)
        self.play(Create(underline), run_time=0.3)
        self.wait(max(0.1, dur - 1.2))
