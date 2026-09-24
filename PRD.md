# PRD — Website Portofolio Muhammad Fajar Ariandi

| | |
|---|---|
| **Versi** | 1.1 (tambah foto kedua dan tautan sosial media) |
| **Tanggal** | 24 September 2026 |
| **Pemilik produk** | Muhammad Fajar Ariandi |
| **Status** | Prototipe HTML selesai (`index.html`), menunggu verifikasi konten |
| **Referensi visual** | Poster portofolio bergaya kertas sobek, tipografi tebal, dan coretan tangan (ungu-krem) yang diberikan pemilik |

---

## 1. Ringkasan

Website portofolio satu halaman (single page) yang memperkenalkan Fajar sebagai **IT/Jaringan + Konten Kreator**. Tampilannya meniru gaya poster referensi: judul "PORTFOLIO" raksasa dengan foto menembus huruf, ID card yang berayun di lanyard, kertas sobek, coretan tangan, dan lima "Selected Work" bergaya foto polaroid.

**Masalah yang diselesaikan:** CV PDF saat ini bersifat statis dan tidak menonjolkan sisi kreatif maupun proyek lapangan. Website ini menjadi "kartu nama digital" yang bisa dibagikan lewat satu tautan, dan gambar promosinya dipakai untuk menarik pengunjung.

## 2. Tujuan dan indikator keberhasilan

| Tujuan | Indikator |
|---|---|
| Rekruter/klien paham profil Fajar dalam < 10 detik | Judul, foto, dan label profesi terlihat tanpa scroll |
| Mengarahkan pengunjung menghubungi Fajar | Klik tombol "Hubungi saya" dan WhatsApp/email |
| Menampilkan proyek nyata secara meyakinkan | 5 kartu Selected Work tampil dengan angka konkret dari CV |
| Terasa unik dan berkesan | Animasi pembuka, ID card berayun, kartu jatuh saat di-scroll |
| Ringan dan cepat | Halaman ±1,1 MB, tanpa dependensi eksternal |

**Non-tujuan (versi 1):** blog, CMS, login, multi-bahasa, form kontak dengan backend.

## 3. Target pengguna

1. **Rekruter dan HRD** perusahaan jaringan, CCTV, ISP, dan logistik yang menilai kelayakan kandidat.
2. **Kontraktor/vendor proyek** yang mencari tenaga instalasi lapangan (CCTV, Starlink, LAN).
3. **Klien konten** yang membutuhkan editing (Canva, CapCut, Lightroom).

## 4. Positioning dan pesan utama

- **Label:** IT/Jaringan & Konten Kreator
- **Tagline doodle:** koneksi · kreasi · konten
- **Kutipan utama:** "Jaringan yang stabil membuat semuanya jalan, konten yang rapi membuatnya terlihat."
- **Bukti:** ±260 unit CCTV, 53 switch + 53 router, 795 PVR sekolah, 6 lokasi SPPG (semua dari CV).

## 5. Ruang lingkup fitur

| # | Fitur | Prioritas |
|---|---|---|
| F1 | Hero: judul PORTFOLIO, foto cutout bergaya stiker, label profesi, navigasi | Wajib |
| F2 | ID card + lanyard yang berayun | Wajib |
| F3 | Tentang saya + kutipan ber-highlight | Wajib |
| F4 | Skill & tools (8 ikon) | Wajib |
| F5 | Pengalaman (5 entri, terbaru di atas) | Wajib |
| F6 | Kontak (email, WhatsApp, lokasi) dengan tautan aktif | Wajib |
| F6b | Sosial media: Instagram, TikTok, LinkedIn, GitHub (tautan aktif, buka di tab baru) | Wajib |
| F6c | Foto full body (cutout stiker) di bagian Tentang saya | Wajib |
| F7 | Selected Work: 5 kartu polaroid bernomor | Wajib |
| F8 | Navigasi anchor (Tentang, Skill, Pengalaman, Karya, Hubungi saya) | Wajib |
| F9 | Responsif desktop, tablet, mobile | Wajib |
| F10 | Detail proyek (modal/halaman) dengan foto lapangan asli | Fase 2 |
| F11 | Unduh CV (PDF) | Fase 2 |

## 6. Sistem desain

### 6.1 Warna

| Token | Hex | Pemakaian |
|---|---|---|
| `--paper` | `#F6F3EC` | Latar kertas krem |
| `--indigo` | `#4636B8` | Huruf PORTFOLIO, latar Selected Work |
| `--indigo-2` | `#3A2CA3` | Judul seksi, garis pemisah |
| `--ink` | `#15112E` | Teks, bayangan keras, label |
| `--lav` | `#D9D2F7` | Highlight kutipan, latar foto ID card |
| Aksen kapur | `#E6FF5A` `#FFB14A` `#FF5C6C` `#A78BFF` | Nomor 1–5, ikon tools |

### 6.2 Tipografi

| Peran | Font | Catatan |
|---|---|---|
| Judul raksasa, label, poster kartu | **Bowlby One** | Bayangan keras offset 0.045em warna `#17123F` |
| Judul seksi, nama, nomor | **Caveat Brush** | Bergaya kuas tangan |
| Isi teks | **Patrick Hand** | 20–23 px, panjang baris < 80 karakter |

Semua font di-embed (base64) agar tampil sama tanpa koneksi ke Google Fonts.

### 6.3 Elemen visual khas

- Tepi kertas sobek (SVG ber-fringe + bayangan) antar seksi
- Grain kertas halus (SVG noise)
- Foto cutout dengan outline putih + indigo (efek stiker)
- Coretan tangan: elips teks, bintang, panah, smiley, mahkota, pesawat kertas
- Selotip dan klip kertas pada kartu

## 7. Struktur halaman

```
┌──────────────────────────────────────────────┐
│ [lanyard]   (koneksi kreasi konten)  nav ▸ CTA│
│    ┃        P O R T F O L I O  (foto menembus)│
│    ┃                 [IT/JARINGAN & KONTEN…]  │
│ ~~~┃~~~~~~~~~~~~~~~ kertas sobek ~~~~~~~~~~~~ │
│  [ID card]   Tentang saya ↷   bio    [foto   │
│              + highlight kutipan      full   ]│
│ ─────────────────────────────────────────────│
│  Skill & tools │ Pengalaman     │ Kontak +    │
│                │                │ Ikuti saya  │
│ ~~~~~~~~~~~~~~ kertas sobek ungu ~~~~~~~~~~~~~│
│              Selected Work 👑                 │
│  ①CCTV  ②Starlink  ③Switch  ④PVR  ⑤SPPG      │
│  [catatan]                       [catatan]    │
└──────────────────────────────────────────────┘
```

## 8. Spesifikasi konten

### 8.1 Data profil (dari CV, mohon diverifikasi)

- **Nama:** Muhammad Fajar Ariandi
- **Lokasi:** Tangerang, Indonesia
- **Email:** Fajarariandi669@gmail.com
- **WhatsApp:** +62 882 1340 0530 (tautan `wa.me/6288213400530`)
- **Pendidikan:** SMK Fadilah, Otomotif, 2019–2021

### 8.1b Sosial media (diberikan pemilik)

| Platform | Handle tampil | Tautan |
|---|---|---|
| Instagram | @fjrarndii_ | https://www.instagram.com/fjrarndii_ |
| TikTok | @fajardev.ai | https://www.tiktok.com/@fajardev.ai |
| LinkedIn | Fajar Ariandi | https://www.linkedin.com/in/fajar-ariandi-90ba5a21a/ |
| GitHub | fajarariandi17 | https://github.com/fajarariandi17 |

Semua tautan memakai `target="_blank"` dan `rel="noopener noreferrer"`. Ditampilkan di kolom Kontak di bawah subjudul "Ikuti saya", dan dicantumkan juga pada gambar promosi.

### 8.1c Aset foto

| Foto | Pemakaian | Perlakuan |
|---|---|---|
| Portrait berlatar merah | Hero (menembus huruf PORTFOLIO) dan ID card | Background dihapus, dipotong sebatas dada, outline putih + indigo |
| Berdiri di zebra cross (full body) | Bagian Tentang saya (kanan) | Background dihapus, dipotong pas badan, outline stiker, miring 3° dan jatuh saat di-scroll |

### 8.2 Pengalaman (terbaru di atas)

| Periode | Peran | Perusahaan |
|---|---|---|
| Nov 2025 – Jan 2026 | Field Installation & Tim Staging | Project IoT BGN – PERURI, Karawang |
| Sep 2024 – Mei 2025 | Driver | PT. Darun Raynor Istafajar |
| Feb 2024 – Agu 2024 | Teknisi Instalasi Starlink | PT. Fiber Star, Jakarta Selatan |
| Jan 2023 – Des 2023 | Staff Gudang | J&T Express, Ciputat |
| Mar 2022 – Sep 2022 | Office Boy | PT. Cahaya Berkat Anugrah |

### 8.3 Skill & tools

Mikrotik, Kali Linux, Python, HTML & CSS, Canva, CapCut, Lightroom, MS Office. Tambahan (teks): crimping UTP/RJ-45, konfigurasi DHCP CCTV, instalasi Windows, Bahasa Inggris pasif.

### 8.4 Selected Work (5 kartu)

| No | Judul kartu | Angka/Isi | Sumber di CV |
|---|---|---|---|
| 1 | CCTV ±260 Unit | Hiview & Skyview, staging & instalasi | Project IoT BGN–PERURI |
| 2 | Instalasi Starlink | Instalasi + speed test | PT. Fiber Star |
| 3 | Switch & Router | 53 unit masing-masing | Project IoT BGN–PERURI |
| 4 | PVR & Digital Signage | 795 PVR sekolah, 53 digital signage | Project IoT BGN–PERURI |
| 5 | 6 Lokasi SPPG | Penarikan kabel LAN & crimping RJ-45 | Project IoT BGN–PERURI |

## 9. Spesifikasi animasi

Prinsip: satu momen pembuka yang berkesan, sisanya hemat. Semua animasi mati bila `prefers-reduced-motion` aktif.

| Elemen | Pemicu | Efek | Durasi |
|---|---|---|---|
| Huruf PORTFOLIO | Muat halaman | Jatuh dari atas dengan pantulan, berurutan (70 ms/huruf) | ~0,8 s + jeda |
| Foto profil | Muat halaman (+0,85 s) | Naik dan muncul dengan overshoot | 0,9 s |
| Label profesi | Muat halaman (+1,6 s) | Efek cap/stempel (skala 2,2 → 1) | 0,5 s |
| Elips "koneksi kreasi konten" | Muat halaman (+2 s) | Digambar (stroke-dashoffset) | 1,6 s |
| Pesawat kertas | Loop | Terbang persis di atas jalur titik-titik (jejak dan pesawat memakai satu koordinat yang sama, hidung pesawat selalu searah lintasan) lewat CSS `offset-path`, lalu memudar di ujung | 9 s |
| ID card + lanyard | Loop | Berayun ±1,2° dari titik gantung | 6 s |
| Highlight kutipan | Masuk viewport | Tersapu kiri ke kanan | 1 s |
| Daftar pengalaman | Masuk viewport | Muncul berurutan dari kiri | 0,5 s/entri |
| 5 kartu Selected Work | Masuk viewport | Jatuh dan menempel dengan miring acak (140 ms/kartu) | 0,9 s |
| Foto full body | Masuk viewport | Jatuh dari bawah dengan miring, lalu lurus saat di-hover | 0,9 s |
| Hover kartu | Hover | Lurus, naik 10 px, nomor berputar | 0,35 s |
| Hover ikon tools / kontak | Hover | Melompat/berputar kecil | 0,25 s |
| Ilustrasi kartu | Loop | LED CCTV berkedip, sinyal Starlink berdenyut, LED switch, tombol play | 1–2 s |

## 10. Kebutuhan teknis

- **Stack:** HTML + CSS + JavaScript murni dalam satu file (tanpa framework, tanpa build). Ukuran ±1,1 MB karena font dan foto di-embed.
- **Aset foto:** cutout dari foto berlatar merah (background dihapus), lalu dipotong sebatas dada.
- **Kompatibilitas:** Chrome, Edge, Safari, Firefox versi terbaru. `offset-path` (pesawat) adalah peningkatan progresif: bila tidak didukung, pesawat tidak tampil.
- **Breakpoint:** ≥ 1101 px (desktop), 761–1100 px (tablet, lanyard disembunyikan, kartu 3 kolom), ≤ 760 px (mobile, judul dua baris PORT / FOLIO, kartu 2 kolom).
- **Hosting yang disarankan:** GitHub Pages, Netlify, atau Vercel (gratis) dengan domain kustom opsional.

## 11. Aksesibilitas, SEO, dan kinerja

- Kontras teks memenuhi WCAG AA; fokus keyboard terlihat (outline indigo 3 px)
- Semantik: `<header>`, `<nav>`, `<section>`, `<h1>` tunggal (dengan `aria-label`), `role="img"` dan `aria-label` pada foto dan poster kartu
- Dekorasi bertanda `aria-hidden`
- Meta `title`, `description`, `lang="id"`; tambahkan Open Graph (gambar promosi sebagai `og:image`) saat deploy
- Target Lighthouse: Performance ≥ 90, Accessibility ≥ 95

## 12. Rencana rilis

| Tahap | Isi | Status |
|---|---|---|
| 0 | Riset referensi dan ekstraksi data dari CV | Selesai |
| 1 | Prototipe halaman lengkap + gambar promosi | Selesai |
| 2 | Verifikasi konten oleh pemilik (bagian 13) | **Menunggu** |
| 3 | Revisi, isi tautan sosial, foto proyek asli | Berikutnya |
| 4 | Deploy, domain, Open Graph, uji Lighthouse | Berikutnya |

## 13. Poin verifikasi untuk pemilik

1. Apakah nomor WhatsApp dan email di atas sudah benar dan boleh dipublikasikan?
2. Apakah semua angka proyek (±260 CCTV, 53, 795, 6 lokasi) boleh ditampilkan publik? Beberapa proyek mungkin terikat kerahasiaan klien.
3. Apakah kelima pengalaman ditampilkan semua, atau hanya yang relevan (misalnya tanpa Office Boy)?
4. Apakah handle sosial media sudah benar (Instagram @fjrarndii_, TikTok @fajardev.ai, LinkedIn, GitHub fajarariandi17)? Isi akun sebaiknya sudah rapi dan profesional sebelum dipublikasikan.
5. Apakah kartu nomor 5 (SPPG) ingin diganti dengan hasil editing/konten (Canva, CapCut, Lightroom) agar sisi kreator lebih menonjol?
6. Ada nama domain yang diinginkan?

## 14. Risiko dan mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Data proyek bersifat rahasia | Masalah dengan klien | Verifikasi poin 13.2, samarkan nama bila perlu |
| Ilustrasi kartu bukan foto asli | Kurang meyakinkan | Fase 2: ganti dengan foto lapangan asli |
| Animasi berat di HP lawas | Patah-patah | Hanya `transform`/`opacity`, hormati reduced motion |
| Foto cutout kurang rapi di tepi rambut | Terlihat kasar | Ekspor ulang dengan model penghapus latar yang lebih halus bila perlu |
| Foto full body memuat logo merek pada kaus | Bisa dianggap kurang netral untuk profil profesional | Pertimbangkan foto dengan pakaian polos bila ingin lebih formal |
