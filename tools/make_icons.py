"""Dessine l'icône de l'appli (dos de carte) et l'écran de démarrage."""
from PIL import Image, ImageDraw, ImageFont
import pathlib, sys
RES = pathlib.Path("android/app/src/main/res")
SEA=(31,95,122); SEA2=(55,118,142); CREAM=(251,239,210); SUN=(185,125,12)
FONT = sys.argv[1]

def card(size, scale=1.0):
    """Carte face cachée centrée, sur fond transparent, dans un carré `size`."""
    im = Image.new("RGBA",(size,size),(0,0,0,0)); d = ImageDraw.Draw(im)
    w = int(size*0.50*scale); h = int(w*1.45); x0=(size-w)//2; y0=(size-h)//2
    r = int(w*0.14)
    d.rounded_rectangle([x0-int(w*.05),y0-int(w*.05),x0+w+int(w*.05),y0+h+int(w*.05)],r+int(w*.05),fill=CREAM)
    # rayures
    stripes = Image.new("RGBA",(w,h),SEA); sd = ImageDraw.Draw(stripes)
    step = max(4,int(w*0.11))
    for k in range(-h, w+h, step*2):
        sd.polygon([(k,0),(k+step,0),(k+step-h,h),(k-h,h)],fill=SEA2)
    mask = Image.new("L",(w,h),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,w-1,h-1],r,fill=255)
    im.paste(stripes,(x0,y0),mask)
    cr = int(w*0.26); cx=size//2; cy=size//2
    d.ellipse([cx-cr,cy-cr,cx+cr,cy+cr],fill=SEA,outline=CREAM,width=max(2,int(w*0.03)))
    f = ImageFont.truetype(FONT, int(cr*1.45))
    d.text((cx,cy+int(cr*0.05)),"?",font=f,fill=CREAM,anchor="mm")
    return im

def square(size, scale):
    bg = Image.new("RGBA",(size,size),SEA+(255,))
    bg.alpha_composite(card(size,scale)); return bg

dens = {"mdpi":(48,108),"hdpi":(72,162),"xhdpi":(96,216),"xxhdpi":(144,324),"xxxhdpi":(192,432)}
for k,(ic,fg) in dens.items():
    dd = RES/f"mipmap-{k}"
    square(ic,1.0).save(dd/"ic_launcher.png")
    m = Image.new("L",(ic,ic),0); ImageDraw.Draw(m).ellipse([0,0,ic-1,ic-1],fill=255)
    rnd = square(ic,0.95); rnd.putalpha(m); rnd.save(dd/"ic_launcher_round.png")
    card(fg,0.95).save(dd/"ic_launcher_foreground.png")
(RES/"values"/"ic_launcher_background.xml").write_text('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#1F5F7A</color>\n</resources>\n')
# écrans de démarrage
for p in RES.glob("drawable*/splash.png"):
    w,h = Image.open(p).size
    im = Image.new("RGBA",(w,h),(238,242,243,255))
    s = min(w,h); c = card(s,0.75)
    im.alpha_composite(c,((w-s)//2,(h-s)//2)); im.convert("RGB").save(p)
print("icônes ok")
