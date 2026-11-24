# deep-research-domain-council

Skill agent AI untuk **riset mendalam setingkat peneliti senior**, dilengkapi dewan spesialis lintas bidang: penulisan akademik S1–S3, desain web anti-slop, Android, full-stack, keamanan, produksi video AI, dan penghematan token.

| | |
|:---|:---|
| **Versi** | 17.28.0 |
| **Format** | 16 skill fokus di `skills/`, dibangun oleh `scripts/sync.py` untuk format Agent Skills |
| **Kompatibel** | Claude Code, Claude.ai, OpenAI Codex, ChatGPT, Gemini CLI, Gemini app, GitHub Copilot, OpenCode, Cursor, Windsurf, Cline, Roo Code, DeepSeek, API LLM apa pun |
| **Lisensi** | MIT |
| **Penulis** | kasyaf-anugrah |

---

## Pilihan skill

Pilih skill berdasarkan hasil yang ingin dibuat. Panduan inti cukup untuk memulai. Referensi berisi contoh dan prosedur yang bisa dibuka saat diperlukan.

| Skill | Dipakai untuk |
|:---|:---|
| `deep-research-council` | Riset mendalam, literature review, brief keputusan, cek fakta (`deep research: …`) |
| `platform-migration` | Riset kelayakan dan rencana migrasi produk lintas web, Android, iOS, desktop, dan macOS |
| `research-data-analysis` | Audit data, analisis statistik, estimasi, sensitivitas dan sintesis kuantitatif |
| `application-security` | Threat model dan secure code review untuk aplikasi web/API |
| `software-testing` | Strategi tes, implementasi, review dan diagnosis tes flaky lintas stack |
| `web-ui-design` | Riset desain, ritme baca, grid responsif, warna terang/gelap, pengujian hierarki, grafik dan komponen interaktif |
| `ui-component-motion` | Membuat komponen interaktif dan animasi sesuai alur produk, termasuk navigasi keyboard dan tampilan minim gerak |
| `natural-writing` | Tulisan natural, membuang gaya "AI banget" |
| `academic-writing` | Skripsi/tesis/disertasi (Bab I–V), paper, proposal |
| `project-scaffolding` | Memulai proyek/repo baru dengan versi terverifikasi dan quality rails |
| `infrastructure-iac` | Terraform, Kubernetes, CI/CD, DR, dengan persetujuan manusia sebelum ke production |
| `android-compose` | Android, Kotlin, Jetpack Compose |
| `skill-security-audit` | Audit keamanan skill, plugin, dan skrip |
| `ai-video-production` | Perencanaan video AI (Dreamina/Seedance, Veo, Sora, Kling, Runway) |
| `token-efficiency` | Menghemat konteks sambil mempertahankan rujukan bukti, hasil uji, dan catatan yang diperlukan untuk melanjutkan |
| `usage-limit-recovery` | Menyimpan hasil teruji saat kuota sesi, mingguan, atau paket gratis menipis dan melanjutkan pekerjaan dari checkpoint |

Setiap skill memiliki contoh permintaan untuk menguji kapan ia aktif. Lihat [uji pemicu dan skenario perilaku](evals/trigger-tests.md).

## Cara paling gampang: zip folder, lalu upload

1. Klik kanan folder ini → **Compress to ZIP** (Windows) / **Compress** (Mac).
2. Upload zip itu langsung:
   - **Claude** (Cowork/Claude.ai): buat paket khusus dengan `python scripts/sync.py --claude`, lalu unggah `../<nama-folder>-claude.zip` melalui Plugin → Unggah plugin.
   - **Codex**: buat paket khusus dengan `python scripts/sync.py --codex`; folder ini juga berisi `.codex-plugin/plugin.json` dan `.agents/skills/`.
   - **Gemini CLI**: buat paket dengan `python scripts/sync.py --gemini`, lalu jalankan `gemini extensions install <path-folder-ini>`.
   - **GitHub Copilot** dan **OpenCode**: gunakan `--copilot` atau `--opencode` untuk membuat paket platform masing-masing.
   - **Custom GPT atau Gem khusus desain** memakai isi [skill desain](skills/web-ui-design/SKILL.md) setelah frontmatter sebagai instruksi. Lampirkan [modul desain F](skills/web-ui-design/references/part-f-web-design-deep-module.md) sebagai file pengetahuan. Untuk tugas khusus seperti audit dashboard, tambahkan hanya referensi lanjutan yang ditunjuk inti skill.
   - **Asisten lintas bidang** memakai adapter untuk platformnya dan referensi dari skill yang sedang dipakai. Spesifikasi induk dipakai saat membangun distribusi.

Setelah mengedit `deep-research-domain-council/SKILL.md`, jalankan `python scripts/sync.py` dulu sebelum membuat arsip. Skrip ini memperbarui semua salinan, versi ringkas plugin, dan manifest. Pakai `python scripts/sync.py --zip` untuk membuat arsip penuh `../<nama-folder>.zip`, atau gabungkan flag target, misalnya `python scripts/sync.py --claude --codex`. Paket target dibuat di direktori induk dengan akhiran nama platform (`../<nama-folder>-claude.zip`, dan seterusnya); isinya hanya manifest dan berkas yang diperlukan oleh platform tersebut.


## Riset dengan anggaran terbatas

Mulai dari klaim yang paling memengaruhi keputusan. Catat temuan, lokasi bukti, asal data, satuan, dan bukti yang berlawanan. Dua artikel yang mengutip survei yang sama dihitung sebagai satu asal data. Untuk riset Standard/Deep, simpan log ringkas berisi query yang berbeda secara material, alat, tanggal, bahasa, filter, jumlah hasil jika tersedia, dan sumber yang dibuka. Quick cukup memakai satu baris metode. Log ini membantu memeriksa langkah riset dan melanjutkan dari checkpoint tanpa membawa seluruh halaman ke giliran berikutnya. Untuk aplikasi chat dengan konteks kecil, tersedia adapter `INSTRUCTIONS-lite.md` dan versi API `system-prompt-lite.md`.

Saat kuota menipis, agen memprioritaskan satu hasil yang bisa dipakai. Untuk kode, agen menjalankan alur utamanya dan mencatat pemeriksaan yang lolos. Untuk riset, agen menyerahkan temuan yang sudah memiliki sumber dan menandai pertanyaan terbuka. Checkpoint berisi tujuan, hasil terverifikasi, pekerjaan tertunda, tindakan yang hasilnya belum diketahui, dan langkah berikutnya. Jika platform memutus sesi tanpa peringatan, sesi berikutnya dapat memakai checkpoint terakhir yang berhasil disimpan atau dikirim di chat. Contoh perintah lokal ada di [panduan pemulihan](skills/usage-limit-recovery/references/part-t-usage-limit-recovery.md).

## Daftar Isi

1. [Apa yang dilakukan skill ini](#apa-yang-dilakukan-skill-ini)
2. [Instalasi](#instalasi)
3. [Cara pakai](#cara-pakai)
4. [Struktur skill](#struktur-skill)
5. [Cara kerja riset (ringkas)](#cara-kerja-riset-ringkas)
6. [Delivery gates](#delivery-gates)
7. [Fakta yang mudah basi (tanda ⚠)](#fakta-yang-mudah-basi-tanda-)
8. [Riwayat versi](#riwayat-versi)
9. [Sumber utama](#sumber-utama)

---

## Apa yang dilakukan skill ini

Skill ini mengubah cara agen bekerja pada tugas riset dan teknis:

- **Riset seperti peneliti berpengalaman.** Agen memperjelas pertanyaan, menulis hipotesis sebelum mencari, menelusuri klaim sampai sumber aslinya, menghitung sumber yang benar-benar independen, sengaja mencari bukti yang membantah, dan menulis tingkat keyakinan secara jujur.
- **Mengikuti pola riset yang dipublikasikan lab AI besar:** OpenAI Deep Research, Gemini Deep Research, Claude Research (multi-agent), DeepSeek, Microsoft 365 Copilot Researcher, dan Apple Intelligence.
- **Spesialis per bidang.** Ada 14 persona peneliti (ML, software, keamanan, UX, desain, pasar, keuangan, hukum Indonesia, kesehatan, statistik, OSINT etis, penguji S3, pendidikan, energi). Masing-masing punya sumber kebenaran, metode, dan daftar jebakan sendiri.
- **Hasil yang tidak terasa buatan AI.** Desain web dan tulisan dibuat spesifik untuk produknya, natural, dan bebas klise.
- **Dicek dulu sebelum dikirim.** Setiap hasil melewati loop verifikasi: kode dijalankan, sumber dibuka ulang, angka dihitung ulang. Kegagalan dilaporkan terus terang, tidak disembunyikan.
- **Scaffolding dan infrastruktur.** Proyek baru dirancang Gemini 4 Argon dan dibangun Gemini 4 Carbon. Infrastruktur ditulis Claude Opus 5.5 lalu direview Claude Fable 5.2, dan tidak ada perubahan produksi tanpa persetujuan manusia.
- **Satu AI, semua metode deep research.** AI apa pun yang Anda pakai (ChatGPT, Gemini, Claude, Copilot, Perplexity, Grok, DeepSeek) menjalankan satu mesin terpadu yang menggabungkan cara kerja deep research semua platform itu. Cukup ketik "deep research: <pertanyaan>".
- **AI riset saling menguatkan.** ChatGPT, Gemini, Claude, Copilot, Perplexity, Grok, dan DeepSeek bisa dipakai bersama: brief yang sama, format hasil yang sama (Research Packet), lalu digabung, dicek silang, dan saling mengisi celah.
- **Hemat token.** Agen membaca bagian yang relevan, menyimpan lokasi bukti dan memakai diff. Pemeriksaan akhir tetap memakai sumber atau hasil eksekusi yang sesuai.

Skill ini **tidak** membuat model lebih pintar secara ajaib, dan tidak mewakili "isi kepala" karyawan lab mana pun. Isinya adalah kebiasaan kerja yang terdokumentasi dan bisa dicek.

---

## Instalasi

Skill ini mengikuti **Agent Skills open standard**, jadi satu `SKILL.md` bisa dipakai di banyak AI. Panduan lengkap per platform ada di [`adapters/PLATFORMS.md`](adapters/PLATFORMS.md).

### Cepat: pasang global untuk semua agen CLI

```powershell
# Windows
powershell -ExecutionPolicy Bypass -File scripts\install.ps1
```

```bash
# macOS / Linux / WSL
bash scripts/install.sh
```

Skrip menyalin skill ke `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.gemini/skills`, dan `~/.config/opencode/skills`.

### Dukungan per platform

| Platform | Cara |
|:---|:---|
| **Claude Code** | Native: `.claude/skills/` (sudah ada di repo) |
| **Claude.ai** | Buat arsip dengan `python scripts/sync.py --zip` dan gunakan arsip plugin dari direktori induk |
| **OpenAI Codex** | Skill proyek tersedia di `.agents/skills/`. Contoh pemanggilan langsung `$ui-component-motion` atau `$usage-limit-recovery` |
| **ChatGPT** | Untuk GPT atau Project khusus, gunakan inti skill pilihan dan lampirkan referensinya. Adapter lintas bidang tersedia di `adapters/chatgpt/` |
| **Perplexity** | Gunakan inti skill untuk Space khusus atau `adapters/perplexity/INSTRUCTIONS.md` untuk Space lintas bidang. Lampirkan referensi sesuai tugas bila didukung |
| **Grok** | Custom instructions: `adapters/grok/INSTRUCTIONS.md` |
| **Microsoft Copilot** | Instruksi agen/Copilot: `adapters/copilot/INSTRUCTIONS.md` |
| **Claude Projects** | Project instructions: `adapters/claude-project/INSTRUCTIONS.md` (atau pakai zip skill) |
| **Gemini CLI** | Native: `.gemini/skills/` (sudah ada di repo); cek dengan `/skills list` |
| **Gemini app** | Gunakan inti skill pilihan dan referensinya untuk Gem khusus. Adapter lintas bidang tersedia di `adapters/gemini-gem/` |
| **GitHub Copilot** | Native: `.github/skills/` + `.github/copilot-instructions.md` |
| **OpenCode** | Native: `.opencode/skills/` |
| **Cursor / Windsurf / Cline / Roo** | Rule file di `.cursor/rules/`, `.windsurf/rules/`, `.clinerules/`, `.roo/rules/` |
| **DeepSeek / API apa pun** | System prompt: `adapters/api/system-prompt.md` |

Platform native memilih skill dari nama dan deskripsinya sebelum memuat panduan. Di aplikasi chat, satu inti skill dan referensi yang diperlukan dapat dipasang langsung.

### Struktur repo

```
deepresearch-skill/
├── skills/<nama-skill>/   ← instruksi dan referensi untuk agen
├── deep-research-domain-council/SKILL.md   ← spesifikasi induk untuk pemelihara
├── CHANGELOG.md           riwayat perubahan
├── .claude/skills/…      Claude Code
├── .agents/skills/…      Codex, Gemini CLI, agen standar
├── .gemini/skills/…      Gemini CLI
├── .github/skills/…      GitHub Copilot (+ copilot-instructions.md)
├── .opencode/skills/…    OpenCode
├── .cursor/ .windsurf/ .clinerules/ .roo/   rules editor AI
├── AGENTS.md  CLAUDE.md  GEMINI.md          pointer ke skill
├── adapters/
│   ├── CORE_PROMPT.md        panduan inti untuk aplikasi chat
│   ├── PLATFORMS.md          panduan per platform
│   ├── deep-research-hub/    brief, prompt relay/cross-examine/merge, schema, merge_packets.py
│   ├── hosts/                blok khusus per AI (digabung otomatis oleh sync.py)
│   └── chatgpt/ gemini-gem/ claude-project/ copilot/ perplexity/ grok/ api/
└── scripts/  install.ps1  install.sh  sync.py  checkpoint.py
```

Inti dan daftar referensi tiap skill berada di `scripts/sync.py`. Setelah mengubah sumber, jalankan `python scripts/sync.py` untuk membangun ulang katalog, salinan skill, dan adapter. Opsi `--zip` juga membuat arsip di direktori induk.

---

## Cara pakai

Skill aktif otomatis kalau permintaan cocok dengan deskripsinya. Anda juga bisa memanggilnya langsung dengan menyebut namanya atau lewat slash command, tergantung harness.

**Contoh prompt:**

| Kebutuhan | Contoh prompt | Mode yang aktif |
|:---|:---|:---|
| Brief keputusan | "Deep research: pilih Platform A atau B untuk toko online di Indonesia 2027" | Part A, tier S/D |
| Tinjauan pustaka | "Buat SOTA review RAG untuk Bab II skripsi saya" | Part A + C2 + K12 |
| Tinjauan sistematis | "Susun protokol systematic review tentang X, batasi database dan jelaskan alur screening" | Part R6 |
| Analisis kuantitatif | "Analisis CSV ini. Cek data hilang, bandingkan conversion per cohort dan uji sensitivitas" | research-data-analysis |
| Keamanan aplikasi | "Threat-model API ini dan review otorisasi lintas tenant secara lokal" | application-security |
| Desain produk | "Desain ulang alur reservasi bengkel. Di HP pelanggan memilih jam. Di desktop petugas membandingkan antrean. Tunjukkan alasan pemilihan layout dan apa yang terjadi saat slot penuh." | F |
| Komponen dan animasi | "Buat komponen antrean bengkel. Mekanik bisa membuka detail tanpa kehilangan posisi dan tetap bisa memakai keyboard." | F8 dan F9 |
| Hemat token | "Audit kenapa sesi agen saya boros token" | Part H |
| Pemulihan kuota | "Kuota mingguan hampir habis. Selesaikan satu alur yang bisa dijalankan, uji, lalu simpan titik lanjut." | T |
| Video AI | "Buat shot list dan prompt video iklan 15 detik di Dreamina" | M2 |
| Data perusahaan | "Rangkum progres proyek X dari dokumen tim kita" | M1 |
| Asisten proaktif | "Jadi asisten bergaya Jarvis untuk riset mingguan saya" | M4 |
| Proyek baru | "Scaffold aplikasi kasir UMKM (Next.js + Postgres)" | O + N |
| Infrastruktur | "Siapkan Terraform + CI/CD untuk deploy ke GCP region Jakarta" | P + N |
| Multi-AI | "Gabungkan hasil deep research ChatGPT, Gemini, dan Claude soal X" | Q |

**Tips:** sebutkan tujuan keputusan, rentang waktu, dan format hasil. Kalau prompt Anda kurang jelas, skill akan bertanya maksimal 3 hal atau menuliskan asumsinya di bagian atas laporan.

---

## Struktur skill

| Part | Isi | Kapan dipakai |
|:---|:---|:---|
| **A — Research Cognition Core** | 10 hukum peneliti, siklus 8 tahap, tier anggaran Q/S/D/X, penelusuran sumber, ACH, claim ledger, tingkat keyakinan, rubrik, aturan berhenti, multi-agent | **Wajib** untuk semua tugas riset |
| **B — Efficiency & Deep-Thinking** | Efisiensi token/waktu/kode, protokol berpikir 4 tahap, standar kedalaman bernomor | Semua tugas |
| **C — Domain Council** | OpenCode runtime, penulisan akademik + Bab I–V, Android, full-stack, audit keamanan skill dan rujukan C3 ke F0 untuk kritik visual | Sesuai domain |
| **D — Model & Engine Routing** | Fakta OpenAI Deep Research (terverifikasi), routing effort, profil engine | Memilih model/effort |
| **E — Delivery Gates** | 15 gate kelulusan sebelum hasil dikirim | Selalu, di akhir |
| **F — Web & Design Deep Module** | Jalur Full/Patch, sistem visual, gradien dan kaca, pemilihan grafik, layout responsif per komponen, pemulihan interaksi, Canvas/WebGL dan verifikasi render | Website, alur produk, dashboard dan komponen |
| **G — Natural Writing** | Pola tulisan khas AI yang dibuang, ciri tulisan ahli, contoh sebelum/sesudah | Laporan, dokumen, copy |
| **H — Token Economy** | Rumus biaya, 10 sumber pemborosan, kebersihan konteks, prompt caching, tips per harness, audit token | Sesi agen panjang/mahal |
| **I — Templates** | `source_log`, `contradictions`, matriks ACH terisi, contoh rencana riset, kerangka laporan | Riset tier S ke atas |
| **J — Frontier Lab Playbooks** | Praktik publik OpenAI, Google Gemini, Anthropic Claude, DeepSeek, dan konsensus lintas lab | Riset mendalam |
| **K — Expert Field Council** | 14 persona spesialis plus aturan kombinasi | Pertanyaan per bidang |
| **L — Research Evaluation** | Paket evaluasi closed/live yang versioned, korpus multi-file sintetis, tugas live bilingual, locator dan rubrik tersembunyi, pemeriksaan manusia buta, biaya per hasil yang lolos | Mengecek mutu riset dan regresi skill; paket di `evals/deep-research/` |
| **M — Assistant Archetypes** | Copilot (riset data perusahaan), Dreamina (produksi video AI), Siri (privasi bertingkat), "Jarvis Mode", mode router | Sesuai jenis asisten |
| **N — Pre-Delivery Error Handling** | Loop verifikasi sebelum kirim, taksonomi 12 jenis error, checklist pra-kirim, kebijakan retry dan error tool, standar error handling per bahasa, review pendapat kedua, format laporan kegagalan | **Semua output**, sebelum dikirim |
| **O — Scaffolding** | Gemini 4 Argon (arsitek) + Gemini 4 Carbon (builder) dengan fallback, workflow 9 langkah, quality rails, kontrak `scaffold_plan.json`, uji clean clone, layout referensi, template prompt | Proyek atau repo baru |
| **P — Infrastructure** | Claude Opus 5.5 max (author) + Claude Fable 5.2 max (reviewer), 10 prinsip, workflow author/reviewer, checklist review, aturan keamanan agen, penanganan error infra, deliverable wajib | Cloud, IaC, CI/CD, Kubernetes, DR |
| **R — Unified Deep Research Engine** | Mesin 12 tahap; triage antara brief keputusan dan tinjauan formal; penyesuaian tier dengan bukti dan anggaran | **Default** untuk setiap permintaan deep research |
| **Q — Multi-AI Federation** | Roster kekuatan tiap AI riset, 4 pola kolaborasi (Split, Mirror, Relay, Cross-examine), brief universal, format Research Packet + JSON schema, protokol penggabungan berbasis asal sumber, log kalibrasi, prompt hand-off | Memakai beberapa AI riset untuk satu pertanyaan |
| **S — Custom Components and Interaction Motion** | Rujukan lama ke F8. Kontrak komponen, transisi dan perilaku saat gerak dikurangi ada di modul desain | Komponen interaktif web |
| **T — Usage Limit Recovery** | Checkpoint, klasifikasi gangguan, penyerahan hasil parsial dan langkah pemulihan | Sesi terbatas atau pekerjaan terputus |
| **V — Application Security** | Threat model web/API, kontrol ASVS, pengujian lokal, laporan temuan terverifikasi | Kode aplikasi web dan API |
| **W — Research Data Analysis** | Mutu data, penyebut, metode statistik, inferensi kausal, sintesis dan reproduksibilitas | Data kuantitatif dan sintesis riset |
| **X — Software Testing & Quality Engineering** | Pemilihan level tes, fixture deterministik, browser tests, diagnosis flakes dan pelaporan hasil | Menulis, meninjau atau men-debug tes aplikasi |

---

## Cara kerja riset (ringkas)

```
S0 Triage → S1 Brief → S2 Rencana (pohon RQ + hipotesis) → S3 Cari (luas)
→ S4 Perdalam (telusuri asal, cek, bantah) → S5 Sintesis (ACH + ledger)
→ S6 Tulis → S7 Verifikasi & kirim
        ↑____________ bisa kembali merencana ulang kapan saja ____________|
```

Rentang berikut membantu memperkirakan anggaran. Pencarian dapat berhenti ketika bukti sudah menjawab pertanyaan dan pengujian terhadap penjelasan lain selesai. Bila kuota habis lebih dulu, catat celahnya.

| Tier | Sumber dibaca | Sumber independen per klaim kunci | Contoh |
|:---|:---|:---|:---|
| Q | 1–5 | 1–2 | Satu fakta |
| S | 10–25 | ≥2 | Perbandingan, lanskap |
| D | 25–60 | ≥3 | Brief keputusan, investigasi |
| X | 60–200+ | ≥3 + log PRISMA | Tinjauan sistematis |

**Format laporan bawaan:** jawaban di depan (BLUF) → ringkasan eksekutif → analisis per pertanyaan riset → temuan kunci → keyakinan & keterbatasan → metodologi → sumber → pertanyaan lanjutan.

---

## Delivery gates

Hasil baru dikirim setelah lolos gate yang relevan:

| Gate | Fokus |
|:---|:---|
| E1 | Riset: brief, hipotesis, jumlah sumber, sitasi diperiksa, rubrik ≥4 |
| E2 | Berpikir mendalam: estimasi Fermi, keberatan, keyakinan terkalibrasi |
| E3 | Efisiensi |
| E4 | UI anti-slop |
| E5 | Penulisan akademik |
| E6 | Android |
| E7 | Keamanan |
| E8 | Konfigurasi engine/effort |
| E9 | Fakta mudah basi diberi tanggal dan dicek ulang |
| E10 | Keamanan konten (prompt injection, data pribadi, saran teregulasi, hak cipta) |
| E11 | Desain web (slop test, Core Web Vitals) |
| E12 | Tulisan natural |
| E13 | Ekonomi token |
| E14 | Spesialis & evaluasi |
| E15 | Mode asisten (izin, hak video, tangga izin Jarvis) |
| E16 | Verifikasi pra-kirim (loop Part N, checklist, kegagalan dilaporkan) |
| E17 | Scaffolding (versi terverifikasi, ADR, quality rails, uji clean clone) |
| E18 | Infrastruktur (review author/reviewer, tanpa apply prod tanpa izin, rollback, runbook, biaya) |
| E20 | Mesin terpadu (tier diumumkan, tahap R1 dijalankan, recency sweep dan mirror pass untuk tier Deep, baris metode di laporan) |
| E19 | Multi-AI (brief sama, packet dinormalisasi, sumber di-dedup per asal, klaim kunci diverifikasi sendiri) |

---

## Fakta yang mudah basi (tanda ⚠)

Harga model, nama versi, benchmark, dan fitur produk berubah tiap beberapa bulan. Di `SKILL.md`, fakta seperti ini diberi tanda **⚠** dan wajib dicek ulang ke sumber resmi sebelum dikutip. Termasuk di dalamnya:

- status akses Gemini 4 Carbon (per November 2026 masih terbatas untuk pakar keamanan siber tertentu) dan harga promo Gemini 4 Argon yang berakhir 30 November 2026;
- skor dari versi lama yang belum ditemukan sumber primernya (Consulting VRS 61.4, DeepSearchQA 44.2%, Physical Sciences 8.33%);
- fitur prompt caching per provider, nama model Seedance, dan detail Siri pasca-WWDC26.

Fakta OpenAI Deep Research yang **sudah diverifikasi**: HLE 26,6%, BrowseComp 51,5%, harga `o3-deep-research` $10/$40 dan `o4-mini-deep-research` $2/$8 per 1 juta token.

---

## Riwayat versi

### v17.28.0

Memperjelas audit sitasi setelah uji migrasi langsung memakai tautan versi dan kompatibilitas yang hanya tampil sebagai hasil pencarian/tautan terkait tanpa dibuka satu per satu. Tautan tersebut kini hanya petunjuk; klaim rilis, minimum runtime, kompatibilitas, SDK, dan distribusi perlu halaman masing-masing yang berhasil dibuka serta locator dalam ledger klaim-sumber. Rubrik evaluasi memeriksa setiap halaman versi yang dikutip. Runner juga membedakan overrun saat task terakhir selesai (run lengkap tetapi melewati anggaran) dari overrun sebelum semua task selesai (run parsial yang dapat dilanjutkan).

### v17.27.0

Menjadikan audit URL sebagai allowlist: tautan hanya boleh mendukung klaim setelah halaman berhasil dibuka pada sesi ini dan judul, publisher, isi, serta locator cocok. Snippet, halaman 403, tautan belum dibuka, dan endpoint pencarian bertopik lain harus dikeluarkan; klaim penting yang tersisa dinyatakan belum terverifikasi. Memperketat migrasi dengan baris kesiapan terpisah untuk setiap target dan status eksplisit `production feasibility: unresolved` serta `schedule: conditional` ketika akses belum terkonfirmasi.

### v17.26.0

Memperketat batas riset Quick yang selalu ikut dimuat: maksimal empat panggilan web, kueri sempit, satu sumber yang dibuka, lalu satu fallback first-party hanya jika terblokir atau tidak cocok. Kueri/snippet dan tautan yang tidak relevan dinyatakan bukan bukti. Skill riset kini juga aktif untuk pemeriksaan fakta terkini/berisiko tinggi tanpa mendorong pencarian luas. Memaksa matriks kesiapan per target migrasi yang mencatat runtime, SDK/host build dan CI, signing/distribusi, akses tim, status bukti, serta POC sebelum menyebut rute produksi siap.

### v17.25.0

Menambahkan audit wajib dari klaim ke sumber: setiap kutipan penting/volatile harus membuka publisher dan locator yang benar-benar mendukung klaim; tautan yang tidak relevan atau snippet pencarian tidak boleh dipakai sebagai bukti. Menambahkan batas awal aksi per tier riset serta checkpoint sebelum perluasan ketika host tidak bisa membatasi token. Memperkuat migrasi platform dengan gerbang kelayakan build/rilis per target yang memeriksa OS runtime, kematangan core/UI, SDK/toolchain, host build/CI, signing, distribusi, dan akses tim; akses Apple yang belum tersedia menahan keputusan kelayakan sampai POC target lolos.

### v17.24.0

Memperdalam batas kepercayaan untuk konten riset yang membawa instruksi tersembunyi: pisahkan instruksi dari fakta yang masih dapat dipakai, pertahankan kriteria user dan izin tool, verifikasi klaim penting, serta catat locator tanpa menyalin payload. Part L kini meminta evaluasi berpasangan clean/attacked, kontrol negatif berisi kutipan instruksi yang aman, dan penilaian jawaban serta jejak tool secara terpisah. Menambahkan dua kasus regresi Bahasa Indonesia dan memperluas suite menjadi 19 task.

### v17.23.0

Menambahkan kontrol kontaminasi evaluasi riset mendalam. Run paket tertutup wajib menonaktifkan retrieval eksternal dan hanya memberi agen prompt serta paket yang diizinkan; run live mencatat kebocoran artefak benchmark secara terpisah dari sumber primer yang memang menjawab pertanyaan. Menambahkan pencatatan integritas pada template run dan pemeriksa struktur untuk ID tugas, prompt, serta batas paket.

### v17.22.0

Menambahkan gerbang delegasi multi-agen: delegasikan hanya jalur bukti yang independen atau kebutuhan cakupan yang jelas, verifikasi kemampuan host sebelum memilihnya, lalu gabungkan berdasarkan asal sumber dan bukti unik, bukan suara mayoritas. Menambahkan pencatatan biaya agregat dan protokol evaluasi berpasangan single-agent vs dua worker pada CP-EN-14. Panduan efisiensi token kini menghitung biaya koordinator, worker, retry, sintesis, dan verifikasi.

### v17.21.0

Memperdalam pemeriksaan terhadap gema sumber terkoordinasi: telusuri rantai sitasi dan asal data lintas penerbit, bedakan banyaknya publikasi dari independensi bukti, dan hitung asal yang sama satu kali. Menambahkan perbandingan efisiensi berpasangan yang hanya menerima penghematan token jika akurasi, sitasi, dan cakupan tetap lolos. Menambahkan paket evaluasi *multi-site bait* dan evaluasi live migrasi Android ke iOS/macOS/web berbasis dokumentasi resmi, termasuk pemeriksaan kematangan framework tiap target, stable vs RC, dan kompatibilitas.

### v17.20.0

Menambahkan pelacakan asal kriteria keputusan untuk melindungi riset dari *agenda seeding* dan perubahan kriteria terselubung. Tujuan dan syarat wajib dari user dicatat sebelum pencarian; metrik usulan sumber harus diverifikasi otoritas, asal, insentif, dan adopsi independennya sebelum memengaruhi rekomendasi. Menambahkan kasus regresi tertutup dengan metrik peringkat bersponsor yang belum terverifikasi.

### v17.19.0

Menambahkan gerbang scope untuk prompt riset yang terlalu umum dan validasi web terarah: ajukan hanya pertanyaan yang mengubah arah keputusan, atau pakai asumsi terbatas; cari hanya klaim yang memang perlu bukti eksternal terkini; pilih jalur sumber yang relevan; gunakan anggaran bertahap dan berhenti saat pencarian tambahan tidak mengubah jawaban. Menghapus target jumlah sumber dan default menjalankan semua tahap yang dapat mendorong pencarian berlebihan. Menambahkan kasus regresi triase prompt dan rubrik efisiensi untuk tugas web.

### v17.18.0

Menambahkan protokol bukti multimodal untuk locator visual, verifikasi bacaan OCR/grafik, pelacakan dependensi klaim, dan pelaporan tautan bukti yang belum selesai. Evaluasi deep research kini menilai kesesuaian visual-teks dan kebenaran klaim perantara secara terpisah, dengan satu kasus keputusan berbasis grafik sintetis; kasus ini belum dijalankan.

### v17.17.0

Memperjelas gerbang migrasi yang dapat diukur: penyelesaian tugas dan kesinambungan sesi, perilaku API, state tersimpan, invarians data, ambang penghentian per fase, pemilik keputusan, dan tindakan pemulihan. Menambahkan dua paket kasus sintetis untuk migrasi web→Android dan Android→web/desktop; paket ini belum dijalankan sebagai evaluasi.

### v17.16.0

Memperdalam migrasi lintas platform dengan audit repo dan dependensi, pemilik data dan identitas, kompatibilitas API/schema, estimasi berbasis bukti, tabel sumber kebenaran per fase, serta rollback setelah data baru masuk. Panduan juga membedakan kapan migrasi bertahap membantu dan kapan justru tidak cocok.

### v17.15.0

Menambahkan `platform-migration` untuk memeriksa kondisi sistem yang ada, membuat matriks kemampuan per platform, membandingkan jalur migrasi dengan bukti dokumentasi resmi, menguji risiko melalui proof-of-concept kecil, dan menyusun rollout serta rollback. Deep research kini merutekan pertanyaan migrasi ke panduan ini; scaffolding dibedakan dari perpindahan platform.

### v17.14.0

Menambahkan batas anggaran dan checkpoint yang bisa dilanjutkan pada evaluasi riset: simpan hasil setiap tugas, berhenti sebelum panggilan berikutnya melampaui anggaran, lanjutkan dari tugas yang belum selesai, dan laporkan run parsial tanpa menyebutnya pass rate satu paket penuh. Mencatat dua kasus Codex CLI yang sudah dievaluasi sebagai checkpoint, bukan baseline lengkap.

### v17.13.0

Menambahkan log pencarian ringkas untuk riset Standard/Deep dan permintaan yang perlu direproduksi; Quick tetap ringan. Paket evaluasi kini memiliki 10 tugas, termasuk audit tinjauan sistematis dengan duplikasi, full text yang belum tersedia, dan batas sintesis.

### v17.12.0

Menambahkan pemulihan sumber resmi yang terblokir, evaluasi sumber resmi yang mengukur hal berbeda, dan kelanjutan riset dari checkpoint. Efisiensi token diukur bersama klaim penting yang lolos verifikasi.

### v17.11.0

Menambahkan `software-testing` untuk strategi dan pemeliharaan tes lintas stack, dengan fokus pada perilaku pengguna, isolasi, triase flakes, dan pelaporan hasil tanpa menjalankan tes di luar izin tugas.

### v17.10.0

Menambahkan paket evaluasi deep research yang dapat dijalankan manual: empat kasus closed-packet sintetis dan dua tugas live-search bilingual, peta bukti, acceptance criteria tersembunyi, serta template catatan run.

### v17.9.0

Memperdalam evaluasi deep research: paket closed/live yang dapat diulang, metadata run, kasus multi-file dengan distractor, pemeriksaan sitasi per locator, metrik dengan denominator jelas, gerbang error kritis, validasi manusia buta, dan biaya per hasil berkualitas.

### v17.8.0

Mengganti probabilitas dan likelihood ratio generik berbasis jumlah sumber dengan label keyakinan beralasan. Kerja multi-AI menjadi pemeriksaan independen, bukan kenaikan skor otomatis.

### v17.7.0

Menambahkan skill keamanan aplikasi dan analisis data riset. Deep research kini memisahkan riset keputusan dari tinjauan sistematis, menyediakan gerbang protokol formal, serta menilai retrieval dan mutu laporan lewat dimensi yang dapat diperiksa.

### v17.6.0

Semua skill membawa aturan hemat token bersama. Agen membuka hanya referensi yang dibutuhkan, merangkum bukti dan keputusan, serta tetap menjalankan riset dan pemeriksaan wajib.

### v17.5.0

Modul F menyatukan aturan visual, komponen dan gerak. Jalur Full dimulai dari riset dan tiga sketsa, sedangkan Patch dimulai dari perilaku yang rusak dan diakhiri dengan verifikasi render. Lihat [riwayat rilis](CHANGELOG.md).

### v17.4.0

Pilih panduan lanjutan sesuai keputusan yang sedang dikerjakan.

- [Tipografi, grid, dan tema](skills/web-ui-design/references/part-u1-reading-rhythm-grids-and-theme-contrast.md) mencakup dua studi panjang baris, latihan hierarki satu font, perhitungan grid, dan contoh kontras yang gagal jika dibulatkan.
- [Hierarki dan riset pengguna](skills/web-ui-design/references/part-u2-visual-hierarchy-and-task-research.md) memandu latihan dari referensi, uji ingatan tiga detik dan pengamatan penyelesaian tugas.
- [Dashboard dan state komponen](skills/web-ui-design/references/part-u3-dashboard-judgments-and-component-states.md) membahas pemilihan grafik, total parsial, serta perilaku tombol dan formulir ketika data lambat, kosong atau gagal.

### v17.3.0

Skill desain kini memandu pembuatan moodboard beranotasi, tiga wireframe hitam-putih, dan revisi berdasarkan alur yang diuji. Ada contoh skala huruf, grid asimetris, pemilihan foto, microcopy Indonesia, dan perilaku komponen saat data kosong atau gagal disimpan. [Panduan desain produk](skills/web-ui-design/references/part-f-web-design-deep-module.md)

### v17.2.0

Dua skill baru menangani komponen UI beserta animasinya dan pemulihan saat kuota habis. Panduan riset kini memeriksa asal data yang sama, perbedaan penyebut, dan apakah kesimpulan berubah saat sumber yang disengketakan dikeluarkan. Panduan token menyimpan lokasi bukti selama pemadatan konteks.

### v17.1.0 — Perbaikan dari uji langsung
- Uji pemicu: 24/24 benar di Haiku dan Sonnet (lihat `evals/trigger-tests.md`).
- Pertanyaan yang terikat tanggal ("per November 2026", "terbaru") selalu dicek perubahan terbaru, termasuk di tier Quick.
- Hanya sumber yang benar-benar dibuka yang dihitung; aturan format sitasi; template laporan tier Quick.
- `natural-writing`: aturan caption media sosial dan contoh sebelum/sesudah.
- Setiap skill menunjukkan di skill mana Part lain berada.

### v17.0.0 — Dipecah jadi 10 skill fokus
- Deskripsi sempit per skill ("Use when … Not for …") supaya tidak salah aktif.
- Inti per skill ±650–1.300 token; detail di `references/`.
- Nama model diganti kelas model di inti; daftar nama terverifikasi dengan sumber di Part D4.
- `sync.py` membangun ke-10 skill dari satu sumber; `install.ps1`/`install.sh` memasang semuanya dan menghapus skill lama.
- `evals/trigger-tests.md` untuk menguji pemicu.

### v16.0.0 — Mesin deep research terpadu (satu AI, semua metode)
- **Part R:** AI yang sedang dipakai menjalankan 12 tahap gabungan: klarifikasi dan rewrite brief (OpenAI), rencana yang bisa diedit (Gemini), sapuan cepat (Perplexity), jalur paralel (Claude), perburuan fakta sulit (OpenAI), verifikasi di dalam loop (DeepSeek), sapuan berita terbaru (Grok), sapuan data internal (Copilot), mirror pass, review mata segar, penyimpanan state, dan laporan bersitasi.
- Jalur tanpa sub-agent untuk aplikasi chat, adapter per host, dan frasa aktivasi "deep research: …".
- Instruksi khusus per AI: ChatGPT, Gemini, Claude Projects, Copilot, Perplexity, Grok, DeepSeek/API (semuanya < 8.000 karakter).
- `sync.py` kini menggabungkan `adapters/hosts/*.md` dengan `CORE_PROMPT.md` secara otomatis.
- Gate **E20**.

### v15.0.0 — Kolaborasi multi-AI deep research
- **Part Q:** federasi AI riset. Isinya roster kekuatan dan kelemahan tiap platform, pola Split / Mirror / Relay / Cross-examine, brief universal, format Research Packet, protokol penggabungan yang menghitung asal sumber (bukan URL), log kalibrasi, dan prompt hand-off.
- Folder baru `adapters/deep-research-hub/`: `BRIEF_TEMPLATE.md`, `RELAY_PROMPT.md`, `CROSS_EXAMINE_PROMPT.md`, `MERGE_PROMPT.md`, `research_packet.schema.json`, `merge_packets.py`.
- `CORE_PROMPT.md` v15 dengan bagian kerja sama antar-AI.
- Gate **E19**.

### v14.0.0 — Error handling, scaffolding, infrastruktur
- **Part N:** penanganan error sebelum hasil dikirim. Isinya loop verifikasi (maksimal 3 putaran perbaikan), taksonomi error, checklist pra-kirim untuk riset/kode/file/aksi, kebijakan retry, standar error handling per bahasa (TS, Python, Kotlin, Rust, Go, HTTP RFC 9457, UI), review pendapat kedua, dan format laporan DONE / NOT DONE / UNVERIFIED / NEXT.
- **Part O:** scaffolding dengan Gemini 4 Argon sebagai arsitek dan Gemini 4 Carbon sebagai builder, plus fallback karena Carbon belum dibuka untuk umum.
- **Part P:** infrastruktur dengan Claude Opus 5.5 max sebagai author dan Claude Fable 5.2 max sebagai reviewer, disertai disiplin biaya effort max.
- Tabel engine D3 diverifikasi ulang (ID model, harga, status akses).
- `CORE_PROMPT.md` v14 dan `sync.py` v2, yang kini juga membuat ulang file rules dan pointer serta memverifikasi zip.
- Gate **E16–E18**.

### v13.1.0 — Dukungan lintas platform
- Adapter untuk Claude.ai (zip), Codex, Gemini CLI, Copilot, ChatGPT (Custom GPT/Projects), Gemini app (Gem), Cursor, Windsurf, Cline, Roo, dan API (DeepSeek dkk.).
- Versi ringkas `CORE_PROMPT.md` untuk platform berbasis instruksi tetap.
- Skrip `install.ps1`, `install.sh`, dan `sync.py`.

### v13.0.0 — Mode asisten
- **Part M:** Microsoft 365 Copilot Researcher/Analyst (riset data perusahaan sesuai izin), Dreamina (riset dan produksi video AI: shot list, anatomi prompt, log prompt, hak dan etika), Apple Siri (routing privasi bertingkat, aksi lewat tool yang dideklarasikan), "Jarvis Mode" (asisten proaktif dengan tangga izin dan format briefing), serta mode router.
- Gate **E15**.

### v12.0.0 — Playbook lab dan spesialis
- **Part J:** praktik riset yang dipublikasikan OpenAI, Google Gemini, Anthropic Claude, dan DeepSeek, plus 7 prinsip konsensus lintas lab.
- **Part K:** 14 persona spesialis bidang.
- **Part L:** evaluasi kualitas riset (rubrik, golden questions, taksonomi kegagalan).
- Gate **E14**.

### v11.0.0 — Desain, tulisan, token
- **Part F:** modul desain web mendalam (token OKLCH, layout, komponen, aksesibilitas, Core Web Vitals, kritik desain).
- **Part G:** tulisan natural anti-AI-slop.
- **Part H:** ekonomi token lintas harness.
- **Part I:** template dan contoh terisi.
- Gate **E11–E13**.

### v10.0.0 — Inti riset dibangun ulang
- Salinan file yang rusak dan terduplikasi dibuang.
- Batas tetap "≤3 hop" diganti tier anggaran adaptif Q/S/D/X.
- Ditambahkan **Research Cognition Core**: 10 hukum peneliti, siklus 8 tahap, penelusuran asal sumber, lateral reading, citation chasing, pencarian pembantah, ACH, claim ledger, aturan berhenti saat jenuh, rubrik penilaian mandiri, orkestrasi multi-agent, playbook per domain.
- Skor Bayesian dibuat jujur: hanya untuk bukti independen, tanpa presisi palsu.
- Perbaikan teknis: HKDF memakai salt acak; angka latensi cache dikoreksi.
- Fakta yang tidak terverifikasi diberi tanda ⚠.

### v9.0.0 — OpenAI Deep Research Engine
- §10 OpenAI Deep Research Engine: loop browse → interpret → synthesize → pivot, format sitasi `〖source_id†Lstart-Lend〗`, laporan 6 bagian, kerangka keamanan, protokol aktivasi, tabel routing.
- Gate §8.8 (Deep Research) dan §8.9 (Cross-Engine Routing); Final Directive menjadi "nine gates" dengan prinsip "cite, don't claim".
- Perbaikan format: code block yang tidak tertutup, rumus LaTeX yang pecah, tabel rusak, dan bagian akhir file yang terpotong direkonstruksi.

### v8.0.0–v8.1 — Frontier Cognitive Engine
- §9 profil tiga engine (Engine-F, Engine-C, Engine-O), matriks pemilihan effort, protokol aktivasi, tangga effort lintas provider, dan formula pemilihan berbasis biaya.
- Gate §8.7 Cognitive Engine: deklarasi effort, larangan `max` untuk tugas pendek ($T_\infty$ < 5 menit), pengakuan biaya.
- Prinsip baru "calibrate effort, don't brute-force".
- ⚠ Angka harga dan skor engine di versi ini belum diverifikasi ulang; lihat bagian [Fakta yang mudah basi](#fakta-yang-mudah-basi-tanda-).

### v7.1.0 — Fondasi
- Efficiency Triad v2, Deep-Thinking Protocol, Professional Design Reference Layer, Anti-Slop R-01..R-40, Android 15-skill, full-stack, dan Security Auditor.

---

## Sumber utama

- OpenAI — [Introducing deep research](https://openai.com/index/introducing-deep-research/), [BrowseComp](https://openai.com/index/browsecomp/), [Deep Research API Agents Cookbook](https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api_agents)
- Google — [Gemini Deep Research](https://gemini.google/overview/deep-research/)
- Anthropic — [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- DeepSeek — [DeepSeek-V3.2 technical report](https://arxiv.org/abs/2512.02556), [Web Tools API](https://api-docs.deepseek.com/guides/web_tools.md)
- Microsoft — [Researcher agent](https://learn.microsoft.com/copilot/microsoft-365/researcher-agent)
- Apple — [Apple Intelligence](https://www.apple.com/apple-intelligence/)
- Dreamina — [dreamina.capcut.com](https://dreamina.capcut.com/llms.txt)
- Upstream skills — `miqdadbadjuber/anti-slop`, `jin-s13/ai-research-writing-skill`, `dabit3/skill-audit`, `javiercamarenatriguero/android-skills`, [opencode.ai/docs](https://opencode.ai/docs)

---

## Lisensi

MIT. Silakan pakai, ubah, dan bagikan dengan tetap mencantumkan atribusi.
