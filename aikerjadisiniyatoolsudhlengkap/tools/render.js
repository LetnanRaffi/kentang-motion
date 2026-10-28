const path = require('node:path');
const fs = require('node:fs');
const {openBrowser} = require('@remotion/renderer');
const rendererDir = path.dirname(require.resolve('@remotion/renderer'));
const {screenshot} = require(path.join(rendererDir, 'puppeteer-screenshot.js'));

const FPS = 30;
const W = 1080, H = 1920;
const KONTEN = process.env.KONTEN || 'konten-1';
const OUT = path.join(__dirname, '..', 'frames', KONTEN);

(async () => {
  const dur = Number(process.env.DUR || 42.65);
  const total = Math.ceil(dur * FPS);
  const start = Number(process.env.START || 0);
  fs.mkdirSync(OUT, {recursive: true});

  const browser = await openBrowser('chrome', {chromeMode: 'headless-shell', logLevel: 'error'});
  const page = await browser.newPage({
    context: null,
    initialUrl: 'about:blank',
    logLevel: 'error',
    indent: false,
  });
  await page.setViewport({width: W, height: H, deviceScaleFactor: 1});
  await page.goto({url: 'http://127.0.0.1:8123/' + KONTEN + '/index.html?clean=1', timeout: 60000, options: {waitUntil: 'load'}});
  for (let k = 0; k < 120; k++) {
    const ok = await page.evaluate(() => !!(window.OPENER && window.OPENER.ready));
    if (ok) break;
    await new Promise((r) => setTimeout(r, 250));
  }
  await page.evaluate(async () => {
    await document.fonts.ready;
    window.OPENER.tl.pause(0, false);
  });
  await new Promise((r) => setTimeout(r, 800));

  for (let i = start; i < total; i++) {
    const t = i / FPS;
    await page.evaluate((tt) => window.OPENER.seek(tt), t);
    await screenshot({
      page,
      type: 'jpeg',
      width: W,
      height: H,
      scale: 1,
      omitBackground: false,
      jpegQuality: 96,
      path: path.join(OUT, 'f' + String(i).padStart(5, '0') + '.jpg'),
      remotionSharedMemory: null,
    });
    if (i % 100 === 0) process.stdout.write(`frame ${i}/${total}\n`);
  }
  await browser.close({silent: true});
  console.log('done', total);
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
