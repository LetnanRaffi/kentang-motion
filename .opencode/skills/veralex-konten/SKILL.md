---
name: veralex-konten
description: Alur kerja produksi konten Veralex Consulting — video edukasi vertikal 9:16 gaya kartun panggung (HTML+GSAP, VO ElevenLabs, SFX, subtitle, render MP4). Pakai setiap kali user minta "bikin konten", "konten baru", "konten-2", "naskah VO", "video edukasi/promo Veralex", "render konten", atau menyebut nomor konten. Mengatur urutan kerja, gate approval, penamaan folder, aturan anti-ulang tokoh/latar, dan hukum teknis render.
---

# Produksi konten Veralex

Video edukasi 9:16 yang **bercerita dulu, jualan di ekor**. Penonton harus keburu
peduli ke tokohnya sebelum nama brand muncul. Bukan iklan produk.

- Root pipeline: workspace root (`./` atau `./engine`)
- Gaya visual: skill `bang-motion` → `references/kartun-panggung.md` (wajib dibaca)
- Log anti-ulang: `konten-log.md`

## Prinsip

1. **Cerita dulu, jualan di ekor.** 75 % awal tanpa brand, harga, atau CTA. Brand
   masuk sebagai akibat cerita (panggung resolusi). CTA maksimal 1 kalimat di
   6 detik terakhir.
2. **Panjang boleh, kosong jangan.** Durasi mengikuti bobot cerita (21–45 dtk),
   bukan angka. Yang dilarang: adegan/kalimat tanpa informasi baru.
3. **Anti-ulang.** Tiap konten tokoh baru, latar & angle beda dari konten
   sebelumnya (tokoh lama boleh balik setelah jeda 4 konten). Cek log dulu.
4. **Kartun panggung.** Panggung 1080×1920 seukuran frame; kamera hanya di dalam
   panggung (zoom 1,08–1,95, tidak pernah wide); antar panggung cut atau geser
   96 px (x) / 72 px (y) + blur ≤10 px; tiap panggung ≥10 benda beraksi; sendi
   ditulis manual; palet flat cerah tanpa tekstur.
5. **Subtitle satu-satunya teks kalimat di layar** (sadar menyimpang dari "nol
   caption"): bawah 500 px, Nunito 600 42 px, 3 lapis shadow, pinggir 80 px.
   Di bawah 500 px ketutup UI Reels/TikTok.
6. **Bahasa sopan**: aku/kamu ("Anda" untuk audiens bisnis), bukan lo/gue.

## Gaya cerita — pinjam dari Kok Bisa

Referensi rasa: kanal edukasi animasi **Kok Bisa**. Yang diambil cuma DNA-nya,
bukan durasi (mereka 5–10 mnt) dan bukan kulit visualnya:

| Ciri Kok Bisa | Terjemahan ke 9:16 (21–45 dtk) |
|---|---|
| Judul/hook berupa pertanyaan atau fakta ganjil | Hook = pertanyaan yang bikin berhenti scroll ("Kenapa brand bisa direbut?") |
| Narasi menyapa penonton ("kamu pernah...") | VO pakai "kamu", bukan "konsumen" atau "pelaku usaha" |
| Miskonsepsi umum dibongkar dulu | Sebut keyakinan salah ("yang pakai duluan yang menang") sebelum aturan sebenarnya |
| Konsep abstrak → analogi sehari-hari | **Satu analogi visual per konten** yang benar-benar digambar di panggung (cth merek = nama rumah; first to file = siapa yang cap buku pertama) |
| Penjelasan bertahap, satu ide per beat | Tiap panggung membawa satu ide; jangan gabung dua konsep |
| Penutup berupa takeaway, bukan rangkuman | Tutup dengan satu kalimat yang bisa diulang penonton, baru CTA |

Bedanya: Kok Bisa menjelaskan panjang karena tayang di YouTube; di sini
penjelasannya harus selesai dalam satu tarikan napas. Kalau analogi butuh
30 detik untuk dijelaskan, analoginya yang salah — ganti yang lebih instan.

Analogi visual wajib dicatat di rundown (kolom visual) supaya tidak berubah
jadi diagram abstrak di tengah produksi.

## Konteks bisnis (sumber ide)

PT. Veralex Consulting Indonesia (Bekasi): merek DJKI (daftar/perpanjang/alih/
hak cipta/desain industri), badan usaha (PT PMDN/PMA/perorangan, CV), visa &
ITAS/KITAS, sertifikasi produk (halal, SNI, BPOM, K3L, Postel).
Pembeda: portal tracking proyek. Bukti: 150+ klien, 99% success, 5.0/5 review.
CTA tunggal: WhatsApp `0812 1947 6385` · veralexconsulting.com.
Ide: https://veralexconsulting.com/artikel (tenggat regulasi bulanan = hook kuat).

## Tokoh, latar, angle

- **Tokoh**: tidak ada daftar tetap — dibuat per konten (nama, umur, profesi,
  kostum). Syarat: beda dari 4 konten terakhir.
- **Brand nyata**: boleh plesetan nama ("Kopi Kenangan" → "Kopi Kenanga"), tanpa
  logo/maskot/nama asli, dan brand nyata tidak boleh jadi pihak yang bersalah.
- **Konsultan Veralex** hanya muncul di panggung resolusi, bukan tokoh utama.
- **Latar** (rotasi): kedai · dapur rumahan · bengkel · ruang perawatan · gudang
  ekspor · pasar · kantor notaris · loket DJKI · kafe · ruko.
- **Angle** (rotasi): nama merek direbut · tenggat regulasi · salah pilih badan
  usaha · ditolak BPOM/SNI · KITAS hampir habis · halal belum ada · CV vs PT
  perorangan.

## Alur — 11 langkah, 4 gate

Gate wajib lewat **sebelum** menulis kode. Rombak rundown murah, rombak kode mahal.

| # | Langkah | Output | Gate |
|---|---|---|---|
| 0 | Cek log; tentukan tokoh + latar + angle | 1 baris tujuan | — |
| 1 | Brief gaya | 6 baris | **GATE 1** |
| 2 | Naskah VO | `voiceovernaskahai/<k>/naskah-vo.txt` | user generate audio |
| 3 | Rundown panggung | tabel | **GATE 2** |
| 4 | Scaffold folder | 7 folder | — |
| 5 | Bangun scene | `simpenhtml/<k>/index.html` | — |
| 6 | Sinkron VO → `DUR`, `SUBS`, cue | angka pasti | — |
| 7 | SFX + mix | `audio/sfx/<k>/mix.wav` | — |
| 8 | Verifikasi visual | contact sheet 6–20 frame | **GATE 3** |
| 9 | Render + encode | `hasil/<k>/<k>.mp4` | — |
| 10 | Caption + log | `caption.txt` | **GATE 4** |

### 0 — Topik

Satu baris: `tokoh · latar · angle · layanan · rasa yang ditinggalkan`.
Cek `konten-log.md` supaya tokoh/latar/angle tidak mengulang.

### 1 — Brief gaya (6 baris)

tema/layanan · 3 kata rasa · palet (maroon `#4A0E0E`, navy `#172E3C`, gold
`#C8A15A`, cream `#FFF3DC` + aksen per cerita) · font display (Baloo 2 + Nunito
untuk scene; hindari Poppins/Inter/Roboto) · tanda tangan gerak (satu jenis) ·
jumlah panggung + end card.

### 2 — Naskah VO

5 blok, dipisah baris kosong, tanpa header/judul, tanpa tag SSML (langsung paste
ke ElevenLabs). Patokan 5,5 suku kata/detik: satu konflik ≈ 25–30 dtk, dua babak
(masalah → salah langkah → pelajaran) ≈ 35–45 dtk.

```
1. Hook (masalah langsung)   0–3 dtk   pertanyaan/fakta ganjil, bikin berhenti scroll
2. Pemicu / kisah            3–9 dtk   masalah nyata & spesifik
3. Edukasi aturan            9–17 dtk  fakta/regulasi, tanpa jualan
4. Resolusi                 17–23 dtk  brand masuk wajar
5. Penutup + CTA            23–27 dtk  CTA 1 kalimat
```
(detik = patokan 27 dtk; geser proporsional untuk versi panjang)

Tes tiap adegan: ada info baru tiap 3 dtk? bisa dihapus tanpa kehilangan cerita?
tidak ada kalimat pengantar ("jadi gini...")? Kalau tidak muat, potong adegan —
jangan dipercepat VO-nya. Angka untuk TTS tidak disingkat: `0812 1947 6385`.

### 3 — Rundown panggung

`detik | panggung | kalimat VO | visual (≥10 benda bergerak) | kamera`.
Satu panggung per adegan cerita, bukan per kalimat. Kalau hanya aksi yang berubah,
tetap di panggung yang sama. 4–6 panggung + end card, sesuai jumlah babak.

### 4 — Scaffold

```bash
./engine new konten-2-2026-10-30
```

Membuat 7 folder: `simpenhtml`, `frames`, `hasil`, `caption`,
`voiceovernaskahai`, `audio/voiceover`, `audio/sfx`.

### 5 — Bangun scene

`simpenhtml/<k>/index.html`. Mulai dari copy konten sebelumnya, ganti panggung +
timing. Kontrak wajib:

- `?clean=1` → tahan di frame 0 (untuk render), `?t=12.3` → seek, `?debug=1` → scrub.
- `window.OPENER = {tl, seek(t), ready}` dipakai `tools/render.js`.
- Semua visual fungsi murni dari `tl.time()` — tanpa `Date.now()`/`Math.random()`.
- Font dari CDN Google Fonts (render butuh internet).

### 6 — Sinkron VO

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1 audio/voiceover/<k>/*.mp3
ffmpeg -hide_banner -i audio/voiceover/<k>/*.mp3 -af "silencedetect=noise=-30dB:d=0.25" -f null - 2>&1 | grep silence_
```

- Durasi audio = patokan `DUR`; video = `ceil(DUR*30)` frame.
- Jeda ≥0,40 dtk = batas blok VO → geser cue `slide()`/`cut()` dan array `SUBS`
  supaya kalimat mulai tepat saat panggungnya muncul.
- VO perlu digeser: potong `vo-final.wav` (`atrim` + `aevalsrc=0:d=<jeda>` +
  `concat`), lalu mix ulang.
- `DUR` berubah → `rm frames/<k>/*.jpg` sebelum render (frame sisa bikin ekor).

### 7 — SFX + Score + Mix

Sesuaikan cue di `audio/sfx/<k>/cues.txt` dengan timeline HTML, lalu jalankan:

```bash
./engine audio <k> [dur]     # generate sfx + score + mix ducking -> audio/sfx/<k>/mix.wav
```

### 8 — Verifikasi (jangan render penuh untuk mengecek)

Potret beberapa detik kunci (awal tiap panggung, teks muncul, transisi) untuk cek:
frame wide (<1,08)? kepala/objek terpotong? tokoh lepas di sendi?
teks ketutup UI bawah? subtitle melenceng dari VO?

### 9 — Render + encode

```bash
./engine export <k> <durasi>   # otomatis start server + render frame + encode MP4
# Atau terpisah:
./engine render <k> <durasi>
./engine encode <k>
```

frame = detik × 30. Engine memakai Chrome Headless Shell sequential bawaan Remotion
(sangat aman untuk laptop RAM 4 GB). Encode wajib `-pix_fmt yuv420p -movflags +faststart -shortest`.

### 10 — Caption + log

`caption/<k>/caption.txt`: caption singkat + tepat 5 hashtag. Lalu tambah satu
baris di `konten-log.md` (konten · tanggal · tokoh · latar · angle · layanan ·
durasi · status).

## Checklist serah

- [ ] Tokoh baru; latar & angle beda dari konten sebelumnya (log dicek)
- [ ] 75 % awal tanpa brand/harga/CTA; CTA ≤6 dtk di ekor
- [ ] Ada satu analogi visual konkret yang benar-benar tampil di panggung
- [ ] Durasi sesuai bobot cerita; hook ≤1,5 dtk; tiap adegan berisi
- [ ] Naskah 5 blok, bahasa sopan, angka tidak disingkat
- [ ] Tiap panggung ≥10 benda beraksi; tidak ada zoom <1,08
- [ ] Sendi pakai `J()` + proxy; tidak ada `transformOrigin`/`rotation` GSAP di sendi
- [ ] Subtitle ikut waktu VO (bukan waktu scene), posisi bottom 500 px
- [ ] `DUR` ≥ durasi audio; frame lama dihapus kalau `DUR` berubah
- [ ] Caption + tepat 5 hashtag; log diperbarui
