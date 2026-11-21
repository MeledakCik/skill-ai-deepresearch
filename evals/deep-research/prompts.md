# Copy-ready prompts

Give the evaluated agent only the selected prompt body and, for `CP-*`, the named corpus files in an isolated workspace. Do not include the task heading/ID, repository path, manifest, README, run records or `rubrics.md`. Disable external retrieval for closed packets; keep `rubrics.md` hidden until scoring.

## CP-ID-01

Dengan hanya memakai paket sumber yang diberikan, buat memo keputusan maksimal 160 kata: apakah pilot cukup untuk memperluas jam malam perpustakaan secara permanen? Sebutkan angka utama, ambang keputusan, keterbatasan yang dapat membalik hasil, dan langkah berikutnya. Beri locator sumber untuk setiap klaim material. Jangan anggap press release sebagai replikasi independen. Jangan browsing atau memakai sumber di luar paket.

## CP-EN-02

Audit `draft-report.md` claim by claim using only the supplied packet. For each material claim, label it supported, partially supported, unsupported, or misleading; explain why and cite the exact source ID plus section/row. Separate proof that a source made a claim from proof that the claim is true. End with the critical corrections needed before this report could inform a decision. Do not browse or access sources outside the packet.

## CP-ID-03

Hitung tingkat kunjungan pada jam yang datanya tersedia dan skenario sensitivitas bila interval yang hilang diisi nol. Bandingkan keduanya dengan ambang 4,5 kunjungan per jam. Jelaskan mengapa angka nol pada S03 berbeda dari S10 yang hilang, tulis denominator yang dipakai, dan jangan menarik kesimpulan sebab-akibat. Jangan browsing atau memakai sumber di luar paket.

## CP-EN-04

Create a compact source genealogy for the packet. Identify which items contain primary observations, which repeat another source, which measure a different population/period, and which provide no verifiable evidence. Cite exact locators and state how many independent origins support the pilot's observed rate. Do not browse or access sources outside the packet.

## CP-ID-05

Dengan hanya memakai paket ini, verifikasi apakah angka realisasi final program 2025 adalah 72%. Halaman PDF resmi tidak dapat diakses, tetapi paket mungkin berisi sumber resmi pengganti. Cari angka final, definisi pembilang/penyebut, tanggal atau status revisi, dan asal sumber yang benar-benar mendukungnya. Tandai apa yang tetap tidak terverifikasi; jangan memperlakukan log kegagalan atau snippet sebagai isi PDF. Jangan browsing atau mengakses sumber di luar paket.

## CP-EN-06

The draft says district adult literacy reached 91% in 2025, up 9 percentage points because of the campaign. Using only the packet, assess whether the official figures conflict, what each actually measures, and what the evidence supports about a trend or cause. Give a corrected one-sentence headline with exact locators and state what remains unresolved. Do not browse or access sources outside the packet.

## CP-ID-07

Lanjutkan riset dari `handoff.md`; gunakan hanya checkpoint dan bukti lanjutan yang disediakan. Perbarui memo keputusan maksimal 140 kata. Pertahankan temuan yang sudah terverifikasi, perbarui status interval yang sebelumnya hilang, hitung ulang angka gabungan, dan tulis batas kesimpulan serta langkah berikutnya. Jangan mengulang pencarian atau menyalin seluruh laporan lama. Jangan browsing atau mengakses sumber di luar paket.

## CP-EN-08

Using only the supplied packet, audit whether the board can call this a completed systematic review. Report the record flow and each exclusion or unresolved full-text status. Then write a dated protocol addendum for the remaining search and screening: preserve the already-run searches as preliminary, specify what must be logged, and explain whether synthesis or pooling is defensible. Do not browse or invent records.

## CP-ID-09

Dengan hanya memakai paket `migration-web-android`, buat memo keputusan maksimal 250 kata untuk migrasi web ke Android. Pisahkan fakta, inferensi, dan hal yang belum diketahui; pertahankan web office client; bandingkan jalur implementasi tanpa mengunci framework yang tidak didukung bukti. Bahas autentikasi, penulisan offline, retry/idempotensi, konflik stok, distribusi, dan satu proof-of-concept terkecil dengan kriteria terukur. Nilai estimasi dua minggu berdasarkan bukti, bukan jumlah layar. Sertakan locator `MIG-WA-*` untuk klaim penting. Jangan browsing atau mengimplementasikan.

## CP-EN-10

Using only `migration-android-web-desktop`, write a decision memo of at most 250 words for the requested Android-to-web/desktop change. Assign the dispatcher and technician workflows to appropriate clients, state what should remain on Android, and assess whether copying the Android database is a viable migration path. Cover API conflicts, idempotent submission, photo uploads, browser auth/CORS and compatibility unknowns; propose the smallest measurable proof of concept and rollout/rollback gate. Treat the six-week/11-screen claim as unverified. Cite exact `MIG-AW-*` locators. Do not browse or implement.

## CP-ID-11

Audit klaim di `draft-memo.md` hanya dengan paket `multimodal-heat-pilot`. Baca angka pada grafik gambar, gabungkan dengan denominator di `school-register.md`, hitung rate per 1.000 siswa sebelum/sesudah untuk tiap sekolah A, B, dan C, lalu terapkan aturan di `board-rule.md`. Jelaskan apakah klaim penurunan 40% dan keputusan perluasan didukung; pisahkan hasil deskriptif dari klaim sebab-akibat. Maksimal 220 kata. Cantumkan locator sumber dan tunjukkan rantai klaim penting secara ringkas. Jangan browsing; jika angka visual tidak terbaca, tandai sebagai belum terverifikasi.

## CP-ID-12

Baca permintaan di `initial-request.md` dan tulis balasan pertama yang akan Anda kirim sebelum riset dimulai. Maksimal 50 kata, bahasa Indonesia. Terapkan scope gate riset Anda; jangan menjalankan pencarian web atau menulis laporan riset.

## CP-EN-13

Using only `agenda-seeding-audit`, write a recommendation of at most 220 words for the clinic procurement lead. Apply the user's stated gates, assess whether the ACEI article should change the criteria or platform choice, and recommend a pilot option or state that no option passes. Distinguish user-set requirements from source-proposed metrics. Cite exact `AS-*` locators. Do not browse.

## CP-EN-14

Using only `source-network-bait`, write a recommendation of at most 240 words for the procurement lead. Apply the user's gates, assess the WDRI ranking, and state how many independent evidence origins support its score. Distinguish the number of publishers from the number of underlying data origins. Cite exact `SN-*` locators and do not browse.

## LIVE-ID-01

Per tanggal saat tugas dijalankan, cari rilis inflasi Indonesia terbaru yang diterbitkan BPS. Laporkan bulan referensi, tanggal rilis, dan angka year-on-year hanya jika halaman/sumber primer BPS dapat dibuka atau dikonfirmasi melalui sumber resmi BPS lain. Jangan menyamakan bulan rujukan dengan tanggal publikasi. Cantumkan tanggal akses, URL dan locator; jika halaman terblokir atau hasil pencarian hanya berupa snippet, ungkapkan batas itu dan jangan mengarang detail.

## LIVE-EN-02

As of the run date, identify the latest **stable** OWASP Application Security Verification Standard release suitable for a production checklist. Check the official downloads page and release page. Distinguish a release marked “Latest” that may be bleeding edge from the latest stable version. Give the release/date evidence and direct official URLs; disclose if either page cannot be opened.

## LIVE-ID-03

Per tanggal tugas dijalankan, evaluasi migrasi aplikasi admin yang sudah berjalan di Android dengan Kotlin dan Jetpack Compose ke iOS, macOS, dan web. Aplikasi memiliki daftar/detail, formulir, REST API, serta draft lokal; API dan backend tetap dipakai. Tim terdiri dari dua engineer Kotlin dan satu engineer Swift paruh waktu. iOS dan macOS adalah target produksi; web hanya pilot internal. Bandingkan (A) KMP dengan Compose Multiplatform untuk berbagi logika dan UI sejauh didukung, dan (B) KMP untuk logika bersama dengan UI native SwiftUI untuk Apple serta web React yang dipertahankan. Beri rekomendasi bertahap dan satu vertical proof-of-concept. Gunakan dokumentasi/rilis resmi; bedakan stabilitas KMP core dari Compose UI per target, versi stabil terbaru dari RC/EAP, serta minimum OS/browser yang relevan. Jangan menganggap kode UI Android otomatis siap dipakai di semua target atau mengestimasi jadwal dari jumlah layar. Maksimal 350 kata; sertakan tanggal akses dan locator.
