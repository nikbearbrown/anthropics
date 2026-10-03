from pathlib import Path
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parent
files=sorted((root/'media/images/scenes').glob('B*.png'))
out=Image.new('RGB',(1280,390*((len(files)+1)//2)), '#F2F0E9')
d=ImageDraw.Draw(out)
for i,p in enumerate(files):
    im=Image.open(p).convert('RGB').resize((640,360))
    x,y=(i%2)*640,(i//2)*390
    out.paste(im,(x,y+25)); d.text((x+10,y+5),p.name,fill='#3D3929')
out.save(root/'preview-contact.jpg')
