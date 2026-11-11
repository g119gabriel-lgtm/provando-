# Guía SUNAT — Prácticas PRA N.º 003-2026

| Archivo | Para qué |
|---|---|
| `pdf/SUNAT_guia_completa_A4.pdf` | Versión digital completa (35 págs.): teoría, trampas, mapa de artículos, balotario resuelto, simulacro de 30 preguntas y chuleta. |
| `pdf/SUNAT_bolsillo_A6_paginas.pdf` | Librito de repaso A6 (24 págs.) en orden de lectura, para leer en el celular. |
| `pdf/SUNAT_bolsillo_A4_para_cortar.pdf` | El mismo librito impuesto 4 por cara en 3 hojas A4, para imprimir y cortar. |

## Cómo armar el librito A6
1. Imprimí `SUNAT_bolsillo_A4_para_cortar.pdf` a **doble cara, volteo por el borde largo**, tamaño real (100 %, sin "ajustar a página").
2. Apilá las 3 hojas en el orden en que salieron y cortá por las líneas punteadas (una vertical y una horizontal).
3. Quedan 4 mazos: superior-izquierdo (págs. 1–6), superior-derecho (7–12), inferior-izquierdo (13–18), inferior-derecho (19–24).
4. Poné los mazos uno detrás de otro en ese orden, abrochá o anillá por el borde izquierdo, y listo.

## Regenerar
```bash
cd src && node build.js && cd .. && python3 src/impose.py pdf/SUNAT_bolsillo_A6_paginas.pdf pdf/SUNAT_bolsillo_A4_para_cortar.pdf
```
Tipografía: Literata (Google Fonts, OFL), Inter y JetBrains Mono.
