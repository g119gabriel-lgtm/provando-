// Genera los PDF a partir del HTML con Chromium (Playwright).
const { chromium } = require('playwright');
const path = require('path');
const out = path.resolve(__dirname, '..', 'pdf');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Guía digital A4 con número de página al pie
  await page.goto('file://' + path.join(__dirname, 'guia.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: path.join(out, 'SUNAT_guia_completa_A4.pdf'),
    preferCSSPageSize: true,
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7pt;color:#7b858c;padding:0 17mm;display:flex;justify-content:space-between">
      <span>Guía de estudio SUNAT · PRA N.º 003-2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });

  // Librito A6 (páginas sueltas en orden de lectura)
  await page.goto('file://' + path.join(__dirname, 'bolsillo.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: path.join(out, 'SUNAT_bolsillo_A6_paginas.pdf'),
    preferCSSPageSize: true,
    printBackground: true,
  });

  await browser.close();
  console.log('ok');
})();
