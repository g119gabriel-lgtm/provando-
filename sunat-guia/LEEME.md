# Guía SUNAT — Prácticas PRA N.º 003-2026

| Archivo | Para qué |
|---|---|
| `pdf/SUNAT_guia_completa_A4.pdf` | Versión digital completa (35 págs.): teoría, trampas, mapa de artículos, balotario resuelto, simulacro de 30 preguntas y chuleta. |
| `pdf/SUNAT_bolsillo_A6_paginas.pdf` | Librito de repaso A6 (24 págs.) en orden de lectura, para leer en el celular. |
| `pdf/SUNAT_bolsillo_A6_ahorro_tinta.pdf` | Librito A6 sin fondos de color (para imprimir). |
| `pdf/SUNAT_bolsillo_A4_doble_faz_cortar_y_doblar.pdf` | Cuadernillo A6 listo para imprimir en 3 hojas A4, sin fondos (ahorra tinta). |

## Cómo armar el cuadernillo A6
1. Imprimí `SUNAT_bolsillo_A4_doble_faz_cortar_y_doblar.pdf` a **doble cara, volteo por el borde LARGO**, tamaño real (100 %).
2. Cortá cada hoja A4 **una vez**, por la línea horizontal del medio (✂). Salen 6 medias hojas; cada una tiene impreso "pliego N/6".
3. Doblá cada media hoja por la mitad (marcas en el borde), con la cara "frente" hacia afuera.
4. Encartá los pliegos uno dentro de otro: el 1 afuera (lleva la portada), el 2 adentro del 1, ... el 6 en el centro.
5. Grapá o pegá por el lomo (el doblez). Queda el librito A6 en orden de la 1 a la 24.

## Regenerar
```bash
cd src && node build.js && cd .. && python3 src/impose_folleto.py pdf/SUNAT_bolsillo_A6_ahorro_tinta.pdf pdf/SUNAT_bolsillo_A4_doble_faz_cortar_y_doblar.pdf
```
Tipografía: Literata (Google Fonts, OFL), Inter y JetBrains Mono.
