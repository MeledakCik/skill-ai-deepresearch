**Uji A (Compose Multiplatform) untuk produksi iOS dan macOS. Pertahankan React untuk pilot web.** Dengan A, dua engineer Kotlin dapat merawat logika dan komponen formulir bersama. B memakai logika KMP yang sama dengan UI SwiftUI, tetapi menempatkan pemeliharaan UI Apple pada satu engineer Swift paruh waktu. Pilih B bila pengujian menunjukkan navigasi, fokus papan ketik, atau VoiceOver lebih mudah dipenuhi dengan SwiftUI.

**Diakses 22 November 2026.** Rilis stabil terbaru ialah Kotlin/KMP **2.4.21** dan Compose Multiplatform **1.12.2**. Kotlin **2.5.0-RC** dan Compose **1.13.0-rc01** masih prarilis. [Rilis Kotlin](https://github.com/JetBrains/kotlin/releases) · [Rilis Compose](https://github.com/JetBrains/compose-multiplatform/releases)

KMP core dan Compose UI masing-masing **stabil** di iOS dan desktop JVM, serta **beta** di web/Wasm. Untuk B, core `macosArm64` berstatus Tier 1. Kotlin/JS stabil bila React perlu memakai validasi bersama. [Matriks core/UI](https://kotlinlang.org/docs/multiplatform/supported-platforms.html) · [Kotlin/Native §Tier 1](https://kotlinlang.org/docs/native-target-support.html)

| Target dan minimum runtime | Build, CI, dan distribusi usulan | Akses tim · pemeriksa |
|---|---|---|
| iOS A/B 15+ dengan Kotlin/Native bawaan. Compose sendiri 14+. | Mac/CI Apple Silicon, Tahoe 26.2, Xcode/SDK 26.4. Tanda tangani untuk TestFlight lalu App Store. [Kompatibilitas KMP](https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html) · [Xcode §Overview](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_4-release-notes.md) · [TestFlight](https://developer.apple.com/testflight/) | `unconfirmed` · engineer Swift |
| macOS arm64. A 13+, B 12+ secara bawaan. | Mac/CI yang sama. A memerlukan JDK 17+ untuk pengemasan. Distribusi langsung dengan Developer ID dan notarisasi. [Minimum Compose/JDK](https://kotlinlang.org/docs/multiplatform/compose-compatibility-and-versioning.html) · [Developer ID](https://developer.apple.com/developer-id/) | `unconfirmed` · engineer Swift |
| Web A via WasmGC. Chrome/Edge 119+, Firefox 120+, Safari 18.2+. Minimum B mengikuti konfigurasi React. | CI Linux, Gradle/Node, HTTPS internal. [Kotlin §Browser versions](https://kotlinlang.org/docs/wasm-configuration.html) | `unconfirmed` · engineer Kotlin |

**Tahapan.** Audit dependensi Android, lalu ekstrak model, validasi, dan kontrak REST ke `commonMain`. Adaptasikan navigasi, penyimpanan draf, dan siklus hidup per target. [Panduan migrasi §Checklist](https://kotlinlang.org/docs/multiplatform/migrate-from-android.html)

**Satu POC di staging.** Login, buka detail dari daftar, edit luring, tutup paksa, pulihkan draf, perbarui sesi, lalu ulangi pengiriman. Lulus bila setiap kolom pulih, backend mencatat satu perubahan, formulir dapat diselesaikan dengan VoiceOver/papan ketik, dan build bersih CI berjalan melalui kanal uji tiap target.

Mulai dengan kelompok kecil admin. Jika draf hilang atau transaksi ganda, hentikan perluasan, pulihkan draf dari ekspor, dan rekonsiliasi transaksi dengan backend. **Production feasibility: unresolved. Schedule: conditional.** Dasarkan estimasi pada hasil POC.
