---
name: kentang-motion
description: Engine & workflow produksi motion graphic video pendek 9:16 (Reels/TikTok/Shorts) dengan gaya animasi kartun ekspresif (terinspirasi Kok Bisa) + performa marketing konversi tinggi. Memakai HTML + SVG + GSAP yang dirender frame-by-frame secara sekuensial lewat Chrome Headless Shell + FFmpeg agar lancar di laptop kentang (RAM 4GB). Gunakan skill ini setiap kali membuat video vertikal, explainer pendek, hook video viral, animasi kartun edukasi/marketing, atau ketika user meminta "bikin konten", "konten baru", "konten-N", "naskah vo", atau "render video".
---

# Kentang Motion — Engine Kartun Marketing 9:16

**Kok Bisa Energy × Marketing Conversion × Kentang Hardware Stability.**

Skill ini adalah evolusi dari *kartun panggung*: membuang kekakuan visual jurnalisme korporat, menggantinya dengan **energi kartun ekspresif, metafora visual absurd, dan struktur marketing video pendek** yang dirancang untuk menahan jempol penonton (*stop-scroll*) dan mengonversi di akhir video.

Semua gerak dibangun dengan **vektor SVG + GSAP**, dirender per frame secara deterministik oleh `./engine` (Chrome Headless Shell + FFmpeg) tanpa risiko laptop overheat atau kehabisan RAM.

---

## 1. Formula Cerita Marketing (Kok Bisa Style)

Setiap video berdurasi **20–40 detik** dengan struktur 5 babak:

| Babak | Durasi | Tujuan | Gaya Visual & Narasi |
|---|---|---|---|
| **1. Reverse Hook** | 0–2.5 dtk | Stop-scroll instan | **Pertanyaan terbalik / premis absurd.** *"Cara paling cepat bikin tokomu disita Satpol PP!"* Objek visual langsung kena bencana komikal. |
| **2. Bencana Nyata** | 2.5–10 dtk | Bangun urgensi & relatabilitas | Tokoh mengalami masalah konkret (bukan konsep abstrak). Surat somasi raksasa turun, toko berguncang, uang beterbangan. |
| **3. Metafora Edukatif** | 10–22 dtk | Membongkar mitos & memberi insight | **Satu metafora visual literal yang digambar:** Bisnis tanpa PT = gedung di atas agar-agar goyang. Merek tanpa DJKI = plang toko diganti orang lain. |
| **4. Solusi Heroik** | 22–32 dtk | Brand hadir sebagai penyelamat | Layanan (Veralex) masuk meredakan masalah. Portal tracking menyala, stempel resmi hijau mengunci gedung jadi beton kokoh. |
| **5. CTA Tajam** | 32–38 dtk | Konversi tanpa bertele-tele | 1 kalimat ajakan tindakan konkret + kartu kontak jelas (WhatsApp/Web). |

> **Hukum Marketing 75%:** 75% awal adalah murni hiburan edukatif penonton. Brand hanya muncul di 25% terakhir sebagai *jawaban atas masalah*, bukan jualan dari awal.

---

## 2. Hukum Animasi Anti-Kaku (Bouncy & Expressive)

Di video pendek, musuh utama adalah gambar yang diam atau gerak linear kaku. Terapkan prinsip kartun ini di GSAP:

### A. Physics Bouncy (Pop-In & Slam)
- Jangan pernah pakai `ease: "power1.out"` atau linear untuk objek baru.
- Gunakan `ease: "back.out(2)"` untuk objek yang meletup (*pop-in*).
- Gunakan `ease: "elastic.out(1, 0.4)"` untuk benda lentur (papan, plang toko, stempel jatuh).
- Objek berat (stempel penolakan, palu, brankas) jatuh cepat `power4.in`, lalu tanah/panggung **berguncang** (screen shake 3–4 cycle cepat).

```javascript
// Contoh Pop-in Bouncy
tl.fromTo(element, 
  { scale: 0, opacity: 0 }, 
  { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }
);
```

### B. Squash and Stretch
Saat karakter atau objek mendarat atau kaget:
- Gepengkan dulu (`scaleX: 1.25, scaleY: 0.75`), lalu membal kembali (`scaleX: 1, scaleY: 1`).
- Kepala memanjang saat kaget mendadak (`scaleX: 0.85, scaleY: 1.25`).

### C. Karikatur Ekspresi Wajah Ekstrem
Bukan cuma senyum/sedih biasa:
- **Kaget (Shock):** Mata melotot keluar lingkar kepala (`CI(x, y, 16, '#FFF')`), mulut elips vertikal besar, titik keringat muncrat ke kiri-kanan.
- **Panik (Panic):** Kepala geleng cepat (`rot(head, t, 12, 0.08, yoyo: true)`), alis miring ekstrem, tanda seru `!` merah membal di atas kepala.
- **Lega (Relief):** Mata tertutup garis lengkung bahagia, semburat blush pipi naik, desah napas putih keluar.

### D. Aksesoris Kartun Komikal
Tambahkan micro-animations di sekeliling adegan:
- **Dust Puff (Asap Lari):** 3 lingkaran putih mengecil saat objek bergerak cepat.
- **Dizzy Stars (Bintang Pusing):** 3 bintang kuning berputar di atas kepala saat kena tolak/bencana.
- **Speed Lines:** Garis-garis putih tipis horizontal saat karakter lari atau panik.

---

## 3. Komposisi 9:16 & Safe Zone Layar HP

Layar Reels/TikTok/Shorts dipenuhi tombol antarmuka:
- **Zona Terlarang Atas (0–280px):** Search bar, tombol Back, nama audio.
- **Zona Terlarang Kanan (900–1080px):** Tombol Like, Comment, Share, Remix.
- **Zona Terlarang Bawah (1440–1920px):** Nama akun, caption panjang, tombol sound.

### Standar Koordinat Panggung 1080×1920:
- **Fokus Karakter / Objek Utama:** `Y = 750 – 1250` (Tengah panggung).
- **Subtitles:** **Wajib `bottom: 500px`** (atau `Y = 1380`), teks tebal `Nunito 600–800`, ukuran `38–44px`, 3-lapis drop-shadow hitam tebal agar kontras di latar warna apa pun.
- **Judul/Headline Panggung:** `Y = 360 – 480`.

---

## 4. Sound Design Ceria (Audio Playful)

Video kartun mati rasa tanpa sound effect yang selaras:

1. **Backsound (BGM):**
   - Nada ceria, rasa ingin tahu (*playful, curious*), tempo 75–85 BPM.
   - Pilihan instrumen: Marimba, pizzicato strings, pluck akustik, bassline membal.
   - **Wajib di-ducking otomatis** di bawah narasi VO (turun -14dB saat narator bicara, naik saat ada jeda adegan).

2. **Sound Effects (SFX) per Event:**
   - Objek jatuh / stempel: `thud` / `slam` berat komikal.
   - Transisi / kamera geser: `whoosh` udara cepat.
   - Ide muncul / centang benar: `ding` lonceng / glockenspiel tinggi.
   - Objek meletup / kartu keluar: `pop` gelembung / gabus botol.
   - Kesalahan / tolak: `buzzer` tet-tot komikal / `record scratch`.

---

## 5. Alur Kerja Produksi KentangMotion (5 Langkah)

Setiap episode diproduksi secara disiplin:

```bash
# 1. Bikin folder konten
./engine new konten-N-YYYY-MM-DD

# 2. Susun naskah VO (5 blok, hook terbalik, analogi konkret)
# Simpan di voiceovernaskahai/<k>/naskah-vo.txt
# Generate VO di ElevenLabs -> simpan di audio/voiceover/<k>/

# 3. Bangun visual HTML (simpenhtml/<k>/index.html)
# Pakai template SVG + GSAP, terapkan prinsip Bouncy & Metafora

# 4. Generate Audio (SFX + Backsound + Mix ducking)
./engine audio <k> <durasi>

# 5. Export MP4 (Render sekuensial aman untuk RAM 4GB + Encode FFmpeg)
./engine export <k> <durasi>
```

---

## 6. Checklist Verifikasi Sebelum Rilis

- [ ] **Hook ≤ 2 detik:** Apakah ada kata atau visual yang langsung bikin kaget / penasaran di 2 detik awal?
- [ ] **Metafora Visual:** Apakah ada benda kartun literal (bukan cuma orang pegang kertas/laptop)?
- [ ] **Bouncy Easing:** Apakah objek masuk membal (`back.out` / `elastic`), bukan geser kaku?
- [ ] **Safe Zone Subtitle:** Apakah subtitle berada di `bottom: 500px` dan tidak terpotong UI TikTok?
- [ ] **Audio Mix:** Apakah narasi terdengar jelas di atas BGM (BGM ter-ducking rapi)?
- [ ] **Jualan di Ekor:** Apakah nama brand baru keluar di 25% terakhir durasi video?
