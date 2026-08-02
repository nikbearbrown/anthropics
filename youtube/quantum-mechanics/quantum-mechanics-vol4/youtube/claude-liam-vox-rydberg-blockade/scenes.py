import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.7):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=24).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL): return VGroup(Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD),Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)).arrange(DOWN,buff=.4)
class B02_Levels(Scene):
 def construct(self):
  g=VGroup(*[VGroup(chip(f"ATOM {a}",c,2.5),chip("|g>",SLATE,1.5),chip("|r>",c,1.5)).arrange(DOWN,buff=.35) for a,c in [("A",TEAL),("B",CRIMSON)]]).arrange(RIGHT,buff=2);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B02"]-1))
class B03_Resonant(Scene):
 def construct(self):
  g=VGroup(chip("|gg>",SLATE,2.3),chip("laser resonant",TEAL,3),VGroup(chip("|rg>",TEAL,2),chip("|gr>",CRIMSON,2)).arrange(DOWN,buff=.3)).arrange(RIGHT,buff=.7);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B03"]-1))
class B04_DoubleShift(Scene):
 def construct(self):
  base=Line(LEFT*2,RIGHT*2,color=SLATE);shift=Line(LEFT*2,RIGHT*2,color=CRIMSON).shift(UP*1.4);labs=VGroup(Text("|rr> without interaction",font=MONO,color=SLATE,font_size=28).next_to(base,LEFT),Text("|rr> + V",font=MONO,color=CRIMSON,font_size=32).next_to(shift,LEFT));arr=Arrow(base.get_center(),shift.get_center(),color=CRIMSON,buff=.15);self.play(Create(base),FadeIn(labs[0]),run_time=.5);self.play(GrowArrow(arr),Create(shift),FadeIn(labs[1]),run_time=.8);self.wait(max(.5,D["B04"]-1.3))
class B05_OffResonant(Scene):
 def construct(self):
  laser=Line(LEFT*3,RIGHT*3,color=TEAL,stroke_width=5);level=Line(LEFT*3,RIGHT*3,color=CRIMSON,stroke_width=5).shift(UP*1.4);gap=DoubleArrow(laser.get_center(),level.get_center(),color=INK,buff=.15);lab=Text("interaction shift > drive bandwidth",font=DISPLAY,color=INK,font_size=39,weight=BOLD).to_edge(DOWN,buff=.8);self.play(Create(laser),Create(level),GrowArrow(gap),FadeIn(lab),run_time=1);self.wait(max(.5,D["B05"]-1))
class B06_SpectralNotWall(Scene):
 def construct(self):
  a=title("NOT CONTACT","atoms need not touch",CRIMSON);b=title("SPECTRAL BLOCKADE","interaction changes the energy gap",TEAL);g=VGroup(a,b).arrange(DOWN,buff=.8);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B06"]-1))
class B07_Regimes(Scene):
 def construct(self):
  a=chip("dipole-dipole regime",TEAL,4);b=chip("van der Waals regime",CRIMSON,4);g=VGroup(a,b).arrange(DOWN,buff=.7);cap=Text("scaling depends on levels, fields, and separation",font=SERIF,color=INK,font_size=30,slant=ITALIC).next_to(g,DOWN,buff=.6);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B07"]-1))
class B08_ConditionalGate(Scene):
 def construct(self):
  rows=VGroup(VGroup(chip("control not Rydberg",SLATE,4),chip("target pulse acts",TEAL,3.4)).arrange(RIGHT,buff=.6),VGroup(chip("control Rydberg",CRIMSON,4),chip("target blockaded",CRIMSON,3.4)).arrange(RIGHT,buff=.6)).arrange(DOWN,buff=.8);self.play(FadeIn(rows),run_time=1);self.wait(max(.5,D["B08"]-1))
class B09_Imperfections(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,2.5) for t,c in [("laser error",TEAL),("motion",CRIMSON),("lifetime",SLATE),("finite blockade",CRIMSON)]]).arrange(RIGHT,buff=.45);cap=Text("platform numbers are not universal",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B09"]-1))
class B11_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("The Atom That Gets",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("Too Big to Share",font=SERIF,color="#D7C8FF",font_size=42,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B11"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Each atom has a qubit manifold and'))
  stmt=Text('Each atom has a qubit manifold and a highly excited Ryd',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A laser is tuned to drive the chosen ground-to-Rydberg ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('With neither atom excited, the single-ex'))
  stmt=Text('With neither atom excited, the single-excitation transi',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Either atom can be promoted by the drive',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('The same laser is now detuned from'))
  stmt=Text('The same laser is now detuned from B\'s transition into ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('When the interaction shift is large compared with the d',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Blockade is therefore spectral, not a me'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Blockade is therefore spectral, not a mechanical wall',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Atom A changes an energy gap',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.0
  self.add(bg(),ttl('The interaction may behave like resonant'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The interaction may behave like resonant dipole-dipole ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The scaling is not one universal n-to-the-four over r-c',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('A blockade-based gate uses that conditio'))
  stmt=Text('A blockade-based gate uses that conditional resonance',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The target\'s pulse follows a different evolution depend',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.0
  self.add(bg(),ttl('Real performance also depends on laser e'))
  stmt=Text('Real performance also depends on laser errors, atomic m',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('No single radius, shift, or gate time describes every n',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('The atom that gets too big to'))
  stmt=Text('The atom that gets too big to share: a Rydberg excitati',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
