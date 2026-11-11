"""Imposición 'cortar y apilar': 4 páginas A6 por cara de A4, doble faz.
Imprimir doble cara volteando por el borde LARGO, cortar en cruz,
y apilar los 4 mazos en orden (mazo 1 arriba). Queda el librito en orden."""
import sys
from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from io import BytesIO

src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
pages = list(r.pages)
mm2pt = 72 / 25.4
A4W, A4H = 210 * mm2pt, 297 * mm2pt
CW, CH = A4W / 2, A4H / 2                      # celda = A6 exacto (105 x 148.5)
while len(pages) % 8:
    pages.append(None)
N = len(pages); S = N // 8                     # hojas
cells = [(0, 1), (1, 1), (0, 0), (1, 0)]       # (col, fila) fila 1 = arriba

def marks(back):
    buf = BytesIO(); c = canvas.Canvas(buf, pagesize=(A4W, A4H))
    c.setStrokeColorRGB(.55, .55, .55); c.setLineWidth(.3)
    c.setDash(2, 2)
    c.line(CW, 4*mm, CW, A4H - 4*mm); c.line(4*mm, CH, A4W - 4*mm, CH)
    c.setDash()
    for x in (0, CW, A4W):                      # marcas de corte en bordes
        c.line(x, 0, x, 3*mm); c.line(x, A4H - 3*mm, x, A4H)
    for y in (0, CH, A4H):
        c.line(0, y, 3*mm, y); c.line(A4W - 3*mm, y, A4W, y)
    c.save(); buf.seek(0)
    return PdfReader(buf).pages[0]

w = PdfWriter()
for s in range(S):
    for side in (0, 1):
        sheet = PageObject.create_blank_page(width=A4W, height=A4H)
        for k, (col, row) in enumerate(cells):
            idx = k * 2 * S + 2 * s + side      # mazo k, hoja s
            p = pages[idx]
            if p is None: continue
            c = 1 - col if side else col        # reverso espejado (borde largo)
            pw, ph = float(p.mediabox.width), float(p.mediabox.height)
            sc = min(CW / pw, CH / ph)
            tx = c * CW + (CW - pw * sc) / 2
            ty = row * CH + (CH - ph * sc) / 2
            sheet.merge_transformed_page(p, Transformation().scale(sc, sc).translate(tx, ty))
        sheet.merge_page(marks(side))
        w.add_page(sheet)
w.add_metadata({"/Title": "SUNAT de bolsillo — imposición A6 en A4"})
with open(dst, "wb") as f: w.write(f)
print(f"{N} páginas A6 -> {S} hojas A4 doble faz ({2*S} caras)")
