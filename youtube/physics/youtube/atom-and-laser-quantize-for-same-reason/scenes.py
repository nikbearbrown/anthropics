"""scenes.py — atom-and-laser-quantize-for-same-reason
Bears Notes 12-beat version (no worked numbers).
Beats with render=manim: INTRO, H01, H02, A01–A08.
OUTRO has render=none (skip).
"""
import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
ACCENT = "#5A5653"
RED    = "#C0392B"
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

# ── Geometry ──────────────────────────────────────────────────────────────────
WALL_H = 3.2
WALL_X_L = -4.2
WALL_X_R =  4.2
WAVE_Y = -0.3

def make_walls(color=INK):
    wl = Line([WALL_X_L, WAVE_Y - WALL_H / 2, 0], [WALL_X_L, WAVE_Y + WALL_H / 2, 0],
              color=color, stroke_width=7)
    wr = Line([WALL_X_R, WAVE_Y - WALL_H / 2, 0], [WALL_X_R, WAVE_Y + WALL_H / 2, 0],
              color=color, stroke_width=7)
    return VGroup(wl, wr)

def standing_wave(n=1, amplitude=0.9, color=ACCENT):
    L = WALL_X_R - WALL_X_L
    xs = np.linspace(WALL_X_L, WALL_X_R, 400)
    ys = amplitude * np.sin(n * np.pi * (xs - WALL_X_L) / L)
    pts = [[x, WAVE_Y + y, 0] for x, y in zip(xs, ys)]
    return VMobject(color=color, stroke_width=3.5).set_points_smoothly(pts)

def mismatched_wave(amplitude=0.8, color=RED):
    L = WALL_X_R - WALL_X_L
    xs = np.linspace(WALL_X_L, WALL_X_R, 400)
    k = 1.35 * np.pi / L   # non-integer → doesn't vanish at walls
    ys = amplitude * np.sin(k * (xs - WALL_X_L) + 0.35)
    pts = [[x, WAVE_Y + y, 0] for x, y in zip(xs, ys)]
    return VMobject(color=color, stroke_width=3.5).set_points_smoothly(pts)


# ══════════════════════════════════════════════════════════════════════════════

class INTRO_TitleCard(Scene):
    def construct(self):
        self.add(bg())
        series = ink_txt("Bear's Notes", size=32).move_to([0, 2.5, 0])
        title = ink_txt(
            "Why an Atom and a Laser Cavity\nQuantize for the Same Reason",
            size=40, line_spacing=1.3
        ).move_to([0, 0.5, 0])
        wave = standing_wave(n=3, amplitude=0.4, color=ACCENT).move_to([0, -2.0, 0])
        self.play(Write(series), run_time=0.6)
        self.play(Write(title), run_time=d("INTRO", 4.78) * 0.65)
        self.play(Create(wave), run_time=d("INTRO", 4.78) * 0.25)
        self.wait(d("INTRO", 4.78) * 0.1)


class H01_LaserAndAtom(Scene):
    """Laser emits exact colors; atom holds exact energies."""
    def construct(self):
        self.add(bg())
        laser_lbl = ink_txt("laser → exact colours", size=34).move_to([-3.5, 1.5, 0])
        atom_lbl = ink_txt("atom → exact energies", size=34).move_to([3.5, 1.5, 0])
        # Spectral lines as vertical bars
        colours = ["#e74c3c", "#27ae60", "#2980b9", "#8e44ad", "#f39c12"]
        laser_lines = VGroup(*[
            Line([-5.5 + 0.8 * i, 0.0, 0], [-5.5 + 0.8 * i, -1.2, 0],
                 color=c, stroke_width=6)
            for i, c in enumerate(colours)
        ])
        # Energy rungs for atom
        atom_rungs = VGroup(*[
            Line([2.5, -0.5 + 0.55 * i, 0], [4.5, -0.5 + 0.55 * i, 0],
                 color=ACCENT, stroke_width=5)
            for i in range(4)
        ])
        arrow_l = ink_txt("?", size=56, color=RED).move_to([0, 0.0, 0])
        self.play(Write(laser_lbl), Write(atom_lbl), run_time=0.7)
        self.play(Create(laser_lines), Create(atom_rungs), run_time=d("H01", 5.89) * 0.6)
        self.play(Write(arrow_l), run_time=0.5)
        self.wait(d("H01", 5.89) * 0.1)


class H02_SameFact(Scene):
    """The laser and atom are the same fact."""
    def construct(self):
        self.add(bg())
        laser_lbl = ink_txt("laser", size=38).move_to([-3.5, 0.5, 0])
        atom_lbl = ink_txt("atom", size=38).move_to([3.5, 0.5, 0])
        eq = ink_txt("=", size=72, color=ACCENT).move_to([0, 0.5, 0])
        why = ink_txt("both are really the same fact", size=32
                      ).move_to([0, -1.2, 0])
        self.play(Write(laser_lbl), Write(eq), Write(atom_lbl), Write(why),
                  run_time=d("H02", 3.61) * 0.9)
        self.wait(d("H02", 3.61) * 0.1)


class A01_TwoWalls(Scene):
    """Trap a wave between two walls."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        prompt = ink_txt("Trap a wave between two walls.", size=34).move_to([0, 2.8, 0])
        baseline = Line([WALL_X_L, WAVE_Y, 0], [WALL_X_R, WAVE_Y, 0],
                        color=INK, stroke_width=1.5, stroke_opacity=0.4)
        self.play(Write(prompt), run_time=0.5)
        self.play(Create(walls), Create(baseline), run_time=d("A01", 2.65) * 0.85)
        self.wait(d("A01", 2.65) * 0.15)


class A02_MismatchedWave(Scene):
    """Pick a random wavelength — it doesn't vanish at the walls."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        baseline = Line([WALL_X_L, WAVE_Y, 0], [WALL_X_R, WAVE_Y, 0],
                        color=INK, stroke_width=1.5, stroke_opacity=0.4)
        self.add(walls, baseline)
        bad = mismatched_wave()
        # Non-zero endpoints — estimate from parametric wave
        y_l = 0.8 * np.sin(0.35)
        y_r = 0.8 * np.sin(1.35 * np.pi + 0.35)
        dot_l = Dot([WALL_X_L, WAVE_Y + y_l, 0], radius=0.12, color=RED)
        dot_r = Dot([WALL_X_R, WAVE_Y + y_r, 0], radius=0.12, color=RED)
        lbl = ink_txt("doesn't reach zero", size=28, color=RED).move_to([0, -2.0, 0])
        self.play(Create(bad), FadeIn(dot_l), FadeIn(dot_r), Write(lbl),
                  run_time=d("A02", 3.8) * 0.85)
        self.wait(d("A02", 3.8) * 0.15)


class A03_WaveCancels(Scene):
    """The reflected copy is out of phase — they cancel to nothing."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        baseline = Line([WALL_X_L, WAVE_Y, 0], [WALL_X_R, WAVE_Y, 0],
                        color=INK, stroke_width=1.5, stroke_opacity=0.4)
        bad = mismatched_wave()
        y_l = 0.8 * np.sin(0.35)
        y_r = 0.8 * np.sin(1.35 * np.pi + 0.35)
        dot_l = Dot([WALL_X_L, WAVE_Y + y_l, 0], radius=0.12, color=RED)
        dot_r = Dot([WALL_X_R, WAVE_Y + y_r, 0], radius=0.12, color=RED)
        self.add(walls, baseline, bad, dot_l, dot_r)
        # Reflected copy
        L = WALL_X_R - WALL_X_L
        xs = np.linspace(WALL_X_L, WALL_X_R, 400)
        k = 1.35 * np.pi / L
        ys_neg = -0.8 * np.sin(k * (xs - WALL_X_L) + 0.35)
        refl_pts = [[x, WAVE_Y + y, 0] for x, y in zip(xs, ys_neg)]
        reflected = VMobject(color=RED, stroke_width=2, stroke_opacity=0.5
                             ).set_points_smoothly(refl_pts)
        flat = Line([WALL_X_L, WAVE_Y, 0], [WALL_X_R, WAVE_Y, 0],
                    color=INK, stroke_width=3)
        cancel_lbl = ink_txt("cancels", size=34, color=RED).move_to([0, -2.0, 0])
        self.play(Create(reflected), run_time=0.6)
        self.play(Transform(bad, flat), Transform(reflected, flat.copy()),
                  FadeOut(dot_l), FadeOut(dot_r),
                  Write(cancel_lbl), run_time=d("A03", 4.52) * 0.8)
        self.wait(d("A03", 4.52) * 0.1)


class A04_FittedWave(Scene):
    """Only a wave that vanishes at both walls survives."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        baseline = Line([WALL_X_L, WAVE_Y, 0], [WALL_X_R, WAVE_Y, 0],
                        color=INK, stroke_width=1.5, stroke_opacity=0.4)
        self.add(walls, baseline)
        good = standing_wave(n=1, amplitude=1.0, color=ACCENT)
        zero_l = Dot([WALL_X_L, WAVE_Y, 0], radius=0.12, color=ACCENT)
        zero_r = Dot([WALL_X_R, WAVE_Y, 0], radius=0.12, color=ACCENT)
        lbl = ink_txt("zero at both walls — it survives", size=30, color=ACCENT
                      ).move_to([0, -2.0, 0])
        self.play(Create(good), FadeIn(zero_l), FadeIn(zero_r), Write(lbl),
                  run_time=d("A04", 3.67) * 0.85)
        self.wait(d("A04", 3.67) * 0.15)


class A05_Reinforces(Scene):
    """Every round trip lands in step — reinforcing into a stable standing wave."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        baseline = Line([WALL_X_L, WAVE_Y, 0], [WALL_X_R, WAVE_Y, 0],
                        color=INK, stroke_width=1.5, stroke_opacity=0.4)
        self.add(walls, baseline)
        wave = standing_wave(n=1, amplitude=0.6, color=ACCENT)
        self.add(wave)
        reinforces_lbl = ink_txt("reinforces", size=32, color=ACCENT).move_to([0, -2.0, 0])
        wave_big = standing_wave(n=1, amplitude=1.1, color=ACCENT)
        wave_settle = standing_wave(n=1, amplitude=0.9, color=ACCENT)
        self.play(Transform(wave, wave_big), run_time=d("A05", 5.29) * 0.3)
        self.play(Transform(wave, wave_settle), Write(reinforces_lbl),
                  run_time=d("A05", 5.29) * 0.5)
        self.wait(d("A05", 5.29) * 0.15)


class A06_ModeLadder(Scene):
    """A discrete set of waves fits: n=1,2,3,…"""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        offsets = [-1.8, 0.3, 2.4]
        n_vals = [1, 2, 3]
        waves = VGroup()
        dashed_lvls = VGroup()
        labels = VGroup()
        for n, y_off in zip(n_vals, offsets):
            w = standing_wave(n=n, amplitude=0.55, color=ACCENT)
            w.shift([0, y_off - WAVE_Y, 0])
            dashes = DashedLine([WALL_X_L - 0.3, y_off, 0], [WALL_X_R + 0.3, y_off, 0],
                                 color=INK, stroke_width=1, stroke_opacity=0.4)
            lbl = ink_txt(f"n = {n}", size=26).move_to([WALL_X_R + 0.9, y_off, 0])
            waves.add(w); dashed_lvls.add(dashes); labels.add(lbl)
        self.play(FadeIn(walls), FadeIn(dashed_lvls), run_time=0.5)
        self.play(LaggedStartMap(FadeIn, waves, lag_ratio=0.3),
                  LaggedStartMap(FadeIn, labels, lag_ratio=0.3),
                  run_time=d("A06", 4.44) * 0.85)
        self.wait(d("A06", 4.44) * 0.15)


class A07_AtomVsLaserTag(Scene):
    """Same ladder tagged 'ATOM: energies' and 'LASER: colors'."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        offsets = [-1.8, 0.3, 2.4]; n_vals = [1, 2, 3]
        waves = VGroup(); dashed_lvls = VGroup(); labels = VGroup()
        for n, y_off in zip(n_vals, offsets):
            w = standing_wave(n=n, amplitude=0.55, color=ACCENT)
            w.shift([0, y_off - WAVE_Y, 0])
            dashes = DashedLine([WALL_X_L - 0.3, y_off, 0], [WALL_X_R + 0.3, y_off, 0],
                                 color=INK, stroke_width=1, stroke_opacity=0.4)
            lbl = ink_txt(f"n = {n}", size=26).move_to([WALL_X_R + 0.9, y_off, 0])
            waves.add(w); dashed_lvls.add(dashes); labels.add(lbl)
        self.add(walls, waves, dashed_lvls, labels)
        atom_tag = ink_txt("ATOM: energies", size=28, color=ACCENT
                           ).move_to([WALL_X_L - 1.2, 0.3, 0]).rotate(PI / 2)
        laser_tag = ink_txt("LASER: colours", size=28, color=TERRA
                            ).move_to([WALL_X_R + 1.8, 0.3, 0]).rotate(-PI / 2)
        self.play(FadeIn(atom_tag), FadeIn(laser_tag), run_time=d("A07", 6.19) * 0.85)
        self.wait(d("A07", 6.19) * 0.15)


class A08_OnlyWhatFits(Scene):
    """Same fact, twice: only the waves that fit are allowed to exist."""
    def construct(self):
        self.add(bg())
        walls = make_walls()
        offsets = [-1.8, 0.3, 2.4]; n_vals = [1, 2, 3]
        waves = VGroup(); dashed_lvls = VGroup(); labels = VGroup()
        for n, y_off in zip(n_vals, offsets):
            w = standing_wave(n=n, amplitude=0.55, color=ACCENT)
            w.shift([0, y_off - WAVE_Y, 0])
            dashes = DashedLine([WALL_X_L - 0.3, y_off, 0], [WALL_X_R + 0.3, y_off, 0],
                                 color=INK, stroke_width=1, stroke_opacity=0.4)
            lbl = ink_txt(f"n = {n}", size=26).move_to([WALL_X_R + 0.9, y_off, 0])
            waves.add(w); dashed_lvls.add(dashes); labels.add(lbl)
        atom_tag = ink_txt("ATOM: energies", size=28, color=ACCENT
                           ).move_to([WALL_X_L - 1.2, 0.3, 0]).rotate(PI / 2)
        laser_tag = ink_txt("LASER: colours", size=28, color=INK
                            ).move_to([WALL_X_R + 1.8, 0.3, 0]).rotate(-PI / 2)
        self.add(walls, waves, dashed_lvls, labels, atom_tag, laser_tag)
        close_lbl = ink_txt("only what fits survives", size=36, color=RED
                            ).move_to([0, -2.9, 0])
        self.play(Write(close_lbl), run_time=d("A08", 4.16) * 0.85)
        self.wait(d("A08", 4.16) * 0.15)
