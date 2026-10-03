"""Extract real frames, never fabricate review evidence. Produces contact sheets for inspection."""
import argparse,json,subprocess,math
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--master');args=parser.parse_args()
out=R/'_qc'/'inspection';out.mkdir(parents=True,exist_ok=True)
sheet=json.loads((R/'beat_sheet.json').read_text())
def frame(video,at,name):
    p=out/name
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(at),'-i',str(video),'-frames:v','1','-vf','scale=960:-1',str(p)],check=True)
    return p
def contact(items,name,cols,w,h):
    canvas=Image.new('RGB',(cols*w,math.ceil(len(items)/cols)*(h+24)),'#F2F0E9');d=ImageDraw.Draw(canvas)
    for i,(p,text) in enumerate(items):
        x,y=i%cols*w,i//cols*(h+24)
        canvas.paste(Image.open(p).convert('RGB').resize((w,h)),(x,y+24));d.text((x+6,y+5),text,fill='#3D3929')
    canvas.save(out/name)
if not args.master:
    items=[]
    for b in sheet['beats']:
        bid=b['beat_id'];p=R/'media'/f'{bid}.mp4'
        if not p.exists():p=R/'manim'/f'{bid}.mp4'
        dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(p)]))
        for f in (.15,.5,.85):
            image=frame(p,dur*f,f'{bid}-{int(f*100)}.png');items.append((image,f'{bid} {int(f*100)}%'))
    for n in range(0,len(items),21): contact(items[n:n+21],f'beats-{n//21+1}.jpg',3,480,270)
else:
    video=Path(args.master)
    subprocess.run(['ffmpeg','-v','error','-y','-i',str(video),'-vf','fps=2,scale=384:-1',str(out/'scan-%04d.jpg')],check=True)
    items=[(p,f'{(i/2):.1f}s') for i,p in enumerate(sorted(out.glob('scan-*.jpg')))]
    for n in range(0,len(items),64):contact(items[n:n+64],f'scan-sheet-{n//64+1}.jpg',8,384,216)
print(out)
