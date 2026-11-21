**Fakta**

Web kantor harus tetap berfungsi. Armada memakai Android 10+, dengan distribusi melalui Managed Play (`MIG-WA-BRIEF` §1). Login web memakai cookie sesi dan token CSRF (`MIG-WA-REPO` §2). Muat ulang menghapus isian. Dari 40 laporan sif, 14 menyebut gangguan jaringan dan delapan menyebut entri ulang. Jumlah duplikat belum diketahui (`MIG-WA-OPS` §§1–2). API memerlukan koneksi untuk mencatat penerimaan. PostgreSQL menjadi acuan stok. Kontrak tidak mendokumentasikan kunci idempotensi (`MIG-WA-API` §§1–2).

**Inferensi dan keputusan**

Pertahankan web kantor dan kompatibilitas API. Batasi tahap awal Android pada penerimaan satu SKU. Membungkus web berpeluang menggunakan kembali formulir. Klien Android terpisah memerlukan formulir baru, tetapi dapat mengelola pemindai dan penyimpanan lokal sendiri. Kedua jalur memerlukan antrean persisten dan deduplikasi di server saat pengiriman diulang. Pilihan framework masih terbuka (`MIG-WA-REPO` §1, `MIG-WA-API` §§1–3).

**Belum diketahui**

Verifikasi alur login Android, penanganan sesi kedaluwarsa saat sinkronisasi, keamanan data lokal, aturan konflik stok untuk SKU yang sama, serta akses akun dan proses peninjauan Managed Play (`MIG-WA-REPO` §2, `MIG-WA-API` §§2–3, `MIG-WA-OPS` §2).

**PoC dan estimasi**

Dua perangkat memindai SKU yang sama saat luring, masing-masing menerima dua dan tiga unit. Tutup paksa aplikasi, buka kembali, lalu sinkronkan. Putuskan respons setelah transaksi tersimpan dan ulangi dengan ID semula. Lulus bila 10/10 percobaan memulihkan kedua entri, mencatat tepat dua penerimaan, dan menambah stok lima unit di web kantor.

Estimasi dua minggu belum terukur. Sembilan layar tidak mengukur pekerjaan sinkronisasi, autentikasi, atau rilis. Estimasi ulang berdasarkan hasil PoC dan rincian pekerjaan tersisa (`MIG-WA-BRIEF` §1, `MIG-WA-REPO` §§2–3).
