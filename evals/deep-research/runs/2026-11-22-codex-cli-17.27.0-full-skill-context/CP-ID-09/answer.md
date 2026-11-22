**Keputusan (inferensi).** Pertahankan web kantor. Uji satu alur Android, yaitu penerimaan barang. Pembungkus React berpotensi memakai ulang formulir. Klien Android khusus memerlukan UI baru dan dapat mengintegrasikan pemindai langsung. Keduanya memerlukan antrean persisten. Tunda pemilihan framework. (MIG-WA-BRIEF §1, MIG-WA-REPO §1)

**Fakta.** Web memakai cookie sesi *same-site* dan token CSRF. Muat ulang menghapus isian. Dari 40 laporan sif di tiga gudang, 14 menyebut gangguan jaringan dan delapan menyebut entri ulang. Jumlah duplikat belum diukur. API penerimaan memerlukan koneksi. PostgreSQL menjadi acuan stok dan penerimaan. (MIG-WA-OPS §§1–2, MIG-WA-REPO §2, MIG-WA-API §§1–2)

**Belum diketahui.** Alur autentikasi Android, hasil retry setelah respons hilang, dan aturan konflik stok. Kontrak belum mendokumentasikan kunci idempotensi. (MIG-WA-REPO §2, MIG-WA-API §§1–3)

| Target | Toolchain dan host | Akses tim dan distribusi |
|---|---|---|
| Android 10+ | SDK, mesin build dan runner CI belum terverifikasi | `unconfirmed`. Penanggung jawab rilis perlu memverifikasi akses penandatanganan dan akun Managed Play perusahaan. (MIG-WA-BRIEF §1, MIG-WA-REPO §§1–2) |

**PoC terkecil.** Pasang build bertanda tangan melalui Managed Play di Android 10. Masuk, pindai SKU luring (+2), lalu tutup paksa aplikasi. Saat dibuka kembali, satu transaksi harus tetap tertunda. Autentikasi ulang saat sesi kedaluwarsa. Sinkronkan bersamaan dengan penerimaan web (+3) untuk SKU yang sama. Hilangkan respons setelah server mencatat transaksi, lalu kirim ulang memakai ID semula. Lulus jika kedua penerimaan masing-masing tercatat sekali, stok naik tepat lima, dan antrean kosong.

**Kelayakan produksi belum pasti. Jadwal bersyarat.** Sembilan layar belum mendukung estimasi dua minggu. Ukur pekerjaan autentikasi, sinkronisasi, pengujian dan rilis melalui PoC sebelum menetapkan tanggal. (MIG-WA-BRIEF §1, MIG-WA-REPO §3)
