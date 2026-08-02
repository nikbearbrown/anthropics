import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.5):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=25).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_CliffordSet(Scene):
 def construct(self):
  g=VGroup(*[chip(x,c,2.2) for x,c in [("H",TEAL),("S",CRIMSON),("CNOT",TEAL)]]).arrange(RIGHT,buff=.7);cap=Text("Pauli operators map to Pauli operators",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.2),FadeIn(cap),run_time=1.2);self.wait(max(.5,D["B02"]-1.2))
class B03_CompactTracking(Scene):
 def construct(self):
  huge=chip("2^n amplitudes",CRIMSON,3.6);arr=Arrow(LEFT*.5,RIGHT*.5,color=INK);compact=VGroup(chip("Pauli row 1",TEAL,3),chip("Pauli row 2",TEAL,3),chip("...",SLATE,3)).arrange(DOWN,buff=.25);g=VGroup(huge,arr,compact).arrange(RIGHT,buff=.8);cap=Text("compact stabilizer description",font=SERIF,color=INK,font_size=30,slant=ITALIC).next_to(compact,DOWN,buff=.5);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B03"]-1))
class B04_GKScope(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,3) for t,c in [("stabilizer input",TEAL),("Clifford gates",CRIMSON),("Pauli measurements",TEAL)]]).arrange(RIGHT,buff=.5);out=Text("efficient classical simulation",font=DISPLAY,color=INK,font_size=40,weight=BOLD).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(out),run_time=1);self.wait(max(.5,D["B04"]-1))
class B05_NotSufficient(Scene):
 def construct(self):
  a=title("SUPERPOSITION","present in Clifford circuits",TEAL);b=title("ENTANGLEMENT","also present",CRIMSON);c=Text("not sufficient for generic advantage",font=DISPLAY,color=INK,font_size=38,weight=BOLD);g=VGroup(a,b,c).arrange(DOWN,buff=.55);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.2),run_time=1.2);self.wait(max(.5,D["B05"]-1.2))
class B06_TLeavesClosure(Scene):
 def construct(self):
  inside=VGroup(chip("X",TEAL,1.5),chip("Y",CRIMSON,1.5),chip("Z",TEAL,1.5)).arrange(RIGHT,buff=.3);box=SurroundingRectangle(inside,color=SLATE,buff=.5);t=chip("T = phase pi/4",CRIMSON,3.5).next_to(box,UP,buff=.8);arrow=Arrow(t.get_bottom(),box.get_top(),color=CRIMSON,buff=.2);cross=Text("does not stay inside Pauli set",font=SERIF,color=INK,font_size=30,slant=ITALIC).next_to(box,DOWN,buff=.7);self.play(FadeIn(inside),Create(box),FadeIn(t),run_time=.6);self.play(GrowArrow(arrow),FadeIn(cross),run_time=.7);self.wait(max(.5,D["B06"]-1.3))
class B07_GrowingPieces(Scene):
 def construct(self):
  rows=VGroup(*[VGroup(chip(f"T count {n}",SLATE,2.7),VGroup(*[Dot(color=CRIMSON,radius=.12) for _ in range(k)]).arrange(RIGHT,buff=.15)).arrange(RIGHT,buff=.6) for n,k in [("1",2),("4",5),("8",9)]]).arrange(DOWN,buff=.45);cap=Text("illustrative growth in stabilizer pieces",font=SERIF,color=TEAL,font_size=30,slant=ITALIC).next_to(rows,DOWN,buff=.6);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.2),FadeIn(cap),run_time=1.2);self.wait(max(.5,D["B07"]-1.2))
class B08_Resources(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,2.6) for t,c in [("T count",TEAL),("T depth",CRIMSON),("structure",SLATE),("simulator",TEAL)]]).arrange(RIGHT,buff=.45);cap=Text("cost depends on all four",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B08"]-1))
class B09_UniversalNotAlwaysHard(Scene):
 def construct(self):
  yes=title("CLIFFORD + T","universal for approximation",TEAL);no=title("DOES NOT IMPLY","every circuit instance is hard",CRIMSON);g=VGroup(yes,no).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B09"]-1.2))
class B11_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("The Gate That Breaks",font=DISPLAY,color=WHITE,font_size=49,weight=BOLD);b=Text("the Simulator",font=SERIF,color="#D7C8FF",font_size=42,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B11"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('The Clifford gate set includes Hadamard,'))
  stmt=Text('The Clifford gate set includes Hadamard, phase S, and c',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('These gates map Pauli operators to Pauli operators unde',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('A stabilizer state can therefore be repr'))
  stmt=Text('A stabilizer state can therefore be represented by a co',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Clifford gates update that list with polynomial classic',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('That is the Gottesman-Knill lesson: a br'))
  stmt=Text('That is the Gottesman-Knill lesson: a broad class of Cl',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Superposition and entanglement are there'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Superposition and entanglement are therefore not suffic',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Clifford circuits can contain both',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.0
  self.add(bg(),ttl('One T gate is not catastrophic. Classica'))
  stmt=Text('One T gate is not catastrophic',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Classical methods can expand a circuit into a small com',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('That is why T count, T depth,'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('That is why T count, T depth, and related measures of n',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The exact cost depends on the circuit and algorithm use',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.0
  self.add(bg(),ttl('Clifford plus T is also a universal'))
  stmt=Text('Clifford plus T is also a universal gate set for approx',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('But universality does not prove that every such circuit',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('The gate that breaks the compact stabili'))
  stmt=Text('The gate that breaks the compact stabilizer story is T ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
