"""Imposición en cuadernillo (saddle-stitch) A6, a partir de hojas A4.
Cada A4 = 2 medias hojas A5 (arriba y abajo). Doble faz, volteo por el BORDE LARGO.
Cortar cada A4 por la mitad (línea horizontal), doblar cada mitad al medio
(línea vertical) y encartar las mitades una dentro de otra en orden: 1, 2, 3...
Grapar o pegar por el lomo."""
import sys
from io import BytesIO
from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

src, dst = sys.argv[1], sys.argv[2]
pages = list(PdfReader(src).pages)
while len(pages) % 4:
    pages.append(None)
N = len(pages)
H = N // 4                       # medias hojas A5
pt = 72 / 25.4
A4W, A4H = 210 * pt, 297 * pt
CW, CH = A4W / 2, A4H / 2        # celda A6 = 105 x 148.5

def a5(i):
    """(frente izq, frente der), (dorso izq, dorso der) de la media hoja i (0 = exterior)."""
    return (N - 2*i, 2*i + 1), (2*i + 2, N - 2*i - 1)

def guides(labels):
    buf = BytesIO(); c = canvas.Canvas(buf, pagesize=(A4W, A4H))
    c.setStrokeColorRGB(.6, .6, .6); c.setLineWidth(.35)
    c.setDash(3, 2); c.line(0, CH, A4W, CH)                   # corte
    c.setDash(1, 2)
    for y0 in (0, CH):                                        # pliegue (solo marcas en bordes)
        c.line(CW, y0 + 1*mm, CW, y0 + 6*mm); c.line(CW, y0 + CH - 6*mm, CW, y0 + CH - 1*mm)
    c.setDash(); c.setFont("Helvetica", 5); c.setFillColorRGB(.55, .55, .55)
    c.drawString(2*mm, CH + 1*mm, "✂ cortar")
    for y0, t in labels:
        c.drawRightString(A4W - 2*mm, y0 + CH - 3*mm, t)
    c.save(); buf.seek(0)
    return PdfReader(buf).pages[0]

def place(sheet, pnum, col, row):
    if pnum is None or pages[pnum-1] is None: return
    p = pages[pnum-1]
    pw, ph = float(p.mediabox.width), float(p.mediabox.height)
    s = min(CW / pw, CH / ph)
    tx = col*CW + (CW - pw*s)/2; ty = row*CH + (CH - ph*s)/2
    sheet.merge_transformed_page(p, Transformation().scale(s, s).translate(tx, ty))

w = PdfWriter()
for k in range(0, H, 2):                      # cada A4 lleva medias hojas k (arriba) y k+1 (abajo)
    for side in (0, 1):
        sheet = PageObject.create_blank_page(width=A4W, height=A4H)
        labels = []
        for half, row in ((k, 1), (k + 1, 0)):
            if half >= H: continue
            fr, bk = a5(half)
            l, r = (fr if side == 0 else bk)
            place(sheet, l, 0, row); place(sheet, r, 1, row)
            labels.append((row*CH, f"pliego {half+1}/{H}" + (" (frente)" if side == 0 else " (dorso)")))
        sheet.merge_page(guides(labels))
        w.add_page(sheet)
w.add_metadata({"/Title": "SUNAT de bolsillo — cuadernillo A6 (A4 doble faz)"})
with open(dst, "wb") as f: w.write(f)
print(f"{N} págs. A6 -> {H} pliegos A5 -> {len(w.pages)//2} hojas A4 doble faz")
