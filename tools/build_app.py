"""Génère www/index.html (appli Android) à partir de la page source de l'artifact."""
import re, sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
out = pathlib.Path(sys.argv[2])
src = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>\n?', '', src)
src = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', '', src)
title = re.search(r'<title>.*?</title>', src).group(0)
src = src.replace(title, '', 1)
fonts = """
@font-face{font-family:"Young Serif";src:url(fonts/young-serif-latin-400-normal.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Figtree";src:url(fonts/figtree-latin-400-normal.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Figtree";src:url(fonts/figtree-latin-500-normal.woff2) format("woff2");font-weight:500;font-display:swap}
@font-face{font-family:"Figtree";src:url(fonts/figtree-latin-600-normal.woff2) format("woff2");font-weight:600;font-display:swap}
@font-face{font-family:"Figtree";src:url(fonts/figtree-latin-700-normal.woff2) format("woff2");font-weight:700;font-display:swap}
*,*::before,*::after{box-sizing:border-box}
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);-webkit-text-size-adjust:100%}
body{margin:0;-webkit-tap-highlight-color:transparent}
img{max-width:100%}
"""
head = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
{title}
<style>{fonts}</style>
</head>
<body>
"""
out.write_text(head + src + "\n</body>\n</html>\n", encoding="utf-8")
print("written", out, len(src))
