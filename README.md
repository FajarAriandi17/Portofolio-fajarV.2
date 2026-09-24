# Portofolio — Muhammad Fajar Ariandi

Website portofolio satu halaman bergaya **poster kertas sobek** yang memperkenalkan Fajar sebagai IT/Jaringan & Konten Kreator.

- **Nama:** Muhammad Fajar Ariandi
- **Peran:** Teknisi Jaringan, CCTV, Starlink · Konten Kreator (Canva, CapCut, Lightroom)
- **Lokasi:** Tangerang, Indonesia

## URL

- **Produksi (GitHub Pages):** https://fajarariandi17.github.io/Portofolio-fajarV.2/
- **Repositori:** https://github.com/FajarAriandi17/Portofolio-fajarV.2

### Cara mengaktifkan (sekali saja, ~30 detik)

1. Buka repo → **Settings** → **Pages**
2. **Source:** pilih `Deploy from a branch`
3. **Branch:** pilih `main`, folder `/ (root)` → **Save**
4. Tunggu ±1 menit, situs langsung tayang di URL produksi di atas.

Setiap `git push` ke `main` berikutnya akan otomatis memperbarui situs.

## Fitur yang sudah selesai

| Kode | Fitur | Status |
|---|---|---|
| F1 | Hero: judul PORTFOLIO raksasa, foto cutout menembus huruf, label profesi, navigasi | ✅ |
| F2 | ID card + lanyard berayun (±1,2°, loop 6 s) | ✅ |
| F3 | Tentang saya + kutipan ber-highlight tersapu | ✅ |
| F4 | Skill & tools (8 ikon interaktif) | ✅ |
| F5 | Pengalaman (5 entri, muncul berurutan) | ✅ |
| F6 | Kontak: email, WhatsApp, lokasi (tautan aktif) | ✅ |
| F6b | Sosial media: Instagram, TikTok, LinkedIn, GitHub | ✅ |
| F6c | Foto full body cutout di bagian Tentang saya | ✅ |
| F7 | Selected Work: 5 kartu polaroid bernomor, animasi jatuh | ✅ |
| F8 | Navigasi anchor + smooth scroll | ✅ |
| F9 | Responsif desktop / tablet / mobile | ✅ |
| F10 | Detail proyek: 5 kartu Selected Work bisa diklik → modal detail (aksesibel) | ✅ |
| F11 | Tombol unduh CV + halaman `cv.html` siap-cetak (Simpan sebagai PDF) | ✅ |
| — | Open Graph + Twitter Card + `og-image.jpg` | ✅ |
| — | Favicon + apple-touch-icon | ✅ |
| — | Structured data JSON-LD (`schema.org/Person`) | ✅ |
| — | `.nojekyll` agar Pages menyajikan berkas apa adanya | ✅ |

## Entri fungsional (anchor)

| Path | Bagian |
|---|---|
| `/` atau `/#top` | Hero (judul, foto, label profesi) |
| `/#tentang` | Tentang saya + kutipan + foto full body |
| `/#skill` | Skill & tools |
| `/#pengalaman` | Riwayat pengalaman kerja |
| `/#kontak` | Kontak & sosial media |
| `/#karya` | Selected Work (5 kartu, klik untuk detail) |
| `/cv.html` | CV siap-cetak (tombol “Simpan sebagai PDF”) |
| `/?static` | Mode tanpa animasi (untuk screenshot / pengujian) |
| `/og-image.jpg` | Gambar pratinjau saat dibagikan |

## Belum dikerjakan (Fase 2)

| Kode | Fitur |
|---|---|
| — | Ganti ilustrasi SVG kartu dengan foto proyek asli (slot foto sudah disiapkan di dalam modal) |
| — | Domain kustom |
| — | Verifikasi konten oleh pemilik (lihat bagian 13 PRD) |

## Langkah berikutnya yang disarankan

1. Aktifkan GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root** (sekali saja).
2. Verifikasi poin di PRD bagian 13 — terutama apakah angka proyek (±260 CCTV, 53, 795, 6 lokasi) boleh dipublikasikan.
3. Ganti ilustrasi SVG kartu Selected Work dengan foto lapangan asli agar lebih meyakinkan (slot foto sudah tersedia di dalam modal detail).
4. Ganti isi `cv.html` bila ada CV terbaru, atau tetap pakai versi ini lalu “Simpan sebagai PDF”.
5. Uji Lighthouse (target: Performance ≥ 90, Accessibility ≥ 95).

## Arsitektur data

- **Model data:** Tidak ada. Seluruh konten bersifat statis dan ditulis langsung di `index.html`.
- **Layanan penyimpanan:** Tidak ada database. Tidak ada backend, tidak ada form yang mengirim data.
- **Alur data:** Pengunjung memuat satu berkas HTML → font, foto, dan ikon sudah ter-*embed* sebagai data-URI → tidak ada permintaan jaringan tambahan. Kontak dilakukan lewat tautan keluar (`mailto:`, `wa.me`, sosial media).

## Panduan pemakaian

**Untuk pengunjung:** buka tautan produksi, gulir dari atas ke bawah, lalu klik tombol **Hubungi saya** atau ikon kontak di bagian Kontak.

**Untuk pemilik (mengubah isi):**
1. Buka `index.html` — seluruh konten ada di dalam `<body>`, terbagi jelas dengan komentar `<!-- HERO -->`, `<!-- ABOUT -->`, dst.
2. Ubah teks langsung di HTML, simpan, lalu `git push`. Pages akan ter-deploy otomatis.
3. Bila mengganti foto atau teks OG image, jalankan ulang:
   ```bash
   python3 tools/make_og.py
   ```

**Menjalankan lokal:**
```bash
npx serve . -l 3000     # lalu buka http://localhost:3000
```
Atau cukup buka `index.html` langsung di browser (tidak butuh server).

## Struktur berkas

```
.
├── index.html            # Seluruh situs: HTML + CSS + JS + font & foto ter-embed
├── cv.html               # CV siap-cetak (Simpan sebagai PDF lewat browser)
├── og-image.jpg          # Gambar pratinjau 1200×630 untuk media sosial
├── favicon.ico
├── apple-touch-icon.png
├── tools/make_og.py      # Regenerasi og-image & favicon dari aset di index.html
├── .nojekyll             # Nonaktifkan pemrosesan Jekyll di GitHub Pages
├── PRD.md                # Dokumen kebutuhan produk
└── README.md
```

## Aksesibilitas & performa

- Satu `<h1>` dengan `aria-label`, tag semantik (`<header>`, `<nav>`, `<section>`, `<main>`)
- Dekorasi bertanda `aria-hidden`, foto dan poster kartu punya `role="img"` + `aria-label`
- Fokus keyboard terlihat (outline indigo 3 px)
- Seluruh animasi mati bila `prefers-reduced-motion: reduce` aktif
- Animasi hanya memakai `transform` dan `opacity` agar mulus di HP
- Nol dependensi eksternal — tanpa CDN, tanpa Google Fonts, tanpa framework

## Deployment

- **Platform:** GitHub Pages (deploy dari branch `main`)
- **Status:** ✅ Terunggah — tinggal aktifkan Pages di Settings
- **Tech stack:** HTML + CSS + JavaScript murni, satu berkas, tanpa build
- **Ukuran halaman:** ±1,2 MB (font & foto ter-embed, dimuat sekali lalu di-cache)
- **Terakhir diperbarui:** 24 September 2026

---

© 2026 Muhammad Fajar Ariandi · Tangerang
