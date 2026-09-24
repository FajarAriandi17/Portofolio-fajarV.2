# Foto

Folder aset foto untuk website.

## Foto profil (header CV)
- **`portrait.png`** — dipakai di header `cv.html`. Ganti berkas ini (nama sama) untuk memperbarui foto CV.

## Foto lapangan proyek (modal "Selected Work")
Tiap kartu proyek punya slot foto di dalam modal detailnya. Cukup letakkan berkas dengan nama berikut, lalu foto otomatis muncul menggantikan ilustrasi poster (tanpa perlu ubah kode):

| Berkas | Kartu / Proyek |
|---|---|
| `proyek-1.jpg` | CCTV ±260 Unit |
| `proyek-2.jpg` | Instalasi Starlink |
| `proyek-3.jpg` | Switch & Router |
| `proyek-4.jpg` | PVR & Digital Signage |
| `proyek-5.jpg` | 6 Lokasi SPPG |

**Saran:** foto lanskap (mis. 1200×900), < 300 KB per foto. Format `.jpg`. Jika berkas tidak ada, modal tetap menampilkan ilustrasi poster + catatan slot (tidak error).

Setelah menambahkan foto: `git add img/ && git commit -m "add foto lapangan" && git push`.
