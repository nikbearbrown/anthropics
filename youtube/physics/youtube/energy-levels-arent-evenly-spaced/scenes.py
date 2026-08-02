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


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("Why Quantum Energy Levels\nAren't Evenly Spaced", size=52)
        title.move_to(ORIGIN)
        bear = terra_txt("Bear's Notes · Quantum Mechanics", size=28)
        bear.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(title), run_time=0.8)
        self.play(FadeIn(bear), run_time=0.5)
        self.wait(max(0.1, dur - 1.3))


class H01_ClassicalLadder(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        label = ink_txt("Classical expectation:\nevenly spaced rungs", size=36)
        label.to_edge(LEFT, buff=1.0)
        # Draw evenly-spaced ladder
        rung_x_left = 1.5
        rung_x_right = 5.5
        rung_ys = [-3.0, -1.5, 0.0, 1.5, 3.0]
        rungs = VGroup()
        for y in rung_ys:
            r = Line([rung_x_left, y, 0], [rung_x_right, y, 0], color=INK, stroke_width=5)
            rungs.add(r)
        side_l = Line([rung_x_left, -3.0, 0], [rung_x_left, 3.0, 0], color=INK, stroke_width=3)
        side_r = Line([rung_x_right, -3.0, 0], [rung_x_right, 3.0, 0], color=INK, stroke_width=3)
        gap_labels = VGroup()
        for i in range(len(rung_ys) - 1):
            mid_y = (rung_ys[i] + rung_ys[i+1]) / 2
            gl = terra_txt("1", size=24)
            gl.move_to([rung_x_right + 0.5, mid_y, 0])
            gap_labels.add(gl)
        self.play(FadeIn(label), Create(side_l), Create(side_r), run_time=0.6)
        self.play(Create(rungs), run_time=0.8)
        self.play(FadeIn(gap_labels), run_time=0.4)
        self.wait(max(0.1, dur - 1.8))


class H02_QuantumLadder(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        label = ink_txt("Quantum reality:\nrungs widen toward top", size=36)
        label.to_edge(LEFT, buff=1.0)
        rung_x_left = 1.5
        rung_x_right = 5.5
        # Positions at n²: n=1→1, 2→4, 3→9, 4→16; scaled to fit screen
        ns = [1, 2, 3, 4]
        scale = 0.35
        offset = -3.2
        rung_ys = [n*n * scale + offset for n in ns]
        rungs = VGroup()
        for y in rung_ys:
            r = Line([rung_x_left, y, 0], [rung_x_right, y, 0], color=INK, stroke_width=5)
            rungs.add(r)
        side_l = Line([rung_x_left, rung_ys[0], 0], [rung_x_left, rung_ys[-1], 0], color=INK, stroke_width=3)
        side_r = Line([rung_x_right, rung_ys[0], 0], [rung_x_right, rung_ys[-1], 0], color=INK, stroke_width=3)
        gap_vals = [3, 5, 7]
        gap_labels = VGroup()
        for i in range(len(rung_ys) - 1):
            mid_y = (rung_ys[i] + rung_ys[i+1]) / 2
            gl = terra_txt(str(gap_vals[i]), size=24)
            gl.move_to([rung_x_right + 0.5, mid_y, 0])
            gap_labels.add(gl)
        self.play(FadeIn(label), Create(side_l), Create(side_r), run_time=0.6)
        self.play(Create(rungs), run_time=0.6)
        self.play(FadeIn(gap_labels), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class A01_BoxAndAxis(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        # Box on left
        box = Rectangle(width=2.4, height=3.2, color=INK, stroke_width=4)
        box.set_fill(color=CREAM, opacity=1)
        box.move_to([-3.5, -0.3, 0])
        box_label = ink_txt("particle\nin a box", size=26)
        box_label.next_to(box, DOWN, buff=0.3)
        # Energy axis on right
        axis_x = 2.5
        axis_bottom = -2.0
        axis_top = 3.5
        energy_axis = Arrow([axis_x, axis_bottom, 0], [axis_x, axis_top, 0],
                            color=INK, stroke_width=3, buff=0)
        e_label = ink_txt("E", size=36)
        e_label.next_to(energy_axis, UP, buff=0.1)
        n_label = ink_txt("n", size=28)
        n_label.move_to([axis_x - 0.5, axis_top - 0.3, 0])
        self.play(Create(box), run_time=0.5)
        self.play(FadeIn(box_label), run_time=0.3)
        self.play(Create(energy_axis), FadeIn(e_label), run_time=0.6)
        self.play(FadeIn(n_label), run_time=0.3)
        self.wait(max(0.1, dur - 1.7))


class A02_WaveN1(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        # Box on left
        box = Rectangle(width=2.4, height=3.2, color=INK, stroke_width=4)
        box.set_fill(color=CREAM, opacity=1)
        box.move_to([-3.5, -0.3, 0])
        box_label = ink_txt("n = 1", size=28)
        box_label.next_to(box, DOWN, buff=0.3)
        # n=1 wave: one hump
        box_left = -4.7
        box_right = -2.3
        box_bottom = -1.9
        box_top = 1.3
        def wave1(x):
            t = (x - box_left) / (box_right - box_left)
            return np.sin(np.pi * t) * 0.8
        pts = []
        for i in range(60):
            x = box_left + (box_right - box_left) * i / 59
            y = box_bottom + (box_top - box_bottom) / 2 + wave1(x)
            pts.append([x, y, 0])
        wave = VMobject(color=TERRA, stroke_width=4)
        wave.set_points_smoothly(pts)
        # Energy axis on right
        axis_x = 2.5
        axis_bottom = -2.0
        axis_top = 3.5
        energy_axis = Arrow([axis_x, axis_bottom, 0], [axis_x, axis_top, 0],
                            color=INK, stroke_width=3, buff=0)
        e_label = ink_txt("E", size=36)
        e_label.next_to(energy_axis, UP, buff=0.1)
        # Rung at E=1 (n=1)
        scale = 0.35; offset = -2.0
        rung_y = 1 * scale + offset
        rung = Line([axis_x - 0.3, rung_y, 0], [axis_x + 0.3, rung_y, 0],
                    color=INK, stroke_width=5)
        rung_label = ink_txt("E₁", size=28)
        rung_label.move_to([axis_x + 0.7, rung_y, 0])
        self.add(box, energy_axis, e_label)
        self.play(FadeIn(box_label), run_time=0.3)
        self.play(Create(wave), run_time=0.7)
        self.play(Create(rung), FadeIn(rung_label), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


class A03_WaveN2(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        box = Rectangle(width=2.4, height=3.2, color=INK, stroke_width=4)
        box.set_fill(color=CREAM, opacity=1)
        box.move_to([-3.5, -0.3, 0])
        box_label = ink_txt("n = 2", size=28)
        box_label.next_to(box, DOWN, buff=0.3)
        box_left = -4.7; box_right = -2.3; box_bottom = -1.9; box_top = 1.3
        # n=2 wave: two humps
        def wave2(x):
            t = (x - box_left) / (box_right - box_left)
            return np.sin(2 * np.pi * t) * 0.65
        pts = []
        for i in range(80):
            x = box_left + (box_right - box_left) * i / 79
            y = box_bottom + (box_top - box_bottom) / 2 + wave2(x)
            pts.append([x, y, 0])
        wave = VMobject(color=TERRA, stroke_width=4)
        wave.set_points_smoothly(pts)
        axis_x = 2.5; axis_bottom = -2.0; axis_top = 3.5
        energy_axis = Arrow([axis_x, axis_bottom, 0], [axis_x, axis_top, 0],
                            color=INK, stroke_width=3, buff=0)
        e_label = ink_txt("E", size=36)
        e_label.next_to(energy_axis, UP, buff=0.1)
        scale = 0.35; offset = -2.0
        # n=1 rung (grey reference)
        r1_y = 1 * scale + offset
        r1 = Line([axis_x - 0.3, r1_y, 0], [axis_x + 0.3, r1_y, 0], color=INK, stroke_width=3)
        r1_lbl = ink_txt("E₁", size=22)
        r1_lbl.move_to([axis_x + 0.7, r1_y, 0])
        # n=2 rung at E=4
        r2_y = 4 * scale + offset
        r2 = Line([axis_x - 0.3, r2_y, 0], [axis_x + 0.3, r2_y, 0], color=TERRA, stroke_width=5)
        r2_lbl = terra_txt("4E₁", size=28)
        r2_lbl.move_to([axis_x + 0.8, r2_y, 0])
        self.add(box, energy_axis, e_label, r1, r1_lbl)
        self.play(FadeIn(box_label), run_time=0.3)
        self.play(Create(wave), run_time=0.8)
        self.play(Create(r2), FadeIn(r2_lbl), run_time=0.6)
        self.wait(max(0.1, dur - 1.7))


class A04_WavesN3N4(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        box = Rectangle(width=2.4, height=3.2, color=INK, stroke_width=4)
        box.set_fill(color=CREAM, opacity=1)
        box.move_to([-3.5, -0.3, 0])
        box_left = -4.7; box_right = -2.3; box_mid_y = -0.3
        axis_x = 2.5; axis_bottom = -2.0; axis_top = 3.5
        energy_axis = Arrow([axis_x, axis_bottom, 0], [axis_x, axis_top, 0],
                            color=INK, stroke_width=3, buff=0)
        e_label = ink_txt("E", size=36)
        e_label.next_to(energy_axis, UP, buff=0.1)
        scale = 0.35; offset = -2.0
        # existing rungs
        rungs_data = [(1, "E₁"), (4, "4E₁")]
        prev_rungs = VGroup()
        for en, lbl in rungs_data:
            ry = en * scale + offset
            r = Line([axis_x - 0.3, ry, 0], [axis_x + 0.3, ry, 0], color=INK, stroke_width=3)
            rl = ink_txt(lbl, size=20)
            rl.move_to([axis_x + 0.8, ry, 0])
            prev_rungs.add(r, rl)
        self.add(box, energy_axis, e_label, prev_rungs)
        # n=3 wave
        n = 3
        pts3 = []
        for i in range(90):
            x = box_left + (box_right - box_left) * i / 89
            t = (x - box_left) / (box_right - box_left)
            y = box_mid_y + np.sin(n * np.pi * t) * 0.55
            pts3.append([x, y, 0])
        wave3 = VMobject(color=TERRA, stroke_width=3)
        wave3.set_points_smoothly(pts3)
        n3_lbl = ink_txt("n=3", size=22)
        n3_lbl.move_to([-3.5, box_mid_y - 1.2, 0])
        r3_y = 9 * scale + offset
        r3 = Line([axis_x - 0.3, r3_y, 0], [axis_x + 0.3, r3_y, 0], color=TERRA, stroke_width=5)
        r3_lbl = terra_txt("9E₁", size=26)
        r3_lbl.move_to([axis_x + 0.8, r3_y, 0])
        self.play(Create(wave3), FadeIn(n3_lbl), run_time=0.6)
        self.play(Create(r3), FadeIn(r3_lbl), run_time=0.4)
        # n=4 wave
        n = 4
        pts4 = []
        for i in range(100):
            x = box_left + (box_right - box_left) * i / 99
            t = (x - box_left) / (box_right - box_left)
            y = box_mid_y + np.sin(n * np.pi * t) * 0.45
            pts4.append([x, y, 0])
        wave4 = VMobject(color=INK, stroke_width=3)
        wave4.set_points_smoothly(pts4)
        n4_lbl = ink_txt("n=4", size=22)
        n4_lbl.move_to([-3.5, box_mid_y + 1.0, 0])
        r4_y = 16 * scale + offset
        r4 = Line([axis_x - 0.3, r4_y, 0], [axis_x + 0.3, r4_y, 0], color=INK, stroke_width=5)
        r4_lbl = ink_txt("16E₁", size=24)
        r4_lbl.move_to([axis_x + 0.85, r4_y, 0])
        self.play(Create(wave4), FadeIn(n4_lbl), run_time=0.6)
        self.play(Create(r4), FadeIn(r4_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 2.0))


class A05_WideningGaps(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        axis_x = 0.5; axis_bottom = -3.5; axis_top = 3.5
        energy_axis = Arrow([axis_x, axis_bottom, 0], [axis_x, axis_top, 0],
                            color=INK, stroke_width=3, buff=0)
        e_label = ink_txt("E", size=36)
        e_label.next_to(energy_axis, UP, buff=0.1)
        scale = 0.35; offset = -3.0
        ns = [1, 4, 9, 16]
        n_labels = ["E₁", "4E₁", "9E₁", "16E₁"]
        rungs = VGroup()
        rung_ys = []
        for en, lbl in zip(ns, n_labels):
            ry = en * scale + offset
            rung_ys.append(ry)
            r = Line([axis_x - 0.3, ry, 0], [axis_x + 0.3, ry, 0], color=INK, stroke_width=5)
            rl = ink_txt(lbl, size=22)
            rl.move_to([axis_x + 0.9, ry, 0])
            rungs.add(r, rl)
        self.add(energy_axis, e_label, rungs)
        # Bracket gaps
        gap_vals = [3, 5, 7]
        gap_labels_group = VGroup()
        braces = VGroup()
        for i in range(len(rung_ys) - 1):
            y1, y2 = rung_ys[i], rung_ys[i + 1]
            mid_y = (y1 + y2) / 2
            bx = axis_x - 0.8
            brace = Brace(Line([bx, y1, 0], [bx, y2, 0]), direction=LEFT, color=TERRA)
            gl = terra_txt(f"ΔE = {gap_vals[i]}E₁", size=24)
            gl.next_to(brace, LEFT, buff=0.15)
            braces.add(brace)
            gap_labels_group.add(gl)
        self.play(Create(braces), run_time=0.8)
        self.play(FadeIn(gap_labels_group), run_time=0.5)
        note = ink_txt("gaps widen: 3, 5, 7…", size=30)
        note.to_edge(RIGHT, buff=1.0)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.1, dur - 1.7))


class A06_WavelengthShrinks(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        title = ink_txt("Wavelength λₙ = 2L/n shrinks with n", size=34)
        title.to_edge(UP, buff=0.6)
        self.add(title)
        box_left = -6.0; box_right = -3.0; L = box_right - box_left
        ys = [2.0, 0.3, -1.4]
        ns = [1, 2, 3]
        colors = [INK, TERRA, INK]
        for n, y, c in zip(ns, ys, colors):
            pts = []
            for i in range(100):
                x = box_left + L * i / 99
                t = i / 99
                yv = y + np.sin(n * np.pi * t) * 0.5
                pts.append([x, yv, 0])
            wave = VMobject(color=c, stroke_width=3)
            wave.set_points_smoothly(pts)
            box_line = Line([box_left, y - 0.7, 0], [box_left, y + 0.7, 0], color=INK, stroke_width=3)
            box_rline = Line([box_right, y - 0.7, 0], [box_right, y + 0.7, 0], color=INK, stroke_width=3)
            wlabel = ink_txt(f"n={n},  λ={'' if n==1 else str(int(round(2*3/n,0)))+'/3 '}2L/{n}", size=22)
            wlabel.move_to([box_left + L/2, y - 0.85, 0])
            self.add(wave, box_line, box_rline, wlabel)
        arrow = Arrow([-2.5, 2.5, 0], [-2.5, -1.5, 0], color=TERRA, buff=0)
        shrink_lbl = terra_txt("λ shrinks", size=28)
        shrink_lbl.next_to(arrow, RIGHT, buff=0.2)
        self.play(Create(arrow), FadeIn(shrink_lbl), run_time=0.6)
        self.wait(max(0.1, dur - 0.6))


class A07_NSquaredRelationship(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        title = ink_txt("The n → n² relationship", size=40)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.5)
        # Table of n vs n²
        headers = VGroup(
            ink_txt("n", size=36),
            ink_txt("Eₙ / E₁", size=36),
        )
        headers[0].move_to([-1.5, 1.5, 0])
        headers[1].move_to([1.5, 1.5, 0])
        self.play(FadeIn(headers), run_time=0.4)
        rows = [(1, 1), (2, 4), (3, 9), (4, 16)]
        row_groups = VGroup()
        for i, (n, nsq) in enumerate(rows):
            y = 0.5 - i * 1.0
            nl = ink_txt(str(n), size=32)
            nl.move_to([-1.5, y, 0])
            nsql = terra_txt(str(nsq), size=32)
            nsql.move_to([1.5, y, 0])
            arrow = Arrow([-0.9, y, 0], [0.8, y, 0], color=TERRA, buff=0, stroke_width=2)
            row_groups.add(nl, nsql, arrow)
            self.play(FadeIn(nl), Create(arrow), FadeIn(nsql), run_time=0.3)
        formula = terra_txt("Eₙ = n² · E₁", size=38)
        formula.move_to([0, -2.5, 0])
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(max(0.1, dur - 2.2))


class A08_EnergyGrowsN2(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        # Full ladder with TERRA label
        axis_x = -1.0; axis_bottom = -3.2; axis_top = 3.5
        energy_axis = Arrow([axis_x, axis_bottom, 0], [axis_x, axis_top, 0],
                            color=INK, stroke_width=3, buff=0)
        e_label = ink_txt("E", size=36)
        e_label.next_to(energy_axis, UP, buff=0.1)
        scale = 0.35; offset = -3.0
        ns = [1, 4, 9, 16]
        n_labels = ["1", "4", "9", "16"]
        rungs = VGroup()
        rung_ys = []
        for en, lbl in zip(ns, n_labels):
            ry = en * scale + offset
            rung_ys.append(ry)
            r = Line([axis_x - 0.3, ry, 0], [axis_x + 0.3, ry, 0], color=INK, stroke_width=5)
            rl = ink_txt(lbl + "E₁", size=22)
            rl.move_to([axis_x + 0.85, ry, 0])
            rungs.add(r, rl)
        self.add(energy_axis, e_label, rungs)
        # Big red/terra label
        label = terra_txt("energy grows as n²", size=48)
        label.move_to([1.5, -0.5, 0])
        underline = Line(label.get_left() + DOWN * 0.1,
                         label.get_right() + DOWN * 0.1,
                         color=TERRA, stroke_width=3)
        self.play(Write(label), run_time=0.8)
        self.play(Create(underline), run_time=0.3)
        self.wait(max(0.1, dur - 1.1))
