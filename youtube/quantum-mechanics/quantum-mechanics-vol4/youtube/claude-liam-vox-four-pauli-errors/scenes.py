import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.3):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=26).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_FourActions(Scene):
 def construct(self):
  g=VGroup(*[VGroup(chip(p,c,1.5),Text(s,font=SERIF,color=c,font_size=27,slant=ITALIC)).arrange(DOWN,buff=.25) for p,s,c in [("I","nothing",SLATE),("X","bit flip",TEAL),("Y","bit + phase",CRIMSON),("Z","phase flip",TEAL)]]).arrange(RIGHT,buff=.65);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.18),run_time=1.2);self.wait(max(.5,D["B02"]-1.2))
class B03_OperatorBasis(Scene):
 def construct(self):
  eq=Text("E = a I + b X + c Y + d Z",font=MONO,color=INK,font_size=50);basis=VGroup(*[chip(x,c,1.4) for x,c in [("I",SLATE),("X",TEAL),("Y",CRIMSON),("Z",TEAL)]]).arrange(RIGHT,buff=.45).next_to(eq,DOWN,buff=.8);self.play(FadeIn(eq),run_time=.6);self.play(LaggedStart(*[FadeIn(x) for x in basis],lag_ratio=.15),run_time=.8);self.wait(max(.5,D["B03"]-1.4))
class B04_TiltedRotation(Scene):
 def construct(self):
  c=Circle(radius=2,color=SLATE).shift(UP*.35);old=Arrow(c.get_center(),c.get_center()+UP*1.6,color=INK,buff=0);new=Arrow(c.get_center(),c.get_center()+RIGHT*1.1+UP*1.2,color=CRIMSON,buff=0);eq=Text("U = cos(theta/2) I - i sin(theta/2) n·sigma",font=MONO,color=TEAL,font_size=25);eq.scale_to_fit_width(10.5).move_to(DOWN*2.55);self.play(Create(c),GrowArrow(old),run_time=.6);self.play(Transform(old,new),FadeIn(eq),run_time=.9);self.wait(max(.5,D["B04"]-1.5))
class B05_NotLottery(Scene):
 def construct(self):
  no=title("NOT A HIDDEN LOTTERY","nature need not preselect X, Y, or Z",CRIMSON);yes=title("A LINEAR EXPANSION","coherent components may coexist",TEAL);g=VGroup(no,yes).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B05"]-1.2))
class B06_SyndromeSubspaces(Scene):
 def construct(self):
  src=chip("coherent error",SLATE,3.2);outs=VGroup(*[chip(s,c,1.6) for s,c in [("sX",TEAL),("sY",CRIMSON),("sZ",TEAL)]]).arrange(DOWN,buff=.35).to_edge(RIGHT,buff=1.5);ar=VGroup(*[Arrow(src.get_right(),x.get_left(),color=x[0].get_stroke_color(),buff=.2) for x in outs]);self.play(FadeIn(src),run_time=.4);self.play(*[GrowArrow(x) for x in ar],FadeIn(outs),run_time=1);self.wait(max(.5,D["B06"]-1.4))
class B07_Recovery(Scene):
 def construct(self):
  rows=VGroup(*[VGroup(chip(s,SLATE,2),chip("apply "+p,c,2.5)).arrange(RIGHT,buff=.5) for s,p,c in [("sX","X",TEAL),("sY","Y",CRIMSON),("sZ","Z",TEAL)]]).arrange(DOWN,buff=.35);deg=Text("degenerate codes may merge equivalent errors",font=SERIF,color=INK,font_size=28,slant=ITALIC).next_to(rows,DOWN,buff=.6);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.2),FadeIn(deg),run_time=1.3);self.wait(max(.5,D["B07"]-1.3))
class B08_Linearity(Scene):
 def construct(self):
  top=VGroup(*[chip(x,c,1.5) for x,c in [("I",SLATE),("X",TEAL),("Y",CRIMSON),("Z",TEAL)]]).arrange(RIGHT,buff=.35);arr=Arrow(UP*.4,DOWN*.8,color=INK);out=chip("entire correctable span",CRIMSON,4.8).next_to(arr,DOWN,buff=.25);g=VGroup(top,arr,out).arrange(DOWN,buff=.35);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B08"]-1))
class B09_NoiseChannelScope(Scene):
 def construct(self):
  a=title("OPERATOR BASIS","organizes channel components",TEAL);b=title("NOT ONE UNITARY PAULI","noise may be probabilistic or environmental",CRIMSON);g=VGroup(a,b).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B09"]-1.2))
class B10_Coordinates(Scene):
 def construct(self):
  inf=Text("infinitely many one-qubit operators",font=DISPLAY,color=INK,font_size=42,weight=BOLD);coords=VGroup(*[chip(x,c,1.5) for x,c in [("I",SLATE),("X",TEAL),("Y",CRIMSON),("Z",TEAL)]]).arrange(RIGHT,buff=.35).next_to(inf,DOWN,buff=.8);cap=Text("four coordinates",font=SERIF,color=CRIMSON,font_size=32,slant=ITALIC).next_to(coords,DOWN,buff=.5);self.play(FadeIn(inf),run_time=.5);self.play(FadeIn(coords),FadeIn(cap),run_time=.8);self.wait(max(.5,D["B10"]-1.3))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Every Quantum Error",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("Is Really Just Four",font=SERIF,color="#D7C8FF",font_size=40,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.58
  self.add(bg(),ttl('I does nothing. X flips zero and'))
  stmt=Text('I does nothing',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('X flips zero and one',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=9.0
  self.add(bg(),ttl('This does not mean nature secretly choos'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('This does not mean nature secretly chooses one Pauli er',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('A coherent error can remain a superposition of differen',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.31
  self.add(bg(),ttl('If the syndrome identifies X, the recove'))
  stmt=Text('If the syndrome identifies X, the recovery reverses X',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('If it identifies Z or Y, the corresponding recovery is ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.41
  self.add(bg(),ttl('The deeper principle is linearity: if a'))
  stmt=Text('The deeper principle is linearity: if a code corrects a',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.35
  self.add(bg(),ttl('Real noise can also be probabilistic and'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Real noise can also be probabilistic and entangle the q',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The Pauli basis still organizes its single-qubit operat',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=6.85
  self.add(bg(),ttl('Every one-qubit operator is built from f'))
  stmt=Text('Every one-qubit operator is built from four: identity, ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
