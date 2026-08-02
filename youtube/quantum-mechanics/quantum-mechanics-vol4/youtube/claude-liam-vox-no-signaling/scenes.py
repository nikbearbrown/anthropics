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
class B02_SharedPair(Scene):
 def construct(self):
  a=chip("ALICE",TEAL,2.7);b=chip("BOB",CRIMSON,2.7);line=Line(a.get_right(),b.get_left(),color=INK,stroke_width=5);g=VGroup(a,line,b).arrange(RIGHT,buff=1);lab=Text("same basis → matched records",font=SERIF,color=SLATE,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.8);self.play(FadeIn(g),FadeIn(lab),run_time=1);self.wait(max(.5,D["B02"]-1))
class B03_BobRandom(Scene):
 def construct(self):
  g=VGroup(VGroup(chip("0",TEAL,2),chip("50%",SLATE,2)).arrange(DOWN,buff=.35),VGroup(chip("1",CRIMSON,2),chip("50%",SLATE,2)).arrange(DOWN,buff=.35)).arrange(RIGHT,buff=1.5);head=Text("BOB'S LOCAL RECORD",font=DISPLAY,color=INK,font_size=42,weight=BOLD).next_to(g,UP,buff=.8);self.play(FadeIn(head),FadeIn(g),run_time=1);self.wait(max(.5,D["B03"]-1))
class B04_ZConditionals(Scene):
 def construct(self):
  rows=VGroup(VGroup(chip("Alice Z: 0",TEAL,3),chip("Bob |0>",TEAL,2.7)).arrange(RIGHT,buff=.7),VGroup(chip("Alice Z: 1",CRIMSON,3),chip("Bob |1>",CRIMSON,2.7)).arrange(RIGHT,buff=.7)).arrange(DOWN,buff=.7);cap=Text("Alice cannot choose the random outcome",font=SERIF,color=INK,font_size=30,slant=ITALIC).next_to(rows,DOWN,buff=.6);self.play(LaggedStart(*[FadeIn(x) for x in rows],lag_ratio=.25),FadeIn(cap),run_time=1.2);self.wait(max(.5,D["B04"]-1.2))
class B05_AverageCenter(Scene):
 def construct(self):
  branches=VGroup(chip("|0> half",TEAL,2.5),chip("|1> half",CRIMSON,2.5)).arrange(RIGHT,buff=.6).move_to(UP*2.1);circle=Circle(radius=1.25,color=SLATE).move_to(DOWN*.9);arr=Arrow(branches.get_bottom(),circle.get_top(),color=INK,buff=.2);dot=Dot(circle.get_center(),color=INK,radius=.14);cap=Text("average: maximally mixed",font=SERIF,color=CRIMSON,font_size=30,slant=ITALIC).next_to(circle,RIGHT,buff=.6);self.play(FadeIn(branches),run_time=.4);self.play(GrowArrow(arr),Create(circle),FadeIn(dot),FadeIn(cap),run_time=1);self.wait(max(.5,D["B05"]-1.4))
class B06_XConditionals(Scene):
 def construct(self):
  left=VGroup(chip("Alice X: +",TEAL,3),chip("Bob |+>",TEAL,2.7)).arrange(DOWN,buff=.4);right=VGroup(chip("Alice X: -",CRIMSON,3),chip("Bob |->",CRIMSON,2.7)).arrange(DOWN,buff=.4);g=VGroup(left,right).arrange(RIGHT,buff=1.3);cap=Text("unconditioned Bob: same center",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.7);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B06"]-1))
class B07_LocalOperations(Scene):
 def construct(self):
  ops=VGroup(chip("unitary",TEAL,2.5),chip("measure",CRIMSON,2.5),chip("do nothing",SLATE,2.8)).arrange(RIGHT,buff=.45);arr=Arrow(UP*.2,DOWN*.9,color=INK);out=chip("Bob's reduced state unchanged",CRIMSON,5).next_to(arr,DOWN,buff=.25);g=VGroup(ops,arr,out).arrange(DOWN,buff=.35);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B07"]-1))
class B08_PostselectionNeedsMessage(Scene):
 def construct(self):
  post=chip("Alice's selected outcome",TEAL,4);channel=chip("classical message",CRIMSON,3.5);bob=chip("Bob sorts runs",SLATE,3.2);g=VGroup(post,channel,bob).arrange(RIGHT,buff=.65);ar=VGroup(Arrow(post.get_right(),channel.get_left(),color=INK,buff=.15),Arrow(channel.get_right(),bob.get_left(),color=INK,buff=.15));self.play(FadeIn(g),run_time=.6);self.play(*[GrowArrow(x) for x in ar],run_time=.7);self.wait(max(.5,D["B08"]-1.3))
class B09_CompareRecords(Scene):
 def construct(self):
  local=VGroup(chip("Alice log",TEAL,3),chip("Bob log",CRIMSON,3)).arrange(RIGHT,buff=1);arr=Arrow(local.get_bottom(),DOWN*1,color=INK,buff=.2);joint=chip("joint correlation pattern",SLATE,4.5).next_to(arr,DOWN,buff=.3);g=VGroup(local,arr,joint).arrange(DOWN,buff=.4);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B09"]-1))
class B10_DescriptionNotSignal(Scene):
 def construct(self):
  a=title("CONDITIONAL UPDATE","depends on Alice's outcome",TEAL);b=title("LOCAL SIGNAL","none in Bob's counts",CRIMSON);g=VGroup(a,b).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Entanglement Can't",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("Send a Message",font=SERIF,color="#D7C8FF",font_size=42,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Let Alice and Bob share a Bell'))
  stmt=Text('Let Alice and Bob share a Bell pair',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('If both measure the same basis, their outcomes show a p',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Before comparison, Bob\'s own results are'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Before comparison, Bob\'s own results are random: zero h',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('A random string carries no chosen bit from Alice',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Suppose Alice measures Z. If she gets'))
  stmt=Text('Suppose Alice measures Z',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('If she gets zero, Bob\'s conditional Z state is zero',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('If Alice instead measures X, Bob\'s condi'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('If Alice instead measures X, Bob\'s conditional states a',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('But Bob measuring locally, without Alice\'s result, stil',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Alice may also apply a local unitary'))
  stmt=Text('Alice may also apply a local unitary or do nothing',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Any local trace-preserving operation, with outcomes ign',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('That classical comparison reveals the no'))
  stmt=Text('That classical comparison reveals the nonclassical join',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It arrives no faster than the communication channel car',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('The instant update is therefore an updat'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The instant update is therefore an update to a conditio',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Result',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('Entanglement cannot send a message: the '))
  stmt=Text('Entanglement cannot send a message: the surprise lives ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
