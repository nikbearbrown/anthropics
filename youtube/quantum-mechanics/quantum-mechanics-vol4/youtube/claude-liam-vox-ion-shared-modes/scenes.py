import sys,json,pathlib,numpy as np
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
def ions(): return VGroup(*[Dot(color=TEAL if i in [0,5] else SLATE,radius=.18) for i in range(6)]).arrange(RIGHT,buff=.8)
class B02_NormalModes(Scene):
 def construct(self):
  top=ions().shift(UP*1.2);bot=ions().shift(DOWN*1.2);ar1=VGroup(*[Arrow(d.get_center(),d.get_center()+UP*.55,color=TEAL,buff=0) for d in top]);ar2=VGroup(*[Arrow(d.get_center(),d.get_center()+(UP if i%2==0 else DOWN)*.55,color=CRIMSON,buff=0) for i,d in enumerate(bot)]);self.play(FadeIn(top),FadeIn(bot),*[GrowArrow(a) for a in ar1],*[GrowArrow(a) for a in ar2],run_time=1.2);self.wait(max(.5,D["B02"]-1.2))
class B03_CollectiveCoordinates(Scene):
 def construct(self):
  g=VGroup(chip("MODE 1",TEAL,2.5),chip("MODE 2",CRIMSON,2.5),chip("MODE 3",SLATE,2.5)).arrange(RIGHT,buff=.7);cap=Text("each mode has amplitudes across the chain",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B03"]-1))
class B04_SpinMotionCoupling(Scene):
 def construct(self):
  a=chip("selected spins",TEAL,3);b=chip("laser force",CRIMSON,3);c=chip("collective motion",SLATE,3.5);g=VGroup(a,b,c).arrange(RIGHT,buff=.7);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B04"]-1))
class B05_CloseLoop(Scene):
 def construct(self):
  circle=Circle(radius=1.8,color=CRIMSON).move_to(LEFT*3.2);dot=Dot(circle.point_at_angle(0),color=TEAL,radius=.15);arr=CurvedArrow(circle.point_at_angle(.1),circle.point_at_angle(-.1),angle=5.5,color=INK);lab=title("MOTION RETURNS","spin phase remains",TEAL).scale(.78).move_to(RIGHT*3.2);self.play(Create(circle),FadeIn(dot),Create(arr),FadeIn(lab),run_time=1.2);self.wait(max(.5,D["B05"]-1.2))
class B06_FlexibleNotFree(Scene):
 def construct(self):
  a=title("NON-NEIGHBOR GATES","often available without SWAP chains",TEAL);b=title("NOT FREE ALL-TO-ALL","pair cost and fidelity can differ",CRIMSON);g=VGroup(a,b).arrange(DOWN,buff=.8);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B06"]-1))
class B07_Limits(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,2.4) for t,c in [("spectrum",TEAL),("chain size",CRIMSON),("heating",SLATE),("crosstalk",CRIMSON)]]).arrange(RIGHT,buff=.45);cap=Text("pair-dependent speed and error",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B07"]-1))
class B08_MultipleModes(Scene):
 def construct(self):
  a=chip("COM mode",TEAL,3);plus=Text("+",font=DISPLAY,color=INK,font_size=40);b=chip("other collective modes",CRIMSON,4);g=VGroup(a,plus,b).arrange(RIGHT,buff=.6);cap=Text("pulse design may use one or several modes",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B08"]-1))
class B10_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Every Ion Shares",font=DISPLAY,color=WHITE,font_size=51,weight=BOLD);b=Text("One Spring",font=SERIF,color="#D7C8FF",font_size=43,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B10"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.47
  self.add(bg(),ttl('A chain of confined ions has many'))
  stmt=Text('A chain of confined ions has many normal modes',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('In one mode the ions move together',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=8.19
  self.add(bg(),ttl('No one mode belongs to a single'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('No one mode belongs to a single ion',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Each normal mode is a collective coordinate with a part',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.39
  self.add(bg(),ttl('State-dependent laser forces couple sele'))
  stmt=Text('State-dependent laser forces couple selected ion spins ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A carefully shaped pulse makes the joint spin state acq',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.3
  self.add(bg(),ttl('In a well-designed gate, the motional tr'))
  stmt=Text('In a well-designed gate, the motional trajectory closes',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The modes disentangle from the spins, while the desired',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.21
  self.add(bg(),ttl('Because multiple ions participate in sha'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Because multiple ions participate in shared modes, non-',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('That is flexible connectivity, not free perfect all-to-',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.88
  self.add(bg(),ttl('Gate strength and fidelity depend on mod'))
  stmt=Text('Gate strength and fidelity depend on mode spectrum, ion',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Different pairs need not have identical speed or error',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.22
  self.add(bg(),ttl('The bus is also not always only'))
  stmt=Text('The bus is also not always only the center-of-mass mode',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Practical entangling gates can involve one or several c',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.42
  self.add(bg(),ttl('Every ion shares one spring — more'))
  stmt=Text('Every ion shares one spring — more precisely, a family ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
