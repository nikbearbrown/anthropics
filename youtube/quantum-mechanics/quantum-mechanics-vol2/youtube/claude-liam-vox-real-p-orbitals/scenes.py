import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def dumbbell(axis='x'):
 if axis=='x':
  a=Ellipse(width=3.3,height=1.8,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15).shift(LEFT*1.65); b=Ellipse(width=3.3,height=1.8,color=TEAL,fill_color=TEAL,fill_opacity=.15).shift(RIGHT*1.65)
 else:
  a=Ellipse(width=1.8,height=3.3,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15).shift(UP*1.65); b=Ellipse(width=1.8,height=3.3,color=TEAL,fill_color=TEAL,fill_opacity=.15).shift(DOWN*1.65)
 return VGroup(a,b,Dot(ORIGIN,radius=.12,color=INK))
class B02_Subspace(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('THE l = 1 SUBSPACE HAS THREE BASIS STATES')); boxes=VGroup(*[RoundedRectangle(width=2.4,height=1.5,corner_radius=.15,color=c).set_fill(c,.1) for c in [CRIMSON,INK,TEAL]]).arrange(RIGHT,buff=.7); labs=VGroup(*[Text(s,font=MONO,font_size=32,color=c).move_to(b) for s,c,b in zip(['m = -1','m = 0','m = +1'],[CRIMSON,INK,TEAL],boxes)]); eq=Text('L^2 = 2 hbar^2 for every combination',font=MONO,font_size=32,color=INK).move_to(DOWN*2.3); self.play(Create(boxes),FadeIn(labs,eq),run_time=1); self.wait(max(.1,d-1))
class B03_Winding(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('OPPOSITE PHASE WINDING · OPPOSITE Lz')); c1=Circle(radius=1.5,color=TEAL).shift(LEFT*3); c2=Circle(radius=1.5,color=CRIMSON).shift(RIGHT*3); a1=CurvedArrow(LEFT*3+DOWN*1.2,LEFT*3+UP*1.2,color=TEAL); a2=CurvedArrow(RIGHT*3+UP*1.2,RIGHT*3+DOWN*1.2,color=CRIMSON); labs=VGroup(Text('m = +1 -> +hbar',font=MONO,font_size=28,color=TEAL).move_to(LEFT*3+DOWN*2.4),Text('m = -1 -> -hbar',font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*3+DOWN*2.4)); self.play(Create(c1),Create(c2),Create(a1),Create(a2),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B04_Density(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('THE TWO DENSITIES LOOK THE SAME')); t1=VGroup(Ellipse(width=4,height=1.4,color=TEAL),Ellipse(width=2,height=.65,color=TEAL)).shift(LEFT*3); t2=VGroup(Ellipse(width=4,height=1.4,color=CRIMSON),Ellipse(width=2,height=.65,color=CRIMSON)).shift(RIGHT*3); labs=VGroup(Text('|Y+1|^2',font=MONO,font_size=29,color=TEAL).move_to(LEFT*3+DOWN*2),Text('|Y-1|^2',font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*3+DOWN*2),Text('phase carries the difference',font=SERIF,font_size=31,color=INK).move_to(DOWN*3)); self.play(Create(t1),Create(t2),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B05_Morph(Scene):
 def construct(self):
  d=DUR.get('B05',10); self.add(bg(),ttl('OPPOSITE-m STATES COMBINE INTO REAL DUMBBELLS')); rings=VGroup(Circle(radius=1.2,color=TEAL).shift(LEFT*4),Circle(radius=1.2,color=CRIMSON).shift(LEFT*1.5)); plus=Text('+ relative phase',font=MONO,font_size=27,color=INK).move_to(UP*2); db=dumbbell('x').scale(.65).shift(RIGHT*3); arrow=Arrow(LEFT*.2,RIGHT*1.3,color=INK,buff=0); self.play(Create(rings),FadeIn(plus),GrowArrow(arrow),Create(db),run_time=1.2); self.wait(max(.1,d-1.2))
class B06_Node(Scene):
 def construct(self):
  d=DUR.get('B06',9); self.add(bg(),ttl('p_x: ORIENTED LOBES · y-z NODAL PLANE')); db=dumbbell('x'); plane=DashedLine(DOWN*2.7,UP*2.7,color=INK); labs=VGroup(Text('+ phase',font=MONO,font_size=26,color=TEAL).move_to(RIGHT*3),Text('- phase',font=MONO,font_size=26,color=CRIMSON).move_to(LEFT*3),Text('sign is not charge',font=SERIF,font_size=29,color=INK).move_to(DOWN*2.8)); self.play(Create(db),Create(plane),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B07_Outcomes(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('p_x IS NOT AN Lz EIGENSTATE')); db=dumbbell('x').scale(.55).shift(LEFT*3); split=VGroup(Arrow(ORIGIN,RIGHT*2+UP*1,color=TEAL,buff=0),Arrow(ORIGIN,RIGHT*2+DOWN*1,color=CRIMSON,buff=0)).shift(RIGHT*.5); labs=VGroup(Text('+hbar   50%',font=MONO,font_size=29,color=TEAL).move_to(RIGHT*4+UP*1),Text('-hbar   50%',font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*4+DOWN*1),Text('<Lz> = 0',font=MONO,font_size=31,color=INK).move_to(DOWN*2.5)); self.play(Create(db),*[GrowArrow(x) for x in split],FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B08_Variance(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('ZERO MEAN DOES NOT MEAN ZERO ANGULAR MOMENTUM')); rows=VGroup(Text('<Lz> = 0',font=MONO,font_size=38,color=SLATE),Text('Var(Lz) = hbar^2',font=MONO,font_size=38,color=CRIMSON),Text('L^2 = 2 hbar^2  (sharp)',font=MONO,font_size=38,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B09_Bases(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('SAME SUBSPACE · DIFFERENT CONVENIENT BASES')); left=VGroup(Text('COMPLEX m BASIS',font=DISPLAY,font_size=30,color=TEAL),Text('sharp Lz',font=MONO,font_size=30,color=TEAL),Text('phase winding',font=SERIF,font_size=28,color=TEAL)).arrange(DOWN).shift(LEFT*3); right=VGroup(Text('REAL CARTESIAN BASIS',font=DISPLAY,font_size=28,color=CRIMSON),Text('oriented p_x, p_y',font=MONO,font_size=30,color=CRIMSON),Text('bond symmetry',font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B10_Context(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('CONTEXT CHOOSES THE BASIS')); mol=VGroup(Dot(LEFT*1.5,color=INK),Dot(RIGHT*1.5,color=INK),Line(LEFT*1.5,RIGHT*1.5,color=CRIMSON),Text('molecular axis',font=MONO,font_size=28,color=CRIMSON).move_to(DOWN*1.2)).shift(LEFT*3); field=VGroup(Arrow(DOWN*1.5,UP*1.5,color=TEAL,buff=0),Text('B along z',font=MONO,font_size=28,color=TEAL).move_to(DOWN*2)).shift(RIGHT*3); self.play(FadeIn(mol),Create(field),run_time=1); self.wait(max(.1,d-1))
class B11_Caveat(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('THE TITLE IS A DELIBERATE OVERSTATEMENT')); rows=VGroup(Text('real p orbitals ARE valid quantum states',font=MONO,font_size=33,color=TEAL),Text('sharp L^2 · not sharp Lz',font=MONO,font_size=33,color=CRIMSON),Text('many-electron orbitals are model-dependent objects',font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B12_Example(Scene):
 def construct(self):
  d=DUR.get('B12',9); self.add(bg(),ttl('WORKED RESULT: MEASURE Lz IN p_x')); rows=VGroup(Text('+hbar with probability 1/2',font=MONO,font_size=36,color=TEAL),Text('-hbar with probability 1/2',font=MONO,font_size=36,color=CRIMSON),Text('average 0 · every result nonzero',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B13_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B13',10); self.add(bg(),ttl('YOUR TURN: NOW PREPARE p_y')); db=dumbbell('y').scale(.55).shift(LEFT*3); rows=VGroup(Text('Lz = +hbar or -hbar',font=MONO,font_size=33,color=INK),Text('each with probability 1/2',font=MONO,font_size=31,color=TEAL),Text('relative phase rotates p_x into p_y',font=SERIF,font_size=29,color=CRIMSON)).arrange(DOWN,buff=.6).shift(RIGHT*2.6); self.play(Create(db),FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B14_Recap(Scene):
 def construct(self):
  d=DUR.get('B14',9); self.add(bg(),Text('WHY CHEMISTRY DRAWS REAL DUMBBELLS',font=DISPLAY,font_size=35,color=CRIMSON).move_to(UP*2.3),Text('opposite-m states combine',font=MONO,font_size=34,color=TEAL).move_to(UP*.8),Text('L^2 sharp · Lz not sharp',font=MONO,font_size=34,color=INK).move_to(DOWN*.4),Text('same l=1 subspace · basis fits the question',font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.59
  self.add(bg(),ttl('For orbital angular momentum l equals on'))
  stmt=Text('For orbital angular momentum l equals one, there are th',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Every linear combination remains inside the same three-',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.71
  self.add(bg(),ttl('The m equals plus one and minus'))
  stmt=Text('The m equals plus one and minus one states are complex',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Their phases wind in opposite directions around the z a',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.72
  self.add(bg(),ttl('Their probability densities are the same'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Their probability densities are the same torus-shaped a',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The opposite angular momentum is encoded in phase windi',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.23
  self.add(bg(),ttl('Add and subtract the opposite-m states w'))
  stmt=Text('Add and subtract the opposite-m states with the proper ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The azimuthal phase factors interfere into real angular',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.81
  self.add(bg(),ttl('A real p-x orbital has two lobes'))
  stmt=Text('A real p-x orbital has two lobes separated by the y-z n',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The signs on the lobes describe wavefunction phase, not',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.93
  self.add(bg(),ttl('The real dumbbell is not an L-z'))
  stmt=Text('The real dumbbell is not an L-z eigenstate',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Its L-z expectation is zero, but zero expectation does ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=13.53
  self.add(bg(),ttl('Those two outcomes give L-z variance h-b'))
  step1=Text('Those two outcomes give L-z variance h-bar squared',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('Meanwhile L squared remains sharp at l times l plu',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('The real orbital keeps definite total orbital angu',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.8
  self.add(bg(),ttl('Neither basis is more real. The complex'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Neither basis is more real',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The complex m basis diagonalizes L-z',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.66
  self.add(bg(),ttl('Chemistry favors oriented orbitals becau'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Chemistry favors oriented orbitals because molecular ax',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Physics often favors m states when a z-directed magneti',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.1
  self.add(bg(),ttl('Prepare p-x and measure L-z. Half the'))
  stmt=Text('Prepare p-x and measure L-z',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Half the trials return plus h-bar and half return minus',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B13_SDT(Scene):
 # B13 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=13.91
  self.add(bg(),ttl('Your turn. For p-y, what are the'))
  step1=Text('For p-y, what are the possible L-z outcomes? Again',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('What changes from p-x is the relative phase betwee',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('result',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
