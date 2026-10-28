# AGENTS.md — Veralex konten (KentangMotion Engine)

Root kerja: workspace root (`./`).

**Produksi konten baru → pakai skill `veralex-konten`**
(`.opencode/skills/veralex-konten/SKILL.md`): alur 11 langkah, 4 gate approval,
aturan anti-ulang, dan hukum teknis render. Cek `konten-log.md` sebelum mulai.

Pipeline video dijalankan via `./engine` di root repository.

## Aturan singkat

- Satu konten = satu nama folder `konten-N-YYYY-MM-DD`, sama persis di semua
  subfolder. Tanpa spasi. Bikin folder lewat `./engine new <k>`.
- CLI engine terpadu: jalankan `./engine` di root (`setup`, `new`, `audio`, `render`, `encode`, `export`, `status`).
- Setup di laptop/mesin baru: `./engine setup` (cek node/python/ffmpeg + npm install).
- Cerita dulu, jualan di ekor: brand/CTA hanya di ±25 % terakhir.
- Bahasa Indonesia sopan (aku/kamu; "Anda" untuk audiens bisnis), bukan lo/gue.
- Palette: maroon `#4A0E0E`, navy `#172E3C`, gold `#C8A15A`, cream `#FFF3DC`.
