"""Icône de l'appli à partir d'une photo (recadrée sur le visage)."""
from PIL import Image, ImageDraw
import pathlib, sys
RES = pathlib.Path("android/app/src/main/res")
im = Image.open(sys.argv[1]).convert("RGB")
cx, cy = int(sys.argv[2]), int(sys.argv[3])   # centre du visage
def crop(side):
    h = side//2
    return im.crop((cx-h, cy-h, cx+h, cy+h))
tight, wide = crop(840), crop(1080)   # icônes classiques / icône adaptative (bords rognés par Android)
dens = {"mdpi":(48,108),"hdpi":(72,162),"xhdpi":(96,216),"xxhdpi":(144,324),"xxxhdpi":(192,432)}
for k,(ic,fg) in dens.items():
    d = RES/f"mipmap-{k}"
    sq = tight.resize((ic,ic), Image.LANCZOS).convert("RGBA")
    m = Image.new("L",(ic,ic),0); ImageDraw.Draw(m).rounded_rectangle([0,0,ic-1,ic-1],int(ic*.18),fill=255)
    s2 = sq.copy(); s2.putalpha(m); s2.save(d/"ic_launcher.png")
    m2 = Image.new("L",(ic,ic),0); ImageDraw.Draw(m2).ellipse([0,0,ic-1,ic-1],fill=255)
    r = sq.copy(); r.putalpha(m2); r.save(d/"ic_launcher_round.png")
    wide.resize((fg,fg), Image.LANCZOS).save(d/"ic_launcher_foreground.png")
print("icône photo ok")
