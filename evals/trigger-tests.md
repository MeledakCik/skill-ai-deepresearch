# Trigger tests

Use these to check that the right skill activates (and that none activates when it should not).
Run each prompt in a fresh chat and note which skill loaded. Target: >= 9 of 10 correct per skill.

| Prompt | Expected skill |
|:---|:---|
| deep research: dampak QRIS terhadap UMKM di Jawa Barat 2024-2026 | deep-research-council |
| Tolong cek apakah klaim "ekspor nikel naik 40%" itu benar, kasih sumber | deep-research-council |
| Bandingkan 3 platform toko online untuk UMKM, mana yang paling murah biaya transaksinya | deep-research-council |
| Buatkan landing page aplikasi kasir yang tidak kelihatan seperti template AI | web-ui-design |
| Perbaiki kontras dan aksesibilitas halaman login ini | web-ui-design |
| Tulis ulang email ini supaya tidak terdengar seperti ChatGPT | natural-writing |
| Rapikan caption Instagram ini biar natural | natural-writing |
| Bantu susun Bab II skripsi tentang sistem rekomendasi | academic-writing |
| Review metodologi tesis saya, cari kelemahannya seperti penguji | academic-writing |
| Buat project baru Next.js + Postgres lengkap dengan CI | project-scaffolding |
| Siapkan Terraform untuk deploy ke GCP region Jakarta | infrastructure-iac |
| Review plan Terraform ini sebelum apply ke production | infrastructure-iac |
| Refactor layar Compose ini ke MVI | android-compose |
| Audit plugin ini, aman tidak untuk diinstal? | skill-security-audit |
| Buat shot list video iklan 15 detik untuk Dreamina | ai-video-production |
| Kenapa sesi Claude Code saya boros token? | token-efficiency |

## Should NOT trigger any skill

| Prompt | Why |
|:---|:---|
| Ibu kota Prancis apa? | Simple fact |
| Terjemahkan "selamat pagi" ke bahasa Inggris | Translation |
| Fix typo di fungsi ini | Small code edit |
| Hai, apa kabar? | Chat |

## Results log

| Date | Version | Tester | Score | Notes |
|:---|:---|:---|:---|:---|
| 2026-11-19 | 17.0.0 | Claude Haiku (routing only, all real skills visible incl. built-ins) | 24/24 | 16 expected skills, 4 "none", 4 extra prompts routed sensibly (investor market report -> deep-research-council; slides -> pptx) |
| 2026-11-19 | 17.0.0 | Claude Sonnet (same) | 24/24 | Same choices as Haiku |

Quality runs (2026-11-19, Sonnet): natural-writing caption rewrite passed (no invented facts, assumption flagged); deep-research-council Quick tier on "tarif PPN per November 2026" passed with 3 opened sources (2 T1), gaps reported. Gaps found in the skill text were fixed in 17.1.0.
